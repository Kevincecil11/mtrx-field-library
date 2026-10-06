#!/usr/bin/env python3
"""MTRX spaced-review bot for Telegram. Runs in GitHub Actions, stdlib only.

  python3 bot/bot.py             normal run: read Telegram updates, grade answers, send what's due
  python3 bot/bot.py --selftest  check the token, register commands, send a test quiz,
                                 write bot/selftest.json (no secrets in it)

Secrets (GitHub Actions): TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID. Only that chat is served.
State lives in bot/state.json (committed by the workflow). Banks: bot/questions/NN.json
(built from the guides by tools/build_questions.py). Design: docs/ARCHITECTURE.md.
"""
import base64, datetime as dt, glob, html, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_PATH = os.path.join(ROOT, 'bot', 'state.json')
QDIR = os.path.join(ROOT, 'bot', 'questions')
SELFTEST_PATH = os.path.join(ROOT, 'bot', 'selftest.json')
LADDER = [1, 3, 7, 21, 60, 180]          # days after the stop was finished (or last missed)
CAP = 15                                 # max questions per daily review
IST = dt.timezone(dt.timedelta(hours=5, minutes=30))
BOT_USERNAME = 'makingmesmart_bot'
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '').strip()
CHAT = os.environ.get('TELEGRAM_CHAT_ID', '').strip()
_owner, _repo = os.environ.get('GITHUB_REPOSITORY', 'Kevincecil11/mtrx-field-library').split('/')
SITE = os.environ.get('SITE_URL', 'https://%s.github.io/%s' % (_owner.lower(), _repo)).rstrip('/')
COMMANDS = [
    ('today', "Send today's review now"),
    ('status', 'Progress and what is due'),
    ('weak', 'Your weak spots'),
    ('done', 'Mark stops done, e.g. /done 01 1.1-1.6'),
    ('undo', 'Unmark a stop, e.g. /undo 01 1.3'),
    ('pause', 'Pause the daily review'),
    ('resume', 'Resume the daily review'),
    ('time', 'Set the reminder hour (IST), e.g. /time 7'),
    ('help', 'How this works'),
]

# ---------------------------------------------------------------- basics

def now():
    fake = os.environ.get('MTRX_NOW')   # tests only, e.g. 2026-10-09T08:10
    return dt.datetime.fromisoformat(fake).replace(tzinfo=IST) if fake else dt.datetime.now(IST)

def today():
    return now().date()

def d2s(d):
    return d.isoformat()

def s2d(s):
    return dt.date.fromisoformat(s)

def nice(d):
    return d.strftime('%a %-d %b')

def esc(s):
    return html.escape(str(s), quote=False)

def api(method, **params):
    """Call the Telegram Bot API. Tests replace this function."""
    url = 'https://api.telegram.org/bot%s/%s' % (TOKEN, method)
    data = json.dumps(params).encode()
    for attempt in range(4):
        req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                body = json.load(r)
        except urllib.error.HTTPError as e:
            body = json.load(e)
        if body.get('ok'):
            return body['result']
        retry = (body.get('parameters') or {}).get('retry_after')
        if retry and attempt < 3:
            time.sleep(min(int(retry), 30) + 1)
            continue
        raise RuntimeError('%s failed: %s' % (method, body.get('description')))

def load_state():
    try:
        st = json.load(open(STATE_PATH, encoding='utf-8'))
    except (OSError, ValueError):
        st = {}
    base = {'v': 1, 'offset': 0, 'hour': 8, 'paused': False, 'last_push': None, 'done': {}, 'cards': {},
            'polls': {}, 'today': None, 'log': []}
    for k, v in base.items():
        st.setdefault(k, v)
    return st

def save_state(st):
    st['log'] = st['log'][-40:]
    with open(STATE_PATH, 'w', encoding='utf-8') as f:
        json.dump(st, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write('\n')

def load_banks():
    banks = {}
    for p in sorted(glob.glob(os.path.join(QDIR, '[0-9][0-9].json'))):
        b = json.load(open(p, encoding='utf-8'))
        b['by_id'] = {c['id']: c for c in b['cards']}
        banks[b['guide']] = b
    return banks

def log(st, msg):
    st['log'].append('%s %s' % (now().strftime('%Y-%m-%d %H:%M'), msg))

def stop_word(bank):
    return 'Day' if bank.get('day') else 'Stop'

def link(c):
    return '%s/%s' % (SITE, c['link'])

# ---------------------------------------------------------------- progress

def decode_progress(code, banks):
    """'p01_<base64url bitmask>' -> (guide, [stops]). Bit i = i-th stop in document order."""
    m = re.fullmatch(r'p(\d\d)_([A-Za-z0-9_-]*)', code or '')
    if not m or m.group(1) not in banks:
        return None, []
    g, raw = m.group(1), m.group(2)
    bits = base64.urlsafe_b64decode(raw + '=' * (-len(raw) % 4)) if raw else b''
    stops = banks[g]['stops']
    return g, [s for i, s in enumerate(stops) if i // 8 < len(bits) and bits[i // 8] >> (i % 8) & 1]

def expand(spec, stops):
    """'1.1-1.6,2.3' or '1-7' -> stops that exist in the guide, in guide order."""
    want = set()
    for part in re.split(r'[,\s]+', spec.strip()):
        if not part:
            continue
        if '-' in part:
            a, b = part.split('-', 1)
            if a in stops and b in stops:
                i, j = stops.index(a), stops.index(b)
                want.update(stops[min(i, j):max(i, j) + 1])
        elif part in stops:
            want.add(part)
    return [s for s in stops if s in want]

def mark_done(st, banks, g, stops, day):
    new = []
    for s in stops:
        if s not in st['done'].setdefault(g, {}):
            st['done'][g][s] = d2s(day)
            new.append(s)
    sync_cards(st, banks)
    return new

def sync_cards(st, banks):
    """Every finished stop gets a schedule for each of its cards (also picks up cards added later)."""
    for g, stops in st['done'].items():
        if g not in banks:
            continue
        for c in banks[g]['cards']:
            if c['stop'] in stops and c['id'] not in st['cards']:
                anchor = s2d(stops[c['stop']])
                due = anchor + dt.timedelta(days=LADDER[0])
                st['cards'][c['id']] = {'g': g, 'k': 0, 'anchor': d2s(anchor), 'due': d2s(due), 'miss': 0, 'right': 0, 'seen': 0, 'sent': None}

def grade(st, cid, result):
    """result: 'got' | 'partly' | 'miss'"""
    c, t = st['cards'][cid], today()
    c['seen'] += 1
    c['last'] = d2s(t)
    if result == 'got':
        c['right'] += 1
        c['k'] += 1
        if c['k'] >= len(LADDER):
            c['due'] = d2s(t + dt.timedelta(days=365))      # mastered: one check a year
        else:
            c['due'] = d2s(max(s2d(c['anchor']) + dt.timedelta(days=LADDER[c['k']]), t + dt.timedelta(days=1)))
    elif result == 'partly':
        k = min(c['k'], len(LADDER) - 1)
        gap = LADDER[k] - (LADDER[k - 1] if k else 0)
        c['due'] = d2s(t + dt.timedelta(days=max(1, gap // 2)))
    else:
        c.update(k=0, anchor=d2s(t), due=d2s(t + dt.timedelta(days=1)))
        c['miss'] += 1

def is_weak(c):
    return c['miss'] > 0 and c['k'] < 2

# ---------------------------------------------------------------- sending

def due_cards(st, banks, include_sent=False):
    t = d2s(today())
    out = [(cid, c) for cid, c in st['cards'].items()
           if c['due'] <= t and c['g'] in banks and cid in banks[c['g']]['by_id']
           and (include_sent or c.get('sent') != t)]
    out.sort(key=lambda x: (-x[1]['miss'], x[1]['due'], x[0]))
    lanes = {}
    for cid, c in out:
        lanes.setdefault(c['g'], []).append(cid)
    mixed = []
    while any(lanes.values()):                   # interleave guides
        for g in sorted(lanes):
            if lanes[g]:
                mixed.append(lanes[g].pop(0))
    return mixed

def send_text(text, **kw):
    return api('sendMessage', chat_id=CHAT, text=text, parse_mode='HTML',
               link_preview_options={'is_disabled': True}, **kw)

def send_card(st, banks, cid, test=False):
    c = st['cards'].get(cid, {})
    card = banks[cid[:2]]['by_id'][cid]
    bank = banks[card['guide']]
    tag = 'No. %s \u00b7 %s %s' % (card['guide'], stop_word(bank), card['stop'])
    if card['type'] == 'quiz':
        opts = card['options']
        q = '%s\n%s' % (tag, card['q'])
        why = card.get('why') or 'Re-read the stop for the reasoning.'
        fits = len(q) <= 300 and 2 <= len(opts) <= 10 and all(len(o) <= 100 for o in opts)
        if not fits:
            letters = 'ABCDEFGHIJ'[:len(opts)]
            send_text('<b>%s</b>\n%s\n\n%s' % (esc(tag), esc(card['q']),
                      '\n'.join('<b>%s)</b> %s' % (l, esc(o)) for l, o in zip(letters, opts))))
            q, opts = 'Your answer?', list(letters)
        msg = api('sendPoll', chat_id=CHAT, question=q, options=[{'text': o} for o in opts], type='quiz',
                  correct_option_id=card['answer'], is_anonymous=False,
                  explanation=why if len(why) <= 200 else why[:196].rsplit(' ', 1)[0] + ' ...')
        kind = 'quiz'
    else:
        label = card.get('label') or 'Recall'
        send_text('<b>%s \u00b7 %s</b>\n%s\n\nAnswer it in your head (or out loud) first, then tap to reveal:\n<tg-spoiler>%s</tg-spoiler>'
                  % (esc(tag), esc(label), esc(card['q']), esc(card['answer'])))
        msg = api('sendPoll', chat_id=CHAT, question='How did you do? (%s)' % tag,
                  options=[{'text': 'Got it'}, {'text': 'Partly'}, {'text': 'Missed it'}], is_anonymous=False)
        kind = 'recall'
    st['polls'][msg['poll']['id']] = {'card': cid, 'kind': 'test' if test else kind, 'sent': d2s(today())}
    if c:
        c['sent'] = d2s(today())
    time.sleep(0.4 if TOKEN else 0)

def push(st, banks, force=False):
    t = today()
    if not force:
        if st['paused'] or st['last_push'] == d2s(t) or now().hour < int(st['hour']):
            return
    st['last_push'] = d2s(t)
    queue = due_cards(st, banks)[:CAP]
    if not queue:
        if force:
            nxt = next_review(st)
            send_text('Nothing due today. ' + ('Next review: <b>%s</b> (%d questions).' % (nice(nxt[0]), nxt[1]) if nxt else
                      'Finish a stop and tap "Send progress" in the guide to start its review clock.'))
        return
    per = {}
    for cid in queue:
        per[cid[:2]] = per.get(cid[:2], 0) + 1
    mins = max(2, round(len(queue) * 0.4))
    send_text('\u2600\ufe0f <b>Review \u00b7 %s</b>\n%d questions \u00b7 about %d min\n%s\n\nRight answers push a topic further out. Misses come back tomorrow.'
              % (nice(t), len(queue), mins, ' \u00b7 '.join('No. %s \u00d7%d' % (g, n) for g, n in sorted(per.items()))))
    st['today'] = {'date': d2s(t), 'total': len(queue), 'got': 0, 'partly': 0, 'miss': 0, 'summary_sent': False}
    for cid in queue:
        send_card(st, banks, cid)
    log(st, 'pushed %d cards' % len(queue))

def next_review(st):
    t = d2s(today())
    future = sorted(c['due'] for c in st['cards'].values() if c['due'] > t)
    if not future:
        return None
    return s2d(future[0]), sum(1 for d in future if d == future[0])

# ---------------------------------------------------------------- incoming

def handle_answer(st, banks, pa, misses):
    p = st['polls'].pop(pa.get('poll_id'), None)
    if not p or not pa.get('option_ids'):
        return
    choice = pa['option_ids'][0]
    if p['kind'] == 'test':
        send_text('\u2705 Test answer received. The full loop works: send, answer, grade.')
        return
    cid = p['card']
    card = banks.get(cid[:2], {}).get('by_id', {}).get(cid)
    if cid not in st['cards'] or not card:
        return
    if p['kind'] == 'quiz':
        result = 'got' if choice == card['answer'] else 'miss'
    else:
        result = ['got', 'partly', 'miss'][min(choice, 2)]
    grade(st, cid, result)
    td = st.get('today') or {}
    if td.get('date') == p['sent']:
        td[result] = td.get(result, 0) + 1
    if result == 'miss':
        misses.append(card)

def after_answers(st, misses):
    if misses:
        lines = ['\U0001f501 <b>To revisit</b> (back tomorrow):']
        for c in misses:
            extra = (' ' + esc(c['why'])) if c['type'] == 'quiz' and len(c.get('why', '')) > 200 else ''
            lines.append('\u2022 No. %s \u00b7 %s %s: %s%s\n  <a href="%s">Re-read it</a>' % (c['guide'], 'Day' if c['link'].find('#d') > 0 else 'Stop', c['stop'], esc(c['name']), extra, link(c)))
        send_text('\n'.join(lines))
    td = st.get('today') or {}
    if td and not td.get('summary_sent'):
        open_today = [p for p in st['polls'].values() if p['sent'] == td['date'] and p['kind'] != 'test']
        answered = td.get('got', 0) + td.get('partly', 0) + td.get('miss', 0)
        if answered and not open_today:
            nxt = next_review(st)
            send_text('\u2705 <b>Done for today</b>: %d right, %d partly, %d to revisit, out of %d.%s'
                      % (td.get('got', 0), td.get('partly', 0), td.get('miss', 0), td['total'],
                         ('\nNext review: <b>%s</b>.' % nice(nxt[0])) if nxt else ''))
            td['summary_sent'] = True

def handle_text(st, banks, text, msg_day):
    text = (text or '').strip()
    cmd, _, arg = text.partition(' ')
    cmd = cmd.split('@')[0].lower()
    arg = arg.strip()
    if cmd == '/start':
        if arg.startswith('p'):
            g, stops = decode_progress(arg, banks)
            if not g:
                return send_text("That progress code didn't match a guide in the library. Try tapping Send progress again.")
            new = mark_done(st, banks, g, stops, msg_day)
            return reply_progress(st, banks, g, new, len(stops), msg_day)
        return send_text(HELP_INTRO + help_text())
    if cmd == '/done':
        g, _, spec = arg.partition(' ')
        g = g.zfill(2)
        if g not in banks or not spec:
            return send_text('Use it like this: <code>/done 01 1.1-1.6</code> or <code>/done 02 1-7</code>.')
        stops = expand(spec, banks[g]['stops'])
        if not stops:
            return send_text("None of those stops exist in No. %s. Check the numbers on the guide's stop list." % g)
        new = mark_done(st, banks, g, stops, msg_day)
        return reply_progress(st, banks, g, new, None, msg_day)
    if cmd == '/undo':
        g, _, spec = arg.partition(' ')
        g = g.zfill(2)
        stops = expand(spec, banks[g]['stops']) if g in banks else []
        gone = [s for s in stops if st['done'].get(g, {}).pop(s, None)]
        for cid in [k for k, c in st['cards'].items() if c['g'] == g and banks[g]['by_id'].get(k, {}).get('stop') in gone]:
            del st['cards'][cid]
        return send_text('Removed from reviews: %s' % (', '.join(gone) if gone else 'nothing matched'))
    if cmd == '/today':
        return push(st, banks, force=True)
    if cmd == '/status':
        return send_text(status_text(st, banks))
    if cmd == '/weak':
        weak = sorted(((cid, c) for cid, c in st['cards'].items() if is_weak(c) and cid[:2] in banks), key=lambda x: -x[1]['miss'])[:10]
        if not weak:
            return send_text('No weak spots right now. Anything you miss shows up here until you get it right twice.')
        lines = ['\U0001f3af <b>Weak spots</b> (missed, not yet secure):']
        for cid, c in weak:
            card = banks[cid[:2]]['by_id'][cid]
            lines.append('\u2022 No. %s \u00b7 %s %s: %s (missed %d\u00d7)\n  <a href="%s">Re-read</a>'
                         % (card['guide'], stop_word(banks[cid[:2]]), card['stop'], esc(card['name']), c['miss'], link(card)))
        return send_text('\n'.join(lines))
    if cmd == '/pause':
        st['paused'] = True
        return send_text('\u23f8 Paused. Nothing is lost: due reviews wait for you. Send /resume when you are back.')
    if cmd == '/resume':
        st['paused'] = False
        return send_text('\u25b6\ufe0f Resumed. Your next review comes at %d:00 IST (or send /today).' % int(st['hour']))
    if cmd == '/time':
        if arg.isdigit() and 0 <= int(arg) <= 23:
            st['hour'] = int(arg)
            return send_text('\u23f0 Daily review moved to about %d:00 IST.' % int(arg))
        return send_text('Use an hour from 0 to 23, e.g. <code>/time 7</code>.')
    if cmd in ('/help', 'help'):
        return send_text(help_text())
    return send_text('I only understand commands for now. ' + help_text())

def reply_progress(st, banks, g, new, total, day):
    bank = banks[g]
    word = stop_word(bank).lower()
    n_done = len(st['done'].get(g, {}))
    if not new:
        return send_text('No new %ss in No. %s (%d of %d done). Nothing changed.' % (word, g, n_done, len(bank['stops'])))
    n_cards = sum(1 for c in bank['cards'] if c['stop'] in new)
    first = day + dt.timedelta(days=LADDER[0])
    send_text('\U0001f4e5 <b>Logged</b>: %d new %s%s in No. %s (%s).\n%d of %d done.\n\n%d review questions scheduled. First review: <b>%s</b>, then %s.'
              % (len(new), word, '' if len(new) == 1 else 's', g, ', '.join(new[:12]) + (' ...' if len(new) > 12 else ''),
                 n_done, len(bank['stops']), n_cards, nice(first),
                 ', '.join(nice(day + dt.timedelta(days=x)) for x in LADDER[1:])))

def status_text(st, banks):
    t = today()
    lines = ['\U0001f4ca <b>Status \u00b7 %s</b>' % nice(t)]
    for g, b in sorted(banks.items()):
        n = len(st['done'].get(g, {}))
        if n:
            lines.append('No. %s: %d of %d %ss done' % (g, n, len(b['stops']), stop_word(b).lower()))
    if len(lines) == 1:
        lines.append('Nothing logged yet. Tap "Send progress" in a guide after you finish a stop.')
    due = len(due_cards(st, banks, include_sent=True))
    week = sum(1 for c in st['cards'].values() if d2s(t) < c['due'] <= d2s(t + dt.timedelta(days=7)))
    lines += ['', 'Due today: %d \u00b7 next 7 days: %d' % (due, week),
              'Weak spots: %d \u00b7 mastered: %d' % (sum(is_weak(c) for c in st['cards'].values()), sum(c['k'] >= len(LADDER) for c in st['cards'].values())),
              'Daily review: about %d:00 IST%s' % (int(st['hour']), ' (paused)' if st['paused'] else '')]
    return '\n'.join(lines)

HELP_INTRO = '\U0001f44b <b>MTRX Field Library review bot</b>\nRead a stop, mark it done, tap <b>Send progress</b> in the guide. I bring each stop back after 1, 3, 7 and 21 days, then 2 and 6 months.\n\n'

def help_text():
    return ('<b>Commands</b>\n' + '\n'.join('/%s: %s' % (c, d) for c, d in COMMANDS) +
            '\n\nReplies arrive on my next run, usually within 15 minutes. Library: %s' % SITE)

# ---------------------------------------------------------------- runs

def run():
    if not TOKEN or not CHAT:
        print('Secrets TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID are not set; nothing to do.')
        return 0
    st, banks = load_state(), load_banks()
    sync_cards(st, banks)
    try:
        updates = api('getUpdates', offset=st['offset'], timeout=0, allowed_updates=['message', 'poll_answer'])
        misses = []
        for u in updates:
            st['offset'] = u['update_id'] + 1
            try:
                if 'message' in u and str(u['message']['chat']['id']) == CHAT:
                    m = u['message']
                    handle_text(st, banks, m.get('text', ''), dt.datetime.fromtimestamp(m['date'], IST).date())
                elif 'poll_answer' in u and str((u['poll_answer'].get('user') or {}).get('id')) == CHAT:
                    handle_answer(st, banks, u['poll_answer'], misses)
            except Exception as e:                      # one bad update must not block the queue
                log(st, 'update %s failed: %s' % (u.get('update_id'), e))
        after_answers(st, misses)
        push(st, banks)
        cutoff = d2s(today() - dt.timedelta(days=10))
        st['polls'] = {k: v for k, v in st['polls'].items() if v['sent'] >= cutoff}
    finally:
        save_state(st)
    print('ok: %d updates, %d cards tracked, %d due' % (len(updates), len(st['cards']), len(due_cards(st, banks, True))))
    return 0

def selftest():
    report = {'time': now().isoformat(timespec='seconds'), 'ok': False, 'steps': []}
    def step(name, fn):
        try:
            detail = fn()
            report['steps'].append({'step': name, 'ok': True, 'detail': detail})
            return True
        except Exception as e:
            report['steps'].append({'step': name, 'ok': False, 'detail': str(e).replace(TOKEN, '***') if TOKEN else str(e)})
            return False
    st, banks = load_state(), load_banks()
    ok = step('secrets', lambda: 'token and chat id present' if TOKEN and CHAT else (_ for _ in ()).throw(RuntimeError(
        'missing: ' + ', '.join(n for n, v in (('TELEGRAM_BOT_TOKEN', TOKEN), ('TELEGRAM_CHAT_ID', CHAT)) if not v))))
    ok = ok and step('getMe', lambda: '@' + api('getMe')['username'])
    ok = ok and step('deleteWebhook', lambda: api('deleteWebhook', drop_pending_updates=False) and 'polling mode')
    ok = ok and step('setMyCommands', lambda: api('setMyCommands', commands=[{'command': c, 'description': d} for c, d in COMMANDS]) and '%d commands' % len(COMMANDS))
    ok = ok and step('banks', lambda: ', '.join('No. %s: %d cards' % (g, len(b['cards'])) for g, b in sorted(banks.items())) or (_ for _ in ()).throw(RuntimeError('no question banks')))
    ok = ok and step('sendMessage', lambda: send_text(HELP_INTRO + '\u2705 <b>Self-test</b>: I can reach you. Answer the test question below; I confirm it on my next run.\n\n' + help_text()) and 'sent')
    def sample():
        cid = next(c['id'] for c in banks.get('01', next(iter(banks.values())))['cards'] if c['type'] == 'quiz')
        send_card(st, banks, cid, test=True)
        return 'sent quiz ' + cid
    ok = ok and step('sendPoll', sample)
    report['ok'] = bool(ok)
    save_state(st)
    with open(SELFTEST_PATH, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=1)
        f.write('\n')
    print(json.dumps(report, indent=1))
    return 0

if __name__ == '__main__':
    sys.exit(selftest() if '--selftest' in sys.argv else run())

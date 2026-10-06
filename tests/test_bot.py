#!/usr/bin/env python3
"""Offline simulation of the review bot with a fake Telegram. Run: python3 tests/test_bot.py
It never touches the network or the real bot/state.json."""
import base64, json, os, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.update(TELEGRAM_BOT_TOKEN='', TELEGRAM_CHAT_ID='42')
sys.path.insert(0, os.path.join(ROOT, 'bot'))
import bot  # noqa: E402

tmp = tempfile.mkdtemp()
bot.STATE_PATH = os.path.join(tmp, 'state.json')
bot.SELFTEST_PATH = os.path.join(tmp, 'selftest.json')
bot.TOKEN, bot.CHAT = 'test', '42'
bot.time.sleep = lambda s: None

class FakeTelegram:
    def __init__(self):
        self.inbox, self.sent, self.n, self.uid, self.polls = [], [], 0, 0, {}
    def __call__(self, method, **p):
        if method == 'getUpdates':
            out = [u for u in self.inbox if u['update_id'] >= p['offset']]
            self.inbox = []
            return out
        if method == 'getMe':
            return {'username': 'makingmesmart_bot'}
        if method in ('deleteWebhook', 'setMyCommands'):
            return True
        if method == 'sendPoll':
            assert len(p['question']) <= 300 and 2 <= len(p['options']) <= 10, p
            assert all(len(o['text']) <= 100 for o in p['options']), p
            assert len(p.get('explanation', '')) <= 200
            self.n += 1
            pid = 'poll%d' % self.n
            self.polls[pid] = p
            self.sent.append((method, p))
            return {'poll': {'id': pid}}
        self.sent.append((method, p))
        return {'message_id': len(self.sent)}
    def text(self, t, when):
        self.uid += 1
        self.inbox.append({'update_id': self.uid, 'message': {'chat': {'id': 42}, 'text': t, 'date': int(when.timestamp())}})
    def answer(self, pid, opt):
        self.uid += 1
        self.inbox.append({'update_id': self.uid, 'poll_answer': {'poll_id': pid, 'user': {'id': 42}, 'option_ids': [opt]}})
    def texts(self):
        out = [p['text'] for m, p in self.sent if m == 'sendMessage']
        self.sent = []
        return out

T = FakeTelegram()
bot.api = T
def at(ts):
    os.environ['MTRX_NOW'] = ts
    return bot.now()
def run(ts):
    at(ts)
    bot.run()
    return json.load(open(bot.STATE_PATH))

def code(g, done_stops):
    stops = bot.load_banks()[g]['stops']
    b = bytearray((len(stops) + 7) // 8)
    for i, s in enumerate(stops):
        if s in done_stops:
            b[i // 8] |= 1 << (i % 8)
    return 'p%s_%s' % (g, base64.urlsafe_b64encode(bytes(b)).decode().rstrip('='))

fails = []
def check(name, cond, extra=''):
    print(('PASS ' if cond else 'FAIL ') + name + (('  ' + str(extra)) if not cond else ''))
    if not cond:
        fails.append(name)

# 1. Thu 8 Oct, 10 pm: finish six stops of No. 01 and tap Send progress
six = ['0.2', '0.3', '1.1', '1.2', '1.3', '1.4']
c = code('01', six)
check('progress code fits Telegram start param', len(c) <= 64 and all(ch.isalnum() or ch in '_-' for ch in c), c)
T.text('/start ' + c, at('2026-10-08T22:00'))
st = run('2026-10-08T22:05')
msgs = T.texts()
check('six stops logged with the 8 Oct date', sorted(st['done']['01']) == sorted(six) and set(st['done']['01'].values()) == {'2026-10-08'}, st['done'])
check('reply lists the review ladder', msgs and 'Fri 9 Oct' in msgs[0] and 'Thu 15 Oct' in msgs[0] and 'Thu 29 Oct' in msgs[0] and 'Mon 7 Dec' in msgs[0] and 'Tue 6 Apr' in msgs[0], msgs)
check('no review pushed on day zero', not any('Review' in m for m in msgs), msgs)

# 2. Fri 9 Oct, 7:50 am: too early, nothing sent; 8:10 am: daily review arrives
run('2026-10-09T07:50')
check('nothing before the reminder hour', not T.sent and not T.texts())
st = run('2026-10-09T08:10')
polls = [p for m, p in T.sent if m == 'sendPoll']
msgs = T.texts()
n_cards = len([k for k in st['cards'] if k.startswith('01-')])
check('every card of the six stops goes out on 9 Oct', len(polls) == n_cards and n_cards > 0, (len(polls), n_cards))
check('header message announces the review', msgs and msgs[0].startswith('\u2600'), msgs[:1])
check('recall cards hide the answer in a spoiler', any('<tg-spoiler>' in m for m in msgs))

# 3. Answer: all right except the first quiz (wrong option)
quiz_pids = [pid for pid, p in T.polls.items() if p.get('type') == 'quiz']
missed_pid = quiz_pids[0]
for pid, p in list(T.polls.items()):
    if p.get('type') == 'quiz':
        T.answer(pid, p['correct_option_id'] if pid != missed_pid else (p['correct_option_id'] + 1) % len(p['options']))
    else:
        T.answer(pid, 0)
missed_card = st['polls'][missed_pid]['card']
right_card = st['polls'][quiz_pids[1]]['card']
st = run('2026-10-09T08:40')
msgs = T.texts()
check('miss is reported with a re-read link', any('To revisit' in m and 'kevincecil11.github.io/mtrx-field-library/guides/01-tech-wild.html#' in m for m in msgs), msgs)
check('done-for-today summary', any('Done for today' in m for m in msgs), msgs)
check('missed card comes back tomorrow', st['cards'][missed_card]['due'] == '2026-10-10' and st['cards'][missed_card]['miss'] == 1, st['cards'][missed_card])
check('right card moves to the 3-day rung (Sun 11 Oct)', st['cards'][right_card]['due'] == '2026-10-11', st['cards'][right_card])
check('only one daily review per day', (run('2026-10-09T12:00') and not [1 for m, p in T.sent if m == 'sendPoll']))
T.texts()

# 4. Follow the right card up the ladder by answering correctly on each due date
expected = ['2026-10-15', '2026-10-29', '2026-12-07', '2027-04-06', '2028-04-05']
dates = ['2026-10-11', '2026-10-15', '2026-10-29', '2026-12-07', '2027-04-06']
ok = True
for day, exp in zip(dates, expected):
    T.polls.clear()
    run(day + 'T08:05')
    pid = next(pid for pid, p in T.polls.items() if json.load(open(bot.STATE_PATH))['polls'][pid]['card'] == right_card)
    p = T.polls[pid]
    T.answer(pid, p['correct_option_id'] if p.get('type') == 'quiz' else 0)
    st = run(day + 'T09:00')
    T.texts()
    ok = ok and st['cards'][right_card]['due'] == exp
    if not ok:
        print('   ladder broke at', day, st['cards'][right_card])
        break
check('ladder: 9 Oct, 11 Oct, 15 Oct, 29 Oct, 7 Dec, 6 Apr 2027, then yearly', ok)

# 5. Commands
at('2026-10-12T21:00')
for t in ['/done 01 2.1-2.3', '/status', '/weak', '/undo 01 2.3', '/pause', '/time 7', '/resume', '/help', 'hello', '/done 99 1.1', '/today']:
    T.text(t, bot.now())
st = run('2026-10-12T21:05')
msgs = T.texts()
check('/done adds 2.1 to 2.3 then /undo removes 2.3', '2.1' in st['done']['01'] and '2.2' in st['done']['01'] and '2.3' not in st['done']['01'], st['done']['01'])
check('/status reports progress', any('Status' in m and 'No. 01' in m for m in msgs), msgs)
check('/time sets 7 am', st['hour'] == 7)
check('/resume clears pause', st['paused'] is False)
check('/done with a bad guide explains usage', any('Use it like this' in m for m in msgs))
check('every command got a reply', len(msgs) >= 10, len(msgs))

# 6. Messages from strangers are ignored
T.uid += 1
T.inbox.append({'update_id': T.uid, 'message': {'chat': {'id': 999}, 'text': '/status', 'date': int(bot.now().timestamp())}})
run('2026-10-12T21:20')
check('strangers get no reply', not T.texts())

# 7. Daily cap and interleaving across guides
T.text('/start ' + code('05', bot.load_banks()['05']['stops']), at('2026-10-12T22:00'))
T.text('/start ' + code('02', ['1', '2']), at('2026-10-12T22:00'))
run('2026-10-12T22:05'); T.texts(); T.sent.clear(); T.polls.clear()
run('2026-10-13T08:05')
guides = [json.load(open(bot.STATE_PATH))['polls'][pid]['card'][:2] for pid in T.polls]
check('daily cap of 15 questions', len(guides) == bot.CAP, len(guides))
check('guides are interleaved', len(set(guides[:3])) >= 2, guides[:6])

# 8. Self-test against the fake
T.sent.clear()
bot.selftest()
rep = json.load(open(bot.SELFTEST_PATH))
check('self-test passes every step', rep['ok'] and all(s['ok'] for s in rep['steps']), rep)
pid = list(T.polls)[-1]
T.answer(pid, 0)
run('2026-10-13T09:00')
check('test answer is confirmed', any('Test answer received' in m for m in T.texts()))

print('\n%d checks failed' % len(fails) if fails else '\nALL CHECKS PASSED')
sys.exit(1 if fails else 0)

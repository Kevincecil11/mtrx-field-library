#!/usr/bin/env python3
"""Offline checks for widget decks (/deck and /start w...). Run: python3 tests/test_deck.py
Fake Telegram, temp state; never touches the network or bot/state.json."""
import base64, json, os, re, sys, tempfile, zlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.update(TELEGRAM_BOT_TOKEN='', TELEGRAM_CHAT_ID='42')
sys.path.insert(0, os.path.join(ROOT, 'bot'))
import bot  # noqa: E402
import deck  # noqa: E402

tmp = tempfile.mkdtemp()
bot.STATE_PATH = os.path.join(tmp, 'state.json')
bot.TOKEN, bot.CHAT = 'test', '42'
bot.time.sleep = lambda s: None

class Fake:
    def __init__(self):
        self.inbox, self.sent, self.uid = [], [], 0
    def __call__(self, method, **p):
        if method == 'getUpdates':
            out, self.inbox = [u for u in self.inbox if u['update_id'] >= p['offset']], []
            return out
        if method == 'sendWidget':
            raw = p['html'].encode('utf-8')
            assert 1 <= len(raw) <= 32768 and len(zlib.compress(raw, 9)) <= 4096, 'widget too large'
            assert len(p.get('caption', '')) <= 1024
        if method == 'sendPoll':
            self.sent.append((method, p))
            return {'poll': {'id': 'p%d' % len(self.sent)}}
        self.sent.append((method, p))
        return {'message_id': len(self.sent)}
    def text(self, t, when):
        self.uid += 1
        self.inbox.append({'update_id': self.uid, 'message': {'chat': {'id': 42}, 'text': t, 'date': int(when.timestamp())}})
    def take(self, kind):
        out = [p for m, p in self.sent if m == kind]
        self.sent = [x for x in self.sent if x[0] != kind]
        return out

T = Fake()
bot.api = T
def at(ts):
    os.environ['MTRX_NOW'] = ts
    return bot.now()
def run(ts):
    at(ts); bot.run()
    return json.load(open(bot.STATE_PATH))

fails = []
def check(name, cond, extra=''):
    print(('PASS ' if cond else 'FAIL ') + name + (('  ' + str(extra)) if not cond else ''))
    if not cond:
        fails.append(name)

def code(g, done):
    stops = bot.load_banks()[g]['stops']
    b = bytearray((len(stops) + 7) // 8)
    for i, s in enumerate(stops):
        if s in done:
            b[i // 8] |= 1 << (i % 8)
    return 'p%s_%s' % (g, base64.urlsafe_b64encode(bytes(b)).decode().rstrip('='))

banks = bot.load_banks()
g = sorted(banks)[0]
stops = banks[g]['stops'][:6]

# 1. nothing logged yet: /deck sends an ungraded practice deck
T.text('/deck', at('2026-11-10T21:00'))
st = run('2026-11-10T21:01')
w = T.take('sendWidget')
check('practice deck sent when nothing is due', len(w) >= 1 and 'Practice deck' in w[0]['caption'], [x.get('caption') for x in w])
pid = next(iter(st['decks']))
check('practice deck stored', st['decks'][pid]['practice'] is True and st['decks'][pid]['cards'])
grades = 'g' * len(st['decks'][pid]['cards'])
T.text('/start w%s_%s' % (pid, grades), at('2026-11-10T21:10'))
before = {k: dict(v) for k, v in st['cards'].items()}
st = run('2026-11-10T21:11')
msgs = [p['text'] for p in T.take('sendMessage')]
check('practice results are acknowledged, not graded', any('Practice logged' in m for m in msgs) and st['cards'] == before, msgs)

# 2. finish six stops, cards due next day, /deck sends them as widgets
T.text('/start ' + code(g, stops), at('2026-11-10T22:00'))
run('2026-11-10T22:01'); T.sent.clear()
T.text('/deck', at('2026-11-11T07:00'))
st = run('2026-11-11T07:01')
w = T.take('sendWidget')
due = [k for k, c in st['cards'].items() if c['due'] <= '2026-11-11']
decks = {k: v for k, v in st['decks'].items() if not v['practice']}
check('review deck carries every due card', sum(len(v['cards']) for v in decks.values()) == min(len(due), bot.DECK_CAP) and w, (len(due), decks))
did, d = next(iter(decks.items()))
h = w[0]['html']
check('widget links back with /start w<deck>', 'https://t.me/' in h and json.dumps(bot.BOT_USERNAME) in h and json.dumps(did) in h and '?start=w' in h)
check('deck id and grades fit a start param', len('w%s_%s' % (did, 'a' * bot.DECK_CAP)) <= 64 and re.fullmatch(r'[A-Za-z0-9]+', did))
check('cards in a deck are marked sent (no duplicate polls today)', all(st['cards'][c]['sent'] == '2026-11-11' for c in d['cards']))
T.sent.clear()
st = run('2026-11-11T08:05')
check('the 8 am poll review skips cards already sent as a deck', not T.take('sendPoll'))

# 3. results: card 0 got+sure, card 1 got+guess (counts as partly), card 2 miss+sure (blind spot)
ids = d['cards']
res = 'c' + 'a' + 'i' + 'b' * (len(ids) - 3)
k0 = st['cards'][ids[0]]['k']
T.text('/start w%s_%s' % (did, res), at('2026-11-11T08:30'))
st = run('2026-11-11T08:31')
msgs = [p['text'] for p in T.take('sendMessage')]
check('sure + right moves up the ladder', st['cards'][ids[0]]['k'] == k0 + 1, st['cards'][ids[0]])
check('a lucky guess counts as partly (no ladder step)', st['cards'][ids[1]]['k'] == k0 and st['cards'][ids[1]]['seen'] == 1, st['cards'][ids[1]])
check('sure but wrong: back tomorrow, flagged as a blind spot', st['cards'][ids[2]]['due'] == '2026-11-12' and any('blind spots' in m for m in msgs), msgs)
check('summary and a re-read list are sent', any('Deck logged' in m for m in msgs) and any('To revisit' in m for m in msgs), msgs)

# 4. the same results again are refused; an unknown deck explains itself
T.text('/start w%s_%s' % (did, res), at('2026-11-11T08:40'))
T.text('/start wnope0_aaa', at('2026-11-11T08:40'))
st2 = run('2026-11-11T08:41')
msgs = [p['text'] for p in T.take('sendMessage')]
check('double submit is ignored', any('already logged' in m for m in msgs) and st2['cards'] == st['cards'], msgs)
check('unknown deck gets a helpful reply', any("can't find that deck" in m for m in msgs), msgs)

# 5. a failing sendWidget falls back to a polite message, never a crash
orig = T.__call__
def broken(method, **p):
    if method == 'sendWidget':
        raise RuntimeError('sendWidget failed: Bad Request: method not found')
    return orig(method, **p)
bot.api = broken
T.text('/deck practice', at('2026-11-11T09:00'))
run('2026-11-11T09:01')
bot.api = T
msgs = [p['text'] for p in T.take('sendMessage')]
check('widget failure falls back to polls advice', any('Could not send the widget deck' in m for m in msgs), msgs)

# 6. /deck is in the command menu and help
check('/deck registered as a command', any(c == 'deck' for c, _ in bot.COMMANDS))

# 7. every widget built from the real banks fits the server limits
big = [c for b in banks.values() for c in b['cards']]
sizes = [deck.size(h)[1] for _, _, h in deck.build_decks(big[:200], 'test')]
check('decks from real cards stay under 4096 bytes compressed', sizes and max(sizes) <= 4096, max(sizes) if sizes else None)

print('\n%d checks failed' % len(fails) if fails else '\nALL CHECKS PASSED')
sys.exit(1 if fails else 0)

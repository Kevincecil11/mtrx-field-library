#!/usr/bin/env python3
"""Regression tests for Web progress codes and the responsive listener.
No network, real secrets, real state file or repository writes.
"""
import datetime as dt
import json
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'bot'))
os.environ.update(TELEGRAM_BOT_TOKEN='', TELEGRAM_CHAT_ID='42', MTRX_NOW='2026-10-07T22:30')
import bot
import listen

bot.TOKEN, bot.CHAT = 'test-token', '42'
bot.STATE_PATH = os.path.join(tempfile.mkdtemp(), 'state.json')
bot.time.sleep = lambda _: None
banks = bot.load_banks()
failures = []


def check(name, condition):
    print(('PASS ' if condition else 'FAIL ') + name)
    if not condition:
        failures.append(name)


# Kevin's real code has three consecutive underscores. They are valid base64url.
code = 'p01___0DAAAAAAA'
g, stops = bot.decode_progress(code, banks)
check('three underscores in Kevin progress code decode correctly', g == '01' and len(stops) == 17)
check('Kevin code includes stop 2.9', '2.9' in stops)

class Fake:
    def __init__(self):
        self.calls = []
        self.inbox = [
            {'update_id': 1, 'message': {'chat': {'id': 42}, 'text': '/today', 'date': 1791399000}},
            {'update_id': 2, 'message': {'chat': {'id': 42}, 'text': '/status', 'date': 1791399000}},
            {'update_id': 3, 'message': {'chat': {'id': 42}, 'text': '/start ' + code, 'date': 1791399000}},
            {'update_id': 4, 'message': {'chat': {'id': 42}, 'text': '/help', 'date': 1791399000}},
        ]

    def __call__(self, method, **params):
        self.calls.append((method, params))
        if method == 'getUpdates':
            inbox, self.inbox = self.inbox, []
            return inbox
        return {'message_id': len(self.calls)}


fake = Fake()
listen.ORIGINAL_API = fake
listen.install()
check('listener completes a window successfully', listen.listen(0) == 0)
state = bot.load_state()
messages = [p['text'] for method, p in fake.calls if method == 'sendMessage']
check('pending /today got a useful reply', any('Nothing due today' in m for m in messages))
check('pending /status got a useful reply', any('Status' in m and 'Listener: online' in m for m in messages))
check('pasted Web command logs all 17 stops', len(state['done']['01']) == 17)
check('progress reply says Logged', any('Logged' in m and '17 new' in m for m in messages))
check('updated help explains copy, paste and Send', any('Telegram Web' in m and 'paste' in m for m in messages))
check('listener uses 20-second long polling', any(method == 'getUpdates' and p['timeout'] == 20 for method, p in fake.calls))
check('consumed offset and heartbeat are persisted', state['offset'] == 5 and state['listener']['mode'] == 'handoff')
check('review clock is based on the original message date', set(state['done']['01'].values()) == {dt.datetime.fromtimestamp(1791399000, bot.IST).date().isoformat()})
check('review questions were scheduled', len(state['cards']) > 0)

# Re-sending the same command is idempotent and does not reset review dates.
bot.handle_text(state, banks, '/start ' + code, bot.today())
check('same progress twice does not duplicate or reset stops', len(state['done']['01']) == 17)
check('duplicate progress gets a clear reply', 'No new stops' in fake.calls[-1][1]['text'])

# A fresh stranger update cannot trigger a reply.
count = len(fake.calls)
fake.inbox = [{'update_id': 5, 'message': {'chat': {'id': 999}, 'text': '/status', 'date': 1791399000}}]
listen.listen(0)
check('strangers still receive no replies', not any(m == 'sendMessage' for m, _ in fake.calls[count:]))

# A blocked or transient failed poll recovers inside the window.
attempts = [0]
ticks = iter([0, 0, 2])
def retry_api(method, **params):
    if method == 'getUpdates':
        attempts[0] += 1
        if attempts[0] == 1:
            raise RuntimeError('temporary test-token failure')
        return []
    return fake(method, **params)
listen.ORIGINAL_API = retry_api
pauses = []
listen.listen(1, clock=lambda: next(ticks), pause=pauses.append)
check('failed poll retries without killing the listener', attempts[0] == 2 and pauses == [5])
check('token never appears in persisted error log', all('test-token' not in s for s in bot.load_state()['log']))

print('\n%d checks failed' % len(failures) if failures else '\nALL LISTENER CHECKS PASSED')
raise SystemExit(bool(failures))

# Review bot: architecture

Status: built and tested offline 6 Oct 2026 (`tests/test_bot.py`). Live once the two secrets are set. Everything runs free on GitHub and Telegram.

## The loop

```
Guide on GitHub Pages
   |  tap "Send progress"  (assets/mtrx-review.js)
   v
Telegram: t.me/makingmesmart_bot?start=p01_<code>   <------  quizzes, recall cards, re-read links
   |  (Telegram holds unread updates for up to 24 h)            ^
   v                                                            |
GitHub Actions "Review bot", every 15 min  ---------------------+
   1. tools/build_questions.py: guides -> bot/questions/NN.json
   2. bot/bot.py: getUpdates (progress, commands, poll answers), grade, reschedule
   3. first run after the reminder hour (8 am IST): send what is due
   4. tools/commit_state.sh: commit bot/state.json
```

## Scheduling rules

- Per stop, not per percentage: each stop's cards start on the day it is logged.
- Ladder from that day: +1, +3, +7, +21, +60, +180 days (finish on Thu 8 Oct: 9 Oct, 11 Oct, 15 Oct, 29 Oct, 7 Dec, 6 Apr 2027). After the last rung: one check a year.
- Right answer: next rung. "Partly": stays on its rung, back in about half the gap. Miss: back to tomorrow, counted as a weak spot until it climbs two rungs.
- One review a day at most, cap 15 questions, most-missed first, guides interleaved. Unanswered cards are re-sent the next day.

## Cards

- **Quiz** (from each guide's quick checks): a Telegram quiz poll; right or wrong shows instantly with the explanation.
- **Recall** (room lines, drills, No. 02 Q and A blocks): the prompt with the model answer hidden in a spoiler, then a "Got it / Partly / Missed it" poll.

## Commands

`/today` send today's review now, `/status`, `/weak`, `/done 01 1.1-1.6` (or `/done 02 1-7`), `/undo 01 1.3`, `/pause`, `/resume`, `/time 7`, `/help`. Replies come on the next run, usually within 15 minutes.

## Progress code

`p` + guide number + `_` + base64url bitmask; bit i is the i-th `<button class="done" data-mod>` in document order (same order as `stops` in the bank). Fits Telegram's 64-character start parameter for up to 360 stops.

## Files

- `bot/questions/NN.json`: `{guide, title, file, day, stops[], cards[{id, guide, stop, name, link, type, q, options, answer, why | answer, label}]}`. Generated; don't edit.
- `bot/state.json`: `{offset, hour, paused, last_push, done{guide{stop: date}}, cards{id{g, k, anchor, due, miss, right, seen, sent, last}}, polls{poll_id{card, kind, sent}}, today{...}, log[]}`.
- `bot/selftest.json`: last live self-test (getMe, deleteWebhook, setMyCommands, banks, sendMessage, sendPoll). No secrets.

## Facts relied on

- A bot can't message you until you've started it. Only the chat in `TELEGRAM_CHAT_ID` is served; everyone else is ignored.
- Quiz polls must be non-anonymous for the bot to receive `poll_answer`.
- Unread updates expire after 24 h, so the bot must run at least daily.
- Pages is free for public repos; Actions is free for public repos; scheduled runs can start late at busy times; scheduled workflows in public repos pause after 60 days without repo activity (the bot's own commits keep it active, and it can be re-enabled in one click).
- Secrets: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`, set under Settings, Secrets and variables, Actions.

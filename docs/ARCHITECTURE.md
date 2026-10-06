# Review bot: architecture

Status: built and tested offline 6 Oct 2026 (`tests/test_bot.py`). 7 Oct 2026: workflows fixed (a colon inside a `run:` line had made both YAML files invalid) and green end to end on GitHub (banks built, offline test passed, report committed). Goes live the moment the two repository secrets reach the workflow. Everything runs free on GitHub and Telegram.

## The loop

```
Guide on GitHub Pages (desktop or iPad)
   |  tap "Send progress"  (assets/mtrx-review.js)
   v
Telegram: t.me/makingmesmart_bot?start=p01_<code>   <------  quizzes, recall cards, re-read links
   |  (Telegram holds unread updates for up to 24 h)            ^
   v                                                            |
GitHub Actions "Review bot", every 10 min  ---------------------+
   1. tools/build_questions.py: guides -> bot/questions/NN.json
   2. bot/bot.py: getUpdates (progress, commands, poll answers), grade, reschedule
   3. first run after the reminder hour (8 am IST): send what is due
   4. tools/commit_state.sh: commit bot/state.json (only when it changed)
   |
   v
bot/state.json "done" -> read by every guide and the library on open (device sync)
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

`/today` send today's review now, `/status`, `/weak`, `/done 01 1.1-1.6` (or `/done 02 1-7`), `/undo 01 1.3`, `/pause`, `/resume`, `/time 7`, `/help`. Replies come on the next run, usually within 10 minutes (the bot's help text says 15 to allow for late scheduled runs).

## Progress code

`p` + guide number + `_` + base64url bitmask; bit i is the i-th `<button class="done" data-mod>` in document order (same order as `stops` in the bank). Fits Telegram's 64-character start parameter for up to 360 stops.

## Two devices (sync, 7 Oct 2026)

- Each browser stores its own progress in localStorage, so desktop and iPad start separate.
- Send progress from either device merges into `bot/state.json` (the bot only adds stops; `/undo` removes).
- `assets/mtrx-review.js` fetches `https://raw.githubusercontent.com/Kevincecil11/mtrx-field-library/main/bot/state.json` (CORS open, cache-busted) when a guide or the library opens. In a guide it clicks the done button for each stop the bot knows and the browser doesn't, then shows "Synced N stops". On the library it writes straight into each guide's progress key and redraws.
- Each stop is applied once per browser (`mtrx-sync-v1`), so a stop unticked by hand stays unticked. Offline or failed fetch: silently skipped.
- Not synced: notes, highlights, quiz answers inside the guides, dark mode, read mode.

## Read mode

`html.mtrx-read` hides `.thumbs`, `.scrollbar`, `.nk-dock`, `.nk-panel`, `.nk-find`, `.fp-side`, `#mtrx-bar`, `#mtrx-toast` and removes the tab gutter. A faded "Exit read mode" pill sits top right and slides away while scrolling down. Toggle: ¶ button, R key; exit: pill or Esc. Stored in `mtrx-read-v1`.

## Files

- `bot/questions/NN.json`: `{guide, title, file, day, stops[], cards[{id, guide, stop, name, link, type, q, options, answer, why | answer, label}]}`. Generated; don't edit.
- `bot/state.json`: `{offset, hour, paused, last_push, done{guide{stop: date}}, cards{id{g, k, anchor, due, miss, right, seen, sent, last}}, polls{poll_id{card, kind, sent}}, today{...}, log[]}`. Public (stop ids, dates and scores only).
- `bot/selftest.json`: last live self-test (secrets, getMe, deleteWebhook, setMyCommands, banks, sendMessage, sendPoll). No secrets.
- `bot/selftest-sources.json`: whether the token and chat id exist as repository secrets or repository variables (true or false only).

## Facts relied on

- A bot can't message you until you've started it. Only the chat in `TELEGRAM_CHAT_ID` is served; everyone else is ignored.
- Quiz polls must be non-anonymous for the bot to receive `poll_answer`.
- Unread updates expire after 24 h, so the bot must run at least daily.
- Pages is free for public repos; Actions standard runners are free for public repos (GitHub billing docs, checked 7 Oct 2026; the 2026 pricing changes kept this); scheduled runs can start late at busy times; scheduled workflows in public repos pause after 60 days without repo activity (the bot's own commits keep it active, and it can be re-enabled in one click).
- `actions/checkout@v5` (Node 24).
- Secrets: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` as repository secrets under Settings, Secrets and variables, Actions, Secrets tab. Repository variables with the same names work as a fallback. Environment secrets (such as under `github-pages`), Codespaces and Dependabot secrets are not visible to these jobs.

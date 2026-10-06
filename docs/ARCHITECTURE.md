# Spaced-review bot: architecture

Status: Phase 1 being built (Oct 2026). Everything runs free on GitHub and Telegram.

## The loop

```
Guide in the browser (GitHub Pages)
   |  tap "Send progress"  (assets/mtrx-review.js)
   v
Telegram chat with @makingmesmart_bot   <------------  quiz + explanation + re-read link
   |  (Telegram holds unread updates for up to 24 h)        ^
   v                                                        |
GitHub Actions cron (every 3 h, free)  ---------------------+
   1. getUpdates: new progress codes, /done commands, quiz answers
   2. update each question's schedule
   3. on the 8 am IST run, send whatever is due
   v
bot/questions/NN.json   question banks (one per guide)
bot/state.json          what is done, what is due, scores (the "database")
```

## Rules

- **Per stop, not per percentage.** Each stop starts its own clock on the day it is marked done.
- **Ladder:** +1, +3, +7, +21, +60 and +180 days. A right answer moves a question one rung up; a miss sends it back to +1 day and adds it to weak spots.
- **One message a day at most,** around 8 am IST, only when something is due. Cap of about 15 questions; overflow rolls to the next day, most-missed first. Same-day items from different guides are mixed into one quiz (interleaving).
- **Milestone exams:** 20 mixed questions 1 month and 6 months after a guide's start date.
- **Progress transport:** the guide encodes finished stops as a bitmask in a deep link, `t.me/makingmesmart_bot?start=<code>` (start parameter: up to 64 chars of A-Z, a-z, 0-9, _ and -). Backup: `/done 01 1.1-1.12`.

## Data shapes

`bot/questions/01.json`

```json
[{"id": "01-2.4-a", "guide": "01", "stop": "2.4", "q": "max 300 chars", "options": ["max 100 chars each", "2 to 10 options"], "answer": 1, "why": "max 200 chars", "link": "guides/01-tech-wild.html#m2-4"}]
```

About 3 questions per stop, reusing each guide's quick checks first.

`bot/state.json`

```json
{"offset": 0, "done": {"01": {"2.4": "2026-10-08"}}, "cards": {"01-2.4-a": {"rung": 2, "due": "2026-10-15", "misses": 0, "last": "2026-10-11"}}, "polls": {"<poll_id>": "01-2.4-a"}, "weak": ["01-2.4-a"]}
```

## Telegram facts relied on

- A bot cannot message you until you have started it.
- Quiz polls (`sendPoll`, `type=quiz`, `is_anonymous=false`) show right or wrong instantly with the explanation; the bot receives `poll_answer` updates on its next run.
- Unread updates expire after 24 hours, so the cron must run at least daily (every 3 h gives margin).

## GitHub facts relied on

- Pages is free for public repos; private repos need a paid plan for Pages.
- Actions is free for public repos. Scheduled runs can start late at busy times.
- Scheduled workflows in public repos are disabled after 60 days without repo activity; the bot's state commits keep it active, and it can be re-enabled in one click.
- Secrets: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`. Never in files.

# MTRX™ Field Library

Kevin Cecil's personal learning library: the MTRX Field Series guides, a home page that shows what to read next, and a free Telegram bot that brings every finished stop back for spaced review.

**Live site:** https://kevincecil11.github.io/mtrx-field-library/

## Setup

1. **Guides** live in `guides/` (done).
2. **Site:** Settings → Pages → Deploy from a branch → `main`, `/ (root)` → Save.
3. **Bot secrets:** Settings → Secrets and variables → Actions → New repository secret: `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`. Never in a file.
4. **Say hi:** send `/start` to @makingmesmart_bot once.
5. **Self-test:** Actions → Bot self-test → Run workflow. You get a test message and a test quiz; the report lands in `bot/selftest.json`.

## Daily use

Read a stop, mark it done, tap **Send progress** (top left of every guide), then tap Start in Telegram. Reviews arrive around 8 am IST on the days something is due.

Bot commands: `/today` `/status` `/weak` `/done 01 1.1-1.6` `/undo 01 1.3` `/pause` `/resume` `/time 7` `/help`.

## Why it is all free

GitHub Pages and GitHub Actions are free for public repos, the Telegram Bot API is free, and the bot's memory is one JSON file in this repo.

## For AI tools and new chats

Start with [AGENTS.md](AGENTS.md), then [docs/CONTEXT.md](docs/CONTEXT.md).

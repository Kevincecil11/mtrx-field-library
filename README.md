# MTRX™ Field Library

Kevin Cecil's personal learning library: the MTRX Field Series guides, a home page that shows what to read next, and a free Telegram bot that brings every finished stop back for spaced review.

**Live site:** https://kevincecil11.github.io/mtrx-field-library/

## Setup

1. **Guides** live in `guides/` (done).
2. **Site:** Settings → Pages → Deploy from a branch → `main`, `/ (root)` → Save (done).
3. **Bot secrets:** Settings → Secrets and variables → Actions → **Secrets** tab → **New repository secret**: `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`, names exactly as written. They must be *repository* secrets: environment secrets (for example under `github-pages`), Codespaces secrets and Dependabot secrets never reach these workflows. Direct link: https://github.com/Kevincecil11/mtrx-field-library/settings/secrets/actions/new. Never in a file.
4. **Say hi:** send `/start` to @makingmesmart_bot once.
5. **Self-test:** Actions → Bot self-test → Run workflow. You get a test message and a test quiz; the report lands in `bot/selftest.json`, and `bot/selftest-sources.json` says where the two settings were found (true or false only).

## Daily use

Read a stop, mark it done, tap **Send progress** (top left of every guide), then tap Start in Telegram. Reviews arrive around 8 am IST on the days something is due. The bot checks for answers and commands every 10 minutes.

- **Read mode:** tap ¶ Read mode (or press R) to hide every button and just read. Tap ✕ Exit read mode or press Esc to bring them back.
- **Two devices (desktop and iPad):** progress is saved per browser. Tap Send progress on the device you read on; when you open a guide or the library on the other device, it pulls the bot's list and ticks those stops (within about 10 minutes of sending). Notes and highlights stay on the device where you made them; export them from the Notes panel.

Bot commands: `/today` `/status` `/weak` `/done 01 1.1-1.6` `/undo 01 1.3` `/pause` `/resume` `/time 7` `/help`.

## Why it is all free

GitHub Pages and GitHub Actions (standard runners) are free for public repos, the Telegram Bot API is free, and the bot's memory is one JSON file in this repo.

## For AI tools and new chats

Start with [AGENTS.md](AGENTS.md), then [docs/CONTEXT.md](docs/CONTEXT.md).

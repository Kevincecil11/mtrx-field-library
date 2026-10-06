# MTRX™ Field Library

Kevin Cecil's personal learning library: the MTRX Field Series guides, a home page that shows what to read next, and a free Telegram bot for spaced review (being added).

**Live site:** https://kevincecil11.github.io/mtrx-field-library/ (after step 2 below)

## One-time setup

1. **Upload the guides.** On the repo page: Add file → Upload files → drag in the `guides` folder (or its 4 HTML files into `guides/`) → Commit changes.
2. **Turn on the site.** Settings → Pages → Source: Deploy from a branch → Branch: `main`, folder: `/ (root)` → Save. It goes live in about a minute.
3. **Bot secrets.** Settings → Secrets and variables → Actions → New repository secret. Add `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`. Never put either in a file.

## Why it is all free

- GitHub Pages hosts public sites for free.
- GitHub Actions is free for public repos; the bot runs on its schedule.
- The Telegram Bot API is free.
- Review state is one small JSON file in this repo, so there is no database.

## For AI tools and new chats

Start with [AGENTS.md](AGENTS.md). The full build skill is in [docs/skill](docs/skill), and the bot design is in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

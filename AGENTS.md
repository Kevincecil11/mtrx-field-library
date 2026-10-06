# MTRX Field Library: context for AI tools

Read this file first. It is the single entry point for any IDE, coding agent or chatbot working in this repo (Claude Code, Gemini CLI, Cursor, Copilot, ChatGPT, ClickUp Brain). The repo is the whole project: guides, research rules, design system, review bot and history.

## Start here (any new chat)

1. Read this file, then `docs/CONTEXT.md`: who Kevin is, every decision so far, verified corrections, what's next.
2. Building or editing a guide: read `docs/skill/SKILL.md`, then the sub-skill for the job: DESIGN-SYSTEM before styling, COVERAGE-AUDIT before curating, LEARNING-RULES and CURIOSITY-UNLEARNING before writing stops, RESEARCH-PLAYBOOK before research, DARK-TOPICS for No. 03 and No. 04.
3. Touching the review bot: read `docs/ARCHITECTURE.md`.
4. The guides are the research record. Every claim, source and evidence grade lives inside `guides/*.html`; read a guide's text before extending it. New raw research goes in `research/`.

## What this is

- The MTRX™ Field Series: interactive, single-file HTML learning guides written for one learner, Kevin Cecil (founder of MTRX™ Digital; MSc in AI/ML, physics BSc, ex-maths teacher, expert vibe coder).
- Live site (GitHub Pages): https://kevincecil11.github.io/mtrx-field-library/
- Goal of every guide: think, talk and work like an insider, not pass exams. About 20 minutes a day, evidence-graded, zero known gaps.
- Personal project, one user. Everything stays free: GitHub Pages, GitHub Actions, Telegram Bot API. No paid services, no n8n, no database server.
- Kevin reads on desktop and iPad. Progress is per browser; the bot's `bot/state.json` is the shared copy that syncs devices.

## Repo map

| Path | What it is |
|---|---|
| `index.html` | Library home: guide cards, per-guide progress (read from each guide's localStorage key), "Read next", start dates. Guide list is `var G` (also exposed as `window.MTRX_GUIDES` for sync) |
| `guides/NN-slug.html` | One self-contained guide each (CSS, JS, base64 images inline) |
| `assets/mtrx-review.js` | Shared add-on loaded by every guide and the library: top bar (Library, Send progress, Read mode), read mode, and device sync from the bot's `bot/state.json`. Change shared behaviour here, not in the guides |
| `bot/bot.py` | Telegram spaced-review bot (stdlib Python) |
| `bot/questions/NN.json` | Question banks, generated from the guides. Never edit by hand |
| `bot/state.json` | The bot's memory (progress, schedule, scores). Written by the bot only. Public, read by the guides for sync |
| `bot/selftest.json`, `bot/selftest-sources.json` | Last live self-test report, and where the two Telegram settings were found (true or false only) |
| `.github/workflows/` | `review-bot.yml` (every 10 min) and `bot-selftest.yml` |
| `tools/` | `build_questions.py`, `check_guide.py` (lint), `extract_kit.py` (design kit from a guide), `commit_state.sh` |
| `tests/test_bot.py` | Offline simulation of the bot with a fake Telegram |
| `docs/skill/` | The full MTRX Field Guides skill and its six sub-skills |
| `docs/CONTEXT.md` | Kevin, decisions log, verified corrections, roadmap |
| `docs/ARCHITECTURE.md` | How the review bot and device sync work |
| `research/` | Raw research per guide (sources, inventories) |

## The guides

| No. | Title | File | Progress key | Status |
|---|---|---|---|---|
| 00 | The learning operating system | `guides/00-learning-os.html` | `mtrx-lab-v1` | Ready |
| 01 | The tech wild: software, stacks and AI | `guides/01-tech-wild.html` | `mtrx-fieldguide-v1` | Ready |
| 02 | The mind: psychology and philosophy | `guides/02-mind.html` | `mtrx-mind-v1` | Weeks 1 to 2 of 4 |
| 03 | Cons and cults (defence first) | not yet | | In development |
| 04 | Sales and persuasion | not yet | | In development |
| 05 | The long game: lives as lab notes, daily toolkit | `guides/05-long-game.html` | `mtrx-long-v1` | Ready |

Progress shape: `localStorage[key] = {"done": {"1.1": true}}` (No. 02 also stores `g`, `ex`, `field`). Every new guide must use this shape and mark stops with `<button class="done" data-mod="ID">` that toggles `is-done`: Send progress, device sync and the library all depend on it. Stop 1.1 is anchored at `#m1-1`; No. 02 days at `#d1`.

## House rules (non-negotiable)

1. No em dashes or en dashes anywhere. Use commas, colons or parentheses.
2. Write the brand as "MTRX™".
3. One self-contained HTML file per guide, images inlined as base64 webp (about 720px, quality 74).
4. Keep `<meta name="mtrx-slug">`, the progress key and stop ids stable across versions. The bot schedules reviews by stop id, so never renumber stops that exist.
5. Stop ids (`data-mod`, `id="mX-Y"`) are unique inside a guide. (6 Oct 2026: No. 01 "The boardroom" reused 4.1 to 4.3; renumbered to 5.1 to 5.3.)
6. Every guide loads `<script src="../assets/mtrx-review.js" defer></script>` just before the LAST `</body>` (the reader kit JS contains a `</body>` string in an export template). The library loads `assets/mtrx-review.js` after setting `window.MTRX_GUIDES`.
7. Every guide ships with notes (Word, Markdown, PDF export), a persistent highlighter, dark mode (◐), search (⌕, / or Ctrl+K), thumb tabs, read mode (from the shared add-on), quick checks, "Try it · 5 min" tasks, a coverage map and "say it in the room" lines. New floating controls must use a class that read mode hides (add it to the read-mode list in `assets/mtrx-review.js`).
8. Evidence first: grade claims (strong, moderate, weak, failed), date-stamp fast-moving facts, verify every quote against a primary source. Never teach myths.
9. Tone: sharp, warm, plain English, examples from Kevin's world (agency clients, callers, pricing, safari and dental niches).
10. Never commit secrets. The Telegram token and chat id live only in GitHub Actions *repository* secrets (Settings, Secrets and variables, Actions, Secrets tab). Environment, Codespaces and Dependabot secrets do not reach the workflows.
11. Workflow YAML: never put `: ` (colon plus space) inside an unquoted `run:` line; use a `run: |` block. On 6 Oct 2026 `run: bash tools/commit_state.sh "bot: review state"` made both workflow files invalid and every run failed instantly with zero jobs. Lint YAML before pushing.

## Publishing a new or updated guide (the full loop)

1. Research into `research/NN-slug/` (markdown plus JSON, every claim with a source URL). Follow RESEARCH-PLAYBOOK.
2. Coverage audit (COVERAGE-AUDIT) with the inventory saved as `research/NN-slug/inventory.jsonl`.
3. Build: `python3 tools/extract_kit.py guides/05-long-game.html kit/` gives the house CSS, reader kit and core JS. Build one self-contained HTML file.
4. Quick checks as `<div class="check"><script type="application/json">{"q":..., "o":[...], "a": index, "w": "why"}</script></div>` inside each stop: they become Telegram quiz cards. Room lines and drills become recall cards. Aim for 3 cards per stop. Telegram limits: question 300 chars, options 100, explanation 200 (longer ones fall back to a text message plus letter options).
5. Lint: `python3 tools/check_guide.py guides/NN-slug.html` must show 0 errors.
6. Library: update the guide's entry in `var G` in `index.html` (file, key, `st: "ready"`, time, parts with stop ids).
7. Commit. Pages republishes in about a minute; the bot rebuilds its banks from the guides on its next run.

## Review bot (summary)

- Kevin taps "Send progress" in a guide; the bot logs those stops and schedules every card at +1, +3, +7, +21, +60 and +180 days. Right moves a card up; a miss resets it to tomorrow.
- One message a day at most (8 am IST by default), cap 15 questions, guides interleaved. The workflow runs every 10 minutes, so replies and commands land within about 10 minutes.
- Telegram commands: /today /status /weak /done /undo /pause /resume /time /help.
- Two devices: each browser keeps its own progress. Send progress from any device merges into `bot/state.json`; every guide and the library fetch that file from raw.githubusercontent.com on open and tick stops the bot knows about. Adds only, each stop applied once (record in localStorage `mtrx-sync-v1`), so a manual untick sticks. Notes and highlights do not sync.
- Read mode: ¶ button or R hides every floating control and widens the page; ✕ or Esc exits; remembered per browser (`mtrx-read-v1`).
- Test offline: `python3 tools/build_questions.py && python3 tests/test_bot.py`. Live check: run the "Bot self-test" workflow (or push a change to `bot/selftest.request`) and read `bot/selftest.json` and `bot/selftest-sources.json`. Public run status: https://api.github.com/repos/Kevincecil11/mtrx-field-library/actions/runs

## Design system (summary; full spec in `docs/skill/DESIGN-SYSTEM.md`)

- Naturalist field-guide look: 19th-century engraving plates, a cover cube of nine plates, thumb tabs on the right edge.
- Colours: Canvas #ECEAE4, Paper #F6F4EF, Ink #151515, Graphite #55586A, Steel #BCBFCC, Mars #ED691D (text #B3460D), Moss #697132 (text #525923), Gunmetal #2F3E46, Jane #F4E3B2, Red #A44A3F for warnings. One accent per part via `data-part`.
- Type: Tanker display (Fontshare) falling back to Anton; Nunito Sans body; JetBrains Mono labels. Body at least 16px, labels at least 14px.

## Learning engine (summary; full rules in `docs/skill/LEARNING-RULES.md`)

Retrieval before reveal, spacing on real dates, interleaving, prediction plus confidence before answers, worked examples, one idea per stop, concrete cases from Kevin's world, weekly teach-back, monthly cold test, weak-spot log.

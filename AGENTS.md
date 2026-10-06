# MTRX Field Library: context for AI tools

Read this file first. It is the single source of context for any IDE, coding agent or chatbot working in this repo (Claude Code, Gemini CLI, Cursor, Copilot, ChatGPT, ClickUp Brain). Deeper rules live in `docs/skill/`.

## What this is

- The MTRX™ Field Series: interactive, single-file HTML learning guides written for one learner, Kevin Cecil (founder of MTRX™ Digital, a web and AI agency in Ahmedabad; MSc in AI/ML, physics BSc, ex-maths teacher, lifelong learner, expert vibe coder).
- Live site (GitHub Pages): https://kevincecil11.github.io/mtrx-field-library/
- The goal of every guide: think, talk and work like an insider, not pass exams. About 20 minutes a day, evidence-graded, zero known gaps.
- Personal project with one user. Everything must stay free: GitHub Pages, GitHub Actions and the Telegram Bot API. No paid services, no n8n, no database server.

## Repo map

| Path | What it is |
|---|---|
| `index.html` | Library home: guide cards, per-guide progress (read from each guide's localStorage key), "Read next", start dates |
| `guides/NN-slug.html` | One self-contained guide each (CSS, JS and base64 images inline) |
| `assets/mtrx-review.js` | Shared add-on loaded by every guide: the Library link now, the Telegram "Send progress" sync next. Change shared behaviour here, not inside the guides |
| `docs/skill/` | The full MTRX Field Guides skill: workflow, design system, learning rules, coverage audit, research playbook, curiosity and unlearning, dark topics |
| `docs/ARCHITECTURE.md` | How the free Telegram spaced-review bot works |
| `bot/`, `.github/workflows/` | Review bot code, question banks, schedule state and the cron job (being added) |

## The guides

| No. | Title | File | Progress key | Status |
|---|---|---|---|---|
| 00 | The learning operating system | `guides/00-learning-os.html` | `mtrx-lab-v1` | Ready |
| 01 | The tech wild: software, stacks and AI | `guides/01-tech-wild.html` | `mtrx-fieldguide-v1` | Ready |
| 02 | The mind: psychology and philosophy | `guides/02-mind.html` | `mtrx-mind-v1` | Weeks 1 to 2 of 4 |
| 03 | Cons and cults (defence first) | not yet | | In development |
| 04 | Sales and persuasion | not yet | | In development |
| 05 | The long game: lives as lab notes, daily toolkit | `guides/05-long-game.html` | `mtrx-long-v1` | Ready |

Progress shape: `localStorage[key] = {"done": {"1.1": true}}` (No. 02 also stores `g`, `ex` and `field`). Stop 1.1 is anchored at `#m1-1`; No. 02 days are anchored at `#d1`.

## House rules (non-negotiable)

1. No em dashes or en dashes anywhere. Use commas, colons or parentheses. A build should fail if one appears.
2. Write the brand as "MTRX™".
3. One self-contained HTML file per guide, with images inlined as base64 webp (about 720px, quality 74).
4. Keep `<meta name="mtrx-slug">` and the progress key stable across versions, so notes, highlights and progress survive updates.
5. Stop ids (`data-mod` and `id="mX-Y"`) must be unique inside a guide. On 6 Oct 2026, No. 01's "The boardroom" reused 4.1 to 4.3 and clashed with Part IV; it was renumbered to 5.1 to 5.3.
6. Every guide loads `<script src="../assets/mtrx-review.js" defer></script>` just before the LAST `</body>`. The reader kit JS contains a `</body>` string inside its export template, so never replace the first match.
7. Every guide ships with: a notes panel (Word, Markdown and PDF export), a persistent highlighter, dark mode (◐), full-text search (⌕, / or Ctrl+K), thumb-index tabs, quick checks, "Try it · 5 min" tasks, a coverage map and "say it in the room" lines.
8. Evidence first: grade claims (strong, moderate, weak, failed), date-stamp fast-moving facts, and verify every quote against a primary source. Never teach myths (learning styles, 21-day habits, ego depletion as a fuel tank, and so on).
9. Tone: sharp, warm, plain English, with examples from Kevin's world (agency clients, callers, pricing, safari and dental niches).
10. Never commit secrets. The Telegram token and chat id live only in GitHub Actions secrets.

## Design system (summary; full spec in `docs/skill/DESIGN-SYSTEM.md`)

- Naturalist field-guide look: 19th-century engraving plates, a cover cube of nine plates, thumb tabs on the right edge.
- Colours: Canvas #ECEAE4, Paper #F6F4EF, Ink #151515, Graphite #55586A, Steel #BCBFCC, Mars #ED691D (text #B3460D), Moss #697132 (text #525923), Gunmetal #2F3E46, Jane #F4E3B2, Red #A44A3F for warnings. One accent per part via `data-part`.
- Type: Tanker for display (Fontshare), falling back to Anton; Nunito Sans for body; JetBrains Mono for labels. Body text at least 16px, labels at least 14px.
- The canonical CSS and reader-kit JS are embedded in every guide. Copy them from the newest build (`guides/05-long-game.html`) when starting a new guide.

## Learning engine (summary; full rules in `docs/skill/LEARNING-RULES.md`)

Retrieval before reveal, spacing (+1, +3, +7, +21, +60 and +180 days), interleaving, a prediction plus confidence before every answer, worked examples, one idea per stop, concrete cases from Kevin's world, a weekly teach-back, a monthly cold test and a weak-spot log.

## Adding a guide (for example No. 03)

1. Run the coverage audit (`docs/skill/COVERAGE-AUDIT.md`) before writing anything.
2. Build one HTML file with the house CSS and reader kit, unique stop ids, and the script tag from rule 6.
3. Save it as `guides/03-cons-and-cults.html`.
4. In `index.html`, update its entry in `var G`: set `file`, `key`, `st: "ready"`, `time` and `parts` (each part's stop ids).
5. Add its question bank to `bot/questions/03.json` (format in `docs/ARCHITECTURE.md`).

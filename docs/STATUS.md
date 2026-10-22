# Library status (updated 22 Oct 2026, late)

Read this first if you are an AI picking up the repo. Older notes in AGENTS.md, ARCHITECTURE.md and CONTEXT.md still hold; this page lists what changed since 9 Oct and everything still open.

## How courses are built now (22 Oct)

Kevin's motive is curiosity first, practical use second. Behaviour subjects (psychology, philosophy, cons and cults, body language) get long, Crash Course style surveys: the whole series, nothing cut, a question bank with a visible "questions answered" map, 3 to 5 books distilled per stop, myths replaced with the true story, a short practical block last. Still 20 minutes a day; longer means more days, plus an optional go-deeper box. One course in active build at a time, plus one repair slot. Full rules: the MTRX-FIELD-GUIDES skill (CURIOSITY-UNLEARNING, DARK-TOPICS). Kevin loved the question-led format of No. 03: keep it for every behaviour course.

## Open to-do list (in order)

Build queue (Kevin's order, 22 Oct: finish cons and cults, then psychology and philosophy):
1. No. 03 Cons and cults, File 2 The leader (2.1 to 2.7): motive, personality, charisma, why we need leaders, building the "we", when the leader falls.
2. No. 03 File 3 The world around (3.1 to 3.9).
3. No. 03 File 4 The big con (4.1 to 4.6): Lustig, The Sting, Saul.
4. No. 03 File 5 Masks and crews (5.1 to 5.6): Ripley, Lupin, Ocean's, real heists.
5. No. 03 File 6 Money fraud (6.1 to 6.6) and File 7 Power and the reveal (7.1 to 7.6).
6. No. 02 The mind, Week 3 "Self, will and the crowd", Week 4 "How to live", then the full Crash Course Psychology and Philosophy extension (nothing cut).
7. No. 06 Read the room: science course spine (nonverbal textbook syllabus plus actor and director lens); Part II Files 2 to 5 on demand.
8. No. 07 Design: discuss with Kevin, coverage audit, then build. Brief in CURIOSITY-UNLEARNING (fonts and pairing first; Sanzo Wada colour; composition, golden ratio and rule of thirds with truth tags; minimal vs bold; brand identity; Apple, Jobs, Ive; Caravaggio, Picasso; Kubrick, Spielberg; great architects and designers).
9. Later: No. 04 Sales and persuasion, No. 08 Screenwriting. No. 09 not assigned.

Repair slot (one guide per session, alongside the build):
- Quiz giveaways: positions balanced (tools/quiz_audit.py) but the right answer is still the longest option in 126 of 153 checks in older guides. Rewrite distractors, worst first: No. 01, No. 00, No. 05, No. 06. No. 03 is at 6 of 21 (29%).

Checks:
- Bot quiet mode: confirm one nudge (not 15 cards) on 23 Oct around 8:00 IST.

Kevin's side:
- Read No. 03 File 1, one stop a day, and tap Send progress.
- Answer the waiting Telegram reviews, or send /today.
- Tap Send progress in No. 00, 02, 05 and 06.
- Name the brand identity book for No. 07.

## Guides

- No. 00, 01, 05: built.
- No. 02 The mind: Weeks 1 to 2 built.
- No. 03 Cons and cults: Start (0.1, 0.2) and File 1 Inside the cult (1.1 to 1.7) built 22 Oct; 9 of 49 stops. Build: build/03/ via .github/workflows/guide-03.yml (run.py renames inherited mtrx-room-* keys to mtrx-cons-*, balances quizzes, lints, copies to guides/03-cons-and-cults.html, syncs index cards, runs qa.py). Progress key mtrx-cons-v1. Add a file as build/03/fN_k.py modules.
- No. 06 Read the room: Part I (0.1 to 1.12) frozen; Part II File 1 (2.1 to 2.7) built 14 Oct. Format: docs/skill/NO-06-SPOTLIGHT-FILES.md.
- No. 07 Design: library card only (in development).

## Build on GitHub (since 14 Oct)

Big guides are not pushed whole. No. 06: push to build/06/; guide-build.yml runs build/run.py (splices between <!-- mtrx:NAME --> markers, refuses to change Part I, balances quizzes, lints, commits, syncs the No. 06 card). No. 03: push to build/03/; guide-03.yml. Both share concurrency group guide-build; guide-build.yml ignores build/03/**. quiz-balance.yml rebalances every guide when tools/quiz_audit.py changes.

## Review bot

- Listener model and handoffs as described in ARCHITECTURE.md (fix of 9 Oct: commit_state.sh lays state on top of fresh main, no rebase).
- Quiet mode (22 Oct): after 3 daily reviews in a row with no answer, one nudge, then no new reviews until any answer or message. Cards stay due. State fields: silent, nudged. Tests: tests/test_bot.py sections 9 and 10.
- Banks rebuild from the guides on every bot run.

## House rules worth repeating

No em or en dashes in content. No Indian cinema in any guide (real Indian cases are fine). Verify every bold quote against a primary source. Stop ids are append only. Dark topics: mechanisms, warning signs and defences, never usable scripts; writing drills are fiction only.

# Library status (updated 23 Oct 2026)

Read this first if you are an AI picking up the repo. Older notes in AGENTS.md, ARCHITECTURE.md and CONTEXT.md still hold; this page lists what changed since 9 Oct and everything still open.

## How courses are built now (22 Oct)

Kevin's motive is curiosity first, practical use second. Behaviour subjects (psychology, philosophy, cons and cults, body language) get long, Crash Course style surveys: the whole series, nothing cut, a question bank with a visible "questions answered" map, 3 to 5 books distilled per stop, myths replaced with the true story, a short practical block last. Still 20 minutes a day; longer means more days, plus an optional go-deeper box. One course in active build at a time, plus one repair slot. Full rules: the MTRX-FIELD-GUIDES skill (CURIOSITY-UNLEARNING, DARK-TOPICS). Kevin loved the question-led format of No. 03: keep it for every behaviour course.

## Open to-do list (in order)

Build queue (Kevin, 23 Oct: "Fix it then start No. 07 Part 1"):
1. No. 07 Design, Part 1: in build from 23 Oct. Inputs: the 32-page research blueprint (MTRX-No07-Design-Research-Blueprint, docx and PDF) and its research notes. Brief in CURIOSITY-UNLEARNING (fonts and pairing first; Sanzo Wada colour; composition, golden ratio and rule of thirds with truth tags; minimal vs bold; brand identity; Apple, Jobs, Ive; Caravaggio, Picasso; Kubrick, Spielberg; great architects and designers).
2. No. 07 Design, Part 2.
3. No. 02 The mind, Week 3 "Self, will and the crowd", Week 4 "How to live", then the full Crash Course Psychology and Philosophy extension (nothing cut).
4. No. 06 Read the room: science course spine (nonverbal textbook syllabus plus actor and director lens); Part II Files 2 to 5 on demand.
5. Later: No. 04 Sales and persuasion, No. 08 Screenwriting. No. 09 not assigned.

Repair slot (one guide per session, alongside the build):
- Quiz giveaways: positions are balanced by tools/quiz_audit.py, but the right answer is still often the longest option. No. 03: 82 of 159 (52%) on the 23 Oct build; the five worst (6.3 twice, 6.5, 6.6, 7.3) were rewritten on 23 Oct. Next: the rest of No. 03 above 1.4x, then No. 01, No. 00, No. 05, No. 06.

Checks:
- Bot quiet mode: confirm one nudge (not 15 cards) on 23 Oct around 8:00 IST.

Kevin's side:
- Read No. 03, one stop a day, and tap Send progress.
- Answer the waiting Telegram reviews, or send /today.
- Tap Send progress in No. 00, 02, 05 and 06.
- Name the brand identity book for No. 07.

## Guides

- No. 00, 01, 05: built.
- No. 02 The mind: Weeks 1 to 2 built.
- No. 03 Cons and cults: complete on 23 Oct. Start (0.1, 0.2) plus Files 1 to 8, 53 stops (55 with Start), 159 checks. File 8 "The interrogation room" is a bonus deep dive: KUBARK, Biderman's chart, MKUltra, the torture report, Hubbard and Manson. On 23 Oct, at Kevin's request, 1.1 and 1.2 swapped content (1.1 is now "what a cult is", 1.2 "who joins"), with every cross-reference updated. Build: build/03/ via .github/workflows/guide-03.yml (run.py renames inherited mtrx-room-* keys to mtrx-cons-*, balances quizzes, lints, copies to guides/03-cons-and-cults.html, syncs index cards, runs qa.py). Progress key mtrx-cons-v1. Add a file as build/03/fN_k.py modules, plus a PLAN entry in build.py.
- No. 06 Read the room: Part I (0.1 to 1.12) frozen; Part II File 1 (2.1 to 2.7) built 14 Oct. Format: docs/skill/NO-06-SPOTLIGHT-FILES.md.
- No. 07 Design: library card only; Part 1 in build.

## Build on GitHub (since 14 Oct)

Big guides are not pushed whole. No. 06: push to build/06/; guide-build.yml runs build/run.py (splices between <!-- mtrx:NAME --> markers, refuses to change Part I, balances quizzes, lints, commits, syncs the No. 06 card). No. 03: push to build/03/; guide-03.yml. Both share concurrency group guide-build; guide-build.yml ignores build/03/**. quiz-balance.yml rebalances every guide when tools/quiz_audit.py changes.

Gotcha (23 Oct): tools/check_guide.py fails any build whose output contains the text "_files/" (a browser Save page leftover), and a failed candidate leaves the live guide unchanged without any loud error. A real URL with that path must be written with %5F, as in the 6.6 OHCHR link. Always read build/out/03-report.txt after a push.

## Review bot

- Listener model and handoffs as described in ARCHITECTURE.md (fix of 9 Oct: commit_state.sh lays state on top of fresh main, no rebase).
- Quiet mode (22 Oct): after 3 daily reviews in a row with no answer, one nudge, then no new reviews until any answer or message. Cards stay due. State fields: silent, nudged. Tests: tests/test_bot.py sections 9 and 10.
- Banks rebuild from the guides on every bot run.

## House rules worth repeating

No em or en dashes in content. No Indian cinema in any guide (real Indian cases are fine). Verify every bold quote against a primary source. Stop ids are append only (the 1.1/1.2 content swap was a one-off at Kevin's request). Dark topics: mechanisms, warning signs and defences, never usable scripts; writing drills are fiction only.

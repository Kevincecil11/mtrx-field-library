# Library status (updated 22 Oct 2026)

Read this first if you are an AI picking up the repo. Older notes in AGENTS.md, ARCHITECTURE.md and CONTEXT.md still hold; this page lists what changed since 9 Oct and everything still open.

## How courses are built now (22 Oct)

Kevin's motive is curiosity first, practical use second. Behaviour subjects (psychology, philosophy, cons and cults, body language) get long, Crash Course style surveys: the whole series, nothing cut, a question bank with a visible "questions answered" map, 3 to 5 books distilled per stop, myths replaced with the true story, a short practical block last. Still 20 minutes a day; longer means more days, plus an optional go-deeper box. One course in active build at a time, plus one repair slot. Full rules: the MTRX-FIELD-GUIDES skill (CURIOSITY-UNLEARNING, DARK-TOPICS).

## Open to-do list (in order)

Build queue (one per session):
1. No. 02 The mind, Week 3: "Self, will and the crowd". Overdue since about 16 Oct. Doubles as the foundation for the cults file.
2. No. 03 Cons and cults: coverage audit and question bank, then the cults file (the biggest, curiosity first), then the con files. Weighting 60% screenwriting, 40% business.
3. No. 02 Week 4: "How to live". Closes the first 28 days.
4. No. 06 Read the room: a proper science course as the spine (built from the nonverbal textbook syllabus, plus the actor and director lens). Part I and Part II stay as the applied files.
5. No. 02 extension: the rest of Crash Course Psychology and Philosophy, so nothing is cut (about 8 to 10 more weeks).
6. Rest of No. 03 files.
7. Later: No. 04 Sales and persuasion, No. 08 Screenwriting.

On demand (when Kevin finishes the file before it):
- No. 06 Part II File 2 The Read (2.8 to 2.13), File 3 George Newman (2.14 to 2.22), File 4 Network (2.23 to 2.30), File 5 The line (2.31 to 2.34).

Repair slot (one guide per session, alongside the build):
- Quiz giveaways: right-answer positions are balanced (22 Oct, tools/quiz_audit.py) but the right answer is still the longest option in 126 of 153 checks. Rewrite distractors to equal length and plausibility, worst first: No. 01 client scenarios, then No. 00, No. 05, No. 06. Report: build/out/quiz-audit.txt.

Checks:
- Bot quiet mode: confirm one nudge (not 15 cards) on 23 Oct around 8:00 IST.

Kevin's side:
- Answer the waiting Telegram reviews, or send /today.
- Tap Send progress in every guide read so far (No. 00, 02, 05 and 06 have never sent progress).
- Read No. 06 Part II File 1 and run the Stop 2.7 boss fight; that unlocks File 2.
- Name the cases he is sick of for No. 03.

## Guides

- No. 00, 01, 05: built.
- No. 02 The mind: Weeks 1 to 2 built.
- No. 06 Read the room: Part I (stops 0.1 to 1.12) built and frozen. Part II "The Spotlight Files": File 1 (2.1 to 2.7) built 14 Oct. Format and numbering: docs/skill/NO-06-SPOTLIGHT-FILES.md.
- No. 03 Cons and cults: not started; brief saved in the DARK-TOPICS skill.

## Build on GitHub (since 14 Oct)

Big guides are not pushed whole. Push small sources to build/06/; .github/workflows/guide-build.yml runs build/run.py, which splices parts between <!-- mtrx:NAME --> markers, refuses to change Part I, balances quiz answer positions, lints, commits the guide, and syncs the No. 06 card on index.html (build/06/index_card.py). Plan from build/out/06-skeleton.txt and 06-probe.txt, not the HTML. Details: build/README.md. .github/workflows/quiz-balance.yml rebalances every guide when tools/quiz_audit.py changes.

## Review bot

- Listener model and handoffs as described in ARCHITECTURE.md (fix of 9 Oct: commit_state.sh lays state on top of fresh main, no rebase).
- Quiet mode (22 Oct): after 3 daily reviews in a row with no answer, the bot sends one nudge and stops sending new reviews until any answer or message. Cards stay due, nothing is lost. State fields: silent, nudged. Tested in tests/test_bot.py sections 9 and 10.
- Banks rebuild from the guides on every bot run, so rebalanced quizzes reach Telegram automatically.

## House rules worth repeating

No em or en dashes in content. No Indian cinema in any guide (real Indian cases are fine where relevant). Verify every bold quote against a primary source. Stop ids are append only.

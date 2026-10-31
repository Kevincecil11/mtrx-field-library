# Library status (updated 27 Oct 2026)

Read this first if you are an AI picking up the repo. Older notes in AGENTS.md, ARCHITECTURE.md and CONTEXT.md still hold; this page lists what changed since 9 Oct and everything still open.

## How courses are built now (22 Oct)

Kevin's motive is curiosity first, practical use second. Behaviour subjects (psychology, philosophy, cons and cults, body language) get long, Crash Course style surveys: the whole series, nothing cut, a question bank with a visible "questions answered" map, 3 to 5 books distilled per stop, myths replaced with the true story, a short practical block last. Still 20 minutes a day; longer means more days, plus an optional go-deeper box. One course in active build at a time, plus one repair slot. Full rules: the MTRX-FIELD-GUIDES skill (CURIOSITY-UNLEARNING, DARK-TOPICS). Kevin loved the question-led format of No. 03: keep it for every behaviour course.

## Open to-do list (27 Oct)

Kevin's plan (27 Oct): finish No. 02 and No. 06, leave No. 05 as it is (complete), no quiz repairs in No. 01, then finish No. 07 as a light inspiration guide with no new quizzes. Done on 27 Oct, published through the one-off import workflow (.github/workflows/import-sources.yml).

Next, when Kevin asks:
1. No. 09 not assigned. Next candidates: an applied-AI deep dive, a second No. 08 season (feature-length craft: sequences, TV pilot, adaptation in depth).
2. No. 02 extension: the rest of Crash Course Psychology and Philosophy (nothing cut), as Weeks 5 onward.
3. Repair slot: quiz giveaways (right answer often the longest). No. 06 File 1: 15 of 21. No. 01 repairs are off the list (Kevin, 27 Oct).
4. Proposed skill updates (branch by learning purpose; craft guides vs behaviour guides) are drafted but NOT saved: Kevin has not approved them.

Kevin's side:
- Read, tap Send progress, answer the Telegram reviews.
- Name the brand identity book for No. 07, if he wants it distilled.

## Guides

- No. 00, 01, 03, 05: complete.
- No. 04 Sales and persuasion: complete, 28 days (built 27 Oct 2026, like No. 02). Fields Persuasion (per) and Sales (sal), 14 days each; internal codes psy/phi reuse the No. 02 shell. Sources: build/04/front.py (cover, maps, coverage, question bank, library) and w1a.py to w4b.py (plain data, normalised from drafts/04). build/04/build.py uses guides/02-mind.html as the shell; pipeline build/04/run.py via guide-04.yml; card sync build/04/index_card.py; plates cached in build/out/04-img. Research: 264-concept inventory (207 MUST), question bank, persuasion and sales insider reports (kept in the build pack, not the repo). Durations marked ~ are approximate; Days 27 and 28 use long talks with a stopping rule.
- No. 08 Screenwriting: complete, 28 days (built 1 Nov 2026, like No. 02 and No. 04). Fields Story (sto) and Script (scr), 14 days each; internal codes psy/phi. Each day's Write it drill builds a 5-page short (Week 1 premise and logline, Week 2 character and outline, Week 3 first draft, Week 4 rewrite and a 90-day plan). Sources: build/08/front.py (maps, coverage, question bank, library with legal screenplays) and w1a.py to w4b.py. build/08/build.py uses guides/02-mind.html as the shell; pipeline build/08/run.py via guide-08.yml; card sync build/08/index_card.py; key mtrx-screen-v1, slug mtrx-field-guide-to-screenwriting; plates cached in build/out/08-img. Research: 274-concept inventory (228 MUST), 75-question bank, story and script insider reports (kept in the build pack). Long talks carry a stopping rule.
- No. 02 The mind: complete, 28 days. Weeks 3 and 4 are rendered from build/02/w3a.py, w3b.py, w4a.py, w4b.py by build/02/build.py (splices between <!-- mtrx:w3 --> and <!-- mtrx:w4 -->, hash-protects days 1 to 14, idempotent). Pipeline: build/02/run.py via guide-02.yml; card sync build/02/index_card.py. Plates are Commons files cached in build/out/02-img.
- No. 03 Cons and cults: complete, 55 stops, 159 checks. build/03/ via guide-03.yml.
- No. 06 Read the room: complete, 48 stops. Part I frozen (sha256 b121690af0ea). Part II Files 1 to 5 in build/06/p2_file1.py to p2_file5.py; Files 3 to 5 took over the old watch-ahead sections and keep their plates and scenes under "Scene library: more to watch". build/06/build.py is idempotent (fixed 27 Oct).
- No. 07 Design and taste: complete, 78 stops. Part 1 (1.1 to 1.5) is the full format with 15 checks. Parts 2 to 9 are lite inspiration stops (no quizzes, "Mark stop X seen") in build/07/f2_lite_a.py to f9_lite.py; their images load from Wikimedia Commons at reading time. The editorial edition (build/07/editorial.py + editorial-data.json) adds the cover, the 34-entry style atlas as 6.3 (between 6.2 and 6.4, no quiz), the eight dials, and the proportion workbench after 2.11. build/07/ via guide-07.yml.

## Build on GitHub (since 14 Oct)

Big guides are not pushed whole. No. 06: push to build/06/; guide-build.yml runs build/run.py (splices between <!-- mtrx:NAME --> markers, refuses to change Part I, balances quizzes, lints, commits, syncs the No. 06 card). No. 03: push to build/03/; guide-03.yml. No. 02: build/02/ via guide-02.yml. No. 07: build/07/ via guide-07.yml. All share concurrency group guide-build; guide-build.yml ignores build/02/**, build/03/** and build/07/**. Big source drops can go through import-sources.yml: push import/request.json with a short-lived zip URL and its sha256; the workflow unpacks only build/02, build/06, build/07 and docs, runs all three pipelines and commits. Commits made by Actions do not trigger other workflows. quiz-balance.yml rebalances every guide when tools/quiz_audit.py changes.

Gotcha (23 Oct): tools/check_guide.py fails any build whose output contains the text "_files/" (a browser Save page leftover), and a failed candidate leaves the live guide unchanged without any loud error. A real URL with that path must be written with %5F, as in the 6.6 OHCHR link. Always read build/out/03-report.txt after a push.

## Review bot

- Listener model and handoffs as described in ARCHITECTURE.md (fix of 9 Oct: commit_state.sh lays state on top of fresh main, no rebase).
- Quiet mode (22 Oct): after 3 daily reviews in a row with no answer, one nudge, then no new reviews until any answer or message. Cards stay due. State fields: silent, nudged. Tests: tests/test_bot.py sections 9 and 10.
- Banks rebuild from the guides on every bot run.

## House rules worth repeating

No em or en dashes in content. No Indian cinema in any guide (real Indian cases are fine). Verify every bold quote against a primary source. Stop ids are append only (the 1.1/1.2 content swap was a one-off at Kevin's request). Dark topics: mechanisms, warning signs and defences, never usable scripts; writing drills are fiction only.

- 1 Nov 2026 design pass: No. 02 (Weeks 3 and 4), No. 04 and No. 08 now use house-style engraving plates (build/NN/plates, AI-generated with the DESIGN-SYSTEM prompt) instead of Wikimedia photos; cover tiles are named; diagram labels are fitted at build time by build/NN/svgfit.py.

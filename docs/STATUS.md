# Library status (updated 22 Oct 2026)

Read this first if you are an AI picking up the repo. Older notes in AGENTS.md, ARCHITECTURE.md and CONTEXT.md still hold; this page lists what changed since 9 Oct.

## Guides

- No. 00, 01, 05: built.
- No. 02 The mind: Weeks 1 to 2 built. Weeks 3 to 4 ("Self, will and the crowd", "How to live") next, one week per drop.
- No. 06 Read the room: Part I (stops 0.1 to 1.12) built and frozen. Part II "The Spotlight Files": File 1 (2.1 to 2.7) built 14 Oct. Files 2 to 5 (2.8 to 2.34) are built one at a time, as Kevin finishes the previous file. Format and numbering: docs/skill/NO-06-SPOTLIGHT-FILES.md.
- No. 03 Cons and cults: next new guide, after No. 02 Weeks 3 to 4. Case-file format plus the DARK-TOPICS page pattern; coverage audit against the CFE syllabus, white-collar crime courses and cult-recovery research before writing.
- No. 04 Sales and persuasion, No. 08 Screenwriting: later.

## Build on GitHub (since 14 Oct)

Big guides are not pushed whole. Push small sources to build/06/; .github/workflows/guide-build.yml runs build/run.py, which splices parts between <!-- mtrx:NAME --> markers, refuses to change Part I, lints, commits the guide, and syncs the No. 06 card on index.html (build/06/index_card.py). Plan from build/out/06-skeleton.txt and 06-probe.txt, not the HTML. Details: build/README.md.

## Review bot

- Listener model and handoffs as described in ARCHITECTURE.md (fix of 9 Oct: commit_state.sh lays state on top of fresh main, no rebase).
- Quiet mode (22 Oct): after 3 daily reviews in a row with no answer, the bot sends one nudge and stops sending new reviews until any answer or message. Cards stay due, nothing is lost. State fields: silent, nudged. Tested in tests/test_bot.py sections 9 and 10.

## House rules worth repeating

No em or en dashes in content. No Indian cinema in any guide (real Indian cases are fine where relevant). Verify every bold quote against a primary source. Stop ids are append only.

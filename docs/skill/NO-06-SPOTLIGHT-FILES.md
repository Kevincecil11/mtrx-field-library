# No. 06 Part II: The Spotlight Files (saved 14 Oct 2026, before the build)

Kevin's verdict on Part I: useful but "boring and lacklusting". He liked the old ClickUp docs (JFK Spotlight, Bureau Method, Saul Goodman file): a person at the centre, named techniques, swagger, what to do today. Part I stays exactly as built (his words: keep part 1 as it is, the video clips are fine). No Indian cinema anywhere.

## Format of every Part II stop (a case file)

Cold open (anomaly, predict, confidence, reveal in details) > dossier (subject, role, known for, the move, stamp) > the story (3 to 4 paragraphs, verbatim quotes only, fetched from primary pages) > the move (big line + 3 steps) > the scene(s) (oEmbed-verified YouTube, watch for, read, steal this, reality check, content note) > why it works (specs + one SVG + graded evidence table) > truth tags (holds up / partly / myth, one line + source, used to correct the old docs' myths) > in your world > drill (bot recall card) > Try it 5 min > writer's note (No. 08) > room line > next question > 3 checks > done button.

## Numbering (append only, the bot and Send progress key off order)

- File 1 The Spotlight: 2.1 to 2.7 (section s4, data-part 4, tab data-t 4). Built 14 Oct.
- File 2 The Read: 2.8 to 2.13 (planned: hungers rebuilt, Kazan reading actors, reading a group). Insert as section s6 right after s4, tab data-t 6.
- File 3 George Newman: 2.14 to 2.22 (old s2 watch-ahead: walk and swing GIFs, stance, voice plates, scene library A to H).
- File 4 Pitch and network: 2.23 to 2.30 (old s3). File 5 The Line: 2.31 to 2.34 (old s5).

## Build pipeline (repo, not sandbox: sandbox resets wiped the old build)

- Push small sources to build/06/ (build.py, p2_fileN.py, p2_svgs.py, p2.css). .github/workflows/guide-build.yml runs build/run.py on GitHub: splices between <!-- mtrx:NAME --> markers, refuses to write if Part I's bytes change, lints with tools/check_guide.py, commits the guide only if clean.
- Read build/out/06-report.txt, 06-skeleton.txt and 06-probe.txt instead of the 840 KB HTML.
- New file = new p2_fileN.py module added to FILES in build.py. Never edit build/out by hand.

## Status 14 Oct

File 1 sources were delivered to Kevin as a zip (build/06, four files) because the first batch was too big to send safely through the API in one call. When he uploads build/06, the workflow builds the guide by itself. From File 2 on, push the new module directly. No. 02 Weeks 3 to 4 are due around 16 Oct.

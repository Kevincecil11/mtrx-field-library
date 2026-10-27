# Field Series checkpoint, 27 Oct 2026 (read this first)

Kevin's plan (27 Oct): finish No. 02 and No. 06 properly; leave No. 05 as it is (it is complete); skip quiz repairs in No. 01; then finish No. 07 as a light, quiz-free inspiration guide. Every guide must end up complete. Full freedom on order.

## Build pack (authoritative copy of today's work)

[MTRX-Field-Series-Build-2026-10-27.zip](https://t90161376302.p.clickup-attachments.com/t90161376302/4593eea2-9d92-5194-9ec2-a2e439a12426/MTRX-Field-Series-Build-2026-10-27.zip?view=open) contains build/02, build/06, build/07, drafts/ (all research fragments, FORMAT notes, validator, merge script, QA script) and tools/.

## State: drafted, validated, built locally, NOT yet published

- **No. 02 The mind:** Weeks 3 and 4 written (days 15 to 28, 14 days, 28 new glossary terms, both week tie-ups, whole-guide capstone). New splice pipeline build/02/ (build.py, render02.py, w3a.py, w3b.py, w4a.py, w4b.py). Local build: 28 stops, 0 lint errors, no page errors desktop or mobile. Days 1 to 14 are hash-protected. Plates are Wikimedia Commons files fetched in CI into build/out/02-img/. Still needed: build/02/run.py, a guide-02 workflow (copy guide-07.yml pattern), and the index card update (G entry 02: st ready, time 'Complete · 28 days').
- **No. 06 Read the room:** Part II Files 2 to 5 written (stops 2.8 to 2.34, 27 stops, 46 oEmbed-verified scenes). build/06/build.py updated: File 2 inserted after File 1, Files 3 to 5 take over the old watch-ahead sections s2, s3, s5 and KEEP their plates, GIFs and scene library under 'Scene library: more to watch'. index_card.py marks the guide ready when all 5 files exist. Local build: 48 stops, 149 checks, 0 lint errors, Part I unchanged byte for byte, no overflow desktop or mobile. Push build/06/*.py and guide-build.yml rebuilds it.
- **No. 07 Design:** 10 lite fragments drafted for Parts 2 to 9 (70 stops, no quizzes, Commons images loaded remotely via Special:FilePath to keep the file small). build/07/build.py gained lite_stop() and loads modules exporting STOPS and IMAGES. All fragments validate. Still needed: copy drafts/07/p*.py into build/07 as f2_lite.py ... f9_lite.py (merge p2a+p2b, p4a+p4b), update editorial.py cover text (hardcoded '8 stops built of 78') and place the 6.3 atlas between 6.2 and 6.4, then build, QA and publish together with the editorial redesign files (editorial.py, editorial-data.json).
- **Not started (outside Kevin's current plan):** No. 04 Sales and persuasion, No. 08 Screenwriting, No. 09.

## Publishing plan

The new sources total about 800 KB, too much to paste through the GitHub tool comfortably. Preferred route: a one-off import workflow that downloads a relay link of the build pack (needs Kevin's one-click confirmation for the relay link), extracts only build/02, build/06, build/07 and runs the three pipelines (commits made by Actions do not trigger other workflows, so the import job must run build/run.py, build/02/run.py and build/07/run.py itself). Fallback: push files in batches with the GitHub tool, verifying blob SHAs.

After publishing: read build/out/*-report.txt, confirm the live guides, update docs/STATUS.md.

## House rules

No em or en dashes. No Indian cinema. Verbatim quotes only from opened sources. Stop ids append only. Keep progress keys and mtrx-slug values stable.

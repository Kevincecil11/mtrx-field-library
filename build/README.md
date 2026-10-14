# build/: update big guides by pushing small files

Guides are single HTML files of 400 KB to 1.7 MB, too big for an AI to push
through the GitHub API. So a guide part lives here as small source files, and
`.github/workflows/guide-build.yml` renders it on GitHub and commits the guide.

- `run.py`: the pipeline. Builds `build/out/06-candidate.html`, lints it with
  `tools/check_guide.py`, and only a clean candidate replaces the guide.
- `skeleton.py`: writes `build/out/06-skeleton.txt`, a compact map of the live
  guide (stops, ids, classes, outline, one full stop). Read this, not the HTML.
- `06/`: No. 06 parts. `build.py` splices rendered parts between
  `<!-- mtrx:part2 -->` markers and leaves Part I byte for byte untouched.
- `out/`: written by the workflow. Never edit by hand.

Rules: push sources only, never `build/out/`. Stop ids are append only (the
review bot keys reviews and the Send progress code off their order).

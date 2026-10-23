# Field Series continuation checkpoint

Prepared 23 October 2026. Read before continuing in a new chat.

## Download the complete working state

- [Complete resume pack: source snapshot, redesigned guide, research, source audit, QA and detailed handoff](https://t90161376302.p.clickup-attachments.com/t90161376302/361d5f84-5121-59f1-b492-f4fb3c628992/MTRX-Field-Series-Resume.zip?view=open)
- [Detailed CONTINUE-HERE handoff](https://t90161376302.p.clickup-attachments.com/t90161376302/d4ea7e3f-0cef-5f7f-a4ee-ead92318893d/MTRX-Field-Series-Handoff.md?view=open)
- [Portable No.07 editorial edition](https://t90161376302.p.clickup-attachments.com/t90161376302/f4faae9a-e7bb-5cc5-9d51-bebab0b19cd6/07-design.html?view=open)

The resume ZIP is the authoritative copy of the uncommitted redesign. A browser upload attempt showed no push permission for that browser account. **The live No.07 guide has NOT been replaced by this edition.** This documentation commit does not deploy it. The connected GitHub integration can be used to publish the source patch in a subsequent step.

## New-chat starting prompt

Load the MTRX Field Guides skill, read this checkpoint and the detailed handoff in the resume pack. Continue from the existing files, not from scratch. No.07's editorial edition is built and locally QA-tested but not yet deployed. Keep the approved 4 + 2 + 1 direction, all 34 style entries, eight design dials and stable reader keys. Fetch current remote sources before applying the three-file source patch, verify the build and public page, then report. Ask before saving the proposed skill changes if they have not yet been approved.

## What belongs where

Repository: current source, research, decisions, coverage, QA and deployment checkpoint. Skill: reusable methodology and decision rules, not stale status. Memory: brief enduring preferences, not implementation details. Chat: discussion, not the only copy of project state.

The memory write was unavailable in this conversation. The new preference record is preserved here and in the handoff instead; do not claim it was saved to memory.

## Kevin's guide-by-guide feedback

- No.01: loved the clear purpose, relevance, clarity and coherent map.
- No.02: loved detailed, well-researched psychology/philosophy tailored to his curiosity and intellect.
- No.03: best work yet; preserve deep cases, questions, mechanisms, sources and the writer/business lenses.
- No.05: not started by Kevin; no quality verdict yet.
- No.06: early version boring, later improved. Avoid thin practical tips and debunking without substantive replacement explanations.
- No.07: a craft-learning guide. Basic principles, practical applications, comparison across many visual styles and actual making. Do not force the curiosity-led behavior-course sequence onto it.

## Approved No.07 direction

**4's chapter variety + 2's monograph reading discipline + 1's interactive atelier studies.**

Realistic imagery and authentic credited artwork. Vary chapter composition while retaining one book identity and consistent reader controls. Generated illustrations are clearly labelled, not presented as photos of named buildings or faithful historical reproductions.

Golden ratio: applications first, not 'is it real?'. Demonstrate proportions, layout and type scales. Keep the caution about universal beauty/retroactive overlays brief. Earlier Dalí, Tschichold and software-overlay claims were not all verified in the prior reply; verify before teaching them. The built preview uses explained arithmetic and the verified Fondation Le Corbusier Modulor source.

Minimal and bold are independent dials: density and visual emphasis. Eight teaching dials: Density, Volume, Structure, Temperature, Finish, Era, Source and Mood. They are a heuristic, not validated numerical measurements of style.

34 entries / 10 groups: Order (4), Quiet nature (3), Luxury (3), Raw (3), Loud (4), Rebel (3), Time travel (4), Place (2), Screens (3), Clothing (5). Quiet luxury intentionally has general-design and clothing versions. Distinguish movements, traditions, cultural concepts, interface effects and marketing labels. Quiet/warm/natural safari styling is a possible direction, not an industry law.

## Built and tested, pending deployment

- Seven original stops preserved, plus early-release 6.3 atlas: 8 of 78 planned stops, 18 checks.
- All 34 requested entries have visuals, cues, explanations, authentic examples to study, uses, limitations and sources.
- Eight persisted dials, presets, two-style comparison, filters and search.
- Golden-ratio application workbench under Part 2; full 2.11 is still forthcoming.
- Artwork Squint slider, grayscale, thirds grid and reset.
- Monograph reading layout, chapter-specific openers, editorial cover and reduced card clutter.
- Reader notes, highlights, progress, review tools and search preserved. Later chapters remain planned.

## Actual Squint defect

`assets/mtrx-scroll.js` injects an important `filter:none` rule, overriding the old toggle. The edition uses a more specific No.07-scoped rule driven by slider CSS variables. Chromium verified `blur(9px) grayscale(0)` and reset to none.

## Three source files to publish

1. `build/07/build.py`: small editorial-transform hook.
2. `build/07/editorial.py`: additive markup transform, visual studies, CSS, interactions, atlas and ratio workbench.
3. `build/07/editorial-data.json`: 34 researched records, fictional AI study images, embedded fallback font and license.

They are in `repo/` inside the resume ZIP. The ZIP also has a generated HTML and index, but let the existing CI pipeline generate those rather than pushing them manually. Fetch current remote files first. Existing pipeline: `.github/workflows/guide-07.yml` -> `build/07/run.py` -> build, quiz audit, lint, index sync, QA. The additions require only existing BeautifulSoup/Pillow dependencies.

Atlas 6.3 is currently appended by the editorial transform, not a standard `f6_3.py`. Refactor deliberately when writing full Part 6 to avoid duplicating the stop. The indexer depends on attribute serialization order and the exact last shared-review script tag; the transform preserves those.

## Stable storage

Slug `mtrx-field-series-07-design`; progress `mtrx-design-v1`; log `mtrx-design-log-v1`; new dials `mtrx-design-style-dials-v1`. Keep all original stop IDs. Hosted and local-file browser storage do not automatically migrate between origins, even with identical keys. Export notes/highlights before changing reading location.

The portable HTML inlines all images, fallback display font and shared reader scripts. Videos and optional device synchronization still need internet.

## QA and source evidence

The pack includes desktop 1440px and mobile 390px Chromium results, light/dark screenshots, quiz audit and reader tests. 8 stops, 18 rendered checks, 34 entries, 8 dials; no page exceptions or page-level overflow. Every inline image decoded. Clothing filter returns 5 entries. Notes, progress and dials persist after reload. Highlight restoration and Word export passed. Global search reveals filtered styles. Selecting ratio 1.5 produces 60/40. Compare changes to Techwear. No duplicate IDs or external script dependencies in the portable edition.

Final source audit: 38 unique URLs / 41 source references across the atlas. A second pass corrected 15 weak/inaccessible/mismatched entries. Use the final `research/style-atlas/styles.json`, not the first-pass sources. The full earlier No.07 research is also included.

## Proposed skill changes: NOT SAVED, awaiting agreement

1. Main skill: branch by purpose (technical map, curiosity survey, craft studio), replace stale status paragraphs with a repo-checkpoint rule.
2. Design System: engraving/cube becomes an adaptable default, not a universal mandate; preserve the No.07 editorial system and clear image provenance.
3. Curiosity/Unlearning: keep curiosity-led depth for behavior guides; allow application-led worked examples and visual making for craft guides; correct the stale No.07 not-built brief.

Preserve source verification, coverage audits, no Indian cinema examples, no em/en dashes, balanced quizzes, stable keys and real reader QA. Do not silently alter those standards.

Suggested safe tests after approval: plan a psychology week; teach golden-ratio applications for a safari page; continue No.07 without rewriting finished stops. No publishing in tests.

## Usage and cost limits

No exact billed input/output token totals, active-context percentage, cache usage or provider bill are available. Earlier chat content is partly summarized. Do not fabricate a full-chat token estimate.

Measured across seven saved guides, excluding scripts/styles/SVG/navigation: 173,753 readable words and 1,024,719 characters, approximately 256k prose tokens at characters/4. This includes output from multiple sessions and is NOT chat usage, billed output or total model work. Research, code, retries, repeated inputs, images and discarded drafts are excluded. Consult ClickUp's actual AI Usage page for account-level usage and credit spending.

# DESIGN-SYSTEM

## The look

- **The idea:** a 19th-century naturalist field guide. Each guide has a cover with a 3x3 "cube face" of nine plates, thumb-index tabs on the right edge (bottom bar on mobile), numbered stops or days, and "say it in the room" lines.
- **Palette:** Canvas #ECEAE4, Paper #F6F4EF, Ink #151515, Graphite #55586A, Steel #BCBFCC.
- **Accent colours:** Mars #ED691D (text #B3460D), Moss #697132 (text #525923), Gunmetal #2F3E46 and Jane #F4E3B2. Red #A44A3F is for warnings.
- **Colour by section:** each part or field gets one accent through `data-part` (1 = Mars, 2 = Gunmetal, 3 = Moss, 4 = Jane/Ink, 5 = Red, 6 = Graphite). In No. 02, psychology is Moss and philosophy is Gunmetal.
- **Type:** Tanker for display (Fontshare), falling back to Anton. Nunito Sans for body text. JetBrains Mono for labels. Reading text at least 16px, labels at least 14px.
- **Brand mark:** write "MTRX™".

## Components (all in the house CSS embedded in every guide)

- **Structure:** cover, `.part-head`, `article.mod` with `.mod-meta`, `.mod-title` and `.mod-why`.
- **Callouts:** `.room` (black "say it in the room" box), `.mtrx` (jane "in your world" box), `.warn`.
- **Content blocks:** `.specs`/`.spec` cards, `.stats`/`.stat`, `.tbl`, `.fig` (SVG card), `.plate` (image plus field marks), `.flips` (tap cards), `.board` (held up / mixed / failed scoreboard), `.trail` (roadmap), `.check` (quick check with `.opt` buttons), `.tryit`, `.widget`, `.drill`.
- **Grades:** `.grade.g-s` strong, `.grade.g-m` moderate, `.grade.g-h` weak or heuristic.
- **Reader and navigation:** `.thumbs` tabs, `.fp-side` field picker, `.fieldpick` in-page picker, `.rv[data-rv]` mode-tagged reviews, `.trk` track label, `.pvs`/`.pv` watch-ahead cards.
- **Day parts:** `.daybar`, `.qa` with `details.ans`, `.watch` (episode card), `.notes`, `.usecase`, `.further`.

## Diagram grammar

- **Format:** inline SVG with a viewBox 1000 to 1240 wide. The CSS gives it a minimum width and lets it scroll horizontally on phones.
- **Classes:** boxes `s-box`, `s-card`, `s-box-j` (jane), `s-box-a` (accent soft); text `s-t` (mono bold), `s-t-sm`, `s-t-b` (sans heavy), `s-t-d` (display); lines `s-line`, `s-line-m` (orange), `s-dash`, `march` (animated).
- **Arrowheads:** global markers `url(#ah)` and `url(#ahm)`.
- **Reach for these first:** a hierarchy tree, a 2x2 grid, a ladder of evidence, a flowchart, a three-lane timeline braid, a confound triangle, or 3 columns with a certainty meter.
- **Fit the text:** at 14px mono, allow about 8.5px per character. Size columns to the longest label, then check the screenshot for collisions.

## AI plate prompt (use it every time for consistency)

"A hand-coloured 19th-century copperplate engraving in the style of a naturalist field guide plate. Subject: <one concrete object or scene that carries the idea>. Fine crosshatching and stippling in sepia-black ink, with muted watercolour washes of ochre, moss green and burnt orange. Isolated and centred on a plain warm off-white paper background, generous empty space, no border, no frame, no text, no letters, no labels."

Objects only, no portraits. Post-process: white-balance the paper by dividing by the corner colour, resize to 720px webp at quality 74, make a 300px thumbnail for the cover cube. Plates sit on light cards with `mix-blend-mode: multiply`. Pick subjects that teach: Clever Hans for research methods, a black swan for falsification, a hare and tortoise for System 1/2.

## Kit

The kit source files (kit-base.css, kit-day.css, kit-render.py, kit-build.py, kit-app.js, kit-reader.css/js, kit-inject.py and examples) are attached to the ClickUp skill. In this repo the same CSS and JS are embedded in every guide; copy them from the newest build, `guides/05-long-game.html`. The reader kit adds notes (Word, Markdown, PDF export), a persistent highlighter that re-anchors by text, dark mode with light "island" cards, and search (⌕, / or Ctrl+K). Its slug comes from `<meta name="mtrx-slug">` if present, else the title.

## Build rules

- One HTML file. Images as base64. An inline `document.documentElement.className='js'` snippet in the head, and `.nojs-only` hints.
- No em or en dashes in the content. The build fails if it finds any.
- Answers live in `<details>`. Video cards are plain links.
- Load `../assets/mtrx-review.js` before the LAST `</body>`.

## QA checklist (headless Chromium, network blocked)

- No page errors; every inline script parses.
- Unique stop ids and anchors.
- Search: a term jumps to a centred match; a term in a filtered-out field switches back to Both.
- Screenshot after scrolling with a 1 to 1.5 s wait (shorter waits give blank frames that aren't real bugs).
- Screenshots of the cover, a diagram, one full stop, a plate and a table, at desktop and 390px mobile, in light and dark mode.
- A programmatic highlight survives a reload; a notes .doc download works.
- Look at every screenshot for overlapping SVG text, cramped plates and unreadable dark-mode islands before delivering.

# MTRX Field Guides (main skill)

Mirror of the ClickUp skill "MTRX Field Guides", 6 Oct 2026. It is written for an AI builder; "he" is Kevin. Keep this copy and the ClickUp copy in sync.

Kevin learns topics in the MTRX Field Series. So far there's No. 00 (learning operating system), No. 01 (software, stacks and AI, now with Stop 2.14, the developer's workbench), No. 02 (the mind: psychology and philosophy, Weeks 1 to 2 built) and No. 05 (the long game). Next up are cons and cults (insider view, 48 Laws of Power style), then sales and persuasion. Each guide is a single self-contained HTML file. It's never a ClickUp artifact.

## Who it's for, and what "good" means

- **The learner:** MSc in AI/ML, physics background, ex-maths teacher, founder of a web/AI agency in Ahmedabad. He learns action-first by pattern recognition and thinks like a generalist.
- **The goal:** to **talk like an insider**, not pass exams. That means knowing the map of the field, the 15 to 20 terms insiders actually use, what's robust vs contested vs debunked *today*, the key names and live debates, and one line he can say in a meeting.
- **The format:** about 20 minutes a day of self-reading. A free primary video series comes first (Crash Course when it exists), with an insider layer and further resources on top.
- **Tone:** sharp, warm, plain English, with analogies from his world (clients, callers, pricing, safari and dental niches). Use no em or en dashes anywhere, because they render badly for him. Use commas, colons or parentheses instead.
- **Token efficiency matters to him.** Reuse the kit, research in one parallel wave, and ship in weekly drops instead of one giant build. Later drops add one `weekN.py` content module and leave earlier weeks untouched.

## Workflow

1. **Scope in one pass.** Use what he has said. Defaults: 28 days (4 themed weeks of 7), one video per day, two related fields interleaved where possible. The first drop is the map, the full 28-day roadmap with every episode linked, and Week 1 fully built. Later drops add one week each. Ask only if the topic or primary series is unclear, and offer a recommended default.
2. **Research in one parallel wave.** Brief independent workers on: (a) a verified episode catalogue for each video series, (b) an insider layer for each field, and (c) further resources with verified YouTube IDs. Briefs and the per-topic checklist are in RESEARCH-PLAYBOOK.md. Learning-science rules are already distilled in LEARNING-RULES.md, so don't re-research them unless he asks.
3. **Curate the 20%.** Pick roughly a third of the episodes by insider value. Group them into weekly themes that build on each other, and alternate fields so each sharpens the other. End every week with a scoreboard or synthesis plus an optional "boss fight" transfer task.
4. **Write content as data, then render static HTML.** Fill one record per day (schema below) and render it. Static rendering matters: ClickUp's file preview blocks scripts, so videos, answers (as `<details>`), spaced reviews and maps must all work with JavaScript off. Interactivity is only an enhancement.
5. **Make the visuals do the teaching.** Each day: one hand-built SVG diagram (hierarchy, flowchart, 2x2, ladder or timeline) and one AI-generated plate in the house engraving style. The map: 3 to 4 diagrams (each field's family tree, a timeline braid, and where the fields meet). Every image must carry the day's idea, never decoration. The house style is in DESIGN-SYSTEM.md.
6. **Build, inject the reader kit, QA.** Build one file with images inlined as base64 webp (about 720px, quality 74; about 1MB per week of content is fine). Always include the reader kit, then QA headlessly on desktop, mobile and dark mode. The checklist is in DESIGN-SYSTEM.md.

## Required in every guide

- **Notes:** a side panel with autosave, a "+ Add heading: where I am" stamp, and export to Word (.doc), Markdown and PDF. Exports include every highlight, grouped by section.
- **Highlighter:** select text, then "Highlight" or "Highlight + note". Highlights persist across reloads and survive new content being added (they re-anchor by text).
- **Dark mode:** the ◐ button, remembered per browser. Diagrams, plates and callouts stay on light "island" cards.
- **Search:** a ⌕ Search button plus the / and Ctrl+K shortcuts. Full-text search across every stop, day, answer and glossary entry, with snippets, jump-to-result, opened answers and the match highlighted on the page.
- **Tabs on the side:** one thumb tab per part or week. Weeks not built yet still get a tab, showing that week's episodes as watch-ahead cards.
- **Field picker (two-field guides):** Both / Field A only / Field B only. It hides the other field's days, switches warm-up reviews to a single-field track, and adds a "track · day k of N" label.
- **Storage stays stable across drops:** keep the `mtrx-slug` meta tag fixed when the title changes, so notes and highlights carry over. Keep the progress key too.
- **The shared add-on:** every guide loads `../assets/mtrx-review.js` before the last `</body>` (see AGENTS.md).

## The 20-minute day (each element is backed by evidence; see LEARNING-RULES.md)

| Step | Time | What it contains |
|---|---|---|
| 1 Warm-up review | 2 min | 1 to 3 recall prompts from days n-1, n-3 and n-7. Day 1 gets a 1 to 5 self-rating baseline instead. |
| 2 Predict first | 2 min | One central question, 2 prequestions (one must be a tempting misconception) and 5 key terms to pre-train. |
| 3 Watch | about 10 min | One episode card linking to YouTube (thumbnail from i.ytimg.com), plus 3 "watch for" cues. Don't embed: YouTube embeds fail from local files. |
| 4 Insider layer | 3 min | Plate image with caption, 4 insider bullets (what the video got wrong or dated, the 2026 status, missing perspectives), 2 key names, the day's diagram, and one "say it in the room" line. |
| 5 Recall + use | 3 min | A 60-word "explain it, video closed" box with a model answer, 3 recall prompts with Got it / Missed it grading, and one transfer case from his business life. |
| Go further | optional | 3 links: one video, one book or reference, one podcast or article. |

**Day record fields:** n, field, title, episode (series, number, id, duration, title), image key and caption, hook, central question, 5 terms, 2 prequestions, 3 watch-for cues, the SVG and its caption, 4 insider bullets, 2 names, the room line, the explain prompt and model answer, 3 recall prompts and answers, a use case and answer, 3 further links.

## Kevin's standard (non-negotiable, Oct 2026)

- Zero known gaps: run COVERAGE-AUDIT.md BEFORE curating or writing. Never list topics from memory alone.
- Every stop has a "Try it · 5 min" hands-on task and a quick check; every guide has a visible coverage map module.
- Explain the thinking approach when delivering; state what the audit proves and does not prove.
- Expect iteration: quarterly re-audit, changelog, repair drops built from Kevin's weak-spot export.
- No. 00 (learning OS) is the reference for rhythm, principles and lenses; keep it updated when research moves.
- Lesson learned: No. 01 v1 missed cookies, analytics, CMS and serverless because it was built top-down from salience. Bottom-up from syllabi fixed it (119/320 to 320/320).
- Every stop opens with a real anomaly plus prediction and confidence, resolves promptly, cuts seductive details, and ends with a new question (CURIOSITY-UNLEARNING.md). Kevin keeps a question ledger. Verify every famous quote against a primary source.
- Market check (Oct 2026): generic tutor skills exist (Socratic mode, pre/post tests, spaced repetition, proficiency levels 1 to 5). Borrow per-concept proficiency levels and a persistent learner profile. Ours differs by syllabus-audited coverage, personalisation and offline HTML guides.
- Ask-split rule: one guide part per turn; save the skill before building.
- No. 05 "The long game" (built 5 Oct 2026): 12 lives in 4 themes over 12 weeks (Seneca, Marcus Aurelius, Franklin; Darwin, Feynman, Curie; Leonardo, Angelou, Ramanujan; Nightingale, Gandhi, Munger), each with one primary-source practice; 18 drills graded strong or moderate, covering 15 of 16 BCT Taxonomy v1 groups; a stack builder; a "what failed" list; 14 fake quotes flagged. Kevin's starter stack: If-then + Stack, Reappraise the Trigger, Evidence Ledger, weekly Plan Premortem.
- Quote rule proven: verification caught 3 errors in No. 05 drafts (the Marcus 8.47 paraphrase, a Hurston line credited to Angelou, Angelou's hotel-room wording). Fetch the primary page for every quote that goes in bold.

## Sub-skills in this folder

- RESEARCH-PLAYBOOK.md: worker briefs, verification rules, the per-topic insider checklist.
- DESIGN-SYSTEM.md: the MTRX look, components, SVG grammar, image prompt, reader kit, build and QA checklist.
- LEARNING-RULES.md: ranked, evidence-graded rules and what each one changes on the page.
- COVERAGE-AUDIT.md: gap-proofing protocol.
- CURIOSITY-UNLEARNING.md: curiosity rules, unlearning protocol, any-age evidence, self-help verdicts.
- DARK-TOPICS.md: how to teach cons, cults, power and persuasion without making a fraud manual.

# COVERAGE-AUDIT: gap-proof every guide before writing prose

Why this exists: Field Guide No. 01 v1 was built top-down from "what impresses in a room" and missed cookies, sessions, analytics, CMS, email auth and serverless. The audit found only 119 of 320 must-know concepts explained. Listing from memory is the broken step (experts omit most tacit knowledge: Sullivan 2014, cognitive task analysis). Kevin's standard: zero known gaps, iterate, show the thinking.

## Protocol (every new guide and every quarterly re-audit)

1. **Boundary and target performances:** what Kevin must recognise, explain, decide, build and teach. Name the "room" (No. 01: a senior web-agency lead who builds with AI, not a CS graduate).
2. **Triangulate 5+ independent source families:** a handbook or canonical text; 2 syllabi; a job or certification blueprint (O*NET, ESCO, SFIA, cert outlines); a corpus or glossary; primary sources plus a recent review; practitioners; error sources (forums, support threads, victim reports).
3. **Inventory** as JSONL, one concept per line: concept, category, definition, sources[], tier MUST/SHOULD/AWARE, new_2024_26, note. The No. 01 inventory had 380 concepts from 14 sources.
4. **Run the 13 lenses:** boundary, words, things, mechanisms, procedures, decisions, tools, failure, numbers, money, rules, people and history, frontier. Any lens with no inventory rows is a gap.
5. **Mark gateway concepts,** build a prerequisite graph, and write tests before lessons (distractors from real misconceptions).
6. **Five omission passes:** boundary, counterexample, error, practice (job tasks), transfer.
7. **Coverage check in the body text, not the glossary,** with an alias map. Target: MUST 100%, SHOULD 100%, AWARE mentioned. Glossary-only counts as a gap.
8. **Ship a visible coverage map** in the guide (before/after per area, and what it proves and doesn't).
9. **Every stop:** mechanism, cost, where it breaks, room line, quick check, "Try it · 5 min" hands-on box.
10. **Date-stamp fast-moving facts;** re-audit quarterly (No. 01 next: Jan 2027). Keep a changelog.

Honesty rule: coverage proves the guide covers the sources, not that Kevin understands, and not that zero unknown unknowns remain. Say so in the guide.

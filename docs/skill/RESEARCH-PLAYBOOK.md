# RESEARCH-PLAYBOOK

Run all of this in one parallel wave, then read the outputs selectively: list each file's headings first, then pull only the sections needed for the current drop.

## Worker briefs (one each, in parallel)

Every brief includes Kevin's profile, today's date, the output file name and shape, and when to stop.

**1. Video catalogue (one per series), as a comprehensive collection job.**

- The official playlist ID, plus every episode in order: number, exact title, YouTube ID, duration (mm:ss) and date.
- Verify every ID against `https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=ID&format=json`, check the title matches, and record the method used.
- Leave durations null rather than guessing.
- Also 8 to 12 verified complementary short videos from other channels, including non-Western perspectives where relevant.
- Output JSON: `series{title,host,year,playlist_id,episode_count}`, `episodes[{n,title,id,duration,date,verified,summary}]`, `extras[{title,channel,id,duration,topic,why,verified}]`.

**2. Insider layer (one per field), as a thorough research job, 5,000 to 8,000 words with source URLs.** Ask for:

1. A field map: branches, schools and how they nest.
2. A dated timeline of 15 to 30 items.
3. A robust / mixed / failed audit of the famous claims that intro courses teach, each with its source.
4. Current debates and frontiers, date-stamped.
5. 25 to 35 insider terms, with how insiders actually use them.
6. 15 to 25 key people with one line each.
7. Ranked further resources (books, free courses, podcasts, sites, verified YouTube IDs).
8. One compact entry per episode topic: core idea, 2026 update, 2 names, 3 terms, a "say it in the room" line, a business or life use, one resource.
9. Ten diagram ideas.
10. What professionals actually believe (surveys, if any exist).

**3. Learning science:** skip; it's distilled in LEARNING-RULES.md.

## Insider checklist (every topic)

- **The map before the details:** a hierarchy of 5 to 9 nodes per field.
- **Status labels on every famous claim:** held up / mixed / failed, with the date checked. For psychology, flag WEIRD samples and replication. For philosophy, separate textual interpretation from survey facts.
- **Missing perspectives:** Crash Course is Western-centric, so add the Indian and Chinese parallels Kevin will care about.
- **Outsider mistakes:** turn each common one into a prequestion.
- **The practical layer:** one realistic use per day (agency, clients, callers, pricing, founders). Don't force it.
- **Link hygiene:** verified IDs only, primary or reputable sources, no snippet-only evidence, no invented quotes.

## Lessons from past builds

- Crash Course thumbnails: `https://i.ytimg.com/vi/ID/hqdefault.jpg`.
- Normalise titles with the suffix ": Crash Course X #n", and replace any em dashes found in source titles.
- Research workers can't always reach oEmbed live, so ask them to state their verification method.

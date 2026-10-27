#!/usr/bin/env python3
"""Keep the No. 02 card on the library page in step with the guide: counts the day
articles actually built and rewrites only the "02" entry of index.html's G array.
Usage: python build/02/index_card.py guides/02-mind.html index.html"""
import json, re, sys

WEEKS = [('How to think', range(1, 8)), ("What's real, and how do we know?", range(8, 15)),
         ('Self, will and the crowd', range(15, 22)), ('How to live', range(22, 29))]


def main(guide, index):
    g = open(guide, encoding='utf-8').read()
    built = {int(n) for n in re.findall(r'<article class="mod day" id="d(\d+)"', g)}
    parts = [[t, [str(n) for n in r if n in built]] for t, r in WEEKS]
    done = all(n in built for n in range(1, 29))
    nweeks = sum(1 for t, r in WEEKS if all(n in built for n in r))
    time = 'Complete · 28 days · 20 min a day' if done else 'Weeks 1 to %d built · %d of 28 days' % (nweeks, len(built))
    s = open(index, encoding='utf-8').read()
    m = re.search(r'var G=(\[.*?\]);\nvar A=', s, re.S)
    if not m:
        raise SystemExit('G array not found in index.html')
    G = json.loads(m.group(1))
    e = next((x for x in G if x.get('n') == '02'), None)
    if e is None:
        raise SystemExit('no 02 entry in G')
    e['time'], e['parts'], e['st'] = time, parts, ('ready' if done else 'partial')
    new = json.dumps(G, ensure_ascii=False, separators=(',', ':'))
    out = s[:m.start(1)] + new + s[m.end(1):]
    if done:
        out = out.replace("why='Next main track: one day at a time, Weeks 1 to 2 are ready.';",
                          "why='Next main track: one day at a time, all four weeks are ready.';")
    if out != s:
        open(index, 'w', encoding='utf-8').write(out)
        print('index card 02 updated: %s' % time)
    else:
        print('index card 02 already current')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

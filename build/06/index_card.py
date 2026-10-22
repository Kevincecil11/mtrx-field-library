#!/usr/bin/env python3
"""Keep the No. 06 card on the library page (index.html) in step with the guide.
Reads the built guide's stop order and rewrites only the "06" entry in the
page's G array: its time line and its parts list. Run by build/run.py.

Usage: python build/06/index_card.py guides/06-read-the-room.html index.html
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p2_file1 as F1  # noqa: E402

FILES = [F1]


def main(guide, index):
    g = open(guide, encoding='utf-8').read()
    mods = []
    for m in re.findall(r'<button class="done[^"]*" data-mod="([^"]+)"', g):
        if m not in mods:
            mods.append(m)
    built = {s['id']: F.FILE['n'] for F in FILES for s in F.STOPS}
    parts = [['Start here', [m for m in mods if m.startswith('0.')]],
             ['Read the room', [m for m in mods if m.startswith('1.')]]]
    for f in F1.INTRO['files']:
        parts.append(['Part II · File %d · %s' % (f['n'], f['title']), [m for m in mods if built.get(m) == f['n']]])
    p2 = sum(1 for m in mods if m in built)
    nfiles = len({built[m] for m in mods if m in built})
    time = 'Part I built · Part II: %d of 5 files, %d stops · daily 20 min' % (nfiles, p2)
    s = open(index, encoding='utf-8').read()
    m = re.search(r'var G=(\[.*?\]);\nvar A=', s, re.S)
    if not m:
        raise SystemExit('G array not found in index.html')
    G = json.loads(m.group(1))
    e = next((x for x in G if x.get('n') == '06'), None)
    if e is None:
        raise SystemExit('no 06 entry in G')
    e['time'], e['parts'], e['st'] = time, parts, 'partial'
    new = json.dumps(G, ensure_ascii=False, separators=(',', ':'))
    if new != m.group(1):
        s = s[:m.start(1)] + new + s[m.end(1):]
        open(index, 'w', encoding='utf-8').write(s)
        print('index card 06 updated: %s; %d parts' % (time, len(parts)))
    else:
        print('index card 06 already current')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

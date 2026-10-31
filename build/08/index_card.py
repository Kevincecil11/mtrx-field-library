#!/usr/bin/env python3
"""Keep the No. 08 card on the library page in step with the guide.
Usage: python build/08/index_card.py guides/08-screenwriting.html index.html"""
import importlib.util, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main(guide, index):
    spec = importlib.util.spec_from_file_location('front08', os.path.join(HERE, 'front.py'))
    F = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(F)
    g = open(guide, encoding='utf-8').read()
    built = {int(n) for n in re.findall(r'<article class="mod day" id="d(\d+)"', g)}
    parts = [[F.WEEKS[w][0], [str(n) for n in range(7 * w - 6, 7 * w + 1) if n in built]] for w in range(1, 5)]
    done = all(n in built for n in range(1, 29))
    time = 'Complete \u00b7 28 days \u00b7 20 min a day' if done else '%d of 28 days built' % len(built)
    s = open(index, encoding='utf-8').read()
    m = re.search(r'var G=(\[.*?\]);\nvar A=', s, re.S)
    if not m:
        raise SystemExit('G array not found in index.html')
    G = json.loads(m.group(1))
    e = dict(n='08', t='Screenwriting', sub='Story theory and the craft of the screenplay, 20 minutes a day, with a daily drill that builds your own 5-page short.',
             time=time, file='08-screenwriting.html', key='mtrx-screen-v1', acc='red', st='ready' if done else 'partial', day=True, parts=parts)
    i = next((k for k, x in enumerate(G) if x.get('n') == '08'), None)
    if i is None:
        i = next((k for k, x in enumerate(G) if x.get('n') > '08'), len(G))
        G.insert(i, e)
    else:
        G[i] = e
    new = json.dumps(G, ensure_ascii=False, separators=(',', ':'))
    out = s[:m.start(1)] + new + s[m.end(1):]
    if out != s:
        open(index, 'w', encoding='utf-8').write(out)
        print('index card 08 updated: %s' % time)
    else:
        print('index card 08 already current')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

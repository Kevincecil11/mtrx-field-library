#!/usr/bin/env python3
"""Sync the No. 03 card on the library home and keep the No. 07 Design card (in development) up to date.
python build/03/index_card.py guides/03-cons-and-cults.html index.html"""
import json, re, sys

guide, idx = sys.argv[1], sys.argv[2]
g = open(guide, encoding='utf-8').read()
s = open(idx, encoding='utf-8').read()
m = re.search(r'(var G=)(\[.*?\])(;\s*\nvar A=)', s, re.S)
if not m:
    sys.exit('G array not found')
G = json.loads(m.group(2))
parts, built = [], 0
for sm in re.finditer(r'<section class="part" id="s\d+"[^>]*data-title="([^"]*)"[^>]*>(.*?)</section>', g, re.S):
    ids = re.findall(r'<button class="done" data-mod="([^"]+)"', sm.group(2))
    parts.append([sm.group(1).replace('&amp;', '&'), ids])
    built += len(ids)
total = sum(len(re.findall(r'<li><a href="#', x)) for x in re.findall(r'<ol class="stops">(.*?)</ol>', g, re.S))
e03 = next(x for x in G if x['n'] == '03')
e03.update(t='Cons and cults', sub='Why cults work, how cons are built, and the writer\'s room behind both. Question-led, evidence-graded.',
           time='%d stops built of %d planned \u00b7 7 files \u00b7 20 min a day' % (built, total + 2), file='03-cons-and-cults.html',
           key='mtrx-cons-v1', acc='red', st='partial', day=False, parts=parts)
D07 = dict(t='Design', sub='Type first: how to choose and pair fonts. Then colour (Sanzo Wada\'s combinations), composition, minimal versus bold, brand identity, and the philosophies of Apple, Jobs and Ive, painters like Caravaggio and Picasso, directors like Kubrick and Spielberg, and great architects.',
           time='In development \u00b7 to be discussed', file='', key=None, acc='moss', st='dev', day=False, parts=[])
e07 = next((x for x in G if x['n'] == '07'), None)
if e07 is None:
    i = next((k for k, x in enumerate(G) if x['n'] > '07'), len(G))
    G.insert(i, dict(n='07', **D07))
elif e07.get('st') == 'dev':
    e07.update(D07)
out = s[:m.start(2)] + json.dumps(G, ensure_ascii=False, separators=(',', ':')) + s[m.end(2):]
open(idx, 'w', encoding='utf-8').write(out)
print('index: No. 03 has %d built stops in %d parts; No. 07 card up to date' % (built, len(parts)))

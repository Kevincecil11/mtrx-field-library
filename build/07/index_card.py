#!/usr/bin/env python3
"""Sync the No. 07 card on the library home: python build/07/index_card.py guides/07-design.html index.html"""
import html, json, re, sys

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
    parts.append([html.unescape(sm.group(1)), ids])
    built += len(ids)
start = len(parts[0][1]) if parts and parts[0][0] == 'Start here' else 0
total = sum(len(re.findall(r'<li><a href="#', x)) for x in re.findall(r'<ol class="stops">(.*?)</ol>', g, re.S)) + start
e = dict(n='07', t='Design and taste',
         sub='How designers see, decide and make: the brief, attention, value, principles, type, colour, composition, the makers, brand, aesthetics and story. Question-led, evidence-graded, with a director\'s eye in every stop.',
         time='%d stops built of %d planned \u00b7 10 parts \u00b7 20 min a day' % (built, total), file='07-design.html',
         key='mtrx-design-v1', acc='moss', st='ready' if built >= total else 'partial', day=False, parts=parts)
i = next((k for k, x in enumerate(G) if x['n'] == '07'), None)
if i is None:
    i = next((k for k, x in enumerate(G) if x['n'] > '07'), len(G))
    G.insert(i, e)
else:
    G[i] = e
out = s[:m.start(2)] + json.dumps(G, ensure_ascii=False, separators=(',', ':')) + s[m.end(2):]
open(idx, 'w', encoding='utf-8').write(out)
print('index: No. 07 has %d built stops of %d in %d parts' % (built, total, len(parts)))

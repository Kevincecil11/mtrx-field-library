#!/usr/bin/env python3
"""No. 02 The mind: splice Weeks 3 and 4 into the live guide.
python build/02/build.py guides/02-mind.html out.html

Days 1 to 14 stay byte for byte (checked by hash). Weeks 3 and 4 are rendered from the
content modules w3a.py, w3b.py, w4a.py, w4b.py with render02.py and replace the old
watch-ahead sections s4 and s5 between <!-- mtrx:w3 --> / <!-- mtrx:w4 --> markers.
Warm-up reviews reuse the recall prompts already in the guide for days 1 to 14.
Plate images are Wikimedia Commons files, fetched once in CI and cached in build/out/02-img/
(committed); a missing image renders as a caption card, never a build failure.
"""
import base64, hashlib, html, importlib.util, io, json, os, re, sys, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import render02 as R  # noqa: E402

CACHE = os.path.join(ROOT, 'build', 'out', '02-img')
UA = 'MTRX-Field-Library-build/1.0 (+https://github.com/Kevincecil11/mtrx-field-library)'
MODS = ['w3a', 'w3b', 'w4a', 'w4b']
WEEKS = {3: ('s4', 'w3', 'Week 3 \u00b7 7 days \u00b7 about 20 min each', range(15, 22)),
         4: ('s5', 'w4', 'Week 4 \u00b7 7 days \u00b7 about 20 min each', range(22, 29))}
LOG = []


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _get(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read()


def image(key, spec):
    """data URI for a Commons file, cached; '' if unavailable."""
    os.makedirs(CACHE, exist_ok=True)
    out = os.path.join(CACHE, key + '.webp')
    meta = os.path.join(CACHE, key + '.json')
    if not (os.path.exists(out) and os.path.exists(meta) and json.load(open(meta)).get('file') == spec['file']):
        if os.environ.get('MTRX_OFFLINE'):
            return ''
        try:
            api = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(
                {'action': 'query', 'titles': spec['file'], 'prop': 'imageinfo', 'iiprop': 'url', 'iiurlwidth': 900, 'format': 'json'})
            page = next(iter(json.loads(_get(api).decode())['query']['pages'].values()))
            ii = page['imageinfo'][0]
            raw = _get(ii.get('thumburl') or ii['url'])
            from PIL import Image
            im = Image.open(io.BytesIO(raw)).convert('RGB')
            if im.width > 720:
                im = im.resize((720, round(im.height * 720 / im.width)), Image.LANCZOS)
            im.save(out, 'WEBP', quality=72, method=6)
            json.dump({'file': spec['file']}, open(meta, 'w'))
        except Exception as e:  # noqa: BLE001
            LOG.append('IMAGE %s not fetched: %s' % (key, str(e)[:120]))
            return ''
    return 'data:image/webp;base64,' + base64.b64encode(open(out, 'rb').read()).decode('ascii')


def old_recall(s):
    """Recall prompts (q_html, a_html) for days already in the guide, from each day's own Step 5."""
    rec, fields = {}, {}
    for m in re.finditer(r'<article class="mod day" id="d(\d+)" data-mod="\d+" data-part="\d+" data-f="(\w+)">(.*?)</article>', s, re.S):
        n = int(m.group(1))
        fields[n] = m.group(2)
        qs = re.findall(r'<div class="qa" data-id="d%dr(\d)"><p class="q">(.*?)</p><details class="ans"><summary>Show answer</summary>'
                        r'<div class="a">(.*?)</div></details>' % n, m.group(3), re.S)
        got = {}
        for i, q, a in qs:
            if '<small>' not in q and int(i) not in got:
                got[int(i)] = (q, a)
        if got:
            rec[n] = [got[i] for i in sorted(got)]
    return rec, fields


def first14(s):
    i = s.find('<section class="part" id="s2"')
    j = s.find('<section class="part" id="s4"')
    k = s.find('<!-- mtrx:w3 -->')
    j = min(x for x in (j, k) if x > 0)
    return s[i:j]


def main(src, dst):
    s = open(src, encoding='utf-8').read()
    s = s.replace('Next drop: Week 3, Self, will and the crowd.', 'Tomorrow: Day 15. Same time, same cue.')
    keep = hashlib.sha256(first14(s).encode()).hexdigest()
    mods = [load(n) for n in MODS]
    days = sorted([d for m in mods for d in m.DAYS], key=lambda d: d['n'])
    images = {}
    for m in mods:
        images.update(getattr(m, 'IMAGES', {}))
    tie = {21: mods[1].TIEUP, 28: mods[3].TIEUP}
    recall, fields = old_recall(s)
    LOG.append('reused recall prompts from %d existing days' % len(recall))
    for d in days:
        recall[d['n']] = [(html.escape(q), html.escape(a)) for q, a in d['recall']]
        fields[d['n']] = d['f']
    total = {f: sum(1 for v in fields.values() if v == f) for f in ('psy', 'phi')}

    def track(n):
        f = fields[n]
        return sorted(k for k, v in fields.items() if v == f).index(n) + 1, total[f]
    uris = {}

    def img(key):
        if key not in uris:
            uris[key] = image(key, images[key]) if key in images else ''
        return uris[key]
    for wk, (sid, mark, kicker, rng) in WEEKS.items():
        arts = []
        for d in [x for x in days if x['n'] in rng]:
            extra = ''
            if d['n'] in tie:
                t = tie[d['n']]
                extra = R.tieup(wk, t['title'], t['intro'], t['rows'], t['boss'], t['calib'])
            nxt = None
            if d['n'] == 28:
                nxt = 'You finished all 28 days. Next: the library and glossary below, then your spaced reviews keep it alive.'
            arts.append(R.day(d, dict(recall=recall, fields=fields, img=img, track=track, last=28, extra_html=extra, next_line=nxt)))
        b, e = '<!-- mtrx:%s -->' % mark, '<!-- /mtrx:%s -->' % mark
        if b in s:
            i, j = s.index(b), s.index(e) + len(e)
            sec = s[i + len(b):s.index(e)]
        else:
            i = s.find('<section class="part" id="%s"' % sid)
            j = s.find('</section>', i) + len('</section>')
            sec = s[i:j]
        head_end = sec.find('<div class="wrap">', sec.find('</div></div>'))
        head = sec[:head_end]
        head = re.sub(r'<div class="kicker">.*?</div>', '<div class="kicker">%s</div>' % kicker, head, count=1, flags=re.S)
        block = head + '<div class="wrap">\n' + '\n'.join(arts) + '\n</div>\n</section>'
        s = s[:i] + b + block + e + s[j:]
        LOG.append('week %d: %d days into %s' % (wk, len(arts), sid))
    css = ('<style id="mtrx-w34-css">.day .notes,.day .notes li,.day .notes figcaption,.day .further a,.day .usecase,.day .qa'
           '{overflow-wrap:anywhere;min-width:0}.day .notes>*{min-width:0}.plate-missing{padding:18px;min-height:0}</style>')
    if '<style id="mtrx-w34-css">' not in s:
        s = s.replace('</head>', css + '</head>', 1)
    # Roadmap: every day now links inside the guide.
    s, n = re.subn(r'(<li data-d="(\d+)" data-f="\w+"><a href=")https://www\.youtube\.com/watch\?v=[\w-]+(" target="_blank" rel="noopener")',
                   lambda m: m.group(1) + '#d' + m.group(2) + '"' if int(m.group(2)) <= 28 else m.group(0), s)
    LOG.append('roadmap links pointed inside: %d' % n)
    # Glossary: add the new terms, keep alphabetical order.
    gi = s.find('<div class="gloss" id="gloss">')
    if gi >= 0:
        start = gi + len('<div class="gloss" id="gloss">')
        ents = []
        p = start
        pat = re.compile(r'<div class="g"><b>(.*?)</b><em>(.*?)</em><p>(.*?)</p></div>', re.S)
        while True:
            m = pat.match(s, p)
            if not m:
                break
            ents.append((html.unescape(m.group(1)), m.group(2), m.group(3)))
            p = m.end()
        seen = {e[0].lower() for e in ents}
        added = 0
        for m in mods:
            for t, d, c in getattr(m, 'GLOSS', []):
                if t.lower() not in seen:
                    ents.append((t, c, html.escape(d)))
                    seen.add(t.lower())
                    added += 1
        ents.sort(key=lambda e: e[0].lower())
        s = s[:start] + ''.join('<div class="g"><b>%s</b><em>%s</em><p>%s</p></div>' % (html.escape(t), c, d) for t, c, d in ents) + s[p:]
        LOG.append('glossary: %d terms (%d new)' % (len(ents), added))
    swaps = [('Next drop: Week 3, Self, will and the crowd.', 'Tomorrow: Day 15. Same time, same cue.'),
             ('Weeks 1 and 2 are fully built. Weeks 3 and 4 link straight to the episodes, so you can watch ahead while the next drops are built.',
              'All four weeks are fully built: every day has the review, predict, insider layer, diagram and recall.'),
             ('28 days \u00b7 2 fields \u00b7 this drop: Weeks 1-2 + the full map', '28 days \u00b7 2 fields \u00b7 complete: all four weeks + the full map'),
             ("c.href='#w3';c.textContent='Weeks 1-2 done. Watch ahead: Week 3 \u2192';", "c.href='#s6';c.textContent='All 28 days done. Library and glossary \u2192';")]
    for a_, b_ in swaps:
        if a_ in s:
            s = s.replace(a_, b_)
            LOG.append('updated: %s' % a_[:50])
        elif b_ not in s:
            LOG.append('NOT FOUND: %s' % a_[:50])
    if hashlib.sha256(first14(s).encode()).hexdigest() != keep:
        raise SystemExit('Weeks 1 and 2 changed unexpectedly: refusing to write')
    body = re.sub(r'<(script|style)\b.*?</\1>', ' ', s, flags=re.S)
    if '\u2014' in body or '\u2013' in body:
        raise SystemExit('dash found in content')
    fetched = sum(1 for v in uris.values() if v)
    LOG.append('images: %d of %d plates inlined' % (fetched, len(uris)))
    open(dst, 'w', encoding='utf-8').write(s)
    LOG.append('wrote %s (%d bytes)' % (dst, len(s)))
    print('\n'.join(LOG))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

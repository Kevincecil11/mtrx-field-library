#!/usr/bin/env python3
"""No. 04 Sales and persuasion: build the whole guide from small sources.
python build/04/build.py guides/02-mind.html out.html

The shell (fonts, CSS, reader kit, notes, highlighter, search, dark mode, week tabs and the
field picker) is taken from No. 02, which Kevin asked No. 04 to match. Everything inside
<div class="site"> is rendered here from front.py (cover, how-to, maps, coverage, questions,
library) and the day modules w1a ... w4b (28 days, render04.day). Internal field codes stay
psy/phi because the shared CSS and picker use them: per -> psy (Persuasion), sal -> phi (Sales).
Plates are Wikimedia Commons files fetched in CI and cached in build/out/04-img (720px webp);
a missing image renders as a caption card, never a build failure.
"""
import base64, html, importlib.util, io, json, os, re, sys, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import render04 as R  # noqa: E402

E = html.escape
CACHE = os.path.join(ROOT, 'build', 'out', '04-img')
UA = 'MTRX-Field-Library-build/1.0 (+https://github.com/Kevincecil11/mtrx-field-library)'
MODS = ['w1a', 'w1b', 'w2a', 'w2b', 'w3a', 'w3b', 'w4a', 'w4b']
CODE = {'per': 'psy', 'sal': 'phi'}
KEY, SLUG = 'mtrx-sales-v1', 'mtrx-field-guide-to-sales-and-persuasion'
TITLE = 'MTRX\u2122 Field Guide to Sales and Persuasion \u00b7 28 days'
DESC = ('Sales and persuasion in 28 days, 20 minutes a day: the science of influence and the craft of selling, '
        'one free video a day plus an insider layer checked October 2026. Prepared for Kevin Cecil.')
SEC = {1: ('s2', '2'), 2: ('s3', '3'), 3: ('s4', '4'), 4: ('s5', '1')}
LOG = []
CSS = ('<style id="mtrx-04-css">.seg{margin:10px 0 0;font-size:16px;line-height:1.5}'
       'details.deeper{margin:20px 0 0;background:var(--paper);border-left:4px solid var(--moss);padding:12px 18px;border-radius:12px}'
       'details.deeper summary{cursor:pointer;font:700 14px/1.4 var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--moss)}'
       '.deeper-b p{max-width:68ch;overflow-wrap:anywhere}.qbank{padding-left:20px}.qbank li{margin:8px 0}.qbank a{font:700 13px var(--mono);margin-left:6px;white-space:nowrap}'
       '.day .notes,.day .notes li,.day .notes figcaption,.day .further a,.day .usecase,.day .qa,.deeper-b{overflow-wrap:anywhere;min-width:0}'
       '@media (max-width:560px){.cover-title{font-size:clamp(40px,12.5vw,64px)}.cover>div{min-width:0}}.day .notes>*{min-width:0}.plate-missing{padding:18px;min-height:0}</style>')


def load(name):
    spec = importlib.util.spec_from_file_location('c04_' + name, os.path.join(HERE, name + '.py'))
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
    out, meta = os.path.join(CACHE, key + '.webp'), os.path.join(CACHE, key + '.json')
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


def fp(cls='fieldpick'):
    return ('<div class="%s js-only" role="group" aria-label="Choose what to learn"><button type="button" data-field="both">Both fields</button>'
            '<button type="button" data-field="psy">Persuasion only</button><button type="button" data-field="phi">Sales only</button></div>') % cls


def part_head(kicker, title, promise):
    return ('<div class="part-head"><div class="wrap"> <div class="kicker">%s</div> <h2 class="part-title">%s</h2> '
            '<p class="part-promise">%s</p> </div></div>') % (kicker, E(title), E(promise))


def main(src, dst):
    shell = open(src, encoding='utf-8').read()
    F = load('front')
    mods = [load(n) for n in MODS]
    days = sorted([dict(d, f=CODE[d['f']]) for m in mods for d in m.DAYS], key=lambda d: d['n'])
    if [d['n'] for d in days] != list(range(1, 29)):
        raise SystemExit('days must be exactly 1 to 28, got %s' % [d['n'] for d in days])
    images = {}
    for m in mods:
        images.update(getattr(m, 'IMAGES', {}))
    ties = {}
    for m in mods:
        if hasattr(m, 'TIEUP'):
            ties[max(d['n'] for d in m.DAYS)] = m.TIEUP
    LOG.append('days 1 to 28 loaded; tie-ups after days %s' % sorted(ties))
    # ---------- head ----------
    head = shell[:shell.find('</head>')]
    head = re.sub(r'<title>.*?</title>', '<title>%s</title>' % TITLE, head, count=1, flags=re.S)
    head = re.sub(r'<meta name="mtrx-slug" content="[^"]*">', '<meta name="mtrx-slug" content="%s">' % SLUG, head, count=1)
    if '<meta name="description"' in head:
        head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % E(DESC, quote=True), head, count=1)
    else:
        head = head.replace('<meta name="mtrx-slug"', '<meta name="description" content="%s">\n<meta name="mtrx-slug"' % E(DESC, quote=True), 1)
    head = head.replace('mtrx-mind-v1', KEY)
    head = head.replace('<style id="mtrx-w34-css">', '<style id="mtrx-w34-css-off" media="not all">')
    head += CSS
    # ---------- body prefix: arrowheads, scrollbar, tabs + side field picker ----------
    b0 = shell.find('<body')
    prefix = shell[b0:shell.find('<div class="site">', b0)]
    prefix = re.sub(r'<div class="fp-side js-only".*?</div>', '<div class="fp-side js-only" role="group" aria-label="Learn one field">'
                    '<button type="button" data-field="both" title="Both fields">Both</button>'
                    '<button type="button" data-field="psy" title="Persuasion only">Pers</button>'
                    '<button type="button" data-field="phi" title="Sales only">Sales</button></div>', prefix, count=1, flags=re.S)
    tail = shell[shell.find('</footer>') + len('</footer>'):]
    nkey = tail.count('mtrx-mind-v1')
    tail = tail.replace('mtrx-mind-v1', KEY)
    LOG.append('progress key replaced %d times in the tail' % nkey)
    uris = {}

    def img(key):
        if key not in uris:
            uris[key] = image(key, images[key]) if key in images else ''
        return uris[key]
    # ---------- cover ----------
    C = F.COVER
    cube = ''.join('<a class="sp" href="#d%d"><img src="%s" alt=""><b>Day %d</b></a>' % (d['n'], img(d['img']), d['n']) for d in days[:9] if img(d['img']))
    cover = ('<header class="wrap cover" id="top"> <div> <div class="kicker">MTRX\u2122 Field Series \u00b7 No. 04 \u00b7 October 2026</div> '
             '<h1 class="cover-title">%s</h1> <p class="cover-sub">%s</p> <ul class="verbs">%s</ul> '
             '<p class="prepared">Prepared for <b>Kevin Cecil</b><br>28 days \u00b7 2 fields \u00b7 complete: all four weeks + the full map<br>'
             'One free video a day \u00b7 facts checked 27 October 2026</p> <a class="btn btn-a" id="continue" href="#d1">Start Day 1 \u2193</a> '
             '<a class="btn btn-ghost" href="#how" style="margin-left:8px">How it works</a> </div> <div><nav class="cube" aria-label="The first plates">%s</nav>'
             '<p class="cube-cap">%s</p></div> </header>') % (C['title_html'], E(C['sub']), ''.join('<li>%s</li>' % E(v.capitalize()) for v in C['verbs']),
                                                              cube, E(C['cube_caption']))
    # ---------- s0: how it works ----------
    H = F.HOW
    i = shell.find('<article class="mod" id="how">')
    loop = re.search(r'<figure class="fig">.*?</figure>', shell[i:shell.find('</article>', i)], re.S).group(0).replace('one Crash Course', 'one video')
    specs = ''.join('<div class="spec"><div class="spec-name">%s <small>%s</small></div><p class="spec-def">%s</p></div>' % (E(a), E(b), E(c)) for a, b, c in H['specs'])
    s0 = ('<section class="part" id="s0" data-part="0" data-sec="0"><div class="wrap"> <article class="mod" id="how"> <div class="mod-meta">Before Day 1 <span class="t">3 min</span></div> '
          '<h2 class="mod-title">How 20 minutes beats an hour</h2> <p class="mod-why">%s</p> %s <div class="specs">%s</div> <div class="mtrx"><p><b>Your cue:</b> %s</p></div> '
          '<h3>Learn one field, or both</h3> <p>%s</p> %s <p class="nojs-note nojs-only"><b>Tip:</b> you are viewing this in a preview that turns off the interactive parts. '
          'Download the file and open it in Chrome to save progress, grade yourself, and keep your notes and highlights.</p> </article> </div></section>') % (
        E(H['why']), loop, specs, E(H['cue']), E(H['field_note']), fp())
    # ---------- s1: the map ----------
    arts = []
    for M in F.MAPS:
        if M['id'] == 'coverage':
            continue
        arts.append('<article class="mod" id="%s"> <div class="mod-meta">%s</div><h2 class="mod-title">%s</h2> <p class="mod-why">%s</p> %s %s </article>' % (
            M['id'], E(M['meta']), E(M['title']), E(M['why']), R.fig(M['svg'], M['figcap']), M.get('extra_html', '')))
    wks = []
    for w in range(1, 5):
        t, p = F.WEEKS[w]
        lis = ''.join('<li data-d="%d" data-f="%s"><a href="#d%d"><b>Day %d</b>%s<i class="%s">%s</i></a></li>' % (
            d['n'], d['f'], d['n'], d['n'], E(d['title']), 'psy' if d['f'] == 'psy' else '', 'Pers' if d['f'] == 'psy' else 'Sales')
            for d in days if (d['n'] - 1) // 7 + 1 == w)
        wks.append('<div class="wk"><h4>Week %d \u00b7 %s</h4><p>%s</p><ol>%s</ol></div>' % (w, E(t), E(p), lis))
    npsy = sum(1 for d in days if d['f'] == 'psy')
    arts.append('<article class="mod" id="plan"> <div class="mod-meta">Map 5 \u00b7 The 28-day trail</div><h2 class="mod-title">Four weeks, one video a day</h2> '
                '<p class="mod-why">%d Persuasion days and %d Sales days, alternating so each field sharpens the other. Every day has the review, predict, '
                'insider layer, diagram, a go-deeper box and recall.</p> %s <div class="trail">%s</div> '
                '<div class="weak js-only" id="weak" hidden=""><h5>Your weak spots</h5><ul id="weak-list"></ul></div> </article>' % (npsy, 28 - npsy, fp(), ''.join(wks)))
    cov = next(M for M in F.MAPS if M['id'] == 'coverage')
    arts.append('<article class="mod" id="coverage"> <div class="mod-meta">%s</div><h2 class="mod-title">%s</h2> <p class="mod-why">%s</p> %s%s </article>' % (
        E(cov['meta']), E(cov['title']), E(cov['why']),
        R.fig(cov['svg'], cov['figcap']) if cov.get('svg') else '',
        cov.get('extra_html', '')))
    qs = ''.join('<li>%s%s</li>' % (E(q), ''.join('<a href="#d%d">Day %d</a>' % (n, n) for n in ds)) for q, ds in F.QUESTIONS)
    arts.append('<article class="mod" id="qbank"> <div class="mod-meta">Map 7 \u00b7 The question bank</div><h2 class="mod-title">The questions this guide answers</h2> '
                '<p class="mod-why">Your questions first, then the ones the fields organise themselves around. Each one links to the days that answer it. '
                'Add new ones to your question ledger: the next drop is built from them.</p><ol class="qbank">%s</ol> </article>' % qs)
    s1 = ('<section class="part" id="s1" data-part="1" data-sec="1"> %s <div class="wrap"> %s </div></section>' % (
        part_head('The map \u00b7 read once, come back often', 'Two fields, one handshake',
                  'Persuasion explains why people say yes. Sales is the craft of earning that yes from a real buyer, honestly. Here is the territory, the timeline, the coverage and what professionals actually believe.'),
        ' '.join(arts)))
    # ---------- weeks ----------
    recall = {d['n']: [(E(q), E(a)) for q, a in d['recall']] for d in days}
    fields = {d['n']: d['f'] for d in days}
    total = {f: sum(1 for v in fields.values() if v == f) for f in ('psy', 'phi')}

    def track(n):
        f = fields[n]
        return sorted(k for k, v in fields.items() if v == f).index(n) + 1, total[f]
    base = ('<div class="rv qa" data-rv="both psy phi"><p class="q"><small>Baseline</small>On a scale of 1 to 5, how well could you explain to a sales leader '
            'and a behavioural scientist why people say yes, and where honest persuasion ends and manipulation begins? Write the number down. '
            'You will rate yourself again at the end of each week.</p></div>')
    secs = []
    for w in range(1, 5):
        sid, dp = SEC[w]
        t, p = F.WEEKS[w]
        out = []
        for d in [x for x in days if (x['n'] - 1) // 7 + 1 == w]:
            extra = ''
            if d['n'] in ties:
                T = ties[d['n']]
                extra = R.tieup(w, T['title'], T['intro'], T['rows'], T['boss'], T['calib'])
            nxt = ('You finished all 28 days. Next: the library and glossary below, then your spaced reviews keep it alive.' if d['n'] == 28 else None)
            a = R.day(d, dict(recall=recall, fields=fields, img=img, track=track, last=28, extra_html=extra, next_line=nxt))
            if d['n'] == 1:
                a = a.replace('<div class="step-k">1 \u00b7 Warm-up review \u00b7 2 min</div></div>', '<div class="step-k">1 \u00b7 Warm-up review \u00b7 2 min</div>%s</div>' % base, 1)
            out.append(a)
        secs.append('<section class="part" id="%s" data-sec="%d" data-part="%s"> %s <div class="wrap">\n%s\n</div>\n</section>' % (
            sid, w + 1, dp, part_head('Week %d \u00b7 7 days \u00b7 about 20 min each' % w, t, p), '\n'.join(out)))
    LOG.append('rendered 4 weeks')
    # ---------- s6: library + glossary ----------
    L = F.LIBRARY
    def short(dur):
        if not dur:
            return 'long'
        return ('~%d min' % max(1, round(R.secs(dur.lstrip('~')) / 60))) if dur.startswith('~') else dur
    spine = ''.join('<li class="core"><b>Day %d</b><a href="https://www.youtube.com/watch?v=%s" target="_blank" rel="noopener">%s \u00b7 %s</a><em>%s</em></li>' % (
        d['n'], d['ep'][2], E(d['ep'][4]), E(d['ep'][0]), E(short(d['ep'][3]))) for d in days)
    extras = ''.join('<a href="https://www.youtube.com/watch?v=%s" target="_blank" rel="noopener"><b>%s</b><span>%s%s \u00b7 %s</span></a>' % (
        vid, E(t), E(ch), (' \u00b7 %s min' % m) if m else '', E(why)) for t, ch, vid, m, why in L['extras'])
    books = ''.join('<a href="%s" target="_blank" rel="noopener"><b>%s, %s (%s)</b><span>%s Weak spot: %s</span></a>' % (
        E(u, quote=True), E(au), E(t), E(str(y)), E(best), E(weak)) for t, au, y, best, weak, u in L['books'])
    courses = ''.join('<a href="%s" target="_blank" rel="noopener"><b>%s</b><span>%s \u00b7 %s</span></a>' % (E(u, quote=True), E(t), E(pv), E(nt)) for t, pv, u, nt in L['courses'])
    gl, seen = [], set()
    for t, dfn, c in list(F.LIB_GLOSS) + [g for m in mods for g in getattr(m, 'GLOSS', [])]:
        if t.lower() in seen:
            continue
        seen.add(t.lower())
        gl.append((t, c, dfn))
    gl.sort(key=lambda g: g[0].lower())
    gloss = ''.join('<div class="g"><b>%s</b><em>%s</em><p>%s</p></div>' % (E(t), E(c), E(dfn)) for t, c, dfn in gl)
    LOG.append('glossary: %d terms' % len(gl))
    s6 = ('<section class="part" id="s6" data-sec="6" data-part="2"> %s <div class="wrap"> '
          '<article class="mod" id="lib-spine"><div class="mod-meta">The spine \u00b7 28 videos</div><h2 class="mod-title">Every day\'s video</h2><p class="mod-why">%s</p><ul class="lib-list">%s</ul></article> '
          '<article class="mod" id="lib-more"><div class="mod-meta">Beyond the spine</div><h2 class="mod-title">Next steps</h2> <h3>More videos, verified</h3><div class="further">%s</div> '
          '<h3>The books this guide distils</h3><div class="further">%s</div> <h3>Free courses</h3><div class="further">%s</div> </article> '
          '<article class="mod" id="glossary"><div class="mod-meta">Glossary \u00b7 all four weeks + the map</div><h2 class="mod-title">Field glossary</h2> '
          '<div class="gloss-tools js-only"><input type="search" id="g-q" placeholder="Search: try \'BATNA\'" aria-label="Search the glossary"><span class="count" id="g-count"></span></div> '
          '<div class="gloss" id="gloss">%s</div> <div style="margin-top:30px"><button class="btn btn-ghost js-only" id="reset">Reset my progress</button></div> </article> </div></section>') % (
        part_head('Library \u00b7 everything, verified', 'Library + glossary', 'The 28 spine videos, the best next videos, the books distilled inside the days, and every term.'),
        E(L['spine_note']), spine, extras, books, courses, gloss)
    footer = ('<footer class="colophon"><div class="wrap"> <div class="kicker">Colophon</div><h2>Notice it. Question it. Earn it.</h2> '
              '<p style="max-width:68ch">Made for Kevin Cecil. %s</p> <p style="max-width:68ch">The plates are historical images from Wikimedia Commons, each chosen to carry the day\'s idea. '
              'Progress, grades and your answers are saved in this browser only.</p> <p><a href="#top">Back to the top \u2191</a></p> </div></footer>') % E(F.COLOPHON)
    s = head + '</head>\n' + prefix + '<div class="site">\n' + cover + '\n' + s0 + '\n' + s1 + '\n' + '\n'.join(secs) + '\n' + s6 + '\n' + footer + tail
    body = re.sub(r'<(script|style)\b.*?</\1>', ' ', s, flags=re.S)
    em, en = body.count('\u2014'), body.count('\u2013')
    if em or en:
        def scrub(m):
            x = m.group(0)
            return x if x.startswith(('<script', '<style')) else x.replace('\u2014', ', ').replace('\u2013', ' to ')
        s = re.sub(r'<(script|style)\b.*?</\1>|[^<]+|<[^>]+>', scrub, s, flags=re.S)
    LOG.append('dashes converted: %d em, %d en' % (em, en))
    if 'mtrx-mind-v1' in s:
        raise SystemExit('old progress key still present')
    LOG.append('images: %d of %d plates inlined' % (sum(1 for v in uris.values() if v), len(uris)))
    open(dst, 'w', encoding='utf-8').write(s)
    LOG.append('wrote %s (%d bytes)' % (dst, len(s)))
    print('\n'.join(LOG))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

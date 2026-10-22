#!/usr/bin/env python3
"""No. 03 Cons and Cults builder: python build/03/build.py out.html

The shell (head, house CSS, reader kit, core scripts, shared add-on tag) is taken from the
live No. 06 guide, so No. 03 gets every reader feature without copying 900 KB through an AI.
Content lives in small files: start.py (Start stops), f<N>_<k>.py (one stop each), p3.css.
PLAN below is the whole roadmap; files without built stops show as watch-ahead heads.
A stop file that fails to import is reported and skipped, never fatal. Dashes in content
are converted (em dash to comma, en dash to " to ") and counted in the report. Stdlib only.
"""
import glob, html, importlib.util, json, os, re, sys, traceback

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
SHELL = os.path.join(ROOT, 'guides', '06-read-the-room.html')
TITLE = 'MTRX\u2122 Field Series No. 03 \u00b7 Cons and cults \u00b7 Kevin Cecil'
SLUG = 'mtrx-field-series-03-cons-and-cults'
KEY = 'mtrx-cons-v1'
DESC = 'How cults, cons and power plays really work: question-led, evidence-graded, with a writer\'s room in every stop. Prepared for Kevin Cecil.'
STAMP = {'hold': 'Holds up', 'part': 'Partly', 'myth': 'Myth', 'anti': 'Anti-model', 'field': 'Field test'}

PLAN = [
    dict(n=1, part=5, short='I.1', tab='Inside', title='Inside the cult',
         kicker='File 1 \u00b7 Week 1 \u00b7 the members', promise='Who joins, what the group does to them, and why it works. Seven stops, one a day.',
         stops=[('1.1', 'Who joins, and why it is not stupidity'), ('1.2', 'What a cult is, and why the word is a fight'),
                ('1.3', "The toolkit: Lifton's eight"), ('1.4', 'Cutting the cord: why cults isolate you'),
                ('1.5', 'Why cults work: strictness, sacrifice and dissonance'), ('1.6', 'Belonging and identity: the happiest time of my life'),
                ('1.7', 'Case file: Jonestown, read with everything')]),
    dict(n=2, part=2, short='I.2', tab='Leader', title='The leader',
         kicker='File 2 \u00b7 Week 2 \u00b7 the leader', promise='Motive, personality, charisma, and the strange question underneath it all: why do humans want leaders?',
         stops=[('2.1', "The leader's motive: true believer, fraud, or both"), ('2.2', "The guru pattern: Storr's Feet of Clay and the narcissism question"),
                ('2.3', 'Charisma: why followers grant it'), ('2.4', 'Why we need leaders at all: prestige, dominance and following'),
                ('2.5', 'Entrepreneurs of identity: how leaders build the "we"'), ('2.6', 'When the leader dies, fails or is exposed'),
                ('2.7', 'Case file: NXIVM, a coaching company that branded women')]),
    dict(n=3, part=3, short='I.3', tab='World', title='The world around the cult',
         kicker='File 3 \u00b7 Week 3 \u00b7 the sociologist', promise='The sociologist\'s lens: networks, panics, violence, leaving, and where "cultish" begins in ordinary life.',
         stops=[('3.1', 'The sociological lens: Weber, Durkheim and collective effervescence'), ('3.2', 'Recruitment runs on networks, and some cults become world religions'),
                ('3.3', 'The brainwashing fight: Singer, the APA and the courts'), ('3.4', 'The cult panic: deprogrammers and what they got wrong'),
                ('3.5', "Violence: what predicts it (Waco, Heaven's Gate, Aum Shinrikyo)"), ('3.6', 'Leaving and after: exit costs and rebuilding a self'),
                ('3.7', 'Born inside: second-generation members'), ('3.8', 'Cultish: online groups, wellness, MLMs and startups'),
                ('3.9', 'On screen: The Master, Midsommar, The Wicker Man, Martha Marcy May Marlene')]),
    dict(n=4, part=1, short='II.1', tab='Big con', title='The big con',
         kicker='File 4 \u00b7 Week 4 \u00b7 the grift', promise='How a con is built, beat by beat, from Victor Lustig selling the Eiffel Tower to Slippin\' Jimmy.',
         stops=[('4.1', "Anatomy of a con: Maurer's big con, step by step"), ('4.2', 'The man who sold the Eiffel Tower: Victor Lustig'),
                ('4.3', "Why smart people fall for cons, and why we are less gullible than films think"), ('4.4', 'The Sting: making the audience the mark'),
                ('4.5', "Slippin' Jimmy to Saul Goodman"), ('4.6', 'Twists that play fair: Nine Queens, House of Games, The Grifters')]),
    dict(n=5, part=4, short='II.2', tab='Masks', title='Masks and crews',
         kicker='File 5 \u00b7 Week 5 \u00b7 the masks', promise='Identity cons and heists: Ripley, the real impostors, Lupin, Ocean\'s, and what real thieves actually did.',
         stops=[('5.1', 'Ripley: the identity con as character'), ('5.2', 'Real impostors: Clark Rockefeller, Anna Delvey and the Abagnale problem'),
                ('5.3', 'The gentleman thief: Lupin'), ('5.4', "Ocean's and the crew film"),
                ('5.5', 'Real heists: Antwerp, Hatton Garden, the Louvre 2025'), ('5.6', 'Social engineering: the con inside the heist')]),
    dict(n=6, part=6, short='II.3', tab='Money', title='Money fraud',
         kicker='File 6 \u00b7 Week 6 \u00b7 the money', promise='Ponzi, Madoff, Theranos, FTX, Wirecard, and the scams that target people like you.',
         stops=[('6.1', 'Ponzi and affinity fraud: from Charles Ponzi to Madoff'), ('6.2', 'Ponzi, pyramid or MLM: telling them apart'),
                ('6.3', 'Theranos: the story that outran the science'), ('6.4', 'FTX and Wirecard: when nobody checks'),
                ('6.5', 'The fraud triangle, and why good people cook the books'), ('6.6', 'Scams that target you: pig butchering, task scams and fake clients')]),
    dict(n=7, part=5, short='III', tab='Power', title='Power and the reveal',
         kicker='File 7 \u00b7 Week 7 \u00b7 the reveal', promise='Which influence levers survive the evidence, how frauds get caught, and your capstone: a con film treatment.',
         stops=[('7.1', "Cialdini's levers: which survived replication"), ('7.2', 'The 48 Laws as story, not science'),
                ('7.3', 'Coercive control: when influence becomes captivity'), ('7.4', 'The investigators: Markopolos, Carreyrou and the short sellers'),
                ('7.5', 'Red-team your own pitch: honest influence for MTRX\u2122'), ('7.6', 'Capstone: write a con film treatment')]),
]
LOG = []


def mid(n):
    return 'm' + n.replace('.', '-')


def a(url, label):
    return '<a href="%s" rel="noopener" target="_blank">%s</a>' % (html.escape(url, quote=True), label)


def load(path):
    name = os.path.splitext(os.path.basename(path))[0]
    try:
        spec = importlib.util.spec_from_file_location('c_' + name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    except Exception:
        LOG.append('SKIPPED %s: %s' % (name, traceback.format_exc().strip().splitlines()[-1]))
        return None


def yt(v, small=None):
    th = ('<div class="vid-th"><span class="ph">%s</span><img alt="Still from %s" loading="lazy" onerror="this.remove()" '
          'src="https://i.ytimg.com/vi/%s/mqdefault.jpg"/><span class="play"></span></div>') % (
        v['title'], html.escape(v['title'], quote=True), v['id'])
    meta = small or '%s%s' % (v.get('who', ''), (' \u00b7 %s' % v['year']) if v.get('year') else '')
    return ('<a class="vid" href="https://www.youtube.com/watch?v=%s" rel="noopener" target="_blank">%s<div class="vid-b">'
            '<div class="vid-t">%s</div><div class="vid-m">%s</div></div></a>') % (v['id'], th, v['title'], meta)


def nodash(x):
    return x.replace('\u2014', ', ').replace('\u2013', ' to ')


def check(c):
    d = {'q': nodash(c['q']), 'o': [nodash(o) for o in c['o']], 'a': c['a'], 'w': nodash(c['w'])}
    return '<div class="check"><script type="application/json">%s</script></div>' % json.dumps(d, ensure_ascii=False).replace('</', '<\\/')


def stop(F, st):
    n = st['id']
    o = ['<article class="mod" id="%s" data-mod="%s">' % (mid(n), n),
         '<div class="mod-meta">File %d \u00b7 Stop %s \u00b7 Day %d <span class="t">20 min</span></div>' % (F['n'], n, st['day']),
         '<h2 class="mod-title">%s</h2>' % st['title'],
         '<p class="qline"><span>The question</span>%s</p>' % st['q'],
         '<p class="mod-why">%s</p>' % st['why']]
    c = st.get('case')
    if c:
        o.append('<div class="dossier"><div class="dos-tab">Case file %s</div><div class="dos-body"><div class="dos-k">%s</div>'
                 '<div class="dos-name">%s</div><div class="dos-role">%s</div><dl class="dos-facts">%s</dl></div>'
                 '<span class="stamp st-%s">%s</span></div>' % (n, c.get('k', 'Subject'), c['name'], c['role'],
                                                                 ''.join('<div><dt>%s</dt><dd>%s</dd></div>' % f for f in c['facts']),
                                                                 c['stamp'][0], c['stamp'][1]))
    o.append('<div class="predict"><div class="predict-k">Cold open \u00b7 predict first \u00b7 2 min</div><p>%s</p>'
             '<p class="conf">Write your answer and how sure you are, 1 to 5, before you open it.</p>'
             '<details class="reveal"><summary>Reveal the answer</summary><p>%s</p></details></div>' % (st['cold']['q'], st['cold']['a']))
    v = st.get('video')
    if v:
        o.append('<h3>Watch</h3><div class="watch3">%s<div><div class="scene-wh">Watch for</div><ul class="scene-w">%s</ul></div></div>' % (
            yt(v), ''.join('<li>%s</li>' % w for w in v['watch'])))
    o.append('<h3>The deep answer</h3><div class="story">%s</div>' % ''.join('<p>%s</p>' % p for p in st['story']))
    if st.get('fig'):
        svg, cap = st['fig']
        o.append('<figure class="fig"><div class="scroll">%s</div><figcaption>%s</figcaption></figure>' % (svg, cap))
    if st.get('specs'):
        o.append('<h3>The words insiders use</h3><div class="specs">%s</div>' % ''.join(
            '<div class="spec"><div class="spec-name">%s</div><p class="spec-def">%s</p></div>' % s for s in st['specs']))
    if st.get('tags'):
        o.append('<h3>Truth tags</h3><ul class="ttags">%s</ul>' % ''.join(
            '<li><span class="stamp st-%s">%s</span><div><p><b>%s</b> %s</p><span class="src">Source: %s</span></div></li>' % (
                tg, STAMP[tg], claim, fix, a(src[1], src[0])) for tg, claim, fix, src in st['tags']))
    if st.get('distil'):
        o.append('<div class="distil"><div class="distil-k">This stop distils</div><ul>%s</ul></div>' % ''.join(
            '<li>%s<span>%s</span></li>' % (a(u, lab), what) for lab, u, what in st['distil']))
    w = st.get('writer')
    if w:
        o.append('<div class="writer wr"><div class="writer-k">Writer\'s room \u00b7 for No. 08</div>%s<p class="wr-drill"><b>Scene drill.</b> %s</p></div>' % (
            ''.join('<p>%s</p>' % p for p in w['notes']), w['drill']))
    if st.get('biz'):
        o.append('<div class="mtrx biz"><p><b>Business lens.</b> %s</p></div>' % st['biz'])
    dr = st.get('drill')
    if dr:
        o.append('<div class="drill"><div class="drill-h"><b>%s</b><span>Drill \u00b7 %s</span></div><ol>%s</ol>'
                 '<p class="drill-x"><b>Usual mistake:</b> %s</p></div>' % (dr['name'], dr['mins'], ''.join('<li>%s</li>' % x for x in dr['steps']), dr['mistake']))
    o.append('<div class="tryit"><div class="tryit-k">Try it \u00b7 5 min</div><p>%s</p></div>' % st['tryit'])
    o.append('<p class="room">%s</p>' % st['room'])
    if st.get('deeper'):
        o.append('<details class="deeper"><summary>Go deeper \u00b7 optional 15 min</summary><ul>%s</ul></details>' % ''.join(
            '<li>%s<span>%s</span></li>' % (a(u, lab), why) for lab, u, why in st['deeper']))
    o.append('<p class="nextq"><b>Your next question.</b> %s</p>' % st['nextq'])
    for c in st['checks']:
        o.append(check(c))
    o.append('<button class="done" data-mod="%s">Mark stop %s done</button></article>' % (n, n))
    return ''.join(o)


def part_head(F, built):
    lis = ''.join('<li><a href="#%s"><span>%s</span>%s<em>%s</em></a></li>' % (
        mid(i) if i in built else 's%d' % F['n'], i, x, '20 min' if i in built else 'soon') for i, x in F['stops'])
    return ('<div class="part-head"><div class="wrap"><div class="kicker">%s</div><h2 class="part-title">%s</h2>'
            '<p class="part-promise">%s</p><ol class="stops">%s</ol></div></div>') % (F['kicker'], F['title'], F['promise'], lis)


def main(dst):
    shell = open(SHELL, encoding='utf-8').read()
    head = shell[:shell.find('</head>')]
    head = re.sub(r'<title>.*?</title>', '<title>%s</title>' % TITLE, head, count=1, flags=re.S)
    head = re.sub(r'<meta name="mtrx-slug" content="[^"]*">', '<meta name="mtrx-slug" content="%s">' % SLUG, head, count=1)
    head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % html.escape(DESC, quote=True), head, count=1)
    css = open(os.path.join(HERE, 'p3.css'), encoding='utf-8').read() if os.path.exists(os.path.join(HERE, 'p3.css')) else ''
    head += '<style id="mtrx-p3-css">%s</style>' % css
    b0 = shell.find('<body')
    prefix = shell[b0:shell.find('<nav class="thumbs"', b0)]
    fend = shell.find('</footer>') + len('</footer>')
    tail = shell[fend:]
    n_key = 0

    def fix_script(m):
        nonlocal n_key
        if 'mtrx-kit-js' in m.group(1) or 'json' in m.group(1):
            return m.group(0)
        n_key += m.group(2).count('mtrx-room-v1')
        return '<script%s>%s</script>' % (m.group(1), m.group(2).replace('mtrx-room-v1', KEY))
    tail = re.sub(r'<script([^>]*)>(.*?)</script>', fix_script, tail, flags=re.S)
    LOG.append('progress key replaced %d times in core scripts' % n_key)
    left = re.sub(r'<(script|style)\b.*?</\1>', '', tail, flags=re.S)
    LOG.append('tail outside scripts: %r' % left[:200])
    for m in re.finditer(r'<script([^>]*)>(.*?)</script>', tail, re.S):
        if 'mtrx-kit-js' not in m.group(1) and m.group(2).strip():
            hits = sorted(set(re.findall(r'[\w-]*(?:room|06|Part I)[\w-]*', m.group(2))))
            LOG.append('core script %d bytes, 06-specific words: %s' % (len(m.group(2)), hits[:20]))

    start = load(os.path.join(HERE, 'start.py'))
    built = {}
    for p in sorted(glob.glob(os.path.join(HERE, 'f[0-9]_*.py')), key=lambda x: [int(z) for z in re.findall(r'\d+', os.path.basename(x))]):
        mod = load(p)
        if mod and hasattr(mod, 'STOP'):
            built[mod.STOP['id']] = mod.STOP
    LOG.append('built stops: %s' % ', '.join(sorted(built, key=lambda s: [int(z) for z in s.split('.')])))
    sources = []
    tabs = [('0', 'Start', 'Start', '00')] + [(str(F['n']), F['title'], F['tab'], F['short']) for F in PLAN]
    nav = '<nav class="thumbs" aria-label="Sections">%s</nav>' % ''.join(
        '<button class="thumb" type="button" data-t="%s" aria-label="%s"><span class="lbl"><span class="full">%s</span>'
        '<span class="short">%s</span></span><i></i></button>' % t for t in tabs)
    nbuilt = len(built)
    total = sum(len(F['stops']) for F in PLAN)
    cube = ''.join('<a href="%s"><span class="ph">%s</span><img src="https://i.ytimg.com/vi/%s/mqdefault.jpg" alt="Still from %s" loading="lazy" onerror="this.remove()"><b>%s</b></a>' % (
        href, html.escape(lab), vid, html.escape(lab, quote=True), tag) for href, lab, vid, tag in start.CUBE) if start else ''
    cover = ('<header class="wrap cover" id="top" data-sec="0"><div><div class="kicker">MTRX\u2122 Field Series \u00b7 No. 03 \u00b7 October 2026</div>'
             '<h1 class="cover-title">Cons and <span class="o">cults</span></h1><p class="cover-sub">%s</p>'
             '<ul class="verbs"><li>Ask</li><li>Explain</li><li>Write</li></ul>'
             '<p class="prepared">Prepared for <b>Kevin Cecil</b>, founder, MTRX\u2122 Digital, and future director<br>%d stops built of %d planned \u00b7 7 files \u00b7 20 minutes a day \u00b7 a writer\'s room in every stop<br>Sources checked 22 October 2026</p>'
             '<a class="btn btn-a" href="#m0-1">Start here <span aria-hidden="true">\u2193</span></a></div>'
             '<div class="cover-plate"><nav class="cube6" aria-label="Nine videos in this guide">%s</nav><p class="cube-cap">Nine of the videos inside. Tap one to jump to its stop.</p></div></header>') % (
        start.SUB if start else '', nbuilt + (len(start.STOPS) if start else 0), total + (len(start.STOPS) if start else 0), cube)
    secs = []
    if start:
        secs.append('<section class="part" id="s0" data-part="0" data-sec="0" data-title="Start here"><div class="wrap">%s</div></section>' % ''.join(
            '<article class="mod" id="%s" data-mod="%s"><div class="mod-meta">Stop %s \u00b7 Start <span class="t">%s min</span></div>'
            '<h2 class="mod-title">%s</h2><p class="mod-why">%s</p>%s<p class="room">%s</p><button class="done" data-mod="%s">Mark stop %s done</button></article>' % (
                mid(s['id']), s['id'], s['id'], s['mins'], s['title'], s['why'], ''.join(s['body']), s['room'], s['id'], s['id']) for s in start.STOPS))
        sources += getattr(start, 'SOURCES', [])
    for F in PLAN:
        mine = [built[i] for i, _ in F['stops'] if i in built]
        body = ''.join(stop(F, st) for st in mine)
        if not mine:
            body = '<div class="later"><p>This file is planned and audited. Its stops arrive one week at a time; the question bank in Stop 0.2 shows what each one answers.</p></div>'
        secs.append('<section class="part" id="s%d" data-part="%d" data-sec="%d" data-title="File %d \u00b7 %s">%s<div class="wrap">%s</div></section>' % (
            F['n'], F['part'], F['n'], F['n'], html.escape(F['title'], quote=True), part_head(F, built), body))
        for st in mine:
            sources += [(lab, u, st['id']) for lab, u, _ in st.get('distil', [])]
            sources += [(src[0], src[1], st['id']) for _, _, _, src in st.get('tags', [])]
    seen, cards = set(), []
    for lab, u, sid in sources:
        if u in seen:
            continue
        seen.add(u)
        cards.append('<a class="read-card" href="%s" target="_blank" rel="noopener"><b>%s</b><span>Stop %s</span></a>' % (html.escape(u, quote=True), lab, sid))
    footer = ('<footer class="colophon"><div class="wrap"><div class="kicker">Sources</div><h2 class="part-title" style="font-size:clamp(40px,6vw,72px)">Every claim, linked</h2>'
              '<div class="vids" style="grid-template-columns:repeat(auto-fill,minmax(260px,1fr))">%s</div>%s</div></footer>') % (
        ''.join(cards), start.COLOPHON if start and hasattr(start, 'COLOPHON') else '')
    out = head + '</head>' + prefix + nav + '<div class="site">' + cover + ''.join(secs) + footer + tail
    body_txt = re.sub(r'<(script|style)\b.*?</\1>', ' ', out, flags=re.S)
    em, en = body_txt.count('\u2014'), body_txt.count('\u2013')
    if em or en:
        def scrub(m):
            if m.group(0).startswith('<script') or m.group(0).startswith('<style'):
                return m.group(0)
            return m.group(0).replace('\u2014', ', ').replace('\u2013', ' to ')
        out = re.sub(r'<(script|style)\b.*?</\1>|[^<]+|<[^>]+>', scrub, out, flags=re.S)
    LOG.append('dashes converted: %d em, %d en' % (em, en))
    LOG.append('sources: %d unique' % len(cards))
    open(dst, 'w', encoding='utf-8').write(out)
    LOG.append('wrote %s (%d bytes)' % (dst, len(out)))
    print('\n'.join(LOG))


if __name__ == '__main__':
    main(sys.argv[1])

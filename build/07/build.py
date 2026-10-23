#!/usr/bin/env python3
"""No. 07 Design builder: python build/07/build.py out.html

Same approach as No. 03: the shell (head, house CSS, reader kit, core scripts, shared add-on tag)
comes from the live No. 06 guide. Content lives in small files: start.py (Start stops),
f<N>_<k>.py (one stop each), p7.css (plus the shared build/03/p3.css). PLAN is the whole map;
parts without built stops show as watch-ahead heads.

Images: images.py names public-domain and openly licensed works by their Wikimedia Commons file
title. On the first build with network access each one is fetched once, resized and saved as WebP
in build/out/07-img/ (committed, so later builds reuse it), then inlined as base64. Value plates
also get a greyscale and a two-value (notan) version. A missing image becomes a link card, never
a build failure. Stdlib, plus Pillow when it is installed.
"""
import base64, glob, html, importlib.util, io, json, os, re, sys, traceback, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
SHELL = os.path.join(ROOT, 'guides', '06-read-the-room.html')
CACHE = os.path.join(ROOT, 'build', 'out', '07-img')
TITLE = 'MTRX\u2122 Field Series No. 07 \u00b7 Design and taste \u00b7 Kevin Cecil'
SLUG = 'mtrx-field-series-07-design'
KEY = 'mtrx-design-v1'
DESC = 'How designers see, decide and make: question-led, evidence-graded, with a director\'s eye and a studio lens in every stop. Prepared for Kevin Cecil.'
STAMP = {'hold': 'Holds up', 'part': 'Partly', 'myth': 'Myth', 'anti': 'Anti-model', 'field': 'Field test',
         'unv': 'Unverified', 'thumb': 'Rule of thumb'}
UA = 'MTRX-Field-Library-build/1.0 (+https://github.com/Kevincecil11/mtrx-field-library)'


def P(n, part, short, tab, title, kicker, promise, stops):
    return dict(n=n, part=part, short=short, tab=tab, title=title, kicker=kicker, promise=promise, stops=stops)


PLAN = [
    P(1, 5, '1', 'Seeing', 'Seeing like a designer', 'Part 1 \u00b7 Week 1 \u00b7 the loop before the looks',
      'Before any style: the brief, the process, how attention really works, the visual alphabet, and value. Five stops, one a day.',
      [('1.1', 'What problem are we actually designing?'), ('1.2', 'How do designers get from fog to a decision?'),
       ('1.3', 'What does the eye grab first, and what does it miss?'), ('1.4', 'What are point, line, plane, shape and form doing?'),
       ('1.5', 'Why do designers squint?')]),
    P(2, 2, '2', 'Principles', 'Shared principles', 'Part 2 \u00b7 Weeks 2 and 3 \u00b7 the deep one',
      'Twelve stops on the principles every field shares, each with its evidence status, named makers, a web use, a film use and a drill.',
      [('2.1', 'What does your eye see first, and who chose that?'), ('2.2', 'Why do scattered dots become a group?'),
       ('2.3', 'Can an empty shape become the subject?'), ('2.4', 'Can spacing beat a border?'), ('2.5', 'Where will the gaze go next?'),
       ('2.6', 'What makes order feel alive instead of boring?'), ('2.7', 'Why does one small dark shape outweigh a big pale one?'),
       ('2.8', 'Why do designers draw invisible lines?'), ('2.9', 'Can beauty make a bad interface feel usable?'),
       ('2.10', 'Can more detail make a design less interesting?'), ('2.11', 'Are the golden ratio and rule of thirds really laws?'),
       ('2.12', 'Boss fight: can a rule survive a real brief?')]),
    P(3, 3, '3', 'Type', 'Type', 'Part 3 \u00b7 Week 4 \u00b7 letters with a voice',
      'Anatomy to shipping, with your own Tanker and Nunito Sans as the case.',
      [('3.1', 'What is a letter before it is a font?'), ('3.2', 'Why do type families sound different?'), ('3.3', 'Should good type be invisible?'),
       ('3.4', 'How do Tanker and Nunito Sans become a system?'), ('3.5', 'Can one site speak Gujarati, Hindi and English?'),
       ('3.6', 'How does type enter film?'), ('3.7', 'What makes a type decision safe to ship?')]),
    P(4, 6, '4', 'Colour', 'Colour', 'Part 4 \u00b7 Weeks 5 and 6 \u00b7 the StudioBinder ladder',
      'The overall theory first, then the specific colour theories, then colour in story and brand.',
      [('4.1', 'What is colour before it is a design choice?'), ('4.2', 'Which three knobs do you actually turn?'),
       ('4.3', 'Why does the same grey look different twice?'), ('4.4', 'Which colour scheme gives the frame a job?'),
       ('4.5', "What are Itten's seven contrasts?"), ('4.6', 'Can a 1930s Japanese dictionary pick your palette?'),
       ('4.7', 'How much of colour psychology is real?'), ('4.8', 'How does a colour become a character?'),
       ('4.9', 'Can a palette carry a whole film?'), ('4.10', 'Can a brand own a colour?'), ('4.11', 'Boss fight: palette to pixels, paint and grade')]),
    P(5, 1, '5', 'Composition', 'Composition, light and image', 'Part 5 \u00b7 Week 7 \u00b7 the frame',
      'Kubrick, Caravaggio and Picasso, plus the camera, layout and data stops.',
      [('5.1', 'Why can a centred frame feel powerful or dead?'), ('5.2', 'What do diagonals do to your nerves?'), ('5.3', 'How does light stage attention?'),
       ('5.4', 'What can disappear before the bull stops being a bull?'), ('5.5', 'What does a camera add to composition?'),
       ('5.6', 'How does a layout survive a phone, a poster and a billboard?'), ('5.7', 'How does data become a legible picture?'),
       ('5.8', 'Can pattern and texture carry identity?')]),
    P(6, 4, '6', 'Makers', 'Philosophies and the makers', 'Part 6 \u00b7 Week 8 \u00b7 the arguments',
      'The arguments worth having, then Ahmedabad as a living case study.',
      [('6.1', 'When does form actually follow function?'), ('6.2', 'Is ornament a crime or a meaning?'), ('6.3', 'Less is more, or less is a bore?'),
       ('6.4', 'What did the Bauhaus teach before it taught a style?'), ('6.5', 'Does good design disappear?'), ('6.6', 'What does emptiness give the user?'),
       ('6.7', 'What does the brick want?'), ('6.8', 'Can architecture be a social framework?'), ('6.9', 'When should a designer refuse?')]),
    P(7, 5, '7', 'Brand', 'Brand identity and digital systems', 'Part 7 \u00b7 Week 9 \u00b7 the system',
      'Wheeler distilled, then the bridge from brand to a working website.',
      [('7.1', 'Is a brand a logo, a promise or a memory?'), ('7.2', 'Why does a five-phase process take so long?'), ('7.3', 'Which kind of mark does the job?'),
       ('7.4', 'Can one symbol cross every language?'), ('7.5', 'Why do rebrands blow up?'), ('7.6', 'How does identity scale into a website?'),
       ('7.7', 'Can it feel usable before it looks beautiful?'), ('7.8', 'Is it accessible by default?'), ('7.9', 'Boss fight: brand sheet and handoff for a safari lodge')]),
    P(8, 2, '8', 'Aesthetics', 'Aesthetics', 'Part 8 \u00b7 Week 10 \u00b7 taste',
      'Modern versus vintage, clothing as a design system, taste philosophy and Pinterest-style boards.',
      [('8.1', 'Why does a style feel old or new before we can name it?'), ('8.2', 'Can you date a design without a logo?'),
       ('8.3', 'Why do trends spread, mutate and die?'), ('8.4', 'What are you wearing, as a design system?'), ('8.5', 'Is taste personal, trained or class power?'),
       ('8.6', 'Beautiful, sublime, camp or kitsch?'), ('8.7', 'How do you fake an era honestly?'), ('8.8', 'How do you build taste on purpose?')]),
    P(9, 3, '9', 'Story', 'Storytelling and the capstone', 'Part 9 \u00b7 Week 11 \u00b7 meaning',
      'Meaning, sequence and the bridge to film, ending in your own aesthetic manifesto.',
      [('9.1', 'What does an image say beyond what it shows?'), ('9.2', 'How does a place become a character?'),
       ('9.3', 'How do line, shape, tone, colour and rhythm tell a story?'), ('9.4', 'How does sequence create meaning?'),
       ('9.5', 'How does a brand tell a story before it speaks?'), ('9.6', 'Can a manifesto make a style repeatable?'), ('9.7', 'Capstone: one aesthetic, two media')]),
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


# ---------- images ----------
try:
    import images as IMG
    IMAGES = IMG.IMAGES
except Exception:
    IMAGES = {}
    LOG.append('no images.py: %s' % traceback.format_exc().strip().splitlines()[-1])
NET = {'tried': 0, 'ok': 0}


def _get(url, timeout=45):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def _strip(x):
    return html.unescape(re.sub(r'<[^>]+>', '', x or '')).strip()


def fetch(key, spec):
    """Cached image files for one plate: dict(files={main, gray, notan}, artist, licence)."""
    os.makedirs(CACHE, exist_ok=True)
    mp = os.path.join(CACHE, key + '.json')
    if os.path.exists(mp):
        meta = json.load(open(mp, encoding='utf-8'))
        if meta.get('file') == spec['file'] and all(os.path.exists(os.path.join(CACHE, f)) for f in meta['files'].values()) \
                and (not spec.get('values') or 'notan' in meta['files']):
            return meta
    if os.environ.get('MTRX_OFFLINE'):
        raise RuntimeError('offline build, image not fetched')
    NET['tried'] += 1
    api = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(
        {'action': 'query', 'titles': spec['file'], 'prop': 'imageinfo', 'iiprop': 'url|extmetadata', 'iiurlwidth': 1280, 'format': 'json'})
    d = json.loads(_get(api).decode('utf-8'))
    page = next(iter(d['query']['pages'].values()))
    ii = page['imageinfo'][0]
    em = ii.get('extmetadata', {})
    raw = _get(ii.get('thumburl') or ii['url'])
    files = {}
    try:
        from PIL import Image, ImageOps
        im = Image.open(io.BytesIO(raw)).convert('RGB')
        if im.width > 1100:
            im = im.resize((1100, round(im.height * 1100 / im.width)), Image.LANCZOS)

        def save(img, name, q):
            img.save(os.path.join(CACHE, name), 'WEBP', quality=q, method=6)
            return name
        files['main'] = save(im, key + '.webp', 74)
        if spec.get('values'):
            g = ImageOps.grayscale(im)
            files['gray'] = save(g, key + '-gray.webp', 70)
            hist, acc, cut = g.histogram(), 0, 128
            half = sum(hist) / 2
            for i, h in enumerate(hist):
                acc += h
                if acc >= half:
                    cut = i
                    break
            files['notan'] = save(g.point(lambda p: 255 if p > cut else 0), key + '-notan.webp', 60)
    except ImportError:
        files['main'] = key + '.jpg'
        open(os.path.join(CACHE, files['main']), 'wb').write(raw)
    meta = dict(file=spec['file'], artist=_strip(em.get('Artist', {}).get('value'))[:90],
                licence=_strip(em.get('LicenseShortName', {}).get('value'))[:40], files=files)
    json.dump(meta, open(mp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    NET['ok'] += 1
    return meta


def uri(name):
    mime = {'webp': 'image/webp', 'jpg': 'image/jpeg', 'png': 'image/png'}[name.rsplit('.', 1)[1]]
    return 'data:%s;base64,%s' % (mime, base64.b64encode(open(os.path.join(CACHE, name), 'rb').read()).decode('ascii'))


def plate(p):
    spec = IMAGES.get(p['key'])
    if not spec:
        LOG.append('IMAGE %s: not in images.py' % p['key'])
        return ''
    page = 'https://commons.wikimedia.org/wiki/' + urllib.parse.quote(spec['file'].replace(' ', '_'))
    try:
        meta = fetch(p['key'], spec)
    except Exception as e:
        meta = None
        LOG.append('IMAGE %s not fetched: %s' % (p['key'], str(e)[:140]))
    lic = (meta or {}).get('licence') or spec.get('lic', 'see file page')
    credit = '%s \u00b7 %s \u00b7 %s' % (spec['credit'], lic, a(page, 'Wikimedia Commons'))
    alt = html.escape(spec['alt'], quote=True)
    if meta:
        img = '<img src="%s" alt="%s" loading="lazy">' % (uri(meta['files']['main']), alt)
        vals = ''
        if spec.get('values') and 'notan' in meta['files']:
            vals = ('<div class="plate-vals"><figure><img src="%s" alt="%s, colour removed" loading="lazy"><figcaption>Colour removed: the value pattern</figcaption></figure>'
                    '<figure><img src="%s" alt="%s, reduced to two values" loading="lazy"><figcaption>Two values only: the notan</figcaption></figure></div>') % (
                uri(meta['files']['gray']), alt, uri(meta['files']['notan']), alt)
        body = '<div class="plate-img">%s</div>%s' % (img, vals)
        btn = '<button class="sq" type="button" onclick="this.closest(\'figure\').classList.toggle(\'squint\')">Squint test</button>'
    else:
        body = '<a class="plate-out" href="%s" target="_blank" rel="noopener"><b>%s</b><span>Open the image on Wikimedia Commons</span></a>' % (page, spec['credit'])
        btn = ''
    return '<figure class="plate">%s<figcaption><span class="plate-cap">%s</span><span class="credit">%s</span>%s</figcaption></figure>' % (body, p['cap'], credit, btn)


def philo(ph):
    q = '<blockquote>%s</blockquote>' % ph['q'] if ph.get('quote', True) else '<p class="philo-idea">%s</p>' % ph['q']
    src = (' \u00b7 ' + a(ph['src'][1], ph['src'][0])) if ph.get('src') else ''
    return ('<div class="philo"><div class="philo-k">Philosophy</div>%s<p class="philo-who">%s%s</p><p>%s</p>'
            '<p class="philo-q"><b>Argue with it.</b> %s</p></div>') % (q, ph['who'], src, ph['means'], ph['argue'])


def stop(F, st):
    n = st['id']
    o = ['<article class="mod" id="%s" data-mod="%s">' % (mid(n), n),
         '<div class="mod-meta">Part %d \u00b7 Stop %s \u00b7 Day %d <span class="t">20 min</span></div>' % (F['n'], n, st['day']),
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
    plates = {}
    for p in st.get('plates', []):
        plates.setdefault(p.get('after', len(st['story']) - 1), []).append(plate(p))
    paras = ''.join('<p>%s</p>%s' % (p, ''.join(plates.get(i, []))) for i, p in enumerate(st['story']))
    o.append('<h3>The deep answer</h3><div class="story">%s</div>' % paras)
    if st.get('fig'):
        svg, cap = st['fig']
        o.append('<figure class="fig"><div class="scroll">%s</div><figcaption>%s</figcaption></figure>' % (svg, cap))
    if st.get('specs'):
        o.append('<h3>The words insiders use</h3><div class="specs">%s</div>' % ''.join(
            '<div class="spec"><div class="spec-name">%s</div><p class="spec-def">%s</p></div>' % s for s in st['specs']))
    if st.get('philo'):
        o.append(philo(st['philo']))
    if st.get('tags'):
        o.append('<h3>Truth tags</h3><ul class="ttags">%s</ul>' % ''.join(
            '<li><span class="stamp st-%s">%s</span><div><p><b>%s</b> %s</p><span class="src">Source: %s</span></div></li>' % (
                tg, STAMP[tg], claim, fix, a(src[1], src[0])) for tg, claim, fix, src in st['tags']))
    if st.get('distil'):
        o.append('<div class="distil"><div class="distil-k">This stop distils</div><ul>%s</ul></div>' % ''.join(
            '<li>%s<span>%s</span></li>' % (a(u, lab), what) for lab, u, what in st['distil']))
    w = st.get('writer')
    if w:
        o.append('<div class="writer wr"><div class="writer-k">Director\'s eye \u00b7 for No. 08 and No. 09</div>%s<p class="wr-drill"><b>Frame drill.</b> %s</p></div>' % (
            ''.join('<p>%s</p>' % p for p in w['notes']), w['drill']))
    if st.get('biz'):
        o.append('<div class="mtrx biz"><p><b>Studio lens \u00b7 MTRX\u2122.</b> %s</p></div>' % st['biz'])
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
    css = ''
    for f in (os.path.join(ROOT, 'build', '03', 'p3.css'), os.path.join(HERE, 'p7.css')):
        if os.path.exists(f):
            css += open(f, encoding='utf-8').read() + '\n'
    head += '<style id="mtrx-p7-css">%s</style>' % css
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
        return '<script%s>%s</script>' % (m.group(1), m.group(2).replace('mtrx-room-v1', KEY).replace('mtrx-room-log-v1', 'mtrx-design-log-v1'))
    tail = re.sub(r'<script([^>]*)>(.*?)</script>', fix_script, tail, flags=re.S)
    LOG.append('progress key replaced %d times in core scripts' % n_key)
    start = load(os.path.join(HERE, 'start.py'))
    built = {}
    for p in sorted(glob.glob(os.path.join(HERE, 'f[0-9]_*.py')), key=lambda x: [int(z) for z in re.findall(r'\d+', os.path.basename(x))]):
        mod = load(p)
        if mod and hasattr(mod, 'STOP'):
            built[mod.STOP['id']] = mod.STOP
    LOG.append('built stops: %s' % ', '.join(sorted(built, key=lambda s: [int(z) for z in s.split('.')])))
    sources = []
    tabs = [('0', 'Start', 'Start', '0')] + [(str(F['n']), F['title'], F['tab'], F['short']) for F in PLAN]
    nav = '<nav class="thumbs" aria-label="Sections">%s</nav>' % ''.join(
        '<button class="thumb" type="button" data-t="%s" aria-label="%s"><span class="lbl"><span class="full">%s</span>'
        '<span class="short">%s</span></span><i></i></button>' % t for t in tabs)
    nstart = len(start.STOPS) if start else 0
    nbuilt = len(built) + nstart
    total = sum(len(F['stops']) for F in PLAN) + nstart
    cube = ''.join('<a href="%s"><span class="ph">%s</span><img src="https://i.ytimg.com/vi/%s/mqdefault.jpg" alt="Still from %s" loading="lazy" onerror="this.remove()"><b>%s</b></a>' % (
        href, html.escape(lab), vid, html.escape(lab, quote=True), tag) for href, lab, vid, tag in start.CUBE) if start else ''
    cover = ('<header class="wrap cover" id="top" data-sec="0"><div><div class="kicker">MTRX\u2122 Field Series \u00b7 No. 07 \u00b7 October 2026</div>'
             '<h1 class="cover-title">Design and <span class="o">taste</span></h1><p class="cover-sub">%s</p>'
             '<ul class="verbs"><li>See</li><li>Decide</li><li>Make</li></ul>'
             '<p class="prepared">Prepared for <b>Kevin Cecil</b>, founder, MTRX\u2122 Digital, and future director<br>%d stops built of %d planned \u00b7 10 parts \u00b7 20 minutes a day \u00b7 a director\'s eye and a studio lens in every stop<br>Sources checked 23 October 2026</p>'
             '<a class="btn btn-a" href="#m0-1">Start here <span aria-hidden="true">\u2193</span></a></div>'
             '<div class="cover-plate"><nav class="cube6" aria-label="Nine videos in this guide">%s</nav><p class="cube-cap">Nine of the videos inside. Tap one to jump to its stop.</p></div></header>') % (
        start.SUB if start else '', nbuilt, total, cube)
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
            body = '<div class="later"><p>This part is planned and audited. Its stops arrive one part at a time; the question bank in Stop 0.2 shows what each one answers.</p></div>'
        secs.append('<section class="part" id="s%d" data-part="%d" data-sec="%d" data-title="Part %d \u00b7 %s">%s<div class="wrap">%s</div></section>' % (
            F['n'], F['part'], F['n'], F['n'], html.escape(F['title'], quote=True), part_head(F, built), body))
        for st in mine:
            sources += [(lab, u, st['id']) for lab, u, _ in st.get('distil', [])]
            sources += [(src[0], src[1], st['id']) for _, _, _, src in st.get('tags', [])]
    LOG.append('images: %d fetched now of %d tried; cache %s' % (NET['ok'], NET['tried'], 'present' if os.path.isdir(CACHE) else 'absent'))
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

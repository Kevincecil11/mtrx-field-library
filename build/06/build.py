#!/usr/bin/env python3
"""No. 06 Part II splice: python build/06/build.py guides/06-read-the-room.html out.html

Reads the live guide and writes a candidate with Part II spliced in. Part I is
checked byte for byte and never changes. Every insertion sits between
<!-- mtrx:NAME --> markers, so the next drop replaces its own block instead of
stacking a second copy. Content lives in p2_file*.py; diagrams in p2_svgs.py;
styles in p2.css. Stdlib only.
"""
import hashlib, html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p2_file1 as F1  # noqa: E402
import p2_file2 as F2  # noqa: E402
import p2_file3 as F3  # noqa: E402
import p2_file4 as F4  # noqa: E402
import p2_file5 as F5  # noqa: E402
from p2_svgs import SVG  # noqa: E402

FILES = [F1, F2, F3, F4, F5]
for _F in FILES[1:]:
    SVG.update(getattr(_F, 'SVG', {}))
# File 1's intro predates the other files: give it the same, current file list.
F1.INTRO['files'] = [dict(f, now=(f['n'] == 1)) for f in F2.INTRO['files']]
# Files 3 to 5 take over the old watch-ahead sections and keep their plates and scene library.
OLD_SECTION = {3: 's2', 4: 's3', 5: 's5'}
GRADE = {'s': ('g-s', 'Strong'), 'm': ('g-m', 'Moderate'), 'h': ('g-h', 'Weak'), 'x': ('g-x', 'Failed')}
STAMP = {'hold': 'Holds up', 'part': 'Partly', 'myth': 'Myth', 'anti': 'Anti-model', 'field': 'Field test'}
PART_I_SCENES = 24
LATER = {}
TABS = [('0', 'Start', 'Start', '00'), ('1', 'Part I: Read the room', 'Part I', 'I'), ('4', 'File 1: The Spotlight', 'Spotlight', 'II.1'),
        ('6', 'File 2: The Read', 'The Read', 'II.2'), ('2', 'File 3: George Newman', 'Newman', 'II.3'), ('3', 'File 4: Work the network', 'Network', 'II.4'),
        ('5', 'File 5: The line', 'The line', 'II.5')]
LIB_MARK = '<!-- p2lib -->'


def mid(n):
    return 'm' + n.replace('.', '-')


def link(F, key, label=None):
    lab = label or next((a for a, k, _ in F.SOURCES if k == key), key)
    return '<a href="%s" rel="noopener" target="_blank">%s</a>' % (html.escape(F.U[key], quote=True), lab)


def yt_card(sc, small=None):
    t = sc['title']
    th = ('<div class="vid-th"><span class="ph">%s</span><img alt="Still from %s" loading="lazy" onerror="this.remove()" '
          'src="https://i.ytimg.com/vi/%s/mqdefault.jpg"/><span class="play"></span>%s</div>') % (
        t, html.escape(t, quote=True), sc['id'], ('<span class="dur">%s</span>' % sc['dur']) if sc.get('dur') and not small else '')
    meta = small or '%s · <span class="s">%s</span>' % (sc['who'], sc['role'])
    return ('<a class="vid" href="https://www.youtube.com/watch?v=%s" rel="noopener" target="_blank">%s<div class="vid-b">'
            '<div class="vid-t">%s (%s)</div><div class="vid-m">%s</div></div></a>') % (sc['id'], th, t, sc['year'], meta)


def scene(sc):
    return ('<div class="scene">%s<div class="scene-b"><div class="scene-k">%s</div><p class="scene-line">%s</p>'
            '<div class="scene-wh">Watch for</div><ul class="scene-w">%s</ul><p><b>The read.</b> %s</p><p><b>Steal this.</b> %s</p>'
            '<p class="scene-rc"><b>Reality check.</b> %s</p><p class="scene-n">%s</p></div></div>') % (
        yt_card(sc), sc['key'], sc['line'], ''.join('<li>%s</li>' % w for w in sc['watch']), sc['read'], sc['steal'], sc['rc'], sc['note'])


def stop(F, st):
    n = st['id']
    d = st['dossier']
    o = ['<article class="mod" id="%s" data-mod="%s">' % (mid(n), n),
         '<div class="mod-meta">File %d · Stop %s · Day %d <span class="t">20 min</span></div>' % (F.FILE['n'], n, st['day']),
         '<h2 class="mod-title">%s</h2><p class="mod-why">%s</p>' % (st['title'], st['why']),
         '<div class="dossier"><div class="dos-tab">Case file %s</div><div class="dos-body"><div class="dos-k">%s</div>'
         '<div class="dos-name">%s</div><div class="dos-role">%s</div><dl class="dos-facts">%s</dl></div>'
         '<span class="stamp st-%s">%s</span></div>' % (n, d.get('k', 'Subject'), d['name'], d['role'],
                                                         ''.join('<div><dt>%s</dt><dd>%s</dd></div>' % f for f in d['facts']),
                                                         d['stamp'][0], d['stamp'][1]),
         '<div class="predict"><div class="predict-k">Cold open · predict first · 2 min</div><p>%s</p>'
         '<details class="reveal"><summary>Reveal the answer</summary><p>%s</p></details></div>' % (st['cold']['q'], st['cold']['a']),
         '<h3>The story</h3><div class="story">%s</div>' % ''.join('<p>%s</p>' % p for p in st['story']),
         '<div class="move"><div class="move-k">The move</div><p class="move-line">%s</p><ol class="move-steps">%s</ol></div>' % (
             st['move']['line'], ''.join('<li><b>%s</b> %s</li>' % s for s in st['move']['steps']))]
    if st.get('extra'):
        o.append(st['extra'])
    if st['scenes']:
        o.append('<h3>%s</h3>%s' % ('The scenes' if len(st['scenes']) > 1 else 'The scene', ''.join(scene(s) for s in st['scenes'])))
    if st.get('rewatch'):
        cards = [yt_card(sc, 'Stop %s' % s['id']) for s in F.STOPS for sc in s['scenes']]
        o.append('<h3>Warm up: rewatch the file</h3><div class="rewatch">%s</div>' % ''.join(cards))
    o.append('<h3>Why it works</h3><div class="specs">%s</div>' % ''.join(
        '<div class="spec"><div class="spec-name">%s</div><p class="spec-def">%s</p></div>' % s for s in st['specs']))
    key, cap = st['fig']
    o.append('<figure class="fig"><div class="scroll">%s</div><figcaption>%s</figcaption></figure>' % (SVG[key], cap))
    rows = ''.join('<tr><td>%s</td><td><span class="grade %s">%s</span></td><td>%s</td></tr>' % (
        c, GRADE[g][0], GRADE[g][1], link(F, k, lab)) for c, g, lab, k in st['evidence'])
    o.append('<details class="sci"><summary>The evidence, graded</summary><div class="tbl-wrap"><table class="tbl"><thead><tr>'
             '<th>Claim</th><th>Grade</th><th>Source</th></tr></thead><tbody>%s</tbody></table></div></details>' % rows)
    o.append('<h3>Truth tags</h3><ul class="ttags">%s</ul>' % ''.join(
        '<li><span class="stamp st-%s">%s</span><div><p><b>%s</b> %s</p><span class="src">Source: %s</span></div></li>' % (
            t, STAMP[t], claim, fix, link(F, k)) for t, claim, fix, k in st['tags']))
    o.append('<div class="mtrx"><p>%s</p></div>' % st['world'])
    dr = st['drill']
    o.append('<div class="drill"><div class="drill-h"><b>%s</b><span>Drill · %s</span></div><ol>%s</ol>'
             '<p class="drill-x"><b>Usual mistake:</b> %s</p></div>' % (dr['name'], dr['mins'], ''.join('<li>%s</li>' % x for x in dr['steps']), dr['mistake']))
    o.append('<div class="tryit"><div class="tryit-k">Try it · 5 min</div><p>%s</p></div>' % st['tryit'])
    o.append('<div class="writer"><div class="writer-k">Writer\'s note · for No. 08</div><p>%s</p></div>' % st['writer'])
    o.append('<p class="room">%s</p>' % st['room'])
    o.append('<p class="nextq"><b>Your next question.</b> %s</p>' % st['nextq'])
    for c in st['checks']:
        o.append('<div class="check"><script type="application/json">%s</script></div>' % json.dumps(c, ensure_ascii=False))
    o.append('<button class="done" data-mod="%s">Mark stop %s done</button></article>' % (n, n))
    return ''.join(o)


def file_section(F):
    f, I = F.FILE, F.INTRO
    lis = ''.join('<li><a href="#%s"><span>%s</span>%s<em>20 min</em></a></li>' % (mid(s['id']), s['id'], s['title']) for s in F.STOPS)
    files = ''.join('<a class="file%s" href="%s" style="--fc:%s"><span>File %d · %s</span><b>%s</b><em>%s</em></a>' % (
        ' is-now' if x.get('now') else '', x['href'], x['c'], x['n'], x['stops'], x['title'], x['note']) for x in I['files'])
    intro = ('<div class="p2-intro" id="p2-intro"><p class="lede">%s</p><h3>How a case file works</h3><ol class="anatomy">%s</ol>'
             '<h3>The five files</h3><div class="files">%s</div><details class="sci"><summary>The coverage map for File %d</summary>%s</details></div>') % (
        I['lede'], ''.join('<li>%s</li>' % a for a in I['anatomy']), files, f['n'], I['coverage'])
    return ('<section class="part" id="s%s" data-part="%s" data-sec="%s"><div class="part-head"><div class="wrap"><div class="kicker">%s</div>'
            '<h2 class="part-title">%s</h2><p class="part-promise">%s</p><ol class="stops">%s</ol></div></div><div class="wrap">%s%s</div></section>') % (
        f['sec'], f['part'], f['sec'], f['kicker'], f['title'], f['promise'], lis, intro, ''.join(stop(F, s) for s in F.STOPS))


_file_section = file_section


def file_section(F):
    out = _file_section(F)
    n = F.FILE['n']
    return out if n == 1 else out.replace('id="p2-intro"', 'id="p2-intro-%d"' % n, 1)


def later_head(sid):
    k, t, p, items = LATER[sid]
    lis = ''.join('<li><a href="#%s"><span>%s</span>%s<em>soon</em></a></li>' % (sid, n, x) for n, x in items)
    return ('<div class="part-head"><div class="wrap"><div class="kicker">%s</div><h2 class="part-title">%s</h2>'
            '<p class="part-promise">%s</p><ol class="stops">%s</ol></div></div>') % (k, t, p, lis)


def put(s, name, block, at):
    b, e = '<!-- mtrx:%s -->' % name, '<!-- /mtrx:%s -->' % name
    if b in s:
        i = s.index(b)
        j = s.index(e, i) + len(e)
        return s[:i] + b + block + e + s[j:], 'replaced'
    i = at(s)
    if i < 0:
        raise SystemExit('anchor for %s not found' % name)
    return s[:i] + b + block + e + s[i:], 'inserted'


def part1(s):
    i = s.find('<section class="part" id="s1"')
    j = s.find('<section class="part"', i + 10)
    k = s.find('<!-- mtrx:', i + 10)
    j = min(x for x in (j, k) if x > 0)
    return s[i:j]


def after_part1(s):
    i = s.find('<section class="part" id="s1"')
    return s.find('<section class="part"', i + 10) if i >= 0 else -1


def after_last_card(s):
    f = s.find('<footer class="colophon">')
    k = s.rfind('<a class="read-card"', f, s.find('</footer>', f))
    return s.find('</a>', k) + 4 if f >= 0 and k >= 0 else -1


def after_marker(name):
    def at(s):
        e = '<!-- /mtrx:%s -->' % name
        return s.index(e) + len(e) if e in s else -1
    return at


def old_library(s, n, sid):
    """The plates and scene library of the old watch-ahead section, kept under the new file."""
    b, e = '<!-- mtrx:p2f%d -->' % n, '<!-- /mtrx:p2f%d -->' % n
    if b in s:
        blk = s[s.index(b):s.index(e)]
        if LIB_MARK not in blk:
            return ''
        lib = blk[blk.index(LIB_MARK) + len(LIB_MARK):blk.rindex('</section>')]
        head = '<div class="wrap"><h3 class="lib-h">'
        if lib.startswith(head):
            lib = lib[lib.index('</div>') + len('</div>'):]
        return lib
    i = s.find('<section class="part" id="%s"' % sid)
    j = s.find('</section>', i)
    seg = s[i:j]
    k = seg.find('<div class="part-head">')
    end = seg.find('</ol></div></div>', k) + len('</ol></div></div>')
    return seg[end:]


def replace_old(s, n, sid, block):
    b, e = '<!-- mtrx:p2f%d -->' % n, '<!-- /mtrx:p2f%d -->' % n
    if b in s:
        i, j = s.index(b), s.index(e) + len(e)
        return s[:i] + b + block + e + s[j:], 'replaced'
    i = s.find('<section class="part" id="%s"' % sid)
    if i < 0:
        raise SystemExit('old section %s not found' % sid)
    j = s.find('</section>', i) + len('</section>')
    return s[:i] + b + block + e + s[j:], 'took over ' + sid


def main(src, dst):
    s = open(src, encoding='utf-8').read()
    p1 = hashlib.sha256(part1(s).encode()).hexdigest()
    log = []
    css = open(os.path.join(HERE, 'p2.css'), encoding='utf-8').read()
    s, how = put(s, 'p2css', '<style id="mtrx-p2-css">%s</style>' % css, lambda x: x.find('</head>'))
    log.append('css ' + how)
    for F in FILES:
        n = F.FILE['n']
        if n == 1:
            s, how = put(s, 'p2f1', file_section(F), after_part1)
        elif n == 2:
            s, how = put(s, 'p2f2', file_section(F), after_marker('p2f1'))
        else:
            lib = old_library(s, n, OLD_SECTION[n])
            sec = file_section(F)
            if lib.strip():
                sec = sec[:sec.rindex('</section>')] + LIB_MARK + ('<div class="wrap"><h3 class="lib-h">Scene library: more to watch</h3>'
                      '<p class="muted">The plates and scenes from the watch-ahead, kept for rewatching.</p></div>') + lib + '</section>'
            s, how = replace_old(s, n, OLD_SECTION[n], sec)
        log.append('file %d %s: %d stops' % (n, how, len(F.STOPS)))
    for sid in LATER:
        s, n = re.subn(r'(<section class="part" id="%s"[^>]*>)<div class="part-head">.*?</ol></div></div>' % sid,
                       lambda m: m.group(1) + later_head(sid), s, count=1, flags=re.S)
        log.append('%s head %s' % (sid, 'retitled' if n else 'NOT FOUND'))
    nav = '<nav class="thumbs" aria-label="Sections">%s</nav>' % ''.join(
        '<button class="thumb" type="button" data-t="%s" aria-label="%s"><span class="lbl"><span class="full">%s</span>'
        '<span class="short">%s</span></span><i></i></button>' % t for t in TABS)
    s, n = re.subn(r'<nav class="thumbs" aria-label="Sections">.*?</nav>', lambda m: nav, s, count=1, flags=re.S)
    log.append('tabs ' + ('rebuilt' if n else 'NOT FOUND'))
    scenes = PART_I_SCENES + sum(len(st['scenes']) for F in FILES for st in F.STOPS)
    stops = sum(len(F.STOPS) for F in FILES)
    line = ('Part I: 12 stops · Part II: 5 files, %d stops · 20 minutes a day · %d scenes plus the scene library'
            '<br>Sources checked 9 and 14 October 2026, Part II Files 2 to 5 on 27 October 2026') % (stops, scenes)
    s, n = re.subn(r'(<p class="prepared">.*?<br>)(.*?)(</p>)', lambda m: m.group(1) + line + m.group(3), s, count=1, flags=re.S)
    log.append('cover ' + ('updated' if n else 'NOT FOUND'))
    cards = ''.join('<a class="read-card" href="%s" target="_blank" rel="noopener"><b>%s</b><span>Stop %s</span></a>' % (
        html.escape(F.U[k], quote=True), lab, st) for F in FILES for lab, k, st in F.SOURCES)
    s, how = put(s, 'p2src', cards, after_last_card)
    log.append('sources %s: %d cards' % (how, sum(len(F.SOURCES) for F in FILES)))
    if hashlib.sha256(part1(s).encode()).hexdigest() != p1:
        raise SystemExit('Part I changed: refusing to write')
    log.append('Part I unchanged (sha256 %s)' % p1[:12])
    bad = [c for c in ('\u2014', '\u2013') if c in re.sub(r'<(script|style)\b.*?</\1>', ' ', s, flags=re.S)]
    if bad:
        raise SystemExit('dash found in content')
    open(dst, 'w', encoding='utf-8').write(s)
    log.append('wrote %s (%d bytes)' % (dst, len(s)))
    print('\n'.join(log))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

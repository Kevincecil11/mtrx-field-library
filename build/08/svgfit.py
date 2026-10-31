"""Fit SVG diagram text inside its boxes at build time (static, works with JavaScript off).

Each <text> is matched to the smallest <rect> that contains its anchor point. If the label is wider
than the box, it is wrapped onto 2 or 3 lines (the box, and same-row sibling boxes, grow if there is
free space below), else the font is reduced (not below 72%), and as a last resort compressed with
textLength. Widths: JetBrains Mono is 0.6 em per character; sans text uses Nunito Sans advance
widths baked in below (600 for s-t-s, 800 for s-t-b), so CI needs no font files.
"""
import re
import xml.etree.ElementTree as ET

CLS = {'s-t': ('mono', 15), 's-t-sm': ('mono', 14), 's-t-b': ('sans', 19), 's-t-s': ('sans', 16), 's-t-d': ('disp', 34)}
PAD = 8


NS_CHARS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~’‘“”é·×→…ō'
NS_W = {600: [263,237,417,600,600,937,708,230,336,336,451,600,237,429,237,297,600,600,600,600,600,600,600,600,600,600,237,237,600,600,600,450,948,736,682,676,751,589,554,731,767,267,338,643,552,861,743,775,642,775,677,622,611,733,700,1107,660,606,596,333,297,333,600,500,500,537,591,467,591,537,347,594,576,243,246,516,306,866,576,565,591,591,373,484,365,569,520,846,534,520,468,370,276,370,600,237,237,416,416,537,237,600,500,713,565], 800: [278,260,480,600,600,954,745,255,382,382,454,600,260,440,260,331,600,600,600,600,600,600,600,600,600,600,260,260,600,600,600,468,952,753,695,683,774,605,570,742,780,296,373,687,573,876,753,796,664,796,696,641,632,743,727,1120,685,631,615,377,331,377,600,500,500,557,610,478,610,549,382,615,595,268,273,558,333,889,595,589,610,610,412,492,404,590,534,861,559,533,480,414,302,414,600,260,260,472,472,549,260,600,500,780,589]}


def _sans_w(txt, size, wght=800):
    """Nunito Sans advance widths (1000 units, opsz 12, wdth 100), measured from the Google Fonts file."""
    tab = dict(zip(NS_CHARS, NS_W[wght]))
    return sum(tab.get(c, 560) for c in txt) * size / 1000.0


def width(txt, kind, size):
    if kind == 'mono':
        return len(txt) * size * 0.6
    if kind == 'disp':
        return len(txt) * size * 0.5
    return _sans_w(txt, size, 600 if size < 18 else 800)


def _num(v, d=0.0):
    try:
        return float(re.match(r'-?[\d.]+', str(v)).group())
    except (TypeError, AttributeError, ValueError):
        return d


def _offset(el, parents):
    """Sum of translate() on ancestors; None if any other transform is present."""
    dx = dy = 0.0
    node = el
    while node is not None:
        t = node.get('transform')
        if t:
            m = re.fullmatch(r'\s*translate\(\s*(-?[\d.]+)[ ,]*(-?[\d.]*)\s*\)\s*', t)
            if not m:
                return None
            dx += float(m.group(1))
            dy += float(m.group(2) or 0)
        node = parents.get(node)
    return dx, dy


def _inherit(el, parents, attr):
    node = el
    while node is not None:
        if node.get(attr):
            return node.get(attr)
        node = parents.get(node)
    return None


def _split(words, k):
    """Balanced split of words into k lines (greedy on target length)."""
    total = sum(len(w) for w in words) + len(words) - 1
    target = total / k
    lines, cur = [], []
    for w in words:
        if cur and len(' '.join(cur + [w])) > target and len(lines) < k - 1:
            lines.append(' '.join(cur))
            cur = [w]
        else:
            cur.append(w)
    lines.append(' '.join(cur))
    return lines


def _fs(el, size):
    """Inline style beats the class rule (a font-size attribute would lose to .s-t-* CSS)."""
    st = re.sub(r'font-size:[^;]*;?', '', el.get('style') or '').strip()
    el.set('style', ('%s;' % st.rstrip(';') if st else '') + 'font-size:%.1fpx' % size)


def fit(svg, log=None):
    if '<svg' not in svg:
        return svg
    try:
        root = ET.fromstring(svg)
    except ET.ParseError as e:
        if log is not None:
            log.append('svgfit: parse error %s' % e)
        return svg
    parents = {c: p for p in root.iter() for c in p}
    rects = []
    for r in root.iter('rect'):
        off = _offset(r, parents)
        if off is None:
            continue
        x, y = _num(r.get('x')) + off[0], _num(r.get('y')) + off[1]
        w, h = _num(r.get('width')), _num(r.get('height'))
        if w > 30 and h > 14:
            rects.append(dict(el=r, x=x, y=y, w=w, h=h, off=off))
    vb = [_num(v) for v in (root.get('viewBox') or '0 0 1000 400').split()]
    texts = []
    for t in root.iter('text'):
        if len(t):  # has tspans: leave alone
            continue
        off = _offset(t, parents)
        cls = (t.get('class') or '').split()
        kind = next((CLS[c] for c in cls if c in CLS), None)
        if off is None or kind is None or not (t.text or '').strip():
            continue
        m_ = re.search(r'font-size:\s*([\d.]+)', t.get('style') or '')
        size = float(m_.group(1)) if m_ else kind[1]
        x, y = _num(t.get('x')) + off[0], _num(t.get('y')) + off[1]
        texts.append(dict(el=t, x=x, y=y, kind=kind[0], size=size, off=off,
                          anchor=_inherit(t, parents, 'text-anchor') or 'start'))
    changed = 0
    for T in texts:
        txt = T['el'].text.strip()
        inside = [R for R in rects if R['x'] - 1 <= T['x'] <= R['x'] + R['w'] + 1 and R['y'] - 1 <= T['y'] <= R['y'] + R['h'] + 1]
        R = min(inside, key=lambda r: r['w'] * r['h']) if inside else None
        left, right = (R['x'] + PAD, R['x'] + R['w'] - PAD) if R else (vb[0] + 4, vb[0] + vb[2] - 4)
        a, x = T['anchor'], T['x']
        avail = {'start': right - x, 'end': x - left}.get(a, 2 * min(x - left, right - x))
        w = width(txt, T['kind'], T['size'])
        if avail <= 20 or w <= avail + 1:
            continue
        el, size = T['el'], T['size']
        done = False
        words = txt.split()
        heading = T['kind'] in ('sans', 'disp') and T['size'] >= 18
        if heading and w * 0.8 <= avail:
            _fs(el, size * avail / w)
            done = True
        if not done and R and len(words) > 1:
            for k in (2, 3):
                lines = _split(words, k)
                if max(width(l, T['kind'], size) for l in lines) > avail:
                    continue
                lh = size * 1.18
                bottom = T['y'] + (k - 1) * lh + size * 0.32
                below = [o for o in texts if o is not T and R['x'] <= o['x'] <= R['x'] + R['w'] and T['y'] < o['y'] <= R['y'] + R['h']]
                shift = (k - 1) * lh
                need = max(bottom, max([o['y'] + shift + o['size'] * 0.32 for o in below], default=0)) - (R['y'] + R['h'] - 5)
                grow = max(0.0, need)
                if grow:
                    row = [Q for Q in rects if abs(Q['y'] - R['y']) < 1 and abs(Q['h'] - R['h']) < 1]
                    zone = lambda Q: (Q['x'], Q['y'] + Q['h'], Q['x'] + Q['w'], Q['y'] + Q['h'] + grow + 4)
                    def clash(Q):
                        x0, y0, x1, y1 = zone(Q)
                        for P in rects:
                            if P in row or P is Q:
                                continue
                            if P['x'] < x1 and P['x'] + P['w'] > x0 and P['y'] < y1 and P['y'] + P['h'] > y0 and not (P['x'] <= Q['x'] and P['x'] + P['w'] >= Q['x'] + Q['w'] and P['y'] <= Q['y'] and P['y'] + P['h'] >= Q['y'] + Q['h']):
                                return True
                        for o in texts:
                            if x0 <= o['x'] <= x1 and y0 - 2 <= o['y'] - o['size'] * 0.7 <= y1:
                                return True
                        return y1 > vb[1] + vb[3]
                    if any(clash(Q) for Q in row):
                        continue
                    for Q in row:
                        Q['el'].set('height', '%g' % (Q['h'] + grow))
                        Q['h'] += grow
                for o in below:
                    o['el'].set('y', '%g' % (_num(o['el'].get('y')) + shift))
                    o['y'] += shift
                el.text = None
                bx = el.get('x')
                for i, l in enumerate(lines):
                    ts = ET.SubElement(el, 'tspan', {'x': bx})
                    if i:
                        ts.set('dy', '%g' % round(lh, 1))
                    ts.text = l
                done = True
                break
        if not done:
            ratio = max(avail / w, 0.72)
            _fs(el, size * ratio)
            if w * ratio > avail + 1:
                el.set('textLength', '%d' % avail)
                el.set('lengthAdjust', 'spacingAndGlyphs')
        changed += 1
    if not changed:
        return svg
    if log is not None:
        log.append('svgfit: %d labels fitted' % changed)
    out = ET.tostring(root, encoding='unicode', short_empty_elements=True)
    return out.replace('ns0:', '').replace(':ns0', '')

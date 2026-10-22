"""SVG helpers for No. 03 diagrams (house classes from the design system)."""


def box(x, y, w, h, cls='s-card', rx=14):
    return '<rect x="%s" y="%s" width="%s" height="%s" rx="%s" class="%s"/>' % (x, y, w, h, rx, cls)


def t(x, y, s, cls='s-t', anchor='middle'):
    return '<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>' % (cls, x, y, anchor, s)


def arrow(x1, y1, x2, y2, m=False, dash=False):
    return '<path class="%s%s" d="M%s,%s L%s,%s" marker-end="url(#%s)"/>' % (
        's-line-m' if m else 's-line', ' s-dash' if dash else '', x1, y1, x2, y2, 'ahm' if m else 'ah')


def line(x1, y1, x2, y2, m=False, dash=False):
    return '<path class="%s%s" d="M%s,%s L%s,%s"/>' % ('s-line-m' if m else 's-line', ' s-dash' if dash else '', x1, y1, x2, y2)


def circle(cx, cy, r, cls='s-card', op=None):
    st = ' style="fill-opacity:%s"' % op if op else ''
    return '<circle cx="%s" cy="%s" r="%s" class="%s"%s/>' % (cx, cy, r, cls, st)


def svg(w, h, label, inner):
    return '<svg viewBox="0 0 %s %s" role="img" aria-label="%s">%s</svg>' % (w, h, label, inner)

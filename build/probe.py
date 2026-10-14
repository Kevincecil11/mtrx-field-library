#!/usr/bin/env python3
"""Dump the exact raw pieces of a guide an AI needs before splicing a new part:
the main guide script, every part head after Part I, the footer, dark-mode CSS
and the CSS of the stop components. Read only.

Usage: python build/probe.py guides/06-read-the-room.html build/out/06-probe.txt
"""
import re, sys

STRIP = [(r'data:[\w/+.-]+;base64,[A-Za-z0-9+/=]+', lambda m: 'data:[%d]' % len(m.group(0))),
         (r'(<svg\b[^>]*>)(.*?)(</svg>)', lambda m: m.group(1) + '[svg %d]' % len(m.group(2)) + m.group(3))]


def strip(s):
    for p, f in STRIP:
        s = re.sub(p, f, s, flags=re.S)
    return s


def main(src, dst):
    raw = open(src, encoding='utf-8').read()
    o = []
    w = o.append
    # 1. main guide script: the inline script that owns the progress store
    for m in re.finditer(r'<script>(.*?)</script>', raw, re.S):
        if 'button.done' in m.group(1) and 'thumb' in m.group(1):
            w('== 1. main guide script at offset %d (%d chars)\n%s' % (m.start(), len(m.group(1)), m.group(1)))
            break
    # 2. every part section: raw head, then an index of what its body holds
    secs = [(m.start(), m.group(0)) for m in re.finditer(r'<section class="part"[^>]*>', raw)]
    for i, (pos, tag) in enumerate(secs):
        end = secs[i + 1][0] if i + 1 < len(secs) else raw.find('</div>', raw.rfind('</section>')) 
        body = raw[pos:end]
        w('\n== 2. %s at offset %d..%d (%d chars)' % (tag, pos, end, len(body)))
        h = re.search(r'<div class="part-head">.*?</ol></div></div>', body, re.S)
        if h:
            w('-- raw part head (%d chars):\n%s' % (len(h.group(0)), h.group(0)))
        idx = re.findall(r'<h3>(.*?)</h3>|<div class="vids-h">(.*?)</div>|<figure class="([^"]*)"><img[^>]*alt="([^"]*)"|<article class="mod" id="([^"]+)"', body)
        w('-- body index: ' + ' | '.join(next(x for x in t if x) if not t[2] else 'figure.%s: %s' % (t[2], t[3][:60]) for t in idx)[:3000])
        tail = body[-700:]
        w('-- raw tail of section:\n' + strip(tail))
    # 3. everything after the last part section up to the first body script
    last = raw.rfind('</section>')
    sc = raw.find('<script', last)
    w('\n== 3. raw after the last </section> (offset %d) up to the first script (offset %d)\n%s' % (last, sc, strip(raw[last:sc])[:6000]))
    # 4. CSS: dark mode rules and the stop components
    css = '\n'.join(re.findall(r'<style[^>]*>(.*?)</style>', raw, re.S))
    rules = re.findall(r'([^{}]+)\{([^{}]*)\}', css)
    dark = ['%s{%s}' % (a.strip()[:160], b.strip()[:240]) for a, b in rules if 'data-theme="dark"' in a]
    w('\n== 4a. dark-mode rules (%d)\n' % len(dark) + '\n'.join(dark)[:7000])
    want = re.compile(r'(^|[\s,>])\.(mod|mod-meta|mod-title|mod-why|predict|specs|spec|spec-name|spec-def|tryit|writer|room|mtrx|scene|scene-b|scene-k|scene-line|vid|vid-th|part-head|part-title|part-promise|kicker|stops|check|verdict|chip|chips|warn|tbl|grade|g-s|g-m|g-h|lede|big-line|done|thumb|thumbs|cover|prepared|tiles|tile|xlist|oklist)\b')
    comp = ['%s{%s}' % (a.strip()[:140], b.strip()[:300]) for a, b in rules if want.search(a) and 'data-theme' not in a]
    w('\n== 4b. component rules (%d)\n' % len(comp) + '\n'.join(comp)[:12000])
    root = ['%s{%s}' % (a.strip()[:80], b.strip()[:900]) for a, b in rules if a.strip() in (':root', 'html', 'body')]
    w('\n== 4c. root rules\n' + '\n'.join(root)[:3000])
    # 5. stop 0.1 text, svg and data stripped (the coverage map lives here)
    m = re.search(r'<article class="mod" id="m0-1".*?</article>', raw, re.S)
    if m:
        t = strip(m.group(0))
        w('\n== 5. stop 0.1 (%d chars)\n%s' % (len(t), t[:7000]))
    open(dst, 'w', encoding='utf-8').write('\n'.join(o) + '\n')
    print('probe: %s -> %s (%d chars)' % (src, dst, len('\n'.join(o))))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

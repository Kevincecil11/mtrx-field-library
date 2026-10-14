#!/usr/bin/env python3
"""Write a compact structural skeleton of a guide, so an AI can plan edits without
reading 800 KB of HTML. Read only: it never changes the guide.

Usage: python build/skeleton.py guides/06-read-the-room.html build/out/06-skeleton.txt
"""
import re, sys
from bs4 import BeautifulSoup, NavigableString, Comment, Tag

CAP = {'D': 9000, 'E': 22000, 'F': 16000, 'G': 9000, 'H': 6000}


def squash(t, n=90):
    t = re.sub(r'\s+', ' ', t or '').strip()
    return t if len(t) <= n else t[:n] + '...'


def val(v, n=70):
    if isinstance(v, list):
        v = ' '.join(v)
    v = re.sub(r'data:[\w/+.-]+;base64,[A-Za-z0-9+/=]+', lambda m: 'data:[%d]' % len(m.group(0)), v)
    return squash(v, n)


def stag(el, n=70):
    a = ' '.join('%s="%s"' % (k, val(v, n)) for k, v in el.attrs.items())
    return '<%s%s>' % (el.name, (' ' + a) if a else '')


def outline(el, depth, maxd, out, budget, stop_fold=True):
    for ch in el.children:
        if sum(len(x) for x in out) > budget:
            out.append('  ' * depth + '[cut: budget]')
            return
        if isinstance(ch, Comment):
            out.append('  ' * depth + '<!--%s-->' % squash(str(ch), 60))
        elif isinstance(ch, NavigableString):
            t = squash(str(ch), 80)
            if t:
                out.append('  ' * depth + '"%s"' % t)
        elif isinstance(ch, Tag):
            pos = 'L%s' % ch.sourceline if ch.sourceline else ''
            if ch.name in ('svg', 'script', 'style', 'template'):
                out.append('  ' * depth + '%s %s [%d chars inside] %s' % (stag(ch), ch.name, len(ch.decode_contents()), pos))
                continue
            if stop_fold and ch.name == 'article' and ch.get('data-mod'):
                ttl = ch.find(class_='mod-title')
                out.append('  ' * depth + '%s TITLE="%s" [%d chars] %s' % (stag(ch), squash(ttl.get_text(' ') if ttl else '', 60), len(str(ch)), pos))
                continue
            out.append('  ' * depth + stag(ch) + ' ' + pos)
            if depth < maxd:
                outline(ch, depth + 1, maxd, out, budget, stop_fold)
            else:
                kids = [k for k in ch.children if isinstance(k, Tag)]
                if kids:
                    out.append('  ' * (depth + 1) + '[%d child tags: %s]' % (len(kids), ', '.join(sorted({k.name for k in kids}))))
                else:
                    t = squash(ch.get_text(' '), 80)
                    if t:
                        out.append('  ' * (depth + 1) + '"%s"' % t)


def strip_markup(s):
    s = re.sub(r'data:[\w/+.-]+;base64,[A-Za-z0-9+/=]+', lambda m: 'data:[%d]' % len(m.group(0)), s)
    s = re.sub(r'(<svg\b[^>]*>)(.*?)(</svg>)', lambda m: m.group(1) + '[svg %d chars]' % len(m.group(2)) + m.group(3), s, flags=re.S)
    s = re.sub(r'(<script\b[^>]*>)(.{400,}?)(</script>)', lambda m: m.group(1) + m.group(2)[:300] + '[...%d chars]' % len(m.group(2)) + m.group(3), s, flags=re.S)
    return s


def main(src, dst):
    raw = open(src, encoding='utf-8').read()
    soup = BeautifulSoup(raw, 'html.parser')
    o = []
    w = o.append
    w('SKELETON of %s (%d bytes, %d lines)' % (src, len(raw), raw.count('\n') + 1))
    mods = [b.get('data-mod') for b in soup.select('button.done[data-mod]')]
    w('\n== A. stops (button.done data-mod, document order): %d\n%s' % (len(mods), ' '.join(mods)))
    arts = soup.select('article[data-mod]')
    w('articles with data-mod: %d | ids: %s' % (len(arts), ' '.join('%s=%s' % (a.get('data-mod'), a.get('id')) for a in arts)))
    parts = sorted({x.get('data-part') for x in soup.select('[data-part]')})
    w('data-part values: %s' % parts)
    w('elements with data-t: %s' % ' | '.join(stag(x, 40) for x in soup.select('[data-t]'))[:1500])
    w('counts: details=%d, .check=%d, .drill=%d, .room=%d, figure=%d, img=%d, svg=%d, a.yt/watch-like=%d' % (
        len(soup.find_all('details')), len(soup.select('div.check')), len(soup.select('div.drill')),
        len(soup.select('.room')), len(soup.find_all('figure')), len(soup.find_all('img')), len(soup.find_all('svg')),
        len(soup.select('a[href*="youtube"], a[href*="youtu.be"]'))))
    w('\n== B. head')
    head = soup.head
    for el in head.find_all(['meta', 'title', 'link']):
        w('  ' + stag(el, 120) + (' ' + squash(el.get_text(), 100) if el.name == 'title' else ''))
    for i, el in enumerate(soup.find_all(['style', 'script'])):
        where = 'head' if el.find_parent('head') else 'body'
        w('  #%d %s %s %s chars=%d L%s first=%r' % (i, where, el.name, ' '.join('%s=%s' % (k, val(v, 50)) for k, v in el.attrs.items()),
                                                 len(el.decode_contents()), el.sourceline, squash(el.decode_contents(), 70)))
    css = '\n'.join(el.decode_contents() for el in soup.find_all('style'))
    cls = sorted(set(re.findall(r'\.([a-zA-Z][\w-]*)', re.sub(r'url\([^)]*\)|"[^"]*"', '', css))))
    w('\n== C. CSS: %d chars, %d classes\n%s' % (len(css), len(cls), ' '.join(cls)))
    w('custom props: %s' % ' '.join(sorted(set(re.findall(r'(--[\w-]+)\s*:', css))))[:2500])
    dp = [squash(l, 220) for l in re.split(r'}', css) if 'data-part' in l][:30]
    w('data-part rules:\n  ' + '\n  '.join(dp))
    w('media queries: %s' % ' | '.join(sorted(set(re.findall(r'@media[^{]+', css))))[:1200])
    w('\n== D. body outline (stop articles folded)')
    d = []
    outline(soup.body, 0, 5, d, CAP['D'])
    w('\n'.join(d))
    w('\n== E. one full stop, svg and data stripped')
    pick = None
    for want in ('1.8', '1.6', '1.2'):
        pick = soup.select_one('article[data-mod="%s"]' % want)
        if pick:
            break
    if pick is None and arts:
        pick = arts[0]
    if pick is not None:
        s = strip_markup(str(pick))
        w(s[:CAP['E']] + ('\n[cut %d more chars]' % (len(s) - CAP['E']) if len(s) > CAP['E'] else ''))
    w('\n== F. after the last Part I stop: outline')
    last1 = [a for a in arts if str(a.get('data-mod', '')).startswith('1.')]
    if last1:
        la = last1[-1]
        f = []
        node = la
        seen = 0
        # walk following siblings up the tree
        cur = la
        while cur is not None and cur.name != 'body':
            for sib in cur.next_siblings:
                if isinstance(sib, Tag):
                    f.append(stag(sib) + ' L%s' % sib.sourceline)
                    outline(sib, 1, 6, f, CAP['F'], stop_fold=False)
                elif isinstance(sib, NavigableString) and not isinstance(sib, Comment) and squash(str(sib)):
                    f.append('"%s"' % squash(str(sib)))
                if sum(len(x) for x in f) > CAP['F']:
                    f.append('[cut: budget]')
                    break
            f.append('[end of siblings inside %s]' % stag(cur.parent, 40) if cur.parent else '')
            cur = cur.parent
            if sum(len(x) for x in f) > CAP['F']:
                break
        w('\n'.join(f))
        i = raw.find('data-mod="%s"' % la.get('data-mod'))
        j = raw.find('</article>', raw.find('<article', i - 2000 if i > 2000 else 0) if i >= 0 else 0)
        k = raw.rfind('<article', 0, i)
        end = raw.find('</article>', i)
        w('\n-- raw boundary after the last Part I article (offset %d):\n%s' % (end, strip_markup(raw[end:end + 1500])))
    w('\n== G. JS excerpts (keywords)')
    g = []
    keys = re.compile(r"data-t|thumbs|\.done|data-mod|localStorage|mtrx-room|part|hash|scrollIntoView|nk:", re.I)
    for i, el in enumerate(soup.find_all('script')):
        js = el.decode_contents()
        if len(js) < 200 or el.get('type') == 'application/json':
            continue
        lines = re.split(r'(?<=[;{}])\s*', js)
        hits = [squash(l, 200) for l in lines if keys.search(l)]
        if hits:
            g.append('-- script #%d (%d chars) %s' % (i, len(js), ' '.join('%s=%s' % (k, val(v, 40)) for k, v in el.attrs.items())))
            g.extend('   ' + h for h in hits[:40])
        if sum(len(x) for x in g) > CAP['G']:
            g.append('[cut: budget]')
            break
    w('\n'.join(g))
    w('\n== H. raw head of body (first 3000 chars after <body>), stripped')
    b = raw.find('<body')
    w(strip_markup(raw[b:b + 6000])[:CAP['H']])
    open(dst, 'w', encoding='utf-8').write('\n'.join(o) + '\n')
    print('skeleton: %s -> %s (%d chars)' % (src, dst, len('\n'.join(o))))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

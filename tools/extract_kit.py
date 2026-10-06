#!/usr/bin/env python3
"""Extract the house design system and reader kit from a built guide, to start a new guide.
  python3 tools/extract_kit.py guides/05-long-game.html kit/
Writes: house.css (design system), reader-kit.css + reader-kit.js (notes, highlighter, dark mode,
search), guide-core.js (progress, quick checks, tabs) and head-snippets.html."""
import os, re, sys

src, out = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else 'kit')
s = open(src, encoding='utf-8').read()
os.makedirs(out, exist_ok=True)
styles = re.findall(r'<style([^>]*)>(.*?)</style>', s, re.S)
scripts = [(a, b) for a, b in re.findall(r'<script([^>]*)>(.*?)</script>', s, re.S) if 'json' not in a and 'src=' not in a]
house = max((b for a, b in styles if 'id=' not in a), key=len)
files = {
    'house.css': house,
    'reader-kit.css': next(b for a, b in styles if 'mtrx-kit-css' in a),
    'reader-kit.js': next(b for a, b in scripts if 'mtrx-kit-js' in a),
    'guide-core.js': max((b for a, b in scripts if 'id=' not in a), key=len),
    'head-snippets.html': '\n'.join('<script>%s</script>' % b for a, b in scripts if len(b) < 400) + '\n',
}
for name, body in files.items():
    open(os.path.join(out, name), 'w', encoding='utf-8').write(body.strip() + '\n')
    print('%-20s %6d bytes' % (name, len(body)))

#!/usr/bin/env python3
"""Lint a guide before publishing: python3 tools/check_guide.py guides/03-cons-and-cults.html
Checks the house rules in AGENTS.md that a machine can check. Exit code 1 on any error."""
import collections, re, sys

def check(path):
    s = open(path, encoding='utf-8').read()
    errs, warns = [], []
    text = re.sub(r'<(script|style)\b.*?</\1>', ' ', s, flags=re.S)
    for ch, name in (('\u2014', 'em dash'), ('\u2013', 'en dash')):
        if ch in text:
            i = text.index(ch)
            errs.append('%s in content near: %r' % (name, re.sub(r'<[^>]+>', '', text[max(0, i - 60):i + 20])))
    ids = collections.Counter(re.findall(r'\sid="([^"]+)"', s))
    dup = [k for k, v in ids.items() if v > 1]
    if dup:
        errs.append('duplicate ids: %s' % dup[:10])
    mods = collections.Counter(re.findall(r'<button[^>]*class="done[^"]*"[^>]*data-mod="([^"]+)"', s))
    if not mods:
        errs.append('no <button class="done" data-mod> found (progress and the review bot need them)')
    if [k for k, v in mods.items() if v > 1]:
        errs.append('stop ids reused: %s' % [k for k, v in mods.items() if v > 1])
    tag = '<script src="../assets/mtrx-review.js" defer></script>'
    if s.count(tag) != 1 or s.rfind(tag) > s.rfind('</body>') or s.rfind('</body>') - s.rfind(tag) > len(tag) + 3:
        errs.append('shared add-on tag must appear once, right before the last </body>: ' + tag)
    for bad in ('_files/', '?view=open', 'saved from url'):
        if bad in s:
            errs.append('leftover from a browser "Save page": %s' % bad)
    if 'name="mtrx-slug"' not in s:
        warns.append('no <meta name="mtrx-slug">: notes and highlights key off the title, so never rename it')
    if 'id="mtrx-kit-js"' not in s:
        errs.append('reader kit missing (notes, highlighter, dark mode, search)')
    if re.search(r'<img[^>]+src="(?!data:|https://i\.ytimg\.com)', s):
        warns.append('an <img> is not inlined as base64 (only YouTube thumbnails may be remote)')
    print('%s: %d stops, %d errors, %d warnings' % (path, len(mods), len(errs), len(warns)))
    for e in errs:
        print('  ERROR ' + e)
    for w in warns:
        print('  warn  ' + w)
    return not errs

if __name__ == '__main__':
    ok = all([check(p) for p in sys.argv[1:]]) if sys.argv[1:] else False
    sys.exit(0 if ok else 1)

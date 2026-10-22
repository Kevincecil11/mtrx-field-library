#!/usr/bin/env python3
"""Audit and balance the multiple-choice checks in the guides. Stdlib only.

  python3 tools/quiz_audit.py                      audit every guide, print the report
  python3 tools/quiz_audit.py --fix                also rebalance answer positions in place
  python3 tools/quiz_audit.py --fix FILE ...       only these files (build/run.py uses this on the No. 06 candidate)
  --report PATH                                    also write the report to PATH

A check is <div class="check"><script type="application/json">{"q","o","a","w"}</script>.
--fix moves the right answer to a balanced, unpredictable position and orders the
distractors by a hash, so the result depends only on the question, never on the old
order: running it twice changes nothing. Checks are skipped (left as they are) when
an option or the explanation points at positions ("all of the above", "B", "both"),
when options are a numeric scale, or when option text also appears as static HTML.
A fixed file is kept only if tools/check_guide.py is no worse on it than before.
Length bias (the right answer is the longest, most careful option) cannot be fixed
by a script: the report lists the worst cases for a content repair.
"""
import glob, hashlib, json, os, re, subprocess, sys, tempfile
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECK = re.compile(r'(<div class="check"><script type="application/json">)(.*?)(</script>)', re.S)
POSREF = re.compile(r'\b(all|none|both|neither) of (the )?(above|these|them)\b|^\s*(both|neither|all|none)\b|'
                    r'\b(option|answer|choice) [A-F]\b|\([A-F]\)|\b[A-F] and [A-F]\b|\b[A-F]\)', re.I)
NUMERIC = re.compile(r'^\W*\d')


def clean(s):
    s = re.sub(r'<[^>]+>', '', s or '')
    return re.sub(r'\s+', ' ', s).strip()


def h(s):
    return int(hashlib.sha1(s.encode('utf-8')).hexdigest(), 16)


def stop_of(s, pos):
    m = None
    for m in re.finditer(r'<article\b[^>]*data-mod="([^"]+)"', s[:pos]):
        pass
    return m.group(1) if m else '?'


def scan(s):
    out = []
    for m in CHECK.finditer(s):
        try:
            d = json.loads(m.group(2))
            o, a = list(d['o']), int(d['a'])
        except (ValueError, KeyError, TypeError):
            continue
        if not 0 <= a < len(o) or len(o) < 2:
            continue
        out.append((m, d, o, a))
    return out


def why_skip(s, m, d, o):
    texts = [clean(x) for x in o]
    if any(POSREF.search(t) for t in texts) or POSREF.search(clean(d.get('w', ''))):
        return 'points at positions'
    if all(NUMERIC.match(t) for t in texts):
        return 'numeric scale'
    tail = s[m.end():m.end() + 4000]
    close = tail.find('</div>')
    after = tail[:close if close >= 0 else 0]
    if any(t and len(t) > 12 and t in clean(after) for t in texts):
        return 'static options in HTML'
    return ''


def stats(s):
    items = scan(s)
    pos, longest, ratios, worst = Counter(), 0, [], []
    for m, d, o, a in items:
        L = [len(clean(x)) for x in o]
        pos['%d of %d' % (a + 1, len(o))] += 1
        if L[a] == max(L) and L.count(max(L)) == 1:
            longest += 1
        others = [l for i, l in enumerate(L) if i != a]
        r = L[a] / max(1.0, sum(others) / len(others))
        ratios.append(r)
        if r >= 1.6:
            worst.append((r, stop_of(s, m.start()), clean(d['q'])[:70]))
    ratios.sort()
    med = ratios[len(ratios) // 2] if ratios else 0
    return len(items), pos, longest, med, sorted(worst, reverse=True)


def balance(s):
    items = scan(s)
    counts, last, plan, skipped = Counter(), [], {}, Counter()
    for m, d, o, a in items:
        reason = why_skip(s, m, d, o)
        if reason:
            skipped[reason] += 1
            continue
        n = len(o)
        least = min(counts[i] for i in range(n))
        cands = [i for i in range(n) if counts[i] == least]
        if len(last) >= 2 and last[-1] == last[-2] and len(cands) > 1 and last[-1] in cands:
            cands.remove(last[-1])
        key = clean(d['q']) + '|' + clean(o[a])
        t = cands[h(key) % len(cands)]
        counts[t] += 1
        last.append(t)
        right = o[a]
        rest = sorted((x for i, x in enumerate(o) if i != a), key=lambda x: h(clean(x)))
        new = rest[:t] + [right] + rest[t:]
        plan[m.start()] = (m, dict(d, o=new, a=t))
    if not plan:
        return s, 0, skipped
    parts, prev, changed = [], 0, 0
    for start in sorted(plan):
        m, nd = plan[start]
        if nd['o'] != items[[x[0].start() for x in items].index(start)][2] or nd['a'] != items[[x[0].start() for x in items].index(start)][3]:
            changed += 1
        js = json.dumps(nd, ensure_ascii=True).replace('</', '<\\/')
        parts += [s[prev:m.start(2)], js]
        prev = m.end(2)
    parts.append(s[prev:])
    return ''.join(parts), changed, skipped


def lint(path):
    tool = os.path.join(ROOT, 'tools', 'check_guide.py')
    if not os.path.exists(tool):
        return 0, ''
    r = subprocess.run([sys.executable, tool, path], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def line(name, s):
    n, pos, longest, med, worst = stats(s)
    if not n:
        return '%s: no multiple-choice checks' % name, []
    by_n = {}
    for k, v in pos.items():
        i, tot = k.split(' of ')
        by_n.setdefault(int(tot), Counter())[int(i)] = v
    dist = '; '.join('%d options: %s' % (tot, ' '.join('%s=%d' % ('ABCDEF'[i - 1], c[i]) for i in range(1, tot + 1)))
                     for tot, c in sorted(by_n.items()))
    return ('%s: %d checks | right-answer position %s | right answer is the longest option in %d of %d (%d%%) | '
            'median length ratio %.2f' % (name, n, dist, longest, n, round(100 * longest / n), med)), worst


def main(argv):
    fix = '--fix' in argv
    report = argv[argv.index('--report') + 1] if '--report' in argv else None
    files = [a for a in argv if a.endswith('.html')] or sorted(glob.glob(os.path.join(ROOT, 'guides', '[0-9][0-9]-*.html')))
    rep, worst_all = [], []
    for path in files:
        name = os.path.basename(path)
        s = open(path, encoding='utf-8').read()
        before, worst = line(name, s)
        rep.append('BEFORE ' + before)
        worst_all += [(r, name[:2], st, q) for r, st, q in worst]
        if fix:
            new, changed, skipped = balance(s)
            note = 'changed %d checks; skipped %s' % (changed, dict(skipped) or 'none')
            if changed:
                rc0, out0 = lint(path)
                tmp = tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8')
                tmp.write(new); tmp.close()
                rc1, out1 = lint(tmp.name)
                os.unlink(tmp.name)
                out0 = out0.replace(path, 'F').replace(os.path.basename(path), 'F')
                out1 = out1.replace(tmp.name, 'F').replace(os.path.basename(tmp.name), 'F')
                if rc1 == 0 or (rc1 == rc0 and out1.count('\n') <= out0.count('\n')):
                    open(path, 'w', encoding='utf-8').write(new)
                    rep.append('AFTER  ' + line(name, new)[0] + ' | ' + note)
                else:
                    rep.append('KEPT OLD %s: lint got worse after balancing (%s)' % (name, out1.strip()[:300]))
            else:
                rep.append('AFTER  unchanged | ' + note)
    for path in files:                                   # markup notes for the next session
        s = open(path, encoding='utf-8').read()
        m = CHECK.search(s)
        if m:
            rep.append('')
            rep.append('Markup after the first check in %s: %r' % (os.path.basename(path), s[m.end():m.end() + 400]))
            js = [x for x in re.finditer(r'\.check\b|"check"|\'check\'', s) if not s[max(0, x.start() - 60):x.start()].count('<div ')]
            if js:
                rep.append('Script near the first check reference: %r' % s[max(0, js[0].start() - 200):js[0].start() + 300])
            break
    rep.append('')
    rep.append('Worst length bias (right answer at least 1.6x the average distractor), for a content repair:')
    for r, g, st, q in sorted(worst_all, reverse=True)[:25]:
        rep.append('  %.1fx  No. %s stop %s: %s' % (r, g, st, q))
    text = '\n'.join(rep) + '\n'
    if report:
        os.makedirs(os.path.dirname(os.path.join(ROOT, report)) or '.', exist_ok=True)
        open(os.path.join(ROOT, report), 'w', encoding='utf-8').write(text)
    print(text)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

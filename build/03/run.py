#!/usr/bin/env python3
"""No. 03 pipeline (.github/workflows/guide-03.yml runs it on pushes to build/03/).
1. Probe: writes build/out/03-probe.txt (shell facts from No. 06, the shared add-on, index.html).
2. If build/03/build.py exists: builds build/out/03-candidate.html, balances quizzes, lints,
   and only a clean candidate replaces guides/03-cons-and-cults.html. Report: build/out/03-report.txt.
"""
import datetime, os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
os.makedirs('build/out', exist_ok=True)
rep = ['build %s UTC' % datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M')]


def run(*cmd):
    r = subprocess.run([sys.executable] + list(cmd), capture_output=True, text=True)
    rep.append('$ %s (exit %d)\n%s%s' % (' '.join(cmd), r.returncode, r.stdout[-6000:], r.stderr[-4000:]))
    return r.returncode


def nob64(x):
    return re.sub(r'data:[a-z/+-]+;base64,[A-Za-z0-9+/=]+', 'data:...', x)


def probe():
    out = []
    g = open('guides/06-read-the-room.html', encoding='utf-8').read()
    out.append('== 06 size %d' % len(g))
    for a, b in re.findall(r'<(style|script)([^>]*)>', g)[:40]:
        pass
    for m in re.finditer(r'<(style|script)([^>]*)>(.*?)</\1>', g, re.S):
        out.append('tag <%s%s> %d bytes' % (m.group(1), m.group(2)[:80], len(m.group(3))))
    head = re.sub(r'<(style|script)([^>]*)>.*?</\1>', lambda m: '<%s%s>...</%s>' % (m.group(1), m.group(2), m.group(1)), g[:g.find('<body')], flags=re.S)
    out.append('== head\n' + nob64(head)[:3000])
    body = g[g.find('<body'):]
    out.append('== body start\n' + nob64(body)[:5000])
    i = body.find('<section class="part" id="s0"')
    out.append('== s0\n' + nob64(body[i:i + 3500]) if i >= 0 else '== no s0')
    i = body.find('<footer')
    out.append('== footer\n' + nob64(body[i:i + 2500]))
    out.append('== tail\n' + nob64(body[-1500:]))
    sects = re.findall(r'<section[^>]*>', body)
    out.append('== sections\n' + '\n'.join(sects[:30]))
    scripts = [b for a, b in re.findall(r'<script([^>]*)>(.*?)</script>', g, re.S) if 'json' not in a and 'src=' not in a]
    core = max(scripts, key=len) if scripts else ''
    pat = re.compile(r'localStorage|sessionStorage|t\.me|makingmesmart|p0|slug|data-t|thumb|\.check|check-|done|progress|data-mod|data-part|data-sec|prepared|nojs|guide', re.I)
    out.append('== core js %d bytes, matching lines' % len(core))
    for ln in core.split('\n'):
        if pat.search(ln):
            for mm in pat.finditer(ln):
                out.append('  ' + ln[max(0, mm.start() - 110):mm.start() + 110].strip())
                break
    for small in [b for b in scripts if len(b) < 400]:
        out.append('== small script: ' + small[:400])
    if os.path.exists('assets/mtrx-review.js'):
        a = open('assets/mtrx-review.js', encoding='utf-8').read()
        out.append('== assets/mtrx-review.js %d bytes' % len(a))
        out.append(a[:2500])
        for mm in re.finditer(r'guide|0[0-9]|location|pathname|meta', a):
            out.append('  ' + a[max(0, mm.start() - 90):mm.start() + 110].replace('\n', ' '))
    idx = open('index.html', encoding='utf-8').read()
    out.append('== index.html %d bytes' % len(idx))
    for m in re.finditer(r'<a[^>]*class="[^"]*card[^"]*"[^>]*>', idx):
        out.append('  card tag: ' + m.group(0)[:200])
    j = idx.find('06-read-the-room')
    out.append('== index around 06\n' + nob64(idx[max(0, j - 1500):j + 2500]))
    j = idx.find('03')
    out.append('== index first 03 mention\n' + nob64(idx[max(0, j - 300):j + 600]))
    p2 = re.search(r'<style id="mtrx-p2-css">(.*?)</style>', g, re.S)
    if p2:
        out.append('== p2 css classes: ' + ' '.join(sorted(set(re.findall(r'\.([a-z][a-z0-9-]+)', p2.group(1))))))
    house = max((b for a, b in re.findall(r'<style([^>]*)>(.*?)</style>', g, re.S) if 'id=' not in a), key=len)
    out.append('== house css %d bytes, root vars: %s' % (len(house), re.search(r':root\{[^}]*\}', house).group(0)[:1500] if re.search(r':root\{[^}]*\}', house) else 'none'))
    out.append('== data-part rules: ' + ' | '.join(re.findall(r'\[data-part="?\d"?\][^{]*\{[^}]*\}', house)[:8]))
    open('build/out/03-probe.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')


probe()
status = 'probe only'
GUIDE, CAND = 'guides/03-cons-and-cults.html', 'build/out/03-candidate.html'
if os.path.exists('build/03/build.py'):
    if os.path.exists(CAND):
        os.remove(CAND)
    if run('build/03/build.py', CAND) == 0 and os.path.exists(CAND):
        run('tools/quiz_audit.py', '--fix', CAND)
        if run('tools/check_guide.py', CAND) == 0:
            shutil.copyfile(CAND, GUIDE)
            status = 'candidate passed lint and replaced the guide'
            if os.path.exists('build/03/index_card.py'):
                run('build/03/index_card.py', GUIDE, 'index.html')
        else:
            status = 'candidate FAILED lint, guide unchanged'
    else:
        status = 'build FAILED, guide unchanged'
    if os.path.exists(CAND):
        os.remove(CAND)
rep.insert(1, 'status: ' + status)
open('build/out/03-report.txt', 'w', encoding='utf-8').write('\n'.join(rep) + '\n')
print('\n'.join(rep))

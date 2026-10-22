#!/usr/bin/env python3
"""No. 03 pipeline (.github/workflows/guide-03.yml runs it on pushes to build/03/).
1. Probe: writes build/out/03-probe.txt (shell facts from No. 06), only if missing.
2. If build/03/build.py exists: builds build/out/03-candidate.html, renames the No. 06
   storage keys it inherited (mtrx-room-*) to No. 03 keys (mtrx-cons-*), balances quizzes,
   lints, and only a clean candidate replaces guides/03-cons-and-cults.html.
3. Syncs the library card and runs the headless QA. Report: build/out/03-report.txt.
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
    for m in re.finditer(r'<(style|script)([^>]*)>(.*?)</\1>', g, re.S):
        out.append('tag <%s%s> %d bytes' % (m.group(1), m.group(2)[:80], len(m.group(3))))
    body = g[g.find('<body'):]
    out.append('== body start\n' + nob64(body)[:5000])
    open('build/out/03-probe.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')


if not os.path.exists('build/out/03-probe.txt'):
    probe()
status = 'no build.py yet'
GUIDE, CAND = 'guides/03-cons-and-cults.html', 'build/out/03-candidate.html'
if os.path.exists('build/03/build.py'):
    if os.path.exists(CAND):
        os.remove(CAND)
    if run('build/03/build.py', CAND) == 0 and os.path.exists(CAND):
        s = open(CAND, encoding='utf-8').read()
        rep.append('renamed %d inherited No. 06 storage keys (mtrx-room-*) to mtrx-cons-*' % s.count('mtrx-room-'))
        open(CAND, 'w', encoding='utf-8').write(s.replace('mtrx-room-', 'mtrx-cons-'))
        run('tools/quiz_audit.py', '--fix', CAND)
        if run('tools/check_guide.py', CAND) == 0:
            shutil.copyfile(CAND, GUIDE)
            status = 'candidate passed lint and replaced the guide'
            if os.path.exists('build/03/index_card.py'):
                run('build/03/index_card.py', GUIDE, 'index.html')
            if os.path.exists('build/03/qa.py'):
                run('build/03/qa.py')
        else:
            status = 'candidate FAILED lint, guide unchanged'
    else:
        status = 'build FAILED, guide unchanged'
    if os.path.exists(CAND):
        os.remove(CAND)
rep.insert(1, 'status: ' + status)
open('build/out/03-report.txt', 'w', encoding='utf-8').write('\n'.join(rep) + '\n')
print('\n'.join(rep))

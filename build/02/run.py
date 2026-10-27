#!/usr/bin/env python3
"""No. 02 pipeline (.github/workflows/guide-02.yml runs it on pushes to build/02/).
Splices Weeks 3 and 4 into guides/02-mind.html via build/02/build.py (idempotent: it
re-renders between the mtrx:w3 / mtrx:w4 markers and hash-protects days 1 to 14),
lints the candidate, and only a clean candidate replaces the guide. Then the library
card is synced. Report: build/out/02-report.txt."""
import datetime, os, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
os.makedirs('build/out', exist_ok=True)
rep = ['build %s UTC' % datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M')]
GUIDE, CAND = 'guides/02-mind.html', 'build/out/02-candidate.html'


def run(*cmd):
    r = subprocess.run([sys.executable] + list(cmd), capture_output=True, text=True)
    rep.append('$ %s (exit %d)\n%s%s' % (' '.join(cmd), r.returncode, r.stdout[-6000:], r.stderr[-4000:]))
    return r.returncode


status = 'no build.py, guide unchanged'
if os.path.exists('build/02/build.py'):
    if os.path.exists(CAND):
        os.remove(CAND)
    if run('build/02/build.py', GUIDE, CAND) == 0 and os.path.exists(CAND):
        if run('tools/check_guide.py', CAND) == 0:
            shutil.copyfile(CAND, GUIDE)
            status = 'candidate passed lint and replaced the guide'
        else:
            status = 'candidate FAILED lint, guide unchanged'
    else:
        status = 'build FAILED, guide unchanged'
    if os.path.exists(CAND):
        os.remove(CAND)
run('tools/check_guide.py', GUIDE)
run('build/02/index_card.py', GUIDE, 'index.html')
rep.insert(1, 'status: ' + status)
open('build/out/02-report.txt', 'w', encoding='utf-8').write('\n'.join(rep) + '\n')
print('\n'.join(rep))

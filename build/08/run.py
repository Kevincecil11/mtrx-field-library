#!/usr/bin/env python3
"""No. 08 pipeline (.github/workflows/guide-08.yml runs it on pushes to build/08/).
Builds build/out/08-candidate.html from the No. 02 shell plus build/08 sources, lints it,
and only a clean candidate replaces guides/08-screenwriting.html. Then the library card is synced.
Report: build/out/08-report.txt."""
import datetime, os, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
os.makedirs('build/out', exist_ok=True)
rep = ['build %s UTC' % datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M')]
SHELL, GUIDE, CAND = 'guides/02-mind.html', 'guides/08-screenwriting.html', 'build/out/08-candidate.html'


def run(*cmd):
    r = subprocess.run([sys.executable] + list(cmd), capture_output=True, text=True)
    rep.append('$ %s (exit %d)\n%s%s' % (' '.join(cmd), r.returncode, r.stdout[-6000:], r.stderr[-4000:]))
    return r.returncode


status = 'build FAILED, guide unchanged'
if os.path.exists(CAND):
    os.remove(CAND)
if run('build/08/build.py', SHELL, CAND) == 0 and os.path.exists(CAND):
    if run('tools/check_guide.py', CAND) == 0:
        shutil.copyfile(CAND, GUIDE)
        status = 'candidate passed lint and replaced the guide'
    else:
        status = 'candidate FAILED lint, guide unchanged'
if os.path.exists(CAND):
    os.remove(CAND)
if os.path.exists(GUIDE):
    run('tools/check_guide.py', GUIDE)
    run('build/08/index_card.py', GUIDE, 'index.html')
rep.insert(1, 'status: ' + status)
open('build/out/08-report.txt', 'w', encoding='utf-8').write('\n'.join(rep) + '\n')
print('\n'.join(rep))

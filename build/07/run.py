#!/usr/bin/env python3
"""No. 07 pipeline (.github/workflows/guide-07.yml runs it on pushes to build/07/).
Builds build/out/07-candidate.html, balances quizzes, lints, and only a clean candidate
replaces guides/07-design.html, then syncs the library card and runs qa.py.
Report: build/out/07-report.txt."""
import datetime, os, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
os.makedirs('build/out', exist_ok=True)
rep = ['build %s UTC' % datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M')]


def run(*cmd):
    r = subprocess.run([sys.executable] + list(cmd), capture_output=True, text=True)
    rep.append('$ %s (exit %d)\n%s%s' % (' '.join(cmd), r.returncode, r.stdout[-6000:], r.stderr[-4000:]))
    return r.returncode


status = 'no build.py yet'
GUIDE, CAND = 'guides/07-design.html', 'build/out/07-candidate.html'
if os.path.exists('build/07/build.py'):
    if os.path.exists(CAND):
        os.remove(CAND)
    if run('build/07/build.py', CAND) == 0 and os.path.exists(CAND):
        run('tools/quiz_audit.py', '--fix', CAND)
        if run('tools/check_guide.py', CAND) == 0:
            shutil.copyfile(CAND, GUIDE)
            status = 'candidate passed lint and replaced the guide'
            run('build/07/index_card.py', GUIDE, 'index.html')
            run('build/07/qa.py')
        else:
            status = 'candidate FAILED lint, guide unchanged'
    else:
        status = 'build FAILED, guide unchanged'
    if os.path.exists(CAND):
        os.remove(CAND)
rep.insert(1, 'status: ' + status)
open('build/out/07-report.txt', 'w', encoding='utf-8').write('\n'.join(rep) + '\n')
print('\n'.join(rep))

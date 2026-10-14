#!/usr/bin/env python3
"""Guide build pipeline. GitHub Actions runs this on every push to build/
(.github/workflows/guide-build.yml), so an AI can update a big guide by pushing
small source files instead of the whole HTML.

1. If build/06/build.py exists, it writes build/out/06-candidate.html.
2. The candidate is linted with tools/check_guide.py. Only a clean candidate
   replaces guides/06-read-the-room.html, so a bad build never ships.
3. A compact skeleton of the live guide goes to build/out/06-skeleton.txt and a
   report to build/out/06-report.txt, so the next session can plan without
   reading 800 KB of HTML.
"""
import datetime, os, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
os.makedirs('build/out', exist_ok=True)
GUIDE = 'guides/06-read-the-room.html'
CAND = 'build/out/06-candidate.html'
rep = ['build %s UTC' % datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M')]


def run(*cmd):
    r = subprocess.run([sys.executable] + list(cmd), capture_output=True, text=True)
    rep.append('$ %s (exit %d)\n%s%s' % (' '.join(cmd), r.returncode, r.stdout, r.stderr))
    return r.returncode


status = 'no part build found, guide unchanged'
if os.path.exists('build/06/build.py'):
    if os.path.exists(CAND):
        os.remove(CAND)
    if run('build/06/build.py', GUIDE, CAND) == 0 and os.path.exists(CAND):
        if run('tools/check_guide.py', CAND) == 0:
            shutil.copyfile(CAND, GUIDE)
            status = 'candidate passed lint and replaced the guide'
        else:
            status = 'candidate FAILED lint, guide unchanged'
    else:
        status = 'part build FAILED, guide unchanged'
    if os.path.exists(CAND):
        os.remove(CAND)
run('tools/check_guide.py', GUIDE)
run('build/skeleton.py', GUIDE, 'build/out/06-skeleton.txt')
if os.path.exists('build/probe.py'):
    run('build/probe.py', GUIDE, 'build/out/06-probe.txt')
rep.insert(1, 'status: ' + status)
open('build/out/06-report.txt', 'w', encoding='utf-8').write('\n'.join(rep) + '\n')
open('build/out/LAST_BUILD.txt', 'w', encoding='utf-8').write(rep[0] + ' | ' + status + '\n')
print('\n'.join(rep))

#!/usr/bin/env python3
"""Headless check of the built No. 03 guide (network blocked). Writes build/out/03-qa.txt."""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
out = []
try:
    from playwright.sync_api import sync_playwright
except Exception as e:
    out.append('qa skipped: playwright not available (%s)' % e)
else:
    path = 'file://' + os.path.join(ROOT, 'guides', '03-cons-and-cults.html')
    with sync_playwright() as p:
        b = p.chromium.launch()
        for w, h, name in ((1280, 900, 'desktop'), (390, 844, 'mobile')):
            pg = b.new_page(viewport={'width': w, 'height': h})
            errs = []
            pg.on('pageerror', lambda e: errs.append('pageerror: %s' % e))
            pg.on('console', lambda m: errs.append('console %s: %s' % (m.type, m.text)) if m.type == 'error' else None)
            pg.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') else r.abort())
            pg.goto(path)
            pg.wait_for_timeout(1500)
            info = pg.evaluate('''() => {
              const q = s => document.querySelectorAll(s).length;
              const checks = [...document.querySelectorAll('.check')];
              return {stops: q('button.done'), checks: checks.length,
                      rendered: checks.filter(c => c.querySelector('button,input,label')).length,
                      thumbs: q('.thumbs .thumb'), search: !!document.getElementById('nk-find'),
                      bar: !!document.getElementById('mtrx-bar'), title: document.title,
                      overflowX: document.documentElement.scrollWidth > window.innerWidth + 2};
            }''')
            out.append('%s: %s' % (name, info))
            try:
                pg.click('button.done[data-mod="1.1"]', timeout=3000)
                pg.wait_for_timeout(300)
                keys = pg.evaluate('() => Object.keys(localStorage).map(k => k + "=" + (localStorage.getItem(k) || "").slice(0, 80))')
                out.append('%s after marking 1.1 done, localStorage: %s' % (name, keys))
            except Exception as e:
                out.append('%s: could not click done 1.1 (%s)' % (name, str(e)[:160]))
            try:
                first = pg.query_selector('.check button, .check label, .check input')
                if first:
                    first.click()
                    pg.wait_for_timeout(200)
                    out.append('%s: clicked a quiz option, check html: %s' % (name, pg.evaluate("() => (document.querySelector('.check') || {}).innerHTML.slice(0, 300)")))
            except Exception as e:
                out.append('%s: quiz click failed (%s)' % (name, str(e)[:160]))
            out.append('%s errors: %s' % (name, errs[:12] or 'none'))
            pg.close()
        b.close()
open(os.path.join(ROOT, 'build', 'out', '03-qa.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('\n'.join(out))

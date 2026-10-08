/* Browser integration checks against the real library and all four guide pages.
   CI installs the pinned motion packages; CDN requests are served from those packages. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const { chromium } = require('playwright');
const root = process.cwd();
const output = path.join(root, 'motion-screenshots');
fs.mkdirSync(output, { recursive: true });
const gsapDir = path.dirname(require.resolve('gsap'));
const lenisDir = path.dirname(require.resolve('lenis'));
const libraries = {
  'gsap.min.js': path.join(gsapDir, 'gsap.min.js'),
  'ScrollTrigger.min.js': path.join(gsapDir, 'ScrollTrigger.min.js'),
  'lenis.min.js': path.join(lenisDir, 'lenis.min.js')
};
const server = http.createServer((req, res) => {
  const pathname = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
  const file = path.resolve(root, '.' + (pathname === '/' ? '/index.html' : pathname));
  if (!file.startsWith(root + path.sep) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) {
    res.writeHead(404); res.end('Not found'); return;
  }
  res.setHeader('Content-Type', file.endsWith('.js') ? 'text/javascript' : file.endsWith('.html') ? 'text/html' : 'application/octet-stream');
  res.end(fs.readFileSync(file));
});
async function run() {
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const base = 'http://127.0.0.1:' + server.address().port;
  const browser = await chromium.launch({ headless: true });
  const errors = [];
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  async function route(ctx, block) {
    await ctx.route('**/*', async route => {
      const url = new URL(route.request().url());
      if (url.origin === base) return route.continue();
      if (url.hostname === 'cdn.jsdelivr.net') {
        if (block) return route.abort();
        const filename = url.pathname.split('/').pop();
        assert.ok(libraries[filename], 'Unexpected motion dependency: ' + filename);
        return route.fulfill({ path: libraries[filename], contentType: 'text/javascript' });
      }
      if (url.hostname === 'raw.githubusercontent.com') {
        return route.fulfill({ body: '{"done":{}}', contentType: 'application/json' });
      }
      return route.fulfill({ body: '', contentType: url.pathname.endsWith('.js') ? 'text/javascript' : 'text/css' });
    });
  }
  await route(context, false);
  const page = await context.newPage();
  page.on('pageerror', error => errors.push(error.message));
  const mode = value => page.waitForFunction(expected => document.documentElement.dataset.mtrxMotion === expected, value);
  try {
    await page.goto(base + '/index.html');
    await mode('smooth');
    assert.equal(await page.locator('#grid .card').count(), 6);
    await page.mouse.move(500, 400);
    await page.mouse.wheel(0, 600);
    await page.waitForTimeout(1100);
    assert.ok(await page.evaluate(() => scrollY) > 300, 'Wheel smoothing must advance the page');
    await page.locator('.card[data-n="01"]').click();
    assert.match(await page.locator('#det h2').innerText(), /tech wild/i);
    await page.screenshot({ path: path.join(output, 'library-desktop.png') });
    await page.evaluate(() => window.dispatchEvent(new CustomEvent('mtrx:synced')));
    await page.waitForTimeout(250);
    assert.equal(await page.locator('#grid .card').count(), 6);
    await page.emulateMedia({ reducedMotion: 'reduce' });
    await mode('native');
    assert.equal(await page.locator('#mtrx-motion-css').count(), 0);
    await page.emulateMedia({ reducedMotion: 'no-preference' });
    await mode('smooth');

    const guides = ['00-learning-os.html', '01-tech-wild.html', '02-mind.html', '05-long-game.html'];
    for (const filename of guides) {
      await page.goto(base + '/guides/' + filename);
      await mode('smooth');
      assert.equal(await page.locator('#mtrx-motion-script').count(), 1);
      await page.keyboard.press('r');
      await mode('native');
      assert.equal(await page.locator('#mtrx-motion-css').count(), 0);
      await page.keyboard.press('Escape');
      await mode('smooth');
      await page.locator('button.done[data-mod]').first().click();
      const code = await page.evaluate(() => window.MTRX_PROGRESS_CODE());
      assert.ok(code.startsWith('p' + filename.slice(0, 2) + '_'), 'Progress code must remain valid');
      await page.locator('#mtrx-send').click();
      assert.equal(await page.locator('#mtrx-transfer').evaluate(el => el.open), true);
      await page.locator('#mtrx-transfer .mt-close').click();
      assert.equal(await page.locator('#mtrx-transfer').evaluate(el => el.open), false);
      await page.evaluate(() => scrollTo({ top: 0, behavior: 'instant' }));
      await page.waitForTimeout(100);
      if (filename === '05-long-game.html') {
        await page.locator('a[href="#m0-1"]').first().click();
        await page.waitForFunction(() => location.hash === '#m0-1');
        assert.ok(Math.abs(await page.locator('#m0-1').evaluate(el => el.getBoundingClientRect().top)) < 100);
        await page.screenshot({ path: path.join(output, 'guide-desktop.png') });
      }
      console.log('PASS', filename, 'smooth scroll, Read mode, progress and dialog');
    }
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(base + '/index.html');
    await mode('smooth');
    assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), 'No mobile horizontal overflow');
    await page.screenshot({ path: path.join(output, 'library-mobile.png') });
    await page.goto(base + '/guides/05-long-game.html');
    await mode('smooth');
    await page.screenshot({ path: path.join(output, 'guide-mobile.png') });
    assert.deepEqual(errors, [], 'No uncaught browser exceptions');

    const fallback = await browser.newContext();
    await route(fallback, true);
    const blocked = await fallback.newPage();
    await blocked.goto(base + '/index.html');
    await blocked.waitForFunction(() => document.documentElement.dataset.mtrxMotion === 'native');
    assert.equal(await blocked.locator('#grid .card').count(), 6);
    assert.equal(await blocked.locator('#mtrx-motion-css').count(), 0);
    await fallback.close();

    const reduced = await browser.newContext({ reducedMotion: 'reduce' });
    await route(reduced, false);
    const quiet = await reduced.newPage();
    let requests = 0;
    quiet.on('request', req => { if (req.url().includes('cdn.jsdelivr.net')) requests++; });
    await quiet.goto(base + '/guides/00-learning-os.html');
    await quiet.waitForFunction(() => document.documentElement.dataset.mtrxMotion === 'native');
    assert.equal(requests, 0, 'Reduced motion must not download animation packages');
    await reduced.close();
    console.log('PASS homepage, dynamic cards, anchors, mobile, reduced motion and CDN fallback');
  } finally {
    await browser.close();
    await new Promise(resolve => server.close(resolve));
  }
}
run().catch(error => { console.error(error); server.close(); process.exitCode = 1; });

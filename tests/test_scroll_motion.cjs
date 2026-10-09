/* Run from the repository root: node tests/test_scroll_motion.cjs
   Requires Playwright + Chromium. Native scroll only; no Lenis package needed.
   Exercises the actual homepage and all four guides, not the design fixture. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const { chromium } = require('playwright');
const root = process.cwd();
const server = http.createServer((req,res)=>{
  const pathname = decodeURIComponent(new URL(req.url,'http://localhost').pathname);
  const file = path.resolve(root,'.'+(pathname==='/'?'/index.html':pathname));
  if(!file.startsWith(root+path.sep)||!fs.existsSync(file)||fs.statSync(file).isDirectory()){
    res.writeHead(404);res.end();return;
  }
  res.setHeader('Content-Type',file.endsWith('.js')?'text/javascript':file.endsWith('.html')?'text/html':'application/octet-stream');
  res.end(fs.readFileSync(file));
});
async function run(){
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const base='http://127.0.0.1:'+server.address().port;
  const browser=await chromium.launch({headless:true});
  const errors=[], motionRequests=[];
  async function context(options={}){
    const ctx=await browser.newContext({viewport:{width:1280,height:900},...options});
    await ctx.route('**/*',async route=>{
      const url=new URL(route.request().url());
      if(url.origin===base)return route.continue();
      if(/lenis|gsap|scrolltrigger/i.test(url.href))motionRequests.push(url.href);
      if(url.hostname==='raw.githubusercontent.com')return route.fulfill({body:'{"done":{}}',contentType:'application/json'});
      return route.fulfill({body:'',contentType:url.pathname.endsWith('.js')?'text/javascript':'text/css'});
    });
    ctx.on('page',page=>page.on('pageerror',e=>errors.push(e.message)));
    return ctx;
  }
  async function native(page){
    await page.waitForFunction(()=>window.MTRX_SCROLL?.native===true);
    assert.equal(await page.evaluate(()=>document.documentElement.dataset.mtrxMotion),'native');
    assert.equal(await page.evaluate(()=>getComputedStyle(document.documentElement).scrollBehavior),'auto');
    assert.equal(await page.evaluate(()=>typeof window.Lenis),'undefined');
    assert.equal(await page.locator('#mtrx-motion-css').count(),0);
  }
  async function tools(page){
    await page.locator('#mtrx-reader-toggle').click();
    assert.equal(await page.locator('#mtrx-reader-panel').evaluate(e=>e.open),true);
  }
  async function palette(page,id){
    if(await page.locator('#mtrx-reader-toggle').count())await tools(page);
    await page.locator('#mtrx-theme-toggle').click();
    await page.locator('input[name="mtrx-palette"][value="'+id+'"]').check();
    await page.locator('#mtrx-themes .mtp-close').click();
  }
  try{
    const ctx=await context(),page=await ctx.newPage();
    await page.goto(base+'/index.html');await native(page);
    assert.equal(await page.locator('#grid .card').count(),6);
    assert.equal(await page.locator('#mtrx-reader-toggle').count(),0,'Homepage keeps its theme button');
    for(const [id,colors] of [
      ['330',['#c1c494','#bce4e5','#97acc8','#099197']],
      ['331',['#c53c69','#1e0e3f','#9a72aa','#4f4086']]
    ]){
      await palette(page,id);
      assert.deepEqual(await page.evaluate(id=>window.MTRX_PALETTES.colors(id),id),colors);
      await page.reload();await native(page);
      assert.equal(await page.evaluate(()=>window.MTRX_PALETTES.get()),id);
    }
    await palette(page,'original');
    const guides=['00-learning-os.html','01-tech-wild.html','02-mind.html','05-long-game.html'];
    for(const file of guides){
      await page.goto(base+'/guides/'+file);await native(page);
      await page.locator('#mtrx-reader-toggle').waitFor();
      assert.equal(await page.locator('#mtrx-bar').isVisible(),false);
      assert.equal(await page.locator('.nk-dock').isVisible(),false);
      await page.mouse.move(640,450);await page.mouse.wheel(0,700);
      await page.waitForFunction(()=>scrollY>300);
      await tools(page);
      assert.equal(await page.locator('#mtrx-reader-panel .nk-dock').isVisible(),true);
      await page.keyboard.press('Escape');
      assert.equal(await page.evaluate(()=>document.activeElement.id),'mtrx-reader-toggle');
      await page.locator('button.done[data-mod]').first().click();
      const before=await page.evaluate(()=>window.MTRX_PROGRESS_CODE());
      assert.ok(before.startsWith('p'+file.slice(0,2)+'_'));
      await tools(page);await page.locator('#mtrx-send').click();
      assert.equal(await page.locator('#mtrx-reader-panel').evaluate(e=>e.open),false);
      assert.equal(await page.locator('#mtrx-transfer').evaluate(e=>e.open),true);
      await page.locator('#mtrx-transfer .mt-close').click();
      await palette(page,'330');await palette(page,'331');
      assert.equal(await page.evaluate(()=>window.MTRX_PROGRESS_CODE()),before);
      await tools(page);await page.locator('#mtrx-read').click();
      assert.equal(await page.locator('#mtrx-reader-toggle').isVisible(),false);
      await page.keyboard.press('Escape');
      await page.locator('#mtrx-reader-toggle').waitFor();
      await page.evaluate(()=>window.MTRX_SCROLL.scrollTo(0));
      assert.equal(await page.evaluate(()=>scrollY),0);
      await palette(page,'original');
      console.log('PASS',file,'native scroll, consolidated controls, themes, progress, Read mode');
    }
    for(const width of [390,320]){
      await page.setViewportSize({width,height:700});
      await tools(page);
      const box=await page.locator('#mtrx-reader-panel').boundingBox();
      assert.ok(box.x>=0 && box.x+box.width<=width && box.y+box.height<=700);
      const heights=await page.locator('#mtrx-reader-panel button,#mtrx-reader-panel a').evaluateAll(es=>es.map(e=>e.getBoundingClientRect().height));
      assert.ok(heights.every(h=>h>=44),'Every reader control has a 44px target');
      await page.locator('#mtrx-theme-toggle').click();
      assert.equal(await page.locator('input[name="mtrx-palette"]').count(),5);
      await page.locator('input[value="331"]').check();
      await page.locator('.mtp-close').click();
      assert.equal(await page.evaluate(()=>document.activeElement.id),'mtrx-reader-toggle');
    }
    for(const options of [{isMobile:true,hasTouch:true,viewport:{width:390,height:844}},{reducedMotion:'reduce'}]){
      const special=await context(options),p=await special.newPage();
      await p.goto(base+'/guides/01-tech-wild.html');await native(p);
      await p.locator('#mtrx-reader-toggle').waitFor();
      await special.close();
    }
    assert.deepEqual(motionRequests,[],'No smooth-scroll dependency may be requested');
    assert.deepEqual(errors,[],'No uncaught browser exceptions');
    console.log('PASS native wheel/touch, five palettes, responsive reader menu and existing study controls');
  } finally {
    await browser.close();
    await new Promise(resolve=>server.close(resolve));
  }
}
run().catch(error=>{console.error(error);server.close();process.exitCode=1;});

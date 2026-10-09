/* Run with: node --test tests/test_themes.cjs
   Storage/token regression tests; browser layout checks are a separate manual step. */
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const source = fs.readFileSync(path.join(__dirname, '../assets/mtrx-themes.js'), 'utf8');

function environment(saved = {}, blocked = false) {
  const storage = new Map(Object.entries(saved)), attrs = {}, styles = [], listeners = {}, events = [];
  const root = {
    setAttribute(k,v){attrs[k]=v;},
    removeAttribute(k){delete attrs[k];}
  };
  const document = {
    documentElement:root, readyState:'loading',
    createElement(tag){return {tag,id:'',textContent:''};},
    head:{appendChild(el){styles.push(el);}},
    addEventListener(){}
  };
  const window = {addEventListener(k,fn){listeners[k]=fn;},dispatchEvent(e){events.push(e);}};
  const ctx={window,document,CustomEvent:function(type,init){this.type=type;this.detail=init.detail;},
    localStorage:{
      getItem(k){if(blocked)throw Error('unavailable');return storage.get(k)||null;},
      setItem(k,v){if(blocked)throw Error('unavailable');storage.set(k,v);}
    }};
  vm.runInNewContext(source,ctx);
  return {api:window.MTRX_PALETTES,attrs,styles,storage,listeners,events,ctx};
}
test('first visit leaves all original tokens untouched',()=>{
  const e=environment();
  assert.equal(e.api.get(),'original');
  assert.equal(e.attrs['data-mtrx-palette'],undefined);
  assert.equal(e.storage.size,0);
});
test('exact source swatches are preserved separately',()=>{
  const e=environment();
  assert.deepEqual(Array.from(e.api.colors('276')),['#f37f94','#fdd4bd','#afd472','#111314']);
  assert.deepEqual(Array.from(e.api.colors('320')),['#f58e84','#f5ecc2','#819238','#a5c8d1']);
});
test('selection persists only in its own key and Original resets the override',()=>{
  const e=environment({'mtrx-theme':'dark','mtrx-fieldguide-v1':'{"done":{"1.1":true}}','notes':'keep'});
  e.api.set('276');
  assert.equal(e.attrs['data-mtrx-palette'],'276');
  assert.equal(e.storage.get('mtrx-palette-v1'),'276');
  assert.equal(e.storage.get('mtrx-theme'),'dark');
  assert.equal(e.storage.get('mtrx-fieldguide-v1'),'{"done":{"1.1":true}}');
  assert.equal(e.storage.get('notes'),'keep');
  e.api.set('original');
  assert.equal(e.attrs['data-mtrx-palette'],undefined);
});
test('saved choices restore and unknown values safely fall back',()=>{
  assert.equal(environment({'mtrx-palette-v1':'320'}).attrs['data-mtrx-palette'],'320');
  assert.equal(environment({'mtrx-palette-v1':'<script>'}).api.get(),'original');
  const e=environment();e.api.set('__proto__');assert.equal(e.api.get(),'original');
});
test('blocked browser storage is nonfatal',()=>{
  const e=environment({},true);e.api.set('320');assert.equal(e.api.get(),'320');
});
test('duplicate loading does not install another style or reset selection',()=>{
  const e=environment();e.api.set('276');vm.runInNewContext(source,e.ctx);
  assert.equal(e.styles.length,1);assert.equal(e.api.get(),'276');
});
test('storage events sync only palette preferences',()=>{
  const e=environment();e.storage.set('mtrx-palette-v1','320');
  e.listeners.storage({key:'other'});assert.equal(e.api.get(),'original');
  e.listeners.storage({key:'mtrx-palette-v1'});assert.equal(e.api.get(),'320');
  e.storage.delete('mtrx-palette-v1');e.listeners.storage({key:null});assert.equal(e.api.get(),'original');
});
test('styles cover light/dark, read mode, reduced motion and semantic feedback',()=>{
  const css=environment().styles[0].textContent;
  for(const marker of ['[data-mtrx-palette="276"]','[data-mtrx-palette="320"]','[data-theme="dark"]','prefers-reduced-motion:reduce','html.mtrx-read','.opt.is-right','.opt.is-wrong']) assert.ok(css.includes(marker),marker);
});

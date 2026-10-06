/* MTRX Field Library: shared add-on loaded by every guide and by the library home (see AGENTS.md, rule 6).
   1. Top bar: "Library" link, "Send progress" and "Read mode".
   2. Send progress: packs the stops marked done into a short code and opens the Telegram review
      bot with it (t.me/<bot>?start=pNN_<base64url bitmask>). Bit i = the i-th
      <button class="done" data-mod> in document order, the same order tools/build_questions.py
      writes into bot/questions/NN.json "stops".
   3. Read mode: hides every floating control (week tabs, reader kit dock, top bar, progress line)
      and widens the page. Toggle with the button, the R key, or Esc to leave. Remembered per browser.
   4. Device sync: reads the bot's public bot/state.json and marks done any stop the bot already
      knows about (sent from another device). It only ever adds, and each stop is applied once,
      so a stop you untick by hand stays unticked. The library home calls the same sync.
   Change shared behaviour here, never inside the guides. */
(function () {
  var BOT = 'makingmesmart_bot';
  var STATE_URL = 'https://raw.githubusercontent.com/Kevincecil11/mtrx-field-library/main/bot/state.json';
  var SYNC_KEY = 'mtrx-sync-v1', READ_KEY = 'mtrx-read-v1';
  if (document.getElementById('mtrx-bar')) return;
  var m = location.pathname.match(/\/(\d\d)-[^\/]*\.html$/);
  var guide = m && m[1];
  var home = !guide && window.MTRX_GUIDES;

  function getJ(k) { try { return JSON.parse(localStorage.getItem(k)) || {}; } catch (e) { return {}; } }
  function setJ(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  function botDone(cb) {
    if (!window.fetch) return;
    fetch(STATE_URL + '?t=' + Date.now(), { cache: 'no-store' })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (st) { if (st && st.done) cb(st.done); })
      .catch(function () {});
  }

  /* Library home: merge the bot's stops straight into each guide's saved progress, then redraw. */
  if (home) {
    botDone(function (done) {
      var seen = getJ(SYNC_KEY), n = 0;
      home.forEach(function (g) {
        if (!g.key || !done[g.n]) return;
        var store = getJ(g.key), s = seen[g.n] || (seen[g.n] = {});
        store.done = store.done || {};
        Object.keys(done[g.n]).forEach(function (k) {
          if (s[k]) return;
          s[k] = done[g.n][k];
          if (!store.done[k]) { store.done[k] = true; n++; }
        });
        setJ(g.key, store);
      });
      setJ(SYNC_KEY, seen);
      if (n) window.dispatchEvent(new CustomEvent('mtrx:synced', { detail: { added: n } }));
    });
    return;
  }

  var css = document.createElement('style');
  css.textContent =
    '#mtrx-bar{position:fixed;top:12px;left:14px;z-index:95;display:flex;gap:8px;align-items:center}' +
    '.mtrx-fab{display:inline-flex;align-items:center;gap:6px;border:0;cursor:pointer;white-space:nowrap;' +
    'font:700 13px/1 "JetBrains Mono",ui-monospace,monospace;letter-spacing:.08em;text-transform:uppercase;' +
    'padding:9px 13px;border-radius:999px;text-decoration:none;box-shadow:0 6px 14px -8px rgba(0,0,0,.5)}' +
    '#mtrx-lib{background:#151515;color:#F6F4EF}' +
    '#mtrx-send{background:#ED691D;color:#151515}' +
    '#mtrx-read{background:#F6F4EF;color:#151515;box-shadow:inset 0 0 0 1.5px #151515,0 6px 14px -8px rgba(0,0,0,.5)}' +
    '#mtrx-toast{position:fixed;left:14px;top:56px;z-index:96;max-width:320px;background:#151515;color:#F6F4EF;' +
    'font:600 14px/1.45 "Nunito Sans",system-ui,sans-serif;padding:12px 14px;border-radius:14px;display:none}' +
    '#mtrx-exit{position:fixed;top:12px;right:14px;z-index:97;display:none;opacity:.6;transition:opacity .2s,transform .25s;' +
    'background:#151515;color:#F6F4EF}' +
    '#mtrx-exit:hover,#mtrx-exit:focus-visible{opacity:1}' +
    'html.mtrx-read #mtrx-exit{display:inline-flex}' +
    'html.mtrx-read #mtrx-exit.away{transform:translateY(-72px)}' +
    'html.mtrx-read .thumbs,html.mtrx-read .scrollbar,html.mtrx-read .nk-dock,html.mtrx-read .nk-panel,' +
    'html.mtrx-read .nk-find,html.mtrx-read .fp-side,html.mtrx-read #mtrx-bar,html.mtrx-read #mtrx-toast{display:none!important}' +
    'html.mtrx-read .site{padding-right:0!important;padding-bottom:0!important}' +
    'html.mtrx-read body{padding-bottom:0!important}' +
    '@media (max-width:760px){.mtrx-fab{font-size:11px;padding:8px 10px;letter-spacing:.05em}#mtrx-bar{gap:6px;left:10px}' +
    '.mtrx-fab .lg{display:none}}';
  document.head.appendChild(css);

  var bar = document.createElement('div'); bar.id = 'mtrx-bar';
  var lib = document.createElement('a');
  lib.id = 'mtrx-lib'; lib.className = 'mtrx-fab'; lib.href = '../index.html';
  lib.textContent = '\u2190 Library'; lib.setAttribute('aria-label', 'Back to the MTRX Field Library');
  bar.appendChild(lib);
  document.body.appendChild(bar);

  /* Read mode */
  var root = document.documentElement;
  var exit = document.createElement('button');
  exit.id = 'mtrx-exit'; exit.type = 'button'; exit.className = 'mtrx-fab';
  exit.textContent = '\u2715 Exit read mode'; exit.setAttribute('aria-label', 'Exit read mode and bring the buttons back');
  document.body.appendChild(exit);
  function setRead(on) {
    root.classList.toggle('mtrx-read', on);
    exit.classList.remove('away');
    try { on ? localStorage.setItem(READ_KEY, '1') : localStorage.removeItem(READ_KEY); } catch (e) {}
  }
  window.MTRX_READ = setRead;
  exit.addEventListener('click', function () { setRead(false); });
  var lastY = window.scrollY;
  window.addEventListener('scroll', function () {
    if (!root.classList.contains('mtrx-read')) return;
    var y = window.scrollY;
    if (y > lastY + 4 && y > 200) exit.classList.add('away');
    else if (y < lastY - 4 || y < 200) exit.classList.remove('away');
    lastY = y;
  }, { passive: true });
  document.addEventListener('keydown', function (e) {
    var t = e.target, typing = t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.tagName === 'SELECT' || t.isContentEditable);
    if (typing || e.ctrlKey || e.metaKey || e.altKey) return;
    if ((e.key === 'r' || e.key === 'R')) { e.preventDefault(); setRead(!root.classList.contains('mtrx-read')); }
    else if (e.key === 'Escape' && root.classList.contains('mtrx-read')) setRead(false);
  });
  try { if (localStorage.getItem(READ_KEY) === '1') setRead(true); } catch (e) {}

  var toast = document.createElement('div'); toast.id = 'mtrx-toast'; toast.setAttribute('role', 'status');
  document.body.appendChild(toast);
  function say(t) { toast.textContent = t; toast.style.display = 'block'; clearTimeout(say.t); say.t = setTimeout(function () { toast.style.display = 'none'; }, 6000); }

  if (guide) {
    var send = document.createElement('button');
    send.id = 'mtrx-send'; send.type = 'button'; send.className = 'mtrx-fab';
    send.innerHTML = 'Send<span class="lg"> progress</span> \u2708'; send.setAttribute('aria-label', 'Send my finished stops to the Telegram review bot');
    bar.appendChild(send);
  }
  var read = document.createElement('button');
  read.id = 'mtrx-read'; read.type = 'button'; read.className = 'mtrx-fab';
  read.innerHTML = '\u00b6<span class="lg"> Read mode</span>';
  read.title = 'Read mode (R)'; read.setAttribute('aria-label', 'Read mode: hide every button and just read (shortcut R)');
  read.addEventListener('click', function () { setRead(true); });
  bar.appendChild(read);
  if (!guide) return;

  function stops() {
    var seen = {}, out = [];
    [].forEach.call(document.querySelectorAll('button.done[data-mod]'), function (b) {
      var k = b.getAttribute('data-mod');
      if (seen[k]) { if (b.classList.contains('is-done')) seen[k].d = true; return; }
      seen[k] = { k: k, d: b.classList.contains('is-done') };
      out.push(seen[k]);
    });
    return out;
  }
  function code(list) {
    var bytes = new Uint8Array(Math.ceil(list.length / 8)), bin = '';
    list.forEach(function (x, i) { if (x.d) bytes[i >> 3] |= 1 << (i & 7); });
    for (var i = 0; i < bytes.length; i++) bin += String.fromCharCode(bytes[i]);
    return 'p' + guide + '_' + btoa(bin).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
  }
  send.addEventListener('click', function () {
    var list = stops(), n = list.filter(function (x) { return x.d; }).length;
    if (!n) { say('Mark a stop done first (the button at the end of each stop), then send.'); return; }
    window.MTRX_LAST_CODE = code(list);
    window.open('https://t.me/' + BOT + '?start=' + window.MTRX_LAST_CODE, '_blank', 'noopener');
    say('Opening Telegram with ' + n + ' finished ' + (n === 1 ? 'stop' : 'stops') + '. Tap Start there. Reviews begin tomorrow.');
  });
  window.MTRX_PROGRESS_CODE = function () { return code(stops()); };

  /* Device sync: tick stops the bot already has (sent from your other device). */
  function applySync(done) {
    var mine = done[guide] || {}, seen = getJ(SYNC_KEY), s = seen[guide] || (seen[guide] = {}), n = 0;
    Object.keys(mine).forEach(function (k) {
      if (s[k]) return;
      s[k] = mine[k];
      var b = null;
      [].some.call(document.querySelectorAll('button.done[data-mod]'), function (x) { if (x.getAttribute('data-mod') === k) { b = x; return true; } });
      if (b && !b.classList.contains('is-done')) { b.click(); n++; }
    });
    setJ(SYNC_KEY, seen);
    if (n) say('Synced ' + n + (n === 1 ? ' stop' : ' stops') + ' you finished on another device.');
    return n;
  }
  window.MTRX_APPLY_SYNC = applySync;
  botDone(applySync);
})();

/* MTRX Field Library: shared add-on loaded by every guide (see AGENTS.md, rule 6).
   1. "Library" link back to the home page.
   2. "Send progress" button: packs the stops marked done into a short code and opens
      the Telegram review bot with it (t.me/<bot>?start=pNN_<base64url bitmask>).
      Bit i = the i-th <button class="done" data-mod> in document order, the same order
      tools/build_questions.py writes into bot/questions/NN.json "stops".
   Change shared behaviour here, never inside the guides. */
(function () {
  var BOT = 'makingmesmart_bot';
  if (document.getElementById('mtrx-lib')) return;
  var m = location.pathname.match(/\/(\d\d)-[^\/]*\.html$/);
  var guide = m && m[1];

  var css = document.createElement('style');
  css.textContent =
    '.mtrx-fab{position:fixed;left:14px;z-index:95;display:inline-flex;align-items:center;gap:6px;border:0;cursor:pointer;' +
    'font:700 13px/1 "JetBrains Mono",ui-monospace,monospace;letter-spacing:.08em;text-transform:uppercase;' +
    'padding:9px 13px;border-radius:999px;text-decoration:none;box-shadow:0 6px 14px -8px rgba(0,0,0,.5)}' +
    '#mtrx-lib{top:12px;background:#151515;color:#F6F4EF}' +
    '#mtrx-send{top:12px;left:128px;background:#ED691D;color:#151515}' +
    '#mtrx-toast{position:fixed;left:14px;top:56px;z-index:96;max-width:320px;background:#151515;color:#F6F4EF;' +
    'font:600 14px/1.45 "Nunito Sans",system-ui,sans-serif;padding:12px 14px;border-radius:14px;display:none}' +
    '@media (max-width:760px){.mtrx-fab{font-size:11px;padding:8px 10px}#mtrx-send{left:112px}}';
  document.head.appendChild(css);

  var lib = document.createElement('a');
  lib.id = 'mtrx-lib'; lib.className = 'mtrx-fab'; lib.href = '../index.html';
  lib.textContent = '\u2190 Library'; lib.setAttribute('aria-label', 'Back to the MTRX Field Library');
  document.body.appendChild(lib);
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
  var toast = document.createElement('div'); toast.id = 'mtrx-toast'; toast.setAttribute('role', 'status');
  document.body.appendChild(toast);
  function say(t) { toast.textContent = t; toast.style.display = 'block'; clearTimeout(say.t); say.t = setTimeout(function () { toast.style.display = 'none'; }, 6000); }

  var send = document.createElement('button');
  send.id = 'mtrx-send'; send.type = 'button'; send.className = 'mtrx-fab';
  send.textContent = 'Send progress \u2708'; send.setAttribute('aria-label', 'Send my finished stops to the Telegram review bot');
  send.addEventListener('click', function () {
    var list = stops(), n = list.filter(function (x) { return x.d; }).length;
    if (!n) { say('Mark a stop done first (the button at the end of each stop), then send.'); return; }
    window.MTRX_LAST_CODE = code(list);
    window.open('https://t.me/' + BOT + '?start=' + window.MTRX_LAST_CODE, '_blank', 'noopener');
    say('Opening Telegram with ' + n + ' finished ' + (n === 1 ? 'stop' : 'stops') + '. Tap Start there. Reviews begin tomorrow.');
  });
  document.body.appendChild(send);
  window.MTRX_PROGRESS_CODE = function () { return code(stops()); };
})();

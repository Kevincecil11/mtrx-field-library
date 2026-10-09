/* MTRX palette layer. Original is a no-op; learning data and illustrations are never changed.
   Source: colors.elwyn.co, Sanzo Wada combinations 276 and 320.
   Palette persistence is independent of the existing mtrx-theme dark-mode preference.
   No dependencies, document-wide observers, scroll listeners or continuous animation. */
(function () {
  'use strict';
  if (window.MTRX_PALETTES) return;
  var KEY = 'mtrx-palette-v1', root = document.documentElement;
  var palettes = {
    original: { name: 'Original', sub: 'The MTRX field notebook', colors: ['#ED691D', '#ECEAE4', '#697132', '#151515'] },
    '276': { name: 'Wada 276', sub: 'Eosine pink, seashell, yellow-green, black', colors: ['#f37f94', '#fdd4bd', '#afd472', '#111314'] },
    '320': { name: 'Wada 320', sub: 'Coral, sulphur yellow, oil green, glaucous blue', colors: ['#f58e84', '#f5ecc2', '#819238', '#a5c8d1'] }
  };
  var current = 'original', dialog, trigger, status;
  function valid(id) { return Object.prototype.hasOwnProperty.call(palettes, id); }
  function read() { try { var id = localStorage.getItem(KEY); return valid(id) ? id : 'original'; } catch (_) { return 'original'; } }
  function rgb(hex) { return hex.slice(1).match(/../g).map(function (v) { return parseInt(v, 16); }); }
  function mix(a, b, ratio) {
    var x = rgb(a), y = rgb(b);
    return '#' + x.map(function (v, i) { return Math.round(v + (y[i] - v) * ratio).toString(16).padStart(2, '0'); }).join('');
  }
  function luminance(hex) {
    var v = rgb(hex).map(function (c) { c /= 255; return c <= .04045 ? c / 12.92 : Math.pow((c + .055) / 1.055, 2.4); });
    return v[0] * .2126 + v[1] * .7152 + v[2] * .0722;
  }
  function contrast(a, b) { var x = luminance(a), y = luminance(b); return (Math.max(x, y) + .05) / (Math.min(x, y) + .05); }
  function readable(color, backgrounds, toward) {
    for (var i = 0; i <= 100; i++) {
      var c = mix(color, toward, i / 100);
      if (backgrounds.every(function (bg) { return contrast(c, bg) >= 4.6; })) return c;
    }
    return toward;
  }
  function tokens(id, dark) {
    var c = palettes[id].colors, ink = id === '276' ? c[3] : mix(c[2], '#111314', .82);
    var canvas = dark ? mix(ink, c[1], .025) : c[1];
    var paper = dark ? mix(canvas, c[1], .065) : mix(canvas, '#ffffff', .72);
    var text = dark ? mix(c[1], '#ffffff', .72) : ink;
    var gun = id === '276' ? ink : c[3], bg = [canvas, paper];
    var t = {
      canvas: canvas, paper: paper, 'paper-2': mix(canvas, dark ? text : ink, .08),
      ink: text, 'ink-2': readable(mix(text, canvas, .12), bg, text),
      graphite: readable(mix(text, canvas, .36), bg, text),
      steel: mix(canvas, text, .32), rule: dark ? 'rgba(255,255,255,.16)' : 'rgba(17,19,20,.16)',
      mars: c[0], 'mars-ink': readable(c[0], bg, text), 'mars-soft': mix(paper, c[0], dark ? .18 : .22),
      moss: c[2], 'moss-ink': readable(c[2], bg, text), 'moss-soft': mix(paper, c[2], dark ? .18 : .25),
      gun: dark && id === '276' ? c[1] : gun, 'gun-ink': readable(gun, bg, text),
      'gun-soft': mix(paper, id === '276' ? ink : c[3], .14),
      jane: dark ? mix(paper, c[1], .16) : mix(c[1], c[2], .17),
      red: readable(c[0], bg, text), 'red-soft': mix(paper, c[0], .18)
    };
    ['mars', 'moss', 'gun', 'red', 'graphite'].forEach(function (key) {
      t['on-' + key] = contrast(t[key], ink) >= contrast(t[key], '#ffffff') ? readable(ink, [t[key]], '#000000') : '#ffffff';
    });
    return t;
  }
  function declarations(t) { return Object.keys(t).map(function (key) { return '--' + key + ':' + t[key] + '!important;'; }).join(''); }
  var islands = ':is(.fig,#lang-map,.plate-img,.sp,.cube,.thumbs,.part-head,.room,.sim,.colophon,.watch,.vid-th,.verbs)';
  var paletteCSS = '';
  ['276', '320'].forEach(function (id) {
    var scope = 'html[data-mtrx-palette="' + id + '"]', light = tokens(id, false), dark = tokens(id, true);
    paletteCSS += scope + '{' + declarations(light) + 'color-scheme:light}' +
      scope + '[data-theme="dark"]{' + declarations(dark) + 'color-scheme:dark}' +
      scope + '[data-theme="dark"] ' + islands + '{' + declarations(light) + '}';
  });
  var p = 'html[data-mtrx-palette] ';
  paletteCSS += p + '{--accent:var(--mars);--accent-ink:var(--mars-ink);--accent-soft:var(--mars-soft);--on-accent:var(--on-mars)}';
  var part = { 1: 'mars', 2: 'gun', 3: 'moss', 4: 'ink', 5: 'red', 6: 'graphite' };
  Object.keys(part).forEach(function (n) {
    var c = part[n], aink = c === 'ink' || c === 'graphite' || c === 'red' ? c : c + '-ink';
    var soft = c === 'ink' || c === 'graphite' ? 'jane' : c + '-soft';
    var on = c === 'ink' ? 'paper' : 'on-' + c;
    var decl = '--accent:var(--' + c + ')!important;--accent-ink:var(--' + aink + ')!important;--accent-soft:var(--' + soft + ')!important;--on-accent:var(--' + on + ')!important;';
    paletteCSS += p + '[data-part="' + n + '"],' + p + '[data-part="' + n + '"] ' + islands + '{' + decl + '}';
  });
  paletteCSS += `
html[data-mtrx-palette] :is(h1 span,.cover-title .o){color:var(--mars-ink)}
html[data-mtrx-palette] .thumb[data-t="1"]{--fg:var(--on-mars)}
html[data-mtrx-palette] .thumb[data-t="2"]{--fg:var(--on-gun)}
html[data-mtrx-palette] .thumb[data-t="3"]{--fg:var(--on-moss)}
html[data-mtrx-palette] .thumb[data-t="5"]{--fg:var(--on-red)}
html[data-mtrx-palette] .thumb[data-t="6"]{--fg:var(--on-graphite)}
html[data-mtrx-palette] .verbs li:nth-child(2){color:var(--on-mars)}
html[data-mtrx-palette] .verbs li:nth-child(3){color:var(--on-moss)}
html[data-mtrx-palette] :is(.btn-a,.sim .btn){color:var(--on-mars)}
html[data-mtrx-palette] .card[data-n="00"]{--a:var(--ink)!important;--a-ink:var(--ink)}
html[data-mtrx-palette] .card[data-n="01"]{--a:var(--mars)!important;--a-ink:var(--mars-ink)}
html[data-mtrx-palette] .card[data-n="02"]{--a:var(--moss)!important;--a-ink:var(--moss-ink)}
html[data-mtrx-palette] .card[data-n="03"]{--a:var(--red)!important;--a-ink:var(--red)}
html[data-mtrx-palette] .card[data-n="04"]{--a:var(--gun)!important;--a-ink:var(--gun-ink)}
html[data-mtrx-palette] .card[data-n="05"]{--a:var(--gun)!important;--a-ink:var(--gun-ink)}
html[data-mtrx-palette] .no{color:var(--a-ink)}
html[data-mtrx-palette] .card p{color:var(--ink-2)}
html[data-mtrx-palette] #det .bar i{background:var(--mars)!important}
html[data-mtrx-palette] .pt .bar{background:var(--paper)}
html[data-mtrx-palette] .next .btn:not(.g){color:var(--on-mars)}
html[data-mtrx-palette] .next p{color:inherit}
html[data-mtrx-palette] .next .k{color:var(--paper)}
html[data-mtrx-palette] :is(.room,.colophon){color:var(--paper)}
html[data-mtrx-palette] .room::before{color:var(--mars)}
html[data-mtrx-palette] :is(.fig,.plate-img,.sp:hover){background:var(--paper)}
html[data-mtrx-palette] .s-card{fill:var(--paper)}
html[data-mtrx-palette] input[type="date"]{color:var(--ink)}
html[data-mtrx-palette] #mtrx-transfer{background:var(--canvas);color:var(--ink);border-color:var(--ink)}
html[data-mtrx-palette] #mtrx-transfer .mt-k{color:var(--mars-ink)}
html[data-mtrx-palette] #mtrx-transfer :is(.mt-close,.mt-small){color:var(--ink)}
html[data-mtrx-palette] #mtrx-transfer textarea{background:var(--paper);color:var(--ink);border-color:var(--graphite)}
html[data-mtrx-palette] #mtrx-transfer .mt-btn{background:var(--ink);color:var(--paper);border-color:var(--ink)}
html[data-mtrx-palette] #mtrx-transfer .mt-web{background:var(--mars);color:var(--on-mars)}
html[data-mtrx-palette] :is(#mtrx-lib,#mtrx-exit,#mtrx-toast){background:var(--ink);color:var(--paper)}
html[data-mtrx-palette] #mtrx-send{background:var(--mars);color:var(--on-mars)}
html[data-mtrx-palette] #mtrx-read{background:var(--paper);color:var(--ink);box-shadow:inset 0 0 0 1.5px var(--ink)}
/* Correct / incorrect must not turn into arbitrary decorative palette colors. */
html[data-mtrx-palette] .opt.is-right{background:#e1eed8;border-color:#315b24;color:#20361b}
html[data-mtrx-palette] .opt.is-wrong{background:#f8e0dd;border-color:#9e303b;color:#5e1d25}
html[data-mtrx-palette] :is(.nk-fab[aria-pressed="true"],.nk-fab .cnt){color:var(--on-mars)}
`;
  var uiCSS = `
#mtrx-theme-toggle{display:inline-flex;align-items:center;justify-content:center;gap:7px;min-height:44px;min-width:44px;padding:8px 12px;border:1.5px solid var(--ink,#151515);border-radius:999px;background:var(--paper,#f6f4ef);color:var(--ink,#151515);font:700 14px/1 var(--sans,system-ui,sans-serif);cursor:pointer;white-space:nowrap}
#mtrx-theme-toggle svg{width:19px;height:19px;flex:none}
#mtrx-theme-home{position:fixed;right:14px;top:10px;z-index:95}
#mtrx-themes{box-sizing:border-box;width:min(520px,calc(100vw - 24px));max-height:calc(100dvh - 32px);overflow:auto;padding:24px;border:2px solid var(--ink,#151515);border-radius:22px;background:var(--paper,#f6f4ef);color:var(--ink,#151515);font:400 16px/1.5 var(--sans,system-ui,sans-serif);box-shadow:0 24px 90px #0005}
#mtrx-themes::backdrop{background:rgba(17,19,20,.55)}
#mtrx-themes h2{margin:4px 48px 8px 0;font:400 42px/1 var(--display,Impact,sans-serif);text-transform:uppercase;letter-spacing:0}
#mtrx-themes p{margin:0 0 16px}
#mtrx-themes .mtp-close{position:absolute;right:14px;top:14px;width:44px;height:44px;border:0;border-radius:50%;background:var(--canvas,#eceae4);color:inherit;font:400 26px/1 system-ui;cursor:pointer}
#mtrx-themes fieldset{padding:0;margin:0;border:0;min-width:0;display:grid;gap:10px}
#mtrx-themes legend{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}
#mtrx-themes .mtp-option{display:block;position:relative;padding:13px 14px 12px;border:2px solid var(--steel,#bcbfcc);border-radius:14px;cursor:pointer;transition:border-color .15s,background-color .15s}
#mtrx-themes .mtp-option:has(input:checked){border-color:var(--ink,#151515);background:var(--canvas,#eceae4)}
#mtrx-themes .mtp-option:has(input:focus-visible){outline:3px solid var(--ink,#151515);outline-offset:3px}
#mtrx-themes input{position:absolute;right:14px;top:16px;width:18px;height:18px;margin:0;accent-color:var(--ink,#151515)}
#mtrx-themes strong{display:block;margin-right:26px;font:800 17px/1.3 var(--sans,system-ui,sans-serif)}
#mtrx-themes .mtp-swatches{display:flex;height:24px;border:1px solid rgba(17,19,20,.18);border-radius:6px;overflow:hidden;margin:9px 0 7px}
#mtrx-themes .mtp-swatches i{flex:1}
#mtrx-themes small{display:block;font:400 14px/1.35 var(--sans,system-ui,sans-serif)}
#mtrx-themes .mtp-note{font-size:14px;color:var(--ink-2,#2b2b2b);margin:14px 0 0}
#mtrx-themes .mtp-source{display:inline-block;margin-top:10px;color:inherit;font-size:14px;text-underline-offset:3px}
#mtrx-theme-status{position:fixed;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}
#mtrx-theme-toggle:focus-visible,#mtrx-themes button:focus-visible,#mtrx-themes a:focus-visible{outline:3px solid currentColor;outline-offset:3px}
html.mtrx-read :is(#mtrx-theme-home,#mtrx-theme-toggle){display:none!important}
@media(max-width:760px){#mtrx-theme-toggle{padding:7px 10px}#mtrx-bar #mtrx-theme-toggle .mtp-label{display:none}}
@media(prefers-reduced-motion:reduce){#mtrx-themes .mtp-option{transition:none}}
@media print{#mtrx-theme-home,#mtrx-theme-toggle,#mtrx-themes,#mtrx-theme-status{display:none!important}}
`;
  var style = document.createElement('style');
  style.id = 'mtrx-palette-css'; style.textContent = paletteCSS + uiCSS;
  document.head.appendChild(style);

  function renderChoice() {
    if (!dialog) return;
    dialog.querySelectorAll('input[name="mtrx-palette"]').forEach(function (input) { input.checked = input.value === current; });
    trigger.setAttribute('aria-label', 'Choose color theme. Current: ' + palettes[current].name);
    trigger.title = 'Color theme: ' + palettes[current].name;
  }
  function apply(id, persist) {
    if (!valid(id)) id = 'original';
    current = id;
    if (id === 'original') root.removeAttribute('data-mtrx-palette');
    else root.setAttribute('data-mtrx-palette', id);
    if (persist) { try { localStorage.setItem(KEY, id); } catch (_) {} }
    renderChoice();
    if (status) status.textContent = palettes[id].name + ' theme applied.';
    window.dispatchEvent(new CustomEvent('mtrx:palette', { detail: { palette: id } }));
  }
  function close() { if (dialog && dialog.open) dialog.close(); }
  function init() {
    if (document.getElementById('mtrx-theme-toggle')) return;
    trigger = document.createElement('button');
    trigger.type = 'button'; trigger.id = 'mtrx-theme-toggle';
    trigger.setAttribute('aria-haspopup', 'dialog'); trigger.setAttribute('aria-controls', 'mtrx-themes');
    trigger.setAttribute('aria-expanded', 'false');
    trigger.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="9" cy="9" r="6"/><circle cx="15" cy="9" r="6"/><circle cx="12" cy="15" r="6"/></svg><span class="mtp-label">Themes</span>';
    var bar = document.getElementById('mtrx-bar');
    if (bar) bar.appendChild(trigger);
    else {
      var home = document.createElement('div'); home.id = 'mtrx-theme-home';
      home.appendChild(trigger); document.body.appendChild(home);
    }
    dialog = document.createElement('dialog'); dialog.id = 'mtrx-themes';
    dialog.setAttribute('aria-labelledby', 'mtrx-themes-title');
    dialog.setAttribute('data-lenis-prevent', '');
    dialog.innerHTML = '<button type="button" class="mtp-close" aria-label="Close color themes">&#215;</button>' +
      '<h2 id="mtrx-themes-title">Same field. New colors.</h2><p>Keep the notebook. Change the palette.</p>' +
      '<fieldset><legend>Color theme</legend></fieldset>' +
      '<p class="mtp-note">Saved across guides in this browser. Light/dark stays separate; artwork stays original. Text uses readable companion shades.</p>' +
      '<a class="mtp-source" href="https://colors.elwyn.co/" target="_blank" rel="noopener noreferrer">Palettes from Sanzo Wada, via Elwyn &#8599;</a>';
    var fieldset = dialog.querySelector('fieldset');
    ['original', '276', '320'].forEach(function (id) {
      var item = palettes[id], label = document.createElement('label'); label.className = 'mtp-option';
      var input = document.createElement('input');
      input.type = 'radio'; input.name = 'mtrx-palette'; input.value = id;
      input.addEventListener('change', function () { if (input.checked) apply(id, true); });
      label.appendChild(input);
      var title = document.createElement('strong'); title.textContent = item.name + (id === 'original' ? ' / default' : '');
      label.appendChild(title);
      var swatches = document.createElement('span'); swatches.className = 'mtp-swatches';
      swatches.setAttribute('aria-hidden', 'true');
      item.colors.forEach(function (color) { var swatch = document.createElement('i'); swatch.style.backgroundColor = color; swatch.title = color.toUpperCase(); swatches.appendChild(swatch); });
      label.appendChild(swatches);
      var sub = document.createElement('small'); sub.textContent = item.sub; label.appendChild(sub);
      fieldset.appendChild(label);
    });
    document.body.appendChild(dialog);
    status = document.createElement('span'); status.id = 'mtrx-theme-status'; status.setAttribute('role', 'status');
    document.body.appendChild(status);
    trigger.addEventListener('click', function () {
      if (dialog.open) return;
      dialog.showModal(); trigger.setAttribute('aria-expanded', 'true');
      dialog.querySelector('input:checked').focus();
    });
    dialog.querySelector('.mtp-close').addEventListener('click', close);
    dialog.addEventListener('close', function () {
      trigger.setAttribute('aria-expanded', 'false');
      if (!root.classList.contains('mtrx-read')) trigger.focus({ preventScroll: true });
    });
    dialog.addEventListener('click', function (event) {
      if (event.target !== dialog) return;
      var r = dialog.getBoundingClientRect();
      if (event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom) close();
    });
    /* Don't let reader shortcuts fire behind a modal. Keep native Esc close intact. */
    document.addEventListener('keydown', function (event) { if (dialog.open) event.stopPropagation(); }, true);
    if (window.MutationObserver) new MutationObserver(function () {
      if (root.classList.contains('mtrx-read')) close();
    }).observe(root, { attributes: true, attributeFilter: ['class'] });
    renderChoice();
  }
  window.MTRX_PALETTES = {
    set: function (id) { apply(id, true); },
    get: function () { return current; },
    colors: function (id) { return valid(id) ? palettes[id].colors.slice() : []; }
  };
  apply(read(), false);
  window.addEventListener('storage', function (event) { if (event.key === KEY || event.key === null) apply(read(), false); });
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, { once: true });
  else init();
})();

/* MTRX reader: scrolling only, no GSAP, reveals, parallax or DOM-wide observers.
   A short Lenis wheel glide on fine-pointer devices; native touch everywhere.
   Read mode keeps the same scroll feel. All content stays visible. */
(function () {
  'use strict';
  if (window.MTRX_SCROLL) return;
  var root = document.documentElement;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  var fine = window.matchMedia('(pointer: fine)');
  var lenis = null, loading = null, failed = false, printing = false;

  /* Stop the guides' decorative blur transitions and infinite SVG dash animation.
     Do not touch quizzes, progress, highlighting or reader controls. */
  var readingCSS = document.createElement('style');
  readingCSS.id = 'mtrx-reading-css';
  readingCSS.textContent =
    '.js .plate-img img,.js .plate.is-in .plate-img img{filter:none!important;opacity:1!important;transition:none!important}' +
    '.sp,.march{animation:none!important}' +
    '@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto!important}}';
  document.head.appendChild(readingCSS);
  function permitted() { return fine.matches && !reduced.matches && !printing; }
  function load() {
    if (window.Lenis) return Promise.resolve();
    if (!loading) loading = new Promise(function (resolve, reject) {
      var script = document.createElement('script'), settled = false;
      script.src = 'https://cdn.jsdelivr.net/npm/lenis@1.3.11/dist/lenis.min.js';
      script.async = true; script.crossOrigin = 'anonymous'; script.referrerPolicy = 'no-referrer';
      function finish(error) {
        if (settled) return;
        settled = true; clearTimeout(timer); script.onload = script.onerror = null;
        if (error) { script.remove(); reject(error); } else resolve();
      }
      var timer = setTimeout(function () { finish(new Error('Scroll library unavailable')); }, 6000);
      script.onload = function () { finish(window.Lenis ? null : new Error('Scroll library unavailable')); };
      script.onerror = function () { finish(new Error('Scroll library unavailable')); };
      document.head.appendChild(script);
    });
    return loading;
  }
  function start() {
    if (lenis || !permitted()) return;
    var css = document.createElement('style');
    css.id = 'mtrx-motion-css';
    css.textContent =
      'html.lenis,html.lenis body{height:auto;scroll-behavior:auto!important}' +
      '.lenis.lenis-smooth [data-lenis-prevent]{overscroll-behavior:contain}' +
      '.lenis.lenis-stopped{overflow:hidden}' +
      '.lenis.lenis-smooth iframe{pointer-events:none}';
    document.head.appendChild(css);
    lenis = new window.Lenis({
      autoRaf: true, autoResize: true, lerp: 0.16,
      smoothWheel: true, syncTouch: false, wheelMultiplier: 1, anchors: false,
      prevent: function (node) {
        return !!(node.matches && node.matches(
          'dialog,.nk-panel,.nk-body,.nk-find,.nk-fres,.tbl-wrap,.scroll,textarea,select,[contenteditable="true"],[data-lenis-prevent]'
        ));
      }
    });
    root.dataset.mtrxMotion = 'smooth';
    window.dispatchEvent(new CustomEvent('mtrx:motion-ready'));
  }
  function stop() {
    if (lenis) { lenis.destroy(); lenis = null; }
    var css = document.getElementById('mtrx-motion-css');
    if (css) css.remove();
    root.dataset.mtrxMotion = 'native';
  }
  function reconcile() {
    if (!permitted()) { stop(); return; }
    if (lenis || failed) return;
    root.dataset.mtrxMotion = 'loading';
    load().then(function () { if (permitted()) start(); }).catch(function () {
      failed = true; stop();
    });
  }
  function scrollTo(target, options) {
    if (lenis) { lenis.scrollTo(target, Object.assign({ lerp: 0.16 }, options)); return; }
    var el = typeof target === 'string' ? document.querySelector(target) : target;
    if (el && el.scrollIntoView) el.scrollIntoView({ behavior: reduced.matches ? 'auto' : 'smooth', block: 'start' });
    else if (typeof target === 'number') window.scrollTo({ top: target, behavior: reduced.matches ? 'auto' : 'smooth' });
  }
  window.MTRX_SCROLL = {
    refresh: function () { if (lenis) lenis.resize(); },
    scrollTo: scrollTo
  };
  /* One delegated anchor listener, including links added later by the library.
     Existing guide buttons/search keep their own native scrollIntoView handlers. */
  document.addEventListener('click', function (event) {
    if (!lenis || event.defaultPrevented || event.button !== 0 ||
        event.metaKey || event.ctrlKey || event.altKey || event.shiftKey) return;
    var link = event.target.closest && event.target.closest('a[href]');
    if (!link || link.hasAttribute('download') || (link.target && link.target !== '_self')) return;
    var url, target;
    try {
      url = new URL(link.href, location.href);
      if (url.origin !== location.origin || url.pathname !== location.pathname ||
          url.search !== location.search || !url.hash) return;
      target = document.getElementById(decodeURIComponent(url.hash.slice(1)));
    } catch (_) { return; }
    if (!target) return;
    event.preventDefault();
    lenis.scrollTo(target, {
      lerp: 0.16, offset: -(parseFloat(getComputedStyle(target).scrollMarginTop) || 16),
      onComplete: function () {
        try { if (location.hash !== url.hash) history.pushState(null, '', url.hash); } catch (_) {}
        var added = !target.hasAttribute('tabindex');
        if (added) target.setAttribute('tabindex', '-1');
        target.focus({ preventScroll: true });
        if (added) target.addEventListener('blur', function () { target.removeAttribute('tabindex'); }, { once: true });
      }
    });
  });
  [reduced, fine].forEach(function (query) {
    if (query.addEventListener) query.addEventListener('change', reconcile);
    else query.addListener(reconcile);
  });
  window.addEventListener('beforeprint', function () { printing = true; reconcile(); });
  window.addEventListener('afterprint', function () { printing = false; reconcile(); });
  reconcile();
})();

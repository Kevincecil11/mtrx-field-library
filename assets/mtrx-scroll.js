/* Native scrolling only. No wheel/touch interception, animation loop, Lenis,
   external motion dependency or automatic layout refresh. */
(function () {
  'use strict';
  if (window.MTRX_SCROLL && window.MTRX_SCROLL.native) return;
  var root = document.documentElement;
  var css = document.getElementById('mtrx-reading-css') || document.createElement('style');
  css.id = 'mtrx-reading-css';
  css.textContent =
    'html,body{scroll-behavior:auto!important}' +
    '.js .plate-img img,.js .plate.is-in .plate-img img{filter:none!important;opacity:1!important;transition:none!important}' +
    '.sp,.march{animation:none!important}';
  if (!css.parentNode) document.head.appendChild(css);
  root.dataset.mtrxMotion = 'native';
  window.MTRX_SCROLL = {
    native: true,
    refresh: function () {},
    scrollTo: function (target, options) {
      options = options || {};
      var el = target;
      if (typeof target === 'string') {
        try { el = document.querySelector(target); } catch (_) { return; }
      }
      if (typeof target === 'number') window.scrollTo({ top: target, behavior: 'instant' });
      else if (el && el.scrollIntoView) {
        var top = el.getBoundingClientRect().top + window.scrollY + (Number(options.offset) || 0);
        window.scrollTo({ top: top, behavior: 'instant' });
      }
      if (typeof options.onComplete === 'function') options.onComplete();
    }
  };
  /* Keep shared UI out of the individual lesson files. */
  var current = document.currentScript;
  if (current && current.src && !document.getElementById('mtrx-reader-script')) {
    var script = document.createElement('script');
    script.id = 'mtrx-reader-script';
    script.src = new URL('mtrx-reader.js?v=1', current.src).href;
    script.async = true;
    document.head.appendChild(script);
  }
})();

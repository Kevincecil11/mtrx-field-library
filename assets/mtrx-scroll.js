/* MTRX Field Library motion layer.
   Lenis owns wheel smoothing; GSAP owns the only animation clock.
   Touch, nested reader panels, reduced motion, print and Read mode stay native.
   No content is hidden before the optional CDN dependencies have loaded. */
(function () {
  'use strict';
  if (window.MTRX_SCROLL) return;
  var root = document.documentElement;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  var fine = window.matchMedia('(min-width: 901px) and (pointer: fine)');
  var active = null, loading = null, failed = false, printing = false;
  var source = document.currentScript && document.currentScript.src;
  var scriptLoads = {};
  var api = window.MTRX_SCROLL = {
    refresh: function () { if (active) active.refresh(); },
    scrollTo: function (target, options) {
      if (active) active.lenis.scrollTo(target, options || {});
      else {
        var el = typeof target === 'string' ? document.querySelector(target) : target;
        if (el && el.scrollIntoView) el.scrollIntoView({ block: 'start', behavior: 'auto' });
        else if (typeof target === 'number') window.scrollTo(0, target);
      }
    }
  };
  function permitted() {
    return !printing && !reduced.matches && !root.classList.contains('mtrx-read');
  }
  function load(url, ready) {
    if (ready()) return Promise.resolve();
    if (scriptLoads[url]) return scriptLoads[url];
    scriptLoads[url] = new Promise(function (resolve, reject) {
      var script = document.createElement('script'), settled = false;
      script.src = url; script.async = true; script.crossOrigin = 'anonymous';
      script.referrerPolicy = 'no-referrer';
      function finish(error) {
        if (settled) return;
        settled = true; clearTimeout(timer);
        script.onload = script.onerror = null;
        if (error) { script.remove(); reject(error); } else resolve();
      }
      var timer = setTimeout(function () { finish(new Error('Motion dependency timeout')); }, 9000);
      script.onload = function () { finish(ready() ? null : new Error('Motion dependency unavailable')); };
      script.onerror = function () { finish(new Error('Motion dependency unavailable')); };
      document.head.appendChild(script);
    });
    return scriptLoads[url];
  }
  function dependencies() {
    if (!loading) loading = Promise.all([
      load('https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js', function () { return !!window.gsap; }),
      load('https://cdn.jsdelivr.net/npm/lenis@1.3.11/dist/lenis.min.js', function () { return !!window.Lenis; })
    ]).then(function () {
      return load('https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js', function () { return !!window.ScrollTrigger; });
    });
    return loading;
  }
  function start() {
    if (active || !permitted()) return;
    var gsap = window.gsap, ScrollTrigger = window.ScrollTrigger;
    gsap.registerPlugin(ScrollTrigger);
    var css = document.createElement('style');
    css.id = 'mtrx-motion-css';
    css.textContent =
      'html.lenis,html.lenis body{height:auto}' +
      'html.lenis,html.lenis body{scroll-behavior:auto!important}' +
      '.lenis.lenis-smooth [data-lenis-prevent]{overscroll-behavior:contain}' +
      '.lenis.lenis-stopped{overflow:hidden}' +
      '.lenis.lenis-smooth iframe{pointer-events:none}' +
      '@media print{html{scroll-behavior:auto!important}}';
    document.head.appendChild(css);
    var lenis = new window.Lenis({
      autoRaf: false, lerp: 0.085, smoothWheel: true, syncTouch: false,
      anchors: false, wheelMultiplier: 1,
      prevent: function (node) {
        return !!(node.closest && node.closest(
          'dialog,.nk-panel,.nk-find,.tbl-wrap,.fig .scroll,textarea,select,[data-lenis-prevent]'
        ));
      }
    });
    var context = gsap.context(function () {}, document.body);
    var seen = new WeakSet(), triggers = [], animations = [], timer = 0, closed = false;
    function tick(seconds) { lenis.raf(seconds * 1000); }
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(tick, false, true);
    gsap.ticker.lagSmoothing(0);
    function reveal(el) {
      context.add(function () {
        animations.push(gsap.fromTo(el,
          { opacity: 0, y: 22 },
          { opacity: parseFloat(getComputedStyle(el).opacity) || 1, y: 0,
            duration: 0.65, ease: 'power3.out', overwrite: 'auto',
            clearProps: 'opacity,transform', immediateRender: false }
        ));
      });
    }
    function scan() {
      triggers = triggers.filter(function (trigger) {
        if (!trigger.trigger || !trigger.trigger.isConnected) { trigger.kill(); return false; }
        return true;
      });
      animations = animations.filter(function (animation) { return animation.isActive(); });
      var selector = window.MTRX_GUIDES
        ? '#grid .card,#next,.det.on h2,.tg,footer'
        : '.part-title,.mod-title,.day-title,.colophon h2';
      document.querySelectorAll(selector).forEach(function (el) {
        if (seen.has(el) || !el.getClientRects().length) return;
        seen.add(el);
        /* Never flash or move content the reader already has in view. */
        if (el.getBoundingClientRect().top < window.innerHeight * 0.92) return;
        context.add(function () {
          triggers.push(ScrollTrigger.create({
            trigger: el, start: 'top 92%', once: true,
            onEnter: function () { reveal(el); },
            onEnterBack: function () { reveal(el); }
          }));
        });
      });
    }
    if (fine.matches) {
      document.querySelectorAll('.cover .cover-plate,.cover .cube').forEach(function (el) {
        context.add(function () {
          gsap.to(el, {
            y: -28, ease: 'none',
            scrollTrigger: { trigger: el.closest('.cover'), start: 'top top', end: 'bottom top',
              scrub: 0.4, invalidateOnRefresh: true }
          });
        });
      });
    }
    function refresh() {
      if (closed) return;
      clearTimeout(timer);
      timer = setTimeout(function () {
        if (closed) return;
        scan(); lenis.resize(); ScrollTrigger.refresh();
      }, 160);
    }
    function anchor(event) {
      if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      var link = event.target.closest && event.target.closest('a[href]');
      if (!link || link.hasAttribute('download') || (link.target && link.target !== '_self')) return;
      var url;
      try { url = new URL(link.href, location.href); } catch (_) { return; }
      if (url.origin !== location.origin || url.pathname !== location.pathname || url.search !== location.search || !url.hash) return;
      var target;
      try { target = document.getElementById(decodeURIComponent(url.hash.slice(1))); } catch (_) { return; }
      if (!target) return;
      event.preventDefault();
      var offset = -(parseFloat(getComputedStyle(target).scrollMarginTop) || 16);
      lenis.scrollTo(target, {
        offset: offset, duration: 0.9,
        onComplete: function () {
          /* Preserve Back navigation and keyboard focus without another browser jump. */
          try { if (location.hash !== url.hash) history.pushState(null, '', url.hash); } catch (_) {}
          var added = !target.hasAttribute('tabindex');
          if (added) target.setAttribute('tabindex', '-1');
          target.focus({ preventScroll: true });
          if (added) target.addEventListener('blur', function () { target.removeAttribute('tabindex'); }, { once: true });
        }
      });
    }
    function settleFocus(event) {
      animations.forEach(function (animation) {
        var targets = animation.targets();
        if (targets.some(function (el) { return el === event.target || el.contains(event.target); })) animation.progress(1);
      });
    }
    var changes = new MutationObserver(refresh);
    changes.observe(document.body, { childList: true, subtree: true });
    var size = window.ResizeObserver ? new ResizeObserver(refresh) : null;
    if (size) size.observe(document.body);
    document.addEventListener('click', anchor);
    document.addEventListener('click', refresh);
    document.addEventListener('toggle', refresh, true);
    document.addEventListener('load', refresh, true);
    document.addEventListener('focusin', settleFocus);
    window.addEventListener('resize', refresh);
    window.addEventListener('pageshow', refresh);
    window.addEventListener('mtrx:synced', refresh);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(refresh);
    active = {
      lenis: lenis, refresh: refresh,
      stop: function () {
        closed = true; clearTimeout(timer); changes.disconnect(); if (size) size.disconnect();
        document.removeEventListener('click', anchor);
        document.removeEventListener('click', refresh);
        document.removeEventListener('toggle', refresh, true);
        document.removeEventListener('load', refresh, true);
        document.removeEventListener('focusin', settleFocus);
        window.removeEventListener('resize', refresh);
        window.removeEventListener('pageshow', refresh);
        window.removeEventListener('mtrx:synced', refresh);
        lenis.off('scroll', ScrollTrigger.update);
        gsap.ticker.remove(tick);
        context.revert(); lenis.destroy(); css.remove();
      }
    };
    root.dataset.mtrxMotion = 'smooth';
    scan(); refresh();
    window.dispatchEvent(new CustomEvent('mtrx:motion-ready'));
  }
  function reconcile() {
    if (!permitted()) {
      if (active) { active.stop(); active = null; }
      root.dataset.mtrxMotion = 'native';
      return;
    }
    if (active || failed) return;
    root.dataset.mtrxMotion = 'loading';
    dependencies().then(function () {
      if (permitted()) start();
    }).catch(function () {
      failed = true; root.dataset.mtrxMotion = 'native';
      /* CDN blocked or slow? The original page remains fully readable and usable. */
      if (active) { active.stop(); active = null; }
    });
  }
  var mode = new MutationObserver(reconcile);
  mode.observe(root, { attributes: true, attributeFilter: ['class'] });
  function listen(query) {
    if (query.addEventListener) query.addEventListener('change', reconcile);
    else query.addListener(reconcile);
  }
  listen(reduced);
  /* Rebuild only the optional desktop parallax when crossing a device breakpoint. */
  function deviceChange() {
    if (active) { active.stop(); active = null; }
    reconcile();
  }
  if (fine.addEventListener) fine.addEventListener('change', deviceChange); else fine.addListener(deviceChange);
  window.addEventListener('beforeprint', function () { printing = true; reconcile(); });
  window.addEventListener('afterprint', function () { printing = false; reconcile(); });
  api.source = source;
  reconcile();
})();

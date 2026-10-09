/* One reader launcher replaces both floating button clusters.
   Move the original controls, not clones: notes/search/progress listeners survive.
   Only the root class and the existing toolbar's direct children are observed. */
(function () {
  'use strict';
  if (window.MTRX_READER) return;
  var root = document.documentElement, launcher, panel, groups;
  var css = document.createElement('style');
  css.id = 'mtrx-reader-css';
  css.textContent = `
#mtrx-reader-toggle{position:fixed;top:max(12px,env(safe-area-inset-top));left:max(12px,env(safe-area-inset-left));z-index:95;display:flex;align-items:center;gap:10px;min-height:44px;padding:0 15px;border:1px solid var(--rule,#ccc);border-radius:12px;background:var(--paper,#f6f4ef);color:var(--ink,#151515);font:800 15px/1 var(--sans,system-ui,sans-serif);box-shadow:0 3px 12px #00000012;cursor:pointer}
#mtrx-reader-toggle svg{width:18px;height:18px}
#mtrx-reader-panel{box-sizing:border-box;position:fixed;inset:64px auto auto 12px;margin:0;width:min(336px,calc(100vw - 24px));max-height:calc(100dvh - 80px);overflow:auto;padding:16px;border:1px solid var(--rule,#ccc);border-radius:18px;background:var(--paper,#f6f4ef);color:var(--ink,#151515);font:400 16px/1.5 var(--sans,system-ui,sans-serif);box-shadow:0 16px 55px #0003}
#mtrx-reader-panel::backdrop{background:rgba(17,19,20,.28)}
#mtrx-reader-panel .mr-head{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:12px}
#mtrx-reader-panel h2{margin:0;font:800 20px/1.2 var(--sans,system-ui,sans-serif);letter-spacing:0;text-transform:none}
#mtrx-reader-panel .mr-close{display:flex;align-items:center;justify-content:center;width:44px;height:44px;border:0;border-radius:10px;background:transparent;color:inherit;font:400 26px/1 system-ui;cursor:pointer}
#mtrx-reader-panel .mr-caption{margin:12px 10px 6px;font:700 14px/1.4 var(--sans,system-ui,sans-serif);color:var(--ink-2,#2b2b2b)}
#mtrx-reader-panel .mr-caption[hidden]{display:none}
html #mtrx-reader-panel :is(#mtrx-bar,.nk-dock){position:static!important;display:grid;grid-template-columns:1fr;gap:4px;inset:auto;margin:0;padding:0;transform:none;box-shadow:none}
html #mtrx-reader-panel :is(.mtrx-fab,.nk-fab,#mtrx-theme-toggle){box-sizing:border-box;display:flex;align-items:center;justify-content:flex-start;gap:10px;width:100%;min-width:0;height:auto;min-height:46px;padding:11px 12px;border:0;border-radius:10px;background:transparent;color:var(--ink,#151515);font:700 16px/1.3 var(--sans,system-ui,sans-serif);letter-spacing:0;text-transform:none;text-decoration:none;box-shadow:none;white-space:normal;cursor:pointer}
html #mtrx-reader-panel :is(.mtrx-fab,.nk-fab,#mtrx-theme-toggle):hover{background:var(--canvas,#eceae4);color:var(--ink,#151515)}
html #mtrx-reader-panel :is(.lg,.t,.mtp-label){display:inline!important}
html #mtrx-reader-panel .nk-fab .ic{width:20px;font-size:17px;text-align:center}
html #mtrx-reader-panel .nk-fab .cnt{margin-left:auto;background:var(--canvas,#eceae4);color:var(--ink,#151515);font-size:14px}
html #mtrx-reader-panel #mtrx-read{background:var(--canvas,#eceae4)}
#mtrx-reader-toggle:focus-visible,#mtrx-reader-panel :is(button,a):focus-visible{outline:2px solid var(--ink,#151515);outline-offset:2px}
html.mtrx-read #mtrx-reader-toggle{display:none!important}
@media(max-width:600px){#mtrx-reader-panel{inset:auto 12px max(12px,env(safe-area-inset-bottom)) 12px;width:auto;max-height:calc(100dvh - 32px)}}
@media print{#mtrx-reader-toggle,#mtrx-reader-panel{display:none!important}}
`;
  document.head.appendChild(css);
  function close() { if (panel && panel.open) panel.close(); }
  function collect() {
    if (!panel) return;
    var bar = document.getElementById('mtrx-bar');
    if (bar && bar.parentNode !== groups.primary) groups.primary.appendChild(bar);
    var dock = document.querySelector('.nk-dock');
    if (dock && dock.parentNode !== groups.study) groups.study.appendChild(dock);
    groups.caption.hidden = !dock;
    /* Dark mode can be icon-only in the old dock; give it a visible label without
       modifying the icon or the original click listener. */
    if (dock) dock.querySelectorAll('.nk-fab').forEach(function (button) {
      var visible = button.textContent.trim();
      if ((!visible || visible.length < 4) && !button.querySelector('.mr-label')) {
        var label = document.createElement('span'); label.className = 'mr-label';
        label.textContent = 'Light / dark'; button.appendChild(label);
        button.setAttribute('aria-label', 'Toggle light or dark reading mode');
      }
    });
    var theme = document.getElementById('mtrx-theme-toggle');
    if (theme && !panel.contains(theme)) groups.primary.appendChild(theme);
  }
  function init() {
    /* The library home has only the theme button; no reader menu needed there. */
    if (!document.getElementById('mtrx-bar')) return;
    launcher = document.createElement('button');
    launcher.id = 'mtrx-reader-toggle'; launcher.type = 'button';
    launcher.setAttribute('aria-haspopup', 'dialog'); launcher.setAttribute('aria-expanded', 'false');
    launcher.setAttribute('aria-controls', 'mtrx-reader-panel');
    launcher.innerHTML = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M3 4h14M3 10h14M3 16h14"/><circle cx="7" cy="4" r="2" fill="currentColor"/><circle cx="13" cy="10" r="2" fill="currentColor"/><circle cx="7" cy="16" r="2" fill="currentColor"/></svg><span>Reader</span>';
    document.body.appendChild(launcher);
    panel = document.createElement('dialog'); panel.id = 'mtrx-reader-panel';
    panel.setAttribute('aria-labelledby', 'mtrx-reader-title');
    panel.innerHTML = '<div class="mr-head"><h2 id="mtrx-reader-title">Reader tools</h2><button class="mr-close" type="button" aria-label="Close reader tools">&#215;</button></div><div class="mr-primary"></div><p class="mr-caption">Study tools</p><div class="mr-study"></div>';
    document.body.appendChild(panel);
    groups = { primary: panel.querySelector('.mr-primary'), study: panel.querySelector('.mr-study'), caption: panel.querySelector('.mr-caption') };
    collect();
    launcher.addEventListener('click', function () {
      collect(); panel.showModal(); launcher.setAttribute('aria-expanded', 'true');
      panel.querySelector('.mr-close').focus();
    });
    panel.querySelector('.mr-close').addEventListener('click', close);
    /* Close before the original handler opens notes/search/themes/progress.
       Do not intercept keyboard activation, hrefs or the original event itself. */
    panel.addEventListener('click', function (event) {
      var control = event.target.closest('button,a');
      if (control && !control.classList.contains('mr-close')) close();
    }, true);
    panel.addEventListener('click', function (event) {
      if (event.target !== panel) return;
      var r = panel.getBoundingClientRect();
      if (event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom) close();
    });
    panel.addEventListener('close', function () {
      launcher.setAttribute('aria-expanded', 'false');
      /* A subsequent control may already own focus; never steal it. */
      if (!root.classList.contains('mtrx-read') && (panel.contains(document.activeElement) || document.activeElement === document.body)) launcher.focus({ preventScroll: true });
    });
    document.addEventListener('keydown', function (event) { if (panel.open) event.stopPropagation(); }, true);
    window.addEventListener('mtrx:themes-ready', collect);
    if (window.MutationObserver) {
      new MutationObserver(function () { if (root.classList.contains('mtrx-read')) close(); }).observe(root, { attributes: true, attributeFilter: ['class'] });
      var bar = document.getElementById('mtrx-bar');
      if (bar) new MutationObserver(collect).observe(bar, { childList: true });
    }
  }
  window.MTRX_READER = { close: close };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, { once: true });
  else init();
})();

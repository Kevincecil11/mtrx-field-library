/* MTRX Field Library: shared add-on loaded by every guide.
   v0: adds a "Library" link. The Telegram review sync is added here later,
   so guides never need re-uploading when the review engine changes. */
(function(){
  if (document.getElementById('mtrx-lib')) return;
  var a = document.createElement('a');
  a.id = 'mtrx-lib'; a.href = '../index.html'; a.textContent = '\u2190 Library';
  a.setAttribute('aria-label', 'Back to the MTRX Field Library');
  a.style.cssText = 'position:fixed;left:14px;top:14px;z-index:95;background:#151515;color:#F6F4EF;' +
    'font:700 13px/1 "JetBrains Mono",ui-monospace,monospace;letter-spacing:.08em;text-transform:uppercase;' +
    'padding:9px 13px;border-radius:999px;text-decoration:none;box-shadow:0 6px 14px -8px rgba(0,0,0,.5)';
  document.body.appendChild(a);
})();

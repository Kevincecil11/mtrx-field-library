"""No.07 editorial edition: monograph reading, chapter rhythms, atelier studies.
One additive build transform. Original lesson text, stop IDs and reader keys survive.
The eight style dials are a teaching heuristic, not a scientific taxonomy.
"""
import base64, html, json, re
from pathlib import Path
from bs4 import BeautifulSoup

HERE = Path(__file__).parent
E = html.escape

CSS = r"""
/* Signature: the changing exhibition, held together by a quiet book grid. */
:root{--radius:0px;--book:Georgia,'Times New Roman',serif;--canvas:#eceae4;--paper:#f7f5ef;--display:"Tanker","MTRX Narrow",Impact,"Arial Narrow",sans-serif}
body{font-size:17px;line-height:1.7}
.site{padding:80px 28px 90px 174px}
.wrap{max-width:1220px;padding:0 38px}
.ed-mast{position:fixed;inset:0 0 auto;height:76px;z-index:91;background:var(--canvas);border-bottom:1px solid var(--rule);display:flex;align-items:center;gap:28px;padding:0 30px}
.ed-brand{font:400 32px/1 var(--display);text-decoration:none;letter-spacing:-1px}
.ed-mast .ed-label{font:600 14px/1.3 var(--mono);letter-spacing:.1em}
.ed-mast>a:last-child{font:700 14px var(--sans);margin-left:auto;margin-right:140px}
html #mtrx-reader-toggle{left:auto!important;right:24px;top:16px;border-radius:0;box-shadow:none}
html #mtrx-reader-panel{left:auto;right:24px;inset:70px 24px auto auto}
.nk-dock{left:auto;right:24px;top:17px;bottom:auto;gap:5px}
.nk-fab{box-shadow:none;border:0;border-radius:0;background:transparent;padding:9px 10px;font-size:14px}
.nk-panel{z-index:120}.nk-pop{z-index:125}.nk-find{z-index:121}
.thumbs{left:24px;right:auto;top:112px;bottom:80px;transform:none;width:135px;gap:0;overflow:auto;border-left:1px solid var(--rule)}
.thumb,.thumb.is-active{width:100%;height:49px;min-height:49px;border-radius:0;background:transparent!important;color:var(--ink)!important;box-shadow:none;justify-content:flex-start;padding:0 12px;border-left:2px solid transparent}
.thumb .lbl{writing-mode:horizontal-tb;transform:none;font:600 14px var(--sans);letter-spacing:0;text-transform:none}
.thumb .short{display:inline;margin-right:8px;color:var(--graphite)}
.thumb .full{display:inline}.thumb .lbl{display:flex;flex-direction:row-reverse;justify-content:flex-end;align-items:center}
.thumb.is-active{border-left-color:var(--mars);color:var(--mars-ink)!important}
.thumb i{width:2px;left:0;background:var(--mars)}
.cover{min-height:0;padding-top:50px;padding-bottom:50px;display:block}
.ed-cover-top{display:flex;justify-content:space-between;gap:22px;border-top:1px solid var(--ink);padding:15px 0;font:500 14px var(--mono);letter-spacing:.08em}
.ed-cover-grid{display:grid;grid-template-columns:1fr 1.2fr;gap:35px;align-items:end}
.cover-title{font:400 clamp(70px,8.5vw,130px)/.92 var(--display);margin:26px 0;letter-spacing:-.02em;max-width:7ch}
.cover-title .o{color:var(--ink)}.ed-issue{color:var(--mars);font:400 80px/.9 var(--display);display:block;margin:20px 0}
.cover-sub{font:400 20px/1.5 var(--book);max-width:29ch}.ed-cover-image{margin:0;position:relative}
.ed-cover-image>img{width:100%;height:540px;object-fit:cover;object-position:center;background:#ddd9cd}
.ed-cover-image figcaption{font:500 14px/1.5 var(--mono);margin-top:12px}
.ed-paper-note{position:absolute;right:-14px;bottom:70px;background:#f7f5efe8;color:#151515;max-width:205px;padding:20px;transform:rotate(3deg);box-shadow:0 5px 20px #0001;font:italic 20px/1.3 var(--book);border-top:3px solid var(--mars)}
.ed-cover-foot{display:grid;grid-template-columns:1.3fr 1fr;gap:40px;margin:35px 0 0;padding-top:22px;border-top:1px solid var(--rule)}
.ed-cover-foot p{font:500 14px/1.7 var(--mono);margin:0}
.ed-actions{display:flex;align-items:center;gap:24px;flex-wrap:wrap}.ed-actions a{font:700 15px var(--sans)}
.ed-actions a:first-child{padding:14px 19px;background:var(--ink);color:var(--paper);text-decoration:none}
.ed-strip{display:flex;align-items:center;gap:20px;padding:22px 0;border-bottom:1px solid var(--ink);font:500 14px/1.6 var(--mono)}
.ed-strip b{color:var(--mars-ink);white-space:nowrap}.ed-strip p{margin:0}
.part-head{background:var(--paper);color:var(--ink);padding:65px 0;margin:70px 0 0;border-top:1px solid var(--ink)}
.part-title{font-size:clamp(50px,6.7vw,96px);max-width:17ch;line-height:.98;letter-spacing:-.015em}
.part-promise{font:400 21px/1.5 var(--book);max-width:48ch}
.stops{grid-template-columns:1fr 1fr;gap:4px 30px}.stops a{font:500 16px/1.5 var(--sans);border-bottom:1px solid var(--rule);padding:13px 0}
.stops a span{color:var(--mars-ink)}.stops a em{font-size:14px}
#s1 .part-head{background:#2f3e46;color:#f6f4ef}#s1 .part-head .kicker,#s1 .stops a span{color:#f4e3b2}
#s3 .part-head .part-title{font-family:var(--book);text-transform:none;font-weight:400}
#s4 .part-head{background:#e2c64a;color:#151515}
#s5 .part-head{background:#23231f;color:#f6f4ef}#s5 .part-head .kicker,#s5 .stops a span{color:#edb28e}
#s6 .part-head{background:#e1e2d6;color:#151515}
#s8 .part-head{background:#c3d5d1;color:#151515}
.mod{padding:70px 0 30px;border-bottom:1px solid var(--rule);scroll-margin-top:95px}
.mod-title{font-size:clamp(42px,5vw,68px);max-width:24ch;line-height:1.06;letter-spacing:-.01em}
.mod-meta{letter-spacing:.04em;line-height:1.5;flex-wrap:wrap;font-size:14px}
.mod-why{font:400 21px/1.55 var(--book);max-width:55ch}
.qline{border:0!important;border-left:3px solid var(--mars)!important;border-radius:0!important;background:transparent!important;padding:9px 0 9px 20px!important}
.story>p{max-width:66ch;font:400 20px/1.8 var(--book);margin:22px auto 26px 0}
.mod>h3{margin-top:48px;font:700 15px/1.5 var(--sans);text-transform:uppercase;letter-spacing:.14em;color:var(--graphite);border-top:1px solid var(--rule);padding-top:17px}
.dossier,.predict,.writer,.mtrx,.drill,.tryit,.philo,.distil,.check,.fig,.fields>div,.read-card,.spec,.stats>div,.later{border-radius:0!important;box-shadow:none!important}
.dossier{border:1px solid var(--rule);max-width:100%;margin:32px 0}.dos-body{background:var(--paper);padding:22px}
.dossier>.stamp{max-width:calc(100% - 44px);white-space:normal;line-height:1.4}
.dos-tab{border-radius:0;background:var(--ink);color:var(--paper)}
.predict{background:transparent;padding:24px 0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.predict .reveal{border-radius:0;background:var(--paper);padding:15px}.predict p{max-width:70ch}
.watch3{grid-template-columns:minmax(220px,1fr) 1fr;gap:30px;padding:20px 0;border-bottom:1px solid var(--rule)}
.vid{border-radius:0;box-shadow:none}.vid:hover{transform:none;box-shadow:none}
.specs{gap:22px}.spec{background:transparent;border-top:2px solid var(--ink);padding:16px 0}
.spec-name{font-size:20px}.philo{background:var(--paper);border-left:0;border-top:1px solid var(--ink);padding:30px}
.philo blockquote,.philo-idea{font:400 27px/1.45 var(--book)}.philo-q{border-radius:0;background:transparent;border-top:1px solid var(--rule);padding:15px 0 0}
.writer{background:transparent!important;border-left:3px solid var(--gun);padding:18px 24px}.mtrx{background:#e8e2ce;color:#151515}
.tryit{background:transparent!important;border:1px solid var(--ink);padding:24px}.room{border-radius:0;padding:22px;margin-top:26px}
.distil{background:transparent;border-top:1px solid var(--rule);padding:22px 0}.distil ul{display:block}.distil li{padding:8px 0}
.fig{background:#f7f5ef;padding:20px}.fig svg{min-width:680px}
.check{max-width:none;border-top:1px solid var(--rule);background:transparent;padding:24px 0}.opt{border-radius:0;background:var(--paper);border:1px solid var(--rule);padding:15px 18px}
.done{border-radius:0!important}.deeper{border-radius:0!important;box-shadow:none!important;border:1px solid var(--rule)}
.plate{display:block!important;padding:0;margin:40px 0;background:transparent;box-shadow:none}
.plate-img{position:relative;top:auto;aspect-ratio:auto;background:transparent;border-radius:0;padding:0;display:block;overflow:hidden}
.plate .plate-img img,.js .plate.is-in .plate-img img,.js .plate .plate-img img{display:block;width:100%;height:auto;max-height:710px;object-fit:contain;border-radius:0;mix-blend-mode:normal;opacity:1;filter:blur(var(--squint,0px)) grayscale(var(--mono-img,0));transition:filter .12s linear}
html body .site .plate .plate-img img{filter:blur(var(--squint,0px)) grayscale(var(--mono-img,0))!important}
.plate-vals{margin-top:16px;gap:16px}.plate-vals img{border-radius:0;max-height:330px;object-fit:contain}
.plate>figcaption{margin:16px 0;display:block}.plate-cap{display:block;font:400 18px/1.5 var(--book);max-width:72ch}.credit{font-size:14px;display:block;margin-top:10px}
.ed-lab-controls{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin:15px 0;padding:15px 0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);font:600 14px var(--sans)}
.ed-lab-controls label{display:flex;align-items:center;gap:12px}.ed-lab-controls input[type=range]{width:180px;accent-color:var(--mars)}
.ed-lab-controls button{border:1px solid var(--rule);background:var(--paper);border-radius:0;padding:9px 12px;font:600 14px var(--sans)}
.ed-lab-controls button[aria-pressed=true]{background:var(--ink);color:var(--paper)}
.ed-overlay{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;display:none}
.show-guides .ed-overlay{display:block}.ed-lab-note{font:400 14px/1.5 var(--mono);color:var(--graphite)}
.ed-atlas{margin-top:50px}.ed-section-intro{max-width:65ch;font:400 21px/1.6 var(--book)}
.ed-dial-lab{display:grid;grid-template-columns:minmax(240px,.8fr) 1.2fr;gap:40px;padding:30px 0 45px;border-block:1px solid var(--rule)}
.ed-dials{display:grid;gap:12px}.ed-dial label{display:flex;justify-content:space-between;font:600 14px var(--sans)}
.ed-dial input{width:100%;accent-color:var(--mars);margin:10px 0 0}.ed-dial small{font:400 14px var(--mono);display:flex;justify-content:space-between}
.ed-live{align-self:start;position:sticky;top:96px;min-height:400px;background:#e9e5d7;color:#151515;padding:25px;overflow:hidden;border:1px solid #b6b1a2}
.ed-live .live-head{display:flex;justify-content:space-between;font:600 14px Arial}.ed-live h4{font:400 44px/.98 Impact;margin:25px 0 18px;max-width:10ch}
.ed-live img{width:100%;height:170px;object-fit:cover}.ed-live p{font:400 16px/1.5 Georgia;margin:18px 0}
.ed-live .live-extra{display:none}.ed-live .live-extra span{display:block;border-top:1px solid currentColor;padding:7px 0;font:600 14px Arial}
.ed-live footer{font:600 14px Arial;border-top:1px solid currentColor;padding-top:12px}
.ed-presets{display:flex;gap:8px;flex-wrap:wrap;margin:18px 0}.ed-presets button,.ed-compare button{border:1px solid var(--rule);background:var(--paper);padding:10px 14px;border-radius:0;font:600 14px var(--sans)}
.ed-dial-note{font:400 14px/1.6 var(--mono);margin-top:16px;max-width:70ch}
.ed-filter{position:sticky;top:76px;z-index:20;background:var(--canvas);display:grid;grid-template-columns:1fr 1fr auto;gap:12px;padding:18px 0;border-bottom:1px solid var(--ink);margin:40px 0 28px}
.ed-filter label{font:600 14px var(--sans);display:grid;gap:6px}.ed-filter input,.ed-filter select,.ed-compare select{min-width:0;width:100%;padding:12px;background:var(--paper);border:1px solid var(--rule);color:var(--ink);font:400 16px var(--sans);border-radius:0}
.ed-filter output{font:600 14px var(--mono);align-self:end;padding-bottom:12px}
.ed-atlas-grid{display:grid;grid-template-columns:1fr 1fr;gap:50px 32px}
.ed-style{min-width:0;scroll-margin-top:185px;border-bottom:1px solid var(--rule);padding-bottom:28px}
.ed-style[hidden]{display:none}
.ed-style-art{aspect-ratio:3/2;position:relative;overflow:hidden;background:#e7e4da;margin:0 0 14px}
.ed-style-art img{width:100%;height:100%;object-fit:cover}.ed-style-art svg{display:block;width:100%;height:100%}
.ed-style-art figcaption{position:absolute;left:10px;bottom:10px;background:#f6f4efed;color:#151515;padding:4px 7px;font:500 14px/1.3 var(--sans)}
.ed-style-meta{font:500 14px/1.5 var(--mono);color:var(--graphite);margin:0 0 8px}
.ed-style h3{font:400 32px/1.1 var(--display);text-transform:uppercase;margin:8px 0 16px}
.ed-style p{font:400 17px/1.6 var(--book)}.ed-cues{list-style:none;padding:0;margin:0 0 16px;display:flex;flex-wrap:wrap;gap:5px 14px}
.ed-cues li{font:600 14px/1.5 var(--sans);padding:3px 0;border-bottom:1px solid var(--rule)}
.ed-style details{border-top:1px solid var(--rule);padding:12px 0;font-size:16px}
.ed-style summary{cursor:pointer;font:700 14px var(--sans);padding:5px 0}.ed-style details p{margin:13px 0}
.ed-style .ed-source{font:400 14px/1.6 var(--sans);overflow-wrap:anywhere}
.ed-style details a{display:block;margin-top:7px}
.ed-compare{border-block:1px solid var(--rule);padding:25px 0;margin:40px 0}
.ed-compare-fields{display:grid;grid-template-columns:1fr 1fr;gap:25px}
.ed-compare label{font:600 14px var(--sans);display:grid;gap:8px}
.ed-compare-result{display:grid;grid-template-columns:1fr 1fr;gap:25px;margin-top:25px}.ed-compare-result h4{font:400 26px var(--display);margin-top:15px}
.ed-compare-result p{font:400 17px/1.5 var(--book)}
.ed-workbench{margin:45px 0;border-top:3px solid var(--mars);padding:35px 0}
.ed-workbench h3{font:400 40px/1.1 var(--display);text-transform:uppercase;margin:10px 0 20px}
.ed-ratio-stage{display:grid;grid-template-columns:61.8fr 38.2fr;min-height:180px;margin:20px 0;gap:0}
.ed-ratio-stage>div{padding:30px 20px;background:#2f3e46;color:#f6f4ef;font:500 18px var(--mono);display:flex;flex-direction:column;justify-content:space-between}
.ed-ratio-stage>div+div{background:#ed691d;color:#151515}.ed-ratio-stage strong{font:400 46px var(--display)}
.ed-scale{display:flex;align-items:baseline;gap:24px;flex-wrap:wrap;border-bottom:1px solid var(--rule);padding-bottom:20px}
.ed-scale span{line-height:1.2}.ed-scale small{display:block;font:500 14px var(--mono);margin-top:10px}
.ed-coverage{padding:25px 0;border-block:1px solid var(--rule);margin:35px 0}
.ed-coverage p{font:400 16px/1.65 var(--sans)}
.ed-noresults{padding:35px 0;font:400 22px var(--book)}
.colophon{background:var(--paper);color:var(--ink);margin-top:60px}.colophon .vids{gap:0 25px}
.read-card{background:transparent;border-top:1px solid var(--rule);padding:18px 0}
html[data-theme=dark]{--canvas:#181916;--paper:#24261f;--paper-2:#30332a;--ink:#f2f0e9;--ink-2:#e3e0d6;--graphite:#bcbeb2;--rule:rgba(255,255,255,.2);--mars-ink:#f5ad7e}
html[data-theme=dark] body{background:#181916;color:#f2f0e9}
[data-theme=dark] .ed-mast,[data-theme=dark] .ed-filter{background:#181916}
html[data-theme=dark] #mtrx-reader-toggle{background:#24261f;color:#f2f0e9}
[data-theme=dark] .ed-mast,[data-theme=dark] .thumbs{--ink:#f2f0e9;--paper:#181916;--graphite:#bebeb2;--mars-ink:#f4ab7a}
[data-theme=dark] .thumb{color:#f2f0e9!important}
[data-theme=dark] .part-head:not(#s1 .part-head):not(#s4 .part-head):not(#s5 .part-head):not(#s6 .part-head):not(#s8 .part-head){background:#22241f;color:#f2f0e9}
[data-theme=dark] .plate{background:transparent}[data-theme=dark] .philo{background:#262821}
[data-theme=dark] .writer{color:#eeece4}[data-theme=dark] .colophon{background:#24261f;color:#eeece4}
[data-theme=dark] .ed-style-art{color:#151515}
@media(min-width:1500px){.ed-cover-image>img{height:610px}.wrap{max-width:1280px}}
@media(max-width:1100px){.site{padding-left:125px;padding-right:16px}.thumbs{left:12px;width:106px}.thumb{padding-left:8px}.thumb .lbl{font-size:14px}.thumb .short{display:none}.wrap{padding:0 22px}.ed-cover-grid{gap:25px}.ed-cover-image>img{height:450px}.ed-mast .ed-label{display:none}.ed-dial-lab{gap:24px}.ed-style h3{font-size:28px}.ed-cover-foot{gap:22px}}
@media(max-width:760px){
.site{padding:64px 0 100px}.wrap{padding:0 21px}.ed-mast{height:64px;padding:0 20px}.ed-brand{font-size:27px}.ed-mast>a:last-child{margin-right:130px;font-size:14px}.nk-dock{right:9px;top:10px}.nk-fab{padding:9px 7px}.nk-fab span.t{display:none}
.thumbs{left:0;right:0;top:auto;bottom:0;width:100%;height:55px;flex-direction:row;overflow-x:auto;background:var(--canvas);border:0;border-top:1px solid var(--rule);gap:0;z-index:90}
.thumb,.thumb.is-active{min-width:64px;width:auto;height:54px;min-height:54px;flex:0 0 64px;justify-content:center;padding:6px;border-left:0;border-top:2px solid transparent}.thumb.is-active{border-top-color:var(--mars)}.thumb .short{display:inline;margin:0}.thumb .full{display:none}
.thumb i{height:2px;width:calc(var(--p,0) * 1%)}
.cover{padding-top:28px;padding-bottom:25px}.ed-cover-top{font-size:14px;gap:12px}.ed-cover-grid{grid-template-columns:1fr;gap:25px}
.cover-title{font-size:86px;max-width:10ch;margin:16px 0}.ed-issue{display:inline;font-size:55px;margin:0}.cover-sub{font-size:20px;max-width:31ch;margin:0}
.ed-cover-image>img{height:auto;max-height:470px;object-fit:contain}.ed-paper-note{right:8px;bottom:52px;max-width:155px;font-size:17px;padding:14px}
.ed-cover-foot{grid-template-columns:1fr;gap:20px;margin-top:25px}.ed-strip{display:block}.ed-strip b{display:block;margin-bottom:10px}
.part-head{padding:40px 0;margin-top:45px}.part-title{font-size:52px}.part-promise{font-size:20px}.stops{grid-template-columns:1fr}
.mod{padding-top:45px;scroll-margin-top:78px}.mod-title{font-size:43px}.mod-meta{font-size:14px}.story>p{font-size:19px;line-height:1.72}
.dossier{grid-template-columns:minmax(0,1fr)}.dos-body{min-width:0;overflow-wrap:anywhere}.dos-facts{grid-template-columns:minmax(0,1fr)}.dos-tab{min-width:0}
.watch3{grid-template-columns:1fr}.specs{grid-template-columns:1fr}.plate-vals{grid-template-columns:1fr 1fr}
.ed-dial-lab{grid-template-columns:1fr}.ed-live{position:relative;top:auto}.ed-dials{grid-template-columns:1fr 1fr;gap:18px}.ed-dial small{font-size:14px}.ed-dial label{display:block}.ed-dial output{float:right}
.ed-filter{top:64px;grid-template-columns:1fr;gap:9px;padding:12px 0;position:relative}.ed-filter output{padding:0}.ed-atlas-grid{grid-template-columns:1fr;gap:35px}.ed-style-art{aspect-ratio:3/2}.ed-style h3{font-size:33px}
.ed-compare-fields,.ed-compare-result{gap:12px}.ed-compare-result .ed-style-art{aspect-ratio:1}.ed-compare-result .ed-style-art figcaption{display:none}.ed-compare-result h4{font-size:23px}.ed-compare-result p{font-size:16px}
.ed-lab-controls{gap:10px}.ed-lab-controls input[type=range]{width:130px}.ed-ratio-stage>div{padding:20px 12px}.ed-ratio-stage strong{font-size:33px}.ed-scale{gap:15px}.philo{padding:23px}.philo blockquote{font-size:24px}
.nk-dock{bottom:auto}.ed-section-intro{font-size:20px}.dos-name{overflow-wrap:anywhere}
}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation:none!important;transition:none!important}}
@media print{.ed-mast,.thumbs,.nk-dock,.ed-filter,.ed-presets{display:none!important}.site{padding:0}.ed-style{break-inside:avoid}.ed-live{position:static}.ed-atlas-grid{display:block}.ed-style-art{max-height:250px}}
"""

JS = r"""
(()=>{'use strict';
const q=(s,e=document)=>e.querySelector(s),qa=(s,e=document)=>[...e.querySelectorAll(s)];
qa('.plate').forEach(p=>{
 const im=q('.plate-img img',p);if(!im)return;
 const range=q('.ed-squint',p),mono=q('.ed-mono',p),guides=q('.ed-guides',p);
 const update=()=>{p.style.setProperty('--squint',range.value+'px');q('output',p).textContent=range.value+'px';};
 range.addEventListener('input',update);
 mono.addEventListener('click',()=>{const on=mono.getAttribute('aria-pressed')!=='true';mono.setAttribute('aria-pressed',on);p.style.setProperty('--mono-img',on?1:0)});
 guides.addEventListener('click',()=>{const on=p.classList.toggle('show-guides');guides.setAttribute('aria-pressed',on)});
 q('.ed-reset',p).addEventListener('click',()=>{range.value=0;update();mono.setAttribute('aria-pressed','false');p.style.setProperty('--mono-img',0);p.classList.remove('show-guides');guides.setAttribute('aria-pressed','false')});
});
const atlas=q('#m6-3');if(atlas){
const cards=qa('.ed-atlas-grid>.ed-style',atlas), group=q('#style-group'), find=q('#style-find'), count=q('#style-count');
function filter(){let n=0;cards.forEach(c=>{const match=(!group.value||c.dataset.group===group.value)&&c.textContent.toLowerCase().includes(find.value.toLowerCase().trim());c.hidden=!match;if(match)n++});count.textContent=n+' / '+cards.length;q('#style-empty').hidden=n>0;}
group.addEventListener('change',filter);find.addEventListener('input',filter);
document.addEventListener('nk:reveal',()=>{group.value='';find.value='';filter()});
const compare=()=>{const box=q('#compare-result');box.innerHTML='';qa('.ed-compare select').forEach(sel=>{const card=document.getElementById(sel.value),d=document.createElement('div');const art=q('.ed-style-art',card).cloneNode(true);qa('[id]',art).forEach(e=>e.removeAttribute('id'));d.append(art);const h=document.createElement('h4');h.textContent=q('h3',card).textContent;d.append(h);const p=document.createElement('p');p.textContent=q('.ed-idea',card).textContent;d.append(p);box.append(d)})};
qa('.ed-compare select').forEach(s=>s.addEventListener('change',compare));compare();
const sliders=qa('.ed-dial input'),live=q('#style-live'),key='mtrx-design-style-dials-v1';
const defaults=[20,76,15,35,70,35,35,35];
try{const vals=JSON.parse(localStorage.getItem(key)||'null');if(Array.isArray(vals)&&vals.length===8)sliders.forEach((s,i)=>s.value=Math.max(0,Math.min(100,Number(vals[i])||0)))}catch(e){}
function paint(){const v=sliders.map(s=>+s.value);sliders.forEach(s=>q('output',s.parentElement).textContent=s.value);try{localStorage.setItem(key,JSON.stringify(v))}catch(e){}
live.style.background=`hsl(${40+v[3]*1.5} ${12+v[7]/5}% ${93-v[0]/12}%)`;
live.style.padding=(35-v[0]/5)+'px';
q('h4',live).style.fontSize=(28+v[1]*.45)+'px';q('h4',live).style.fontFamily=v[5]<45?'Georgia,serif':'Impact,sans-serif';
q('h4',live).style.transform=`rotate(${(v[2]-15)/20}deg)`;
q('h4',live).textContent=v[7]>60?'Go where curiosity takes you.':'A different way to see.';
q('img',live).style.borderRadius=(100-v[6])*.4+'px';q('img',live).style.filter=`saturate(${.35+v[7]/60})`;
live.style.borderWidth=v[4]<35?'3px':'1px';live.style.boxShadow=v[4]>70?'0 12px 25px #0001':'none';
q('.live-extra',live).style.display=v[0]>50?'block':'none';q('p',live).style.display=v[0]<15?'none':'block';
q('footer',live).textContent=`Density ${v[0]} / Volume ${v[1]} / ${v[1]>65&&v[0]<35?'Minimal AND bold':v[0]>65?'Layered composition':'Balanced composition'}`;
}
sliders.forEach(s=>s.addEventListener('input',paint));
qa('[data-preset]').forEach(b=>b.addEventListener('click',()=>{const presets={swiss:[15,90,0,55,80,60,95,20],memphis:[80,92,75,35,55,45,80,100],safari:[22,45,20,20,75,35,12,25],reset:defaults};sliders.forEach((s,i)=>s.value=presets[b.dataset.preset][i]);paint()}));paint();
}
const r=q('#ratio-choice');if(r){const update=()=>{const ratio=+r.value,a=ratio/(1+ratio)*100,b=100-a;q('#ratio-stage').style.gridTemplateColumns=a+'fr '+b+'fr';q('#ratio-major').textContent=a.toFixed(1)+'%';q('#ratio-minor').textContent=b.toFixed(1)+'%';qa('#ratio-scale>span').forEach((s,i)=>{let px=Math.round(16*Math.pow(ratio,i));s.style.fontSize=px+'px';q('small',s).textContent=px+'px'});q('#ratio-note').textContent=ratio===1.618?'Golden-ratio starting point. Test content fit, contrast and reading comfort.':'Alternative ratio. A coherent system does not require phi.'};r.addEventListener('change',update);update();}
})();
"""

def svg_visual(sid):
    """Original visual studies, deliberately not reproductions of named works."""
    bg, fg, accent = '#f2efe5','#171917','#e85f29'
    if sid in ('punk-diy','grunge','zine'): bg,fg,accent='#e8e5da','#171717','#db4729'
    if sid in ('quiet-luxury','editorial-luxury','quiet-luxury-clothing'): bg,fg,accent='#d9d2bf','#3e382a','#9e977e'
    if sid in ('retro-futurism','y2k','glassmorphism'): bg,fg,accent='#b6c8e7','#26225d','#b740d2'
    if sid in ('art-nouveau','victorian','dark-academia'): bg,fg,accent='#293c32','#efe5cc','#a9a77b'
    body=''
    def text(x,y,t,size=30,fill=None,font='Arial',weight=700,extra=''):
        return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" fill="{fill or fg}" {extra}>{E(t)}</text>'
    def rect(x,y,w,h,c,more=''):
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}" {more}/>'
    def circle(x,y,r,c,more=''):
        return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {more}/>'
    if sid=='swiss-international':
        body=rect(35,40,115,200,accent)+circle(270,135,85,fg)+text(35,285,'form / field',48)+text(35,330,'ORDER IS A CHOICE',15)
        body+=''.join(f'<path d="M{x} 28V370" stroke="#17201c" opacity=".15"/>' for x in range(35,590,55))
        body+=text(360,215,'07',110)+text(360,258,'SEE',30)+text(360,290,'CLEARLY.',30)
    elif sid=='bauhaus':
        body=circle(195,168,100,'#e5ac2e')+rect(270,70,160,160,'#244c90')+f'<path d="M245 290L440 340L380 140Z" fill="#bc322a"/>'
        body+=text(35,365,'form + material + making',26)
    elif sid=='mid-century-modern':
        body=rect(0,285,600,115,'#bc6435')+f'<path d="M140 190Q190 30 290 175L395 215Q320 285 165 245Z" fill="#8f502d"/><path d="M180 245L155 335M350 245L405 335" stroke="#222" stroke-width="12"/>'
        body+=circle(475,85,40,'#d4b546')+text(35,52,'EVERYDAY / MODERN',21)
    elif sid in ('japandi','organic-biophilic'):
        body=rect(60,65,480,270,'#dcd9c6')+f'<path d="M110 320Q35 120 210 83Q450 -10 515 205Q450 365 260 300Z" fill="#738365"/>'
        body+=f'<path d="M75 305Q170 210 340 205T540 80" fill="none" stroke="#f4f0db" stroke-width="4"/>'
        body+=rect(275,240,140,14,'#b28d58')+rect(292,250,8,95,'#775e3c')+rect(391,250,8,95,'#775e3c')+text(35,48,'SPACE TO BREATHE',23)
    elif sid in ('editorial-luxury','quiet-luxury'):
        body=rect(355,40,210,290,'#b6ad96')+f'<path d="M390 270Q360 180 428 95Q490 30 510 180Q530 270 470 280Z" fill="#7d8068"/>'
        body+=text(35,123,'The art',55,font='Georgia',weight=400)+text(35,185,'of less.',55,font='Georgia',weight=400)+text(35,325,'MATERIAL. SPACE. RESTRAINT.',17)
    elif sid=='neo-brutalist-web':
        body=rect(42,48,515,300,fg)+rect(30,35,515,300,'#ddec50',f'stroke="{fg}" stroke-width="4"')
        body+=text(55,100,'NOT A SOFT',48)+text(55,160,'IMPRESSION.',48)+rect(62,218,290,64,fg)+rect(53,209,290,64,'#f6e5ef',f'stroke="{fg}" stroke-width="3"')+text(70,250,'PRESS HERE  →',28)
    elif sid=='maximalism':
        bg='#522f57'
        body=''.join(circle(x,y,20,'#9c5d77') for x in range(20,600,55) for y in range(20,400,55))
        body+=rect(50,45,210,270,'#b49a4a')+rect(62,57,186,246,'#1e5c4d')+circle(155,160,64,'#dd6634')+rect(305,78,215,235,'#dfc987')+text(330,150,'MORE',36)+text(330,195,'IS A',36)+text(330,240,'CHOICE.',36)+text(65,367,'LAYER / REPEAT / CONNECT',23,'#f3d3a3')
    elif sid=='pop-art':
        bg='#f2d53e'
        body=''.join(circle(x,y,3.5,'#2a3d90') for x in range(10,600,14) for y in range(10,400,14))
        body+=f'<path d="M70 80L350 40L540 170L470 280L270 300L200 365L190 298L60 260Z" fill="#f7efdb" stroke="#202023" stroke-width="8"/>'
        body+=text(140,223,'LOOK!',100,'#df3d33',extra='transform="rotate(-6 200 200)"')
    elif sid=='psychedelic':
        bg='#f59a4f'
        for i,c in enumerate(['#c92965','#5a3794','#e4cc4b','#c92965','#54469e','#e5a448','#df4667']):
            body+=f'<ellipse cx="300" cy="200" rx="{280-i*32}" ry="{180-i*21}" fill="{c}" transform="rotate({i*9} 300 200)"/>'
        body+=text(185,218,'SHIFT',64,'#f8ecb8',font='Georgia',extra='transform="rotate(-8 300 200)"')
    elif sid in ('punk-diy','zine','grunge'):
        body=rect(30,30,540,340,'#d4d0bf')
        for i,(word,y) in enumerate([('MAKE',120),('YOUR',215),('OWN.',310)]):
            body+=f'<g transform="rotate({[-6,4,-2][i]} 300 {y})">'+rect(50+i*18,y-68,410,82,fg if i!=1 else accent)+text(70+i*18,y,word,82,'#f1ede1',font='Georgia' if sid=='zine' else 'Arial')+'</g>'
        if sid=='grunge':
            body+=''.join(f'<path d="M{(i*53)%600} {(i*37)%400}l120 -8" stroke="{bg}" stroke-width="{1+i%3}"/>' for i in range(65))
        body+=text(460,365,'DIY',22)
    elif sid in ('art-nouveau','victorian'):
        body=rect(25,25,550,350,'none',f'stroke="{fg}" stroke-width="2"')+rect(36,36,528,328,'none',f'stroke="{accent}"')
        for x,sgn in [(90,1),(510,-1)]:
            body+=f'<path d="M{x} 355C{x+110*sgn} 230 {x-90*sgn} 180 {x+30*sgn} 70S{x+135*sgn} 210 {x+45*sgn} 190" fill="none" stroke="{accent}" stroke-width="6"/>'
            body+=f'<ellipse cx="{x+30*sgn}" cy="90" rx="25" ry="55" fill="{accent}" transform="rotate({40*sgn} {x+30*sgn} 90)"/>'
        body+=text(300,178,'FIELD',55,font='Georgia',weight=400,extra='text-anchor="middle"')+text(300,237,'NOTES',55,font='Georgia',weight=400,extra='text-anchor="middle"')
        if sid=='victorian': body+=text(300,302,'A CABINET OF CURIOSITIES',16,extra='text-anchor="middle"')
    elif sid in ('retro-futurism','y2k'):
        body=circle(430,100,70,'#eee2d9')+f'<path d="M0 300L140 240L245 295L400 190L600 285V400H0Z" fill="#4a508a"/>'
        if sid=='retro-futurism':
            body+=f'<ellipse cx="285" cy="195" rx="145" ry="40" fill="#c7a66f"/><path d="M220 185Q285 80 350 185Z" fill="#e0e5da"/>'+text(35,65,'TOMORROW, THEN.',30)
        else:
            body+=f'<ellipse cx="295" cy="190" rx="210" ry="65" fill="none" stroke="#f1eef9" stroke-width="15" transform="rotate(-25 295 190)"/>'+text(90,240,'NEW ERA',75,'#f5f4ff',extra='font-style="italic"')
    elif sid=='critical-regionalism':
        bg='#ddcdb0'
        body=rect(55,120,490,210,'#ae7b53')+rect(80,165,90,165,'#3d4f40')+rect(210,165,90,165,'#3d4f40')+rect(340,165,90,165,'#3d4f40')
        body+=f'<path d="M50 120Q140 0 225 120Q310 0 395 120Q480 0 550 120" fill="#e8e3d2" stroke="#8b735a" stroke-width="3"/>'
        body+=text(50,365,'SHADE / AIR / MATERIAL / PLACE',22)+f'<path d="M95 230H430m-20 -10l20 10l-20 10" stroke="#e2d98e" stroke-width="4" fill="none"/>'
    elif sid in ('skeuomorphic','flat-design','glassmorphism'):
        bg='#b1c1d6' if sid=='glassmorphism' else '#d4dadb'
        body=circle(460,110,125,'#9c7dc7')+circle(140,285,140,'#62b2ad') if sid=='glassmorphism' else ''
        if sid=='skeuomorphic':
            body=rect(60,50,480,300,'#4b4032', 'rx="18"')+rect(77,72,445,255,'#cabe9c', 'rx="10"')+rect(95,90,410,43,'#775b3b')+text(120,120,'STUDIO NOTEBOOK',24,'#f0e5c8')
            body+=''.join(f'<path d="M105 {y}H495" stroke="#8c8571"/>' for y in range(165,310,30))
            body+=f'<path d="M135 145V310" stroke="#a95e52" stroke-width="2"/>'
        elif sid=='flat-design':
            body=rect(65,55,470,290,'#faf7ef')+rect(65,55,470,63,'#326ba0')+text(88,97,'STUDIO NOTES',26,'#fff')+rect(90,155,75,75,'#e8b941')+rect(190,155,75,75,'#d3604e')+rect(290,155,215,16,'#b3b5ad')+rect(290,190,180,16,'#b3b5ad')+rect(90,270,410,35,'#326ba0')
        else:
            body+=rect(70,65,465,270,'#fff','opacity=".48" rx="25" stroke="#fff" stroke-width="2"')+text(110,145,'A lighter layer.',37)+rect(110,180,350,14,'#fff','opacity=".7"')+rect(110,218,240,14,'#fff','opacity=".7"')+rect(110,268,150,34,'#fff','opacity=".7" rx="12"')
    elif sid in ('quiet-luxury-clothing','streetwear','dark-academia','workwear'):
        palette={'quiet-luxury-clothing':('#c9c0aa','#726756'),'streetwear':('#db7844','#28576a'),'dark-academia':('#77644f','#332a22'),'workwear':('#aa7845','#4d5d65')}
        a,b=palette[sid]
        body=f'<path d="M215 72L160 110L105 245L165 265L195 195L195 345H405V195L435 265L495 245L440 110L385 72L345 100H255Z" fill="{a}" stroke="{b}" stroke-width="4"/>'
        body+=f'<path d="M255 100L300 170L345 100M300 170V345" fill="none" stroke="{b}" stroke-width="5"/>'
        if sid in ('workwear','streetwear'): body+=rect(215,200,65,75,b)+rect(320,200,65,75,b)
        if sid=='dark-academia': body+=''.join(f'<path d="M195 {y}H405" stroke="#c2a47b" opacity=".3"/>' for y in range(185,345,16))
        body+=text(35,45,{'quiet-luxury-clothing':'CUT BEFORE LOGO','streetwear':'SILHOUETTE + COMMUNITY','dark-academia':'HERITAGE, RECOMPOSED','workwear':'FUNCTION LEAVES A SHAPE'}[sid],22)
    else:
        body=rect(65,50,470,300,'#e6dfcb')+circle(300,200,110,accent)+text(70,365,'FORM / MATERIAL / INTENTION',23)
    return f'<svg viewBox="0 0 600 400" role="img" aria-label="{E(sid.replace("-"," "))}: original schematic style study" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="{bg}"/>{body}</svg>'

def visual(row, photos):
    sid=row['id']
    if sid in photos:
        im=f'<img src="{photos[sid]}" alt="AI-generated fictional material and spatial study for {E(row["name"])}" loading="lazy" width="450" height="300">'
        cap='AI illustration / fictional study'
    else:
        im=svg_visual(sid);cap='Original schematic study'
    return '<figure class="ed-style-art">'+im+'<figcaption>'+cap+'</figcaption></figure>'

def atlas_html(data):
    rows=data['styles'];photos=data['photos'];groups=list(dict.fromkeys(x['group'] for x in rows))
    dials=[('Density','minimal','maximal',20),('Volume','quiet','loud',76),('Structure','ordered','expressive',15),('Temperature','warm','cool',35),('Finish','raw','polished',70),('Era','vintage','futuristic',35),('Source','natural','synthetic',35),('Mood','serious','playful',35)]
    controls=''.join(f'<div class="ed-dial"><label for="dial-{i}">{name}<output>{v}</output></label><input id="dial-{i}" type="range" min="0" max="100" value="{v}" aria-label="{name}: {a} to {b}"><small><span>{a}</span><span>{b}</span></small></div>' for i,(name,a,b,v) in enumerate(dials))
    cards=[]
    for i,r in enumerate(rows):
        sources=''.join(f'<a href="{E(s["url"],quote=True)}" target="_blank" rel="noopener">{E(s["title"])}</a>' for s in r['sources'])
        cards.append(f'''<div class="ed-style" id="style-{r['id']}" data-group="{E(r['group'])}">
        {visual(r,photos)}<div class="ed-style-meta">{i+1:02d} / {E(r['group'])} / {E(r['kind'])}</div><h3>{E(r['name'])}</h3>
        <ul class="ed-cues">{''.join('<li>'+E(c)+'</li>' for c in r['cues'])}</ul>
        <p class="ed-idea">{E(r['idea'])}</p><details><summary>Look closer: example, use, limit + sources</summary>
        <p><b>Study next.</b> {E(r['example'])}</p><p><b>Try it for.</b> {E(r['use'])}</p><p><b>Do not confuse it with.</b> {E(r['trap'])}</p>
        <div class="ed-source">{sources}</div></details></div>''')
    options=''.join(f'<option value="style-{r["id"]}">{E(r["name"])}</option>' for r in rows)
    compare2=options.replace('value="style-memphis"','selected value="style-memphis"')
    quiz=[
      dict(q='One poster has two elements: one enormous word and one photograph. Which description fits?',o=['High density, because large letters take up substantial space.','Low density and high volume, because few elements speak loudly.','Low density and low volume, because there are only two elements.'],a=1,w='Density counts the amount and layering of information. Volume describes emphasis. Minimal and bold can coexist.'),
      dict(q='A safari brand wants curiosity and energy rather than quiet luxury. What should guide its style?',o=['Use the same warm beige palette as other lodges to signal category membership.','Choose the most expressive option regardless of reading comfort or trust.','Match audience, offer and tone, then test a coherent direction with real content.'],a=2,w='Quiet, warm and natural is one possible direction, not a wildlife-industry law. An expedition, research project and luxury lodge may need different signals.'),
      dict(q='Which is the strongest starting point for a critical-regionalist building study?',o=['Observe shade, airflow, terrain, materials and how people occupy the site.','Collect regional motifs and repeat them across an otherwise standard facade.','Copy the silhouette of a famous building and replace its finishes with local ones.'],a=0,w='Place is not a surface decoration. Climate, construction, terrain and lived culture shape the decisions.')]
    checks=''.join('<div class="check"><script type="application/json">'+json.dumps(x,ensure_ascii=False)+'</script></div>' for x in quiz)
    courtyard=photos['bawa-tropical-modernism']
    return f'''<article class="mod ed-atlas" id="m6-3" data-mod="6.3">
    <div id="style-atlas"></div><div class="mod-meta">6.3 / Visual style atlas / browse any time</div>
    <h2 class="mod-title">More than minimal.<br>More than bold.</h2>
    <p class="ed-section-intro">A poster can be minimal and shout. A room can be full and quiet. The useful question is not “which style is best?” It is: <b>what is this design doing, and what choices make it happen?</b></p>
    <div class="predict"><div class="predict-k">Predict first</div><p>Two elements. One enormous red word. Almost nothing else. Is that minimal, bold, both or neither? Choose, then rate your confidence from 1 to 5.</p><details class="reveal"><summary>Reveal the distinction</summary><p>Both. Minimal describes low density. Bold describes high emphasis. They belong on different dials, so they are not opposites.</p></details></div>
    <h3>Eight dials, not two boxes</h3><p>Move one control at a time. The same small editorial composition changes while its message stays recognisable. These are exploratory directions, not objective scores for a style.</p>
    <div class="ed-presets"><button data-preset="swiss">Minimal + bold</button><button data-preset="memphis">Expressive + playful</button><button data-preset="safari">One wildlife direction</button><button data-preset="reset">Reset dials</button></div>
    <div class="ed-dial-lab"><div class="ed-dials">{controls}</div><div class="ed-live" id="style-live"><div class="live-head"><span>FIELD / STUDIO</span><span>No. 07</span></div><h4>A different way to see.</h4><img src="{courtyard}" alt="AI-generated fictional tropical courtyard" width="450" height="300"><p>Observe the space. Notice the light. Make one deliberate choice.</p><div class="live-extra"><span>01 / The place</span><span>02 / The material</span><span>03 / The experience</span></div><footer>Density and volume are independent.</footer></div></div>
    <p class="ed-dial-note">Teaching heuristic, not a validated taxonomy. Real designs mix these qualities, and culture changes their meaning. The live example exaggerates changes so you can see them; it does not automatically produce an authentic historical style.</p>
    <h3>Compare before you name</h3><p>Look for relationships, not just colours. Compare the same kind of decision across two approaches, then explain what each one makes easier or harder.</p>
    <div class="ed-compare"><div class="ed-compare-fields"><label>First approach<select aria-label="First style to compare">{options}</select></label><label>Second approach<select aria-label="Second style to compare">{compare2}</select></label></div><div class="ed-compare-result" id="compare-result" aria-live="polite"></div></div>
    <h3>The atlas / 34 entries / 10 families</h3><p>Every entry has a visual, three recognition cues, the idea underneath, a named example and a boundary. Some entries are movements; some are traditions, cultural ideas, interface effects or loose contemporary labels. They are not interchangeable kinds of thing.</p>
    <div class="ed-filter"><label>Find a style<input id="style-find" type="search" placeholder="Try Bauhaus, material, clothing..." autocomplete="off"></label><label>Browse a family<select id="style-group"><option value="">All 10 families</option>{''.join('<option>'+E(g)+'</option>' for g in groups)}</select></label><output id="style-count" aria-live="polite">34 / 34</output></div>
    <div class="ed-atlas-grid">{''.join(cards)}</div><p class="ed-noresults" id="style-empty" hidden>No match. Try another word or choose all families.</p>
    <div class="ed-coverage"><h3>What this atlas covers</h3><p>All 34 requested entries are present across Order, Quiet nature, Luxury, Raw, Loud, Rebel, Time travel, Place, Screens and Clothing. Quiet luxury appears twice because a spatial/graphic direction and a clothing code are related but different applications.</p><p>Original schematic studies and clearly labelled AI illustrations teach visual cues. They are not reproductions of the named works, photographs of actual heritage sites, or evidence that a movement can be reduced to three traits. Follow each entry's sources for authentic examples.</p><p>This checks coverage of your requested list, not mastery, completeness of design history or a scientific classification of taste. Research checked 23 October 2026; contemporary labels remain contested and changeable.</p></div>
    <div class="mtrx"><p><b>Studio lens / MTRX™.</b> Quiet, ordered, warm, natural and polished can suit a high-end wildlife operator, with the photograph doing the loud work. It is a starting hypothesis, not a category rule. A field-research expedition, family safari and rebellious outdoor brand may need quite different voices.</p></div>
    <div class="tryit"><div class="tryit-k">Try it / 5 min</div><p>Choose a real safari page. Name its density and volume separately. Pick two families from this atlas and sketch the same heading, photo and booking link in each. Keep the content unchanged. Explain which audience each version serves better and which cue you deliberately refused to copy.</p></div>
    <details class="deeper"><summary>Go deeper / a three-session route</summary><p>Session 1: dials, Order, Quiet nature and Luxury. Session 2: Raw, Loud, Rebel and Time travel. Session 3: Place, Screens, Clothing and a cross-style brief. Spend 20 minutes each; the atlas is a reference shelf, not one cram session.</p></details>
    <p class="room">Style is a system of choices, not a bag of decorative effects.</p><button class="done" data-mod="6.3">Mark stop 6.3 seen</button></article>'''

def ratio_html():
    return '''<div class="ed-workbench" id="golden-lab"><div class="kicker">2.11 / application workbench</div><h3>Use the ratio.<br>Then judge the result.</h3>
    <p class="ed-section-intro">The golden ratio gives you a relationship, about 1 : 1.618. Try it as a starting proportion for a layout or a type scale, then compare alternatives using the same content.</p>
    <label for="ratio-choice">Choose a relationship</label><select id="ratio-choice" style="padding:10px;font-size:16px;margin:12px"><option value="1.618">1 : 1.618 / golden ratio</option><option value="1.5">1 : 1.5 / perfect fifth</option><option value="1.333">1 : 1.333 / perfect fourth</option></select>
    <div class="ed-ratio-stage" id="ratio-stage"><div><span>Primary field</span><strong id="ratio-major">61.8%</strong></div><div><span>Secondary field</span><strong id="ratio-minor">38.2%</strong></div></div>
    <div id="ratio-scale" class="ed-scale"><span>Aa<small>16px</small></span><span>Aa<small>26px</small></span><span>Aa<small>42px</small></span><span>Aa<small>68px</small></span></div>
    <p id="ratio-note" class="ed-dial-note">Golden-ratio starting point. Test content fit, contrast and reading comfort.</p>
    <p><b>Apply it:</b> divide an image/text composition, build a heading hierarchy from a 16px base, or derive a coordinated set of sizes. Fibonacci steps such as 8, 13, 21 and 34 approach this relationship; they are an optional spacing system, not a usability requirement.</p>
    <p><b>A documented architectural application:</b> Le Corbusier's Modulor combined human dimensions with the golden section and Fibonacci relationships. Study how it creates related sizes, while questioning whose body its standard represents. <a href="https://www.fondationlecorbusier.fr/en/thematic-folder/corbusean-vocabulary/" target="_blank" rel="noopener">Fondation Le Corbusier: Modulor</a>.</p>
    <div class="tryit"><div class="tryit-k">Try it / 5 min</div><p>Sketch one hero at 62/38 and again at 50/50. Use the same image and words. Then compare 16/26/42px with 16/24/36px type. Choose the version that fits the content, and explain why.</p></div>
    <details><summary>A small boundary, not the whole lesson</summary><p>A deliberate proportional system is useful even without being a universal law of beauty. Do not infer an artist's intention merely because an overlay can be made to fit. Stop 2.11 above covers the history and the honest limits; this is the working tool.</p></details></div>'''

def apply(out, root):
    data=json.loads((HERE/'editorial-data.json').read_text())
    soup=BeautifulSoup(out,'html.parser')
    fontcss='@font-face{font-family:"MTRX Narrow";src:url('+data['font']+') format("woff2");font-weight:400 900;font-display:swap;}' if data.get('font') else ''
    style=soup.new_tag('style',id='mtrx-editorial-css');style.string=fontcss+CSS;soup.head.append(style)
    def fragment(x): return BeautifulSoup(x,'html.parser')
    # Persistent navigation and tools remain the original, proven reader.
    mast=fragment('<div class="ed-mast"><a class="ed-brand" href="#top">MTRX™</a><span class="ed-label">FIELD SERIES / DESIGN &amp; TASTE / 07</span><a href="#m6-3">Style atlas ↗</a></div>')
    soup.body.insert(0,mast)
    painting=soup.select_one('#m1-4 .plate-img img') or soup.select_one('.plate-img img')
    art=painting.get('src','') if painting else ''
    old=soup.select_one('header.cover')
    nstops=len({b.get('data-mod') for b in soup.select('button.done')})+(0 if soup.select_one('button.done[data-mod="6.3"]') else 1)
    cover=f'''<header class="wrap cover" id="top" data-sec="0"><div class="ed-cover-top"><span>FIELD SERIES / NO. 07</span><span>A visual education</span></div>
    <div class="ed-cover-grid"><div><span class="ed-issue">07</span><h1 class="cover-title">Design<br>&amp; taste.</h1><p class="cover-sub">Learn the principles.<br>Read the choices.<br>Develop an eye of your own.</p></div><figure class="ed-cover-image"><img src="{art}" alt="Wassily Kandinsky, Composition VIII, 1923: an authentic study in point, line and plane" width="1100" height="770"><div class="ed-paper-note">Not one look.<br>A way of seeing.</div><figcaption>PLATE 01 / Kandinsky, Composition VIII, 1923.<br>Public-domain artwork via Wikimedia Commons. Full credit in Stop 1.4.</figcaption></figure></div>
    <div class="ed-cover-foot"><p>Prepared for Kevin Cecil / MTRX™<br>{nstops} stops / 10 parts / browse at your own pace<br>Part 1 in depth, Parts 2 to 9 as visual stops / 27 October 2026</p><div class="ed-actions"><a href="#m0-1">Begin the guide ↓</a><a href="#m6-3">Explore the style atlas ↗</a></div></div>
    <div class="ed-strip"><b>THIS EDITION</b><p>Part 1 teaches the eye in depth, with checks. Parts 2 to 9 are visual stops for occasional visits: real works to look at, what to steal, a director\u2019s eye and a studio lens. Plus a 34-entry style atlas, eight dials and a proportion workbench.</p></div></header>'''
    old.replace_with(fragment(cover))
    # Preserve questions but correct the two rejected framings everywhere.
    swaps={
      'Is the golden ratio real? And the rule of thirds?':'How do designers apply the golden ratio and rule of thirds?',
      'Are the golden ratio and rule of thirds really laws?':'How do designers actually use the golden ratio?',
      'Minimal or bold: which is better?':'Which visual styles can I use, and how do they differ?',
      'Less is more, or less is a bore?':'More than minimal vs bold: the visual style atlas',
      'Composition, with the truth about the golden ratio and the rule of thirds. Minimal versus bold.':'Composition, with applications of the golden ratio and rule of thirds. A visual atlas of styles beyond minimal versus bold.'
    }
    for node in list(soup.find_all(string=True)):
        if node.parent.name in ('script','style'):continue
        new=str(node)
        for a,b in swaps.items():new=new.replace(a,b)
        if new!=str(node):node.replace_with(new)
    wrap=soup.select_one('#s6>.wrap')
    nxt=soup.select_one('#m6-4')
    if nxt:nxt.insert_before(fragment(atlas_html(data)))
    else:wrap.append(fragment(atlas_html(data)))
    later=wrap.select_one('.later')
    if later:later.clear();later.append('The visual atlas (6.3) is available early below. The other Part 6 lessons remain planned.')
    for a in soup.select('#s6 .stops a'):
        if a.select_one('span') and a.select_one('span').text=='6.3':
            a['href']='#m6-3'
            a.select_one('em').string='atlas'
    gr=soup.select_one('#m2-11')
    if gr:gr.insert_after(fragment(ratio_html()))
    else:soup.select_one('#s2>.wrap').append(fragment(ratio_html()))
    # Variable-strength controls; blur is no longer overridden by the inherited entrance effect.
    for i,p in enumerate(soup.select('.plate')):
        img=p.select_one('.plate-img img')
        if not img:continue
        for b in p.select('.sq'):b.decompose()
        holder=p.select_one('.plate-img')
        holder.append(fragment('<svg class="ed-overlay" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"><path d="M33.333 0V100M66.667 0V100M0 33.333H100M0 66.667H100" stroke="#ed691d" stroke-width=".35" fill="none"/></svg>'))
        control=f'''<div class="ed-lab-controls"><label for="squint-{i}">Squint <input class="ed-squint" id="squint-{i}" type="range" min="0" max="12" step=".5" value="0"><output>0px</output></label><button class="ed-mono" aria-pressed="false" type="button">Grayscale</button><button class="ed-guides" aria-pressed="false" type="button">Thirds grid</button><button class="ed-reset" type="button">Reset</button></div><p class="ed-lab-note">Study tools: blur suppresses detail; grayscale removes hue, not light. The grid is a comparison aid, not evidence of the artist's intent.</p>'''
        holder.insert_after(fragment(control))
    js=soup.new_tag('script',id='mtrx-editorial-js');js.string=JS;soup.body.append(js)
    result=str(soup)
    # The library lint requires the shared review loader last. The download packager
    # inlines the same engine separately; both editions preserve its storage keys.
    result=re.sub(r'<script\b[^>]*src="\.\./assets/mtrx-review\.js"[^>]*>\s*</script>', '', result)
    before, after=result.rsplit('</body>',1)
    result=before+'<script src="../assets/mtrx-review.js" defer></script>\n</body>'+after
    # Keep the library indexer's established serialized tag order.
    result=re.sub(r'<section ([^>]*\bclass="part"[^>]*)>',lambda m: reorder_section(m.group(1)),result)
    return result

def reorder_section(attrs):
    d=dict(re.findall(r'([\w-]+)="([^"]*)"',attrs))
    order=['class','id','data-part','data-sec','data-title']
    return '<section '+' '.join(f'{k}="{d[k]}"' for k in order if k in d)+'>'

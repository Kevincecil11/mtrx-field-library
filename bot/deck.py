"""MTRX review deck: build one Telegram HTML widget (Bot API 10.4) from bot/questions cards.

Stdlib only, like bot/bot.py. The widget does all grading on the device (no network, no bot round trip),
keeps progress in its per-message localStorage, and hands results back through a t.me deep link
(/start w<deck>_<grades>), which the bot reads like any other message.
Limits checked here: 32768 bytes of HTML, 4096 bytes after zlib level 9 (as the server counts).
"""
import json, zlib

BOT = 'makingmesmart_bot'                     # bot.py overrides BOT and SITE at import
SITE = 'https://kevincecil11.github.io/mtrx-field-library/'
MAX_RAW, MAX_ZIP, TARGET_ZIP = 32768, 4096, 3900
WHY_MAX = 260

# Presentation layer: MTRX look on top of Telegram's theme variables (kept apart from the logic below).
THEME = ('<style>body{margin:0;padding:12px 14px 10px}'
         ':root{--mx:#ED691D;--ok:#2e9d5b;--no:var(--tg-theme-destructive-text-color,#d64545)}'
         '.t{font:600 12px/1.3 ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase;color:var(--tg-theme-hint-color)}'
         '.t b{color:var(--mx);font-weight:700}.bar{height:3px;border-radius:2px;background:var(--tg-theme-secondary-bg-color);margin:8px 0 10px}'
         '.bar i{display:block;height:3px;border-radius:2px;background:var(--mx)}'
         '.q{font-weight:600;margin:0 0 10px}.c{display:flex;gap:6px;margin:0 0 8px}'
         '.c button{flex:1;padding:5px 0;border-radius:8px;font:600 12px ui-monospace,monospace;background:var(--tg-theme-secondary-bg-color);color:var(--tg-theme-text-color)}'
         '.c .on{background:var(--mx);color:#fff}'
         '.o{display:block;width:100%;text-align:left;margin:0 0 6px;padding:9px 11px;border-radius:10px;border:1px solid var(--tg-theme-section-separator-color,rgba(128,128,128,.3));'
         'background:transparent;color:var(--tg-theme-text-color);font:inherit;line-height:1.3}'
         '.o.y{border-color:var(--ok);background:rgba(46,157,91,.14)}.o.n{border-color:var(--no);background:rgba(214,69,69,.12)}'
         '.w{font-size:14px;margin:6px 0 10px;padding:8px 10px;border-left:3px solid var(--mx);background:var(--tg-theme-secondary-bg-color);border-radius:0 8px 8px 0}'
         '.row{display:flex;gap:6px}.row button{flex:1}.h{color:var(--tg-theme-hint-color);font-size:13px;margin:8px 0 0}'
         '.o b{color:var(--mx);font-family:ui-monospace,monospace}.s{margin:6px 0 10px}.big{font:700 34px/1 ui-monospace,monospace;color:var(--mx);margin:6px 0}</style>')

# Logic layer. D: [tag, kind 'q'|'r', question, options|null, answer index|answer text, why|label, link]
LOGIC = r'''<div id="a"></div><script>
const W=window.TelegramWidget,$=document.getElementById.bind(document),K='mx1';
let S={i:0,r:[],c:1};try{S=JSON.parse(localStorage.getItem(K))||S}catch(e){}
const sv=()=>{try{localStorage.setItem(K,JSON.stringify(S))}catch(e){}},hp=t=>{try{W&&W.HapticFeedback.notificationOccurred(t)}catch(e){}};
function el(t,c,h){const e=document.createElement(t);if(c)e.className=c;if(h!=null)e.textContent=h;return e}
function head(n){const d=el('div');const t=el('div','t');t.innerHTML='<b>'+(n<D.length?D[n][0]:'Done')+'</b> · '+Math.min(n+1,D.length)+' / '+D.length;
const b=el('div','bar'),i=el('i');i.style.width=(n/D.length*100)+'%';b.append(i);d.append(t,b);return d}
function conf(){const c=el('div','c');['Guess','Unsure','Sure'].forEach((x,k)=>{const b=el('button',k==S.c?'on':'',x);b.onclick=()=>{S.c=k;draw()};c.append(b)});return c}
function next(res){S.r[S.i]=res*3+S.c;S.i++;S.c=1;S.p=null;sv();draw()}
function draw(){const a=$('a');a.replaceChildren(head(S.i));if(S.i>=D.length)return end(a);
const d=D[S.i];a.append(el('p','q',d[2]));
if(d[1]=='q'){const p=S.p;if(p==null)a.append(conf());
d[3].forEach((o,k)=>{const b=el('button','o'),l=el('b','',String.fromCharCode(65+k)+'  ');b.append(l,o);
if(p!=null){if(k==d[4])b.className+=' y';else if(k==p)b.className+=' n'}else b.onclick=()=>{S.p=k;sv();hp(k==d[4]?'success':'error');draw()};a.append(b)});
if(p!=null){a.append(el('div','w',(p==d[4]?'Right. ':'Not quite. ')+d[5]));const n=el('button','',S.i+1<D.length?'Next':'Finish');n.onclick=()=>next(p==d[4]?0:2);a.append(n)}}
else{if(S.p==null){a.append(conf(),el('p','h','Say it out loud first.'));const b=el('button','','Reveal');b.onclick=()=>{S.p=1;sv();draw()};a.append(b)}
else{a.append(el('div','w',d[4]));const r=el('div','row');['Got it','Partly','Missed'].forEach((x,k)=>{const b=el('button','',x);b.onclick=()=>{hp(k?'warning':'success');next(k)};r.append(b)});a.append(r)}}}
function end(a){const g=S.r.filter(x=>x<3).length,m=[];S.r.forEach((x,k)=>{if(x>=6)m.push(k)});
a.append(el('div','big',g+' / '+D.length),el('p','h',m.length?m.length+' to revisit. Send results so the bot can reschedule them.':'Clean sheet. Send results to log it.'));
const s=el('button','s','Send results to the bot');s.onclick=()=>{if(!W)return;try{W.openTelegramLink('https://t.me/'+B+'?start=w'+I+'_'+S.r.map(x=>'abcdefghi'[x]).join(''));s.textContent='Sent'}catch(e){s.textContent='Could not open the bot'}};a.append(s);
[...new Map(m.map(k=>[D[k][6],k])).values()].slice(0,3).forEach(k=>{const b=el('button','o','Re-read: '+D[k][0]);b.onclick=()=>{try{W&&W.openLink(L+D[k][6])}catch(e){}};a.append(b)});
const f=el('p','h','MTRX™ Field Library');a.append(f)}
draw();W&&W.ready&&W.ready();
</script>'''


def pack(c):
    tag = 'No. %s · %s %s' % (c['guide'], 'Day' if '#d' in c['link'] else 'Stop', c['stop'])
    link = c['link'].replace('guides/', '')
    if c['type'] == 'quiz':
        why = c.get('why') or 'Re-read the stop for the reasoning.'
        if len(why) > WHY_MAX:
            why = why[:WHY_MAX - 4].rsplit(' ', 1)[0] + ' ...'
        return [tag, 'q', c['q'], c['options'], c['answer'], why, link]
    return [tag, 'r', c['q'], None, c['answer'], c.get('label') or 'Recall', link]


def html_for(cards, deck_id):
    data = json.dumps([pack(c) for c in cards], ensure_ascii=False, separators=(',', ':'))
    head = '<script>const D=%s,I=%s,B=%s,L=%s</script>' % (data, json.dumps(deck_id), json.dumps(BOT), json.dumps(SITE + 'guides/'))
    return THEME + head + LOGIC


def size(html):
    raw = html.encode('utf-8')
    return len(raw), len(zlib.compress(raw, 9))


def build_decks(cards, deck_prefix):
    """Greedy split: as many cards per widget as fit under TARGET_ZIP. Returns [(deck_id, cards, html)]."""
    decks, cur = [], []
    for c in cards:
        trial = cur + [c]
        raw, z = size(html_for(trial, '%s%d' % (deck_prefix, len(decks))))
        if cur and (z > TARGET_ZIP or raw > MAX_RAW or len(trial) > 21):
            did = '%s%d' % (deck_prefix, len(decks))
            decks.append((did, cur, html_for(cur, did)))
            cur = [c]
        else:
            cur = trial
    if cur:
        did = '%s%d' % (deck_prefix, len(decks))
        decks.append((did, cur, html_for(cur, did)))
    return decks


def parse_result(payload):
    """'w<deck>_<grades>' -> (deck_id, [(result, confidence)]). result: got/partly/miss, confidence: guess/unsure/sure."""
    if not payload.startswith('w') or '_' not in payload:
        return None, []
    deck, _, g = payload[1:].partition('_')
    out = []
    for ch in g:
        k = 'abcdefghi'.find(ch)
        out.append(None if k < 0 else (('got', 'partly', 'miss')[k // 3], ('guess', 'unsure', 'sure')[k % 3]))
    return deck, out

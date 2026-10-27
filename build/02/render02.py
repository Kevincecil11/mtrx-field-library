"""No. 02 day renderer (port of the kit renderer used for Weeks 1 and 2).
Day records are plain dicts; see drafts/FORMAT-02.md. Stdlib only."""
import html, re

E = html.escape
FIELD = {'psy': ('Psychology', '3'), 'phi': ('Philosophy', '2')}
GRADE_BTNS = ('<div class="grade js-only"><button type="button" data-g="1">Got it</button>'
              '<button type="button" data-g="0">Missed it</button></div>')


def yt(i):
    return 'https://www.youtube.com/watch?v=%s' % i


def qa(id_, q, a, label='', grade=True):
    return ('<div class="qa" data-id="%s"><p class="q">%s%s</p><details class="ans"><summary>Show answer</summary>'
            '<div class="a">%s</div></details>%s</div>') % (id_, ('<small>%s</small>' % label) if label else '', q, a,
                                                             GRADE_BTNS if grade else '')


def review(n, f, recall, fields):
    """recall: {day: [(q_html, a_html), ...]} for every earlier day; fields: {day: 'psy'|'phi'}."""
    fname = FIELD[f][0].lower()
    items, order = {}, []

    def add(m, i, label, mode):
        k = (m, i)
        if k not in items:
            items[k] = [label, set()]
            order.append(k)
        items[k][1].add(mode)
    for k in (1, 3, 7):
        m = n - k
        if m >= 1 and m in recall:
            add(m, (n + k) % 3, 'Day %d \u00b7 %d day%s ago' % (m, k, 's' if k > 1 else ''), 'both')
    S = sorted(d for d, ff in fields.items() if ff == f)
    pos = S.index(n)
    words = {1: 'your last %s day' % fname, 2: 'two %s days back' % fname, 4: 'four %s days back' % fname}
    for j in (1, 2, 4):
        if pos - j >= 0 and S[pos - j] in recall:
            add(S[pos - j], (n + j) % 3, 'Day %d \u00b7 %s' % (S[pos - j], words[j]), f)
    out = ''
    for k in order:
        m, i = k
        label, modes = items[k]
        rq = recall[m]
        q, a = rq[i % len(rq)]
        out += '<div class="rv" data-rv="%s">' % ' '.join(sorted(modes)) + qa('d%dr%d' % (m, i % len(rq)), q, a, label) + '</div>'
    return out


def linkify(x):
    """Bare URLs in insider text become short numbered source links."""
    n = [0]

    def rep(m):
        n[0] += 1
        u = m.group(0).rstrip('.,;:')
        tail = m.group(0)[len(u):]
        return '<a href="%s" target="_blank" rel="noopener">source %d</a>%s' % (u, n[0], tail)
    parts = re.split(r'(<a\b[^>]*>.*?</a>)', x, flags=re.S)
    return ''.join(p if p.startswith('<a') else re.sub(r'https?://[^\s<]+', rep, p) for p in parts)


def fig(svg, cap):
    # The guide defines the arrowheads #ah and #ahm once, globally; drop local copies.
    svg = re.sub(r'<marker\b[^>]*\bid="ahm?"[^>]*>.*?</marker>', '', svg, flags=re.S)
    svg = re.sub(r'<defs>\s*</defs>', '', svg)
    return '<figure class="fig"><div class="scroll">%s</div><figcaption>%s</figcaption></figure>' % (svg, cap)


def day(d, ctx):
    """ctx: dict(recall, fields, img(key)->data uri or '', track(n)->(k, total), last, next_line, extra_html)."""
    n = d['n']
    fname, part = FIELD[d['f']]
    series, epn, vid, dur, eptitle = d['ep']
    mm, ss = dur.split(':')
    mins = int(mm) + (1 if int(ss) >= 30 else 0)
    bar = ('<div class="daybar" aria-hidden="true"><span style="--w:2"><b>Review</b>2 min</span><span style="--w:2"><b>Predict</b>2 min</span>'
           '<span class="w" style="--w:%d"><b>Watch</b>%s</span><span style="--w:3"><b>Insider</b>3 min</span><span style="--w:3"><b>Recall</b>3 min</span></div>') % (mins, dur)
    terms = ''.join('<div class="term"><b>%s</b>%s</div>' % (E(t), E(x)) for t, x in d['terms'])
    pre = ''.join(qa('d%dp%d' % (n, i), E(q), E(a), 'Guess first', grade=False) for i, (q, a) in enumerate(d['pre']))
    watch = ('<a class="watch" href="%s" target="_blank" rel="noopener"><div class="th"><span class="ph">%s #%s</span>'
             '<img src="https://i.ytimg.com/vi/%s/hqdefault.jpg" alt="" loading="lazy"><span class="play"></span></div><div>'
             '<div class="meta">%s \u00b7 #%s \u00b7 %s</div><h4>%s</h4><p>Opens on YouTube. Watch it straight through, then come back for the insider layer.</p></div></a>') % (
        yt(vid), E(series), epn, vid, E(series), epn, dur, E(eptitle))
    wf = ''.join('<li>%s</li>' % E(w) for w in d['watch'])
    ins = ''.join('<li>%s</li>' % linkify(x) for x in d['insider'])
    names = ''.join('<div><b>%s</b>%s</div>' % (E(a), E(b)) for a, b in d['names'])
    rec = ''.join(qa('d%dr%d' % (n, i), E(q), E(a)) for i, (q, a) in enumerate(d['recall']))
    eq, ea = d['explain']
    uq, ua = d['use']
    fur = ''.join('<a href="%s" target="_blank" rel="noopener"><b>%s</b><span>%s</span></a>' % (E(u, quote=True), E(t), E(m)) for t, u, m in d['further'])
    k, total = ctx['track'](n)
    src = ctx['img'](d['img'])
    plate = ('<div class="plate-img"><img src="%s" alt="%s" loading="lazy"><figcaption>%s</figcaption></div>' % (src, E(d.get('imgalt', ''), quote=True), E(d['imgcap']))
             if src else '<div class="plate-img plate-missing"><figcaption>%s</figcaption></div>' % E(d['imgcap']))
    tomorrow = ctx.get('next_line') or ('Tomorrow: Day %d. Same time, same cue.' % (n + 1) if n < ctx['last'] else '')
    return '''<article class="mod day" id="d{n}" data-mod="{n}" data-part="{part}" data-f="{f}">
<div class="mod-meta">Day {n} \u00b7 {fname} <span class="trk" data-trk="{f}">{fname} track \u00b7 {k} of {total}</span> <span class="t">about 20 min</span></div>
<h2 class="mod-title">{title}</h2>
<p class="mod-why">{hook}</p>
{bar}
<div class="step"><div class="step-k">1 \u00b7 Warm-up review \u00b7 2 min</div>{rv}</div>
<div class="step"><div class="step-k">2 \u00b7 Predict first \u00b7 2 min</div><p class="centralq">{q}</p>{pre}<p style="margin-top:14px"><b>Five words to know before you press play:</b></p><div class="terms">{terms}</div></div>
<div class="step"><div class="step-k">3 \u00b7 Watch \u00b7 {dur}</div>{watch}<p style="margin:14px 0 4px"><b>Watch for:</b></p><ul class="watchfor">{wf}</ul></div>
<div class="step"><div class="step-k">4 \u00b7 The insider layer \u00b7 3 min</div>
<div class="notes">{plate}<div><h4>What Crash Course doesn't tell you</h4><ul>{ins}</ul><div class="names">{names}</div></div></div>
{fig}
<p class="room">{room}</p></div>
<div class="step"><div class="step-k">5 \u00b7 Recall and use it \u00b7 3 min</div>
<div class="qa"><p class="q"><small>Explain it, video closed</small>{eq}</p><textarea class="explain" data-ex="d{n}" aria-label="Your 60-word explanation" placeholder="Type it here, from memory."></textarea><div class="wc js-only"></div><details class="ans"><summary>Compare with a model answer</summary><div class="a">{ea}</div></details></div>
{rec}
<div class="usecase"><p class="q">{uq}</p><details class="ans"><summary>Show a model answer</summary><div class="a">{ua}</div></details></div></div>
{extra}
<div class="step"><div class="step-k">Go further \u00b7 optional</div><div class="further">{fur}</div></div>
<p class="tomorrow">{tomorrow}</p>
<button class="done" data-mod="{n}">Mark day {n} done</button>
<span class="nojs-only muted" style="font-size:15px;margin-left:10px">(progress saves when you open the downloaded file)</span>
</article>'''.format(n=n, part=part, f=d['f'], fname=fname, k=k, total=total, title=E(d['title']), hook=E(d['hook']), bar=bar,
                     rv=review(n, d['f'], ctx['recall'], ctx['fields']), q=E(d['q']), pre=pre, terms=terms, dur=dur, watch=watch, wf=wf,
                     plate=plate, ins=ins, names=names, fig=fig(d['fig'], d['figcap']), room=E(d['room']), eq=E(eq), ea=E(ea), rec=rec,
                     uq=E(uq), ua=E(ua), extra=ctx.get('extra_html', ''), fur=fur, tomorrow=tomorrow)


def tieup(week, title, intro, rows, boss, calib):
    """Week tie-up block appended to the last day of a week."""
    trs = ''.join('<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>' % (E(a), E(b), E(c)) for a, b, c in rows)
    return ('<div class="step"><div class="step-k">Week %d tie-up \u00b7 %s</div><p>%s</p><div class="tbl-wrap"><table class="tbl"><thead><tr>'
            '<th>Day</th><th>The lesson</th><th>Say it in the room</th></tr></thead><tbody>%s</tbody></table></div>'
            '<div class="usecase"><p class="q">%s</p><details class="ans"><summary>Show a model answer</summary><div class="a">%s</div></details></div>'
            '<div class="qa"><p class="q"><small>Calibration</small>%s</p></div></div>') % (week, E(title), E(intro), trs, E(boss[0]), boss[1], E(calib))

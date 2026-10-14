"""Hand-built diagrams for No. 06 Part II, File 1 (one per stop). Plain SVG with
p2fig classes from p2.css; every marker id is unique in the guide."""


def _arrow(i, color='#151515'):
    m = ('<marker id="p2%s%s" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" '
         'markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker>')
    return '<defs>' + m % ('a', i, '#151515') + m % ('m', i, '#ED691D') + '</defs>'



def _svg(i, h, label, body, color='#151515'):
    return ('<svg class="p2fig" viewBox="0 0 1000 %d" role="img" aria-label="%s">%s%s</svg>'
            % (h, label, _arrow(i, color), body))


SVG = {}

SVG['2.1'] = _svg('21', 400, 'Two spotlights: pitch first puts the light on you; the spotlight move puts it on them', (
    '<text class="t" x="40" y="38">PITCH FIRST</text>'
    '<text class="t tm" x="540" y="38">THE SPOTLIGHT</text>'
    '<circle class="bk" cx="250" cy="70" r="16"/><circle class="bk" cx="750" cy="70" r="16"/>'
    '<polygon class="beam" points="238,80 262,80 440,250 60,250"/>'
    '<polygon class="beam" points="738,80 762,80 960,250 540,250"/>'
    '<rect class="bj" x="60" y="250" width="380" height="58" rx="10"/>'
    '<text class="tb" x="250" y="285" text-anchor="middle">YOU: services, stack, price</text>'
    '<rect class="bx" x="130" y="326" width="240" height="40" rx="8" style="stroke-dasharray:5 5"/>'
    '<text class="ts" x="250" y="351" text-anchor="middle">them: polite nodding</text>'
    '<rect class="bj" x="540" y="250" width="420" height="58" rx="10"/>'
    '<text class="tb" x="750" y="285" text-anchor="middle">THEM: their work, win, worry</text>'
    '<rect class="bx" x="610" y="326" width="280" height="40" rx="8"/>'
    '<text class="ts" x="750" y="351" text-anchor="middle">you: one question, one credit</text>'
    '<path class="lm mv" d="M455 160 L525 160" marker-end="url(#p2m21)"/>'
    '<text class="ts" x="490" y="146" text-anchor="middle">hand it over</text>'
    '<text class="ts" x="250" y="392" text-anchor="middle">They leave knowing your list.</text>'
    '<text class="ts" x="750" y="392" text-anchor="middle">They leave feeling interesting.</text>'
))

_names = [('1 HEAR IT', 'the first hear'), ('2 SAY IT BACK', '"Rhea? Hi, Rhea."'), ('3 LINK IT', 'a face, a friend'),
          ('4 WRITE IT', 'within the hour'), ('5 USE IT', 'once, at goodbye')]
_b = ''
for k, (a, b) in enumerate(_names):
    x = 31 + k * 192
    _b += ('<rect class="%s" x="%d" y="60" width="170" height="70" rx="12"/>'
           '<text class="t" x="%d" y="101" text-anchor="middle">%s</text>'
           '<text class="ts" x="%d" y="156" text-anchor="middle">%s</text>') % ('bj' if k else 'bx', x, x + 85, a, x + 85, b)
    if k < 4:
        _b += '<path class="ln" d="M%d 95 L%d 95" marker-end="url(#p2a22)"/>' % (x + 172, x + 190)
_b += ('<path class="lr" d="M31 186 L201 186"/><text class="ts tr" x="116" y="208" text-anchor="middle">most people stop here</text>'
       '<path class="lm mv" d="M884 60 C 884 18, 116 18, 116 56" marker-end="url(#p2m22)"/>'
       '<text class="ts tm" x="500" y="16" text-anchor="middle">next meeting: the callback (Stop 2.6)</text>'
       '<text class="ts" x="500" y="262" text-anchor="middle">Names slip because they mean nothing. Steps 2 to 4 give them meaning.</text>')
SVG['2.2'] = _svg('22', 290, 'The name loop: hear it, say it back, link it, write it, use it, then call back next time', _b)

SVG['2.3'] = _svg('23', 430, 'Three deep: door question, follow-up, follow-up to the follow-up, then something else; the boomerask branch fails', (
    '<rect class="bx" x="40" y="300" width="290" height="80" rx="12"/>'
    '<text class="t" x="60" y="328">1 DOOR</text><text class="ts" x="60" y="354">"What are you working on?"</text>'
    '<rect class="bj" x="250" y="200" width="300" height="80" rx="12"/>'
    '<text class="t" x="270" y="228">2 DEEPER</text><text class="ts" x="270" y="254">"What\'s the hardest part?"</text>'
    '<rect class="bj" x="470" y="100" width="330" height="80" rx="12"/>'
    '<text class="t" x="490" y="128">3 DEEPEST</text><text class="ts" x="490" y="154">"What would fixing it change?"</text>'
    '<rect class="bm" x="650" y="14" width="330" height="70" rx="12"/>'
    '<text class="t tm" x="670" y="42">CLOSE</text><text class="ts" x="670" y="66">"Is there something else?"</text>'
    '<path class="ln" d="M300 298 L330 284" marker-end="url(#p2a23)"/>'
    '<path class="ln" d="M520 198 L550 184" marker-end="url(#p2a23)"/>'
    '<path class="ln" d="M740 98 L770 88" marker-end="url(#p2a23)"/>'
    '<path class="lr" d="M185 382 L185 412 L420 412"/>'
    '<text class="ts tr" x="430" y="408">BOOMERASK: "Mine was amazing!" reads insincere</text>'
    '<text class="ts" x="560" y="236">ask about THEIR answer,</text><text class="ts" x="560" y="254">not your next topic</text>'
))

_q = [('PASSIVE', 'CONSTRUCTIVE', '"Nice, congrats."', 'polite, but flat', 'bx', 60, 110),
      ('ACTIVE', 'CONSTRUCTIVE', '"That\'s huge! How did they find you?"', 'the only one that builds the bond', 'bj', 520, 110),
      ('PASSIVE', 'DESTRUCTIVE', '"Cool. About the invoice..."', 'ignores it', 'bx', 60, 290),
      ('ACTIVE', 'DESTRUCTIVE', '"Hope the site can take the traffic."', 'kills the moment', 'bx', 520, 290)]
_b = '<text class="t" x="500" y="30" text-anchor="middle">Your client: "We just got featured in a travel magazine!"</text>'
for a, c, line, verdict, cls, x, y in _q:
    _b += ('<rect class="%s" x="%d" y="%d" width="420" height="150" rx="14"/>'
           '<text class="t" x="%d" y="%d">%s · %s</text>'
           '<text class="tb" x="%d" y="%d">%s</text>'
           '<text class="ts" x="%d" y="%d">%s</text>') % (cls, x, y, x + 20, y + 32, a, c, x + 20, y + 80, line, x + 20, y + 120, verdict)
_b += ('<path class="ln" d="M60 460 L940 460" marker-end="url(#p2a24)"/><text class="ts" x="940" y="452" text-anchor="end">more active</text>'
       '')
SVG['2.4'] = _svg('24', 470, 'Four ways to answer good news: only active and constructive builds the relationship', _b)

_c = [('GENERIC', ['"Great job!"'], 60, 'feels nice, gone by lunch'),
      ('SPECIFIC', ['"The way you calmed', 'that angry patient."'], 120, 'proves you noticed'),
      ('SPECIFIC + IMPACT', ['"...I\'m teaching it', 'to my callers now."'], 190, 'proves it changed something')]
_b = ''
for k, (h, lines, bar, note) in enumerate(_c):
    x = 40 + k * 320
    _b += '<rect class="%s" x="%d" y="40" width="290" height="150" rx="14"/>' % ('bj' if k == 2 else 'bx', x)
    _b += '<text class="t" x="%d" y="72">%s</text>' % (x + 20, h)
    for j, ln in enumerate(lines):
        _b += '<text class="tb" x="%d" y="%d">%s</text>' % (x + 20, 108 + j * 26, ln)
    _b += '<rect class="bg" x="%d" y="210" width="290" height="22" rx="11"/><rect class="bk" x="%d" y="210" width="%d" height="22" rx="11"/>' % (x, x, bar + 60)
    _b += '<text class="ts" x="%d" y="258">%s</text>' % (x, note)
_b += '<text class="ts" x="500" y="300" text-anchor="middle">Bars show how it lands on my scale, not data. The data: people underrate all three.</text>'
SVG['2.5'] = _svg('25', 316, 'Three compliments: generic, specific, specific plus impact', _b)

_rows = [('NAME', 'Rhea Shah (Dr.)'), ('MET AT', 'Dental expo, Ahmedabad, Oct'), ('PERSONAL', 'daughter has board exams in March'),
         ('BUSINESS', 'opening a second clinic in Jan'), ('WIN / WORRY', 'too many no-shows'), ('NEXT TOUCH', '10 Jan, after the opening'),
         ('CALLBACK', '"How did the second clinic open?"')]
_b = '<rect class="bx" x="30" y="24" width="580" height="356" rx="10"/><rect class="bm" x="30" y="24" width="580" height="44" rx="10"/>'
_b += '<text class="t tm" x="50" y="52">PEOPLE FILE · ONE CARD, TEN MINUTES</text>'
for k, (a, b) in enumerate(_rows):
    y = 104 + k * 40
    _b += '<line class="rule" x1="50" y1="%d" x2="590" y2="%d"/>' % (y + 12, y + 12)
    _b += '<text class="t" x="50" y="%d">%s</text><text class="ts" x="200" y="%d">%s</text>' % (y, a, y, b)
_b += ('<path class="ln" d="M660 60 L660 330 L970 330"/>'
       '<path class="lm" d="M664 74 C 690 220, 760 280, 966 300"/>'
       '<text class="ts" x="664" y="352">now</text><text class="ts" x="760" y="352">a day</text><text class="ts" x="900" y="352">a week</text>'
       '<text class="t" x="680" y="52">WHAT YOU REMEMBER</text>'
       '<path class="ln" d="M780 130 L700 160" marker-end="url(#p2a26)"/>'
       '<text class="ts" x="786" y="122">write it here,</text><text class="ts" x="786" y="140">within 10 minutes</text>'
       '<text class="ts" x="660" y="378">shape: Ebbinghaus, replicated 2015</text>')
SVG['2.6'] = _svg('26', 390, 'A people-file card with seven fields, beside a forgetting curve that drops steeply at first', _b)

_t = [('ARRIVE', 'hand the light', '2.1'), ('INTROS', 'catch the name', '2.2'), ('TALK', 'three deep', '2.3'),
      ('GOOD NEWS', 'ball in their court', '2.4'), ('LEAVING', 'one real compliment', '2.5'), ('IN THE CAB', 'write the cards', '2.6')]
_b = '<path class="ln" d="M50 150 L950 150"/>'
for k, (a, b, c) in enumerate(_t):
    x = 80 + k * 168
    _b += '<circle class="%s" cx="%d" cy="150" r="20"/>' % ('bk' if k in (0, 5) else 'bj', x)
    _b += '<text class="t" x="%d" y="110" text-anchor="middle">%s</text>' % (x, a)
    _b += '<text class="ts" x="%d" y="200" text-anchor="middle">%s</text>' % (x, b)
    _b += '<text class="ts tm" x="%d" y="222" text-anchor="middle">Stop %s</text>' % (x, c)
_b += '<text class="ts" x="500" y="40" text-anchor="middle">One evening, six moves, spread across the room. Never all six on one person.</text>'
SVG['2.7'] = _svg('27', 250, 'Timeline of one evening: arrive, intros, talk, good news, leaving, in the cab', _b)

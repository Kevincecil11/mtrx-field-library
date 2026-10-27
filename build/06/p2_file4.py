"""No. 06 Part II, File 4: Work the network (stops 2.23 to 2.30). Content as data, rendered by build.py.
Drafted 27 Oct 2026 by parallel research agents, sources and scenes verified, merged by merge06.py.
No em or en dashes anywhere (the lint fails on them)."""

FILE = {'n': 4,
 'sec': '3',
 'part': '3',
 'title': 'Work the network',
 'kicker': 'Part II · The Spotlight Files · File 4 of 5 · 8 stops',
 'promise': 'Ruddy got the Godfather job because he was known for one thing: making films cheap and fast. This file builds your one thing, the pitch '
            'that sells it, and the favour economy around it, without the mafia.'}

U = {'ruddy': 'https://www.independent.co.uk/independentpremium/long-reads/al-ruddy-mafia-offer-godfather-b2036443.html',
 'godfather_program': 'http://www.thegodfathertrilogy.com/program.txt',
 'granovetter': 'https://doi.org/10.1086/225469',
 'linkedin': 'https://doi.org/10.1126/science.abl4476',
 'pitch': 'https://doi.org/10.1177/0001839215597270',
 'chen': 'https://doi.org/10.5465/amj.2009.36462018',
 'player': 'https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=SuVRQBIdUfE&format=json',
 'godfather_clip': 'https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=DTtpWgrhS78&format=json',
 'ocean_clip': 'https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=1mJf24luhuo&format=json',
 'peaky_clip': 'https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=7cOfn_sjlXM&format=json',
 'jecker': 'https://doi.org/10.1177/001872676902200407',
 'grant': 'https://adamgrant.net/book/give-and-take/',
 'grant_interview': 'https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/givers-vs-takers-the-surprising-truth-about-who-gets-ahead/',
 'gifts': 'https://doi.org/10.1177/0963721416656937',
 'dormant': 'https://doi.org/10.1287/orsc.1100.0576',
 'dormant_mit': 'https://sloanreview.mit.edu/article/the-power-of-reconnection-how-dormant-ties-can-surprise-you/',
 'girard': 'https://automotivehalloffame.org/honoree/joe-girard/',
 'hbr_leads': 'https://hbr.org/2011/03/the-short-life-of-online-sales-leads',
 'black_hole': 'https://doi.org/10.1509/jm.10.0047',
 'cadence': 'https://resources.insidesales.com/wp-content/uploads/2020/02/research-SuccessfulSalesCadence.pdf',
 'memory': 'https://doi.org/10.1371/journal.pone.0120644',
 'ingram': 'https://doi.org/10.2189/asqu.52.4.558',
 'columbia_mixer': 'https://business.columbia.edu/insights/chazen-global-insights/what-really-happens-mixers',
 'prestige': 'https://doi.org/10.1037/a0030398',
 'gatsby': 'https://www.youtube.com/watch?v=2zHHkSu1br4',
 'american_psycho': 'https://www.youtube.com/watch?v=rC0HFwnK_5E',
 'greene': 'https://archive.org/stream/The48LawsOfPower_180/The48LawsOfPower_djvu.txt',
 'greene_guardian': 'https://www.theguardian.com/books/2012/dec/03/robert-greene-48-laws-of-power',
 'influence_meta': 'https://www.sciencedirect.com/science/article/abs/pii/S1048984316301655',
 'pursuit_short': 'https://www.youtube.com/watch?v=emzARZsJntw',
 'pursuit_long': 'https://www.youtube.com/watch?v=xPBBnS4br9w'}

SOURCES = [('The Independent, Al Ruddy and The Godfather', 'ruddy', '2.23'),
 ('The Godfather production programme', 'godfather_program', '2.23'),
 ('Granovetter 1973', 'granovetter', '2.23'),
 ('Rajkumar et al. 2022, Science', 'linkedin', '2.23'),
 ('Huang and Pearce 2015', 'pitch', '2.24'),
 ('Chen et al. 2009', 'chen', '2.24'),
 ('The Player pitch clip, oEmbed', 'player', '2.24'),
 ('Jecker and Landy 1969', 'jecker', '2.25'),
 ('Grant, Give and Take', 'grant', '2.25'),
 ('Grant, Knowledge at Wharton interview', 'grant_interview', '2.25'),
 ('Galak, Givi and Williams 2016', 'gifts', '2.25'),
 ('The Godfather favour clip, oEmbed', 'godfather_clip', '2.25'),
 ("Ocean's Eleven clip, oEmbed", 'ocean_clip', '2.26'),
 ('Levin, Walter and Murnighan 2011', 'dormant', '2.26'),
 ('Levin, Walter and Murnighan, MIT Sloan Review', 'dormant_mit', '2.26'),
 ('Peaky Blinders clip, oEmbed', 'peaky_clip', '2.26'),
 ('Automotive Hall of Fame, Joe Girard', 'girard', '2.27'),
 ('Oldroyd, McElheran and Elkington, HBR 2011', 'hbr_leads', '2.27'),
 ('Sabnis et al., The Sales Lead Black Hole', 'black_hole', '2.27'),
 ('InsideSales, The Truth Behind Successful Sales Cadences', 'cadence', '2.27'),
 ('Murre and Dros 2015', 'memory', '2.27'),
 ('Ingram and Morris 2007', 'ingram', '2.28'),
 ('Columbia Business School, What Really Happens at Mixers', 'columbia_mixer', '2.28'),
 ('Cheng et al. 2012, prestige and dominance', 'prestige', '2.28'),
 ('The Great Gatsby clip, Movieclips, oEmbed checked', 'gatsby', '2.28'),
 ('Greene and Elffers, The 48 Laws of Power', 'greene', '2.29'),
 ('American Psycho business card scene, The Dollar Theater, oEmbed checked', 'american_psycho', '2.29'),
 ('The Guardian interview with Robert Greene', 'greene_guardian', '2.29'),
 ('Lee et al. 2017, influence tactics meta-analysis', 'influence_meta', '2.29'),
 ('The Pursuit of Happyness clip, 390potrero, oEmbed checked', 'pursuit_short', '2.27'),
 ('The Pursuit of Happyness clip, Movieclips, oEmbed checked', 'pursuit_long', '2.30'),
 ('Oldroyd, McElheran and Elkington, HBR 2011', 'hbr_leads', '2.30'),
 ('InsideSales, The Truth Behind Successful Sales Cadences', 'cadence', '2.30'),
 ('Ingram and Morris 2007', 'ingram', '2.30')]

INTRO = {'lede': 'A network is not a pile of names. It is a reputation for one thing, a pitch people can repeat, favours that flow both ways, ties you keep '
         'warm, and a system that remembers for you.',
 'anatomy': ['Cold open: predict first', 'The subject', 'The story', 'The move', 'The scenes', 'Why it works', 'Truth tags', 'Do it today'],
 'files': [{'n': 1,
            'title': 'The Spotlight',
            'stops': '2.1 to 2.7',
            'note': 'Attention, names, questions, compliments, callbacks.',
            'href': '#m2-1',
            'now': False,
            'c': 'var(--jane)'},
           {'n': 2,
            'title': 'The Read',
            'stops': '2.8 to 2.13',
            'note': "Hungers, the director's read, groups, subtext, culture.",
            'href': '#m2-8',
            'c': 'var(--graphite)',
            'now': False},
           {'n': 3,
            'title': 'George Newman',
            'stops': '2.14 to 2.22',
            'note': 'Prep, voice, body, calm, warmth, monologues, the off switch.',
            'href': '#m2-14',
            'c': 'var(--gun)',
            'now': False},
           {'n': 4,
            'title': 'Pitch and network',
            'stops': '2.23 to 2.30',
            'note': 'Known for one thing, the pitch, favours, dormant ties, follow-up.',
            'href': '#m2-23',
            'c': 'var(--moss)',
            'now': True},
           {'n': 5,
            'title': 'The Line',
            'stops': '2.31 to 2.34',
            'note': 'Influence vs manipulation, Belfort, Barry Seal, the mask.',
            'href': '#m2-31',
            'c': 'var(--red)',
            'now': False}],
 'coverage': '<p><b>What File 4 covers.</b> 8 stops, 31 sources, every scene oEmbed-verified on 27 Oct 2026.</p><ul><li><b>2.23</b> Known for one '
             'thing: the website guy</li><li><b>2.24</b> The one-minute pitch</li><li><b>2.25</b> Favours and gifts, done right</li><li><b>2.26</b> '
             'Waking dormant ties</li><li><b>2.27</b> The follow-up system</li><li><b>2.28</b> Working a room</li><li><b>2.29</b> The 48 Laws worth '
             'knowing, decoded</li><li><b>2.30</b> Boss fight: the follow-up week</li></ul>'}

SVG = {'2.23': '<svg class="p2fig" viewBox="0 0 1000 330" role="img" aria-label="Positioning: a clear one thing sits at the intersection of a client, a '
         'proof, and a bridge to a new network"><defs><marker id="p2a223" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" '
         'markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#151515"/></marker><marker id="p2m223" '
         'viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path '
         'd="M0,0 L10,5 L0,10 z" fill="#ED691D"/></marker></defs><text class="t tm" x="500" y="34" text-anchor="middle">YOUR ONE THING</text><circle '
         'class="bx" cx="240" cy="142" r="104"/><circle class="bx" cx="500" cy="142" r="104"/><circle class="bx" cx="760" cy="142" r="104"/><text '
         'class="t" x="185" y="130" text-anchor="middle">CLIENT</text><text class="ts" x="185" y="154" text-anchor="middle">a costly '
         'problem</text><text class="t" x="500" y="130" text-anchor="middle">PROOF</text><text class="ts" x="500" y="154" text-anchor="middle">a '
         'repeatable result</text><text class="t" x="815" y="130" text-anchor="middle">BRIDGE</text><text class="ts" x="815" y="154" '
         'text-anchor="middle">a new weak tie</text><rect class="bj" x="290" y="220" width="420" height="68" rx="14"/><text class="tb" x="500" '
         'y="248" text-anchor="middle">websites for wildlife and safari brands</text><text class="ts" x="500" y="272" text-anchor="middle">proof: '
         'faster booking journeys, not a service list</text><path class="lm mv" d="M500 44 L500 80" marker-end="url(#p2m223)"/><text class="ts" '
         'x="500" y="316" text-anchor="middle">Say it so the right person can repeat it.</text></svg>',
 '2.24': '<svg class="p2fig" viewBox="0 0 1000 330" role="img" aria-label="A one minute pitch: problem, proof, promise, and next step, with the '
         'listener speaking next"><defs><marker id="p2a224" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" '
         'markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#151515"/></marker><marker id="p2m224" viewBox="0 0 10 '
         '10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 '
         'L0,10 z" fill="#ED691D"/></marker></defs><rect class="bx" x="35" y="66" width="205" height="100" rx="12"/><text class="t" x="55" y="98">1 '
         'PROBLEM</text><text class="ts" x="55" y="130">what is costly now?</text><text class="ts" x="55" y="150">name it plainly</text><rect '
         'class="bj" x="270" y="66" width="205" height="100" rx="12"/><text class="t" x="290" y="98">2 PROOF</text><text class="ts" x="290" '
         'y="130">one result</text><text class="ts" x="290" y="150">one credible detail</text><rect class="bj" x="505" y="66" width="205" '
         'height="100" rx="12"/><text class="t" x="525" y="98">3 PROMISE</text><text class="ts" x="525" y="130">what changes</text><text class="ts" '
         'x="525" y="150">for this listener?</text><rect class="bm" x="740" y="66" width="225" height="100" rx="12"/><text class="t tm" x="760" '
         'y="98">4 NEXT</text><text class="ts" x="760" y="130">a small, clear ask</text><text class="ts" x="760" y="150">then stop</text><path '
         'class="ln" d="M242 116 L265 116" marker-end="url(#p2a224)"/><path class="ln" d="M477 116 L500 116" marker-end="url(#p2a224)"/><path '
         'class="ln" d="M712 116 L735 116" marker-end="url(#p2a224)"/><path class="lm mv" d="M850 190 C 850 260, 150 260, 150 190" '
         'marker-end="url(#p2m224)"/><text class="ts tm" x="500" y="232" text-anchor="middle">your pitch ends where their question '
         'starts</text><text class="ts" x="500" y="304" text-anchor="middle">No origin story. No jargon pile. No promise without proof.</text></svg>',
 '2.25': '<svg class="p2fig" viewBox="0 0 1000 340" role="img" aria-label="Healthy reciprocity is an open loop: give useful value, make a clean ask, '
         'and leave refusal safe"><defs><marker id="p2a225" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" '
         'markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#151515"/></marker><marker id="p2m225" viewBox="0 0 10 '
         '10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 '
         'L0,10 z" fill="#ED691D"/></marker></defs><circle class="bj" cx="180" cy="152" r="82"/><text class="t" x="180" y="146" '
         'text-anchor="middle">GIVE</text><text class="ts" x="180" y="168" text-anchor="middle">useful, wanted</text><circle class="bx" cx="500" '
         'cy="152" r="82"/><text class="t" x="500" y="146" text-anchor="middle">ASK</text><text class="ts" x="500" y="168" '
         'text-anchor="middle">specific, optional</text><circle class="bj" cx="820" cy="152" r="82"/><text class="t" x="820" y="146" '
         'text-anchor="middle">THANK</text><text class="ts" x="820" y="168" text-anchor="middle">no scorekeeping</text><path class="ln" d="M270 152 '
         'L405 152" marker-end="url(#p2a225)"/><path class="ln" d="M590 152 L725 152" marker-end="url(#p2a225)"/><path class="lm mv" d="M820 242 C '
         '700 320, 300 320, 180 242" marker-end="url(#p2m225)"/><text class="ts tm" x="500" y="294" text-anchor="middle">the other person can say no '
         'and keep the relationship</text><rect class="bm" x="350" y="38" width="300" height="42" rx="12"/><text class="ts tm" x="500" y="65" '
         'text-anchor="middle">not a debt ledger</text></svg>',
 '2.26': '<svg class="p2fig" viewBox="0 0 1000 350" role="img" aria-label="Waking a dormant tie: remember the shared context, offer a useful update, '
         'ask for perspective, and release the pressure"><defs><marker id="p2a226" viewBox="0 0 10 10" refX="9" refY="5" '
         'markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" '
         'fill="#151515"/></marker><marker id="p2m226" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" '
         'markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#ED691D"/></marker></defs><rect class="bx" x="35" y="74" '
         'width="205" height="104" rx="12"/><text class="t" x="55" y="106">REMEMBER</text><text class="ts" x="55" y="138">where you met</text><text '
         'class="ts" x="55" y="158">what mattered then</text><rect class="bj" x="270" y="74" width="205" height="104" rx="12"/><text class="t" '
         'x="290" y="106">UPDATE</text><text class="ts" x="290" y="138">what you are doing</text><text class="ts" x="290" y="158">now</text><rect '
         'class="bj" x="505" y="74" width="205" height="104" rx="12"/><text class="t" x="525" y="106">ASK</text><text class="ts" x="525" y="138">one '
         'real question</text><text class="ts" x="525" y="158">not a hidden sale</text><rect class="bm" x="740" y="74" width="225" height="104" '
         'rx="12"/><text class="t tm" x="760" y="106">RELEASE</text><text class="ts" x="760" y="138">no urgency</text><text class="ts" x="760" '
         'y="158">easy no</text><path class="ln" d="M242 126 L265 126" marker-end="url(#p2a226)"/><path class="ln" d="M477 126 L500 126" '
         'marker-end="url(#p2a226)"/><path class="ln" d="M712 126 L735 126" marker-end="url(#p2a226)"/><text class="ts" x="500" y="240" '
         'text-anchor="middle">dormant is not dead: it is trust plus a new angle</text><path class="lm mv" d="M850 198 C 850 290, 150 290, 150 198" '
         'marker-end="url(#p2m226)"/><text class="ts tm" x="500" y="322" text-anchor="middle">reply is a gift, not an obligation</text></svg>',
 '2.27': '<svg class="p2fig" viewBox="0 0 1000 390" role="img" aria-label="A people CRM loop: capture, promise, useful follow-up, next date, and a '
         'stop rule"><defs><marker id="p2a227" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" '
         'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#151515"/></marker><marker id="p2m227" viewBox="0 0 10 10" refX="9" '
         'refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" '
         'fill="#ED691D"/></marker></defs><text class="t tm" x="500" y="30" text-anchor="middle">THE FOLLOW-UP LOOP</text><circle class="bk" '
         'cx="180" cy="160" r="54"/><text class="t" x="180" y="155" text-anchor="middle">CAPTURE</text><text class="ts" x="180" y="178" '
         'text-anchor="middle">name, need, date</text><circle class="bj" cx="500" cy="160" r="54"/><text class="t" x="500" y="155" '
         'text-anchor="middle">PROMISE</text><text class="ts" x="500" y="178" text-anchor="middle">one next action</text><circle class="bj" cx="820" '
         'cy="160" r="54"/><text class="t" x="820" y="155" text-anchor="middle">HELP</text><text class="ts" x="820" y="178" text-anchor="middle">new '
         'useful thing</text><path class="ln" d="M238 160 L438 160" marker-end="url(#p2a227)"/><path class="ln" d="M558 160 L758 160" '
         'marker-end="url(#p2a227)"/><path class="lm" d="M820 220 C820 340,180 340,180 220" marker-end="url(#p2m227)"/><text class="ts tm" x="500" '
         'y="320" text-anchor="middle">date it, then stop after a clear no</text><rect class="bx" x="100" y="248" width="160" height="48" '
         'rx="9"/><text class="ts" x="180" y="277" text-anchor="middle">ClickUp card</text><rect class="bx" x="420" y="248" width="160" height="48" '
         'rx="9"/><text class="ts" x="500" y="277" text-anchor="middle">next date</text><rect class="bx" x="740" y="248" width="160" height="48" '
         'rx="9"/><text class="ts" x="820" y="277" text-anchor="middle">permission</text><text class="ts" x="500" y="378" text-anchor="middle">Fast '
         'for a fresh inbound lead. Human for a real relationship. Never a drip campaign in disguise.</text></svg>',
 '2.28': '<svg class="p2fig" viewBox="0 0 1000 360" role="img" aria-label="A room map: start at the edge, enter with a bridge, contribute, then exit '
         'cleanly"><defs><marker id="p2a228" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" '
         'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#151515"/></marker><marker id="p2m228" viewBox="0 0 10 10" refX="9" '
         'refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" '
         'fill="#ED691D"/></marker></defs><text class="t tm" x="500" y="28" text-anchor="middle">EDGE TO EDGE</text><ellipse class="bx" cx="215" '
         'cy="170" rx="130" ry="78"/><text class="t" x="215" y="165" text-anchor="middle">KNOWN CLUSTER</text><text class="ts" x="215" y="188" '
         'text-anchor="middle">comfort, low discovery</text><ellipse class="bj" cx="500" cy="170" rx="130" ry="78"/><text class="t" x="500" y="165" '
         'text-anchor="middle">BRIDGE</text><text class="ts" x="500" y="188" text-anchor="middle">host, topic, person</text><ellipse class="bx" '
         'cx="785" cy="170" rx="130" ry="78"/><text class="t" x="785" y="165" text-anchor="middle">NEW CLUSTER</text><text class="ts" x="785" '
         'y="188" text-anchor="middle">one useful exchange</text><path class="ln" d="M345 170 L365 170" marker-end="url(#p2a228)"/><path class="ln" '
         'd="M630 170 L650 170" marker-end="url(#p2a228)"/><path class="lm" d="M785 265 C785 330,215 330,215 265" marker-end="url(#p2m228)"/><text '
         'class="ts tm" x="500" y="320" text-anchor="middle">exit: name the next conversation and leave</text><text class="ts" x="500" y="80" '
         'text-anchor="middle">Do not parachute into the centre. Find a seam, make the bridge explicit.</text></svg>',
 '2.29': '<svg class="p2fig" viewBox="0 0 1000 420" role="img" aria-label="Decode a power law by separating mechanism, evidence, risk, defence, and '
         'ethical replacement"><defs><marker id="p2a229" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" '
         'markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#151515"/></marker><marker id="p2m229" viewBox="0 0 10 '
         '10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 '
         'L0,10 z" fill="#ED691D"/></marker></defs><text class="t tm" x="500" y="28" text-anchor="middle">THE DECODER</text><rect class="bx" x="35" '
         'y="70" width="170" height="110" rx="12"/><text class="t" x="120" y="105" text-anchor="middle">LAW</text><text class="ts" x="120" y="135" '
         'text-anchor="middle">historical claim</text><text class="ts" x="120" y="155" text-anchor="middle">not a result</text><rect class="bj" '
         'x="240" y="70" width="170" height="110" rx="12"/><text class="t" x="325" y="105" text-anchor="middle">MECHANISM</text><text class="ts" '
         'x="325" y="135" text-anchor="middle">what could cause</text><text class="ts" x="325" y="155" text-anchor="middle">the effect?</text><rect '
         'class="bj" x="445" y="70" width="170" height="110" rx="12"/><text class="t" x="530" y="105" text-anchor="middle">CASE</text><text '
         'class="ts" x="530" y="135" text-anchor="middle">what happened?</text><text class="ts" x="530" y="155" text-anchor="middle">whose '
         'account?</text><rect class="bx" x="650" y="70" width="150" height="110" rx="12"/><text class="t" x="725" y="105" text-anchor="middle">RED '
         'FLAG</text><text class="ts" x="725" y="135" text-anchor="middle">pressure, secrecy,</text><text class="ts" x="725" y="155" '
         'text-anchor="middle">credit theft</text><path class="ln" d="M205 125 L230 125" marker-end="url(#p2a229)"/><path class="ln" d="M410 125 '
         'L435 125" marker-end="url(#p2a229)"/><path class="ln" d="M615 125 L640 125" marker-end="url(#p2a229)"/><rect class="bm" x="150" y="235" '
         'width="700" height="74" rx="12"/><text class="t tm" x="500" y="264" text-anchor="middle">DEFENCE + HONEST VERSION</text><text class="tb" '
         'x="500" y="291" text-anchor="middle">make the value visible, share credit, disclose the ask, allow no</text><text class="ts" x="500" '
         'y="365" text-anchor="middle">If the tactic needs a victim who cannot see the game, it is not networking.</text></svg>',
 '2.30': '<svg class="p2fig" viewBox="0 0 1000 410" role="img" aria-label="A five-day follow-up week: one promise, one useful touch, one room, one '
         'review, one clean close"><defs><marker id="p2a230" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" '
         'markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#151515"/></marker><marker id="p2m230" viewBox="0 0 10 '
         '10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 '
         'L0,10 z" fill="#ED691D"/></marker></defs><text class="t tm" x="500" y="28" text-anchor="middle">THE FOLLOW-UP WEEK</text><path class="ln" '
         'd="M90 150 L910 150"/><circle class="bk" cx="110" cy="150" r="24"/><circle class="bj" cx="310" cy="150" r="24"/><circle class="bj" '
         'cx="510" cy="150" r="24"/><circle class="bj" cx="710" cy="150" r="24"/><circle class="bk" cx="910" cy="150" r="24"/><text class="t" '
         'x="110" y="95" text-anchor="middle">MON</text><text class="t" x="310" y="95" text-anchor="middle">TUE</text><text class="t" x="510" y="95" '
         'text-anchor="middle">WED</text><text class="t" x="710" y="95" text-anchor="middle">THU</text><text class="t" x="910" y="95" '
         'text-anchor="middle">FRI</text><text class="ts" x="110" y="205" text-anchor="middle">capture</text><text class="ts" x="310" y="205" '
         'text-anchor="middle">help</text><text class="ts" x="510" y="205" text-anchor="middle">room</text><text class="ts" x="710" y="205" '
         'text-anchor="middle">ask</text><text class="ts" x="910" y="205" text-anchor="middle">review</text><path class="lm" d="M110 250 C300 '
         '345,710 345,910 250" marker-end="url(#p2m230)"/><text class="ts tm" x="500" y="300" text-anchor="middle">every touch earns the next '
         'touch</text><text class="ts" x="500" y="380" text-anchor="middle">Log the response, not your fantasy about the response. Stop when the '
         'answer is no.</text></svg>'}

STOPS = [{'id': '2.23',
  'day': 35,
  'title': 'Known for one thing: the website guy',
  'why': 'Al Ruddy did not get The Godfather because he was the most experienced producer in Hollywood. He got it because Paramount knew one thing '
         'about him: he could make modest films on time and within budget. That is a lesson in positioning, not a licence to join a mafia.',
  'dossier': {'k': 'Subject',
              'name': 'Albert S. Ruddy',
              'role': 'Producer of The Godfather, 1972 · practical fixer under pressure',
              'facts': [('Known for', 'Making modest films on time and within budget'),
                        ('The move', 'Own one repeatable promise'),
                        ('Steal it for', 'MTRX Digital: websites for wildlife and safari brands')],
              'stamp': ('hold', 'Holds up')},
  'cold': {'q': 'A new client asks what you do. Which answer is easiest for them to repeat: a list of six services, a job title, or one specific '
                'problem you solve for one kind of client? Pick one and rate confidence.',
           'a': '<b>One specific problem.</b> A position is not your whole biography. It is a short handle another person can carry to the next '
                'room. Ruddy had other credits, but cost, speed and delivery made him legible to Paramount.'},
  'story': ["Paramount had bought Mario Puzo's novel and initially imagined a cheap, quick adaptation. The studio invited Ruddy because his early "
            'producing work had already demonstrated the rare skill it needed: bringing modest movies in on time and within budget. The reported '
            'starting budget was $2.5 million, and the brief was to keep the picture small.',
            'That brief changed. Coppola and Puzo pushed the film back into a 1940s period drama, a decision that nearly doubled the budget to $6 '
            "million. Ruddy's useful identity was not merely cheapness. It was the ability to keep a difficult production moving while backing a "
            'strong creative decision. His one thing became practical delivery under constraint.',
            'The network lesson sits inside the production story. Ruddy was not famous for knowing everyone. He was useful to different groups: '
            'studio executives needed control, Coppola needed an ally, and the location community needed someone who would listen. A clear '
            'reputation travels farther than a long menu of capabilities.',
            'For Kevin, the test is not whether every client buys the niche. It is whether a safari owner can say, without opening your portfolio, '
            '<i>Kevin is the website person for wildlife brands.</i> That sentence is a bridge. Proof makes it trustworthy; a narrow promise makes '
            'it memorable.'],
  'move': {'line': 'Make your one thing portable.',
           'steps': [('Choose a costly problem.', 'Name the client and the result, not your software stack.'),
                     ('Prove the pattern.', 'Keep three before and after examples that show the same kind of win.'),
                     ('Give people the sentence.', 'Ask a friend to introduce you using your exact one line, then revise what they mangle.')]},
  'scenes': [{'id': '7cOfn_sjlXM',
              'title': 'Tommy Shelby meets Alfie Solomons',
              'year': '2014',
              'who': 'Cillian Murphy and Tom Hardy',
              'role': 'anti-hero',
              'dur': '',
              'key': 'A quiet offer maps a relationship · Tommy Shelby',
              'line': 'Tommy lets the offer arrive as information rather than pleading.',
              'watch': ['The controlled pace makes the offer feel considered',
                        'He gives the other person a reason to care before asking for movement',
                        'The scene makes leverage visible, which is why the ethical boundary matters'],
              'read': 'Tommy is legible because everyone knows what he brings and what he wants. The film makes reputation look like power.',
              'steal': 'Make your value easy to name, then state the boundary that keeps it honest.',
              'rc': 'Tommy is a criminal leader. Copy clarity and economy, never threat, bribery or hidden leverage.',
              'note': 'Content: criminal violence and menace. Clip on BBC.'}],
  'specs': [('Positioning', 'A short association between a person, a problem and a credible result. It is a memory aid, not a permanent box.'),
            ('Weak ties', 'Granovetter argued that weaker ties can bridge otherwise separate groups and carry new information.'),
            ('Nonlinear weak ties',
             'Rajkumar et al. found causal LinkedIn evidence that weak ties increased job mobility, but the relationship was not simply weaker is '
             'always better. Effects varied by tie measure and industry.'),
            ('Proof before expansion',
             'One repeatable result gives a narrow identity credibility. Add adjacent services only after the memorable promise is true.')],
  'fig': ('2.23', 'A position becomes repeatable where a client problem, a proof pattern and a bridge to a new network overlap.'),
  'evidence': [('Ruddy was hired for a reputation for modest films delivered on time and within budget',
                's',
                'The Independent, Al Ruddy and The Godfather',
                'ruddy'),
               ('Ruddy was producer of The Godfather and the original production plan was modest',
                'm',
                'The Godfather production programme',
                'godfather_program'),
               ('Weak ties can bridge groups and carry information', 's', 'Granovetter 1973', 'granovetter'),
               ('LinkedIn experiments found causal, nonlinear weak tie effects across over 20 million people',
                's',
                'Rajkumar et al. 2022, Science',
                'linkedin')],
  'tags': [('hold',
            '<i>Ruddy got the job because he was known for one thing.</i>',
            'Holds up in the narrower sense: sources support his cost and delivery reputation. It was not the only reason he succeeded, and the film '
            'later outgrew its cheap brief.',
            'ruddy'),
           ('myth',
            '<i>Weak ties are always better than strong ties.</i>',
            'The LinkedIn experiment supports a nonlinear pattern, with effects varying by industry and how tie strength is measured. Build bridges, '
            'but keep trusted collaborators.',
            'linkedin'),
           ('field',
            '<i>I am the website guy.</i>',
            'Use it only if your next three examples can prove it. A niche without proof is costume.',
            'granovetter')],
  'world': 'MTRX line to test: <i>I build booking-first websites for wildlife and safari brands, so owners get more qualified enquiries without '
           'making guests fight the site.</i> Keep your AI, apps and clinic work in the proof drawer. At the next Ahmedabad event, ask one person to '
           'repeat your line back. If they cannot, it is not portable yet.',
  'drill': {'name': 'The one-line test',
            'mins': '2 min',
            'steps': ['Write client, costly problem and measurable result in one sentence.',
                      'Remove tools, credentials and adjectives until the sentence still has a clear win.',
                      'Say it to one friend and ask what they would tell someone else about you.'],
            'mistake': 'Choosing a niche because it sounds stylish. Choose the problem you can repeatedly solve.'},
  'tryit': 'Write three versions of your one thing: safari lodge owner, wildlife tour operator and clinic owner. Send none yet. Read them aloud and '
           'circle the version that contains a result someone can repeat.',
  'writer': 'Ruddy is a useful character because his apparent limitation becomes a dramatic engine. Give a protagonist one reputation that opens a '
            'door, then make the plot punish them when that reputation is no longer enough.',
  'room': '<i>I am not a general digital agency. I am the website person for wildlife and safari brands, and I can show you the booking problem I '
          'fix.</i>',
  'nextq': 'Now that the room can remember you, can you explain the value before its attention expires? Stop 2.24.',
  'checks': [{'q': 'What made Ruddy legible to Paramount?',
              'o': ['A reputation for practical delivery', 'A long list of unrelated skills', 'A famous family connection'],
              'a': 0,
              'w': 'The sources support his cost, speed and delivery reputation. A portable identity made him easy to choose.'},
             {'q': 'What is the careful version of the weak-tie finding?',
              'o': ['Weak ties always beat strong ties',
                    'Weak ties can bridge groups, with effects varying by context',
                    'Only close friends create opportunities'],
              'a': 1,
              'w': 'Granovetter gives the bridge idea; Rajkumar et al. add a nonlinear, industry-dependent causal result.'},
             {'q': 'Which is the strongest positioning line for Kevin?',
              'o': ['I do websites, apps, AI and many other things', 'I am a digital entrepreneur', 'I build safari websites that win bookings'],
              'a': 2,
              'w': 'It names a client, a useful result and a repeatable pattern.'}]},
 {'id': '2.24',
  'day': 36,
  'title': 'The one-minute pitch',
  'why': 'A pitch is not a compressed biography. It is a short act of diagnosis: show that you understand a costly problem, offer one believable '
         'change, and leave the listener with a small next step. The best pitch scene is not the one with the most words. It is the one that changes '
         'what the listener wants to ask.',
  'dossier': {'k': 'Subject',
              'name': 'The working pitch',
              'role': 'A one-minute promise tested in a room, not a speech memorised for applause',
              'facts': [('Known for', 'Turning a vague service into a concrete outcome'),
                        ('The move', 'Problem, proof, promise, next step'),
                        ('Steal it for', 'Client calls, introductions and a future film pitch')],
              'stamp': ('hold', 'Holds up')},
  'cold': {'q': "When investors hear a short pitch, what is safest to trust: your own confidence, the listener's first impression, or a combination "
                'of intuition and analysis anchored in evidence? Pick one and rate confidence.',
           'a': '<b>A combination.</b> Huang and Pearce studied angel investors facing extreme uncertainty. Their gut feel was not magic or a '
                'substitute for analysis. It blended expertise-based intuition with formal analysis, and assessments of the entrepreneur predicted '
                'later outcomes in their setting.'},
  'story': ['The elevator-pitch myth says an entrepreneur must deliver a perfect sixty-second speech to a trapped stranger. Real rooms are less '
            'tidy. You may get twenty seconds, a question, or a distracted listener. The useful constraint is not the stopwatch. It is the '
            'discipline of making the problem and next step clear.',
            "Use four beats. First, name the problem in the listener's language. Second, give one proof, preferably a result or a specific "
            'observation. Third, say what changes for this person. Fourth, ask for a small next conversation. Then stop. A pitch that keeps speaking '
            'after the ask is not confidence; it is failure to read the room.',
            "Huang and Pearce found that angel investors' assessments of the entrepreneur predicted extraordinarily profitable venture success four "
            'years later in their field setting. That does not mean charisma guarantees funding. It means the person is part of the evidence '
            'investors use when the future is unknowable. Your job is to make the person behind the promise credible, not theatrical.',
            'Research on venture presentations also points to persuasion factors such as passion and preparedness. Treat that as a warning against a '
            'false choice between energy and substance. Kevin can sound alive about safari brands while showing one booking-flow result and asking '
            'whether the owner wants a two-minute audit.'],
  'move': {'line': 'Give the room a problem it can answer.',
           'steps': [('Name the cost.', '<i>Guests abandon the booking page on mobile</i> beats <i>digital transformation</i>.'),
                     ('Show one proof.', 'Use one number, before and after, or a short observed moment.'),
                     ('Offer a next step.', 'Ask for a ten-minute look, then let the listener choose the direction.')]},
  'scenes': [{'id': 'SuVRQBIdUfE',
              'title': 'The Player movie pitch scene',
              'year': '1992',
              'who': 'Tim Robbins and pitch participants',
              'role': 'real',
              'dur': '',
              'key': 'A pitch room where the hook must become a story · The Player',
              'line': 'The scene shows competing pitches being reduced to a hook that can be understood immediately.',
              'watch': ['Notice how quickly the room judges whether the premise is legible',
                        'Watch the difference between a list of ingredients and a clear dramatic engine',
                        'Treat the clip as a Hollywood satire, not as a universal formula'],
              'read': 'The room is not only judging the idea. It is judging whether the person can make the idea understandable under pressure.',
              'steal': 'Lead with the human problem and the change, not the inventory of features.',
              'rc': 'The film caricatures studio development and the clip is a re-upload, not a transcript of real investor practice. Use its '
                    'compression as a writing lesson, not as evidence of a success rate.',
              'note': 'Content: Hollywood satire, workplace pressure. Clip on Filmograscene.'}],
  'specs': [('Problem', "A specific pain or desire in the listener's world, stated before your solution."),
            ('Proof', 'A concrete result, observation or credible reason to believe the promise. One good detail beats five claims.'),
            ('Gut feel',
             'Huang and Pearce use the term for dynamic emotion and cognition that blends expertise-based intuition and analysis under extreme '
             'uncertainty.'),
            ('Prepared energy', 'Passion can help a presentation, but it should point to a prepared story and evidence rather than replace them.')],
  'fig': ('2.24', 'A short pitch is a handoff: problem, proof, promise, next step, then the listener gets the next line.'),
  'evidence': [('Angel investors blended expertise-based intuition with formal analysis and entrepreneur assessment predicted later success in the '
                'study',
                's',
                'Huang and Pearce 2015',
                'pitch'),
               ('Passion and preparedness in business-plan presentations were linked to investor funding decisions', 'm', 'Chen et al. 2009', 'chen'),
               ('The Player clip metadata and title were verified through YouTube oEmbed', 'h', 'The Player pitch clip, oEmbed', 'player')],
  'tags': [('myth',
            '<i>The perfect elevator pitch lasts exactly one minute.</i>',
            'There is no universal stopwatch rule. Use one minute as rehearsal space, then adapt to the room and stop when the listener starts '
            'asking useful questions.',
            'pitch'),
           ('part',
            '<i>Investors fund the most confident speaker.</i>',
            'Investors use impressions, intuition and analysis together. Confidence without evidence can read as noise; evidence without a person '
            'can be hard to trust.',
            'pitch'),
           ('field',
            '<i>I can redesign your safari booking flow. Want a ten-minute audit?</i>',
            'Test whether this creates a question, not whether it earns a polite compliment.',
            'chen')],
  'world': 'For a safari owner: <i>Many lodge sites show beautiful rooms but make the booking path hard on a phone. I build wildlife-brand sites '
           "around the guest's decision, and on one recent flow we cut the route from five screens to two. If you send me your booking link, I will "
           'return a two-minute friction audit. No pitch deck needed.</i>',
  'drill': {'name': 'Four beats, one breath',
            'mins': '2 min',
            'steps': ["Write the listener's costly problem in twelve words.",
                      'Add one proof and one changed outcome.',
                      'End with a small ask and practise stopping for three seconds.'],
            'mistake': 'Answering an imagined objection before the listener has shown interest. Let their question choose the next beat.'},
  'tryit': 'Record a 60-second pitch for a safari-lodge owner. Listen once for jargon and once for whether the ask is clear. Cut one sentence. Send '
           'it only to yourself, then rewrite the line that sounded most like a brochure.',
  'writer': 'A pitch scene is a miniature power scene. Give one character a clock, one listener a hidden criterion and one detail that proves the '
            'speaker has done the work. Let the listener interrupt before the speech ends.',
  'room': '<i>The pitch is not my speech. It is the first question I make easy for you to ask.</i>',
  'nextq': 'If a useful introduction is a gift, when does a favour become a debt? Stop 2.25.',
  'checks': [{'q': "What belongs first in Kevin's one-minute pitch?",
              'o': ["The client's costly problem", 'His entire technology stack', 'His childhood and degree'],
              'a': 0,
              'w': "Lead with the listener's problem. Proof and promise follow."},
             {'q': 'What did Huang and Pearce mean by investor gut feel?',
              'o': ['A mystical sixth sense', 'Expertise plus analysis', 'A fixed checklist used by every investor'],
              'a': 1,
              'w': 'Their study describes dynamic emotion-cognition under extreme uncertainty, not magic.'},
             {'q': 'After the small next step, what should Kevin do?',
              'o': ['Keep adding features until they agree', 'Offer three unrelated services', 'Stop and let the listener respond'],
              'a': 2,
              'w': 'The pitch ends where a real conversation starts.'}]},
 {'id': '2.25',
  'day': 37,
  'title': 'Favours and gifts, done right',
  'why': 'The opening of The Godfather is a masterclass in a dangerous exchange. Bonasera asks for a violent service, Vito turns the request into a '
         'relationship, and the future debt is left hanging in the air. Study it as an anti-model. In a healthy network, a favour is useful, '
         'voluntary and safe to refuse.',
  'dossier': {'k': 'Subject',
              'name': 'Vito Corleone, as the anti-model',
              'role': 'The Godfather, 1972 · patronage, reciprocity and coercive obligation',
              'facts': [('Known for', 'Making every favour feel like family business'),
                        ('The move', 'Give value without manufacturing a debt'),
                        ('Steal it for', 'Introductions, audits and small acts of useful help')],
              'stamp': ('anti', 'Anti-model')},
  'cold': {'q': 'Which gift is most likely to be useful: the impressive gift you enjoy choosing, the generic gift that proves you remembered, or the '
                'thing matched to what the recipient will actually use? Pick one and rate confidence.',
           'a': "<b>The thing matched to the recipient's use.</b> Gift research finds a recurring giver-recipient gap: givers focus on the moment of "
                'exchange, while recipients often care more about value after they own it. In business, a useful audit beats a branded object.'},
  'story': ['Bonasera enters the wedding day asking Vito to arrange murder. Vito does not answer the transaction at face value. He asks why Bonasera '
            'went to the police and why he did not come first. The request is reclassified as a failure of relationship, then Vito offers justice as '
            'a gift while making the future service unmistakable.',
            'That is the mafia favour economy: warmth plus memory plus an implied ledger, backed by violence. It can look like networking because it '
            'contains the same visible ingredients as trust: attention, help and continuity. The difference is consent. A favour that cannot be '
            'declined is not generosity. It is control.',
            "The Ben Franklin effect is often told as a clean trick: ask someone for a small favour and they will like you more. Jecker and Landy's "
            '1969 study is the classic source, but it was a single older experiment. Treat the effect as partly supported and context-bound, not as '
            'a lever to pull on a rival. Ask for help because the person has relevant knowledge and because no is genuinely fine.',
            "Adam Grant's giver, matcher and taker language is useful as a map, not a personality diagnosis. Givers help without strings, matchers "
            'keep exchange fair, and takers seek more than they contribute. The healthy target is generous but bounded: give what you can afford, '
            'ask clearly, and do not turn generosity into an invoice.'],
  'move': {'line': 'Make the favour free to refuse.',
           'steps': [('Give something useful.', 'Match the gift to their need, not your desire to look generous.'),
                     ('Ask cleanly.', 'State the request, time cost and why them, with an explicit no-pressure exit.'),
                     ('Close the loop.', 'Thank them, report what happened and do not imply they now owe you.')]},
  'scenes': [{'id': 'DTtpWgrhS78',
              'title': 'Godfather Favor',
              'year': '1972',
              'who': 'Marlon Brando',
              'role': 'anti-hero',
              'dur': '',
              'key': 'Bonasera receives justice as a gift · Vito Corleone',
              'line': '"Some day, and that day may never come, I\'ll call upon you to do a service for me."',
              'watch': ['The pause makes a future debt sound almost tender',
                        'The word gift sits beside the implied obligation',
                        'The warmth cannot be separated from the threat behind it'],
              'read': 'Vito converts help into controlled obligation. The scene teaches why a favour can feel intimate and frightening at once.',
              'steal': 'Name mutuality honestly: <i>I can do this, and there is no debt. If I ask later, you can say no.</i>',
              'rc': 'This is a trimmed, user-uploaded clip and a criminal patronage scene. Copy the pause and clarity only as craft; reject '
                    'coercion, violence and hidden leverage.',
              'note': 'Content: mafia threat and violence. Clip on Jamie Grove.'}],
  'specs': [('Reciprocity', 'The social expectation that help can circulate. Healthy reciprocity leaves timing, amount and refusal open.'),
            ('Ben Franklin effect',
             'Jecker and Landy reported increased liking after a direct favour request in one 1969 experiment. The evidence is too narrow for a '
             'guaranteed networking rule.'),
            ('Gift gap',
             'Givers often evaluate the exchange moment; recipients often evaluate how useful the gift is once owned. Ask or observe before giving.'),
            ('Bounded giving', 'Generosity is durable when the cost is affordable and the giver does not keep a hidden score.')],
  'fig': ('2.25', 'A healthy favour loop has an open door, not a debt ledger. Give useful value, ask optionally, thank and release.'),
  'evidence': [('The direct-favour liking study exists, but is a single 1969 experiment', 'm', 'Jecker and Landy 1969', 'jecker'),
               ('Givers, matchers and takers describe different reciprocity preferences', 'h', 'Grant, Give and Take', 'grant'),
               ('Givers and recipients can value different features of gifts', 's', 'Galak, Givi and Williams 2016', 'gifts'),
               ('The Godfather clip was verified through YouTube oEmbed', 'h', 'The Godfather favour clip, oEmbed', 'godfather_clip')],
  'tags': [('anti',
            '"Some day, and that day may never come, I\'ll call upon you."',
            "In Vito's mouth this is an implied debt backed by power. In your network, make the ask explicit, bounded and safe to refuse.",
            'godfather_clip'),
           ('part',
            '<i>Ask for a favour and people will like you.</i>',
            'The classic Jecker and Landy result is real but old and narrow. Ask for expertise because it is relevant, not to manufacture '
            'attachment.',
            'jecker'),
           ('hold',
            '<i>The best gift is what the receiver can use.</i>',
            "The gift-gap literature supports checking the recipient's future use instead of optimising for the giver's feeling at the exchange.",
            'gifts')],
  'world': 'Good MTRX favour: send a safari owner a two-minute screen recording showing one broken booking step, with no sales call attached. If you '
           'later ask for an introduction, say exactly who it is for, how long it takes and <i>No pressure if it is not useful.</i> A favour is '
           'still honest when the answer is no.',
  'drill': {'name': 'Open-loop reciprocity',
            'mins': '2 min',
            'steps': ['Choose one useful thing you can give without resentment.',
                      'Write a request with cost, reason and an easy no.',
                      'Write the thank-you you will send even if the answer is no.'],
            'mistake': 'Giving something unwanted, then silently charging interest. Ask what would actually help.'},
  'tryit': 'Do one small useful act for a current or former contact: an introduction only if both sides want it, a specific audit or a relevant '
           'link. Do not attach an ask. Notice whether removing the ledger changes how you feel.',
  'writer': 'The Godfather opening works because the gift and the threat share a sentence. Write a clean version and a rotten version of the same '
            'favour. Keep the words similar; change who can refuse and what happens after no.',
  'room': '<i>I can help with that. You do not owe me anything, and if I ask for a favour later you can say no without damaging the '
          'relationship.</i>',
  'nextq': 'What if the person you need has not heard from you in three years? Stop 2.26.',
  'checks': [{'q': 'What makes the Godfather favour an anti-model?',
              'o': ['The request is backed by coercive power', 'It is too short', 'It contains gratitude'],
              'a': 0,
              'w': 'The problem is not reciprocity. It is that refusal is unsafe and the debt is enforced.'},
             {'q': 'What is the careful status of the Ben Franklin effect?',
              'o': ['A guaranteed networking trick', 'A single classic study', 'A finding with no study at all'],
              'a': 1,
              'w': 'Jecker and Landy published the classic 1969 experiment. Its narrow evidence does not justify a guaranteed tactic.'},
             {'q': 'What should guide a professional gift?',
              'o': ['How impressive it looks to you', 'How much future debt it creates', 'What the recipient can use'],
              'a': 2,
              'w': 'Gift research finds a recurring giver-recipient mismatch. Start with their use.'}]},
 {'id': '2.26',
  'day': 38,
  'title': 'Waking dormant ties',
  'why': 'The contact you have not messaged since college may be more useful than the person you see every week. Not because time creates magic, but '
         'because a dormant tie can combine old trust with a new perspective. Reconnect as a person first, not as a sales funnel with a human name '
         'attached.',
  'dossier': {'k': 'Subject',
              'name': 'The dormant tie',
              'role': 'A former contact, now out of touch, with shared context and a changed world',
              'facts': [('Known for', 'Trust that can wake up faster than a cold introduction'),
                        ('The move', 'Remember, update, ask, release'),
                        ('Steal it for', 'Old classmates, former clients, film contacts and wildlife operators')],
              'stamp': ('hold', 'Holds up')},
  'cold': {'q': 'Which first message is least awkward: a generic <i>hope you are well</i>, a sudden sales pitch, or a specific memory plus a genuine '
                'update and question? Pick one and rate confidence.',
           'a': '<b>A specific memory plus a genuine update and question.</b> It gives the recipient context and a reason to reply. Levin, Walter '
                'and Murnighan found that reconnecting dormant contacts for work advice produced outcomes comparable to current ties, and previously '
                'strong dormant ties could offer novelty, efficiency, trust and shared perspective.'},
  'story': ['Levin, Walter and Murnighan asked Executive MBA students to consult contacts they had not been in touch with for at least three years '
            'on an important work project. The dormant contacts were not dead weight. Their advice compared favourably with advice from current '
            'ties.',
            'The mechanism is a useful surprise. A dormant relationship can retain trust and shared perspective from the old connection while '
            'offering information from a different current network. That combination can be more useful than a close colleague who already sees the '
            'problem exactly as you do.',
            'The awkwardness comes from pretending the gap did not happen or hiding the real reason for writing. Do neither. Name the old context, '
            'say what changed for you, ask one bounded question and make the reply optional. A two-way update is a reconnection. A disguised '
            'referral request is a transaction.',
            'Danny Ocean is a fictional anti-hero who understands the social value of old ties: he recruits people through shared history and a '
            'specific role rather than a mass announcement. Borrow the respect for distinct skills, not the deception. Kevin can wake old classmates '
            'by asking about a real wildlife, product or film problem and offering a useful update of his own.'],
  'move': {'line': 'Reconnect with context, not guilt.',
           'steps': [('Remember the bridge.', 'Name where you met and one real detail you remember.'),
                     ('Bring an update.', 'Say what you are doing now and why it made you think of them.'),
                     ('Ask and release.', 'Ask one useful question, then add that there is no pressure to reply or help.')]},
  'scenes': [{'id': '1mJf24luhuo',
              'title': "Ocean's Eleven: Reeling in Reuben",
              'year': '2001',
              'who': 'George Clooney and Elliott Gould',
              'role': 'anti-hero',
              'dur': '',
              'key': 'Shared history before the ask · Danny Ocean and Reuben Tishkoff',
              'line': 'Danny uses gratitude, humour and shared history before asking Reuben to consider the project.',
              'watch': ['The relationship is established before the request arrives',
                        'Danny treats Reuben as a capable insider, not a lead in a funnel',
                        'The exit after resistance keeps the tie intact'],
              'read': 'Danny knows the old relationship is an asset, but he does not use it as a threat. He makes the role specific.',
              'steal': 'Reopen an old tie with one remembered detail, one current update and one bounded question.',
              'rc': 'Danny is a con man and the project is criminal. Copy the respect for history and refusal, not deception or manipulation.',
              'note': 'Content: mild language and criminal planning. Clip on Movieclips.'}],
  'specs': [('Dormant tie',
             'A former relationship in which the people have lost touch. It can retain relational knowledge while opening a different information '
             'path.'),
            ('Novelty',
             'Dormant contacts may sit outside your current work cluster, so their advice can add information you are not already hearing.'),
            ('Low-friction reconnection',
             'Specific shared context lowers the cognitive load of replying. A real question gives the message a purpose.'),
            ('No hidden funnel',
             'If the actual aim is a referral or sale, disclose that after the relationship is reopened. Do not counterfeit nostalgia.')],
  'fig': ('2.26', 'A dormant tie wakes through memory, an honest update, one bounded question and an easy release.'),
  'evidence': [('Reconnecting dormant contacts produced useful work advice comparable to current ties',
                's',
                'Levin, Walter and Murnighan 2011',
                'dormant'),
               ('Previously strong dormant ties offered benefits associated with both weak and strong ties',
                's',
                'Levin, Walter and Murnighan 2011',
                'dormant'),
               ('The authors describe dormant ties as a deep, useful pool, not a guaranteed source of help',
                'm',
                'Levin, Walter and Murnighan, MIT Sloan Review',
                'dormant_mit'),
               ("The Ocean's Eleven clip was verified through YouTube oEmbed", 'h', "Ocean's Eleven clip, oEmbed", 'ocean_clip')],
  'tags': [('hold',
            '<i>Dormant ties are worthless because you let them go cold.</i>',
            'The study directly challenges that assumption. Reconnection can recover trust and add novelty, though it does not guarantee a favour or '
            'opportunity.',
            'dormant'),
           ('myth',
            '<i>A dormant tie is a shortcut to a referral.</i>',
            'The evidence concerns advice and knowledge, not a guaranteed sale. Rebuild the relationship before asking for an introduction.',
            'dormant_mit'),
           ('field',
            '<i>I saw your lodge launch post and remembered our wildlife-club project. I now build booking flows for safari brands. What is the '
            'hardest part of getting guests from interest to enquiry? No pressure to reply.</i>',
            'Use a message like this as a test of honesty, not a script to pressure a person.',
            'dormant')],
  'world': 'Pick three people from college, old MTRX work or a previous safari conversation. Send one message that names the shared context, gives a '
           'current update and asks one real question. Do not attach a deck. If a reply comes, be curious. If none comes, do not send a guilt '
           'follow-up.',
  'drill': {'name': 'The warm re-entry',
            'mins': '2 min',
            'steps': ['Write the shared context and one detail you genuinely remember.',
                      'Write your current update in two sentences, with no achievement parade.',
                      'Ask one bounded question and add an easy no or no-reply option.'],
            'mistake': 'Pretending the silence did not happen. Acknowledge the gap lightly and give the person a reason that is about them as well '
                       'as you.'},
  'tryit': 'Choose one dormant tie and draft a 70-word message. Read it as the recipient: does it contain a real memory, a real update and a real '
           'question? Remove any hidden ask. Send only if the answer is yes.',
  'writer': 'Dormant ties are dramatic because the history is offscreen. In five minutes, write two characters meeting after ten years. Let one old '
            'detail prove intimacy, then let a changed detail prove that memory is not the same as knowledge.',
  'room': '<i>We have been out of touch, so I will not pretend this is casual. I remembered your work on X, and I would value your view on one '
          'specific question. No pressure if now is not a good time.</i>',
  'nextq': 'You have a one thing, a pitch and a living network. Next, build the follow-up system that keeps it from evaporating.',
  'checks': [{'q': 'What did the dormant-ties study compare?',
              'o': ['Advice from dormant and current ties', 'Old contacts compared with strangers', 'Sales from gifts to sales from pitches'],
              'a': 0,
              'w': 'Executive MBA students consulted dormant and current contacts on an important work project.'},
             {'q': 'What should open a reconnection message?',
              'o': ['A hidden referral request', 'A real context and update', 'A long portfolio attachment'],
              'a': 1,
              'w': 'Context lowers awkwardness and gives the person a reason to reply.'},
             {'q': "What is the ethical boundary in the Ocean's Eleven lesson?",
              'o': ['Use history to pressure a yes', 'Never contact anyone from the past', 'Use history with a safe refusal'],
              'a': 2,
              'w': 'Shared history can support a respectful ask, but it cannot make refusal unsafe.'}]},
 {'id': '2.27',
  'day': 39,
  'title': 'The follow-up system',
  'why': 'The best follow-up is not a reminder that you exist. It is a small promise kept on a date, with a useful reason to reopen the '
         'conversation. Joe Girard built a record career by re-contacting buyers, but his famous number was not magic: it was a system that made the '
         'next contact hard to forget.',
  'dossier': {'k': 'Subject',
              'name': 'Joe Girard',
              'role': 'Detroit car salesman, Automotive Hall of Fame inductee, 1963 to 1977',
              'facts': [('Known for', 'More than 13,000 retail cars in 13 years'),
                        ('The move', 'Constant contact after the sale'),
                        ('Steal it for', 'MTRX prospects who are interested, not yet ready'),
                        ('Evidence status', 'Holds up as a documented case, not a universal sales law')],
              'stamp': ('hold', 'Holds up')},
  'cold': {'q': 'A study of 2,241 US companies sent a web-generated test lead. What was the average response time among companies that eventually '
                'replied within 30 days: 4 hours, 42 hours, or 10 days? Rate your confidence from 1 to 5.',
           'a': '<b>42 hours.</b> That is an audit of response behaviour, not proof that every business should answer in exactly 5 minutes. A '
                'separate 1.25 million lead analysis reported that contact within an hour was nearly seven times as likely to qualify as contact an '
                'hour later, and more than 60 times as likely as waiting 24 hours or longer. Treat those as associations in the studied sales '
                'settings, not a promise about MTRX conversion.'},
  'story': ['Joe Girard sold more than 13,000 cars one at a time during a 13-year career. The Automotive Hall of Fame account says he would move on '
            'to another customer, or re-contact a recent buyer to check that the new car was working well. The follow-up was not a desperate request '
            "for a referral. It began with the buyer's outcome.",
            'The same account records his constant-contact idea and his estimate that a satisfied buyer could influence a large circle of friends '
            'and family. That 250 figure came from his own informal polling of wedding planners and funeral directors. It is a useful story about '
            "reputational stakes, not a peer-reviewed estimate of everyone's network.",
            'The modern data point is less glamorous and more useful. Oldroyd, McElheran and Elkington audited 2,241 companies: 37 percent answered '
            'within an hour, 16 percent in one to 24 hours, 24 percent after more than 24 hours, and 23 percent never answered. Their separate '
            'analysis covered 1.25 million leads across 29 B2C and 13 B2B companies. Speed mattered in those samples, but this is sales-lead '
            'evidence, not a licence to pester a person who said no.',
            "So build Kevin's people CRM as a memory and permission system. Capture what matters, record the promised next action, set the date, "
            'send one useful thing, and log the result. A ClickUp task can hold the relationship without pretending a human being is a funnel '
            'stage.'],
  'move': {'line': 'Follow up with memory, value, date, and an exit.',
           'steps': [('Capture the human context.', 'Name, organisation, problem, what they care about, and the last conversation.'),
                     ('Make one small promise.', 'A teardown, example, introduction, or answer. Put a date on it before the call ends.'),
                     ('Close the loop cleanly.', 'Send the useful thing, ask one next question, then pause or archive after a clear no.')]},
  'scenes': [{'id': 'emzARZsJntw',
              'title': 'Pursuit of Happyness: Cold Calling',
              'year': '2006',
              'who': 'Chris Gardner',
              'role': 'Will Smith',
              'dur': '01:54',
              'key': 'The list becomes a timed work block · YouTube title verified by oEmbed',
              'line': 'Gardner works a call sheet under a severe time limit, protecting the minutes that can produce a real conversation.',
              'watch': ['He works from a defined list instead of waiting for motivation',
                        'He keeps the work moving after ordinary refusals',
                        'The film turns persistence into a clock problem, not a personality myth'],
              'read': 'The useful beat is disciplined contact under constraint. It is not evidence that every prospect wants repeated calls.',
              'steal': 'Create a short, scheduled follow-up block and measure promises kept, not just dials made.',
              'rc': "This is a dramatized sales story and a cold-calling scene, not a controlled test of Gardner's method.",
              'note': 'Content: financial strain and high-pressure sales. Channel: 390potrero, oEmbed title checked October 2026.'}],
  'specs': [('Fresh inbound deserves speed',
             'The HBR study found a 42-hour average response among companies that replied within 30 days; its separate lead analysis associated '
             'contacting within an hour with much higher qualification rates.'),
            ('A CRM is an external memory',
             'A dated next action prevents the Zeigarnik-like feeling of an unfinished relationship from becoming random chasing. Use the card to '
             'remember context, not to manufacture intimacy.'),
            ('Cadence is not a law',
             'The vendor study analysed 479,140 activities across 1,456 cadences and explicitly found no one-size-fits-all cadence. Its useful '
             'principle is to test attempts, media, duration, and spacing in your own pipeline.'),
            ('Spacing helps learning',
             'Murre and Dros tested retrieval practice and found a substantial spacing effect in a large online replication. Spaced review helps '
             'your memory of a prospect; it does not prove that spaced messages will convert.')],
  'fig': ('2.27', 'A ClickUp people card becomes ethical only when it stores a promise, a useful next touch, and permission to stop.'),
  'evidence': [('2,241-company audit: response distribution and 42-hour average among responders', 's', 'Oldroyd et al., HBR 2011', 'hbr_leads'),
               ('Separate 1.25 million lead analysis: speed and qualification association', 'm', 'Oldroyd et al., HBR 2011', 'hbr_leads'),
               ('Follow-up failure studied across 461 sales reps in four firms', 's', 'Sabnis et al., Journal of Marketing', 'black_hole'),
               ('479,140 activities across 1,456 cadences, vendor observational study', 'm', 'InsideSales cadence report', 'cadence'),
               ("Joe Girard's career and re-contact practice", 's', 'Automotive Hall of Fame', 'girard')],
  'tags': [('hold',
            'A dated next action beats a vague promise to stay in touch.',
            'Write the action and date while the conversation is still warm.',
            'girard'),
           ('part',
            'A famous 5-minute response rule is a universal law.',
            'The HBR evidence supports speed in studied lead settings, not one magic minute for every MTRX relationship.',
            'hbr_leads'),
           ('anti',
            'More touches are always better.',
            'Use a stop rule: a clear no, no permission, or repeated silence means pause, archive, or ask once for a better channel.',
            'cadence')],
  'world': 'In ClickUp, make one private people card per real prospect: name and organisation, problem, last contact, promised help, next date, '
           'preferred channel, and a status of <i>active</i>, <i>waiting</i>, <i>nurture</i>, or <i>closed</i>. For a safari lodge owner, send the '
           'promised homepage teardown on Tuesday, ask whether the booking engine is the bottleneck, and set the next date only if they want one. '
           'For your two commission callers, log their actual need, not a sales score.',
  'drill': {'name': 'The seven-field card',
            'mins': '2 min',
            'steps': ["Write one person's name, context, and current problem.",
                      'Write one useful thing you can deliver and a date.',
                      'Add the stop condition: what counts as a no or a pause?'],
            'mistake': 'Turning a person into a lead score. The card is for remembering promises and consent.'},
  'tryit': 'Choose one live MTRX prospect. Create the card, send the smallest useful follow-up you already promised, and propose one date only if '
           'the person has left the door open. Record reply, not your interpretation.',
  'writer': 'Show the follow-up as a prop. A character opens a card, sees a promise they made, and must choose between keeping it, hiding from it, '
            'or asking permission to reset it. The moral turn is visible in the choice, not in a speech.',
  'room': '"I do not chase people. I keep promises, add something useful, and make the next step easy to decline."',
  'nextq': 'If everyone arrives intending to meet new people, why do rooms keep becoming islands? Stop 2.28.',
  'checks': [{'q': 'What did the HBR audit find among companies that replied within 30 days?',
              'o': ['An average response of 42 hours', 'A universal five-minute rule', 'No relationship to response time'],
              'a': 0,
              'w': 'The reported average was 42 hours. The study does not establish a universal five-minute law.'},
             {'q': "What belongs in Kevin's people CRM?",
              'o': ['Only a lead score', 'Context, promise, date, and permission to stop', 'A script that handles every possible objection for you'],
              'a': 1,
              'w': 'The system stores human context and agreed next actions, with an exit condition.'},
             {'q': "Joe Girard's 250 figure is best treated as...",
              'o': ['A peer-reviewed network constant', 'A precise conversion forecast', 'An anecdotal business heuristic'],
              'a': 2,
              'w': "The Hall of Fame account says it came from Girard's informal polling, so use it as a story, not a law."}]},
 {'id': '2.28',
  'day': 40,
  'title': 'Working a room',
  'why': 'At a mixer, 95 percent of guests said they wanted new contacts. The tracking tags told a quieter story: the average guest had 14 '
         'encounters, and friends made up about half of them. The room was not rejecting strangers. Comfort was doing the steering.',
  'dossier': {'k': 'Subject',
              'name': 'The bridge-builder',
              'role': 'A practical room role, not a born extrovert',
              'facts': [('Known for', 'Making one new connection without abandoning the old one'),
                        ('The move', 'Enter at the edge, contribute, exit with grace'),
                        ('Steal it for', 'Ahmedabad meetups, lodge conferences, client dinners'),
                        ('Evidence status', 'Holds up in one instrumented mixer, not a universal party formula')],
              'stamp': ('hold', 'Holds up')},
  'cold': {'q': 'At the Ingram and Morris mixer, guests wore electronic tags. The average guest had 14 encounters. What share of those encounters '
                'involved friends: about one tenth, one half, or nearly all? Rate your confidence from 1 to 5.',
           'a': "<b>About one half.</b> Columbia's research summary reports that friends accounted for a disproportionate half of encounters, even "
                'though 95 percent said they wanted to meet new people. The useful inference is not that friends are bad. It is that comfort quietly '
                'consumes the opportunity you thought you were buying.'},
  'story': ['The party experiment was unusually literal. About 100 executives, entrepreneurs, consultants, and bankers wore nTags that recorded when '
            'two tags faced each other within eight feet for at least a minute. Before the event, each person marked whom they already knew. That '
            'gave the researchers a map of intention and behaviour instead of a memory of the night.',
            'The mismatch was the puzzle. Ninety-five percent said their goal was to meet new people. Yet the average guest had 14 encounters, and '
            'friends accounted for half. The researchers attributed much of the pull to comfort: with a friend, there is less risk that a joke dies '
            'or an introduction fails.',
            'The result was not a verdict against mixers. Guests did meet people different from themselves, and the study found surprisingly little '
            'average evidence of demographic homophily in encounters. It also found a time effect: people began with more same-gender encounters and '
            'later crossed more of that boundary as the room itself became familiar.',
            'So enter through a seam, not a performance. Stand near the edge of a group, listen for the topic, and add one relevant observation or '
            'question. If you join through a person who knows both sides, say the bridge out loud. After a few minutes, introduce your new contact '
            'to someone else or name your next conversation and leave. Networking is not collecting bodies. It is making the next connection '
            'easier.'],
  'move': {'line': 'Find the seam, add value, then move the connection onward.',
           'steps': [('Read the shape.', 'Look for an open edge, a person alone, or a topic you can honestly contribute to.'),
                     ('Enter with a bridge.', 'Use the host, shared topic, or mutual contact. Ask what brought them here, then listen.'),
                     ('Exit with generosity.',
                      'Offer an introduction or one useful link, say you are going to greet someone else, and leave without trapping them.')]},
  'scenes': [{'id': '2zHHkSu1br4',
              'title': 'The Great Gatsby: The Mysterious Mr. Gatsby',
              'year': '2013',
              'who': 'Nick Carraway and Jay Gatsby',
              'role': 'Tobey Maguire and Leonardo DiCaprio',
              'dur': '02:38',
              'key': 'A stranger navigates a crowded party and finds the host · YouTube title verified by oEmbed',
              'line': 'Nick moves through a huge party, asks for the host, and is pulled into encounters before he knows the room.',
              'watch': ['The party is a network of overlapping micro-groups, not one conversation',
                        'Nick uses a simple host question to create an entry point',
                        'The camera makes the room feel exciting and socially disorienting at once'],
              'read': 'The scene is a warning as much as a model: spectacle creates contact, but contact is not yet a relationship.',
              'steal': 'Use a clear bridge question, then make one introduction before you leave.',
              'rc': 'A film compresses social uncertainty and gives the protagonist a designed path. Real groups may not welcome an interruption.',
              'note': 'Content: alcohol, crowd pressure, class performance. Channel: Movieclips, oEmbed title checked October 2026.'}],
  'specs': [('Comfort is a structural force',
             'Ingram and Morris found friends occupied a disproportionate half of encounters. The barrier is not simply shyness; existing ties make '
             'the low-risk path easy.'),
            ('A bridge lowers ambiguity',
             'A host, mutual friend, shared topic, or visible task gives both sides a reason for the interruption. This is social infrastructure, '
             'not a clever line.'),
            ('Prestige travels better than dominance',
             'Cheng et al. found both dominance and prestige could raise perceived influence, but prestige targets were liked while dominance '
             'targets were not. Share expertise, do not intimidate.'),
            ('Exit is part of the welcome',
             "A clean exit protects the other person's autonomy and lets you keep a high number of brief, real encounters rather than one exhausting "
             'captive conversation.')],
  'fig': ('2.28', 'The room has a known cluster, a bridge, and a new cluster. Your job is to make the bridge explicit and keep moving.'),
  'evidence': [('95 percent wanted new people, while friends made up about half of encounters',
                's',
                'Columbia summary of Ingram and Morris',
                'columbia_mixer'),
               ('nTags recorded encounters at roughly eight feet and at least one minute',
                's',
                'Columbia summary of Ingram and Morris',
                'columbia_mixer'),
               ('Original mixer paper reports limited new-contact mixing and associative homophily', 's', 'Ingram and Morris 2007', 'ingram'),
               ('Prestige targets were liked more than dominance targets', 's', 'Cheng et al. 2012', 'prestige')],
  'tags': [('hold',
            'Most people drift toward people they already know at mixers.',
            'Arrive with a one-person mission: one new contact, one useful introduction, then return to your friends.',
            'ingram'),
           ('part',
            'People avoid difference at events.',
            'This study found little average evidence of demographic homophily in encounters, while comfort and existing ties still shaped '
            'persistence.',
            'columbia_mixer'),
           ('anti',
            'Dominance is the fastest route to a room.',
            'Prestige can create influence without the dislike attached to intimidation. Demonstrate useful knowledge and share credit.',
            'prestige')],
  'world': 'At an Ahmedabad founder event, do not walk in with a quota of ten contacts. Pick one bridge: the organiser, a safari photographer, or a '
           'clinic owner you already know. Ask them to introduce you to one person working on bookings or patient trust. After three minutes, give '
           'that person one relevant MTRX observation, then say you are going to greet the next person and actually go.',
  'drill': {'name': 'The edge entry',
            'mins': '2 min',
            'steps': ['Name a room you will enter and one honest bridge into it.',
                      'Write one question that fits the room, not your pitch.',
                      'Write your exit: one introduction or useful link, then leave.'],
            'mistake': 'Treating the room as a hunt for status. The aim is a better-connected room after you leave.'},
  'tryit': 'At your next event, spend the first ten minutes with one familiar person, then ask for one introduction outside their immediate cluster. '
           'Make one useful contribution, introduce the two people if you can, and record what happened without scoring yourself on charm.',
  'writer': 'Stage the room as geography. Put the protagonist at the edge of a loud cluster, give them one visible bridge, and let the exit reveal '
            'character. Who leaves a conversation richer, and who leaves a person stranded?',
  'room': '"I am not trying to work the whole room. I am trying to leave one small bridge stronger than I found it."',
  'nextq': 'What happens when a historical anecdote is sold as a law of human nature? Stop 2.29.',
  'checks': [{'q': 'What did the instrumented mixer reveal?',
              'o': ['Friends made about half of encounters', 'Nobody met anyone outside their existing network', 'All guests mixed evenly'],
              'a': 0,
              'w': 'The average guest had 14 encounters and friends accounted for a disproportionate half.'},
             {'q': 'What is the best entry to a group?',
              'o': ['Interrupt with your full pitch',
                    'Use a host, topic, or mutual contact as a bridge',
                    'Stand silently and wait for someone to rescue you'],
              'a': 1,
              'w': 'A bridge makes the interruption legible and gives both people a reason to continue.'},
             {'q': 'In Cheng et al., prestige differed from dominance because prestige targets were...',
              'o': ['More intimidating', 'Less visible', 'More likable'],
              'a': 2,
              'w': 'Both could increase influence, but prestige targets were viewed as likable while dominance targets were not.'}]},
 {'id': '2.29',
  'day': 41,
  'title': 'The 48 Laws worth knowing, decoded',
  'why': "Robert Greene's 48 Laws of Power is a historical cabinet of anecdotes wearing the uniform of a rulebook. Some laws point toward real "
         'mechanisms, such as reputation, planning, and the difference between expertise and intimidation. Others ask you to hide intent, create '
         'dependence, or find a victim. Read it as a smoke alarm, not as a script.',
  'dossier': {'k': 'Decoder',
              'name': 'Robert Greene',
              'role': 'Author of The 48 Laws of Power, 1998',
              'facts': [('Known for', 'Forty-eight laws built from historical stories'),
                        ('The move', 'Turn maxims into mechanisms, then test them'),
                        ('Steal it for', 'Defence against power games, not manipulation'),
                        ('Evidence status', 'Historical anecdotes are not experimental evidence')],
              'stamp': ('part', 'Partly')},
  'cold': {'q': 'Greene gives a historical example for a law. What does that example establish: that the tactic always works, that it happened once '
                'in a particular context, or that modern research has confirmed all 48 laws? Rate your confidence from 1 to 5.',
           'a': '<b>It establishes a story happened as presented, at most.</b> The book itself frames the laws as a distillation of historical '
                'material. A case can suggest a mechanism, but it cannot turn a selective anecdote into a universal law. Ask what the mechanism is, '
                'what evidence would contradict it, and who pays the cost.'},
  'story': ["Open Greene's contents and the tone is clear. Law 1 says not to outshine the master. Law 3 says to conceal intentions. Law 7 says to "
            'get others to do the work and take the credit. Law 9 says actions beat arguments. They sit together as if they had the same evidential '
            'status. They do not.',
            "The book's preface says the laws draw on three thousand years of writings and historical figures. That is a rich source of cases, but "
            'it is also a selection made to illustrate a thesis. The same anecdote can teach a mechanism, conceal a missing variable, or flatter the '
            'storyteller who survived to tell it.',
            'Research gives us better distinctions. Cheng and colleagues separated dominance, gaining rank through force or intimidation, from '
            'prestige, gaining rank through expertise. Both could increase perceived influence, but prestige targets were liked and dominance '
            'targets were not. A meta-analysis of 49 independent samples and 8,987 participants found positive relationships for rational '
            'persuasion, consultation, collaboration, and other tactics, while pressure was negatively related to outcomes; rational persuasion was '
            'the most stable across categories.',
            'Decode a law in five passes: mechanism, case, red flags, defence, honest version. Law 5, reputation, becomes a reason to make your work '
            'legible and repair mistakes. Law 29, planning to the end, becomes contingency planning. Law 14, pose as a friend and spy, becomes a '
            'warning about information extraction. Never convert the last one into a usable script. If a move requires secrecy, dependency, stolen '
            'credit, or a person unable to refuse, reject the move and teach the defence.'],
  'move': {'line': 'Read power tactics as warning labels, then replace the poison.',
           'steps': [('Name the mechanism.', 'Is the move using expertise, reciprocity, pressure, scarcity, ambiguity, or fear?'),
                     ('Find the red flag.', 'Look for hidden intent, stolen credit, manufactured dependence, isolation, or no safe refusal.'),
                     ('Choose the honest version.', 'Disclose the ask, share credit, make the benefit mutual, and let the other person say no.')]},
  'scenes': [{'id': 'rC0HFwnK_5E',
              'title': 'American Psycho: Comparing Business Cards',
              'year': '2000',
              'who': 'Patrick Bateman and colleagues',
              'role': 'Christian Bale and Jared Leto',
              'dur': '05:30',
              'key': 'Status competition disguised as taste · YouTube title verified by oEmbed',
              'line': 'A boardroom exchange turns ordinary business cards into a silent contest for rank, taste, and belonging.',
              'watch': ['The objects do social work before anyone makes an explicit argument',
                        'Small differences in finish become a threat to identity',
                        'The scene makes prestige hunger visible, then turns it grotesque'],
              'read': 'The mechanism is social comparison and status anxiety, not a law that a better card creates power.',
              'steal': 'Make the work and the evidence impressive. Do not use scarcity, secrecy, or humiliation to make another person feel small.',
              'rc': 'The film is stylised satire and contains violent themes. It shows status anxiety, not a general sales effect of business cards.',
              'note': 'Content: graphic violence themes and status anxiety. Channel: The Dollar Theater, oEmbed title checked October 2026.'}],
  'specs': [('Anecdote is not a law',
             "Greene's cases are historical material selected to make a point. They can generate hypotheses, not universal predictions."),
            ('Prestige and dominance are different',
             'Expertise can earn respect; intimidation can earn attention while damaging liking. A room may obey a dominant person and still not '
             'trust them.'),
            ('Pressure is a brittle tactic',
             'Lee et al. found pressure was negatively related to task and relationship outcomes across their meta-analysis, while rational '
             'persuasion was the only tactic with stable positive relationships in both categories.'),
            ('Defence starts with disclosure',
             'Ask what is being requested, who benefits, what information is missing, and whether refusal is genuinely safe. A visible process '
             'removes much of the power of a hidden game.')],
  'fig': ('2.29', 'The decoder keeps the vivid case but adds the missing steps: mechanism, evidence, red flags, defence, and honest version.'),
  'evidence': [('Greene frames the 48 laws as distilled from historical writings and examples',
                's',
                'The 48 Laws of Power, preface and contents',
                'greene'),
               ('Greene described the book as exposing workplace dirty tricks and writing at an extreme for literary purposes',
                's',
                'The Guardian interview',
                'greene_guardian'),
               ('Prestige targets were liked more than dominance targets', 's', 'Cheng et al. 2012', 'prestige'),
               ('Meta-analysis: rational persuasion stable positive, pressure negative', 's', 'Lee et al. 2017', 'influence_meta')],
  'tags': [('hold',
            'Reputation, planning, and expertise can matter.',
            'Use them transparently: show work, plan contingencies, and share know-how.',
            'prestige'),
           ('myth',
            'The 48 laws are timeless, definitive laws.',
            'They are selective historical anecdotes. Treat them as hypotheses and warnings, not evidence.',
            'greene'),
           ('anti',
            'Secrecy and dependence are networking skills.',
            'If you need hidden intent or a victim who cannot refuse, stop. Name the ask and restore the exit.',
            'influence_meta')],
  'world': 'When a client says a competitor is using a Greene-style move, do not counter-manipulate. Write five headings in the ClickUp task: '
           "mechanism, case, red flag, defence, honest version. For example, a competitor's mystery becomes an invitation to show MTRX work openly: "
           "a before and after, a clear scope, a real constraint, and a price range. Kevin's edge is not being harder to read. It is being safer to "
           'trust.',
  'drill': {'name': 'The five-pass decoder',
            'mins': '2 min',
            'steps': ['Choose one law or power move and state its mechanism.',
                      'List the red flag and the defence.',
                      'Write the honest version without a script for controlling anyone.'],
            'mistake': 'Admiring the move before asking who loses. Every tactic has a target and a cost.'},
  'tryit': 'Take one piece of networking advice you have saved. Run the five passes and put the result in your notes. If the advice cannot survive a '
           'visible, voluntary version, delete it.',
  'writer': 'Write two versions of the same scene. In the first, a character hides the ask and wins a short-term concession. In the second, another '
            'character names the mechanism aloud and offers a safe refusal. Let the audience decide which victory can survive the next scene.',
  'room': '"Greene gives me warning labels, not lines. I want the mechanism, the red flag, and the honest replacement."',
  'nextq': 'Can five ordinary days turn all four network skills into behaviour? Stop 2.30.',
  'checks': [{'q': 'What does a historical anecdote prove?',
              'o': ['A universal law', 'A story in a particular context', 'A replicated experiment across many modern workplaces'],
              'a': 1,
              'w': 'Anecdotes can suggest mechanisms, but they do not establish universal effects.'},
             {'q': 'Which status route was liked more in Cheng et al.?',
              'o': ['Dominance through intimidation', 'Neither route', 'Prestige through expertise'],
              'a': 2,
              'w': 'Prestige and dominance could both increase influence, but prestige targets were liked.'},
             {'q': 'What did the influence-tactics meta-analysis find about pressure?',
              'o': ['It was negatively related to outcomes', 'It was always the best tactic in every workplace', 'It was never measured'],
              'a': 0,
              'w': 'Across the meta-analysis, pressure was negatively related to task and relationship outcomes.'}]},
 {'id': '2.30',
  'day': 42,
  'title': 'Boss fight: the follow-up week',
  'rewatch': True,
  'why': 'You now have the whole file: <i>Known for one thing: the website guy</i>, <i>The one-minute pitch</i>, <i>Favours and gifts, done '
         'right</i>, and <i>Waking dormant ties</i>, followed by a people CRM, a room entry, and a decoder for power games. The boss fight is '
         'deliberately small: five working days, three real MTRX prospects, no fantasy pipeline. Chris Gardner supplies the film spine, but your '
         'score is promises kept and consent respected.',
  'dossier': {'k': 'Field case',
              'name': 'Chris Gardner',
              'role': 'Film character in The Pursuit of Happyness, a dramatized sales story',
              'facts': [('Known for', 'Working a call sheet under a hard time limit'),
                        ('The move', 'Turn scarce time into a repeatable block'),
                        ('Steal it for', 'A five-day MTRX follow-up sprint'),
                        ('Evidence status', 'The film is a scene model, not sales data')],
              'stamp': ('field', 'Field test')},
  'cold': {'q': 'In the InsideSales cadence analysis, which pattern had the highest reported contact rate among the compared groups: one call over a '
                'long period, or a short multi-touch cadence with several media? Rate your confidence from 1 to 5.',
           'a': '<b>The short multi-touch cadence.</b> The report says its ten most successful cadences averaged 6.7 attempts, 3.0 media types, and '
                '6.7 days, with a 72.0 percent average contact rate, while its ten most common cadences averaged 21.9 percent. This is vendor '
                'observational data and a comparison of selected groups, not a guarantee for three MTRX prospects.'},
  'story': ['In the film, Gardner has less time than his colleagues and turns the shortage into a system. He works up a call sheet, protects the '
            'minutes, and keeps the phone moving. The cinematic lesson is not to copy the no-water or no-hanging-up tricks. It is to make the work '
            'visible enough that a week can teach you something.',
            'Start Monday with three real prospects: one hot inbound, one warm dormant tie, and one event contact. Give each a one-sentence reason '
            'for the next touch. The hot inbound gets speed and a useful answer. The dormant tie gets context and an easy opt-out. The event contact '
            'gets a bridge, not a pitch.',
            'Tuesday delivers one useful thing. Wednesday is the room move: one introduction, one conversation, and one clean exit. Thursday makes '
            'the ask only where the other person has shown interest, and names the mutual benefit without pressure. Friday reviews the log: which '
            'promise was kept, which channel worked, which person asked for space, and what you should stop doing.',
            'The week is a field test, not a morality play. Compare your own baseline before borrowing any cadence number. The honest output may be '
            'one qualified call, one referral, or three respectful closures. A network grows when people can predict that your follow-up will be '
            'useful and that your no will be accepted.'],
  'move': {'line': 'Five days, three people, one honest measure: did the next step become clearer?',
           'steps': [('Monday and Tuesday: create and help.',
                      "Capture context, send the promised useful thing, and log the exact next date or the person's pause."),
                     ('Wednesday and Thursday: bridge and ask.',
                      'Work one room, make one introduction, then ask only where interest and a mutual benefit are visible.'),
                     ('Friday: review and release.',
                      'Count promises kept, replies, introductions, and clear no answers. Archive what should not be chased.')]},
  'scenes': [{'id': 'xPBBnS4br9w',
              'title': 'The Pursuit of Happyness: Cold Calling',
              'year': '2006',
              'who': 'Chris Gardner',
              'role': 'Will Smith',
              'dur': '',
              'key': 'A call sheet becomes a daily operating system · YouTube title verified by oEmbed',
              'line': 'Gardner moves through a list, protects a narrow work window, and reaches a decision maker when an opening appears.',
              'watch': ['The list gives the day a spine rather than a mood',
                        'He treats each call as a small attempt, not a verdict on his identity',
                        'The scene makes clear that persistence still needs a real opportunity at the other end'],
              'read': 'The film supplies urgency. File 4 adds the missing ethics: useful context, permission, a bridge, and a stop rule.',
              'steal': "Run a five-day experiment with a small list and a review, instead of adopting someone else's sales mythology.",
              'rc': "The scene is edited drama and the movie's sales outcome is not a controlled comparison. Do not copy the unhealthy time-saving "
                    'stunts.',
              'note': 'Content: poverty, pressure, repeated cold calls. Channel: Movieclips, oEmbed title checked October 2026.'}],
  'specs': [('A sprint turns advice into data',
             'Five days is long enough to observe response and short enough to remember what you changed. Keep the list small so you can read the '
             'cases.'),
            ('Different ties need different cadence',
             'An inbound query, a dormant acquaintance, and a new event contact do not carry the same permission or urgency. One schedule for all '
             'three is not a system.'),
            ('The unit is the next step',
             'Do not optimise for messages sent. Optimise for a clear next action, a useful introduction, a pause, or a clean no.'),
            ('Film gives a spine, not evidence',
             "Gardner's work ethic is a narrative model. Use HBR, the Journal of Marketing, and the cadence report for claims about sales behaviour, "
             'with their sampling limits attached.')],
  'fig': ('2.30', 'The week loops from capture to help to room to ask to review. Each day leaves a trace the next day can use.'),
  'evidence': [('Film clip shows Gardner working a call sheet under time pressure', 's', 'The Pursuit of Happyness, Movieclips', 'pursuit_long'),
               ('HBR samples show speed and non-response problems in online lead handling', 's', 'Oldroyd et al., HBR 2011', 'hbr_leads'),
               ('Cadence report compares attempts, media, spacing, and duration, but is vendor observational data',
                'm',
                'InsideSales cadence report',
                'cadence'),
               ('70 percent lead black hole in study of marketing leads, with four-firm sample',
                's',
                'Sabnis et al., Journal of Marketing',
                'black_hole'),
               ('Mixer evidence supports leaving the friend cluster to broaden contacts', 's', 'Ingram and Morris 2007', 'ingram')],
  'tags': [('field',
            'A short experiment beats importing a universal cadence.',
            'Run the same five-day log on three different relationship types, then revise.',
            'cadence'),
           ('hold',
            'Clear next actions and honest stop rules make follow-up sustainable.',
            'Keep the promise, make the ask visible, and accept silence or no.',
            'black_hole'),
           ('anti',
            "Gardner's time-saving stunts are a professional standard.",
            'Copy the block and the list, not dehydration, frantic speed, or disregard for the person on the other end.',
            'pursuit_long')],
  'world': 'Pick three prospects before Monday: a safari-lodge owner who requested an audit, a dormant tie who once mentioned a website problem, and '
           'a clinic owner you meet at a room. Monday create the cards and the one-line next action from <i>The one-minute pitch</i>. Tuesday send '
           'one useful artefact, not a disguised gift. Wednesday attend or simulate a room and make one bridge. Thursday wake one dormant tie and '
           'ask for a 20-minute call only where the reply supports it. Friday review reply, next step, pause, or no. Put the numbers in one ClickUp '
           'list, but write the learning in plain English.',
  'drill': {'name': 'The five-day card',
            'mins': '2 min',
            'steps': ['Choose three prospects and label the relationship type, not just the lead temperature.',
                      'Write Monday, Tuesday, Wednesday, Thursday, and Friday actions.',
                      'Add the review fields: promise kept, reply, next step, pause, or no.'],
            'mistake': 'Treating activity as progress. A full week of touches can still be a failure if the other person never had a real choice.'},
  'tryit': 'Run the five-day plan with three prospects. Keep each message short, specific, and useful. At the end, save one sentence about what you '
           'learned about your own follow-up, not what you assume about the people who did not reply.',
  'writer': 'Use the week as a montage with a moral clock. Monday promises, Tuesday tests, Wednesday exposes the room, Thursday tempts the character '
            'to push, Friday reveals whether they learned. Repeat one prop, the CRM card, and change what it means in the final shot.',
  'room': '"My network is not a pile of names. It is a set of promises I can keep, bridges I can make, and no answers I can respect."',
  'nextq': 'What is the line between a clear ask and a hidden attempt to control the room? File 5, Stop 2.31.',
  'checks': [{'q': 'What is the boss-fight score?',
              'o': ['Messages sent', 'Promises kept and next steps clarified', 'How many people were forced to answer you'],
              'a': 1,
              'w': 'The useful unit is a clearer next step, a useful bridge, a pause, or a clean no.'},
             {'q': 'Why does the cadence evidence need a caveat?',
              'o': ['It is based on vendor observational data', 'It tested every industry equally', 'It proves one schedule for all relationships'],
              'a': 0,
              'w': 'The report is vendor observational data and does not prove a universal schedule.'},
             {'q': 'On Friday, what should Kevin do with repeated silence?',
              'o': ['Escalate forever', 'Invent an objection and answer it', 'Review, pause, or archive'],
              'a': 2,
              'w': 'A stop rule protects the prospect and turns silence into a decision about your process.'}]}]

"""No. 06 Part II, File 2: The Read (stops 2.8 to 2.13). Content as data, rendered by build.py.
Drafted 27 Oct 2026 by parallel research agents, sources and scenes verified, merged by merge06.py.
No em or en dashes anywhere (the lint fails on them)."""

FILE = {'n': 2,
 'sec': '6',
 'part': '6',
 'title': 'The Read',
 'kicker': 'Part II · The Spotlight Files · File 2 of 5 · 6 stops',
 'promise': 'Directors read actors for a living. Six stops on what people really hunger for, how Kazan and Lumet read a performer, who actually '
            'decides in a group, subtext, culture, and one full meeting read with every tool.'}

U = {'sdt': 'https://doi.org/10.1037//0003-066x.55.1.68',
 'sdt_goals': 'https://selfdeterminationtheory.org/SDT/documents/2000_DeciRyan_PIWhatWhy.pdf',
 'fiske': 'https://doi.org/10.1521/soco.1995.13.3.189',
 'status': 'https://doi.org/10.1037/a0038781',
 'maslow': 'https://journals.aom.org/doi/10.5465/amle.2017.0351',
 'sheldon': 'https://doi.org/10.1111/j.1467-6494.2009.00589.x',
 'voss_clip': 'https://www.youtube.com/watch?v=lsotPuX6oxg',
 'voss_oembed': 'https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=lsotPuX6oxg&format=json',
 'kazan_life': 'https://books.google.com/books?id=R7wKgsVUDUYC',
 'kazan_freshair': 'https://freshairarchive.org/segments/celebrating-30-years-fresh-air-filmmaker-and-theater-legend-elia-kazan',
 'lumet_making': 'https://books.google.com/books?id=x7JiAAAAMAAJ',
 'lumet_tv': 'https://interviews.televisionacademy.com/interviews/sidney-lumet',
 'weston': 'https://judithweston.com/web/books-judith-weston',
 'east_clip': 'https://www.youtube.com/watch?v=VfOrY7CidTA',
 'east_oembed': 'https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=VfOrY7CidTA&format=json',
 'hidden': 'https://doi.org/10.1037//0022-3514.48.6.1467',
 'hidden_history': 'https://doi.org/10.1080/1047840x.2003.9682897',
 'raven': 'https://doi.org/10.1111/j.1540-4560.1993.tb01191.x',
 'angry': 'https://www.youtube.com/watch?v=5xNlNV-UIUs',
 'angry_oembed': 'https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=5xNlNV-UIUs&format=json',
 'angry_negotiation': 'https://direct.mit.edu/ngtn/article/23/4/449/122102/Minority-Matters-12-Angry-Men-as-a-Case-Study-of-a',
 'forrester': 'https://www.forrester.com/b2b-marketing/buying-group-roles/',
 'gartner': 'https://www.gartner.com/en/sales/insights/buyer-enablement',
 'pinker': 'https://doi.org/10.1073/pnas.0707192105',
 'sacks': 'https://doi.org/10.2307/413184',
 'repair': 'https://doi.org/10.2307/413107',
 'pomerantz': 'https://doi.org/10.1007/978-1-4612-5092-0_3',
 'mehrabian': 'https://doi.org/10.1037/h0024648',
 'mehrabian_site': 'https://www.kaaj.com/psych/linguistic.html',
 'pinter': 'https://www.theguardian.com/culture/2008/dec/31/harold-pinter-early-essay-writing',
 'dumb_waiter': 'https://www.youtube.com/watch?v=nLwC5RonO_w',
 'lives': 'https://www.youtube.com/watch?v=S7u6kE9emUs',
 'meyer': 'https://erinmeyer.com/books/the-culture-map/',
 'hall': 'https://www.penguinrandomhouse.com/books/73813/beyond-culture-by-edward-t-hall/',
 'hall_pdf': 'https://teaching.up.edu/bus511/xculture/Hall%20and%20Hall%201990,%20ch1.pdf',
 'hofstede': 'https://doi.org/10.1177/0018726702055001602',
 'brewer': 'https://doi.org/10.1177/0170840613517602',
 'kenya': 'https://ecommons.aku.edu/book_chapters/565/',
 'south_africa': 'http://hdl.handle.net/1808/28077',
 'tall_poppy': 'https://researchers.mq.edu.au/en/publications/thou-shalt-not-be-a-tall-poppy-describing-an-australian-communica/',
 'lost': 'https://www.youtube.com/watch?v=FiQnH450hPM',
 'moneyball': 'https://www.youtube.com/watch?v=_5KQDjrVHc8',
 'moneyball_book': 'https://wwnorton.com/books/Moneyball/'}

SOURCES = [('Ryan and Deci 2000, self determination theory', 'sdt', '2.8'),
 ('Deci and Ryan 2000, goal pursuits', 'sdt_goals', '2.8'),
 ('Stevens and Fiske, five core social motives', 'fiske', '2.8'),
 ('Anderson, Hildreth and Howland 2015, status', 'status', '2.8'),
 ('Bridgman, Cummings and Ballard 2019, Maslow history', 'maslow', '2.8'),
 ('Sheldon and Gunz 2009, needs as motives', 'sheldon', '2.8'),
 ('Chris Voss clip oEmbed', 'voss_oembed', '2.8'),
 ('Kazan, A Life', 'kazan_life', '2.9'),
 ('Fresh Air transcript, Elia Kazan 1988 interview', 'kazan_freshair', '2.9'),
 ('Lumet, Making Movies', 'lumet_making', '2.9'),
 ('Television Academy interview, Sidney Lumet', 'lumet_tv', '2.9'),
 ('Judith Weston, Directing Actors', 'weston', '2.9'),
 ('East of Eden clip oEmbed', 'east_oembed', '2.9'),
 ('Stasser and Titus 1985, hidden profiles', 'hidden', '2.10'),
 ('Stasser and Titus 2003, hidden profiles history', 'hidden_history', '2.10'),
 ('Raven 1993, bases of power', 'raven', '2.10'),
 ('12 Angry Men clip oEmbed', 'angry_oembed', '2.10'),
 ('Flouri and Fitsakis 2007, 12 Angry Men negotiation', 'angry_negotiation', '2.10'),
 ('Forrester, B2B buying group roles', 'forrester', '2.10'),
 ('Gartner, buyer enablement', 'gartner', '2.10'),
 ('Pinker, Nowak and Lee 2008', 'pinker', '2.11'),
 ('Sacks, Schegloff and Jefferson 1974', 'sacks', '2.11'),
 ('Schegloff, Jefferson and Sacks 1977', 'repair', '2.11'),
 ('Pomerantz 1984', 'pomerantz', '2.11'),
 ('Mehrabian and Ferris 1967', 'mehrabian', '2.11'),
 ('Mehrabian, clarification of the 7, 38, 55 claim', 'mehrabian_site', '2.11'),
 ('Pinter, The echoing silence', 'pinter', '2.11'),
 ('The Dumb Waiter, Backstreet Box Productions, oEmbed verified', 'dumb_waiter', '2.11'),
 ('The Lives of Others opening scene, Qui Vive, oEmbed verified', 'lives', '2.11'),
 ('Meyer, The Culture Map', 'meyer', '2.12'),
 ('Hall, Beyond Culture', 'hall', '2.12'),
 ('Hall and Hall, Understanding Cultural Differences, chapter 1', 'hall_pdf', '2.12'),
 ('McSweeney 2002, Hofstede critique', 'hofstede', '2.12'),
 ('Brewer and Venaik 2014, ecological fallacy', 'brewer', '2.12'),
 ('Miller and Booker, Communication Modes, Kenyan', 'kenya', '2.12'),
 ('Zulu, Southern African and American business communication', 'south_africa', '2.12'),
 ('Peeters, Australian tall poppy norm', 'tall_poppy', '2.12'),
 ('Lost in Translation, Movieclips, oEmbed verified', 'lost', '2.12'),
 ('Moneyball meeting, Matthew Lahey, oEmbed verified', 'moneyball', '2.13'),
 ('Lewis, Moneyball', 'moneyball_book', '2.13')]

INTRO = {'lede': 'File 1 taught you to put the light on other people. File 2 teaches you to read what you see once the light is on: the want under the '
         'stated want, the room under the room, and the words nobody says out loud.',
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
            'now': True},
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
            'now': False},
           {'n': 5,
            'title': 'The Line',
            'stops': '2.31 to 2.34',
            'note': 'Influence vs manipulation, Belfort, Barry Seal, the mask.',
            'href': '#m2-31',
            'c': 'var(--red)',
            'now': False}],
 'coverage': '<p><b>What File 2 covers.</b> 6 stops, 43 sources, every scene oEmbed-verified on 27 Oct 2026.</p><ul><li><b>2.8</b> The hungers, '
             "rebuilt: what does this person actually want?</li><li><b>2.9</b> The director's read: how Kazan and Lumet read "
             "actors</li><li><b>2.10</b> Reading a group: who really decides?</li><li><b>2.11</b> Subtext: reading what isn't "
             'said</li><li><b>2.12</b> Reading across cultures</li><li><b>2.13</b> Boss fight: read a real meeting</li></ul>'}

SVG = {'2.8': '<svg class="p2fig" viewBox="0 0 1000 360" role="img" aria-label="Motivation map: stated want outside, unmet need underneath, observable '
        'test at the bottom"><defs><marker id="p2a28" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" '
        'markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#151515"/></marker><marker id="p2m28" viewBox="0 0 10 10" '
        'refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" '
        'fill="#ED691D"/></marker></defs><text class="t" x="500" y="30" text-anchor="middle">THE READ IS A HYPOTHESIS, NOT A LABEL</text><rect '
        'class="bx" x="55" y="62" width="260" height="82" rx="12"/><text class="t" x="75" y="92">STATED WANT</text><text class="ts" x="75" '
        'y="120">more traffic, more money</text><rect class="bj" x="370" y="62" width="260" height="82" rx="12"/><text class="t" x="390" '
        'y="92">DEEPER MOTIVE</text><text class="ts" x="390" y="120">status, control, belonging</text><rect class="bm" x="685" y="62" width="260" '
        'height="82" rx="12"/><text class="t tm" x="705" y="92">NEED UNDER IT</text><text class="ts" x="705" y="120">autonomy, competence, '
        'trust</text><path class="ln" d="M315 103 L365 103" marker-end="url(#p2a28)"/><path class="lm" d="M630 103 L680 103" '
        'marker-end="url(#p2m28)"/><path class="lr" d="M500 180 L500 248"/><rect class="bx" x="180" y="248" width="640" height="70" rx="12"/><text '
        'class="t" x="500" y="278" text-anchor="middle">TEST IT</text><text class="ts" x="500" y="302" text-anchor="middle">Ask what would change, '
        'then watch which tradeoff they refuse</text><text class="ts tr" x="500" y="348" text-anchor="middle">A motive predicts a choice. A '
        'stereotype predicts a person.</text></svg>',
 '2.9': '<svg class="p2fig" viewBox="0 0 1000 350" role="img" aria-label="Directing read: script circumstance becomes an actor action, adjusted to '
        'the actor, then protected by the director"><defs><marker id="p2a29" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" '
        'markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#151515"/></marker><marker id="p2m29" '
        'viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path '
        'd="M0,0 L10,5 L0,10 z" fill="#ED691D"/></marker></defs><rect class="bx" x="40" y="60" width="250" height="86" rx="12"/><text class="t" '
        'x="60" y="92">1 SCRIPT</text><text class="ts" x="60" y="120">What does the character need now?</text><rect class="bj" x="375" y="60" '
        'width="250" height="86" rx="12"/><text class="t" x="395" y="92">2 ACTOR</text><text class="ts" x="395" y="120">What makes this person '
        'alive?</text><rect class="bm" x="710" y="60" width="250" height="86" rx="12"/><text class="t tm" x="730" y="92">3 ACTION</text><text '
        'class="ts" x="730" y="120">A playable task, not a result</text><path class="ln" d="M290 103 L370 103" marker-end="url(#p2a29)"/><path '
        'class="lm" d="M625 103 L705 103" marker-end="url(#p2m29)"/><path class="lr" d="M165 190 L835 190"/><circle class="bk" cx="165" cy="190" '
        'r="13"/><circle class="bj" cx="500" cy="190" r="13"/><circle class="bm" cx="835" cy="190" r="13"/><text class="t" x="165" y="228" '
        'text-anchor="middle">KAZAN</text><text class="ts" x="165" y="250" text-anchor="middle">find the spine</text><text class="t" x="500" y="228" '
        'text-anchor="middle">LUMET</text><text class="ts" x="500" y="250" text-anchor="middle">make actors safe</text><text class="t tm" x="835" '
        'y="228" text-anchor="middle">WESTON</text><text class="ts" x="835" y="250" text-anchor="middle">give an action</text><text class="ts" '
        'x="500" y="310" text-anchor="middle">Read the need before you give the note.</text></svg>',
 '2.10': '<svg class="p2fig" viewBox="0 0 1000 390" role="img" aria-label="Room map: official authority, expertise, information and coalition '
         'support converge on the real decision"><defs><marker id="p2a210" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" '
         'markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#151515"/></marker><marker id="p2m210" '
         'viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path '
         'd="M0,0 L10,5 L0,10 z" fill="#ED691D"/></marker></defs><text class="t" x="500" y="28" text-anchor="middle">WHO CAN MOVE THE '
         'DECISION?</text><rect class="bx" x="35" y="68" width="210" height="74" rx="12"/><text class="t" x="55" y="98">TITLE</text><text class="ts" '
         'x="55" y="124">legitimate power</text><rect class="bj" x="270" y="68" width="210" height="74" rx="12"/><text class="t" x="290" '
         'y="98">KNOWLEDGE</text><text class="ts" x="290" y="124">expert power</text><rect class="bm" x="505" y="68" width="210" height="74" '
         'rx="12"/><text class="t tm" x="525" y="98">DATA</text><text class="ts" x="525" y="124">informational power</text><rect class="bx" x="740" '
         'y="68" width="225" height="74" rx="12"/><text class="t" x="760" y="98">TRUST</text><text class="ts" x="760" y="124">referent '
         'power</text><path class="ln" d="M140 142 L140 214 L455 214"/><path class="ln" d="M375 142 L375 214"/><path class="lm" d="M610 142 L610 214 '
         'L545 214" marker-end="url(#p2m210)"/><path class="ln" d="M852 142 L852 214 L655 214"/><rect class="bj" x="350" y="214" width="300" '
         'height="72" rx="12"/><text class="t" x="500" y="244" text-anchor="middle">COALITION</text><text class="ts" x="500" y="268" '
         'text-anchor="middle">champion plus economic buyer</text><text class="ts tr" x="500" y="332" text-anchor="middle">Map eyes, interruptions, '
         'questions and vetoes in the first 5 minutes.</text><text class="ts" x="500" y="362" text-anchor="middle">Talk time is a clue. Permission '
         'to close is the test.</text></svg>',
 '2.11': '<svg class="p2fig" viewBox="0 0 1000 360" role="img" aria-label="Reading subtext: words, timing and relationship create a provisional '
         'inference"><defs><marker id="p2a211" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" '
         'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#151515"/></marker><marker id="p2m211" viewBox="0 0 10 10" refX="9" '
         'refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" '
         'fill="#ED691D"/></marker></defs><text class="t" x="40" y="34">WHAT YOU HEAR</text><text class="t tm" x="380" y="34">WHAT IT MAY '
         'DO</text><text class="t" x="730" y="34">YOUR NEXT MOVE</text><rect class="bx" x="30" y="58" width="270" height="74" rx="12"/><text '
         'class="tb" x="48" y="88">WORDS</text><text class="ts" x="48" y="113">literal content, choice of detail</text><rect class="bj" x="365" '
         'y="58" width="300" height="74" rx="12"/><text class="tb" x="383" y="88">INDIRECT INTENT</text><text class="ts" x="383" y="113">request, '
         'face, deniability</text><rect class="bx" x="730" y="58" width="235" height="74" rx="12"/><text class="tb" x="748" '
         'y="88">HYPOTHESIS</text><text class="ts" x="748" y="113">ask, do not convict</text><path class="ln" d="M304 95 L355 95" '
         'marker-end="url(#p2a211)"/><path class="lm" d="M669 95 L720 95" marker-end="url(#p2m211)"/><rect class="bx" x="30" y="176" width="270" '
         'height="74" rx="12"/><text class="tb" x="48" y="206">TIMING</text><text class="ts" x="48" y="231">pause, overlap, repair</text><rect '
         'class="bj" x="365" y="176" width="300" height="74" rx="12"/><text class="tb" x="383" y="206">SEQUENCE</text><text class="ts" x="383" '
         'y="231">who yields, who fixes, who closes</text><rect class="bx" x="730" y="176" width="235" height="74" rx="12"/><text class="tb" x="748" '
         'y="206">CHECK</text><text class="ts" x="748" y="231">"Did I get that right?"</text><path class="ln" d="M304 213 L355 213" '
         'marker-end="url(#p2a211)"/><path class="lm" d="M669 213 L720 213" marker-end="url(#p2m211)"/><rect class="bm" x="190" y="285" width="620" '
         'height="48" rx="12"/><text class="t tm" x="500" y="315" text-anchor="middle">SUBTEXT IS A TESTABLE READ, NOT A MIND-READING '
         'LICENSE</text></svg>',
 '2.12': '<svg class="p2fig" viewBox="0 0 1000 390" role="img" aria-label="Culture map: a market cue is a starting hypothesis, then individual and '
         'organisation context correct it"><defs><marker id="p2a212" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" '
         'markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#151515"/></marker><marker id="p2m212" '
         'viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path '
         'd="M0,0 L10,5 L0,10 z" fill="#ED691D"/></marker></defs><text class="t" x="55" y="34">START WITH THE MAP</text><text class="t tm" x="570" '
         'y="34">THEN READ THIS PERSON</text><rect class="bj" x="40" y="60" width="410" height="245" rx="14"/><text class="tb" x="65" '
         'y="94">CULTURAL LENS</text><text class="ts" x="65" y="128">communicating: low to high context</text><text class="ts" x="65" '
         'y="154">evaluating: direct to indirect feedback</text><text class="ts" x="65" y="180">persuading: principles to applications</text><text '
         'class="ts" x="65" y="206">leading, deciding, trusting</text><text class="ts" x="65" y="232">disagreeing, scheduling</text><text class="ts '
         'tm" x="65" y="275">A compass, never a verdict</text><rect class="bx" x="535" y="60" width="420" height="245" rx="14"/><text class="tb" '
         'x="560" y="94">FOUR CORRECTIONS</text><text class="ts" x="560" y="128">individual: this person may differ</text><text class="ts" x="560" '
         'y="154">organisation: startup, lodge, ministry</text><text class="ts" x="560" y="180">role: founder, junior, buyer, guest</text><text '
         'class="ts" x="560" y="206">moment: deadline, trust, language</text><text class="ts" x="560" y="250">ask: "How do decisions get made '
         'here?"</text><text class="ts tm" x="560" y="275">Revise your read out loud</text><path class="lm mv" d="M460 180 L525 180" '
         'marker-end="url(#p2m212)"/><text class="ts tm" x="492" y="165" text-anchor="middle">update</text></svg>',
 '2.13': '<svg class="p2fig" viewBox="0 0 1000 420" role="img" aria-label="Boss fight meeting read: stated problem, hungers, power, subtext, '
         'culture, decision"><defs><marker id="p2a213" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" '
         'markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#151515"/></marker><marker id="p2m213" viewBox="0 0 10 '
         '10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M0,0 L10,5 '
         'L0,10 z" fill="#ED691D"/></marker></defs><text class="t" x="40" y="34">MEETING SIGNAL</text><text class="t tm" x="365" y="34">READ IT AS A '
         'SYSTEM</text><text class="t" x="735" y="34">RESPOND</text><rect class="bx" x="25" y="60" width="280" height="62" rx="10"/><text class="tb" '
         'x="42" y="88">STATED PROBLEM</text><text class="ts" x="42" y="108">What are we deciding?</text><rect class="bj" x="350" y="60" width="300" '
         'height="62" rx="10"/><text class="tb" x="367" y="88">HUNGER</text><text class="ts" x="367" y="108">status, safety, control, '
         'belonging</text><rect class="bx" x="695" y="60" width="280" height="62" rx="10"/><text class="tb" x="712" y="88">NAME THE NEED</text><text '
         'class="ts" x="712" y="108">fact, fear, or face?</text><path class="ln" d="M309 91 L340 91" marker-end="url(#p2a213)"/><path class="lm" '
         'd="M654 91 L685 91" marker-end="url(#p2m213)"/><rect class="bx" x="25" y="154" width="280" height="62" rx="10"/><text class="tb" x="42" '
         'y="182">TALK TIME</text><text class="ts" x="42" y="202">who interrupts, who waits</text><rect class="bj" x="350" y="154" width="300" '
         'height="62" rx="10"/><text class="tb" x="367" y="182">POWER MAP</text><text class="ts" x="367" y="202">authority, expertise, '
         'coalition</text><rect class="bx" x="695" y="154" width="280" height="62" rx="10"/><text class="tb" x="712" y="182">CREATE A '
         'TURN</text><text class="ts" x="712" y="202">invite the quiet expert</text><path class="ln" d="M309 185 L340 185" '
         'marker-end="url(#p2a213)"/><path class="lm" d="M654 185 L685 185" marker-end="url(#p2m213)"/><rect class="bx" x="25" y="248" width="280" '
         'height="62" rx="10"/><text class="tb" x="42" y="276">WORDS</text><text class="ts" x="42" y="296">euphemism, certainty, repair</text><rect '
         'class="bj" x="350" y="248" width="300" height="62" rx="10"/><text class="tb" x="367" y="276">SUBTEXT + CULTURE</text><text class="ts" '
         'x="367" y="296">face, directness, context</text><rect class="bm" x="695" y="248" width="280" height="62" rx="10"/><text class="tb" x="712" '
         'y="276">DECISION</text><text class="ts" x="712" y="296">owner, next test, date</text><path class="ln" d="M309 279 L340 279" '
         'marker-end="url(#p2a213)"/><path class="lm" d="M654 279 L685 279" marker-end="url(#p2m213)"/><text class="ts tm" x="500" y="365" '
         'text-anchor="middle">Do not only read the loudest person. Read the room that lets the loudest person win.</text></svg>'}

STOPS = [{'id': '2.8',
  'day': 20,
  'title': 'The hungers, rebuilt: what does this person actually want?',
  'why': 'The owner says she wants a new website. Ten minutes later she is still talking about the last agency that made her feel foolish. The '
         'visible want is a purchase; the live want may be control, competence, status, belonging or trust. Read the tradeoff, not the slogan.',
  'dossier': {'k': 'Subject',
              'name': 'Chris Voss',
              'role': 'Former FBI negotiator and author of Never Split the Difference',
              'facts': [('Known for', 'Turning a stated position into the need underneath it'),
                        ('The move', 'Name the hunger, then test it'),
                        ('Steal it for', 'MTRX discovery calls, pricing and scope conversations')],
              'stamp': ('hold', 'Holds up')},
  'cold': {'q': 'A prospect says the goal is more website traffic. Which question is the fastest route to the real want: What pages do you want? '
                'What would more traffic let you do? or What is your budget? Pick one and rate confidence from 1 to 5.',
           'a': '<b>What would more traffic let you do?</b> The first answer is a stated outcome, not a motive. The second invites a consequence: '
                'independence, proof of competence, status with a partner, or control of the pipeline. Treat it as a hypothesis and ask what would '
                'change if the answer arrived tomorrow.'},
  'story': ['A person can want the same object for five different reasons. A clinic owner may say website because it is the safe noun in the room. '
            'She may actually want to stop being embarrassed in front of a daughter, prove that she can compete with the larger clinic, regain '
            'control after an agency disappeared, or belong to the kind of business owner she imagines herself becoming.',
            'Start with Deci and Ryan, not with a pyramid. Self determination theory gives three psychological nutrients: autonomy, competence and '
            'relatedness. Autonomy is the feeling that I am choosing. Competence is the feeling that I can act effectively. Relatedness is the '
            'feeling that I matter to and with other people. A price, feature or pitch is attractive when it feeds one of these, and threatening '
            'when it takes one away.',
            "Then add Susan Fiske's five core social motives, often remembered as BUC(k)ET: belong, understand, control, enhance self and trust. "
            "Status belongs in the map, but not as a synonym for money or power. Anderson, Hildreth and Howland's review defines status as respect, "
            'admiration and voluntary deference, and argues it is a distinct fundamental motive. A person may want belonging and still want to '
            'outrank the room.',
            'Maslow is useful as cultural furniture and dangerous as a staircase. Bridgman, Cummings and Ballard show that Maslow never drew the '
            'famous pyramid, that the hierarchy has received little empirical support, and that the pyramid was a later presentation device. Your '
            'replacement is dynamic: ask which need is threatened now, listen for the tradeoff, then test the prediction with a small choice. '
            'Sheldon and Gunz add an important complication: unmet needs can arouse desire, but satisfaction does not make wanting vanish forever.'],
  'move': {'line': 'Hear the object. Find the hunger. Test the tradeoff.',
           'steps': [('Name the object.', 'What do they say they want: traffic, a quote, a role, a decision? Do not argue with it.'),
                     ('Ask for the consequence.',
                      'What would that give you, change for you, or let you stop worrying about? Listen for autonomy, competence, relatedness, '
                      'belonging, status or trust.'),
                     ('Offer a choice.',
                      'A real choice reveals the live motive: speed or control, polish or ownership, recognition or privacy. Never use the motive to '
                      'corner them.')]},
  'scenes': [{'id': 'lsotPuX6oxg',
              'title': 'Chris Voss: Tactical Empathy',
              'year': '2023',
              'who': 'Chris Voss',
              'role': 'real',
              'dur': '',
              'key': 'Tactical empathy and the need beneath the ask',
              'line': 'Voss explains the beat of hearing what the other person is trying to protect before proposing a solution.',
              'watch': ['He treats emotion as information, not as an obstacle to bulldoze',
                        "The question is aimed at the other person's world, not at winning a point",
                        'The negotiation stays legitimate: understanding is not permission to exploit'],
              'read': 'A stated demand is often a defence of a deeper need. The negotiator earns information by showing that the need has been '
                      'heard.',
              'steal': 'Ask what the result would change, then reflect the concern in plain language before discussing your offer.',
              'rc': 'A good label is not mind reading. Check it with the person, and accept correction.',
              'note': 'Content: negotiation examples and conflict discussion. Clip on Feisworld Media.'}],
  'specs': [('SDT: three psychological nutrients',
             'Autonomy, competence and relatedness are the needs Ryan and Deci identify as essential to motivation and well-being. A goal can be '
             'attractive while its pursuit feels controlled.'),
            ('Fiske: five social motives',
             'Belong, understand, control, enhance self and trust are broad motives for social life. They overlap, so use them as a listening map, '
             'not five sealed personality types.'),
            ('Status is not just money',
             'Anderson, Hildreth and Howland distinguish status from power, financial success and belonging. Respect and voluntary deference can be '
             'the prize.'),
            ('The pyramid is a presentation myth',
             'Maslow did not draw the pyramid. The later graphic made a flexible, weakly supported hierarchy look like a fixed staircase.')],
  'fig': ('2.8', 'Move from the noun on the surface to the need underneath, then make a small choice that could prove the read wrong.'),
  'evidence': [('Autonomy, competence and relatedness are basic psychological needs in SDT', 's', 'Ryan and Deci 2000', 'sdt'),
               ('Belong, understand, control, enhance self and trust are core social motives', 's', 'Stevens and Fiske', 'fiske'),
               ('Status is distinct from power, money and belonging', 's', 'Anderson, Hildreth and Howland 2015', 'status'),
               ('Maslow never created the pyramid and the hierarchy has little empirical support',
                's',
                'Bridgman, Cummings and Ballard 2019',
                'maslow'),
               ('Unmet needs can arouse corresponding desires', 'm', 'Sheldon and Gunz 2009', 'sheldon')],
  'tags': [('myth',
            'People climb a universal five-level pyramid in order.',
            'Use a moving map of needs. People can seek status while unsafe, autonomy while belonging, or competence while financially secure.',
            'maslow'),
           ('hold',
            'Status is only a disguised need to belong.',
            'Status and belonging can travel together, but the review treats status as a distinct motive: respect and deference are not identical to '
            'inclusion.',
            'status'),
           ('field',
            "A prospect's first noun is the whole truth about the purchase.",
            'Ask what the outcome would change, then offer a choice that tests the motive without pretending you can see inside someone.',
            'sdt')],
  'world': "On an MTRX call, write the client's stated want at the top of the page. Under it write three hypotheses: autonomy, competence, "
           'relatedness or status. Ask what the result would let them do that they cannot do now. If the answer is that they would finally stop '
           'depending on agencies, sell ownership and a handover plan, not only a prettier homepage.',
  'drill': {'name': 'The hunger ladder',
            'mins': '2 min',
            'steps': ['Write one stated want from a real call.',
                      'Write three possible needs underneath it, without choosing one yet.',
                      'Write one question and one tradeoff that could disconfirm each hypothesis.'],
            'mistake': 'Treating a motive label as a diagnosis. It is a question generator, not a verdict.'},
  'tryit': 'Choose one live client or friend. Ask what a desired result would change, then ask what they would choose if forced to trade speed, '
           'control, recognition and price. Record the answer and whether your first read changed.',
  'writer': "Give a character a public want and a private hunger, then make the private hunger choose the scene's tradeoff. A character who says she "
            'wants the job but refuses the credit may want belonging or autonomy more than the job itself.',
  'room': 'I do not ask what people want as if there is one answer. I ask what the result would change, then I test the read with a real choice.',
  'nextq': 'If a person cannot say the need plainly, how does a director discover it without humiliating the actor? Stop 2.9.',
  'checks': [{'q': 'Which question moves most directly from a stated outcome to a deeper motive?',
              'o': ['What exact pages do you want for launch?', 'What would the result let you do?', 'What colour and shape should the buttons be?'],
              'a': 1,
              'w': 'Consequences expose what the stated object is for. Treat the answer as a hypothesis and check it.'},
             {'q': 'Which is the SDT trio?',
              'o': ['Autonomy, competence and relatedness', 'Status, money and financial safety', 'Belonging, fairness and novelty seeking'],
              'a': 0,
              'w': 'Ryan and Deci identify autonomy, competence and relatedness as basic psychological needs.'},
             {'q': 'What is wrong with the familiar Maslow pyramid?',
              'o': ['Maslow never drew it and the fixed staircase lacks strong support in management teaching',
                    'Needs do not affect work or business decisions',
                    'People only want physical comfort before anything else'],
              'a': 2,
              'w': 'The pyramid was a later graphic. Use a dynamic needs map instead.'}]},
 {'id': '2.9',
  'day': 21,
  'title': "The director's read: how Kazan and Lumet read actors",
  'why': 'A bad director gives an actor an emotion: be sadder, be tougher, look natural. A good director notices the person in front of him, then '
         "offers a playable action that unlocks the scene. Elia Kazan read the actor's spine and history. Sidney Lumet read the fear underneath "
         "performance. Judith Weston turns that instinct into a usable language. Kevin, this is your director's stop.",
  'dossier': {'k': 'Subject',
              'name': 'Elia Kazan and Sidney Lumet',
              'role': 'Directors of East of Eden, On the Waterfront and 12 Angry Men',
              'facts': [('Known for', 'Different routes to truthful, actor-led performances'),
                        ('The move', 'Read the need before giving the note'),
                        ('Steal it for', 'Casting, rehearsal, writing subtext and directing your future films')],
              'stamp': ('hold', 'Holds up')},
  'cold': {'q': 'An actor keeps missing a simple emotional beat. Which note is most likely to help: Feel more rejected, Cry now, or Try to make your '
                'father accept this gift? Pick one and rate confidence from 1 to 5.',
           'a': '<b>Try to make your father accept this gift.</b> That is a playable action. It gives the actor something to do to another person. '
                "Emotion may arrive as a consequence. Result direction asks for the audience's response; an action gives the actor a task."},
  'story': ["Kazan's best actor note begins before the note. In the Fresh Air interview about his autobiography, he describes Marlon Brando as "
            "already carrying a deep supply of personality, memories and desires. Kazan told Brando the scene circumstance and the character's "
            'pressure, then got out of the way. With James Dean in East of Eden, he did the opposite: Dean was younger, less technically formed and '
            'personally unsettled, so Kazan stayed close, checked his condition and built a more intense relationship.',
            'That is not a contradiction. It is a read. Kazan recognised that Brando needed room and Dean needed a particular kind of containment. '
            'The famous Cal birthday scene works because the action is concrete: Cal tries to turn money into love, and his father rejects the '
            'transaction. The actor does not need a note saying be wounded. The blocked action produces the wound.',
            'Lumet gives Kevin a second model in Making Movies. He was an actor before becoming a director, and the Television Academy records his '
            'view that acting is painful because good work is self-revelation. His job was not to squeeze confession from an actor. It was to make '
            'the actor more secure and less afraid of releasing what the part required. His rehearsal practice, including concentrated table work, '
            'made the room safe enough for risk.',
            'Judith Weston supplies the guardrail: do not direct results, direct actions. Ask what the character is doing to the other person, what '
            'changes if it succeeds, and what obstacle makes the action urgent. For a future director, read three layers before speaking: what the '
            'script requires, what this actor can access today, and what playable verb will connect the two. Then protect the actor from notes that '
            'make them perform your idea of the audience response.'],
  'move': {'line': 'Read the actor. Find the action. Protect the risk.',
           'steps': [('Read the person in front of you.',
                      'Are they over-controlled, under-prepared, frightened, bored, technically brilliant or searching? Do not confuse a performance '
                      'problem with a character flaw.'),
                     ('Translate emotion into action.',
                      'Replace be angry with corner him, win her back, hide the evidence or make him stay. Give the actor an objective aimed at '
                      'someone.'),
                     ('Adjust the container.',
                      'Some actors need space, some need a clear image, some need repetition and safety. Give one note, run it, and watch the result '
                      'before adding another.')]},
  'scenes': [{'id': 'VfOrY7CidTA',
              'title': 'East of Eden: Give Me a Good Life',
              'year': '1955',
              'who': 'James Dean and Raymond Massey',
              'role': 'James Dean',
              'dur': '',
              'key': 'The rejected birthday gift · Cal and Adam Trask',
              'line': 'If you want to give me a present, give me a good life.',
              'watch': ["Cal tries to make a financial gift stand in for his father's love",
                        'Adam rejects the object and asks for a different kind of life',
                        'Dean moves between offering, pleading and nearly attacking without a note announcing the emotion'],
              'read': 'Kazan gives the actor an impossible action to play: make a father accept proof of love. The emotional temperature comes from '
                      'the blocked action.',
              'steal': "Write the playable verb before you write the emotion. Let the other person's refusal generate the feeling.",
              'rc': 'Film acting is edited and shaped by a director, writer and performer. A powerful take is not proof that one note caused every '
                    'detail.',
              'note': 'Content: parental rejection and emotional distress. Clip on Movieclips.'}],
  'specs': [('Result direction versus action',
             'Be sadder asks for an audience result. Make him forgive you gives the actor an action with an object and an obstacle, which is the '
             'language Weston recommends.'),
            ('Different actors need different containers',
             'Kazan describes giving Brando room while staying close to Dean. The general principle is adaptation, not a universal Method recipe.'),
            ('Safety makes risk possible',
             "Lumet's actor-director account treats security and fear reduction as practical directing tools, not soft extras."),
            ('The character spine',
             "Kazan's useful question is the pressure that runs through the scene: what does this person need from the other person now, and what "
             'will they do when refused?')],
  'fig': ('2.9',
          'A director moves from script circumstance to actor-specific support to a playable action. Emotion is the residue of pursuit and '
          'resistance.'),
  'evidence': [('Kazan adapted his direction to Brando and Dean', 's', 'Fresh Air transcript of Kazan interview', 'kazan_freshair'),
               ('Lumet connected directing to making actors feel secure and unafraid', 's', 'Television Academy interview', 'lumet_tv'),
               ('Making Movies presents directing as craft, decision and collaboration', 'm', 'Lumet, Making Movies', 'lumet_making'),
               ('Weston frames actor direction around action rather than result', 'm', 'Judith Weston, Directing Actors', 'weston'),
               ('The East of Eden scene makes the action legible before emotion', 's', 'East of Eden clip', 'east_clip')],
  'tags': [('anti',
            'Tell an actor the emotion you want to see.',
            'Give an action aimed at another character, then let refusal and stakes generate the emotion.',
            'weston'),
           ('hold',
            'Method directing means forcing actors to relive trauma.',
            'Kazan describes different relationships with Brando and Dean. Read the actor and protect a truthful, voluntary process.',
            'kazan_freshair'),
           ('field',
            'The best note is the cleverest note.',
            'One simple playable verb, one run, then observe. The director is responsible for the conditions, not for showing off interpretation.',
            'lumet_tv')],
  'world': 'For your first short film, do not tell a performer to look more guilty. Give her the action of getting the other person to believe her '
           'before the door opens Before the take, ask what the character wants from the other person. After the take, ask what the actor was trying '
           'to do. Your job is to compare those two maps, not to punish the gap.',
  'drill': {'name': 'The playable verb',
            'mins': '2 min',
            'steps': ['Take one emotional line from a script or film.',
                      'Write three actions aimed at another person: win, hide, corner, comfort or recruit.',
                      'Run the line three ways and note which action creates behaviour without forcing a result.'],
            'mistake': 'Giving five notes at once. One action, one run, one observation.'},
  'tryit': "Watch the East of Eden clip once for the father and once for Cal. Write each character's action in a verb phrase. Then write the one "
           "thing each cannot say. This is your director's first blocking map.",
  'writer': 'Directors reveal character by choosing the note they do not give. In a five-minute fiction drill, write an actor asking for an '
            'emotional result, then let the director replace it with a playable action. The scene should change without anyone naming the emotion.',
  'room': 'I do not direct tears or confidence. I give a person something urgent to do to another person, then make the room safe enough for the '
          'attempt.',
  'nextq': 'You can read one actor. In a room of twelve, how do you find the person who can actually move the decision? Stop 2.10.',
  'checks': [{'q': 'Which is a playable actor direction?',
              'o': ['Be much more visibly heartbroken in this take', 'Make your father accept this gift', 'Give the audience a bigger cry right now'],
              'a': 1,
              'w': 'An action has an object and an obstacle. Emotion can arrive through the attempt.'},
             {'q': 'Why did Kazan treat Brando and Dean differently?',
              'o': ['Every actor must use a different camera setup and visual style for each scene',
                    'He adapted to their needs, technique and condition',
                    'Dean was never allowed to improvise on set'],
              'a': 1,
              'w': 'The point is adaptive direction, not a single Method formula.'},
             {'q': "What does Lumet put under the director's responsibility?",
              'o': ['Make actors secure enough to risk self-revelation',
                    'Guarantee every take is perfect for the audience and critics',
                    'Keep actors from asking difficult questions'],
              'a': 0,
              'w': 'Lumet links good work with security and less fear, while accepting the pain of self-revelation.'}]},
 {'id': '2.10',
  'day': 22,
  'title': 'Reading a group: who really decides?',
  'why': 'In 12 Angry Men, eleven hands rise almost together. That looks like a decision until one calm dissenter asks the room to slow down. The '
         'majority has numbers, Juror 8 has process, Juror 3 has emotional investment, and the quiet old juror supplies a coalition. The real '
         'decider is not automatically the loudest, most senior or most certain person.',
  'dossier': {'k': 'Subject',
              'name': 'Juror 8 and the jury room',
              'role': '12 Angry Men, directed by Sidney Lumet, 1957',
              'facts': [('Known for', 'A lone dissent becoming a coalition without formal authority'),
                        ('The move', 'Map power, information and private stakes'),
                        ('Steal it for', 'MTRX pitches with owners, users, finance and implementers in one room')],
              'stamp': ('part', 'Partly')},
  'cold': {'q': 'You enter a six-person client meeting. Who is most likely to decide: the person speaking most, the person with the highest title, '
                'or the person everyone checks before committing? Choose one and rate confidence from 1 to 5.',
           'a': '<b>The person everyone checks before committing.</b> Talk time and title are clues, not proof. The test is behavioural: who can '
                'grant access, veto a plan, allocate money, translate objections or make the room wait? Observe before you pitch.'},
  'story': ['Lumet puts the whole decision in one hot room. The first vote in 12 Angry Men looks like consensus because common knowledge is '
            'abundant: the same witnesses, the same prosecution story, the same pressure to finish. Juror 8 does not claim to know the boy is '
            'innocent. He refuses to let the group confuse speed with certainty, and proposes a discussion before a life-changing verdict.',
            'That distinction is the hidden-profile problem. Stasser and Titus gave group members partial information about candidates. The group '
            'could have combined its unique clues and chosen the better candidate, but discussion favoured information everyone already shared and '
            'evidence that supported the initial preference. Groups often repeat what is socially easy to say. The crucial fact may be held by the '
            'quiet person whose fact has not yet become common.',
            "French and Raven give you a second map. Raven's review describes reward, coercive, legitimate, expert, referent and informational "
            'power. In the jury room, the foreman has formal legitimacy, Juror 8 brings information and process, Juror 3 brings emotional force and '
            'the threat of a coalition, and other jurors gain referent or expert weight as they contribute. Power is a resource someone can use, not '
            'a permanent personality trait.',
            'For an MTRX buying group, separate champion from economic buyer. The champion wants the change to happen and spends credibility '
            'carrying it internally. The economic buyer controls budget and accepts the business risk. A user may know the workflow, a technical '
            'gatekeeper may hold an informational veto, and a procurement person may control the final terms. In the first five minutes, map who '
            'asks, who is asked, who interrupts, who gets the answer, who can say no, and whose absence would stop the deal.'],
  'move': {'line': 'Map the room before you move the room.',
           'steps': [('Track the eyes.', 'When a question lands, who does everyone look at? Who looks away, and who looks at the clock?'),
                     ('Track the resources.',
                      'Mark title, expertise, information, relationships, budget, veto and implementation risk. One person may hold several.'),
                     ('Track the test.',
                      'Ask a neutral process question: who else needs to be comfortable, what is the approval path, and what would stop this? The '
                      'answer reveals the buying group.')]},
  'scenes': [{'id': '5xNlNV-UIUs',
              'title': '12 Angry Men: The First Voting',
              'year': '1957',
              'who': 'Henry Fonda and ensemble',
              'role': 'Henry Fonda',
              'dur': '',
              'key': 'The first vote and the lone holdout',
              'line': 'Juror 8 refuses to send a boy to die without talking about the case first.',
              'watch': ['The majority treats the first count as if it were proof',
                        'Juror 8 changes the process before trying to win the conclusion',
                        'A quiet juror eventually supplies support that changes the coalition'],
              'read': 'Juror 8 has no chairmanship and no special title. His power comes from process, information and a willingness to remain in '
                      'the room while others want speed.',
              'steal': 'When a group rushes, ask what has not yet been compared. Invite the unshared fact before presenting your answer.',
              'rc': 'The film is a dramatic ideal. A lone dissent does not usually flip a real jury, and a dissent can be wrong. The process lesson '
                    'is stronger than the hero myth.',
              'note': 'Content: murder case, prejudice and death penalty. Clip on Dusan Zivanovic.'}],
  'specs': [('Hidden profiles',
             'Groups discuss shared information more than unique information, so common knowledge can dominate even when the unshared clues would '
             'change the best decision.'),
            ('French and Raven power bases',
             'Reward, coercion, legitimate, expert, referent and informational power explain different routes to influence. Ask which resource is '
             'active here.'),
            ('Champion is not economic buyer',
             'A champion advocates internally. The economic buyer owns budget or business risk. They may be the same person, but never assume they '
             'are.'),
            ('Five-minute room map',
             'Record eyes, interruptions, questions, vetoes, approval path and implementation pain. The map is a working hypothesis, not a ranking '
             'of human worth.')],
  'fig': ('2.10',
          'A group decision is the convergence of several power bases. Titles start the map; eyes, information, vetoes and coalition behaviour '
          'finish it.'),
  'evidence': [('Groups repeat shared information and initial preferences', 's', 'Stasser and Titus 1985', 'hidden'),
               ('The hidden-profile effect has shaped later group-decision research', 'm', 'Stasser and Titus 2003', 'hidden_history'),
               ('Six bases of social power include reward, coercion, legitimate, expert, referent and informational', 's', 'Raven 1993', 'raven'),
               ('12 Angry Men depicts informal authority and coalition building', 'm', 'Flouri and Fitsakis 2007', 'angry_negotiation'),
               ('B2B buying groups separate champion, decision-maker, influencer, user and ratifier roles', 'm', 'Forrester', 'forrester')],
  'tags': [('myth',
            'The highest title is always the decision-maker.',
            'Watch who can approve, veto, fund, translate or make the room wait. Legitimate power is one base among six.',
            'raven'),
           ('myth',
            "A group decision pools everyone's information automatically.",
            'Ask for one fact each person knows that others may not. Hidden profiles show why the room otherwise recycles shared evidence.',
            'hidden'),
           ('field',
            'The person who likes your idea is the buyer.',
            'Ask who owns budget, who carries implementation risk, who champions the change and who can stop it. Build a clean multi-person path.',
            'forrester')],
  'world': 'In the first five minutes of a safari-lodge or clinic meeting, draw six initials. Beside each, mark title, user knowledge, budget, veto, '
           'implementation pain and champion energy. Ask who else needs to be comfortable before this can happen. If the enthusiastic marketing '
           'manager is your champion but the owner controls budget and the operations lead can veto the workflow, prepare three different proofs, '
           'not one generic pitch.',
  'drill': {'name': 'The five-minute room map',
            'mins': '2 min',
            'steps': ['From memory, draw the people in your last meeting and mark who looked at whom.',
                      'Give each person one power base: title, expertise, information, relationship, reward, coercion or budget.',
                      'Write one question that reveals the approval path without asking, "Who is the real boss?"'],
            'mistake': 'Confusing quiet with weak and loud with powerful. Power is what someone can change when resisted.'},
  'tryit': 'In your next group call, do not pitch for the first five minutes. Record who sets the topic, who asks for evidence, who receives '
           'answers, who names the risk, who is interrupted and who gets the final pause. Afterward ask your contact which role each person actually '
           'played.',
  'writer': 'Stage the room as a network of needs, not twelve equal talking heads. Give each person a resource and a private stake. Then let the '
            'protagonist change the coalition by surfacing a fact only one person knows. The camera can read power through eyelines before dialogue '
            'explains it.',
  'room': 'The decider is not always the loudest or highest. I watch who gets looked at, who can veto, who carries the risk and who can make the '
          'room wait.',
  'nextq': 'A group can hide facts from itself. Next, read what is said and what is meant in the gap between them. Stop 2.11.',
  'checks': [{'q': 'What is the hidden-profile trap?',
              'o': ['Groups discuss unique facts before shared facts, then compare them carefully',
                    'Groups always obey the quietest member in the room',
                    'Groups repeat shared facts and support initial preferences'],
              'a': 2,
              'w': 'Stasser and Titus found that common knowledge and initial preference can dominate discussion.'},
             {'q': 'Which statement best separates champion from economic buyer?',
              'o': ['The champion advocates internally; the economic buyer owns budget or business risk and final approval',
                    'The champion always has the highest title in the company and the biggest team',
                    'The economic buyer is only the daily user of the product and never funds it'],
              'a': 0,
              'w': 'Roles can overlap, but advocacy and financial authority are different jobs.'},
             {'q': 'What is the best first-five-minute signal of decision power?',
              'o': ['Who speaks longest and interrupts the most people',
                    'Who others check before committing',
                    'Who has the newest laptop and the most impressive setup'],
              'a': 1,
              'w': 'Eyes and commitment behaviour are stronger clues than talk time or props. Verify with the approval-path question.'}]},
 {'id': '2.11',
  'day': 23,
  'title': "Subtext: reading what isn't said",
  'why': 'A client says, "That is an interesting proposal," and then spends four seconds looking at the floor. Is it praise, a polite no, or a '
         'request for a cheaper version? The sentence is not the message. The message is the sentence, the pause, the relationship and what happens '
         'next.',
  'dossier': {'k': 'Subject',
              'name': 'The pause',
              'role': 'Indirect speech, conversation analysis and Pinteresque subtext',
              'facts': [('Known for', 'Meaning that survives the literal sentence'),
                        ('The move', 'Hear the gap, then test it'),
                        ('Steal it for', 'Client calls, scripts, negotiations, silence')],
              'stamp': ('hold', 'Holds up')},
  'cold': {'q': 'Pinker, Nowak and Lee give indirect speech a strategic advantage. Which one: it makes every request clearer, it gives plausible '
                'deniability, or it removes social risk? Pick one and rate your confidence.',
           'a': '<b>Plausible deniability.</b> An indirect request lets a cooperative listener accept the intended meaning while giving an '
                'uncooperative listener less direct evidence to attack. It is not automatically polite or safe. In a mixed cooperation and conflict '
                'relationship, it can protect face, probe the other person, or conceal a bad motive (Pinker, Nowak and Lee 2008).'},
  'story': ['A request can be a riddle with a payoff. Pinker, Nowak and Lee model why people say the side door thing instead of the thing itself: '
            'indirectness can let the listener cooperate without forcing either person to make the dangerous meaning fully public. A client saying, '
            '"It would be good to have this before the festival," may be asking for a deadline, testing your flexibility, or signalling that the '
            'budget is not the real constraint. The words leave room to retreat.',
            'Conversation analysis makes the invisible less mystical. Turn-taking is organised: who selects the next speaker, where a pause appears, '
            'whether someone overlaps, and how a speaker repairs a word all change the action. Preference organisation is not about liking. It is '
            'the pattern that makes agreement easier to produce than disagreement, so a disagreeing answer may arrive delayed, softened, or with a '
            'preface. Read sequence, not just vocabulary (Sacks, Schegloff and Jefferson; Pomerantz).',
            'The famous 7, 38, 55 rule is a useful myth to kill carefully. Mehrabian and Ferris studied how listeners inferred liking from single '
            'words such as like and dislike when vocal tone and facial expression conflicted. They did not measure all communication, truthfulness, '
            'business calls or ordinary conversation. Mehrabian himself says the formula applies to inconsistent messages about feelings and '
            'attitudes, not to communication in general. Words still matter, especially when you want the details of a proposal.',
            'Pinter gives the writer the cleanest image. His characters talk around the thing because the thing is dangerous. In <i>The Dumb '
            'Waiter</i>, two hitmen wait in a basement, exchange banalities and receive mysterious food orders. The silence is not empty: it is a '
            'contest over who knows what, who can ask, and who must obey. In <i>The Lives of Others</i> opening interrogation, the officer barely '
            'needs volume. Routine questions, repetition and controlled waiting make the room confess before the suspect does.'],
  'move': {'line': 'Hear the gap, then test it.',
           'steps': [('Quote the surface.', 'What did they literally say, without adding your theory?'),
                     ('Map the gap.', 'Note the pause, repair, omission, sequence and power at that moment.'),
                     ('Ask a reversible question.',
                      '"When you say interesting, do you mean the direction works, or should I change the budget?" Give them an easy correction.')]},
  'scenes': [{'id': 'nLwC5RonO_w',
              'title': 'The Dumb Waiter',
              'year': '2013',
              'who': 'Backstreet Box Productions',
              'role': 'real',
              'dur': '',
              'key': 'The basement waiting game · Pinter',
              'line': 'The two men keep talking around the job, while the pauses and the food orders reveal an authority neither names.',
              'watch': ['A banal question is allowed to hang instead of being answered',
                        'One character repairs or redirects rather than confronting the fear',
                        'The dumb waiter turns an unseen demand into pressure in the room'],
              'read': 'Pinteresque subtext is a power relation made audible through delay, evasion and the right to demand an answer.',
              'steal': 'Write the literal exchange first. Then annotate the sentence each character is trying not to say.',
              'rc': 'This is a full stage performance, not a naturalistic business call. Treat its silences as an exercise in attention, not a '
                    'universal lie detector.',
              'note': 'Content: implied violence, coercion and threat. Clip on Backstreet Box Productions.'},
             {'id': 'S7u6kE9emUs',
              'title': 'The Lives of Others',
              'year': '2006',
              'who': 'Ulrich Muhe and the Stasi interrogation team',
              'role': 'actor',
              'dur': '',
              'key': 'Opening interrogation · controlled silence',
              'line': 'The officer uses routine, repetition and waiting to make a suspect supply the story himself.',
              'watch': ['The question returns after the suspect has already answered',
                        'The officer controls the pace without theatrical shouting',
                        'A pause becomes pressure because the power difference is already known'],
              'read': 'The scene makes subtext structural: the stated question is about an alibi, while the real question is whether the institution '
                      'can force a person to doubt his own account.',
              'steal': 'Slow the scene at the point where the answer should be obvious. Let the audience hear who owns the silence.',
              'rc': 'The film compresses a political system into a precise dramatic encounter. Do not assume a quiet pause means guilt in a real '
                    'person.',
              'note': 'Content: state violence, interrogation and psychological coercion. Clip on Qui Vive.'}],
  'specs': [('Indirectness is strategic',
             'Pinker, Nowak and Lee argue that indirect requests can protect plausible deniability and negotiate the relationship, especially where '
             'cooperation and conflict coexist.'),
            ('Conversation is sequential',
             'Turn-taking, repair and preference organisation make timing meaningful. A delayed disagreement is a different social action from a '
             'blunt interruption, even when the proposition is the same.'),
            ('7, 38, 55 is narrow',
             'The original experiments concerned inferred liking from inconsistent verbal, vocal and facial cues in short stimuli. They do not '
             'license a universal percentage for communication or deception.'),
            ('Silence is evidence of work, not a verdict',
             'A pause can be searching, respectful, frightened, strategic or simply cognitive load. Use it to form a question, never a conviction.')],
  'fig': ('2.11', 'A read is strongest when the literal words, timing and relationship point in the same direction. When they do not, ask.'),
  'evidence': [('Indirect speech can create plausible deniability in mixed cooperation and conflict', 's', 'Pinker, Nowak and Lee 2008', 'pinker'),
               ('Turn-taking and repair are organised interactional practices',
                's',
                'Sacks, Schegloff and Jefferson 1974; Schegloff et al. 1977',
                'sacks'),
               ('7, 38, 55 came from narrow studies of inferred liking under inconsistency', 's', 'Mehrabian and Ferris 1967', 'mehrabian'),
               ('Pinter described the gap between spoken and unspoken language', 'm', 'Pinter, The echoing silence', 'pinter')],
  'tags': [('myth',
            '"93% of communication is nonverbal."',
            'That claim is a distorted cousin of a narrow Mehrabian result. In a real proposal, words carry the scope, price, dates and evidence. '
            'Read channels together.',
            'mehrabian_site'),
           ('hold',
            '"Indirect speech is just politeness."',
            'Partly. It can soften a request, but it can also manage dominance, protect deniability or hide a threat. Ask what the indirectness buys '
            'the speaker.',
            'pinker'),
           ('anti',
            '"A long pause means they are lying."',
            "No. A pause is a timing event. Compare it with the person's normal, the sequence and the stakes, then ask what needs more clarity.",
            'pinter')],
  'world': 'On an MTRX call, write two columns: <b>said</b> and <b>may be needed</b>. If a safari-lodge owner says, "The site is fine for now," do '
           'not answer the hidden sentence for them. Ask: "What would make it worth changing this season, and what would stop it?" You turn a guess '
           'into a design brief.',
  'drill': {'name': 'Subtext ledger',
            'mins': '2 min',
            'steps': ['Write one sentence you heard today exactly as said.',
                      'Mark the pause, repair, omission and power relation around it.',
                      'Write one neutral question that lets the speaker correct your read.'],
            'mistake': 'Treating your first inference as the truth. A read is a question with evidence attached.'},
  'tryit': 'Replay two minutes of a call or meeting with the sound on. Note one delayed answer and one repair. Ask the person later what the moment '
           'meant, without telling them your theory first.',
  'writer': 'Pinter does not put subtext in a secret explanation. He makes the audience feel the pressure of the missing sentence. Write a 12-line '
            'scene in which a client asks for a homepage, but the real request is reassurance. Do not let anyone name the fear.',
  'room': '"I do not translate a pause into a verdict. I write down what happened, then ask the question that lets the other person correct me."',
  'nextq': 'If the same sentence lands differently in another country, whose context did you assume? Stop 2.12.',
  'checks': [{'q': 'What did Mehrabian and Ferris actually study?',
              'o': ['Single words and liking cues',
                    'Business calls and lie detection across ordinary deals',
                    'All communication across cultures and every channel'],
              'a': 0,
              'w': 'The result concerns narrow attitude and liking judgments when channels conflict, not a general communication law.'},
             {'q': 'A client says "interesting" after a four-second pause. Best first move?',
              'o': ['Close the proposal immediately', 'Ask what to change', 'Assume rejection and stop'],
              'a': 1,
              'w': 'Keep the inference reversible. Ask a question that distinguishes praise, concern and budget.'},
             {'q': 'In Pinker, Nowak and Lee, why can indirectness help?',
              'o': ['It removes every conflict from the exchange', 'It guarantees agreement from the listener', 'It preserves deniability'],
              'a': 2,
              'w': 'Indirectness can let a cooperative listener accept the intent while leaving an adversarial listener less direct evidence.'}]},
 {'id': '2.12',
  'day': 24,
  'title': 'Reading across cultures',
  'why': 'The American client says, "I need your honest feedback," and the British partner answers, "It is not entirely without merit." One hears a '
         'soft yes. The other has delivered a careful no. Cross-cultural reading is not memorising stereotypes. It is learning which assumptions to '
         'test before you decide what the room meant.',
  'dossier': {'k': 'Subject',
              'name': 'The cultural lens',
              'role': 'Meyer, Hall, Hofstede and the individual in front of you',
              'facts': [('Known for', 'Invisible rules around meaning and trust'),
                        ('The move', 'Map, then ask'),
                        ('Steal it for', 'UK, US, East Africa, South Africa, Costa Rica, Australia')],
              'stamp': ('field', 'Field test')},
  'cold': {'q': "Erin Meyer's Culture Map has eight scales. Which response is the safest when you meet a new market: label the person by country, "
                'map a working hypothesis then ask, or ignore culture and rely on your own style? Pick one and rate your confidence.',
           'a': "<b>Map a hypothesis, then ask.</b> Meyer's scales are comparative tools for communicating, evaluating, persuading, leading, "
                'deciding, trusting, disagreeing and scheduling. They are not personality tests. Hall gives context as another lens, while Hofstede '
                'is useful history with serious limits. The individual, role and organisation still outrank your country stereotype.'},
  'story': ["Meyer's eight scales are not eight national essences. They are questions about relative expectations: how much is explicit in "
            'communicating; how feedback is delivered in evaluating; whether persuasion starts with principles or applications; how leaders lead; '
            'how decisions are made; how trust grows; how disagreement is shown; and how time is scheduled. A US founder can be high-context at '
            'home, a Kenyan manager can be direct with a trusted colleague, and a global hotel chain can teach one meeting style across six '
            'countries.',
            'Hall gives the shorter question: how much meaning sits in the surrounding relationship and situation rather than in the words? In '
            'low-context communication, more of the message is coded explicitly. In high-context communication, shared history, status, setting and '
            'timing do more of the work. This helps explain why UK understatement can be missed by a US listener, and why an American direct request '
            'can feel aggressive where relationship and face must be established first.',
            'For Kevin\'s markets, use local cues as hypotheses. In the UK, "not bad" may be warm approval and "quite a challenge" may be a serious '
            'warning. In the US, a clear ask, fast feedback and an explicit next step are often welcomed. In Kenya and Tanzania, relationship, '
            'status and trusted introductions can shape how business information moves; Kenyan communication research describes indirectness, '
            'stories and third-party communication in sensitive or status-marked situations. South African business rooms are not one thing, so ask '
            'which language, industry and history are in play. Costa Rica may reward rapport before a hard commercial push. Australia often combines '
            'directness with informal humour, and tall poppy norms can make conspicuous self-promotion land badly.',
            "Hofstede's dimensions can organise a first question, not settle an individual. The original work and later popular charts made country "
            'scores look like psychological coordinates. Critics point to assumptions in the data, weak measurement in some replications, and the '
            'ecological fallacy: a country-level average cannot be projected onto a person. The ethical read is simple: do not turn a map into a '
            'cage. Ask how this team gives feedback, who decides, what a no sounds like and how trust is earned here.',
            "The film version is <i>Lost in Translation</i>. Bob hears a Japanese director's long instruction reduced by the translator to a few "
            'short cues, then treats the gap as incompetence or comedy. The director is working through a high-context production relationship, '
            'hierarchy and performance language; Bob is expecting explicit, individual direction. The result is not that one culture cannot '
            'communicate. It is that both sides keep reading through their own default lens.'],
  'move': {'line': 'Map, then ask.',
           'steps': [('Choose one scale.', 'Before the call, pick the live variable: directness, trust, decision rights, or scheduling.'),
                     ('State the hypothesis lightly.',
                      '"I may be reading this through an American directness lens. How is feedback usually given on your team?"'),
                     ('Build a local rule together.',
                      'Confirm the channel, decision owner, deadline and meaning of a soft no. Write it down for the next call.')]},
  'scenes': [{'id': 'FiQnH450hPM',
              'title': 'Lost in Translation',
              'year': '2003',
              'who': 'Bill Murray, Hiroshi Katagiri and translator',
              'role': 'actor',
              'dur': '',
              'key': 'Suntory commercial shoot · translation gap',
              'line': 'Bob receives a long Japanese direction as a short English cue and cannot see the social and production context carrying the '
                      'rest.',
              'watch': ['The director gives more than the translation preserves',
                        'Bob asks for technical clarification while missing the performance relationship',
                        'Humour grows from two incompatible assumptions about what counts as clear'],
              'read': 'The misread is not simply language. It is context, hierarchy, role and expectations about explicit direction.',
              'steal': 'When a translation feels too short, ask what was compressed: decision, emotion, status or next action.',
              'rc': 'The film exaggerates culture shock for comedy and centres an American viewpoint. Use it to notice assumptions, not to '
                    'generalise about Japanese colleagues.',
              'note': 'Content: culture shock and workplace frustration. Clip on Movieclips.'}],
  'specs': [('Culture is comparative',
             "Meyer's dimensions describe relative positions between working cultures. The useful output is a question about a scale, not a label "
             'for a person.'),
            ('Context changes the payload',
             "Hall's high and low context distinction asks whether meaning is carried mostly in explicit words or in shared situation, relationship "
             'and timing.'),
            ('Country averages are not people',
             'Hofstede critiques highlight sampling, measurement and causal assumptions. Brewer and Venaik warn against projecting national-level '
             'correlations onto individuals or organisations.'),
            ('Markets need local hypotheses',
             'UK understatement, US directness, relationship-first East African business, South African plurality, Costa Rican rapport and '
             'Australian anti-boast norms are prompts for questions, not promises about every client.')],
  'fig': ('2.12', 'Use the map to choose what to ask. The person, role, organisation and moment revise the map.'),
  'evidence': [('Culture Map offers eight comparative business communication scales', 's', 'Meyer, The Culture Map', 'meyer'),
               ('High and low context describe where meaning is carried', 'm', 'Hall and Hall, Understanding Cultural Differences', 'hall_pdf'),
               ('National culture scores should not be projected onto individuals', 's', 'Brewer and Venaik 2014', 'brewer'),
               ('Kenyan communication can use indirectness, stories and third parties in status-marked situations',
                'm',
                'Miller and Booker, Communication Modes, Kenyan',
                'kenya'),
               ('Australian tall poppy is a documented communicative and behavioural norm', 'm', 'Peeters, Macquarie University', 'tall_poppy')],
  'tags': [('myth',
            '"Hofstede tells me what this person is like."',
            'Use Hofstede as historical context and a prompt. McSweeney and Brewer and Venaik show why national scores are not individual diagnoses.',
            'hofstede'),
           ('part',
            '"British understatement always means no."',
            'Often it can soften a no, but the individual, industry and relationship matter. Confirm the action: "Should I treat that as a hold, a '
            'no, or a request to revise?"',
            'meyer'),
           ('field',
            '"Relationship-first means avoid the business question."',
            'Wrong. Build enough trust to ask a clear business question, then make the decision path and next step explicit.',
            'kenya')],
  'world': 'For a Costa Rican lodge owner, do not open with a deck and a deadline. Start with the property, people and guest promise, then ask how '
           'decisions are made and who else should be involved. For a US caller, make the ask explicit. For a UK or Australian caller, leave room '
           'for understatement and humour, but confirm the action in writing. In Kenya or Tanzania, ask who should be in the conversation and invest '
           'in the relationship before treating a warm meeting as a closed deal.',
  'drill': {'name': 'Four-lens reset',
            'mins': '2 min',
            'steps': ['Name the likely culture cue without treating it as fact.',
                      'Add the individual, organisation and role as corrections.',
                      'Ask one question about feedback, trust or decisions and record the answer.'],
            'mistake': 'Using a country label to excuse poor listening. Cultural knowledge should make you more curious, not more certain.'},
  'tryit': 'Take one upcoming international call. Write your prediction for directness, trust and decision speed. During the call, mark one thing '
           'that confirms it and one thing that disconfirms it. Send the person a recap that checks the decision owner and date.',
  'writer': 'Cross-cultural conflict is dramatic when both characters are reasonable inside different rules. Write the same pitch twice: once as a '
            'US direct ask, once as a UK understatement. Let the other character misread both, then reveal the rule through a correction rather than '
            'exposition.',
  'room': '"A culture map tells me what to ask about. It does not tell me who the person is. I test the map, then I listen."',
  'nextq': 'You have read the sentence, the person and the culture. Can you read a whole room before it decides? Stop 2.13.',
  'checks': [{'q': 'What is the safest use of a culture framework?',
              'o': ['A testable starting hypothesis', 'A fixed personality diagnosis for this client', 'A replacement for asking direct questions'],
              'a': 0,
              'w': "Meyer's scales and Hall's context are maps. Individual, role and organisation can overturn the first read."},
             {'q': 'Why is Hofstede risky when applied to one client?',
              'o': ['Countries never differ in communication', 'Averages are not diagnoses', 'It measures only language and nothing else'],
              'a': 1,
              'w': 'The ecological fallacy warns against projecting country-level relationships onto people or organisations.'},
             {'q': 'A Kenyan partner is warm but has not signed. Best read?',
              'o': ['The deal is certainly dead already',
                    'Warmth proves the price is accepted without another step',
                    'Check relationship and decision path'],
              'a': 2,
              'w': 'Relationship can be a condition for business, not proof that the commercial decision is complete.'}]},
 {'id': '2.13',
  'day': 25,
  'title': 'Boss fight: read a real meeting',
  'why': "A meeting can sound like a discussion while already being a verdict. In the Oakland A's scouting room, Billy Beane asks what problem the "
         'team is actually solving. The scouts answer with names, reputations and stories. The fight is not just about baseball. It is about who '
         'gets to define reality.',
  'dossier': {'k': 'Subject',
              'name': 'The meeting',
              'role': "Moneyball, the Oakland A's scouts and Billy Beane",
              'facts': [('Known for', 'A room where expertise, status and evidence collide'),
                        ('The move', 'Read the system, not the loudest voice'),
                        ('Steal it for', 'MTRX strategy calls, client reviews, hiring and boards')],
              'stamp': ('hold', 'Holds up')},
  'cold': {'q': 'In a meeting, who has the most power: the person with the title, the person who speaks most, the person who controls the question, '
                'or the person who can stop the decision? Pick one and rate your confidence.',
           'a': '<b>It depends on the decision.</b> Title, airtime, expertise, coalition, agenda control and veto power can belong to different '
                'people. A reliable room read maps who can define the problem, who can block it, who is trusted, and who must live with the '
                'outcome.'},
  'story': ['Watch the Moneyball scouts meeting once as a baseball scene. Then watch it again as a power scene. The scouts talk about players '
            'through body, age, looks, confidence and old reputations. Billy is not merely disagreeing with their taste. He is trying to replace an '
            'inherited definition of value with a measurable question: what gets a player on base at the price Oakland can pay. The people defending '
            'the old read are defending status as much as method.',
            'Now run every File 2 tool. Hungers: the scouts want competence recognised, belonging protected and uncertainty reduced; Billy wants '
            "control over a decision that can save a season and his job. Director's read: the actors use interruption, stillness, glances and tempo "
            'to make power visible before anyone wins an argument. Group power map: Billy has formal authority, the scouts have distributed '
            'expertise and coalition pressure, and the unseen owner and roster create constraints.',
            'Subtext: a player description can be a proxy argument about who is qualified to judge. A compliment can be a veto. A joke can restore '
            'rank after a challenge. Culture: this is a US professional sports organisation with its own subculture, where direct argument, data and '
            'hierarchy collide. Do not call every conflict national culture. Industry culture, role and incentives are doing more work here.',
            'The useful director\'s question is not "Who is right?" It is "What changes when this person speaks?" Track the problem definition, the '
            'hunger beneath each intervention, the power map, the unsaid threat, the local rules and the decision owner. On the final pass, write '
            'one line for each: stated problem, hidden fear, coalition, evidence, next decision. That is a room read you can carry into an MTRX '
            'call.'],
  'move': {'line': 'Read the system, not the loudest voice.',
           'steps': [('Frame the decision.', 'Write the one sentence the room must decide, then notice who keeps changing it.'),
                     ('Map hungers and power.', 'For each speaker, note what they need protected, who they influence, and who can veto.'),
                     ('Close the loop.', 'Name the evidence, owner, next test and date. Invite the quiet expert before the decision hardens.')]},
  'scenes': [{'id': '_5KQDjrVHc8',
              'title': 'Moneyball',
              'year': '2011',
              'who': "Brad Pitt and Oakland A's scouts",
              'role': 'actor',
              'dur': '',
              'key': 'What is the problem? · scouts meeting',
              'line': 'Billy keeps returning the room to the problem it must solve while the scouts return to reputation, looks and familiar player '
                      'stories.',
              'watch': ['Who speaks first, who interrupts and who gets treated as the adult in the room',
                        'The scouts use vivid anecdotes while Billy changes the unit of analysis',
                        'A joke or dismissal protects status when the frame is challenged'],
              'read': 'Billy reads the meeting as an incentive system, not a neutral exchange of opinions. The group is protecting an old way of '
                      'knowing.',
              'steal': 'Before arguing for your solution, ask what problem the room believes it is solving. If the answers differ, that is the '
                       'meeting.',
              'rc': 'The film compresses the baseball history and makes Billy a dramatic centre. Use the scene to practise observation, not to copy '
                    'his aggression.',
              'note': 'Content: workplace conflict and dismissive language. Clip on Matthew Lahey.'}],
  'rewatch': True,
  'specs': [('A room has multiple hungers',
             "Use Stop 2.8's hunger tool: status, safety, control, belonging or meaning. The same objection can protect different needs."),
            ('Power is more than title',
             'Use the group power map from Stop 2.10: formal authority, expertise, airtime, coalition, agenda control and veto power can sit with '
             'different people.'),
            ('Directors read behaviour in sequence',
             "Use the director's read from Stop 2.9: baseline, change, objective, obstacle and tactic. Watch what changes after each line, not just "
             'the line itself.'),
            ('Culture is one layer',
             "Use Stop 2.12's map only after role, industry, organisation and decision stakes are visible. A sports scouting culture may explain "
             'this room better than a country score.')],
  'fig': ('2.13', 'A boss-fight read moves from the stated problem to hungers, power, subtext and culture, then returns to a concrete decision.'),
  'evidence': [('The Moneyball scene foregrounds problem definition and competing evaluation criteria',
                'm',
                'Moneyball meeting clip, oEmbed verified',
                'moneyball'),
               ("Moneyball is based on the Oakland A's use of evidence and constrained resources", 'm', 'Lewis, Moneyball', 'moneyball_book'),
               ('Hunger and group power are File 2 tools, not claims that the film is a laboratory',
                'h',
                'File 2 synthesis, grounded in the prior stops',
                'moneyball'),
               ('Culture frameworks should not replace role and organisation analysis', 's', 'Brewer and Venaik 2014', 'brewer')],
  'tags': [('hold',
            '"The loudest person is the leader."',
            'Airtime can be a tactic or a symptom. Track who frames the decision, controls resources and can veto the next step.',
            'moneyball'),
           ('myth',
            '"A data argument makes the room rational."',
            'Data can still threaten identity and status. Read the social action around the number: who introduces it, who translates it and who '
            'resists it.',
            'moneyball_book'),
           ('field',
            '"Read the whole room before you pitch."',
            'Use a one-page map: decision, hungers, power, subtext, culture, evidence, owner and date. Then test the map in the next meeting.',
            'brewer')],
  'world': 'Before your next MTRX strategy call, draw eight boxes: decision, client hunger, your hunger, formal owner, hidden veto, loudest '
           'coalition, quiet expert and next test. In a safari-lodge redesign, the owner may want bookings, the manager may fear disruption, the '
           'guide may know the guest reality and the finance lead may hold the veto. Ask each role one question before presenting your deck.',
  'drill': {'name': 'Meeting playback',
            'mins': '2 min',
            'steps': ['Watch three minutes with sound and mark who changes the frame.',
                      "Write each speaker's likely hunger and power, with a question mark.",
                      'Name the next decision, owner, evidence and date.'],
            'mistake': 'Explaining everyone psychologically without checking the decision mechanics. A room read must predict what happens next.'},
  'tryit': 'After one meeting today, write the eight-box map from memory. Send one follow-up question to the decision owner and one invitation to '
           'the quiet expert. Compare your prediction with what happens in the next meeting.',
  'writer': "A boardroom scene becomes alive when every line has two jobs: solve the stated problem and protect a person's position. Rewatch the "
            "Moneyball clip with the sound off, then with the dialogue only. Write the same meeting from the quiet expert's point of view, changing "
            'no spoken words.',
  'room': '"I do not only read the presenter. I read who needs what, who can block it, what the room is avoiding and what decision will prove me '
          'wrong."',
  'nextq': 'You have a read. File 3 asks what the room reads in you before you speak: voice, walk and presence.',
  'checks': [{'q': 'What is the first question in a boss-fight meeting read?',
              'o': ['Who is most charismatic and persuasive in the room?', 'What is the decision?', 'Who has the nicest title and longest tenure?'],
              'a': 1,
              'w': 'Frame the decision before interpreting motives. Otherwise you map a meeting without knowing what it can change.'},
             {'q': 'Billy Beane and the scouts mainly disagree about...',
              'o': ['Whether baseball exists as a professional sport', 'Who should speak first in this meeting', 'Player value'],
              'a': 2,
              'w': 'The conflict is over the evaluation frame: reputation and appearance versus the measurable problem Oakland must solve.'},
             {'q': 'Why set rewatch=True on this stop?',
              'o': ['Warm-up', 'To replace the evidence table with a film montage', 'To hide the meeting scene from the reader'],
              'a': 0,
              'w': 'The renderer adds every scene in this file as a warm-up before the final boss-fight read.'}]}]

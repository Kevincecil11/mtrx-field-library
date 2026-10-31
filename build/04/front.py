"""No. 04 content module front (normalised from drafts/04/front.py, 27 Oct 2026). Plain data; see drafts/FORMAT-04.md."""

COVER = {'title_html': 'Field guide to <span class="o">honest influence</span>',
 'sub': 'Sales and persuasion, mapped from rhetoric to repeatable trust.',
 'verbs': ['notice', 'question', 'earn'],
 'cube_caption': 'The honest levers that close deals: clarity, proof, real scarcity, real social proof.'}

HOW = {'why': 'Each day is one short, curated video followed by a compact insider layer. The point is not to collect tricks. It is to notice a '
        'mechanism, test the evidence, and make the next conversation clearer and safer for both sides.',
 'specs': [('Retrieval practice',
            'strong evidence',
            'Try the question before you watch. Pulling an answer from memory makes the video an investigation rather than background '
            'noise.'),
           ('Spacing',
            'strong',
            "Yesterday's question returns in small reviews. Forgetting a little, then rebuilding the answer, is the work."),
           ('Guess first',
            'moderate',
            'A wrong prediction gives the episode somewhere to land. Treat it as data, not a verdict on your intelligence.'),
           ('Interleaving',
            'moderate',
            'Persuasion and sales alternate. The contrast keeps you asking whether a claim is about a mind, a market, a process, or an '
            'ethical boundary.')],
 'cue': 'Pick one fixed moment, such as after morning chai and before Instagram. On a bad day, run rescue mode: one question and the '
        'video. Resume tomorrow without punishment.',
 'field_note': 'How to learn one field or both: 14 Persuasion days and 14 Sales days. The spine is a curated playlist of Crash Course '
               'episodes, university and TED talks, and film clips, not one series.'}

WEEKS = {1: ('Why people say yes',
     'Start with the boundary between influence and force, then meet the classic models of trust, processing, behaviour, and choice. By '
     'Sunday, you can name what a message is asking a person to do and what might make that request fair.'),
 2: ('Finding and opening',
     'Move from abstract influence to the first real conversation: choose a fit, earn attention, lower resistance, discover the buying '
     'process, and qualify without turning a person into a score.'),
 3: ('Value, story and price',
     'Learn to make an outcome legible, show proof, handle objections, price a service, and ask for a decision without manufacturing '
     'pressure. Stories become useful when they remain answerable to evidence.'),
 4: ('Negotiate, defend, keep',
     'Prepare alternatives, negotiate across power differences, defend against dark patterns, and build a repeatable system that keeps '
     'trust after the signature. The final question is what kind of persuader the system makes you.')}

MAPS = [{'id': 'map-per',
  'meta': 'Map 1',
  'title': "Persuasion's family tree",
  'why': 'Persuasion nests from situation to message to mind to behaviour. Rhetoric, attitude-change research, social influence, '
         'behavioural economics, narrative, resistance, and computational persuasion are branches of one larger question: what changes, '
         'for whom, by what route, at what cost?',
  'svg': '<svg viewBox="0 0 1000 430" role="img" aria-label="Persuasion family tree with five nested levels">\n'
         '<rect x="20" y="162" width="190" height="94" rx="16" class="s-box-j"></rect><text class="s-t-b" x="115" y="201" '
         'text-anchor="middle">PERSUASION</text><text class="s-t-sm" x="115" y="226" text-anchor="middle">voluntary influence</text>\n'
         '<path class="s-line" d="M210,209 L270,209" marker-end="url(#ah)"></path>\n'
         '<rect x="270" y="28" width="680" height="350" rx="18" class="s-card"></rect>\n'
         '<rect x="300" y="52" width="620" height="56" rx="10" class="s-box-a"></rect><text class="s-t-b" x="320" y="86">1 '
         'SITUATION</text><text class="s-t-sm" x="505" y="86">audience, timing, power, culture</text>\n'
         '<path class="s-line s-dash" d="M610,108 L610,128"></path>\n'
         '<rect x="320" y="128" width="580" height="56" rx="10" class="s-box-a"></rect><text class="s-t-b" x="340" y="162">2 MESSAGE + '
         'SOURCE</text><text class="s-t-sm" x="575" y="162">ethos, pathos, logos, proof, frame</text>\n'
         '<path class="s-line s-dash" d="M610,184 L610,204"></path>\n'
         '<rect x="340" y="204" width="540" height="56" rx="10" class="s-box-a"></rect><text class="s-t-b" x="360" y="238">3 '
         'PROCESSING</text><text class="s-t-sm" x="530" y="238">central, peripheral, heuristic, story</text>\n'
         '<path class="s-line s-dash" d="M610,260 L610,280"></path>\n'
         '<rect x="360" y="280" width="500" height="56" rx="10" class="s-box-j"></rect><text class="s-t-b" x="380" y="314">4 '
         'RESPONSE</text><text class="s-t-sm" x="535" y="314">attitude, intention, trust, action</text>\n'
         '<text class="s-t-sm" x="500" y="404" text-anchor="middle">Resistance and ethics cut across every level. AI scales every level, '
         'and scales its risks.</text>\n'
         '</svg>',
  'figcap': 'The field nests rather than stacks. A persuasive sales call is simultaneously a rhetorical situation, a source and message, a '
            'processing problem, and a decision with ethical consequences.'},
 {'id': 'map-sal',
  'meta': 'Map 2',
  'title': "Sales' family tree",
  'why': 'Sales is not a single closing trick. It is a buyer-centred process, with frameworks that name different parts of the same '
         'journey. Use a framework as a lens, not as a script that outranks evidence or consent.',
  'svg': '<svg viewBox="0 0 1000 430" role="img" aria-label="Sales family tree showing process and frameworks">\n'
         '<rect x="22" y="164" width="172" height="94" rx="16" class="s-box-j"></rect><text class="s-t-b" x="108" y="203" '
         'text-anchor="middle">SALES</text><text class="s-t-sm" x="108" y="228" text-anchor="middle">help a buyer decide</text>\n'
         '<path class="s-line" d="M194,211 L250,211" marker-end="url(#ah)"></path>\n'
         '<g>\n'
         '<rect x="250" y="32" width="700" height="58" rx="11" class="s-card"></rect><text class="s-t-b" x="272" y="67">1 FIND</text><text '
         'class="s-t-sm" x="400" y="67">ICP, segmentation, positioning, outreach</text>\n'
         '<rect x="250" y="102" width="700" height="58" rx="11" class="s-box-a"></rect><text class="s-t-b" x="272" y="137">2 '
         'DISCOVER</text><text class="s-t-sm" x="420" y="137">SPIN, Mom Test, MEDDICC, jobs to be done</text>\n'
         '<rect x="250" y="172" width="700" height="58" rx="11" class="s-card"></rect><text class="s-t-b" x="272" y="207">3 PROVE '
         'VALUE</text><text class="s-t-sm" x="455" y="207">demo, proof, proposal, ROI, risk reversal</text>\n'
         '<rect x="250" y="242" width="700" height="58" rx="11" class="s-box-j"></rect><text class="s-t-b" x="272" y="277">4 '
         'AGREE</text><text class="s-t-sm" x="410" y="277">price, BATNA, ZOPA, negotiation, next step</text>\n'
         '<rect x="250" y="312" width="700" height="58" rx="11" class="s-box-a"></rect><text class="s-t-b" x="272" y="347">5 '
         'KEEP</text><text class="s-t-sm" x="400" y="347">handoff, delivery, retention, referral, CRM</text>\n'
         '</g>\n'
         '<path class="s-line s-dash" d="M228,211 L250,61"></path><path class="s-line s-dash" d="M228,211 L250,131"></path><path '
         'class="s-line s-dash" d="M228,211 L250,201"></path><path class="s-line s-dash" d="M228,211 L250,271"></path><path class="s-line '
         's-dash" d="M228,211 L250,341"></path>\n'
         '<text class="s-t-sm" x="600" y="404" text-anchor="middle">The buyer can pause or leave at every stage. That is a feature of an '
         'honest process.</text>\n'
         '</svg>',
  'figcap': 'The process is sequential enough to manage, but not linear enough to force. Qualification and disqualification protect both '
            'sides; retention is part of selling, not an afterthought.'},
 {'id': 'map-time',
  'meta': 'Map 3',
  'title': 'Three lanes to 2026',
  'why': 'Influence was never only Greek or only modern. Read down a lane for one tradition, across the lanes for what was happening at '
         'the same time.',
  'svg': '<svg viewBox="0 0 1000 440" role="img" aria-label="Three lanes from ancient rhetoric and statecraft to 2026"><rect x="20" y="16" '
         'width="310" height="44" rx="10" class="s-card"></rect><text class="s-t" x="34" y="44">RHETORIC + SCIENCE</text><path '
         'class="s-line" d="M32,72 L32,412"></path><circle cx="32" cy="87" r="5" class="s-box-a"></circle><text class="s-t" x="48" '
         'y="92">c. 350 BCE · Aristotle</text><text class="s-t-sm" x="48" y="112">Rhetoric: ethos, pathos, logos</text><circle cx="32" '
         'cy="143" r="5" class="s-box-a"></circle><text class="s-t" x="48" y="148">1953 · Hovland, Yale</text><text class="s-t-sm" x="48" '
         'y="168">who says what to whom</text><circle cx="32" cy="199" r="5" class="s-box-a"></circle><text class="s-t" x="48" '
         'y="204">1979 · Kahneman, Tversky</text><text class="s-t-sm" x="48" y="224">prospect theory, loss aversion</text><circle cx="32" '
         'cy="255" r="5" class="s-box-a"></circle><text class="s-t" x="48" y="260">1984 · Cialdini</text><text class="s-t-sm" x="48" '
         'y="280">Influence (Unity added 2021)</text><circle cx="32" cy="311" r="5" class="s-box-a"></circle><text class="s-t" x="48" '
         'y="316">1986 · Petty, Cacioppo</text><text class="s-t-sm" x="48" y="336">the elaboration likelihood model</text><circle cx="32" '
         'cy="367" r="5" class="s-box-a"></circle><text class="s-t" x="48" y="372">2024 · AI dialogue studies</text><text class="s-t-sm" '
         'x="48" y="392">Costello, Pennycook, Rand</text><rect x="345" y="16" width="310" height="44" rx="10" class="s-box-j"></rect><text '
         'class="s-t" x="359" y="44">SELLING + NEGOTIATION</text><path class="s-line" d="M357,72 L357,412"></path><circle cx="357" cy="87" '
         'r="5" class="s-box-a"></circle><text class="s-t" x="373" y="92">1880s · Patterson, NCR</text><text class="s-t-sm" x="373" '
         'y="112">territories, training, the Primer</text><circle cx="357" cy="143" r="5" class="s-box-a"></circle><text class="s-t" '
         'x="373" y="148">1898 · St. Elmo Lewis</text><text class="s-t-sm" x="373" y="168">AIDA</text><circle cx="357" cy="199" r="5" '
         'class="s-box-a"></circle><text class="s-t" x="373" y="204">1936 · Dale Carnegie</text><text class="s-t-sm" x="373" y="224">How '
         'to Win Friends</text><circle cx="357" cy="255" r="5" class="s-box-a"></circle><text class="s-t" x="373" y="260">1981 · Fisher '
         'and Ury</text><text class="s-t-sm" x="373" y="280">Getting to Yes, BATNA</text><circle cx="357" cy="311" r="5" '
         'class="s-box-a"></circle><text class="s-t" x="373" y="316">1988 · Rackham, SPIN</text><text class="s-t-sm" x="373" '
         'y="336">35,000 observed sales calls</text><circle cx="357" cy="367" r="5" class="s-box-a"></circle><text class="s-t" x="373" '
         'y="372">2011 · Challenger, Ross</text><text class="s-t-sm" x="373" y="392">insight selling, SDR teams</text><rect x="670" y="16" '
         'width="310" height="44" rx="10" class="s-box-a"></rect><text class="s-t" x="684" y="44">INDIA + CHINA</text><path class="s-line" '
         'd="M682,72 L682,412"></path><circle cx="682" cy="87" r="5" class="s-box-j"></circle><text class="s-t" x="698" y="92">d. 233 BCE '
         '· Han Feizi</text><text class="s-t-sm" x="698" y="112">the difficulties of persuasion</text><circle cx="682" cy="143" r="5" '
         'class="s-box-j"></circle><text class="s-t" x="698" y="148">c. 2nd BCE to 3rd CE</text><text class="s-t-sm" x="698" '
         'y="168">Arthashastra: four upayas</text><circle cx="682" cy="199" r="5" class="s-box-j"></circle><text class="s-t" x="698" '
         'y="204">c. 2nd century CE</text><text class="s-t-sm" x="698" y="224">Nyaya Sutra: vada, jalpa, vitanda</text><circle cx="682" '
         'cy="255" r="5" class="s-box-j"></circle><text class="s-t" x="698" y="260">1600s on · merchant firms</text><text class="s-t-sm" '
         'x="698" y="280">Gujarati, Marwari credit (sakh)</text><circle cx="682" cy="311" r="5" class="s-box-j"></circle><text class="s-t" '
         'x="698" y="316">1930 · Gandhi, Salt March</text><text class="s-t-sm" x="698" y="336">satyagraha as persuasion</text><circle '
         'cx="682" cy="367" r="5" class="s-box-j"></circle><text class="s-t" x="698" y="372">2023 · India CCPA</text><text class="s-t-sm" '
         'x="698" y="392">13 dark patterns prohibited</text><text class="s-t-sm" x="500" y="434" text-anchor="middle">Dates are anchors, '
         'not one straight line of progress. Ancient dates are scholarly ranges.</text></svg>',
  'figcap': 'Three lanes, one long problem: how to move a person or group without confusing counsel, exchange, pressure, and force. The '
            'modern science inherits more than one history.'},
 {'id': 'map-meet',
  'meta': 'Map 4',
  'title': 'Where persuasion and sales meet',
  'why': 'The shared questions are practical and moral: who is this for, what do they know, what risk do they carry, what evidence would '
         'change their mind, and can they say no without penalty?',
  'svg': '<svg viewBox="0 0 1000 390" role="img" aria-label="Shared questions where persuasion and sales meet">\n'
         '<rect x="35" y="42" width="350" height="270" rx="18" class="s-box-a"></rect><rect x="615" y="42" width="350" height="270" '
         'rx="18" class="s-box-j"></rect>\n'
         '<text class="s-t-b" x="210" y="78" text-anchor="middle">PERSUASION</text><text class="s-t-b" x="790" y="78" '
         'text-anchor="middle">SALES</text>\n'
         '<text class="s-t-sm" x="62" y="120">attitude and belief</text><text class="s-t-sm" x="62" y="153">message and source</text><text '
         'class="s-t-sm" x="62" y="186">processing and resistance</text><text class="s-t-sm" x="62" y="219">autonomy and ethics</text>\n'
         '<text class="s-t-sm" x="642" y="120">fit and problem</text><text class="s-t-sm" x="642" y="153">proof and buyer risk</text><text '
         'class="s-t-sm" x="642" y="186">price and alternatives</text><text class="s-t-sm" x="642" y="219">delivery and trust '
         'repair</text>\n'
         '<rect x="395" y="90" width="210" height="174" rx="16" class="s-card"></rect><text class="s-t-b" x="500" y="123" '
         'text-anchor="middle">SHARED</text><text class="s-t-sm" x="500" y="155" text-anchor="middle">Who?</text><text class="s-t-sm" '
         'x="500" y="180" text-anchor="middle">Why now?</text><text class="s-t-sm" x="500" y="205" text-anchor="middle">What would '
         'count?</text><text class="s-t-sm" x="500" y="230" text-anchor="middle">Can they say no?</text>\n'
         '<path class="s-line" d="M385,145 L395,145" marker-end="url(#ah)"></path><path class="s-line" d="M615,145 L605,145" '
         'marker-end="url(#ah)"></path>\n'
         '<text class="s-t-sm" x="500" y="350" text-anchor="middle">A good sales conversation is a small, reversible experiment in shared '
         'understanding.</text>\n'
         '</svg>',
  'figcap': 'The overlap is not a bag of influence tricks. It is a discipline of fit, evidence, consent, and next steps.',
  'extra_html': '<div class="stats"><div class="stat"><b>61%</b><span>B2B buyers preferred an overall rep-free buying '
                'experience.</span><small>Gartner, 2025, vendor survey: '
                'https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience</small></div><div '
                'class="stat"><b>73%</b><span>B2B buyers actively avoided irrelevant outreach.</span><small>Gartner, 2025, vendor survey: '
                'https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience</small></div><div '
                'class="stat"><b>69%</b><span>B2B buyers reported inconsistencies between a sales website and '
                'sellers.</span><small>Gartner, 2025, vendor survey: '
                'https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience</small></div><div '
                'class="stat"><b>81.2%</b><span>Increase in odds of greater agreement for personalised GPT-4 debate opponents in one '
                'study.</span><small>Salvi et al., Nature Human Behaviour, 2025: '
                'https://doi.org/10.1038/s41562-025-02194-6</small></div></div><p class="room">"Make the claim checkable, the next step '
                'reversible, and the no safe."</p>'},
 {'id': 'coverage',
  'meta': 'Map 6',
  'title': 'The coverage map',
  'why': 'The audit groups the inventory into broad areas so you can see where the 28-day trail spends its time. Counts are MUST concepts, '
         'and days are the roadmap locations, not a claim that a single day masters an area.',
  'svg': '<svg viewBox="0 0 1000 170" role="img" aria-label="Coverage map from inventory areas to the 28 day trail">\n'
         '<rect x="25" y="34" width="210" height="78" rx="14" class="s-box-j"></rect><text class="s-t-b" x="130" y="68" '
         'text-anchor="middle">207 MUST</text><text class="s-t-sm" x="130" y="92" text-anchor="middle">inventory concepts</text>\n'
         '<path class="s-line" d="M235,73 L292,73" marker-end="url(#ah)"></path><rect x="292" y="34" width="380" height="78" rx="14" '
         'class="s-card"></rect><text class="s-t-b" x="482" y="68" text-anchor="middle">28 DAYS</text><text class="s-t-sm" x="482" y="92" '
         'text-anchor="middle">two interleaved fields, four weeks</text>\n'
         '<path class="s-line" d="M672,73 L729,73" marker-end="url(#ah)"></path><rect x="729" y="34" width="246" height="78" rx="14" '
         'class="s-box-a"></rect><text class="s-t-b" x="852" y="68" text-anchor="middle">AUDIT</text><text class="s-t-sm" x="852" y="92" '
         'text-anchor="middle">traceable, not exhaustive</text>\n'
         '<text class="s-t-sm" x="500" y="150" text-anchor="middle">The table below is the useful detail: category, MUST count, and '
         'roadmap days.</text>\n'
         '</svg>',
  'figcap': 'Coverage is a map of deliberate inclusion. It is not a certificate of mastery.',
  'extra_html': '<div class="tbl-wrap"><table class="tbl"><thead><tr><th>Inventory area</th><th>MUST</th><th>Roadmap '
                'days</th></tr></thead><tbody><tr><td>Boundary and ethics</td><td>6</td><td>1, 24, 28</td></tr><tr><td>Words and '
                'definitions</td><td>9</td><td>1, 8, 12, 16, 17</td></tr><tr><td>Mechanisms</td><td>79</td><td>1, 3, 4, 5, 7, 9, 11, 13, '
                '15, 17, 19, 23, 24, 26, 28</td></tr><tr><td>Procedures</td><td>30</td><td>6, 10, 12, 16, 18, 21, 22, 25, '
                '27</td></tr><tr><td>Decisions</td><td>14</td><td>1, 8, 9, 11, 14, 15, 20</td></tr><tr><td>Tools and '
                'measurement</td><td>23</td><td>6, 12, 19, 22, 27</td></tr><tr><td>Numbers and evidence</td><td>10</td><td>3, 7, 13, 19, '
                '22, 26</td></tr><tr><td>Money and pricing</td><td>11</td><td>17, 20, 22, 25, 27</td></tr><tr><td>Rules and '
                'safeguards</td><td>13</td><td>10, 18, 24, 26, 28</td></tr><tr><td>Frontier</td><td>4</td><td>24, 26, '
                '28</td></tr><tr><td>People and history</td><td>5</td><td>1, 2, 20, 22, 23</td></tr><tr><td>Failure and '
                'practice</td><td>3</td><td>10, 16, 24, 27</td></tr></tbody></table></div><p>This audit proves the guide covers the '
                'defined source-backed inventory and that every MUST concept has a roadmap home. It does not prove that you understand '
                'every concept, that 20 minutes produces mastery, that practitioner claims are causal, or that no unknown unknowns remain. '
                'Legal rules and AI governance also change by jurisdiction and date.</p>'}]

QUESTIONS = [('Why do people say yes to strangers?', [1, 3, 4]),
 ('Is persuasion just manipulation with better manners?', [1, 24, 28]),
 ('Why do my DMs get ignored?', [9, 10]),
 ('Why does a discount sometimes lower sales?', [17, 20]),
 ('What do top salespeople actually do differently, according to data?', [6, 13, 27]),
 ('How do you negotiate when the other side has more power?', [22, 23]),
 ('How do Gujarati traders bargain and why does it work?', [4, 23]),
 ('Can AI persuade better than humans?', [26, 28]),
 ('How can I sell websites to international eco tourism brands without sounding generic?', [8, 9, 16]),
 ('How do I sell a chatbot to a dental clinic that thinks it can answer WhatsApp itself?', [12, 16, 20]),
 ('How do I know whether a lead is worth a call?', [14]),
 ('What should my first line say?', [9, 10]),
 ('How do I ask about budget without making it awkward?', [12, 20]),
 ('What is a real objection versus a polite brush off?', [18, 21]),
 ('How much proof is enough?', [13, 16, 19]),
 ('Should I use scarcity in a service business?', [21, 24, 28]),
 ('How do I know when to walk away?', [22, 28]),
 ('Why do buyers say they love it and then disappear?', [21, 25, 27]),
 ('How do I stop selling features?', [16, 17]),
 ('How do I make a proposal easy to approve?', [14, 16, 21]),
 ('Which sales metric should a tiny studio track?', [27]),
 ('Should two commission only callers cold call clinics?', [10, 27]),
 ('How do I follow up without becoming spam?', [10, 25, 27]),
 ('What if the prospect asks for a free prototype?', [16, 20, 22]),
 ('Can stories sell technical AI work?', [15, 16]),
 ('What is the honest version of reciprocity and authority?', [1, 3, 28]),
 ('How should I price in USD and INR?', [17, 20]),
 ('How do I repair trust after a delivery mistake?', [25, 28]),
 ('What should stay human when AI does outreach?', [24, 26, 28]),
 ('How do I make a buyer feel safe saying no?', [1, 21, 28])]

LIBRARY = {'spine_note': 'The 28-day spine is a curated playlist, not one franchise: Crash Course gives compact foundations, while university talks, '
               'TED talks, practitioner lectures, and film clips supply contrast. The books below are depth tools, not a reading '
               'assignment.',
 'books': [('Rhetoric',
            'Aristotle',
            'c. 4th century BCE',
            'The original map of ethos, pathos, logos, enthymeme, audience, and situation.',
            'The surviving text is partial and its civic world is not a modern sales call.',
            'https://classics.mit.edu/Aristotle/rhetoric.html'),
           ('Communication and Persuasion',
            'Carl Hovland, Irving Janis, Harold Kelley',
            '1953',
            'The Yale programme linking source, message, channel, audience, and attitude change.',
            'Early laboratory work does not settle every platform or field context.',
            'https://archive.org/details/communicationper0000unse'),
           ('Communication and Persuasion',
            'Richard Petty and John Cacioppo',
            '1986',
            'The elaboration likelihood model and how motivation and ability shape processing.',
            'Routes are models of processing, not two fixed personality types.',
            'https://doi.org/10.1007/978-1-4612-4964-1'),
           ('Influence: New and Expanded',
            'Robert Cialdini',
            '2021',
            'A memorable practitioner vocabulary for social influence and its ethical uses.',
            'Seven principles are hypotheses and boundary conditions, not universal buttons.',
            'https://www.harpercollins.com/products/influence-new-and-expanded-robert-b-cialdini'),
           ('Prospect Theory',
            'Daniel Kahneman and Amos Tversky',
            '1979',
            'Reference points, framing, diminishing sensitivity, and risky choice.',
            'Loss aversion is robust in some settings but not a universal multiplier.',
            'https://doi.org/10.2307/1914185'),
           ('The Story Model',
            'Jennifer Aaker',
            '2019',
            'A practical bridge from narrative structure to organisational communication and memory.',
            'Story is not prevalence data and can make weak claims feel stronger.',
            'https://www.gsb.stanford.edu/insights/why-your-brain-loves-good-story'),
           ('The Role of Transportation in the Persuasiveness of Public Narratives',
            'Melanie Green and Timothy Brock',
            '2000',
            'The primary narrative transportation experiment and a testable account of story immersion.',
            'Later work finds moderators including realism, identification, and prior belief.',
            'https://doi.org/10.1037/0022-3514.79.5.701'),
           ('Nudge',
            'Richard Thaler and Cass Sunstein',
            '2008',
            'Choice architecture, defaults, and the autonomy question in plain language.',
            'The manifesto is more confident than the later, publication-bias-aware evidence.',
            'https://yalebooks.yale.edu/book/9780300122237/nudge/'),
           ('SPIN Selling',
            'Neil Rackham',
            '1988',
            'Discovery questions and the difference between small and complex sales.',
            'The proprietary observational research is not a universal causal test.',
            'https://doi.org/10.1201/9781003073024'),
           ('The Mom Test',
            'Rob Fitzpatrick',
            '2013',
            'Founder interviews that seek past behaviour and spending rather than compliments.',
            'It is not a complete enterprise qualification or negotiation system.',
            'https://foundry.virginia.edu/resources/the-mom-test'),
           ('Obviously Awesome',
            'April Dunford',
            '2019',
            'Positioning an offer against the alternatives a buyer actually considers.',
            'A strong practitioner method, not a randomised causal trial.',
            'https://www.aprildunford.com/books'),
           ('Successful Negotiation',
            'George Siedel',
            '2014',
            'Preparation, BATNA, interests, options, and practice for real negotiations.',
            'Course framing can simplify repeated, relational, or cross-cultural deals.',
            'https://www.coursera.org/learn/negotiation-skills'),
           ('Getting to Yes',
            'Roger Fisher, William Ury, and Bruce Patton',
            '2011',
            'Separating people from problems and positions from interests.',
            'Principled negotiation does not erase power, identity, or unequal alternatives.',
            'https://www.pon.harvard.edu/daily/batna/batna-negotiators-how-you-can-avoid-striking-out-and-create-mutual-gains-in-your-next-business-negotiation/'),
           ('The Trusted Advisor',
            'David Maister, Charles Green, and Robert Galford',
            '2000',
            'A useful trust heuristic for expertise, credibility, intimacy, and self-orientation.',
            'The equation is a heuristic, not a validated universal measurement scale.',
            'https://www.trustedadvisor.com/'),
           ('Sales Performance: A Meta-Analytic Examination',
            'Willem Verbeke, Frank Dietz, and Ernst Verwaal',
            '2011',
            'The evidence linking selling-related knowledge, adaptiveness, cognitive aptitude, and engagement to performance.',
            'Meta-analysis inherits heterogeneous definitions and mostly organisational samples.',
            'https://link.springer.com/article/10.1007/s11747-010-0211-8')],
 'extras': [('What Can You Learn from Your Competition?',
             'CrashCourse',
             '5hL66Xl6W6M',
             None,
             'A compact companion for alternatives and positioning.'),
            ('Testing Your Product and Getting Feedback',
             'CrashCourse',
             'zzn3xDiw1iE',
             None,
             'Turns claims about value into testable customer evidence.'),
            ('Online Advertising',
             'CrashCourse',
             'cmRcoJZRXEY',
             '10:32',
             'Shows how paid messages, targeting, and media systems shape attention.'),
            ('Social Thinking', 'CrashCourse', 'h6HLDV0T5Q8', None, 'A primer on the social context behind credibility and norms.'),
            ('Social Influence', 'CrashCourse', 'UGxGDdQnC1Y', None, 'Useful contrast for conformity, compliance, and resistance.'),
            ('The Facts about Fact Checking',
             'CrashCourse',
             'EZsaA0w_0z0',
             None,
             'A practical defence against unsupported claims in pitches.'),
            ('Who Can You Trust?', 'CrashCourse', 'o93pM-b97HI', None, 'Source evaluation for proof, testimonials, and public claims.'),
            ('The Power of Pre-Suasion',
             'Royal Society of Arts',
             '_hem3-8XbEI',
             None,
             'Cialdini on attention before the request, to be read with the ethics lens.'),
            ('Jennifer Aaker: The Power of Story',
             'Stanford Graduate School of Business',
             'CdO9a41WUss',
             '49:52',
             'A longer story lecture for narrative structure and organisational meaning.'),
            ('How to Speak So That People Want to Listen',
             'TED',
             'eIho2S0ZahI',
             None,
             'Voice, listening, and delivery without the Mehrabian myth.'),
            ('How to Negotiate Your Job Offer',
             'Deepak Malhotra',
             'km2Hd_xgo9Q',
             None,
             'Preparation and multi-issue negotiation in a clear university talk.'),
            ('Never Split the Difference',
             'Talks at Google',
             'guZa7mQV1l0',
             None,
             'A practitioner counterpoint, with tactical empathy claims treated cautiously.'),
            ('Negotiation: Getting What You Want',
             'Stanford Graduate School of Business',
             'MXFpOWDAhvM',
             None,
             'Interests, alternatives, and preparation from a negotiation researcher.'),
            ('Dark Patterns: User Interfaces Designed to Trick People',
             'Harry Brignull',
             '1KVyFio8gw4',
             None,
             'Names interface manipulation and the honest alternative.')],
 'courses': [('Successful Negotiation',
              'Coursera, University of Michigan',
              'https://www.coursera.org/learn/negotiation-skills',
              'A structured preparation and practice course, with audit availability depending on platform terms.'),
             ('Successful Negotiation: Essential Strategies and Skills',
              'University of Michigan Online',
              'https://online.umich.edu/courses/successful-negotiation-essential-strategies-and-skills/',
              'Short lectures and practice prompts for negotiation preparation.'),
             ('Inbound Sales',
              'HubSpot Academy',
              'https://academy.hubspot.com/courses/inbound-sales',
              'A free process introduction, useful but vendor-produced and naturally aligned with HubSpot tools.'),
             ('Harvard Program on Negotiation resources',
              'Harvard Law School',
              'https://www.pon.harvard.edu/daily/batna/batna-negotiators-how-you-can-avoid-striking-out-and-create-mutual-gains-in-your-next-business-negotiation/',
              'Open reference material for BATNA, alternatives, and principled negotiation.')]}

COLOPHON = ('Built on classical rhetoric, Indian and Chinese traditions of counsel, Yale attitude-change research, dual-process and narrative models, '
 'behavioural economics, sales observation, negotiation research, regulator guidance, and a verified free-video playlist. It is a map for '
 'honest influence, not a promise of mastery or legal advice. Status labels and source checks were reviewed in October 2026; fast-moving '
 'AI, platform, and jurisdiction claims need a fresh check before use.')

LIB_GLOSS = [('Persuasion',
  'Intentional communication that can change attitudes, beliefs, emotions, intentions, or behaviour without physical force.',
  'Persuasion'),
 ('Coercion', 'Compliance obtained through force or a credible threat rather than voluntary influence.', 'Persuasion'),
 ('Manipulation', 'Influence that exploits vulnerability or obscures choice while serving the influencer.', 'Persuasion'),
 ('Ethos', "A speaker's perceived character, credibility, and practical trustworthiness.", 'Persuasion'),
 ('Pathos', 'The emotional and motivational dimension of a message.', 'Persuasion'),
 ('Logos', 'The reasons, evidence, and inferential structure offered to an audience.', 'Persuasion'),
 ('Source credibility', 'Audience judgement that a source is expert, trustworthy, or reliable.', 'Persuasion'),
 ('Elaboration likelihood model', 'A model in which motivation and ability shape central versus peripheral processing.', 'Persuasion'),
 ('Heuristic systematic model', 'A model distinguishing shortcut cues from more effortful systematic thought.', 'Persuasion'),
 ('Reactance', 'Motivated resistance when a person perceives a threat to freedom or choice.', 'Persuasion'),
 ('Inoculation', 'A weakened opposing argument plus refutation that builds resistance to later persuasion.', 'Persuasion'),
 ('Narrative transportation', 'Immersion in a story that can change attention, imagery, emotion, and counterarguing.', 'Persuasion'),
 ('Choice architecture', 'The design of how options are presented without removing the options.', 'Persuasion'),
 ('Nudge', 'A choice-architecture intervention intended to alter behaviour without coercion or major incentives.', 'Persuasion'),
 ('Selling', 'An exchange process that helps a buyer decide whether a solution is worth its expected cost and risk.', 'Sales'),
 ('Value proposition', 'A clear statement of who benefits, which outcome improves, how, and why the offer is credible.', 'Sales'),
 ('Ideal customer profile', 'A description of the account or customer for whom the offer is most useful and viable.', 'Sales'),
 ('Discovery', 'A structured conversation to learn the problem, stakes, constraints, criteria, and process.', 'Sales'),
 ('SPIN questioning', "Situation, Problem, Implication, and Need-payoff questions used to develop a buyer's problem.", 'Sales'),
 ('MEDDICC',
  'A qualification lens covering metrics, economic buyer, decision criteria, decision process, pain, champion, and competition.',
  'Sales'),
 ('Proof', 'Evidence that an outcome, capability, or claim is real and relevant to this buyer.', 'Sales'),
 ('Risk reversal', "A fair design that reduces a buyer's downside without hiding scope, cost, or responsibility.", 'Sales'),
 ('BATNA', 'The best alternative available if no agreement is reached.', 'Sales'),
 ('ZOPA', "The zone of possible agreement where the parties' acceptable ranges overlap.", 'Sales'),
 ('Value based pricing', 'Pricing anchored to credible customer value and alternatives rather than only internal cost.', 'Sales'),
 ('Mutual action plan', 'A shared sequence of owners, evidence, dates, and decisions toward an agreement.', 'Sales'),
 ('Trust repair', 'A deliberate response that acknowledges harm, explains the fix, and rebuilds reliable expectations.', 'Sales'),
 ('Pipeline velocity', 'The rate at which qualified opportunities move through defined stages and value.', 'Sales')]

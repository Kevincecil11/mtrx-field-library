"""No. 08 content module front (normalised from drafts/08/front.py, 1 Nov 2026). Plain data; see drafts/FORMAT-08.md."""

COVER = {'title_html': 'Field guide to <span class="o">the screenplay</span>',
 'sub': 'Story theory, page craft, and the working life of a writer.',
 'verbs': ['notice', 'draft', 'rewrite'],
 'cube_caption': 'A screenplay is a promise to the reader, a plan for collaborators, and a draft that expects to change.'}

HOW = {'why': 'Each day is one free video followed by an insider layer that tests the video against dramatic theory, working scripts, directors, '
        'actors, readers, and the business. The point is not to memorise a formula. It is to notice a promise, make a choice visible, and '
        'revise the result.',
 'specs': [('Retrieval practice',
            'strong evidence',
            'Answer the question before you watch. A wrong answer gives the episode a useful target.'),
           ('Spacing',
            'strong',
            'Earlier ideas return in new scenes. Rebuilding a concept after a gap is more useful than rereading it once.'),
           ('Guess first',
            'moderate',
            'Predict the turn, the missing image, or the reader objection. Treat surprise as evidence about your model.'),
           ('Interleaving',
            'moderate',
            'Story and Script alternate. The contrast keeps a beautiful idea answerable to a page, a performer, and a production.')],
 'cue': 'Choose one fixed moment, such as after morning chai and before Instagram. On a bad day, run rescue mode: the question, the video, '
        'and one sentence of writing. Resume tomorrow without punishment.',
 'field_note': 'How to learn one field or both: 14 Story days and 14 Script days. The daily Write it drill builds a 5-page short, premise '
               'first, then character and outline, first draft, rewrite and polish.'}

WEEKS = {1: ('The engine of story',
     'Meet dramatic action, the screenplay as a working document, structure, premise, character, scene turns, and traditions beyond one '
     'Western model. By Sunday, you have a provisional premise and logline for a contained short.'),
 2: ('Character, conflict and the page',
     'Put pressure on the character and the page: visual action, suspense, dialogue, subtext, theme, genre, and an outline that leaves '
     'room for discovery. By Sunday, your short has a character sheet and one-page plan.'),
 3: ('The first draft',
     "Draft through structure models, nonlinear time, format, process, world, television, and the director's eye. By Sunday, the five-page "
     'short exists as a complete first draft, not a perfect idea.'),
 4: ('Rewrite, the room and the road',
     'Learn to cut, receive notes, pay off a setup, collaborate with actors and producers, understand access and AI, and finish a '
     'calling-card short. By Day 28, you have a polished draft and a realistic next 90 days.')}

MAPS = [{'id': 'map-sto',
  'meta': 'Map 1',
  'title': "Story's family tree",
  'why': 'Story theory is a family, not a single trunk. Aristotle gives action, probability, reversal and recognition. The Natyashastra '
         'gives performance, rasa, bhava and sandhis. Later tools, from McKee and Truby to Yorke and the sequence approach, are working '
         "lenses, while the Hero's Journey and kishotenketsu belong to different debates and should not be treated as universal laws.",
  'svg': '<svg viewBox="0 0 1000 430" role="img" aria-label="Story family tree from classical traditions to modern structure tools">\n'
         '<rect x="24" y="164" width="184" height="92" rx="16" class="s-box-j"></rect><text class="s-t-b" x="116" y="202" '
         'text-anchor="middle">STORY</text><text class="s-t-sm" x="116" y="228" text-anchor="middle">action plus meaning</text>\n'
         '<path class="s-line" d="M208,210 L264,210" marker-end="url(#ah)"></path>\n'
         '<rect x="264" y="30" width="208" height="78" rx="12" class="s-card"></rect><text class="s-t-b" x="368" y="62" '
         'text-anchor="middle">ARISTOTLE</text><text class="s-t-sm" x="368" y="86" text-anchor="middle">plot, turn, recognition</text>\n'
         '<rect x="264" y="126" width="208" height="78" rx="12" class="s-box-a"></rect><text class="s-t-b" x="368" y="158" '
         'text-anchor="middle">NATYASHASTRA</text><text class="s-t-sm" x="368" y="182" text-anchor="middle">rasa, bhava, sandhis</text>\n'
         '<rect x="264" y="222" width="208" height="78" rx="12" class="s-card"></rect><text class="s-t-b" x="368" y="254" '
         'text-anchor="middle">STRUCTURE TOOLS</text><text class="s-t-sm" x="368" y="278" text-anchor="middle">Field, sequence, five '
         'acts</text>\n'
         '<rect x="264" y="318" width="208" height="78" rx="12" class="s-box-a"></rect><text class="s-t-b" x="368" y="350" '
         'text-anchor="middle">COUNTER MODELS</text><text class="s-t-sm" x="368" y="374" text-anchor="middle">kishotenketsu, episodic '
         'form</text>\n'
         '<path class="s-line s-dash" d="M236,210 L264,69"></path><path class="s-line s-dash" d="M236,210 L264,165"></path><path '
         'class="s-line s-dash" d="M236,210 L264,261"></path><path class="s-line s-dash" d="M236,210 L264,357"></path>\n'
         '<rect x="532" y="48" width="422" height="126" rx="14" class="s-box-a"></rect><text class="s-t-b" x="743" y="80" '
         'text-anchor="middle">MODERN LENSES</text><text class="s-t-sm" x="560" y="112">McKee: value change and gap</text><text '
         'class="s-t-sm" x="560" y="138">Truby: moral argument and steps</text><text class="s-t-sm" x="560" y="164">Yorke: pattern, '
         'pressure, reversal</text>\n'
         '<rect x="532" y="210" width="422" height="126" rx="14" class="s-box-j"></rect><text class="s-t-b" x="743" y="242" '
         'text-anchor="middle">MYTHIC FAMILY</text><text class="s-t-sm" x="560" y="274">Campbell: departure, initiation, '
         'return</text><text class="s-t-sm" x="560" y="300">Vogler: a Hollywood development memo</text><text class="s-t-sm" x="560" '
         'y="326">Useful pattern, not a compulsory route</text>\n'
         '<path class="s-line" d="M472,165 L532,111" marker-end="url(#ah)"></path><path class="s-line" d="M472,261 L532,269" '
         'marker-end="url(#ah)"></path>\n'
         '<text class="s-t-sm" x="743" y="386" text-anchor="middle">Compare models by what they help you notice.</text>\n'
         '</svg>',
  'figcap': 'The family tree has several roots and no single legal heir. Aristotle, Bharata, modern craft teachers, and East Asian forms '
            'answer different questions. Sources: https://classics.mit.edu/Aristotle/poetics.html and '
            'https://archive.org/stream/NatyaShastra/natya_shastra_translation_volume_1_-_bharat_muni_djvu.txt'},
 {'id': 'map-scr',
  'meta': 'Map 2',
  'title': "The screenplay's life",
  'why': 'A screenplay changes jobs as it moves through a project. It begins as an idea, becomes a document that can be read and '
         'discussed, then becomes a production instrument, and finally meets the edit, where images, performances, sound and cuts rewrite '
         'the intention again.',
  'svg': '<svg viewBox="0 0 1000 360" role="img" aria-label="The screenplay life from idea to edit">\n'
         '<rect x="22" y="40" width="140" height="72" rx="12" class="s-box-j"></rect><text class="s-t-b" x="92" y="70" '
         'text-anchor="middle">IDEA</text><text class="s-t-sm" x="92" y="94" text-anchor="middle">a pressure point</text>\n'
         '<path class="s-line" d="M162,76 L184,76" marker-end="url(#ah)"></path><rect x="184" y="40" width="140" height="72" rx="12" '
         'class="s-card"></rect><text class="s-t-b" x="254" y="70" text-anchor="middle">LOGLINE</text><text class="s-t-sm" x="254" y="94" '
         'text-anchor="middle">promise and stakes</text>\n'
         '<path class="s-line" d="M324,76 L346,76" marker-end="url(#ah)"></path><rect x="346" y="40" width="140" height="72" rx="12" '
         'class="s-box-a"></rect><text class="s-t-b" x="416" y="70" text-anchor="middle">TREATMENT</text><text class="s-t-sm" x="416" '
         'y="94" text-anchor="middle">story in prose</text>\n'
         '<path class="s-line" d="M486,76 L508,76" marker-end="url(#ah)"></path><rect x="508" y="40" width="140" height="72" rx="12" '
         'class="s-card"></rect><text class="s-t-b" x="578" y="70" text-anchor="middle">OUTLINE</text><text class="s-t-sm" x="578" y="94" '
         'text-anchor="middle">beats and turns</text>\n'
         '<path class="s-line" d="M648,76 L670,76" marker-end="url(#ah)"></path><rect x="670" y="40" width="140" height="72" rx="12" '
         'class="s-box-a"></rect><text class="s-t-b" x="740" y="70" text-anchor="middle">DRAFT</text><text class="s-t-sm" x="740" y="94" '
         'text-anchor="middle">scenes on pages</text>\n'
         '<path class="s-line" d="M810,76 L832,76" marker-end="url(#ah)"></path><rect x="832" y="40" width="140" height="72" rx="12" '
         'class="s-box-j"></rect><text class="s-t-b" x="902" y="70" text-anchor="middle">REWRITES</text><text class="s-t-sm" x="902" '
         'y="94" text-anchor="middle">structure, scene, line</text>\n'
         '<path class="s-line s-dash" d="M902,112 L902,178"></path><rect x="742" y="178" width="180" height="72" rx="12" '
         'class="s-card"></rect><text class="s-t-b" x="832" y="208" text-anchor="middle">NOTES + POLISH</text><text class="s-t-sm" x="832" '
         'y="232" text-anchor="middle">reader and actor tests</text>\n'
         '<path class="s-line" d="M742,214 L718,214" marker-end="url(#ah)"></path><rect x="530" y="178" width="188" height="72" rx="12" '
         'class="s-box-a"></rect><text class="s-t-b" x="624" y="208" text-anchor="middle">SALE OR LAB</text><text class="s-t-sm" x="624" '
         'y="232" text-anchor="middle">access, pitch, support</text>\n'
         '<path class="s-line" d="M530,214 L506,214" marker-end="url(#ah)"></path><rect x="318" y="178" width="188" height="72" rx="12" '
         'class="s-box-j"></rect><text class="s-t-b" x="412" y="208" text-anchor="middle">PRODUCTION</text><text class="s-t-sm" x="412" '
         'y="232" text-anchor="middle">actors, crew, choices</text>\n'
         '<path class="s-line" d="M318,214 L294,214" marker-end="url(#ah)"></path><rect x="78" y="178" width="216" height="72" rx="12" '
         'class="s-card"></rect><text class="s-t-b" x="186" y="208" text-anchor="middle">EDIT = LAST REWRITE</text><text class="s-t-sm" '
         'x="186" y="232" text-anchor="middle">cut, sound, performance</text>\n'
         '<text class="s-t-sm" x="500" y="312" text-anchor="middle">The document is stable enough to collaborate on, never too sacred to '
         'change.</text>\n'
         '</svg>',
  'figcap': 'The pipeline is not a ladder of purity. Feedback, budget, performance and the edit can send a project back upstream. Sources: '
            'https://www.bbc.co.uk/writersroom/documents/screenplay.pdf and https://www.wgfoundation.org/screenplay-primers'},
 {'id': 'map-time',
  'meta': 'Map 3',
  'title': 'Three lanes through screenwriting',
  'why': 'Read down one lane for continuity, then across the lanes for coincidence and pressure. Dates are anchors, not a claim that one '
         'tradition caused the others. Each item has a date line and a short meaning line.',
  'svg': '<svg viewBox="0 0 1000 500" role="img" aria-label="Three lanes: Western dramatic theory, screenwriting and industry, India China '
         'Japan Korea">\n'
         '<rect x="20" y="16" width="310" height="468" rx="12" class="s-card"></rect><text class="s-t" x="175" y="42" '
         'text-anchor="middle">WESTERN DRAMATIC THEORY</text>\n'
         '<rect x="345" y="16" width="310" height="468" rx="12" class="s-box-j"></rect><text class="s-t" x="500" y="42" '
         'text-anchor="middle">SCREENWRITING + INDUSTRY</text>\n'
         '<rect x="670" y="16" width="310" height="468" rx="12" class="s-box-a"></rect><text class="s-t" x="825" y="42" '
         'text-anchor="middle">INDIA, CHINA, JAPAN, KOREA</text>\n'
         '<path class="s-line" d="M36,56 L36,470"></path><path class="s-line" d="M361,56 L361,470"></path><path class="s-line" d="M686,56 '
         'L686,470"></path>\n'
         '<rect x="48" y="64" width="270" height="58" rx="9" class="s-box-a"></rect><text class="s-t" x="62" y="88">c. 335 BCE '
         'Aristotle</text><text class="s-t-sm" x="62" y="108">Poetics: plot and action</text>\n'
         '<rect x="48" y="130" width="270" height="58" rx="9" class="s-box-a"></rect><text class="s-t" x="62" y="154">1949 '
         'Campbell</text><text class="s-t-sm" x="62" y="174">mythic departure and return</text>\n'
         '<rect x="48" y="196" width="270" height="58" rx="9" class="s-box-a"></rect><text class="s-t" x="62" y="220">1979 Syd '
         'Field</text><text class="s-t-sm" x="62" y="240">three-act paradigm spreads</text>\n'
         '<rect x="48" y="262" width="270" height="58" rx="9" class="s-box-a"></rect><text class="s-t" x="62" y="286">1986 Petty, '
         'Cacioppo</text><text class="s-t-sm" x="62" y="306">audience processing model</text>\n'
         '<rect x="48" y="328" width="270" height="58" rx="9" class="s-box-a"></rect><text class="s-t" x="62" y="352">1997 Robert '
         'McKee</text><text class="s-t-sm" x="62" y="372">values, gaps and scene turns</text>\n'
         '<rect x="48" y="394" width="270" height="58" rx="9" class="s-box-a"></rect><text class="s-t" x="62" y="418">2014 John '
         'Yorke</text><text class="s-t-sm" x="62" y="438">pattern, pressure, reversal</text>\n'
         '<rect x="373" y="64" width="270" height="58" rx="9" class="s-card"></rect><text class="s-t" x="387" y="88">1938 Screen Writers '
         'Guild</text><text class="s-t-sm" x="387" y="108">collective voice and credit</text>\n'
         '<rect x="373" y="130" width="270" height="58" rx="9" class="s-card"></rect><text class="s-t" x="387" y="154">1986 Nicholl '
         'begins</text><text class="s-t-sm" x="387" y="174">fellowships for new writers</text>\n'
         '<rect x="373" y="196" width="270" height="58" rx="9" class="s-card"></rect><text class="s-t" x="387" y="220">1990 Final '
         'Draft</text><text class="s-t-sm" x="387" y="240">digital format enters rooms</text>\n'
         '<rect x="373" y="262" width="270" height="58" rx="9" class="s-card"></rect><text class="s-t" x="387" y="286">2005 The Black '
         'List</text><text class="s-t-sm" x="387" y="306">admired unproduced scripts</text>\n'
         '<rect x="373" y="328" width="270" height="58" rx="9" class="s-card"></rect><text class="s-t" x="387" y="352">2023 WGA '
         'agreement</text><text class="s-t-sm" x="387" y="372">AI, staffing, streaming terms</text>\n'
         '<rect x="373" y="394" width="270" height="58" rx="9" class="s-card"></rect><text class="s-t" x="387" y="418">2024 WGA '
         'snapshot</text><text class="s-t-sm" x="387" y="438">1,651 screenwriters worked</text>\n'
         '<rect x="698" y="64" width="270" height="58" rx="9" class="s-box-j"></rect><text class="s-t" x="712" y="88">c. 200 BCE '
         'Natyashastra</text><text class="s-t-sm" x="712" y="108">rasa, bhava, five sandhis</text>\n'
         '<rect x="698" y="130" width="270" height="58" rx="9" class="s-box-j"></rect><text class="s-t" x="712" y="154">c. 3rd BCE Han '
         'Feizi</text><text class="s-t-sm" x="712" y="174">persuasion and statecraft</text>\n'
         '<rect x="698" y="196" width="270" height="58" rx="9" class="s-box-j"></rect><text class="s-t" x="712" y="220">1200s Yuan '
         'zaju</text><text class="s-t-sm" x="712" y="240">four-act song drama</text>\n'
         '<rect x="698" y="262" width="270" height="58" rx="9" class="s-box-j"></rect><text class="s-t" x="712" y="286">1400s '
         'Zeami</text><text class="s-t-sm" x="712" y="306">Noh, jo-ha-kyu rhythm</text>\n'
         '<rect x="698" y="328" width="270" height="58" rx="9" class="s-box-j"></rect><text class="s-t" x="712" y="352">1920s '
         'kishotenketsu</text><text class="s-t-sm" x="712" y="372">four-part turn without rule</text>\n'
         '<rect x="698" y="394" width="270" height="58" rx="9" class="s-box-j"></rect><text class="s-t" x="712" y="418">2019 Bong '
         'Joon-ho</text><text class="s-t-sm" x="712" y="438">class, space, tonal turns</text>\n'
         '</svg>',
  'figcap': 'The lane items are selected anchors. They show parallel resources for thinking about action, performance, format, labour and '
            'audience, not a single march toward Hollywood.'},
 {'id': 'map-meet',
  'meta': 'Map 4',
  'title': 'Where story and script meet',
  'why': 'Story asks what changes for a person in a world. Script asks what a reader, actor, director, producer and editor can do with '
         'that change. The overlap is a promise made concrete, with choices that can be seen, heard, staged, revised and paid for.',
  'svg': '<svg viewBox="0 0 1000 370" role="img" aria-label="Story and Script meeting in a playable promise">\n'
         '<rect x="34" y="40" width="338" height="250" rx="18" class="s-box-a"></rect><text class="s-t-b" x="203" y="78" '
         'text-anchor="middle">STORY</text><text class="s-t-sm" x="64" y="120">desire and need</text><text class="s-t-sm" x="64" '
         'y="154">cause and consequence</text><text class="s-t-sm" x="64" y="188">theme under pressure</text><text class="s-t-sm" x="64" '
         'y="222">audience question</text>\n'
         '<rect x="628" y="40" width="338" height="250" rx="18" class="s-box-j"></rect><text class="s-t-b" x="797" y="78" '
         'text-anchor="middle">SCRIPT</text><text class="s-t-sm" x="658" y="120">filmable action</text><text class="s-t-sm" x="658" '
         'y="154">voice and subtext</text><text class="s-t-sm" x="658" y="188">format and white space</text><text class="s-t-sm" x="658" '
         'y="222">collaboration and notes</text>\n'
         '<rect x="380" y="84" width="240" height="164" rx="18" class="s-card"></rect><text class="s-t-b" x="500" y="116" '
         'text-anchor="middle">MEETING POINT</text><text class="s-t-sm" x="500" y="148" text-anchor="middle">A person wants '
         'something.</text><text class="s-t-sm" x="500" y="174" text-anchor="middle">A choice costs something.</text><text class="s-t-sm" '
         'x="500" y="200" text-anchor="middle">The page makes it playable.</text><text class="s-t-sm" x="500" y="226" '
         'text-anchor="middle">The cut finds the final shape.</text>\n'
         '<path class="s-line" d="M372,145 L380,145" marker-end="url(#ah)"></path><path class="s-line" d="M628,145 L620,145" '
         'marker-end="url(#ah)"></path><text class="s-t-sm" x="500" y="332" text-anchor="middle">The writer supplies an invitation, not a '
         'substitute for the whole film crew.</text>\n'
         '</svg>',
  'figcap': 'The meeting point is the smallest unit that survives translation from thought to page to performance to cut.',
  'extra_html': '<div class="stats"><div class="stat"><b>1,651</b><span>WGA screenwriters working in Q1 to Q3 2024, down from 1,947 in the '
                'same period of 2022.</span><small>WGA Writer Employment Snapshot, 2024 data: <a '
                'href="https://www.wga.org/uploadedfiles/the-guild/reports/WGA_Writer_Employment_Snapshot.pdf">wga.org '
                'report</a></small></div><div class="stat"><b>5,599</b><span>Nicholl entries reported for 2023, with at least two reads '
                'each.</span><small>Academy Nicholl history and rules: <a '
                'href="https://www.oscars.org/nicholl/about">oscars.org</a></small></div><div class="stat"><b>2005</b><span>Year Franklin '
                'Leonard created The Black List survey of admired unproduced scripts.</span><small>Research timeline and official '
                'explanation: <a href="https://blcklst.com/about">blcklst.com/about</a></small></div><div class="stat"><b>Nov 3 to Dec 1, '
                '2026</b><span>BBC Writers Open Call window listed in the October 2026 check, for UK and Republic of Ireland '
                'residents.</span><small>BBC Writers Open Call: <a '
                'href="https://www.bbc.co.uk/writers/opportunities/open-call/">bbc.co.uk/writers</a></small></div></div><p '
                'class="room">The profession is selective and jurisdictional. Treat a number as a dated condition, not a forecast of your '
                'career.</p>'},
 {'id': 'coverage',
  'meta': 'Map 6',
  'title': 'The coverage map',
  'why': 'This audit groups the inventory by its supplied areas, counts MUST concepts, and records the roadmap days that own them. It is a '
         'traceability aid, not a claim that one twenty-minute stop can teach a concept completely.',
  'svg': '<svg viewBox="0 0 1000 170" role="img" aria-label="Coverage map from 228 MUST concepts to the 28 day roadmap">\n'
         '<rect x="25" y="34" width="210" height="78" rx="14" class="s-box-j"></rect><text class="s-t-b" x="130" y="68" '
         'text-anchor="middle">228 MUST</text><text class="s-t-sm" x="130" y="92" text-anchor="middle">inventory concepts</text>\n'
         '<path class="s-line" d="M235,73 L292,73" marker-end="url(#ah)"></path><rect x="292" y="34" width="380" height="78" rx="14" '
         'class="s-card"></rect><text class="s-t-b" x="482" y="68" text-anchor="middle">28 DAYS</text><text class="s-t-sm" x="482" y="92" '
         'text-anchor="middle">Story and Script, four weeks</text>\n'
         '<path class="s-line" d="M672,73 L729,73" marker-end="url(#ah)"></path><rect x="729" y="34" width="246" height="78" rx="14" '
         'class="s-box-a"></rect><text class="s-t-b" x="852" y="68" text-anchor="middle">AUDIT</text><text class="s-t-sm" x="852" y="92" '
         'text-anchor="middle">mapped, not mastered</text>\n'
         '<text class="s-t-sm" x="500" y="150" text-anchor="middle">Areas below come directly from inventory.jsonl and '
         'curriculum.md.</text>\n'
         '</svg>',
  'figcap': 'Coverage is deliberate inclusion, not a certificate of mastery.',
  'extra_html': '<div class="tbl-wrap"><table class="tbl"><thead><tr><th>Inventory area</th><th>MUST</th><th>Roadmap '
                'days</th></tr></thead><tbody><tr><td>Story foundations</td><td>15</td><td>1, 27</td></tr><tr><td>Structure and '
                'causality</td><td>22</td><td>3, 15</td></tr><tr><td>Character and theme</td><td>21</td><td>5, 17, '
                '27</td></tr><tr><td>Genre and audience</td><td>16</td><td>9, 19, 23, 27</td></tr><tr><td>Scene and sequence '
                'craft</td><td>20</td><td>8</td></tr><tr><td>Screenplay format</td><td>28</td><td>16, 22</td></tr><tr><td>Action, '
                'dialogue, visual writing</td><td>20</td><td>10, 12</td></tr><tr><td>Process and development</td><td>29</td><td>14, 18, '
                '22, 28</td></tr><tr><td>Writers room and television</td><td>12</td><td>20</td></tr><tr><td>Business, legal, '
                'career</td><td>21</td><td>22, 24</td></tr><tr><td>Analysis, production, frontier</td><td>24</td><td>11, 12, 13, 21, 25, '
                '28</td></tr></tbody></table></div><p>This audit proves that all 228 defined MUST concepts in the supplied inventory have '
                'a roadmap home, and shows where each area is deliberately introduced. It does not prove that you understands every '
                'concept, that twenty minutes produces mastery, that a craft heuristic is causal, that the videos remain available, or '
                'that legal, guild, contest and AI rules stay unchanged. It also does not prove that a five-page draft will be good, '
                'produced, sold, or eligible for a particular programme.</p>'}]

QUESTIONS = [('Why do some films grip you from the first minute?', [1, 27]),
 ("Is the Hero's Journey real?", [3, 15]),
 ('How does suspense build instead of merely startling me?', [9, 19]),
 ('How do I write dialogue that does not sound written?', [10]),
 ('How do I write what the camera can see and hear?', [8, 12]),
 ('How does theme become felt rather than preached?', [11, 17, 27]),
 ('What does horror promise, and how can it break that promise fairly?', [9, 19]),
 ('How do I outline without killing discovery?', [14, 18]),
 ('What does professional screenplay format communicate?', [16]),
 ('How does television writing differ from a feature?', [20]),
 ('What does a director look for in a script?', [21]),
 ('Why is the edit the final rewrite?', [22]),
 ('How do great endings feel surprising and inevitable?', [3, 23]),
 ('How does a script get read, bought and made?', [22, 24, 28]),
 ("Will AI write films, and what remains the writer's job?", [26]),
 ('What does rasa add to structure models?', [7]),
 ('What is the difference between story and plot?', [1]),
 ('How much backstory should I reveal?', [5, 13]),
 ('What makes a twist fair?', [3, 23]),
 ('Should I write a short or a feature first?', [14, 28]),
 ('Can a story have two protagonists?', [5, 13]),
 ('What makes a location dramatic?', [19, 21]),
 ('How much research is enough?', [14, 21]),
 ('Why do actors improve a script?', [12, 25]),
 ('What does a producer need to know?', [22, 24]),
 ('How can five pages feel complete?', [28]),
 ('What makes a first scene memorable?', [1, 8]),
 ('Why do adaptations feel faithful but dead?', [13, 22]),
 ('Why can a quiet scene feel tense?', [9, 10, 12]),
 ('What does coverage actually measure?', [22, 25])]

LIBRARY = {'spine_note': 'The 28-day spine is a curated playlist, not one franchise: Crash Course and Pixar provide compact foundations, while '
               'BAFTA, StudioBinder, universities, guilds, and film clips add working contrast. The books, legal scripts, and open '
               'resources below are depth tools, not a reading assignment.',
 'books': [('Poetics',
            'Aristotle',
            'c. 335 BCE',
            'Action, plot, reversal, recognition, probability and the disputed catharsis.',
            'A partial text from a theatre culture, not a screenplay manual.',
            'https://classics.mit.edu/Aristotle/poetics.html'),
           ('Natyashastra',
            'Bharata Muni',
            'c. 2nd century BCE to 2nd century CE',
            'Rasa, bhava, performance, and five sandhis as an alternative dramatic vocabulary.',
            'Dating, authorship and translations are contested; do not reduce rasa to an emotion list.',
            'https://archive.org/stream/NatyaShastra/natya_shastra_translation_volume_1_-_bharat_muni_djvu.txt'),
           ('Screenplay',
            'Syd Field',
            '1979',
            'A first practical vocabulary for setup, confrontation, resolution and turning points.',
            'Page proportions are a diagnostic tool, not a law.',
            'https://ia803104.us.archive.org/30/items/screenplaythefoundationsofscreenwritingrevisedupdatedsydfield2005/Screenplay%3B%20The%20Foundations%20of%20Screenwriting%2C%20revised%20%26%20updated%20-%20Syd%20Field%20%282005%29.pdf'),
           ('Story',
            'Robert McKee',
            '1997',
            'Value change, scene gaps, progressive complications and controlling ideas.',
            'Seminar certainty can make a heuristic sound universal.',
            'https://mckeestory.com/books/story/'),
           ('The Anatomy of Story',
            'John Truby',
            '2007',
            'Moral argument, character design and a broad twenty-two-step planning tool.',
            'The steps can encourage reverse engineering of finished films.',
            'https://www.penguinrandomhouse.com/books/305339/the-anatomy-of-story-by-john-truby/'),
           ('Into the Woods',
            'John Yorke',
            '2013',
            'Pattern comparison across film and television, with pressure and reversal.',
            'A persuasive pattern book, not proof that every narrative follows one shape.',
            'https://www.penguin.co.uk/books/111/1115802/into-the-woods/9780141974935.html'),
           ('The Art of Dramatic Writing',
            'Lajos Egri',
            '1946',
            'Premise, character pressure, conflict and conclusion.',
            'Moral premises can overstate what an ambiguous story must mean.',
            'https://www.simonandschuster.com/books/The-Art-of-Dramatic-Writing/Lajos-Egri/9780671213329'),
           ('Save the Cat!',
            'Blake Snyder',
            '2005',
            'A memorable beat vocabulary for diagnosing a commercial draft.',
            'The fifteen beats are not a studio requirement or audience law.',
            'https://savethecat.com/'),
           ("The Writer's Journey",
            'Christopher Vogler',
            '2007',
            "A clear account of the Hero's Journey as a development lens.",
            'Campbell is simplified and the template is overapplied.',
            'https://chrisvogler.com/'),
           ('On Directing Film',
            'David Mamet',
            '1991',
            'Action, objectives and thinking in images and cuts.',
            'Its prescriptions are deliberately narrow and can erase performance nuance.',
            'https://www.penguinrandomhouse.com/books/318456/on-directing-film-by-david-mamet/'),
           ('Making Movies',
            'Sidney Lumet',
            '1995',
            'Rehearsal, collaboration, camera, editing and production decisions.',
            "A director's account, not a universal writer workflow.",
            'https://www.penguinrandomhouse.com/books/159545/making-movies-by-sidney-lumet/'),
           ('Adventures in the Screen Trade',
            'William Goldman',
            '1983',
            'Development, rewriting, studio uncertainty and the screen trade.',
            'A vivid memoir and warning, not a representative labour dataset.',
            'https://www.hachettebookgroup.com/titles/william-goldman/adventures-in-the-screen-trade/9780446391177/'),
           ('Something Like an Autobiography',
            'Akira Kurosawa',
            '1982',
            "Apprenticeship, visual thinking and the director's relation to scripts.",
            "Selective memory and one filmmaker's route, not a universal Asian method.",
            'https://www.penguinrandomhouse.com/books/159924/something-like-an-autobiography-by-akira-kurosawa/'),
           ('In the Blink of an Eye',
            'Walter Murch',
            '1992',
            'Editing as attention, rhythm and the final rewrite of a scene.',
            'Editing insight cannot replace a production edit or audience test.',
            'https://www.silmanjamespress.com/shop/in-the-blink-of-an-eye/'),
           ('The Hollywood Standard',
            'Christopher Riley',
            '2009',
            'Readable screenplay format and professional page conventions.',
            'Market and software conventions change, so compare current guild and broadcaster guidance.',
            'https://www.mwp.com/book/the-hollywood-standard/')],
 'extras': [("The Poetics: WTF? Aristotle's Poetics, Greek Tragedy and Catharsis",
             'Tom Nicholas',
             'YpyobkolyVE',
             None,
             'An accessible explainer to pair with the primary text and its limits.'),
            ('Just Say Noh. But Also Say Kyogen: Crash Course Theater #11',
             'CrashCourse',
             'J1IyUPMXwS0',
             12.92,
             'Performance conventions that widen the dramatic vocabulary beyond realism.'),
            ('China, Zaju, and Beijing Opera: Crash Course Theater #25',
             'CrashCourse',
             'yzAdZDK4XKA',
             11.73,
             'A compact route into yuan zaju and role-based musical structure.'),
            ('Scriptnotes 403 - How to Write a Movie',
             'John August',
             'vSX-DROZuzY',
             None,
             'Working writers on intention, obstacle and readable action.'),
            ('Jordan Peele, Get Out Was Meant to be a More Direct, Brutal Wake-Up',
             'The Hollywood Reporter',
             'bDJKtoj_HCk',
             None,
             'A writer-director on designing horror, social pressure and audience response.'),
            ('Akira Kurosawa on Screenwriting',
             'The Script Lab',
             'is4oTzI5ytQ',
             None,
             'A concise director perspective on scripts, structure and cinema.'),
            ('Hayao Miyazaki in Conversation with Roland Kelts',
             'UC Berkeley Events',
             'wZWmOYq3fX4',
             None,
             'An international visual storytelling perspective from a university event.'),
            ('How to Write Like Taika Waititi',
             'BAFTA Guru',
             'A1y8Dn3YxBs',
             None,
             'Voice, process and productivity from a writer-director, treated as testimony.'),
            ('Guillermo Arriaga, BAFTA Screenwriters Lecture',
             'BAFTA Guru',
             '5Tng0NsWlBA',
             31.67,
             'A long craft lecture on nonlinear structure and character.'),
            ('The Writer Speaks: Billy Wilder',
             'Writers Guild Foundation',
             'tOjDuaLBl9c',
             None,
             'Archival writer-director thinking about economy and dialogue.'),
            ('The Writer Speaks: William Goldman',
             'Writers Guild Foundation',
             'nCs4gdt-mPY',
             None,
             'Career, story and uncertainty from a screen trade veteran.'),
            ('Beyond Words 2022: Original Screenplay Panel',
             'Writers Guild Foundation',
             'NrsoKf1lDdc',
             None,
             'Working nominees discuss process and the profession.'),
            ('BBC Writersroom interviews: Steven Moffat',
             'BBC Writers',
             '_qXuTwdlF9k',
             None,
             'A writer on ideas, career and the moving target of television.'),
            ('Anatomy of a Screenplay, Movie Script Format Explained',
             'StudioBinder',
             '6PLSJBTzaGw',
             None,
             'A second format explanation after the spine, useful for page anatomy.')],
 'courses': [('BBC Writers Open Call and script resources',
              'BBC Writers',
              'https://www.bbc.co.uk/writers/opportunities/open-call/',
              'Free broadcaster guidance, eligibility, opening pages and submission expectations. Current eligibility is '
              'jurisdiction-specific.'),
             ('Nicholl Screenwriting Resources and Winning Scripts',
              'Academy of Motion Picture Arts and Sciences',
              'https://www.oscars.org/nicholl/screenwriting-resources/winning-scripts',
              'Free legal scripts and competition context. The fellowship is for feature scripts, not this first 5-page short.'),
             ('Cinematic Storytelling readings',
              'MIT OpenCourseWare',
              'https://ocw.mit.edu/courses/mas-845-special-topics-in-cinematic-storytelling-spring-2004/pages/readings/',
              'Open readings and course material for film language and story analysis.'),
             ('Screenwriting',
              'University of East Anglia on FutureLearn',
              'https://www.futurelearn.com/courses/screenwriting/1',
              'Free to join course with concepts, analysis and exercises; platform access terms can change.'),
             ('BAFTA and BFI Screenwriter Lectures',
              'BAFTA and BFI',
              'https://player.bfi.org.uk/free/collection/bafta-bfi-screenwriter-lectures',
              'Open lectures from working screenwriters, useful for contrasting process testimonies.')],
 'scripts': [('Chinatown',
              'film',
              1974,
              'https://archive.org/details/chinatown-1974-1973.08.03',
              'Investigation, visual clues and a protagonist who learns too late.'),
             ('The Social Network',
              'film',
              2010,
              'https://deadline.com/wp-content/uploads/2011/01/thesocialnetwork-dl.pdf',
              'Compressed time, verbal status and parallel deposition structure.'),
             ('Get Out',
              'film',
              2017,
              'https://www.oscars.org/margaret-herrick-library/collections/scripts',
              'Politeness as horror, visual escalation and withheld information.'),
             ('Parasite',
              'film',
              2019,
              'https://deadline.com/wp-content/uploads/2020/01/parasite-script.pdf',
              'Geography, class exposition through objects and tonal turns.'),
             ('Whiplash',
              'film',
              2014,
              'https://www.oscars.org/margaret-herrick-library/collections/scripts',
              'Sonic action, goal escalation and a rival relationship.'),
             ('Lady Bird',
              'film',
              2017,
              'https://www.oscars.org/margaret-herrick-library/collections/scripts',
              'Compressed adolescence and arguments that contain love.'),
             ('Arrival',
              'film',
              2016,
              'https://www.oscars.org/margaret-herrick-library/collections/scripts',
              'Braided time, translation and exposition under pressure.'),
             ('Eternal Sunshine of the Spotless Mind',
              'film',
              2004,
              'https://beingcharliekaufman.com/index.php/scripts-writing/scripts-writing/film-scripts',
              'Form as memory, and comparison between draft and released story.'),
             ('Fleabag pilot',
              'series',
              2016,
              'https://www.bbc.com/writers/scripts/tv-drama/',
              'Direct address, comic confession and an episode engine.'),
             ('Breaking Bad pilot',
              'series',
              2008,
              'https://www.oscars.org/margaret-herrick-library/collections/scripts',
              "A cold open that creates a promise and a protagonist's public collapse."),
             ('Lost in Translation',
              'film',
              2003,
              'https://www.focusfeatures.com/article/focus-features-20th-anniversary_lost-in-translatio',
              'Atmosphere, restraint and relationship through small encounters.'),
             ('Moonlight', 'film', 2016, 'https://scriptlist.oscars.org/', 'Chapters, ellipsis, gesture and adapted structure.'),
             ('Nightcrawler',
              'film',
              2014,
              'https://www.oscars.org/margaret-herrick-library/collections/scripts',
              'Action description that creates an amoral worldview.'),
             ('Hereditary',
              'film',
              2018,
              'https://shop.a24films.com/products/hereditary-book',
              'Objects, spatial dread and purposeful visual language.'),
             ('A Quiet Place', 'film', 2018, 'https://www.paramountguilds.com/', 'Silence, sound rules and immediately filmable action.'),
             ('Barbie',
              'film',
              2023,
              'https://deadline.com/wp-content/uploads/2024/02/Barbie-Read-The-Screenplay.pdf',
              'Voice, narration and transitions between artificial worlds.'),
             ('The Zone of Interest',
              'film',
              2023,
              'https://deadline.com/wp-content/uploads/2024/01/The-Zone-Of-Interest-Read-The-Screenplay.pdf',
              'Sound, absence and moral framing.'),
             ('Nanny',
              'film',
              2022,
              'https://deadline.com/wp-content/uploads/2022/12/Nanny-Read-The-Screenplay.pdf',
              'Dream imagery and migration without exposition dumps.')]}

COLOPHON = ('Built from Aristotle, the Natyashastra, East Asian performance traditions, screenwriting craft books, legal screenplay sources, audience '
 'research, director and writer testimony, guild documents, broadcaster guidance, and a verified free-video pool. It is a field guide, not '
 'a formula, production course, legal opinion, or promise of access. Statuses and current policy claims were checked against the supplied '
 'research for October 2026; contest windows, guild terms, AI rules, URLs, and platform availability need a fresh check before submission.')

LIB_GLOSS = [('Story', 'The inferred chain of events, including events a film does not directly show.', 'Story'),
 ('Plot', 'The arranged presentation of events and causes in a dramatic work.', 'Story'),
 ('Fabula and syuzhet', 'Chronological story material versus the order and manner of its presentation.', 'Story'),
 ('Dramatic action', 'An action made legible through agents, choices and consequences.', 'Story'),
 ('Peripeteia', 'A reversal in the direction of an action.', 'Story'),
 ('Anagnorisis', 'Recognition, a movement from ignorance toward knowledge.', 'Story'),
 ('Catharsis', 'A disputed account of the effects of pity and fear in tragedy.', 'Story'),
 ('Rasa', 'An aesthetic relish or experienced flavour evoked through performance.', 'Story'),
 ('Bhava', 'A represented emotional state that helps produce rasa.', 'Story'),
 ('Premise', 'A compressed dramatic proposition that can generate action.', 'Story'),
 ('Want', 'The concrete external objective a character pursues.', 'Story'),
 ('Need', 'The internal change or recognition a character may resist or require.', 'Story'),
 ('Antagonistic force', 'A person, system, environment or contradiction that blocks a goal.', 'Story'),
 ('Genre promise', 'The expectation about tone, world, danger and payoff established by a work.', 'Story'),
 ('Suspense', 'Tension produced by uncertainty, threat, time and unequal knowledge.', 'Story'),
 ('Logline', 'A concise statement of protagonist, goal, opposition and stakes.', 'Script'),
 ('Treatment', "A prose account of a screenplay's story, scenes and movement.", 'Script'),
 ('Outline', 'A planned sequence of beats or scenes before full pages.', 'Script'),
 ('Slugline', 'A scene heading naming interior or exterior, place and approximate time.', 'Script'),
 ('Action line', 'Present-tense description of what can be seen, heard or materially inferred.', 'Script'),
 ('Character cue', 'The character name that identifies who speaks dialogue.', 'Script'),
 ('Parenthetical', 'A brief performance or delivery indication inside a dialogue block.', 'Script'),
 ('Subtext', 'The pressure, intention or meaning beneath the spoken words.', 'Script'),
 ('Spec screenplay', 'An uncommissioned screenplay written as a sample or possible sale.', 'Script'),
 ('Coverage', 'A reader report summarising a script, its strengths, problems and recommendation.', 'Script'),
 ('Option', 'A time-limited right to develop and potentially purchase specified rights.', 'Script'),
 ('Polish', 'A focused late rewrite of language, clarity, rhythm or detail.', 'Script'),
 ('Table read', 'A group reading aloud that exposes pace, logic, character and dialogue problems.', 'Script'),
 ('Showrunner', 'The lead writer and creative manager of a television production.', 'Script'),
 ('Chain of title', 'Documented control and transfer of rights in an underlying work.', 'Script')]

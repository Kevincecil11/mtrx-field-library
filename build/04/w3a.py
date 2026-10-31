"""No. 04 content module w3a (normalised from drafts/04/w3a.py, 27 Oct 2026). Plain data; see drafts/FORMAT-04.md."""

DAYS = [{'n': 15,
  'f': 'per',
  'title': 'Why do stories beat statistics, and when do they not?',
  'ep': ("Stanford Women's Leadership Lab", None, 'oB7FfKPMZvw', '08:36', 'Harnessing the Power of Stories'),
  'seg': None,
  'img': 'd15_gulliver',
  'imgcap': "Jonathan Swift's Gulliver meets the tiny world of Lilliput. A memorable case can carry an idea, but it cannot tell you how "
            'common the idea is.',
  'imgalt': '1727 illustration of Gulliver among the Lilliputians',
  'hook': 'A precise number travels through business slides: stories are 22 times more memorable than facts. Jennifer Aaker repeats it in '
          'the assigned Stanford video, and the number feels too neat to question. But where did it come from? The useful answer is '
          'stranger: the ratio has no traceable primary study, while smaller, real experiments show why stories can help and why a vivid '
          'case can still mislead.',
  'q': 'When should a story carry the argument, and when must data carry it?',
  'terms': [('Narrative transportation', 'absorption in a story through attention, imagery and feeling'),
            ('Identifiable victim effect', 'greater response to a named or pictured individual than to an equivalent statistical group'),
            ('Base rate', 'how common an event is in the relevant population'),
            ('Case study', 'a bounded account of context, action, result and limits'),
            ('Counterarguing', 'generating objections that resist a message')],
  'pre': [("True or false: the 22 times figure is a settled result from Jerome Bruner's book.",
           'False. The number is widely attributed to Bruner or Aaker, but no primary experiment supporting that exact ratio has been '
           'located. Keep the mechanism, drop the fake precision.'),
          ("If one lodge website case study doubled enquiries, does that prove a redesign will double every lodge's enquiries?",
           'No. It is evidence that the change may work in a similar context, not a population estimate. State the baseline, comparison, '
           'time window and what remains unknown.')],
  'watch': ['Where Aaker uses story plus data rather than story instead of data',
            'The four jobs of an effective story: goal, grab, engage and enable action',
            'The Save the Children example, and the difference between a vivid case and a prevalence claim'],
  'fig': '<svg viewBox="0 0 1000 360" role="img" aria-label="How a story and evidence work together in a sales message">\n'
         '<rect x="35" y="45" width="190" height="74" rx="12" class="s-card"/><text x="62" y="77" class="s-t">CASE</text><text x="62" '
         'y="101" class="s-t-sm">one person, stakes</text>\n'
         '<path d="M225 82 L285 82" class="s-line" marker-end="url(#ah)"/>\n'
         '<rect x="285" y="45" width="190" height="74" rx="12" class="s-box-a"/><text x="314" y="77" class="s-t">TRANSPORT</text><text '
         'x="314" y="101" class="s-t-sm">attention, imagery</text>\n'
         '<path d="M475 82 L535 82" class="s-line-m" marker-end="url(#ahm)"/>\n'
         '<rect x="535" y="45" width="190" height="74" rx="12" class="s-box-j"/><text x="564" y="77" class="s-t">TEST</text><text x="564" '
         'y="101" class="s-t-sm">data, baseline</text>\n'
         '<path d="M725 82 L785 82" class="s-line" marker-end="url(#ah)"/>\n'
         '<rect x="785" y="45" width="180" height="74" rx="12" class="s-card"/><text x="812" y="77" class="s-t">DECISION</text><text '
         'x="812" y="101" class="s-t-sm">fit, risk, next step</text>\n'
         '<rect x="95" y="190" width="810" height="86" rx="14" class="s-card"/><text x="125" y="224" class="s-t-b">THE HONEST '
         'STORY</text><text x="125" y="251" class="s-t-sm">A vivid case makes the problem imaginable. Evidence tells you how common, large '
         'and reversible it is.</text>\n'
         '<path d="M500 119 L500 188" class="s-line-m" marker-end="url(#ahm)"/>\n'
         '<text x="95" y="320" class="s-t-sm">Never use one memorable case as if it were a prevalence estimate.</text>\n'
         '</svg>',
  'figcap': 'The honest sequence is case for attention, transport for engagement, evidence for calibration and a decision that names risk.',
  'insider': ['<b>The 22 times claim is myth, checked Oct 2026.</b> The Stanford page and video repeat it, but they do not identify a '
              "study, sample, comparison or calculation. A 2024 source-tracing investigation found no such result in Jerome Bruner's "
              '<i>Actual Minds, Possible Worlds</i>, the book most often cited. Do not quote 22. Source: '
              'https://womensleadership.stanford.edu/tools-resources/voice-influence/harnessing-power-stories and '
              'https://www.linkedin.com/pulse/just-where-did-claim-stories-22-times-more-memorable-patience-davies-ud7le',
              "<b>What holds up is transportation, not a magic multiplier.</b> Green and Brock's four experiments (2000, samples 97, 69, "
              '274 and 258) linked absorption in a narrative with story-consistent beliefs and favourable protagonist evaluations. Highly '
              'transported readers also detected fewer false notes. A story can reduce counterarguing, which is exactly why truth checks '
              'matter. Source: https://pubmed.ncbi.nlm.nih.gov/11079236/',
              '<b>The replacement numbers are real but context-bound.</b> In the Save the Children experiment described by Aaker, a named '
              "child story produced about twice the donations of a statistics-only appeal. Small, Loewenstein and Slovic's "
              'identifiable-victim work explains why a person can evoke more response than a statistical group, while also warning that '
              'this can distort allocation. The case is a door into concern, not a prevalence estimate. Source: '
              'https://doi.org/10.1037/0033-2909.132.6.954',
              '<b>B2B buyers need a story with an audit trail.</b> A 2021 experiment with 233 Korean purchasing managers found narrative '
              'business-reference content increased transportation and reduced perceived functional and financial risk, but it was an '
              'online study, not proof of universal conversion. A 2019 B2B advertising study found story effects on trust and advocacy '
              'were stronger among C-suite decision makers. Pair the arc with baseline, intervention, result, time window and limitations. '
              'Sources: https://doi.org/10.3846/jbem.2021.15527 and https://doi.org/10.1016/j.indmarman.2019.02.002'],
  'deeper': '<p><b>Melanie Green and Timothy Brock, “The Role of Transportation in the Persuasiveness of Public Narratives” (2000)</b>, '
            'gives the causal spine. Transportation combines attention, imagery and affect. Across four experiments, more transportation '
            'predicted story-consistent beliefs and favourable evaluations, and processing instructions that reduced transportation '
            'reduced those effects. The warning is built in: immersion can make readers notice fewer false notes. A well-told case can '
            'therefore move a buyer before the buyer has audited it.</p><p><b>Paul Slovic and colleagues, “If I Look at the Mass I Will '
            'Never Act” (2007)</b>, and <b>Small, Loewenstein and Slovic, “Sympathy and Callousness” (2007)</b>, distinguish a named '
            'person from a statistical population. An identifiable victim can unlock sympathy and giving, but emotional response can '
            "decline when more victims are added. That is not a reason to hide the denominator. In a lodge proposal, one guest's booking "
            'journey can make friction concrete; booking data tells you whether the pattern is typical.</p><p><b>Chip and Dan Heath, '
            '<i>Made to Stick</i> (2007)</b>, popularised a classroom presentation result often repeated as 5 percent recalling a '
            'statistic versus 63 percent recalling a story after ten minutes. The figures are useful teaching evidence, not a general 13 '
            "times law. Aaker's 22 times is even less traceable. The honest replacement is a test: randomise or alternate story-plus-data "
            'versus data-only, then measure delayed recall and qualified action.</p><p><b>Jennifer Aaker and Victoria Chang, <i>How To '
            'Tell A Story</i> (2009)</b>, treats plot as an organising device for meaning, not evidence that emotion beats truth. In a '
            'case study, set the scene, pull the audience in, provide key facts, reveal the crux and implications, then repeat the '
            'implications. Your HansWild case study should follow that arc, with permissioned screenshots and an explicit “not a '
            'guarantee” line. The live debate is not story versus data. It is how narrative changes attention and interpretation, and how '
            'to preserve calibration while it does so. Sources: https://pubmed.ncbi.nlm.nih.gov/11079236/ '
            'https://doi.org/10.1037/0033-2909.132.6.954 https://www.gsb.stanford.edu/faculty-research/case-studies/how-tell-story '
            'https://doi.org/10.3846/jbem.2021.15527</p>',
  'names': [('Melanie C. Green',
             'Narrative transportation researcher; 2000 paper with Timothy Brock established a key experimental measure.'),
            ('Jennifer Aaker',
             'Stanford marketing scholar; teaches signature stories and the disputed 22 times claim in the assigned video.')],
  'room': '"A story earns attention; the baseline earns belief."',
  'explain': ('In 60 words: why is the 22 times claim unsafe but storytelling still useful?',
              'The exact 22 times ratio has no traceable primary study, so it should not be repeated as a law. Narrative transportation '
              'has experimental support: absorption can increase story-consistent beliefs and reduce counterarguing. Use a true, bounded '
              'case to make a problem imaginable, then add base rates, comparison data, limitations and a testable next step.'),
  'recall': [('What is narrative transportation?',
              'Absorption in a story through attention, imagery and feeling. It can increase story-consistent beliefs, so it can carry '
              'error as well as truth.'),
             ('What is the identifiable victim effect?',
              'A named or pictured person can evoke more concern than an equivalent statistical group. It helps attention but can distort '
              'proportional judgement.'),
             ('What should a B2B case study include?',
              'Context and baseline, the intervention, a measured result with time window, permission, limitations and a clear statement '
              'of what it does not prove.')],
  'use': ('A safari lodge asks HansWild for a proposal because its Instagram posts receive attention but direct enquiries are weak. What '
          'do you send?',
          'Open with one real guest journey, not a fabricated hero story. Show the exact mobile path and friction, then give the baseline '
          'enquiry data, a proposed change, a bounded pilot, expected indicators and risks. Keep the story for attention and empathy, and '
          'let the numbers decide whether the pilot worked.'),
  'further': [('Harnessing the Power of Stories', 'https://www.youtube.com/watch?v=oB7FfKPMZvw', 'Video · verified oEmbed, 08:36'),
              ('Green and Brock, The Role of Transportation in the Persuasiveness of Public Narratives',
               'https://pubmed.ncbi.nlm.nih.gov/11079236/',
               'Paper · 2000 experiments'),
              ('Aaker and Chang, How To Tell A Story (A)',
               'https://www.gsb.stanford.edu/faculty-research/case-studies/how-tell-story',
               'Case · 2009 business storytelling')]},
 {'n': 16,
  'f': 'sal',
  'title': 'How do you show value without hype?',
  'ep': ('Crash Course Entrepreneurship',
         11,
         'gaPWVChiyfk',
         '10:29',
         'How to Communicate with Customers: Crash Course Entrepreneurship #11'),
  'seg': None,
  'img': 'd16_demo',
  'imgcap': 'A salesperson demonstrates an iPad. A useful demo makes the buyer inspect an outcome, not admire a feature list.',
  'imgalt': 'Salesperson demonstrating an iPad to a customer',
  'hook': 'A proposal can contain every feature and still leave a buyer asking, “So what changes for me?” The old sales maxim says '
          'features tell and benefits sell. It is directionally useful, but too blunt: a feature becomes a benefit only when a particular '
          'buyer connects it to a valued outcome. A demo is not theatre. It is a small test of whether the promised change can be seen, '
          'checked and scoped.',
  'q': 'How can a pitch make value visible without promising what the evidence cannot support?',
  'terms': [('Feature', 'a property or component of an offer'),
            ('Capability', 'what the feature enables the customer or team to do'),
            ('Outcome', 'a change in performance, cost, risk or experience'),
            ('Proof asset', 'permissioned evidence such as a case, testimonial, baseline or log'),
            ('Risk reversal', 'a fair term that reduces uncertainty without pretending risk is zero')],
  'pre': [('True or false: showing more features makes a demo more persuasive.',
           'False. More features can increase cognitive load. Start with the agreed job, show the shortest path to the outcome and name '
           'what is outside scope.'),
          ('Is a testimonial proof that the same result is guaranteed for a new client?',
           'No. It is social evidence from one context. Pair it with the client type, baseline, time window, what changed and what remains '
           'uncertain.')],
  'watch': ['The difference between acquiring, retaining and informing customers',
            'How channels change communication and why the audience matters',
            'The Thought Bubble example: thesis, evidence, case and questions'],
  'fig': '<svg viewBox="0 0 1000 360" role="img" aria-label="An outcome led pitch from buyer problem to proof and scope">\n'
         '<rect x="40" y="42" width="190" height="78" rx="12" class="s-card"/><text x="68" y="75" class="s-t">CURRENT STATE</text><text '
         'x="68" y="101" class="s-t-sm">friction, cost, risk</text>\n'
         '<path d="M230 81 L295 81" class="s-line" marker-end="url(#ah)"/>\n'
         '<rect x="295" y="42" width="190" height="78" rx="12" class="s-box-a"/><text x="322" y="75" class="s-t">OUTCOME</text><text '
         'x="322" y="101" class="s-t-sm">what changes?</text>\n'
         '<path d="M485 81 L550 81" class="s-line-m" marker-end="url(#ahm)"/>\n'
         '<rect x="550" y="42" width="190" height="78" rx="12" class="s-box-j"/><text x="578" y="75" class="s-t">PROOF</text><text x="578" '
         'y="101" class="s-t-sm">baseline, result</text>\n'
         '<path d="M740 81 L805 81" class="s-line" marker-end="url(#ah)"/>\n'
         '<rect x="805" y="42" width="155" height="78" rx="12" class="s-card"/><text x="831" y="75" class="s-t">SCOPE</text><text x="831" '
         'y="101" class="s-t-sm">limits, next step</text>\n'
         '<rect x="115" y="195" width="770" height="82" rx="14" class="s-card"/><text x="145" y="229" class="s-t-b">FEATURE</text><path '
         'd="M265 236 L350 236" class="s-line" marker-end="url(#ah)"/><text x="377" y="229" class="s-t-b">CAPABILITY</text><path d="M520 '
         '236 L605 236" class="s-line" marker-end="url(#ah)"/><text x="632" y="229" class="s-t-b">OUTCOME</text><text x="145" y="258" '
         'class="s-t-sm">A feature is not a benefit until the buyer can connect it to a measurable change.</text>\n'
         '</svg>',
  'figcap': 'Translate feature to capability to outcome, then attach proof and a scope boundary. Confidence comes from preparation and '
            'inspectability, not volume.',
  'insider': ['<b>“Features tell, benefits sell” is a heuristic, not an audited law.</b> A feature is only persuasive when its capability '
              "connects to a buyer's outcome, such as fewer missed WhatsApp enquiries or a shorter path from wildlife inspiration to "
              'booking. The sales literature supports adaptiveness and knowledge, but does not validate the slogan as a universal effect. '
              'Source: https://link.springer.com/article/10.1007/s11747-010-0211-8',
              '<b>Demo the agreed use case, not the product catalogue.</b> Restate the current state and success metric, show the shortest '
              'path, let the buyer inspect it, explain dependencies and state exclusions. For a clinic, show enquiry to human handoff. For '
              'a lodge, show a mobile booking path only if the owner said direct enquiries matter. This is the practical implication of '
              'solution selling, not a claim that demos automatically close.',
              '<b>Proof needs a denominator and a boundary.</b> A case study should name the starting condition, intervention, result, '
              'time window and limitations. “Increased leads” is not enough. A permissioned HansWild case can say what was measured and '
              'what was not. If you have no result yet, label the asset a hypothesis or prototype, not a case study.',
              '<b>Confidence is the ability to stay accurate under questions.</b> The companion Crash Course video recommends a simple, '
              'concrete, credible and story-shaped message, plus practice and active listening. The evidence-backed version is modest: '
              'rehearse the demo, record it, invite hostile questions, and say “I do not know yet” when a dependency is untested. Source: '
              'https://www.youtube.com/watch?v=sjdxUiAJ0UQ'],
  'deeper': '<p><b>Neil Rackham, <i>SPIN Selling</i> (1988)</b>, is the useful antidote to feature dumping. Its Huthwaite research is '
            'reported as more than 35,000 calls involving 10,000 salespeople in 23 countries, and it distinguishes Situation, Problem, '
            'Implication and Need-payoff questions. The transferable lesson is not a magic script. It is that a pitch should emerge from a '
            "diagnosed problem and the buyer's consequences, so the demo proves something the buyer already said matters. Source: "
            'https://doi.org/10.1201/9781003073024</p><p><b>Matthew Dixon and Brent Adamson, <i>The Challenger Sale</i> (2011)</b>, argues '
            'for teaching a commercially useful insight, tailoring it and taking control of a constructive next step. The framework is '
            'influential but the original vendor research and dramatic “top performer” numbers should not be treated as universal causal '
            'estimates. For MTRX, teaching means showing a real booking-flow friction or missed clinic enquiry, not manufacturing hidden '
            'pain.</p><p><b>April Dunford, <i>Obviously Awesome</i> (2019)</b>, makes positioning the frame in which differentiated value '
            'is obvious. Ask what alternatives the prospect compares, which capability is unusual, what outcome follows and what evidence '
            'supports it. A website is not the same offer to every buyer: a lodge may value direct booking intent, while a clinic values '
            'response speed and handoff.</p><p><b>Glaunsinger, Miesler and Hari (2014)</b> compared a story and visual-metaphor B2B '
            'presentation with a control among 40 young experts. The story condition increased involvement, attitude, product knowledge '
            'and reduced information overload, but the sample was small. Use story to organise a demo, not to replace proof. The honest '
            'pitch is outcome, proof, risk, scope and a reversible next step. A useful proposal also records who owns each dependency, '
            'what the buyer must provide, how acceptance will be judged and when either side can stop. That paperwork is part of the value '
            'because it makes the promise inspectable and prevents later scope disputes. Sources: https://www.aprildunford.com/books '
            'https://hdl.handle.net/11475/13834</p>',
  'names': [('Neil Rackham', 'Sales researcher and author of SPIN Selling; his reported call study challenged one-call closing.'),
            ('April Dunford', 'Positioning author; frames value by alternatives, differentiated capabilities and evidence.')],
  'room': '"If the buyer cannot point to the outcome, I have shown a feature, not value."',
  'explain': ('In 60 words: what makes a demo persuasive without hype?',
              'A persuasive demo begins with a diagnosed current state and a buyer-owned outcome. It shows the shortest path to that '
              'outcome, uses permissioned proof with a baseline and time window, names dependencies and exclusions, and leaves a '
              'reversible next step. It does not imply that one case guarantees the result for a different client.'),
  'recall': [('What is the feature to outcome chain?',
              'A feature is a property, a capability is what it enables, and an outcome is the buyer-valued change. The chain must be '
              'explicit.'),
             ('What belongs in a case study?',
              'Context, baseline, intervention, measured result, time window, permission and limitations. A testimonial alone is not a '
              'causal estimate.'),
             ('What is an honest risk reversal?',
              'A bounded term that reduces uncertainty, such as a paid diagnostic credited to implementation or a defined pilot with a '
              'stop point, without claiming zero risk.')],
  'use': ('A dental clinic asks why MTRX should charge INR 20,000 for a WhatsApp automation when a cheaper plug-in exists. How do you '
          'present it?',
          'Ask about missed enquiries and staff handoff first. Demo the exact patient question, routing and human escalation. Show the '
          'measured problem if available, state integration and support limits, compare total scope rather than only licence price, and '
          'offer a bounded pilot or decline if the clinic cannot resource follow-through.'),
  'further': [('How to Speak With Confidence: Crash Course Business - Soft Skills #4',
               'https://www.youtube.com/watch?v=sjdxUiAJ0UQ',
               'Video · verified oEmbed, 11:12'),
              ('Rackham, SPIN Selling', 'https://doi.org/10.1201/9781003073024', 'Book · 1988 research framework'),
              ('Glaunsinger, Miesler and Hari, SenseMaking presentations',
               'https://hdl.handle.net/11475/13834',
               'Paper · 2014 B2B presentation experiment')]},
 {'n': 17,
  'f': 'per',
  'title': 'Why is value in the eye of the beholder?',
  'ep': ('TED', None, 'iueVZJVEmEs', '18:24', 'Rory Sutherland: Perspective is everything'),
  'seg': None,
  'img': 'd17_valueball',
  'imgcap': 'An 1883 advertising ball turns price tags and social meaning into a crowded theatre of value. Price is not the whole value, '
            'but neither is a clever frame a substitute for quality.',
  'imgalt': '1883 Puck illustration of an advertising ball with price tags',
  'hook': 'The same safari lodge can look expensive in one frame and reassuringly specialised in another. Rory Sutherland calls this '
          'reframing, but behavioural science adds a boundary: expectations can change experience, while price can also be a signal of '
          'quality, status or risk. The exciting part is real. The dangerous part is believing a frame can manufacture value from nothing.',
  'q': 'How can framing change perceived value while keeping the offer truthful and testable?',
  'terms': [('Perceived value', "a buyer's judged worth of an offer relative to its cost and alternatives"),
            ('Reference price', 'a comparison number or standard used to judge a price'),
            ('Placebo effect', 'a change in experience or performance caused partly by expectation and context'),
            ('Costly signalling', 'a signal that is credible because it is difficult or expensive to fake'),
            ('Veblen good', 'a good for which higher price can increase appeal through status, under specified conditions')],
  'pre': [('True or false: a higher price always improves perceived and actual performance.',
           'False. Price can shape expectations and sometimes experience, but effects depend on product, buyer knowledge, credibility and '
           'the task. Higher price can also trigger suspicion or reduce fit.'),
          ('If reframing changes perception, is the new value fake?',
           'Not necessarily. Context, clarity, reassurance and service can create real utility. But a frame must not hide defects, costs, '
           'uncertainty or a weak result.')],
  'watch': ["Sutherland's examples of control, waiting and psychological value",
            'The difference between changing a context and changing a physical product',
            'His Google and Eurostar examples, and which claims are anecdotes rather than trials'],
  'fig': '<svg viewBox="0 0 1000 360" role="img" aria-label="Perceived value as the interaction of outcome evidence expectation and '
         'trust">\n'
         '<rect x="375" y="25" width="250" height="62" rx="12" class="s-box-j"/><text x="420" y="62" class="s-t-b">PERCEIVED VALUE</text>\n'
         '<path d="M500 87 L500 125" class="s-line-m" marker-end="url(#ahm)"/>\n'
         '<rect x="65" y="140" width="220" height="84" rx="12" class="s-card"/><text x="96" y="173" class="s-t">OUTCOME</text><text x="96" '
         'y="198" class="s-t-sm">what improves?</text>\n'
         '<rect x="390" y="140" width="220" height="84" rx="12" class="s-box-a"/><text x="418" y="173" class="s-t">EXPECTATION</text><text '
         'x="418" y="198" class="s-t-sm">what seems possible?</text>\n'
         '<rect x="715" y="140" width="220" height="84" rx="12" class="s-card"/><text x="748" y="173" class="s-t">EVIDENCE</text><text '
         'x="748" y="198" class="s-t-sm">why believe it?</text>\n'
         '<path d="M500 125 L175 140" class="s-line" marker-end="url(#ah)"/><path d="M500 125 L500 140" class="s-line" '
         'marker-end="url(#ah)"/><path d="M500 125 L825 140" class="s-line" marker-end="url(#ah)"/>\n'
         '<rect x="155" y="275" width="690" height="48" rx="12" class="s-card"/><text x="192" y="305" class="s-t-sm">Reframe the meaning, '
         'never conceal the cost, uncertainty or comparison.</text>\n'
         '</svg>',
  'figcap': 'Perceived value is an interaction of expected outcome, meaning and evidence. A price signal can help, but credibility '
            'collapses when the signal is unsupported.',
  'insider': ["<b>The Ariely caveat is part of the lesson, checked Oct 2026.</b> Shiv, Carmon and Ariely's 2005 paper reported three "
              'experiments in which people given the same discounted energy drink solved fewer puzzles than people told they paid regular '
              'price. It is a striking expectancy result, not permission to inflate price or proof that every premium improves efficacy. '
              'Source: https://doi.org/10.1509/jmkr.2005.42.4.383',
              '<b>Do not separate the finding from the data-integrity context.</b> In 2021, Data Colada reported strong evidence that the '
              'mileage data in a different 2012 Ariely co-authored dishonesty field experiment were fabricated, including uniform 0 to '
              '50,000 mile distributions, impossible near-duplicate rows and missing rounding. The paper was retracted. In 2023, NPR '
              'reported that the insurer said it supplied about 3,700 policies, versus more than 13,000 in the paper, and said the dataset '
              'had been supplemented by synthesized or fabricated data. Source: https://datacolada.org/98 and '
              'https://www.npr.org/2023/07/28/1190663435/did-an-honesty-researcher-fabricate-data',
              "<b>The 2024 conclusion is not “all Ariely work is false.”</b> Duke's investigation statement said it found no evidence "
              'Ariely falsified or knowingly used falsified data, but found he should have done more to prevent faulty data from being '
              'published. That is a plain reason to downgrade confidence, inspect methods and seek independent replication. The 2005 '
              'placebo-price paper is not the 2012 dishonesty paper, and the integrity dispute does not by itself refute the 2005 result. '
              'Source: https://danariely.com/wp-content/uploads/2024/04/ArielyEndofIStatment.pdf',
              '<b>A safari lodge sells an experience, not pixels alone.</b> A high price can signal selectivity, conservation standards, '
              'guide quality and reliable service only when those features are real and verifiable. Show what the guest receives, who '
              'delivers it, evidence of outcomes and the comparison set. Never use premium language to conceal an ordinary product. A 2024 '
              'meta-analysis found buyer advantage in negotiations was small and vanished in pure B2B settings, another reminder that '
              'context beats slogans. Source: https://doi.org/10.1016/j.indmarman.2024.11.004'],
  'deeper': '<p><b>Rory Sutherland, “Perspective is everything” (TEDxAthens, 2012)</b>, is a provocative design brief, not a controlled '
            'estimate. His red-light countdown example illustrates how uncertainty can make a wait worse than its duration, and his '
            'Eurostar story asks whether comfort and usefulness can create more value than shaving minutes. Use this as hypothesis '
            'generation: identify the psychological job, then measure satisfaction, conversion or retention rather than treating an '
            'anecdote as proof.</p><p><b>Shiv, Carmon and Ariely, “Placebo Effects of Marketing Actions” (2005)</b>, reported three '
            'experiments in which a discounted price cue reduced performance on an energy-drink puzzle task relative to a regular-price '
            'cue, with expectancy as the proposed mediator. This supports a bounded claim: price and marketing context can alter '
            'expectations and sometimes experience. It does not establish a universal premium effect, and the later Ariely data-integrity '
            'controversy requires transparent methods and independent replication. The relevant 2021 to 2024 timeline is: Data Colada '
            'alleged fabrication in the 2012 dishonesty dataset in 2021; NPR reported insurer contradictions and retraction in 2023; '
            "Duke's 2024 statement cleared the investigation of a finding that Ariely knowingly falsified data but faulted "
            "safeguards.</p><p><b>Rao and Monroe, “The Effect of Price, Brand Name, and Store Name on Buyers' Perceptions of Product "
            'Quality” (1989)</b>, synthesised evidence that price and brand cues affect perceived quality, especially when buyers lack '
            'information. That is a cue-use result, not evidence that the object improved. <b>Veblen, <i>The Theory of the Leisure '
            'Class</i> (1899)</b>, supplies the status-signalling lineage, but modern claims about Veblen goods are conditional: scarcity, '
            'identity, competition and social meaning matter.</p><p>The honest operating rule is to reframe real value, not fabricate it. '
            'For HansWild, call a case “mobile booking friction audit,” show the before state, explain the mechanism, quote the exact '
            'scope and measure qualified enquiries. A premium retainer can buy response time, continuity and accountability if those are '
            'delivered. Source links: https://doi.org/10.1509/jmkr.2005.42.4.383 https://doi.org/10.1177/002224378902600309 '
            'https://danariely.com/wp-content/uploads/2024/04/ArielyEndofIStatment.pdf',
  'names': [('Baba Shiv and Ziv Carmon', 'Marketing researchers who co-authored the 2005 placebo-price paper with Dan Ariely.'),
            ('Rory Sutherland',
             'Ogilvy vice-chair and speaker whose reframing examples distinguish psychological from engineering value.')],
  'room': '"A frame can reveal value, but it cannot substitute for delivery and evidence."',
  'explain': ('In 60 words: what can price and framing legitimately do?',
              'Price and framing can change reference points, expectations, confidence and the meaning of a service. Those effects can '
              'create real utility when they clarify quality, reduce uncertainty or improve the experience. They cannot excuse hidden '
              'costs, fake scarcity or unsupported promises. Because evidence is contextual, test the frame against a measured outcome and '
              'disclose the comparison.'),
  'recall': [('What did the 2005 placebo-price paper actually test?',
              'Three experiments in which price cues around an energy drink were associated with puzzle performance, with the same product '
              'presented as discounted or regular price. It was not a universal premium law.'),
             ('What happened in the Ariely data controversy?',
              'Data Colada alleged fabricated data in a 2012 dishonesty field experiment in 2021. The paper was retracted, NPR reported '
              "insurer contradictions in 2023, and Duke's 2024 statement found no evidence Ariely knowingly falsified data but faulted "
              'safeguards.'),
             ('What is a costly signal?',
              'A cue that is credible partly because it is difficult or expensive to fake. It works only if the cost and the claimed '
              'quality are genuinely connected.')],
  'use': ('A safari operator says a new website must look “luxury” so it can charge more, but has no new service evidence. What do you '
          'advise?',
          'Do not sell luxury as a colour palette. Define the guest outcome and the operational proof: guide expertise, response time, '
          'conservation practice, room quality, transfer reliability and booking support. Build a visual frame that makes those real '
          'differences legible, then test qualified enquiries, conversion and guest feedback against the old experience.'),
  'further': [('Rory Sutherland: Perspective is everything',
               'https://www.youtube.com/watch?v=iueVZJVEmEs',
               'Talk · verified oEmbed, 18:24'),
              ('Shiv, Carmon and Ariely, Placebo Effects of Marketing Actions',
               'https://doi.org/10.1509/jmkr.2005.42.4.383',
               'Paper · 2005 price expectancy experiments'),
              ('Rao and Monroe, Effect of Price, Brand Name, and Store Name',
               'https://doi.org/10.1177/002224378902600309',
               'Review · 1989 price-quality cues')]},
 {'n': 18,
  'f': 'sal',
  'title': 'What is an objection really telling you?',
  'ep': ('Harvard Business Review', None, 'aDMtx5ivKK0', '14:22', 'The Art of Active Listening | The Harvard Business Review Guide'),
  'seg': None,
  'img': 'd18_listening',
  'imgcap': 'Nicolaes Maes painted listening as an act of attention. In a sales call, attention is diagnostic: it helps separate a '
            'condition to solve from a decision to respect.',
  'imgalt': 'Nicolaes Maes painting of a listening housewife',
  'hook': 'A buyer says, “Your price is too high.” The amateur seller hears a challenge and reaches for a rebuttal. The better seller '
          'hears an underspecified sentence. Too high compared with what, for which outcome, under whose budget, with what risk and at '
          'what time? An objection can be a condition, a misunderstanding, a missing stakeholder, a real lack of fit or a polite exit. '
          'Listening is how you find out which.',
  'q': 'How do you investigate an objection without arguing the buyer out of a legitimate no?',
  'terms': [('Objection', 'a stated concern or non-acceptance about an offer'),
            ('Condition', 'a requirement that must be satisfied for a decision'),
            ('Clarification', 'a question that makes an ambiguous concern specific'),
            ('Active listening', 'an attentive, two-way process that checks meaning and invites detail'),
            ('No-decision', 'a legitimate choice not to buy, distinct from an unresolved objection')],
  'pre': [('True or false: every objection is a reflex that a skilled closer should overcome.',
           'False. Some objections are conditions, some are misunderstandings and some are correct no-fit signals. Treating every no as '
           'resistance creates pressure and bad qualification.'),
          ("Does active listening mean staying silent and repeating the buyer's words?",
           'No. Good listening includes attention, relevant questions, paraphrase when useful and a check that the concern was understood. '
           'It is active and two-way, not passive mimicry.')],
  'watch': ['The difference between a sponge listener and a trampoline listener',
            'The six self-check questions, especially “what am I missing?”',
            'Why a leader who hears only smiling faces may be in an information bubble'],
  'fig': '<svg viewBox="0 0 1000 360" role="img" aria-label="A listening loop for diagnosing objections">\n'
         '<rect x="378" y="25" width="245" height="62" rx="12" class="s-box-j"/><text x="428" y="62" class="s-t-b">BUYER CONCERN</text>\n'
         '<path d="M500 87 L500 118" class="s-line" marker-end="url(#ah)"/>\n'
         '<rect x="70" y="130" width="190" height="78" rx="12" class="s-card"/><text x="100" y="164" class="s-t">PAUSE</text><text x="100" '
         'y="188" class="s-t-sm">do not defend</text>\n'
         '<rect x="295" y="130" width="190" height="78" rx="12" class="s-box-a"/><text x="324" y="164" class="s-t">CLARIFY</text><text '
         'x="324" y="188" class="s-t-sm">what does it mean?</text>\n'
         '<rect x="515" y="130" width="190" height="78" rx="12" class="s-box-a"/><text x="544" y="164" class="s-t">EXPLORE</text><text '
         'x="544" y="188" class="s-t-sm">condition or exit?</text>\n'
         '<rect x="735" y="130" width="190" height="78" rx="12" class="s-card"/><text x="764" y="164" class="s-t">RESPOND</text><text '
         'x="764" y="188" class="s-t-sm">evidence or no</text>\n'
         '<path d="M500 118 L165 130" class="s-line" marker-end="url(#ah)"/><path d="M260 169 L295 169" class="s-line" '
         'marker-end="url(#ah)"/><path d="M485 169 L515 169" class="s-line" marker-end="url(#ah)"/><path d="M705 169 L735 169" '
         'class="s-line" marker-end="url(#ah)"/>\n'
         '<path d="M830 208 C830 276 165 276 165 208" class="s-line-m" marker-end="url(#ahm)"/>\n'
         '<text x="275" y="310" class="s-t-sm">Check: did the answer resolve the real concern, or did the buyer say no?</text>\n'
         '</svg>',
  'figcap': "Pause, clarify, explore, respond with evidence or a clean no, then check. The loop protects both the buyer's agency and the "
            "seller's time.",
  'insider': ['<b>Objections are often indirect and delicate.</b> Clark, Drew and Pinch analysed recordings of real telephone-selling '
              'calls and found prospective customers often raised non-acceptances implicitly; explicit objections were less important than '
              'sales training usually assumes. Listen for hesitation, timing, competing priorities and attempts to end the interaction. '
              'Source: https://doi.org/10.1177/0957926594005004002',
              '<b>Use a four-step loop, but do not turn it into a trap.</b> Pause, acknowledge the legitimate concern, clarify what '
              '“expensive” or “not now” means, explore the condition and its consequences, then respond with relevant evidence. Check '
              "whether the answer resolved that specific concern. If it did not, change scope, timing or qualification, not the buyer's "
              'reality. A teaching synthesis of objection models is here: '
              'https://digitalcommons.unomaha.edu/cgi/viewcontent.cgi?article=1035&context=marketingfacpub',
              '<b>Active listening is more than nodding.</b> The HBR video presents listening as a two-way interaction: reflect on why you '
              'are listening, keep attention on the speaker, ask what may be missing, quiet your internal monologue and avoid an '
              'information bubble. The “trampoline” metaphor is useful, but the ethical test is whether the buyer can correct your '
              'paraphrase and decline without penalty. Source: https://www.youtube.com/watch?v=aDMtx5ivKK0',
              '<b>Price objections often contain a comparison.</b> Ask “compared with what?” and “what result would make this worthwhile?” '
              'Then make the comparison fair: scope, ownership, support, integration, response time, risk and total cost. If the clinic '
              'truly has no budget or the lodge is not a fit, say so and leave the relationship intact. A clean no is better than '
              'discounting into an unprofitable promise.'],
  'deeper': '<p><b>Colin Clark, Paul Drew and Trevor Pinch, “Managing Customer Objections during Real-Life Sales Negotiations” (1994)</b>, '
            'is a useful correction to stagey closing manuals. In recorded telephone sales, prospective buyers often raised '
            'non-acceptances indirectly, while both parties initially negotiated them in veiled and delicate ways. The implication is not '
            '“decode every pause.” It is to treat objection handling as conversation, where the buyer may be protecting face, time or an '
            'exit.</p><p><b>Sunil Kumar Singh and colleagues, “Customer Query Handling in Sales Interactions” (2017)</b>, frames questions '
            'and objections as attempts to reduce decision uncertainty. The salesperson is a knowledge broker, not merely a persuader. '
            'That makes evidence proportional: answer the information gap the buyer actually has, rather than reciting a prepared '
            "rebuttal. A clinic's “too expensive” may be a cash-flow condition, a scope comparison or fear of implementation failure. Each "
            "needs a different response.</p><p><b>Jack Zenger and Joseph Folkman's listening work, summarised in the HBR guide (2022)</b>, "
            "challenges the passive sponge model. A strong listener gives the speaker's thinking energy, asks about what is said and "
            "unsaid, and adapts task, analytical, relational or critical listening to the conversation's purpose. The video is "
            'practitioner guidance, not a controlled sales-conversion estimate, so do not promise a percentage lift.</p><p><b>Neil '
            'Rackham, <i>SPIN Selling</i> (1988)</b>, and <b>The Mom Test by Rob Fitzpatrick (2013)</b> both support diagnosis before '
            'prescription: ask about past behaviour, problems, consequences and desired change. The live debate is how much structure '
            'helps before it becomes a script. Your ethical sequence is simple: acknowledge, clarify, explore, answer with proof, check, '
            'and accept no. In an Instagram DM or Gujarati clinic call, an easy opt-out is evidence that listening is not just a closing '
            'technique. It also protects the seller from building a pipeline full of polite maybes: a clear no is usable information, '
            'while a forced yes becomes churn, refund work or a damaged referral. Sources: https://doi.org/10.1177/0957926594005004002 '
            'https://doi.org/10.1007/s11747-017-0569-y https://www.youtube.com/watch?v=aDMtx5ivKK0 https://doi.org/10.1201/9781003073024',
  'names': [('Amy Gallo',
             'Author and HBR contributor whose active-listening guide emphasises purpose, attention, questions and avoiding information '
             'bubbles.'),
            ('Colin Clark, Paul Drew and Trevor Pinch',
             'Conversation analysts who studied implicit non-acceptances in real telephone-selling calls in 1994.')],
  'room': '"Before I answer the objection, can I make sure I understand the condition behind it?"',
  'explain': ('In 60 words: how should a seller handle a price objection?',
              'Pause and acknowledge that price matters. Ask what the buyer is comparing, what outcome would justify the investment and '
              'whether the issue is budget, scope, timing or risk. Explore before responding. Use a relevant baseline or case, state '
              'limits, offer a bounded alternative if it remains viable, check understanding and accept no when the fit is wrong.'),
  'recall': [('What can an objection be?',
              'A condition, misunderstanding, missing stakeholder, lack of fit or polite exit. It is not automatically a reflex to '
              'overcome.'),
             ('What is the listening loop?',
              'Pause, acknowledge, clarify, explore, respond with relevant evidence or a clean no, then check whether the real concern was '
              'resolved.'),
             ('Why are explicit objections not the whole story?',
              'Real-call research found non-acceptances were often implicit and negotiated delicately. Hesitation, timing and attempts to '
              'end the interaction also carry information.')],
  'use': ('A clinic owner says, “INR 15,000 is too much for a website,” then asks for a discount before discussing goals. What do you do?',
          'Ask what they are comparing and whether the concern is cash this month, scope, trust or expected return. Ask how patients '
          'currently find and contact the clinic, show only the relevant path, define pages, revisions, hosting and support, and offer a '
          'smaller honest scope or a later date. If the economics do not work, thank them and stop.'),
  'further': [('The Art of Active Listening | The Harvard Business Review Guide',
               'https://www.youtube.com/watch?v=aDMtx5ivKK0',
               'Video · verified oEmbed, 14:22'),
              ('Singh, Marinova, Singh and Evans, Customer Query Handling in Sales Interactions',
               'https://doi.org/10.1007/s11747-017-0569-y',
               'Paper · 2017 uncertainty reduction'),
              ('Fitzpatrick, The Mom Test', 'https://www.momtestbook.com/', 'Book · 2013 discovery questions')]}]

IMAGES = {'d15_gulliver': {'file': "File:First narrative illustration to Gulliver's Travels.jpg",
                  'credit': "Jonathan Swift, first narrative illustration to Gulliver's Travels, 1727, public domain, Wikimedia Commons",
                  'alt': '1727 public-domain illustration of Gulliver among the Lilliputians'},
 'd16_demo': {'file': 'File:Salesperson at Best Buy demonstrating Apple IPad.jpg',
              'credit': 'Tomwsulcer, Salesperson at Best Buy demonstrating Apple iPad, 2012, CC0, Wikimedia Commons',
              'alt': 'Salesperson demonstrating an iPad to a customer'},
 'd17_valueball': {'file': 'File:The great advertising ball of the season LCCN2012645462.jpg',
                   'credit': 'Puck #317, The great advertising ball of the season, 1883, public domain, Wikimedia Commons',
                   'alt': '1883 public-domain advertising illustration with price tags'},
 'd18_listening': {'file': 'File:Nicolaes Maes - The Listening Housewife - Wallace.jpg',
                   'credit': 'Nicolaes Maes, The Listening Housewife, circa 1655 to 1660, public domain, Wikimedia Commons',
                   'alt': 'Nicolaes Maes painting of a woman listening at a doorway'}}

GLOSS = [('Narrative transportation', 'Absorption in a story through attention, imagery and feeling.', 'Persuasion'),
 ('Identifiable victim effect', 'A named or pictured person can evoke more response than an equivalent statistical group.', 'Persuasion'),
 ('Case study', 'A bounded account of context, action, result and limitations.', 'Sales'),
 ('Perceived value', "A buyer's judged worth of an offer relative to cost and alternatives.", 'Persuasion'),
 ('Costly signalling', 'A cue that is credible partly because it is difficult to fake.', 'Persuasion'),
 ('Objection', 'A stated concern or non-acceptance about an offer.', 'Sales'),
 ('Active listening', 'An attentive, two-way process that checks meaning and invites detail.', 'Sales'),
 ('Risk reversal', 'A fair term that reduces uncertainty without pretending risk is zero.', 'Sales')]

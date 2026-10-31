"""No. 04 content module w1b (normalised from drafts/04/w1b.py, 27 Oct 2026). Plain data; see drafts/FORMAT-04.md."""

DAYS = [{'n': 5,
  'f': 'per',
  'title': 'How does the mind process a pitch?',
  'ep': ('Crash Course Media Literacy', 6, 'VXhLmkrN0-I', '09:51', 'Influence & Persuasion: Crash Course Media Literacy #6'),
  'seg': None,
  'img': 'd05_bernays',
  'imgcap': 'Edward Bernays in 1917, a reminder that media persuasion has a history, an audience and a designer.',
  'imgalt': 'Edward Bernays portrait in 1917',
  'hook': 'A person can watch the same advertisement while distracted, curious or already angry at the brand. The identical words do not '
          'enter an identical mind. Elaboration Likelihood Model research made that variability the starting point: sometimes we inspect '
          'arguments, and sometimes a fluent cue, a familiar face or a crowd does the work. The useful question is not whether a pitch is '
          'rational or emotional, but what processing conditions it meets.',
  'q': 'When does a buyer think through your evidence, and when do surface cues carry the decision?',
  'terms': [('Central route', 'Persuasion through attentive scrutiny of arguments and evidence.'),
            ('Peripheral route', 'Persuasion through cues such as authority, fluency, consensus or mood.'),
            ('Elaboration', 'The amount and quality of thought a person gives to a message.'),
            ('Heuristic', 'A quick judgment rule, such as experts are usually right.'),
            ('Persuasion knowledge', "A buyer's knowledge that someone is trying to influence them and how to cope.")],
  'pre': [('True or false: ELM says every person has a fixed central or peripheral personality.',
           'False. Route use depends on motivation, ability, relevance, distraction and the message. The same buyer can scrutinise a '
           'security promise and skim a font choice.'),
          ('If a beautiful website gets attention, has it proved the service works?',
           'No. Attention is an entry condition. Proof of outcomes still needs relevant evidence, and a polished cue can also trigger '
           'persuasion knowledge.')],
  'watch': ['How motivation and ability change the route a message takes',
            'Why authority, liking, consensus and scarcity are cues rather than guarantees',
            'The advertising fallacies, and the difference between influence and proof'],
  'fig': '<svg viewBox="0 0 1000 330" role="img" aria-label="Two routes from a message to an attitude change">\n'
         '<rect x="40" y="35" width="190" height="65" rx="12" class="s-card"/><text x="65" y="64" class="s-t">MESSAGE</text><text x="65" '
         'y="86" class="s-t-sm">claim plus cues</text>\n'
         '<path d="M230 67 L315 67" class="s-line" marker-end="url(#ah)"/>\n'
         '<rect x="315" y="35" width="190" height="65" rx="12" class="s-box-a"/><text x="340" y="64" class="s-t">MOTIVATION</text><text '
         'x="340" y="86" class="s-t-sm">care, relevance, stakes</text>\n'
         '<path d="M505 67 L590 67" class="s-line" marker-end="url(#ah)"/>\n'
         '<rect x="590" y="35" width="190" height="65" rx="12" class="s-box-j"/><text x="615" y="64" class="s-t">ABILITY</text><text '
         'x="615" y="86" class="s-t-sm">time, knowledge, attention</text>\n'
         '<path d="M780 67 L890 67" class="s-line-m" marker-end="url(#ahm)"/>\n'
         '<rect x="805" y="35" width="155" height="65" rx="12" class="s-card"/><text x="828" y="64" class="s-t">ATTITUDE</text><text '
         'x="828" y="86" class="s-t-sm">more durable change</text>\n'
         '<path d="M355 100 C300 170 180 180 180 225" class="s-line" marker-end="url(#ah)"/><path d="M700 100 C750 170 820 180 820 225" '
         'class="s-line-m" marker-end="url(#ahm)"/>\n'
         '<rect x="65" y="225" width="250" height="65" rx="12" class="s-card"/><text x="90" y="252" class="s-t-b">CENTRAL '
         'ROUTE</text><text x="90" y="274" class="s-t-sm">inspect arguments, counterargue</text>\n'
         '<rect x="685" y="225" width="250" height="65" rx="12" class="s-card"/><text x="710" y="252" class="s-t-b">PERIPHERAL '
         'ROUTE</text><text x="710" y="274" class="s-t-sm">use fluency, authority, consensus</text>\n'
         '</svg>',
  'figcap': 'ELM is conditional, not a two-type personality test. Motivation and ability make sustained argument scrutiny more likely, '
            'while low elaboration increases reliance on cues.',
  'insider': ["<b>ELM is a probability model, not System 1 versus System 2.</b> Petty and Cacioppo's 1986 model says motivation and "
              'ability raise the chance of elaboration, while both routes can operate together. Relevance, distraction, prior knowledge '
              'and accountability matter. A buyer can use a cue to choose what to inspect, then switch to argument scrutiny. Source: '
              'https://doi.org/10.1007/978-1-4612-4964-1',
              "<b>Argument quality matters most under involvement.</b> In Petty, Cacioppo and Schumann's 1983 advertising experiment, "
              'personal relevance changed whether strong arguments or source cues predicted attitudes. This is why a lodge owner comparing '
              'booking systems may inspect load-time evidence, while a casual scroller may remember only a trusted face. Source: '
              'https://doi.org/10.1086/208954',
              "<b>HSM adds a useful correction.</b> Chaiken's heuristic-systematic model allows quick heuristic processing and effortful "
              'systematic processing to coexist. A dentist may believe a recommendation because the speaker is a clinician and still check '
              'implementation details. Do not label a client irrational because they use a cue; cues save scarce attention. Source: '
              'https://doi.org/10.1037//0022-3514.39.5.752',
              '<b>Fluency is not truth, and media literacy is a defence.</b> Familiar, easy-to-process claims can feel credible, but the '
              'effect is not a licence to make weak claims smooth. The Crash Course episode usefully names appeal to emotion, false '
              'dilemma and red herring. Persuasion knowledge rises when a buyer detects a tactic, which can make a hidden commercial '
              'motive backfire. Source: https://doi.org/10.1086/209380'],
  'deeper': '<p><b>Petty and Cacioppo, <i>Communication and Persuasion</i> (1986),</b> gives the causal spine: motivation and ability '
            'raise elaboration, and elaboration makes argument quality consequential. Their model does not divide humanity into rational '
            'thinkers and gullible feelers. Relevance, distraction, knowledge and time change the probability of scrutiny. <b>Chaiken, '
            "Liberman and Eagly's heuristic-systematic model (1989)</b> adds that a quick rule and a reasoned check can run together. A "
            "trusted expert can be a starting shortcut, not a substitute for evidence. <b>O'Keefe, <i>Persuasion: Theory and Research</i> "
            '(2016),</b> is a useful guardrail because effects depend on audience, message and context rather than a single tactic. In a '
            'client proposal, a credible source can earn attention, but the buyer still needs a claim whose scope and uncertainty are '
            "visible. That is how a cue opens a door without pretending to be a result.</p><p><b>Greenwald's cognitive-response tradition "
            '(1968)</b> asks what thoughts the message elicits: agreement, counterargument, source derogation or irrelevant distraction. '
            "That moves attention from what the seller intended to what the buyer actually thought. <b>Friestad and Wright's persuasion "
            'knowledge model (1994)</b> explains why a buyer who recognises a tactic may change goals, distrust the agent or resist the '
            'offer. The same personalisation that feels helpful to one person can feel creepy to another when it reveals '
            'surveillance.</p><p>The live debate is not whether advertising persuades at all, but how durable and transferable effects '
            'are. Media exposure is selected, discussed and interpreted through prior identity, so a lab cue is not a universal sales '
            'lever. The stranger true story is that the famous fluency and cue vocabulary became popular partly because it gives '
            'advertisers a tidy button-board. Research instead says conditions matter. For you, state the evidence, label the commercial '
            "relationship, and make the buyer's route easy: a short claim for scanning, a proof link for scrutiny, and a clear way to "
            'decline. Source map: https://doi.org/10.1007/978-1-4612-4964-1, https://doi.org/10.1086/208954, '
            'https://doi.org/10.1037//0022-3514.39.5.752, https://doi.org/10.1086/209380, '
            'https://doi.org/10.1016/b978-1-4832-3071-9.50012-x.</p>',
  'names': [('Richard Petty and John Cacioppo', 'ELM researchers; their 1986 book linked involvement, ability and argument scrutiny.'),
            ('Shelly Chaiken',
             'Developed heuristic-systematic processing, including the coexistence of shortcuts and systematic thought.')],
  'room': '"What would make this buyer care enough to inspect the evidence?"',
  'explain': ('In 60 words: what does ELM actually predict?',
              'ELM predicts that motivation and ability affect the likelihood of elaboration. With high relevance, time and knowledge, '
              'argument quality has more influence and attitudes can be durable. With low elaboration, cues such as authority, fluency or '
              'consensus matter more. The routes are not personality types, and cues can guide attention before scrutiny begins.'),
  'recall': [('What two conditions increase central processing?',
              'Motivation to think about the issue and ability to do so, including time, attention and relevant knowledge.'),
             ('Why is a cue not proof?',
              'Authority, familiarity or consensus can guide judgement, but their relevance and trustworthiness must still be checked '
              'against evidence.'),
             ('What does persuasion knowledge do?',
              'It lets a recipient infer that someone is trying to influence them, identify tactics and adjust trust, attention or '
              'resistance.')],
  'use': ('A safari lodge asks why your redesign is worth USD 400 a month. What do you send?',
          'Use two layers. First, give a one-sentence outcome hypothesis tied to its booking path. Then offer a short before-and-after '
          'audit, a named metric to test and a permissioned case study. Do not lean on polished visuals alone. Ask what evidence the owner '
          'needs to decide, then make that evidence easy to inspect and easy to reject.'),
  'further': [('Crash Course Media Literacy #6', 'https://www.youtube.com/watch?v=VXhLmkrN0-I', 'Video · 09:51 · verified by oEmbed'),
              ('Petty and Cacioppo, Communication and Persuasion', 'https://doi.org/10.1007/978-1-4612-4964-1', 'Book · 1986 · ELM'),
              ('Friestad and Wright, The persuasion knowledge model', 'https://doi.org/10.1086/209380', 'Paper · 1994 · consumer coping')]},
 {'n': 6,
  'f': 'sal',
  'title': 'What do top sellers actually do differently?',
  'ep': ('The Futur', None, 'yyZ-d8wWJc4', '14:38', "The Real Job of a Sales Call (It's Not What You Think)"),
  'seg': ('00:00', '07:26', 'selling as helping a buyer decide, question control and objective listening'),
  'img': 'd06_merchants',
  'imgcap': "George Chinnery's nineteenth-century street scene with merchants selling wares, an image of selling as situated human "
            'exchange rather than a closing trick.',
  'imgalt': 'Nineteenth-century drawing of merchants selling wares',
  'hook': 'The most impressive seller in a sales call may be the person who speaks least. That sounds backwards in a culture of pitches, '
          'scripts and closing theatre. Research on sales performance points instead to knowledge, adaptiveness, cognitive ability and '
          'work engagement, while practitioner research asks whether the seller diagnosed the buyer before prescribing. The call succeeds '
          'when the next decision becomes clearer, not when the seller wins a verbal contest.',
  'q': 'What behaviours separate consultative diagnosis from confident-sounding product dumping?',
  'terms': [('Consultative selling', "Diagnosing a buyer's situation before proposing a fit."),
            ('Adaptive selling', 'Changing approach in response to the buyer, situation and feedback.'),
            ('SPIN', 'Situation, Problem, Implication and Need-payoff questioning.'),
            ('Implication question', 'A question that explores the cost or consequence of a problem.'),
            ('Talk-to-listen ratio', 'A descriptive measure of conversation airtime, not a universal target.')],
  'pre': [('True or false: the best seller is the most extroverted person in the room.',
           "False. Grant's 2013 study of 340 representatives found an inverted-U relationship, with ambiverts outperforming extreme "
           'introverts and extroverts in that sample.'),
          ('Should you force a 43:57 talk-to-listen ratio on every call?',
           'No. It is vendor data from Gong, not a law. Discovery needs listening; a technical demo or negotiation legitimately needs more '
           'seller explanation.')],
  'watch': ['The shift from pitching to helping a buyer make a decision',
            'How the video uses questions, concise summaries and perspective-taking',
            'Where its practitioner advice is useful, and where research evidence is still limited'],
  'fig': '<svg viewBox="0 0 1000 320" role="img" aria-label="Consultative sales call from problem to next decision">\n'
         '<rect x="35" y="40" width="175" height="70" rx="12" class="s-card"/><text x="60" y="70" class="s-t">SITUATION</text><text x="60" '
         'y="94" class="s-t-sm">what is happening now?</text>\n'
         '<path d="M210 75 L275 75" class="s-line" marker-end="url(#ah)"/>\n'
         '<rect x="275" y="40" width="175" height="70" rx="12" class="s-box-a"/><text x="300" y="70" class="s-t">PROBLEM</text><text '
         'x="300" y="94" class="s-t-sm">where is friction?</text>\n'
         '<path d="M450 75 L515 75" class="s-line-m" marker-end="url(#ahm)"/>\n'
         '<rect x="515" y="40" width="175" height="70" rx="12" class="s-box-j"/><text x="540" y="70" class="s-t">IMPLICATION</text><text '
         'x="540" y="94" class="s-t-sm">what does it cost?</text>\n'
         '<path d="M690 75 L755 75" class="s-line-m" marker-end="url(#ahm)"/>\n'
         '<rect x="755" y="40" width="210" height="70" rx="12" class="s-card"/><text x="780" y="70" class="s-t">NEED PAYOFF</text><text '
         'x="780" y="94" class="s-t-sm">what would better enable?</text>\n'
         '<rect x="135" y="195" width="730" height="65" rx="14" class="s-card"/><text x="165" y="223" class="s-t-b">DIAGNOSE BEFORE '
         'PRESCRIBING</text><text x="165" y="246" class="s-t-sm">buyer speaks, seller tests, both agree on a next decision</text>\n'
         '</svg>',
  'figcap': 'SPIN is a questioning map, not an interrogation script. The seller moves from present conditions to friction, consequences '
            'and a buyer-articulated payoff before recommending a next step.',
  'insider': ["<b>The academic sales-performance result is plural.</b> Verbeke, Dietz and Verwaal's 2011 meta-analysis found "
              'selling-related knowledge, adaptiveness, cognitive aptitude and work engagement positively related to performance, while '
              'role ambiguity was negative. No single talk ratio or personality trait explains a top seller. Source: '
              'https://doi.org/10.1007/s11747-010-0211-8',
              '<b>Ambiversion beat the extremes in one real sales sample.</b> Adam Grant studied 340 outbound representatives and found a '
              'curvilinear relationship between extraversion and sales performance: the middle performed best. This is a sample-specific '
              'association, not a hiring law, and it does not prove personality caused the result. Source: '
              'https://pubmed.ncbi.nlm.nih.gov/23567176/',
              "<b>SPIN challenged premature closing.</b> Rackham's Huthwaite programme reported more than 35,000 calls involving 10,000 "
              'salespeople in 23 countries and organised questions into Situation, Problem, Implication and Need-payoff. Treat those '
              "figures as the book's research account, not as a modern independently audited dataset. The durable idea is diagnosis before "
              'prescription. Source: https://doi.org/10.1201/9781003073024',
              '<b>Vendor ratios are directional, not universal.</b> Gong reports a 43:57 talk-to-listen ratio in its conversation dataset. '
              'Gong is a vendor with a commercial interest and a selected customer corpus, so label this vendor data. For you, measure '
              'positive replies, held meetings and wins by segment rather than rewarding silence or airtime. Source: '
              'https://www.gong.io/blog/talk-to-listen-ratio/'],
  'deeper': '<p><b>Verbeke, Dietz and Verwaal (2011)</b> provide the strongest research anchor for this day: a meta-analysis of '
            'sales-performance predictors, not a list of magic phrases. Knowledge of selling, adaptiveness, cognitive aptitude and work '
            'engagement were positive correlates; role ambiguity was negative. The lesson is a system of capability and clarity. '
            "<b>Grant's ambivert study (2013)</b> adds a memorable correction to the extrovert myth, but the 340-person outbound sample "
            'and correlational design limit what we can generalise.</p><p><b>Rackham, <i>SPIN Selling</i> (1988)</b> is practitioner '
            'research built from a very large observational programme. Situation questions establish context, Problem questions locate '
            'friction, Implication questions make consequences visible, and Need-payoff questions let the buyer articulate value. It is '
            'not a script or permission to manufacture pain. <b>Dixon and Adamson, <i>The Challenger Sale</i> (2011),</b> argues for '
            'teaching a relevant insight, tailoring it and taking control, but its famous high-performer percentages are often repeated '
            'without enough denominator and independent replication. Diagnosis plus a genuinely useful insight is safer than '
            'theatre.</p><p><b>The Futur video is also practitioner evidence.</b> Chris Do says the job is to help a buyer decide, to ask '
            'rather than over-talk, and to summarise the most generous interpretation of a concern. That aligns with active listening, but '
            'its talk numbers and pricing stories are not controlled causal tests. The live debate is measurement: a short call can be '
            "excellent or evasive, and a long explanation can be necessary or self-protective. For you, record the buyer's current state, "
            'consequence, decision criteria, owner and next step. Source map: https://doi.org/10.1007/s11747-010-0211-8, '
            'https://pubmed.ncbi.nlm.nih.gov/23567176/, https://doi.org/10.1201/9781003073024. A practical audit asks whether the seller '
            'identified a real decision, not whether the buyer sounded enthusiastic. The strongest next step may be a smaller paid '
            'diagnostic, a referral elsewhere or a clear no. That restraint is part of consultative competence, because a bad-fit customer '
            'creates delivery risk, churn and damaged trust after the close.</p>',
  'names': [('Neil Rackham', 'Sales researcher and author of SPIN Selling, based on Huthwaite call research.'),
            ('Adam Grant', 'Organisational psychologist who studied extraversion and performance among 340 outbound representatives.')],
  'room': '"Before I recommend anything, may I understand the cost of leaving this problem as it is?"',
  'explain': ('In 60 words: what does consultative selling add?',
              'Consultative selling treats the call as diagnosis and joint decision-making. The seller learns the current state, '
              'identifies a real problem, tests implications, understands desired outcomes and only then recommends a fit. Adaptiveness '
              'means changing the conversation to the buyer rather than reciting a script. It still requires a clear price and next step, '
              'without manufactured pressure.'),
  'recall': [('What four SPIN question types are used?', 'Situation, Problem, Implication and Need-payoff.'),
             ('What did Grant find?',
              'In a sample of 340 outbound representatives, sales performance showed an inverted-U relationship with extraversion, with '
              'ambiverts performing better than extremes.'),
             ('Why is the 43:57 ratio not a rule?',
              'It is a Gong vendor benchmark from a selected conversation dataset, and the right mix varies by discovery, demo, technical '
              'explanation and negotiation.')],
  'use': ('A dental clinic says its receptionist misses WhatsApp enquiries. How should you run discovery?',
          'Ask what happens now, where enquiries drop, how many are missed, what a missed appointment is worth, who handles handoff and '
          "what a safe pilot would require. Summarise the clinic's words, verify the consequence, then propose a bounded automation with "
          'human escalation. Quote INR 20,000 with scope and exclusions, not a vague promise to increase revenue.'),
  'further': [('The Futur, The Real Job of a Sales Call',
               'https://www.youtube.com/watch?v=yyZ-d8wWJc4',
               'Video · 14:38 · verified by oEmbed · practitioner/vendor'),
              ('Rackham, SPIN Selling', 'https://doi.org/10.1201/9781003073024', 'Book · 1988 · consultative questioning'),
              ('Verbeke, Dietz and Verwaal, Drivers of sales performance',
               'https://doi.org/10.1007/s11747-010-0211-8',
               'Meta-analysis · 2011 · sales performance')]},
 {'n': 7,
  'f': 'per',
  'title': 'Why do losses loom larger than gains?',
  'ep': ('Crash Course Economics', 27, 'dqxQ3E1bubI', '~10:30', 'Behavioral Economics: Crash Course Economics #27'),
  'seg': None,
  'img': 'd07_kahneman',
  'imgcap': 'Daniel Kahneman in 2009. Prospect theory changed the question from what an abstractly rational agent should choose to how '
            'reference points shape experienced gains and losses.',
  'imgalt': 'Daniel Kahneman portrait in 2009',
  'hook': 'A five rupee fee can change behaviour more than a five rupee bonus, even when the arithmetic is identical. That is the puzzle '
          'behind plastic-bag charges, reference prices and the fear of losing a client. Prospect theory gives the intuition, but the '
          'slogan that losses are always twice as painful is too neat. The modern debate asks when loss aversion appears, how reference '
          'points are measured and whether nudge effects survive publication-bias correction.',
  'q': "How can a seller use framing and defaults without turning a buyer's fear into a hidden lever?",
  'terms': [('Prospect theory',
             'A model in which people evaluate outcomes relative to a reference point, with curved value and probability weighting.'),
            ('Loss aversion', 'The tendency for some losses to matter more than equivalent gains, under specified reference points.'),
            ('Reference point', 'The comparison state that makes an outcome feel like a gain or loss.'),
            ('Anchoring', 'The pull of an initial number or comparison point on later judgement.'),
            ('Nudge', 'A change in choice architecture that alters behaviour without removing options or materially changing incentives.')],
  'pre': [('True or false: every loss is exactly twice as painful as the same gain is pleasurable.',
           'False. The two-to-one slogan is not a universal constant. Gal and Rucker argued in 2018 that general loss aversion is often '
           'measurement-dependent, while other work finds robust effects in defined risky-choice and consumer contexts.'),
          ('If a default increases uptake, has the nudge definitely worked?',
           'Not necessarily. Defaults can have real average effects, but nudge size varies by context and publication-bias correction. A '
           'live test needs a pre-specified outcome, opt-out visibility and null results.')],
  'watch': ['Reference dependence, framing and the ultimatum game',
            'The plastic-bag bonus versus tax example, and what it does and does not prove',
            'Nudges, defaults and why a famous average effect needs bias checks'],
  'fig': '<svg viewBox="0 0 1000 340" role="img" aria-label="Reference points turn the same outcome into a gain or loss">\n'
         '<rect x="55" y="42" width="250" height="65" rx="12" class="s-card"/><text x="80" y="70" class="s-t">REFERENCE POINT</text><text '
         'x="80" y="93" class="s-t-sm">expected price or status quo</text>\n'
         '<path d="M305 74 L375 74" class="s-line" marker-end="url(#ah)"/>\n'
         '<rect x="375" y="42" width="250" height="65" rx="12" class="s-box-a"/><text x="400" y="70" class="s-t">FRAME</text><text x="400" '
         'y="93" class="s-t-sm">gain, loss, default, anchor</text>\n'
         '<path d="M625 74 L695 74" class="s-line-m" marker-end="url(#ahm)"/>\n'
         '<rect x="695" y="42" width="250" height="65" rx="12" class="s-box-j"/><text x="720" y="70" class="s-t">CHOICE</text><text '
         'x="720" y="93" class="s-t-sm">accept, reject, delay, compare</text>\n'
         '<path d="M500 107 L500 165" class="s-line" marker-end="url(#ah)"/>\n'
         '<rect x="90" y="185" width="360" height="75" rx="12" class="s-card"/><text x="120" y="215" class="s-t-b">GAIN FRAME</text><text '
         'x="120" y="240" class="s-t-sm">save INR 5,000 this month</text>\n'
         '<rect x="550" y="185" width="360" height="75" rx="12" class="s-card"/><text x="580" y="215" class="s-t-b">LOSS FRAME</text><text '
         'x="580" y="240" class="s-t-sm">avoid losing INR 5,000 this month</text>\n'
         '<text x="90" y="305" class="s-t-sm">Honest framing clarifies the same consequences. It does not invent a loss.</text>\n'
         '</svg>',
  'figcap': 'A reference point turns the same INR 5,000 into a saving or an avoided loss. Honest framing names the comparison and '
            "preserves the buyer's ability to opt out.",
  'insider': ["<b>Prospect theory is not a sales licence to scare people.</b> Kahneman and Tversky's 1979 model predicts reference "
              'dependence, diminishing sensitivity and loss aversion in decisions under risk. It does not supply a fixed two-to-one '
              'multiplier for every purchase. Source: https://doi.org/10.2307/1914185',
              "<b>The loss-aversion debate is real.</b> Gal and Rucker's 2018 review argued that broad claims often confuse loss aversion "
              'with status quo, diminishing sensitivity, asymmetrical attention or choice-task artefacts. Other researchers find robust '
              'loss aversion in specified risky-choice and consumer settings. Status: partly, checked Oct 2026. Source: '
              'https://doi.org/10.1037/xge0000340',
              "<b>Defaults are stronger than many nudges, but not magic.</b> Jachimowicz et al.'s meta-analysis covered 58 studies and "
              'pooled N = 73,675, finding d = 0.68, with moderators and occasional negative effects. A default must be easy to reject and '
              "transparent about the chooser's interest. Source: https://doi.org/10.1017/bpp.2018.43",
              '<b>The nudge average is under publication-bias dispute.</b> Mertens et al. reported d = 0.43 before correction, d = 0.31 '
              'under moderate bias assumptions and d = 0.08 under a severe assumption. Maier et al. reported no evidence after bias '
              'correction, while replies dispute estimators and generality. Status: partly, checked Oct 2026. Sources: '
              'https://doi.org/10.1073/pnas.2107346118 and https://doi.org/10.1073/pnas.2200300119'],
  'deeper': '<p><b>Kahneman and Tversky, prospect theory (1979),</b> replaces an abstract wealth total with a value function around a '
            'reference point. Sensitivity bends as outcomes grow, and probabilities are not treated as transparent weights. This explains '
            'why a fee can feel different from a bonus and why a price change is interpreted against an expected price. It does not mean '
            'every customer is irrational or that fear beats evidence.</p><p><b>Gal and Rucker (2018)</b> are the essential corrective: '
            'loss aversion is not one context-free law. Apparent asymmetry can arise from reference-point choice, diminishing sensitivity, '
            'attention, status quo effects or the way a task is framed. Other work finds reliable loss aversion in particular risky-choice '
            'and consumer settings, so the honest status is partly supported, not debunked. <b>Jachimowicz et al. (2019)</b> found a '
            'substantial average default effect across 58 studies and 73,675 participants, but moderators matter. A default can signal '
            'endorsement or exploit inertia, and those mechanisms are ethically different.</p><p><b>Mertens et al. (2022)</b> estimated an '
            'average nudge effect of d = 0.43 before publication-bias correction, falling to 0.31 under moderate and 0.08 under severe '
            'assumptions. <b>Maier et al. (2022)</b> argued the effect disappears after correction; later replies challenged choices of '
            'estimator and the expectation of one universal effect. The stranger true story behind the nudge boom is not a tiny '
            'behavioural trick but a measurement lesson: a memorable field success can be selected from many quiet nulls. For you, never '
            'invent a loss, fake scarcity or hide opt-out. State the baseline, show the gain and avoided cost, disclose assumptions, and '
            'let the buyer choose. Sources: https://doi.org/10.2307/1914185, https://doi.org/10.1037/xge0000340, '
            'https://doi.org/10.1017/bpp.2018.43, https://doi.org/10.1073/pnas.2107346118, https://doi.org/10.1073/pnas.2200300119. '
            '<b>Thaler and Sunstein, <i>Nudge</i> (2008),</b> remains a useful design vocabulary, but its policy manifesto should not be '
            'mistaken for an effect-size guarantee. A nudge is ethically stronger when the choice architect can explain the mechanism, '
            'measure the outcome and accept that the intervention may fail or backfire.</p>',
  'names': [('Daniel Kahneman and Amos Tversky',
             'Prospect theory authors; their 1979 paper formalised reference dependence and loss aversion.'),
            ('Ralph Hertwig and colleagues',
             'Researchers involved in contemporary judgement, decision and evidence debates that test when behavioural effects '
             'generalise.')],
  'room': '"What is the real reference point, and would I show the buyer the same choice without the frame?"',
  'explain': ('In 60 words: what is the careful modern claim about loss aversion?',
              'People often respond more strongly to losses than equivalent gains relative to a reference point, especially in specified '
              'decision contexts. But the size and presence of the effect depend on task, stakes, reference point and measurement. The '
              'two-to-one slogan is not a law. Use transparent framing, real costs and easy opt-out rather than manufactured fear.'),
  'recall': [('What does a reference point do?',
              'It determines whether an outcome is experienced and described as a gain, loss or status quo change.'),
             ('What did the nudge debate question?',
              'Whether average effects remain substantial after correcting for publication bias, and whether one pooled effect generalises '
              'across contexts.'),
             ('What is an ethical default?',
              'A transparent, reversible choice architecture with an easy opt-out, disclosed interests and evidence from the actual '
              'setting.')],
  'use': ('A lodge owner fears losing high-season bookings and is considering your USD 500 retainer. How do you frame it?',
          'Do not say the lodge will lose a guaranteed amount. Show the current enquiry-to-booking baseline, the assumptions behind a '
          'plausible improvement, the retainer cost, a bounded pilot and the stop rule. Present both the upside and the downside. A real '
          'capacity or deadline can be stated, but never use a fake countdown or hidden renewal.'),
  'further': [('Crash Course Economics #27',
               'https://www.youtube.com/watch?v=dqxQ3E1bubI',
               'Video · approximately 10:30 · verified by oEmbed; reliable listings call it about 10.5 minutes'),
              ('Kahneman and Tversky, Prospect Theory', 'https://doi.org/10.2307/1914185', 'Paper · 1979 · reference dependence'),
              ('Mertens et al., Choice architecture interventions',
               'https://doi.org/10.1073/pnas.2107346118',
               'Meta-analysis · 2022 · nudge effects and bias correction')]}]

IMAGES = {'d05_bernays': {'file': 'File:Edward Bernays cropped.png',
                 'credit': 'Bain News Service, Edward Bernays, 1917, public domain',
                 'alt': 'Edward Bernays portrait in 1917'},
 'd06_merchants': {'file': 'File:George Chinnery - Street Scene with Merchants Selling Wares - B1977.14.4173 - Yale Center for British '
                           'Art.jpg',
                   'credit': 'George Chinnery, Street Scene with Merchants Selling Wares, circa 1843, public domain',
                   'alt': 'Nineteenth-century drawing of merchants selling wares'},
 'd07_kahneman': {'file': 'File:Daniel Kahneman (3283955327).jpg',
                  'credit': 'nrkbeta, Daniel Kahneman, 2009, CC BY-SA 2.0',
                  'alt': 'Daniel Kahneman portrait in 2009'}}

GLOSS = [('Central route', 'Persuasion through attentive scrutiny of arguments and evidence.', 'Persuasion'),
 ('Adaptive selling', 'Changing an approach in response to buyer, situation and feedback.', 'Sales'),
 ('SPIN questioning', 'Situation, Problem, Implication and Need-payoff discovery questions.', 'Sales'),
 ('Reference point', 'The comparison state that makes an outcome feel like a gain or loss.', 'Persuasion'),
 ('Loss aversion', 'A context-dependent tendency for losses to weigh more than equivalent gains.', 'Persuasion'),
 ('Nudge', 'Choice architecture that changes behaviour without removing options.', 'Persuasion'),
 ('Persuasion knowledge', "A recipient's understanding of influence tactics and how to cope with them.", 'Persuasion')]

TIEUP = {'title': 'Week 1 tie-up: why people say yes',
 'intro': 'Week 1 moved from rhetoric to selling, trust, routes of processing, diagnosis and behavioural economics. The through-line is '
          'not a bag of buttons. It is a buyer deciding under limited attention and uncertainty, while an honest seller makes fit, '
          'evidence, cost and choice clearer.',
 'rows': [('Day 1 · rhetoric and ethics',
           'Ethos, pathos, logos and kairos describe situated communication; persuasion respects agency while manipulation hides or '
           'exploits the process.',
           '"What would make this influence honest and inspectable?"'),
          ('Day 2 · what selling is',
           'Selling is helping a buyer decide, not always be closing; history gave us scripts, but modern buying needs useful diagnosis '
           'and proof.',
           '"What decision is the buyer trying to make?"'),
          ('Day 3 · why people say yes',
           "Cialdini's principles are hypotheses with evidence boundaries, not universal buttons; real social proof and real scarcity beat "
           'theatre.',
           '"What evidence would remain if the cue disappeared?"'),
          ('Day 4 · trust',
           'Ability, benevolence and integrity reduce perceived risk; a small studio earns trust through relevant proof, boundaries and '
           'reliable follow-through.',
           '"What can this buyer verify before trusting me?"'),
          ('Day 5 · processing',
           'Motivation and ability change whether a buyer scrutinises arguments or uses cues; make both the short claim and the proof '
           'available.',
           '"What would make this buyer inspect the evidence?"'),
          ('Day 6 · consultative sales',
           'Top performance is linked to knowledge, adaptiveness and engagement; diagnose current state, implications and payoff before '
           'prescribing.',
           '"What is the cost of leaving this problem unchanged?"'),
          ('Day 7 · behavioural economics',
           'Reference points, defaults, framing and nudges can change choice, but loss aversion and nudge averages have real debates and '
           'publication-bias limits.',
           '"What is the reference point, and is the choice still fair without my frame?"')],
 'boss': ('A safari lodge owner says, "Your USD 400 monthly retainer sounds expensive. Another agency promises the same thing for USD 150, '
          'and I do not want a fake countdown." Give a response that transfers Week 1, not a pressure script.',
          '<p>First acknowledge the comparison and refuse fake urgency. Ask what outcomes, scope, response time, booking path and proof '
          "the USD 150 offer includes. Establish the lodge's current baseline and decision criteria before arguing price. Then state your "
          'bounded scope, assumptions, exclusions and a testable pilot, with a real stop date only if capacity genuinely requires it. Show '
          'one relevant case or audit, disclose uncertainty, and let the owner choose between a viable smaller scope, the proposed '
          'retainer or no deal. The honest levers are clarity, proof, real scarcity and real social proof, not fear.</p>'),
 'calib': 'Return to your Day 1 baseline: rate yourself from 1 to 5 on explaining why a buyer says yes without reducing people to buttons, '
          'and write one sentence on what changed in your view of honest influence.'}

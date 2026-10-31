"""No. 04 content module w2b (normalised from drafts/04/w2b.py, 27 Oct 2026). Plain data; see drafts/FORMAT-04.md."""

DAYS = [{'n': 12,
  'f': 'sal',
  'title': 'How do you ask questions without interrogating?',
  'ep': ('Techstars', None, 'OTkP2JDeGWM', '~7:00', 'Customer Discovery: What Do You Ask, with Justin Wilcox'),
  'seg': None,
  'img': 'd12_interview',
  'imgcap': 'A public-domain FEMA interview photograph. Good discovery is not an interrogation: the listener helps the other person '
            'reconstruct what actually happened.',
  'imgalt': 'Two people in a public service interview',
  'hook': 'A founder can ask a prospect whether they would buy an AI receptionist and receive a warm yes that means almost nothing. Ask '
          'about the last missed patient message, and the conversation acquires dates, workarounds, emotion and cost. Justin Wilcox built '
          'his discovery lesson around this mismatch between predictions and evidence. The oddest part is that the most useful sales call '
          'may contain no pitch at all.',
  'q': 'How can a question reveal a real problem without manufacturing one?',
  'terms': [('Discovery', 'a structured, mutual investigation of problem, impact, fit and buying process'),
            ('Situation question', 'a question that establishes what happens now, without assuming failure'),
            ('Implication question', 'a question that explores consequences, cost or risk of a problem'),
            ('Need-payoff question', 'a question that lets the buyer articulate the value of a better state'),
            ('Current state', 'the observed process, workaround and constraint that exist before a change')],
  'pre': [('True or false: asking a clinic owner whether they would buy an AI receptionist is strong evidence of demand.',
           'False. It is a prediction, often shaped by politeness or the pitch. Ask about the last real enquiry, the current workaround '
           'and what they already paid to fix it.'),
          ('Should every discovery call follow SPIN in exactly the same order?',
           "No. SPIN is a useful observation-based framework, not a ritual. Start with the buyer's language and use only the questions "
           'needed to understand fit and consequence.')],
  'watch': ["Wilcox's rule against pitching while learning",
            'Why past and present behaviour beat would-you-buy predictions',
            'The sequence: last time, hardest part, why hard, current workaround, why that workaround fails'],
  'fig': '<svg viewBox="0 0 1000 360" role="img" aria-label="A discovery staircase from observed situation to buyer-owned payoff">\n'
         '<rect x="35" y="260" width="210" height="60" rx="12" class="s-card"/><text x="60" y="288" class="s-t">SITUATION</text><text '
         'x="60" y="308" class="s-t-sm">what happens now?</text>\n'
         '<path d="M245 290 L285 290" class="s-line" marker-end="url(#ah)"/>\n'
         '<rect x="285" y="205" width="210" height="60" rx="12" class="s-box-a"/><text x="310" y="233" class="s-t">PROBLEM</text><text '
         'x="310" y="253" class="s-t-sm">where does it fail?</text>\n'
         '<path d="M495 235 L535 235" class="s-line-m" marker-end="url(#ahm)"/>\n'
         '<rect x="535" y="150" width="210" height="60" rx="12" class="s-box-j"/><text x="560" y="178" class="s-t">IMPLICATION</text><text '
         'x="560" y="198" class="s-t-sm">why does it matter?</text>\n'
         '<path d="M745 180 L785 180" class="s-line-m" marker-end="url(#ahm)"/>\n'
         '<rect x="785" y="95" width="180" height="60" rx="12" class="s-card"/><text x="805" y="123" class="s-t">NEED-PAYOFF</text><text '
         'x="805" y="143" class="s-t-sm">what better means</text>\n'
         '<path d="M125 260 C125 125 410 65 785 95" class="s-dash" marker-end="url(#ah)"/>\n'
         '<text x="45" y="55" class="s-t-b">GOOD QUESTIONS FOLLOW EVIDENCE</text><text x="45" y="80" class="s-t-sm">Past behaviour beats a '
         'flattering prediction about the future.</text>\n'
         '</svg>',
  'figcap': 'SPIN gives a useful staircase, but the buyer supplies the evidence. If the conversation jumps straight to need-payoff, the '
            "seller is probably writing the buyer's answer for them.",
  'insider': ["<b>SPIN is field observation, not a magic script.</b> Neil Rackham's Huthwaite research is reported as more than 35,000 "
              'calls involving 10,000 salespeople in 23 countries over 12 years. Situation, Problem, Implication and Need-payoff questions '
              'are most useful as a diagnostic sequence, especially in larger sales. The original proprietary study does not prove that '
              'every service call needs every step. Source: https://doi.org/10.1201/9781003073024',
              '<b>Wilcox corrects the flattering hypothetical.</b> In the Techstars lesson, he recommends a story about the last time the '
              'problem happened, then asks what was hardest, why it was hard, how the person solves it now and why that solution is not '
              'great. This is evidence seeking, not a covert pitch. Source: https://www.youtube.com/watch?v=OTkP2JDeGWM',
              '<b>Listening can clarify a view without making it correct.</b> Itzchakov, DeMarree, Kluger and Turjeman-Levi ran five '
              "experiments, including one preregistered study. High-quality listening increased speakers' attitude clarity, but not "
              "attitude correctness or intention to persuade. In sales, attentive listening can reveal a buyer's priorities, but it cannot "
              "certify that the buyer's diagnosis is true. Source: https://doi.org/10.1177/0146167217747874",
              "<b>Use the gap as a hypothesis, never as seller drama.</b> Keenan's Gap Selling maps current state, desired future state "
              'and the impact of staying put. Its useful correction is diagnosis before demo; its weak spot is that a seller can inflate '
              'pain by asking leading questions. Ask for observed examples, not theatrical suffering. Source: '
              'https://salesgrowth.com/gap-selling-book/'],
  'deeper': "<p><b>Three discovery traditions converge on one discipline.</b> Neil Rackham's <i>SPIN Selling</i> (1988) is the "
            'practitioner account built from observed sales calls: understand the situation, expose a problem, explore implications, then '
            "let the buyer state a need-payoff. Rob Fitzpatrick's <i>The Mom Test</i> (2013) pushes the same epistemic instinct into "
            'founder interviews: ask about recent behaviour, existing workarounds and money already spent, not whether a friendly person '
            "likes your idea. Keenan's <i>Gap Selling</i> (2018) names the distance between current and future state and asks what the gap "
            'costs. These are useful lenses, not independent laws of buyer psychology.</p><p><b>The live debate is evidence versus '
            'performance.</b> A question can sound consultative while smuggling in the answer: How much revenue are you losing because '
            'your website is slow? is not discovery if speed has not been measured. Ask What happens after an Instagram visitor taps Book '
            "now? Then request one recent example. Wilcox's video adds a valuable constraint: future predictions are especially easy to "
            'contaminate because a buyer is responding to your imagined solution. A past event can still be misremembered, so triangulate '
            'with analytics, logs, invoices or a second person.</p><p><b>Listening is also a persuasion event, which creates an ethical '
            'boundary.</b> The five experiments by Itzchakov and colleagues found that good listening made people clearer about their own '
            'attitudes, not more correct. That can help a clinic owner articulate a workflow, but you must not use a vulnerable disclosure '
            'as a pressure lever. Reflect the account, ask what was missed, and allow a no-fit outcome. The test of discovery is not how '
            'much pain the seller extracted. It is whether both sides leave with a more accurate current state, a measurable desired state '
            'and a voluntary next step.</p><p><b>For MTRX, keep a four-line record.</b> Write the observed event, the consequence the '
            'buyer confirms, the workaround already tried, and the decision constraint. For a safari lodge, that might be a mobile booking '
            'handoff that breaks during peak season. For a clinic, it might be an unanswered WhatsApp enquiry and a receptionist '
            'workaround. Only then show the smallest relevant workflow.</p>',
  'names': [('Neil Rackham', '1946 to present. Researcher and author of SPIN Selling, based on observed sales conversations.'),
            ('Justin Wilcox', 'Founder of Nimbus Health and Customer Dev Labs; Techstars teacher of evidence-seeking interviews.')],
  'room': 'Before I recommend anything, may I understand what happens today, what it costs you, and what a better outcome would look like?',
  'explain': ('In 60 words: what makes a discovery question useful?',
              'A useful question asks for observable behaviour, not applause for a proposed solution. Start with a recent event, '
              'reconstruct the process, find the hardest point, ask why it mattered, and learn the workaround. Then test the desired '
              'outcome and decision constraint. The buyer supplies evidence; the seller supplies attention, structure and an honest fit '
              'check.'),
  'recall': [("What are SPIN's four question types?",
              'Situation, Problem, Implication and Need-payoff. They are a sequence for diagnosing a problem, not mandatory wording.'),
             ('Why is tell me about the last time stronger than would you buy?',
              'A recent event contains behaviour, context and workaround evidence. A hypothetical answer is easily shaped by politeness, '
              "imagination or the seller's pitch."),
             ('What did the listening experiments find?',
              'Across five experiments, high-quality listening increased attitude clarity, but not attitude correctness or intention to '
              'persuade.')],
  'use': ('A dental clinic owner says patients often miss appointments and asks for an AI reminder bot. What do you ask first?',
          'Ask about the last missed appointment: how it was booked, when reminders were sent, who handled the reply, what the clinic did '
          'next and what the missed slot cost. Then ask what they have already tried and who approves a change. Only demo reminders if the '
          'evidence points there, and define human handoff and data boundaries.'),
  'further': [('Justin Wilcox, Customer Discovery: What Do You Ask',
               'https://www.youtube.com/watch?v=OTkP2JDeGWM',
               'Video · past behaviour and no pitching'),
              ('Neil Rackham, SPIN Selling', 'https://doi.org/10.1201/9781003073024', 'Book · discovery framework'),
              ('Itzchakov et al., The Listener Sets the Tone',
               'https://doi.org/10.1177/0146167217747874',
               'Paper · five listening experiments')]},
 {'n': 13,
  'f': 'per',
  'title': 'What happens in two brains that are really communicating?',
  'ep': ('TED', None, 'FDhlOovaGrI', '14:52', 'This is your brain on communication | Uri Hasson'),
  'seg': None,
  'img': 'd13_telephone',
  'imgcap': 'Isa Pola as a telephone operator in a 1932 public-domain film still. A channel carries a message, but communication succeeds '
            'only when speaker and listener build enough common ground.',
  'imgalt': 'A 1932 public-domain telephone operator film still',
  'hook': 'The 7-38-55 rule is repeated in sales rooms as if most meaning lives outside words. The stranger truth is much narrower: Albert '
          'Mehrabian studied brief, emotionally inconsistent messages about liking and disliking, not presentations, DMs or all human '
          'communication. In a different line of research, Uri Hasson scanned brains during stories and found speaker-listener neural '
          'coupling related to understanding. One famous number is misapplied; one exciting finding is often overextended.',
  'q': 'When does a message become shared meaning rather than merely transmitted sound?',
  'terms': [('Neural coupling', 'time-linked similarity between speaker and listener brain activity during communication'),
            ('Entrainment', 'alignment of neural or physiological responses to a structured signal'),
            ('Common ground', 'shared knowledge and assumptions that let a message be interpreted'),
            ('Incongruent message', 'a message whose words, voice and face do not point to the same attitude'),
            ('Behavioural mimicry', 'subtle coordination of mannerisms or language, not theatrical copying')],
  'pre': [('True or false: Mehrabian proved that words carry only 7 percent of meaning in every conversation.',
           'False. His studies used narrow, inconsistent messages about feelings and attitudes. The percentages do not describe lectures, '
           'sales calls, technical explanations or ordinary communication.'),
          ('Does neural coupling mean a speaker can upload a memory into another brain?',
           'No. Coupling is measured statistical alignment in brain activity during a task. It is associated with comprehension in these '
           'studies, not literal memory transfer or mind reading.')],
  'watch': ["Hasson's progression from sound to words to coherent story",
            'The English and Russian story comparison and the role of common meaning',
            'Why dialogue and checking understanding are safer than assuming alignment'],
  'fig': '<svg viewBox="0 0 1000 360" role="img" aria-label="Communication alignment from sound to meaning, with the 7 38 55 myth '
         'corrected">\n'
         '<rect x="35" y="55" width="190" height="70" rx="12" class="s-card"/><text x="60" y="84" class="s-t">SOUND</text><text x="60" '
         'y="106" class="s-t-sm">acoustic signal</text>\n'
         '<path d="M225 90 L280 90" class="s-line" marker-end="url(#ah)"/>\n'
         '<rect x="280" y="55" width="190" height="70" rx="12" class="s-box-a"/><text x="305" y="84" class="s-t">WORDS</text><text x="305" '
         'y="106" class="s-t-sm">shared code</text>\n'
         '<path d="M470 90 L525 90" class="s-line-m" marker-end="url(#ahm)"/>\n'
         '<rect x="525" y="55" width="190" height="70" rx="12" class="s-box-j"/><text x="550" y="84" class="s-t">MEANING</text><text '
         'x="550" y="106" class="s-t-sm">common ground</text>\n'
         '<path d="M715 90 L770 90" class="s-line-m" marker-end="url(#ahm)"/>\n'
         '<rect x="770" y="55" width="195" height="70" rx="12" class="s-card"/><text x="795" y="84" class="s-t">ALIGNMENT</text><text '
         'x="795" y="106" class="s-t-sm">understood outcome</text>\n'
         '<rect x="80" y="190" width="840" height="110" rx="15" class="s-card"/><text x="110" y="220" class="s-t-b">7 / 38 / 55 IS NOT ALL '
         'COMMUNICATION</text><text x="110" y="248" class="s-t-sm">It estimates relative weight only in narrow, inconsistent liking '
         'messages.</text><text x="110" y="274" class="s-t-sm">Content, context, voice, face and relationship jointly carry '
         'meaning.</text>\n'
         '</svg>',
  'figcap': 'The real communication pipeline is not a percentage pie. Meaning emerges from content, voice, face, context, relationship and '
            'shared ground, then must be checked in the listener.',
  'insider': ["<b>The 7-38-55 rule is a myth outside its narrow laboratory question, checked Oct 2026.</b> Mehrabian and Wiener's 1967 "
              'study used single spoken words with positive or negative vocal tone to examine inconsistent communications. Mehrabian and '
              'Ferris combined facial expressions with vocal tone, using brief attitude stimuli. The famous ratio was derived for the '
              'relative impact of word meaning, tone and facial expression when communicating feelings in conflict, not for all '
              'communication. Sources: https://doi.org/10.1037/h0024532 and https://doi.org/10.1037/h0024648',
              '<b>Hasson measured alignment, not telepathy.</b> Stephens, Silbert and Hasson (2010) recorded fMRI activity from a speaker '
              'telling an unrehearsed story and listeners hearing it. Speaker activity predicted listener activity; coupling vanished when '
              'communication failed, and greater anticipatory coupling tracked better story comprehension. It was a neuroimaging '
              'correlation in a controlled task, not proof that a pitch enters another mind. Source: '
              'https://doi.org/10.1073/pnas.1008662107',
              '<b>Good listening changes clarity, not truth.</b> In five experiments, Itzchakov and colleagues found empathic, attentive '
              'and nonjudgmental listening reduced social anxiety and increased attitude clarity, but not attitude correctness. For a '
              'seller, reflective listening can help a buyer articulate priorities, while verification still needs data, examples and a '
              'clear success measure. Source: https://doi.org/10.1177/0146167217747874',
              '<b>Mirroring has a small, specific evidence base.</b> Maddux, Mullen and Galinsky studied 104 MBA students in an employment '
              'negotiation. Instructed mimickers actually mimicked about 32.9 percent of the time; dyads with mimicry had mean joint gain '
              '12,511.76 points versus 11,738.89 in controls. That supports subtle coordination in one task, not NLP eye-movement recipes '
              'or copying an accent. Source: https://doi.org/10.1016/j.jesp.2007.02.003'],
  'deeper': "<p><b>Start with the original 7-38-55 puzzle.</b> Albert Mehrabian and Morton Wiener's <i>Decoding of Inconsistent "
            "Communications</i> (1967) and Mehrabian and Susan Ferris's <i>Inference of Attitudes from Nonverbal Communication in Two "
            'Channels</i> (1967) used highly constrained stimuli: brief words, vocal tones and facial photographs whose attitude signals '
            'could conflict. The studies estimated how people inferred positive or negative feeling under that conflict. Their result '
            'became a portable slogan, but a ratio from an incongruent affect task cannot be the information budget for a safari website '
            'audit or an engineering explanation.</p><p><b>Hasson supplies a more interesting replacement story.</b> In Stephens, Silbert '
            'and Hasson, <i>Speaker-listener neural coupling underlies successful communication</i> (2010), fMRI recordings showed that '
            'activity in listeners tracked activity in a speaker during a natural story, including higher-order areas associated with '
            'meaning. The association was stronger when comprehension was better, and some listener regions showed anticipatory activity. '
            'The result is not that stories bypass language. It is that a listener actively predicts and reconstructs meaning from a '
            'structured signal.</p><p><b>The debate is about what alignment means.</b> Neural similarity can reflect shared stimulus '
            "timing, language processing, attention or genuine semantic convergence. The English-Russian comparison in Hasson's talk is a "
            'striking demonstration, but it does not erase cultural interpretation, prior beliefs or misunderstanding. Common ground is '
            'built, not assumed. A single framing sentence can alter how people interpret the same story, which is precisely why a '
            'persuader should invite correction rather than exploit ambiguity.</p><p><b>Mirroring needs the same correction.</b> Maddux, '
            "Mullen and Galinsky's 2007 negotiation study found strategic behavioural mimicry improved joint and individual outcomes in a "
            'controlled exercise, with trust mediating one pathway. That is a cue to coordinate naturally, not a covert conversion switch. '
            "You can repeat a clinic owner's own operational terms to check understanding, or pause when the other person pauses. He "
            'should never imitate identity, accent or disability, and should always summarise the proposal in plain language and ask what '
            'was misunderstood.</p>',
  'names': [('Albert Mehrabian', '1939 to present. Researcher whose two 1967 studies were narrowed into the misapplied 7-38-55 rule.'),
            ('Uri Hasson', 'Neuroscientist at Princeton whose 2010 speaker-listener coupling study linked alignment with comprehension.')],
  'room': 'Here is what I heard. What did I misunderstand?',
  'explain': ('In 60 words: what is the honest lesson behind 7-38-55?',
              'Nonverbal cues matter, especially when words, voice and face conflict about an attitude. But the 7-38-55 percentages came '
              'from narrow 1967 experiments, not from all communication. In a real sales conversation, content, context, relationship, '
              'delivery and evidence interact. The practical lesson is to make signals consistent and check understanding instead of '
              'guessing from posture.'),
  'recall': [('What did Mehrabian actually measure?',
              'Inference of positive or negative attitudes from brief, inconsistent combinations of words, vocal tone and facial '
              'expression, not the meaning of every message.'),
             ("What did Hasson's coupling result predict?",
              'Greater anticipatory speaker-listener coupling was associated with better comprehension in the fMRI story task.'),
             ('What is the ethical use of mirroring?',
              'Natural coordination and repeating language to check understanding, never theatrical copying of accent, identity or posture '
              'as a covert control tactic.')],
  'use': ('You are showing a safari lodge owner a mobile booking flow and they go quiet. What do you do?',
          'Do not infer rejection from body language or invoke 7-38-55. Pause, summarise the exact outcome and ask which part is unclear, '
          'risky or irrelevant. Invite them to walk through their current booking path. Then restate the next step in their language and '
          'ask them to correct your account before discussing price.'),
  'further': [('Uri Hasson, This is your brain on communication',
               'https://www.youtube.com/watch?v=FDhlOovaGrI',
               'Video · neural coupling and common ground'),
              ('Mehrabian and Ferris, 1967', 'https://doi.org/10.1037/h0024648', 'Paper · narrow facial and vocal attitude study'),
              ('Stephens, Silbert and Hasson, 2010', 'https://doi.org/10.1073/pnas.1008662107', 'Paper · speaker-listener fMRI coupling')]},
 {'n': 14,
  'f': 'sal',
  'title': 'Who is worth pursuing?',
  'ep': ('INDIE', None, 'ROsrlUFAVZs', '~45:00', 'Founder-Led Sales with Jen Abel of Jjellyfish'),
  'seg': ('0:00',
          '12:48',
          'the founder as the early product, choosing who to sell to, and qualifying through problem-led discovery; the rest is optional'),
  'img': 'd14_kodak',
  'imgcap': 'A 1919 Kodak sales illustration, public domain or no known restrictions. Qualification is not a hunt for anyone who will '
            'listen; it is a disciplined check for a real problem, a real path to decide and a responsible next step.',
  'imgalt': 'A 1919 illustrated Kodak salesman and customer',
  'hook': 'A friendly contact can praise your demo, introduce nobody and disappear for six weeks. Another prospect can be blunt, busy and '
          "immensely valuable because they own the problem and can move a decision. Jen Abel's founder-led sales lesson begins with an "
          "uncomfortable reversal: early customers are often buying access to the founder's insight before they can buy a proven product. "
          'Qualification therefore asks not only Can they pay? but Is this problem real, who must agree, and what evidence would make a '
          'next step rational?',
  'q': 'How do you separate a promising conversation from a qualified opportunity?',
  'terms': [('Qualification', 'testing fit, problem, people, process, timing and constraints before forecasting a deal'),
            ('ICP', 'ideal customer profile, observable account traits associated with fit and economics'),
            ('Champion', 'an internal advocate with motivation, influence, access and useful action'),
            ('Economic buyer', 'the person who can approve or control budget and business risk'),
            ('Decision process', 'the people, criteria, approvals, procurement and dates required to buy')],
  'pre': [('True or false: a warm, enthusiastic contact is automatically a champion.',
           'False. A champion takes useful action, knows the internal process, has a reason to win and can help you reach the people who '
           'decide.'),
          ('Should you force every $300 to $500 lodge retainer through full enterprise MEDDPICC?',
           'No. Use a light fit check for a small, owner-led deal. Reserve the full checklist for genuinely complex, multi-stakeholder '
           'decisions where paper, criteria and approval paths matter.')],
  'watch': ['Why the founder is often the early product when proof is thin',
            "The warning that a demo should show the buyer's problem, not the whole product",
            'The difference between sales as research and sales as revenue (around 9:30 to 12:48, qualifying through problem-led '
            'discovery)'],
  'fig': '<svg viewBox="0 0 1000 360" role="img" aria-label="A light qualification map separating fit, people, process and timing">\n'
         '<rect x="370" y="20" width="260" height="58" rx="12" class="s-box-j"/><text x="405" y="55" class="s-t-b">REAL '
         'OPPORTUNITY?</text>\n'
         '<path d="M500 78 L500 112" class="s-line-m" marker-end="url(#ahm)"/>\n'
         '<rect x="35" y="120" width="205" height="90" rx="12" class="s-card"/><text x="62" y="151" class="s-t">FIT</text><text x="62" '
         'y="176" class="s-t-sm">problem, segment,</text><text x="62" y="195" class="s-t-sm">outcome, constraints</text>\n'
         '<rect x="265" y="120" width="205" height="90" rx="12" class="s-box-a"/><text x="292" y="151" class="s-t">PEOPLE</text><text '
         'x="292" y="176" class="s-t-sm">owner, champion,</text><text x="292" y="195" class="s-t-sm">economic buyer</text>\n'
         '<rect x="530" y="120" width="205" height="90" rx="12" class="s-card"/><text x="557" y="151" class="s-t">PROCESS</text><text '
         'x="557" y="176" class="s-t-sm">criteria, approvals,</text><text x="557" y="195" class="s-t-sm">paper and proof</text>\n'
         '<rect x="760" y="120" width="205" height="90" rx="12" class="s-box-a"/><text x="787" y="151" class="s-t">TIME</text><text '
         'x="787" y="176" class="s-t-sm">priority, event,</text><text x="787" y="195" class="s-t-sm">next decision</text>\n'
         '<path d="M500 112 L137 120" class="s-line" marker-end="url(#ah)"/><path d="M500 112 L367 120" class="s-line" '
         'marker-end="url(#ah)"/><path d="M500 112 L632 120" class="s-line" marker-end="url(#ah)"/><path d="M500 112 L862 120" '
         'class="s-line" marker-end="url(#ah)"/>\n'
         '<rect x="170" y="260" width="660" height="52" rx="12" class="s-card"/><text x="205" y="292" class="s-t-sm">If one box is blank, '
         'label the deal unqualified, not almost closed.</text>\n'
         '</svg>',
  'figcap': 'Qualification is a map, not a gatekeeping performance. A deal is forecastable only when fit, people, process and time have '
            'evidence.',
  'insider': ['<b>BANT is simple, not sacred.</b> Budget, Authority, Need and Timing can expose obvious gaps, but budget may appear only '
              'after a serious problem is established, and a job title does not prove decision power. CHAMP begins with Challenge, then '
              'Authority, Money and Prioritisation. MEDDIC adds Metrics, Economic buyer, Decision criteria, Decision process, Identify '
              'pain and Champion; MEDDPICC adds paper, competition and compelling event. These are practitioner checklists, not validated '
              'laws. Source: https://www.gartner.com/smarterwithgartner/power-challenger-sales-model',
              "<b>Buying is a group task in complex B2B.</b> Gartner's 2017 survey of 750 B2B buyers reported a median buying group of six "
              'to ten decision makers, six buying jobs and 90 percent of buyers revisiting at least one job. The older survey is '
              'directional, not a universal rule for a local dental clinic. Still, it explains why one friendly contact cannot represent '
              'the whole decision. Source: '
              'https://emt.gartnerweb.com/ngw/globalassets/en/sales-service/documents/trends/win-more-b2b-sales-deals.pdf',
              '<b>Jen Abel updates founder-led sales for thin proof.</b> In the INDIE interview, she argues that early buyers are often '
              "buying access to a founder's subject-matter insight, and that a founder must remain deeply involved while the market and "
              'use case are still being learned. The interview is practitioner evidence, not a controlled trial. Its useful test is '
              'whether you can explain a pointed problem better than a generic agency can. Source: '
              'https://www.youtube.com/watch?v=ROsrlUFAVZs',
              '<b>Disqualification protects trust and capacity.</b> If the problem is not urgent, the owner cannot approve, the data '
              'boundary is unsafe, or no decision date exists, mark the opportunity as nurture or no fit. Do not keep a fantasy pipeline '
              'alive. Sales research also warns that the popular 17 percent supplier-contact statistic is an old Gartner survey scope, not '
              'permission to corner buyers. Source: '
              'https://emt.gartnerweb.com/ngw/globalassets/en/sales-service/documents/trends/win-more-b2b-sales-deals.pdf'],
  'deeper': "<p><b>Qualification has two jobs, and confusing them creates bad forecasts.</b> Neil Rackham's <i>SPIN Selling</i> (1988) "
            "asks whether a problem has enough consequence to justify change. Keenan's <i>Gap Selling</i> (2018) maps current state, "
            'future state and the cost of inaction. MEDDIC, developed as a complex-sales checklist and later expanded to MEDDPICC, asks '
            'whether the opportunity has measurable value, an economic buyer, decision criteria and process, pain and a champion. These '
            'frameworks overlap because a seller needs both problem evidence and a path to decision. None can manufacture urgency or '
            "authority.</p><p><b>The buying-committee evidence changes the lone-contact story.</b> Gartner's 2018 buyer-enablement report, "
            'based on 750 B2B buyers, described a median group of six to ten decision makers and six buying jobs: problem identification, '
            'solution exploration, requirements building, supplier selection, validation and consensus creation. It also reported that 90 '
            'percent revisited at least one job. This is useful for an enterprise lodge group or technology partner, but it should not be '
            'pasted onto every Ahmedabad clinic. A small owner-led purchase may have one economic buyer and one operator. Ask, do not '
            'assume.</p><p><b>The Jen Abel interview supplies the founder-stage correction.</b> When proof is thin, the founder is not a '
            "replaceable closer. The buyer is evaluating the founder's judgement, insight and ability to learn. That makes Day 14 a bridge "
            'between qualification and positioning: a prospect is worth pursuing when MTRX can name a real problem, show why you '
            'understand it, identify who must be comfortable, and agree what evidence will earn the next step. A champion is not the '
            'person who smiles. It is the person who takes an action that advances the decision.</p><p><b>Build a two-person pipeline '
            'around evidence.</b> A caller records account fit, observed challenge, owner or manager, permission, timing and meeting '
            'quality. You confirm current and desired state, success metric, data and human handoff, decision maker, alternative and next '
            'date. Forecast only opportunities with a defined next action and owner. For a lodge, a real next step may be a mobile booking '
            'audit with the marketing lead and owner. For a clinic, it may be a bounded WhatsApp workflow review with the owner. If no one '
            'will take the next action, close the loop kindly.</p>',
  'names': [('Neil Rackham', '1946 to present. SPIN researcher whose work distinguishes small and major sales.'),
            ('Jen Abel', 'Co-founder of Jjellyfish; practitioner voice on founder-led sales, early proof and learning before scale.')],
  'room': 'Who else must be comfortable with this decision, and how do they usually evaluate it?',
  'explain': ('In 60 words: what is a champion, and how do you test one?',
              'A champion is not merely friendly. They have a personal reason to solve the problem, influence or access inside the buying '
              'group, knowledge of criteria and process, and willingness to take useful action. Test gently: ask for an internal '
              'introduction, a decision criterion, a shared document or a dated next step. If action never follows, downgrade the '
              'forecast.'),
  'recall': [('Why can the founder be the early product?',
              "When software or proof is unproven, early buyers may be buying access to the founder's specific insight, judgement and "
              'ability to learn alongside them.'),
             ('What six buying jobs did the Gartner report identify?',
              'Problem identification, solution exploration, requirements building, supplier selection, validation and consensus '
              'creation.'),
             ('What is the smallest honest qualification record?',
              'Observed problem and impact, fit and constraints, decision people, timing, evidence needed, next action and owner.')],
  'use': ('Your two callers book a clinic meeting because the receptionist says the idea sounds interesting. What do you do before '
          'forecasting it?',
          'Check whether the clinic has a real enquiry or follow-up problem, whether the owner or authorised manager will attend, what has '
          'already been tried, what outcome matters, whether healthcare data and handoff constraints are safe, and when a decision could '
          'happen. If the receptionist cannot open that path, label it an exploratory conversation, not a qualified opportunity.'),
  'further': [('Founder-Led Sales with Jen Abel of Jjellyfish',
               'https://www.youtube.com/watch?v=ROsrlUFAVZs',
               'Video · founder involvement and research before revenue'),
              ('Gartner, Win More B2B Sales Deals',
               'https://emt.gartnerweb.com/ngw/globalassets/en/sales-service/documents/trends/win-more-b2b-sales-deals.pdf',
               'Report · buying groups and buying jobs'),
              ('Rackham, SPIN Selling', 'https://doi.org/10.1201/9781003073024', 'Book · problem and consequence discovery')]}]

IMAGES = {'d12_interview': {'file': 'File:FEMA - 42150 - Small Business Administration Interview at Cherokee Center.jpg',
                   'credit': 'George Armstrong, FEMA, 2009, public domain',
                   'alt': 'Two people conducting a public service interview'},
 'd13_telephone': {'file': 'File:La telefonista (1932) Isa Pola (5).jpg',
                   'credit': 'Film still from La telefonista, 1932, public domain in Italy',
                   'alt': 'A 1932 telephone operator film still'},
 'd14_kodak': {'file': 'File:The Kodak Salesman (1919) (14597261697).jpg',
               'credit': 'Internet Archive Book Images, The Kodak Salesman, 1919, no known copyright restrictions',
               'alt': 'A 1919 illustrated Kodak salesman and customer'}}

GLOSS = [('Discovery', 'mutual investigation of problem, impact, fit and process', 'Sales'),
 ('SPIN', 'Situation, Problem, Implication and Need-payoff question sequence', 'Sales'),
 ('Need-payoff', 'a benefit the buyer articulates in their own terms', 'Sales'),
 ('Neural coupling', 'time-linked similarity between speaker and listener brain activity', 'Persuasion'),
 ('Common ground', 'shared knowledge and assumptions that support understanding', 'Persuasion'),
 ('7-38-55 myth', 'misuse of narrow 1967 attitude studies as a universal communication law', 'Persuasion'),
 ('Champion', 'an internal advocate who advances a deal through influence and action', 'Sales'),
 ('Economic buyer', 'person who can approve or control budget and business risk', 'Sales'),
 ('Decision process', 'people, criteria, approvals, procurement and dates needed to buy', 'Sales')]

TIEUP = {'title': 'Week 2 tie-up: from attention to a qualified conversation',
 'intro': 'This week moved from finding the right account to earning enough attention, trust and evidence for a voluntary next step. The '
          'transfer test is whether you can diagnose without inventing pain, communicate without magic percentages, and qualify without '
          'keeping every friendly conversation in the forecast.',
 'rows': [('Day 8',
           'Choose an observable ideal customer profile and position MTRX against a real alternative, not a vague market.',
           'Why this account, why this problem, why now?'),
          ('Day 9',
           "Make a message concrete and memorable by translating expertise into the buyer's language and one useful image.",
           'If the buyer cannot repeat the point, the cleverness did not travel.'),
          ('Day 10',
           'Cold outreach earns replies through relevance, permission and a finite cadence, not an untraceable touch-count slogan.',
           'One true observation beats seven automated nudges.'),
          ('Day 11',
           'Resistance is information about freedom, uncertainty and identity; lower the wall with agency, evidence and honest '
           'alternatives.',
           'A no is data, not an objection to defeat.'),
          ('Day 12',
           'Ask for a recent event, reconstruct the current state, explore implication and let the buyer name the payoff.',
           'Before I recommend anything, may I understand what happens today?'),
          ('Day 13',
           'Communication is shared meaning built through content, delivery and common ground; 7-38-55 is not a universal law.',
           'Here is what I heard. What did I misunderstand?'),
          ('Day 14',
           'Pursue opportunities with fit, people, process and time evidence; a champion takes action, and a clean disqualification '
           'protects both sides.',
           'Who else must be comfortable with this decision, and what is the next evidence?')],
 'boss': ('A safari lodge owner says: We want more direct bookings, your founder seems credible, and send a proposal for the full website '
          'and AI package. You have one 30-minute call left before they compare three agencies. What do you ask, what do you show, and '
          'what would make you walk away?',
          '<p>I would not treat enthusiasm as qualification. I would ask for a recent booking journey from Instagram to confirmation, '
          'where visitors drop out, what the lodge has already tried, the value of a direct booking, the seasonal constraint, the owner '
          'and operational stakeholders, the decision criteria, the alternative agencies, data and integration boundaries, and the date of '
          'the next decision. I would reflect the current state and ask what I misunderstood.</p><p>I would show only the smallest '
          'relevant proof, such as a measured mobile booking friction and a short corrected flow, with evidence and limitations. I would '
          'offer a bounded audit or pilot and a mutual action plan with owners and dates. I would walk away, or close the loop, if the '
          'problem is not real, the buyer will not share the decision path, the requested claims exceed our evidence, the data handling is '
          'unsafe, or no one will take the next action. Credibility is useful only when the buying process can test it.</p>'),
 'calib': 'Rate your confidence from 1 to 5: can you distinguish a polite reply from a real problem, a clear message from a 7-38-55 myth, '
          'and a friendly contact from a champion? Name one piece of evidence you would collect next to move your rating up one point.'}

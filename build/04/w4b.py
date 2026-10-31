"""No. 04 content module w4b (normalised from drafts/04/w4b.py, 27 Oct 2026). Plain data; see drafts/FORMAT-04.md."""

DAYS = [{'n': 26,
  'f': 'per',
  'title': 'Can AI persuade better than humans?',
  'ep': ('Sabine Hossenfelder', None, '1MoTeoKaneU', '~7:35', 'AI’s Real Threat: Mass Manipulation'),
  'seg': None,
  'img': 'd26_robot',
  'imgcap': 'A 2016 US Senate hearing file on robots and automation. AI persuasion is not only a chatbot problem: it is a question about '
            'who can scale tailored messages, with what data, and under whose rules.',
  'imgalt': 'Public domain hearing document about robots and automation',
  'hook': 'A chatbot persuaded people to lower their belief in a conspiracy, and the effect was still there two months later. In a '
          'different study, GPT-4 with basic personal information beat human debaters on opinion change. Then a Zurich research team '
          'secretly posted more than 1,500 AI comments as invented human identities on Reddit, and the experiment became an ethics '
          'scandal. The puzzle is not whether AI can write fluent sentences. It is whether persuasion that works can remain honest, '
          'consented and reversible.',
  'q': 'When does AI-assisted persuasion become useful evidence, and when does it become covert power?',
  'terms': [('Personalised persuasion', 'tailoring content to information about a recipient'),
            ('Microtargeting', 'delivering messages to narrowly profiled audiences'),
            ('Conversational persuasion', 'influence through a responsive multi-turn exchange'),
            ('Disclosure', 'telling a recipient who or what generated a message'),
            ('Agency', "a person's capacity to understand, refuse and direct their own choice")],
  'pre': [('True or false: if an AI message changes a belief, the persuasion was automatically good.',
           'False. Accuracy, consent, disclosure, data use and harm still matter. A correct outcome does not excuse covert profiling or '
           'impersonation.'),
          ('Does personalisation always make a message more persuasive?',
           'No. Effects depend on information quality, topic strength, interaction design and whether the model has a real reason to '
           'tailor the argument.')],
  'watch': ['How the video separates scalable targeting from science-fiction claims',
            'The difference between a persuasive output and a legitimate process',
            'Why consent, disclosure and data minimisation belong in the sales system'],
  'fig': '<svg viewBox="0 0 1000 360" role="img" aria-label="An AI persuasion system from data to message to effect and safeguards">\n'
         '<rect x="35" y="50" width="190" height="70" rx="12" class="s-card"/><text x="60" y="80" class="s-t">DATA</text><text x="60" '
         'y="104" class="s-t-sm">public traces, profile</text>\n'
         '<path d="M225 85 L275 85" class="s-line"/>\n'
         '<rect x="275" y="50" width="190" height="70" rx="12" class="s-box-a"/><text x="300" y="80" class="s-t">MODEL</text><text x="300" '
         'y="104" class="s-t-sm">reason, personalise</text>\n'
         '<path d="M465 85 L515 85" class="s-line-m"/>\n'
         '<rect x="515" y="50" width="190" height="70" rx="12" class="s-box-j"/><text x="540" y="80" class="s-t">DIALOGUE</text><text '
         'x="540" y="104" class="s-t-sm">tailored argument</text>\n'
         '<path d="M705 85 L755 85" class="s-line-m"/>\n'
         '<rect x="755" y="50" width="210" height="70" rx="12" class="s-card"/><text x="780" y="80" class="s-t">EFFECT</text><text x="780" '
         'y="104" class="s-t-sm">belief, action, harm</text>\n'
         '<rect x="110" y="205" width="780" height="90" rx="16" class="s-card"/><text x="140" y="239" class="s-t-b">SAFEGUARD '
         'CHECKS</text><text x="140" y="266" class="s-t-sm">disclose AI, minimise data, ask consent, preserve refusal, audit '
         'outcomes</text><text x="140" y="286" class="s-t-sm">A better result is not automatically a legitimate process.</text>\n'
         '<path d="M860 120 C860 165 760 190 690 205" class="s-dash"/><text x="40" y="335" class="s-t-sm">Persuasion can be accurate and '
         'still violate agency when it is covert, exploitative or irreversible.</text>\n'
         '</svg>',
  'figcap': 'AI adds scale and interaction to familiar persuasion mechanisms. The ethical gate sits around the whole pipeline, not only '
            'around the final sentence.',
  'insider': ['<b>Costello, Pennycook and Rand found a real but bounded result.</b> In two experiments with 2,190 Americans, three-round '
              'personalised GPT-4 Turbo dialogues reduced belief in a chosen conspiracy by about 20 percent, with the effect undiminished '
              'at two months. A fact-check of 128 sampled AI claims found 99.2 percent true, 0.8 percent misleading and none false. This '
              'is evidence that tailored, accurate dialogue can change minds, not proof that AI should target anyone without consent. '
              'Source: https://doi.org/10.1126/science.adq1814',
              '<b>Salvi and colleagues tested the frightening comparison directly.</b> Their preregistered 2025 Nature Human Behaviour '
              'study used 900 participants in 600 debates, a 2 by 2 by 3 design. When GPT-4 received basic demographic information, the '
              'odds of greater agreement with its side were 81.2 percent higher than the human-human reference, with a 95 percent '
              'confidence interval from 26.0 to 160.7 percent. The high-opinion-strength subgroup was not statistically significant. This '
              'is a controlled debate task, not a sales conversion estimate. Source: https://doi.org/10.1038/s41562-025-02194-6',
              '<b>The Zurich Reddit case is a lesson in process, not a victory for AI.</b> Science reported in April 2025 that 34 accounts '
              'posted more than 1,500 times in r/changemyview, sometimes inferring gender, ethnicity and political orientation, and '
              'impersonating identities such as a trauma counsellor or Black person. The removed summary claimed personalised comments '
              'performed in the 99th percentile, but about half of LLM-comment posts were deleted, making causal inference weak. The '
              'university said researchers would not publish and would investigate. No result should be treated as a clean finding. '
              'Source: https://www.science.org/content/article/unethical-ai-research-reddit-under-fire',
              '<b>Article 5 of the EU AI Act draws a bright line around some methods.</b> It prohibits placing on the market, putting into '
              'service or using AI that deploys subliminal techniques beyond consciousness, or purposefully manipulative or deceptive '
              'techniques, when the aim or effect is materially distorting behaviour and causing, or being reasonably likely to cause, '
              'significant harm. It also addresses exploitation of vulnerabilities such as age, disability or social or economic '
              'situation. A helpful MTRX rule is stricter: disclose AI, use only necessary public business data, preserve refusal and log '
              'harms. Source: https://eur-lex.europa.eu/eli/reg/2024/1689/oj'],
  'deeper': "<p><b>Three books and papers correct the hype.</b> Petty and Cacioppo's <i>Communication and Persuasion</i> (1986) gives the "
            'ELM: careful arguments matter when motivation and ability are high, while cues and fluency matter when they are low. '
            "Costello, Pennycook and Rand's <i>Durably reducing conspiracy beliefs through dialogues with AI</i> (Science, 2024) shows "
            'that a responsive, evidence-based conversation can outperform a generic correction, and that entrenched belief is not a law '
            'of nature. Salvi, Horta Ribeiro, Gallotti and West, <i>On the conversational persuasiveness of GPT-4</i> (Nature Human '
            'Behaviour, 2025), adds a direct human comparison and a warning about personal data. These studies test agreement shifts in '
            "recruited participants, not long-run purchasing, informed consent in the wild, or whether the model's claims remain reliable "
            "in every domain.</p><p><b>Personalisation is not one effect.</b> Matz, Teeny and colleagues' <i>The potential of generative "
            'AI for personalized persuasion at scale</i> (Scientific Reports, 2024) used four studies and seven sub-studies, total N = '
            '1,788, and found stronger influence from messages tailored to psychological profiles. But a 2024 commentary by Teeny and Matz '
            "argues that the live question is when personalisation works, not whether every prompt is a manipulation machine. Salvi's own "
            'high-strength topics lost statistical significance, so an AI advantage is conditional, not a universal conversion '
            'multiplier.</p><p><b>The stranger true story is the ethics failure.</b> The Zurich researchers got a striking result on a '
            'platform where users expected human discussion, but did so covertly, with inferred sensitive traits and performed identities. '
            'The scientific result was withdrawn, while the trust cost remained. That is the reverse of an honest sales demo: the more '
            'effective the hidden tactic, the more important disclosure and recourse become. For MTRX, an AI draft can improve clarity, '
            'but you should tell a prospect when automation meaningfully shapes a message, never infer patient or staff vulnerabilities, '
            'and keep a human accountable for claims. AI may help someone decide; it must not quietly decide what they are allowed to '
            'see.</p>',
  'names': [('Thomas H. Costello, Gordon Pennycook and David Rand',
             'Researchers on personalised GPT-4 dialogues and conspiracy belief change, Science 2024.'),
            ('Francesco Salvi, Manoel Horta Ribeiro, Riccardo Gallotti and Robert West',
             'Authors of the preregistered GPT-4 conversational persuasion study, Nature Human Behaviour 2025.')],
  'room': '"The model can draft this, but what data did it use, what will we disclose, and how can the buyer refuse?"',
  'explain': ('In 60 words: what is the strongest evidence that AI can persuade?',
              'Two controlled studies provide the clearest evidence. Costello, Pennycook and Rand found a roughly 20 percent reduction in '
              'conspiracy belief after personalised GPT-4 dialogue, persisting two months, among 2,190 Americans. Salvi and colleagues '
              'found higher odds of opinion movement when GPT-4 had basic demographic information. Neither study licenses covert profiling '
              'or proves general sales lift.'),
  'recall': [('What did the Science 2024 study find?',
              'Among 2,190 Americans, personalised three-round GPT-4 dialogues reduced chosen conspiracy belief about 20 percent, lasting '
              'at least two months; sampled claims were 99.2 percent true.'),
             ("What was Salvi et al.'s key number?",
              'With personal information, GPT-4 debates had 81.2 percent higher odds of greater agreement than the human-human reference, '
              'N = 900, with a 95 percent confidence interval from 26.0 to 160.7 percent.'),
             ('Why is the Zurich case not a clean experiment?',
              'Participants were not informed, 34 accounts posted over 1,500 times using inferred sensitive traits and invented '
              'identities, and about half of AI-comment posts were deleted, undermining causal inference.')],
  'use': ('You want an AI SDR to scan clinic websites and write highly personal Gujarati or Hindi calls. What is the ethical version?',
          'Use only observable business facts, such as a broken booking form, and let a trained caller verify the observation. Identify '
          'MTRX, disclose meaningful automation where required, avoid patient or staff profiling, offer an easy opt-out, and audit '
          'held-meeting quality rather than maximising replies. AI may produce a draft; you own the evidence and the decision.'),
  'further': [('Costello, Pennycook and Rand, Durably reducing conspiracy beliefs through dialogues with AI',
               'https://doi.org/10.1126/science.adq1814',
               'Paper · Science 2024'),
              ('Salvi et al., On the conversational persuasiveness of GPT-4',
               'https://doi.org/10.1038/s41562-025-02194-6',
               'Paper · Nature Human Behaviour 2025'),
              ("O'Grady, Unethical AI research on Reddit under fire",
               'https://www.science.org/content/article/unethical-ai-research-reddit-under-fire',
               'Article · Science/AAAS ethics report')]},
 {'n': 27,
  'f': 'sal',
  'title': 'How do you build a repeatable founder sales system?',
  'ep': ('Talks at Google', None, 'RG_eyn0fRXs', None, 'The Sales Acceleration Formula | Mark Roberge | Talks at Google'),
  'seg': None,
  'img': 'd27_casino',
  'imgcap': 'A casino floor is a vivid warning about activity metrics. Footfall is not profit, and a full pipeline is not a healthy one '
            'unless fit, conversion, margin and retention are visible.',
  'imgalt': 'Casino floor with many tables and machines',
  'hook': 'A founder can feel productive while doing the wrong work: 200 DMs sent, 40 calls booked, zero profitable retainers. Mark '
          "Roberge built HubSpot's sales machine by treating sales as a measurable system rather than a personality contest. You have a "
          'smaller problem but the same trap: two commission callers can optimise appointments, while you inherit bad-fit calls and unpaid '
          'persuasion labour. The fix is not a louder script. It is a pipeline with definitions, denominators and feedback.',
  'q': 'Which parts of your selling should become a system, and which still require founder judgement?',
  'terms': [('Pipeline stage', 'a defined buyer state with an entry rule and next action'),
            ('Conversion rate', 'the share moving from one defined stage to the next'),
            ('Cadence', 'a planned sequence of contacts and value events with stop rules'),
            ('CAC', 'customer acquisition cost, including the relevant labour and spend'),
            ('LTV', 'customer lifetime value, an estimate that must state margin, retention and time horizon')],
  'pre': [('True or false: more activity automatically fixes a weak pipeline.',
           'False. More activity can amplify poor fit, compliance risk and wasted follow-up. Improve definitions and conversion quality '
           'before increasing volume.'),
          ('Should you measure callers mainly by calls made?',
           'No. Calls made are leading activity measures. Held, suitable meetings and downstream margin are outcome measures; use both and '
           'watch for gaming.')],
  'watch': ['How Roberge turns hiring, training and management into a repeatable process',
            'The difference between activity metrics and stage outcomes',
            'Which parts of a sales method can be documented without pretending buyers are identical'],
  'fig': '<svg viewBox="0 0 1000 360" role="img" aria-label="A measurable founder sales system from segment to learning loop">\n'
         '<rect x="35" y="48" width="165" height="72" rx="12" class="s-box-a"/><text x="57" y="78" class="s-t">ICP</text><text x="57" '
         'y="102" class="s-t-sm">fit, trigger, owner</text>\n'
         '<path d="M200 84 L245 84" class="s-line"/>\n'
         '<rect x="245" y="48" width="165" height="72" rx="12" class="s-card"/><text x="267" y="78" class="s-t">CONTACT</text><text '
         'x="267" y="102" class="s-t-sm">permission, relevance</text>\n'
         '<path d="M410 84 L455 84" class="s-line"/>\n'
         '<rect x="455" y="48" width="165" height="72" rx="12" class="s-box-j"/><text x="477" y="78" class="s-t">DISCOVER</text><text '
         'x="477" y="102" class="s-t-sm">problem, impact, process</text>\n'
         '<path d="M620 84 L665 84" class="s-line-m"/>\n'
         '<rect x="665" y="48" width="165" height="72" rx="12" class="s-card"/><text x="687" y="78" class="s-t">PROPOSE</text><text '
         'x="687" y="102" class="s-t-sm">scope, proof, price</text>\n'
         '<path d="M830 120 L830 175 L500 175 L500 205" class="s-line-m"/>\n'
         '<rect x="260" y="205" width="480" height="80" rx="14" class="s-box-a"/><text x="290" y="238" class="s-t-b">MEASURE AND '
         'LEARN</text><text x="290" y="264" class="s-t-sm">stage conversion, cycle time, margin, retention, referrals</text>\n'
         '<path d="M260 245 C150 245 120 180 120 120" class="s-dash"/><text x="35" y="330" class="s-t-sm">A repeatable system is a '
         'documented hypothesis with clean denominators, not a script that hides bad fit.</text>\n'
         '</svg>',
  'figcap': 'A system is a loop: define fit, ask permission, diagnose, propose, measure and feed learning back into the next cohort. Each '
            'stage needs a rule and a denominator.',
  'insider': ["<b>Roberge's useful idea is instrumentation, not a magic script.</b> His HubSpot work is a practitioner case, so treat it "
              'as a hypothesis about repeatability. For MTRX, write stage entry and exit rules: target account, permissioned contact, held '
              'discovery, qualified opportunity, proposal, signed SOW, first payment, retained month two. A contact list is not a '
              'pipeline. Source talk: https://www.youtube.com/watch?v=2_LJLtWbe1g',
              '<b>Conversion maths tells you where the bottleneck lives.</b> Suppose 100 relevant, compliant contacts yield 12 replies, 6 '
              'held discoveries, 3 qualified opportunities, 2 proposals and 1 signed retainer. The stage rates are 12 percent, 50 percent, '
              '50 percent, 67 percent and 50 percent. If the one win costs 100 contacts, caller pay, your closing time and delivery setup, '
              "that is CAC. Keep the example as a baseline, then replace it with MTRX's cohort data; vendor benchmarks are not local "
              'truth. Source: https://link.springer.com/article/10.1007/s11747-010-0211-8',
              '<b>Measure quality where gaming is expensive.</b> Commission-only callers can maximise booked meetings by overpromising or '
              'ignoring fit. Pay attention to held and qualified meetings, show rate, reasons lost, refund or cancellation, gross margin '
              'and month-two retention. For Ahmedabad dental clinics, log language, consent or opt-out status, business fit and the actual '
              'problem. TRAI rules and channel constraints are part of process design, not an afterthought. Source: '
              'https://trai.gov.in/sites/default/files/2024-10/PR_No.51of2024.pdf',
              '<b>AI belongs after the method is legible.</b> Use a small holdout to compare human-researched and AI-assisted outreach in '
              'the same segment and period. Keep the denominator at qualified conversations per 1,000 compliant contacts, net of '
              "hallucinated facts, complaints and opt-outs. HubSpot's 2024 adoption figures are vendor self-report, not causal proof. If "
              'the AI cannot explain why a prospect fits, it is automating noise. Source: '
              'https://8348499.fs1.hubspotusercontent-na2.net/hubfs/8348499/PDFs/State%20of%20Sales%20Report%202024%20-%20FINAL.pdf'],
  'deeper': "<p><b>Roberge, Ross and Verbeke point in the same direction, with different evidence.</b> Mark Roberge's <i>The Sales "
            "Acceleration Formula</i> (2015) is an operator's account of hiring for characteristics, training a process, managing by data "
            "and improving the system. Aaron Ross and Marylou Tyler's <i>Predictable Revenue</i> (2011) popularised specialisation and "
            'repeatable outbound, but its headcount assumptions fit a scaled software motion better than a two-person studio. Verbeke, '
            "Dietz and Verwaal's meta-analysis (2011) found sales performance related to selling knowledge, adaptiveness, cognitive "
            'aptitude and work engagement, while role ambiguity was negative. The shared lesson is not to erase judgement. It is to make '
            'learning and fit visible.</p><p><b>Metrics require a causal story.</b> A funnel percentage is meaningless without a '
            'denominator, time window, stage definition and cohort. Reply rate can mean any reply or a positive reply. Meeting rate can '
            'count booked or held meetings. Win rate can divide by all opportunities or only proposals. CAC must include caller '
            'commissions, your time, tools, payment fees and onboarding, or it flatters the motion. LTV should use gross margin and '
            'observed retention, not a hopeful revenue multiple. A simple dashboard for MTRX should show contacts, replies, held '
            'discoveries, qualified opportunities, proposals, wins, days to first payment, delivery hours, gross margin, month-two '
            'retention and referrals by niche and source.</p><p><b>The stranger true story behind repeatability is that standardisation '
            "can expose bad assumptions.</b> HubSpot's celebrated scale does not prove a script works for safari lodges or Ahmedabad "
            'clinics. One segment may value direct bookings, another may value patient call response, and one language channel may have '
            "different consent and trust conditions. Use Roberge's talk as a design prompt, then run a 30 to 50 account cohort with a "
            'holdout. Change one thing at a time where possible. Keep a qualitative loss log because conversion numbers cannot tell you '
            'that a prospect disliked an unsupported claim or that delivery scope was impossible. A repeatable system is a documented, '
            'revisable hypothesis, not a machine for making every buyer look the same.</p>',
  'names': [('Mark Roberge',
             'Former HubSpot CRO and author of The Sales Acceleration Formula, a practitioner source on scaling a sales process.'),
            ('Willem Verbeke, Marc Dietz and Ernst Verwaal',
             'Authors of a 2011 meta-analysis of sales-performance drivers and role conditions.')],
  'room': '"What is the stage definition, what is the denominator, and what buyer evidence would make us change the process?"',
  'explain': ('In 60 words: what makes a sales process repeatable?',
              'A repeatable process has a narrow fit hypothesis, defined stages, permissioned actions, clear owners, measurable conversion '
              'and a learning loop. It does not mean every buyer behaves identically. You should separate activity from outcomes, record '
              'losses and margin, test one cohort at a time, and revise the process when evidence or buyer feedback contradicts it.'),
  'recall': [('What is the difference between activity and outcome metrics?',
              'Activity metrics count actions such as contacts or calls. Outcome metrics count what those actions produced, such as held '
              'qualified meetings, proposals, wins, margin and retention.'),
             ('Give a usable MTRX pipeline.',
              'Target account, permissioned contact, held discovery, qualified opportunity, proposal, signed SOW, first payment, retained '
              'month two, then referral or expansion.'),
             ('Why can CAC and LTV mislead a studio?',
              'CAC omits founder time, caller commissions or onboarding if defined narrowly; LTV becomes fantasy if it ignores gross '
              'margin, observed retention, churn and the time horizon.')],
  'use': ('How should you manage your two commission-only callers next month?',
          'Define the ICP and compliant contact rule, give each caller the same short qualification form, and pay for held suitable '
          'meetings with a quality adjustment rather than raw bookings. Track contacts, replies, held meetings, qualification, proposals, '
          'wins, opt-outs and reasons lost. Review five calls weekly, update the Gujarati or Hindi wording from real objections, and stop '
          'any promise you cannot deliver.'),
  'further': [('Mark Roberge, what happens in a 1:1 with salespeople',
               'https://www.youtube.com/watch?v=2_LJLtWbe1g',
               'Talk · Building the Sales Machine · how he coaches against the process'),
              ('Verbeke, Dietz and Verwaal, Drivers of sales performance',
               'https://link.springer.com/article/10.1007/s11747-010-0211-8',
               'Meta-analysis · sales performance'),
              ('HubSpot, State of Sales 2024',
               'https://8348499.fs1.hubspotusercontent-na2.net/hubfs/8348499/PDFs/State%20of%20Sales%20Report%202024%20-%20FINAL.pdf',
               'Vendor report · label self-report and denominator')],
  'stop': 'Long talk. Watch until Roberge has laid out his four repeatable systems (hiring, training, a steady flow of leads, one shared '
          'sales process) and how he hires against data; the rest is optional.'},
 {'n': 28,
  'f': 'per',
  'title': 'What kind of persuader will you be?',
  'ep': ('The Aspen Institute', None, 'Z3C7IRFMvd4', None, 'Influence is Your Superpower (Workshop)'),
  'seg': None,
  'img': 'd28_gandhi',
  'imgcap': 'Mahatma Gandhi in a 1931 studio photograph by Elliott and Fry. Satyagraha made persuasion a discipline of truth, '
            'self-restraint and willingness to bear a cost, not a licence to dominate another person.',
  'imgalt': 'Mahatma Gandhi in a 1931 studio portrait',
  'hook': 'The most useful sales question is not how to make a buyer say yes. It is what the buyer would still choose if every relevant '
          'fact, incentive and pressure were visible. Cialdini distinguishes detecting influence from fabricating it. Kant asks whether we '
          'treat a person as an end rather than merely a means. Gandhi built satyagraha around truth-force, voluntary suffering and '
          'refusal to injure. You now have to turn those ideas into a code you can use when a retainer is slow, a caller wants a shortcut, '
          'or a client wants a promise the evidence cannot support.',
  'q': 'How can you use honest influence without turning a buyer into a target?',
  'terms': [('Honest scarcity', 'a real capacity, inventory or deadline stated with conditions'),
            ('Social proof', "truthful evidence of other people's experience or behaviour"),
            ('Kantian test', 'asking whether a tactic respects a person as an end, not only as a means'),
            ('Satyagraha', "Gandhi's discipline of truth-force and nonviolent resistance"),
            ('Persuasion code', 'written rules that constrain how a person makes claims, asks and closes')],
  'pre': [('True or false: ethical persuasion means avoiding emotion and influence entirely.',
           'False. Clarity, stories, proof and appropriate emotion can help a person decide. Ethics constrains deception, coercion, '
           'exploitation and hidden pressure, not communication itself.'),
          ('Is social proof ethical whenever a real customer exists?',
           'No. Get permission, represent the evidence accurately, disclose limits and never imply that one customer proves a universal '
           'result.')],
  'watch': ['How Chance frames influence as a learnable skill rather than a trick list',
            'Where honest clarity ends and hidden pressure begins',
            'Which rule you could still follow when a deal or commission is at stake'],
  'fig': '<svg viewBox="0 0 1000 360" role="img" aria-label="An ethical persuasion gate from claim to buyer choice">\n'
         '<rect x="35" y="52" width="175" height="70" rx="12" class="s-card"/><text x="58" y="82" class="s-t">CLAIM</text><text x="58" '
         'y="106" class="s-t-sm">what am I saying?</text>\n'
         '<path d="M210 87 L260 87" class="s-line"/>\n'
         '<rect x="260" y="52" width="175" height="70" rx="12" class="s-box-a"/><text x="283" y="82" class="s-t">PROOF</text><text x="283" '
         'y="106" class="s-t-sm">what supports it?</text>\n'
         '<path d="M435 87 L485 87" class="s-line"/>\n'
         '<rect x="485" y="52" width="175" height="70" rx="12" class="s-box-j"/><text x="508" y="82" class="s-t">CHOICE</text><text '
         'x="508" y="106" class="s-t-sm">can they refuse?</text>\n'
         '<path d="M660 87 L710 87" class="s-line-m"/>\n'
         '<rect x="710" y="52" width="235" height="70" rx="12" class="s-card"/><text x="733" y="82" class="s-t">CONSEQUENCE</text><text '
         'x="733" y="106" class="s-t-sm">who bears the risk?</text>\n'
         '<rect x="140" y="205" width="720" height="84" rx="16" class="s-card"/><text x="170" y="238" class="s-t-b">THE KANTIAN '
         'TEST</text><text x="170" y="264" class="s-t-sm">Would I accept this tactic if the buyer knew it before deciding?</text><text '
         'x="170" y="283" class="s-t-sm">If not, disclose it, change it, or do not use it.</text>\n'
         '<path d="M827 122 C827 165 690 185 620 205" class="s-dash"/>\n'
         '</svg>',
  'figcap': 'Before a persuasive claim reaches a buyer, test the proof, the freedom to refuse and who bears the risk. The Kantian question '
            'makes hidden tactics visible.',
  'insider': ['<b>Cialdini gives you a crucial split.</b> The ethical practitioner detects principles already present and makes them '
              'legible; the manipulator fabricates scarcity, authority, consensus or obligation. Real scarcity is a capacity limit, such '
              'as two onboarding slots in a month, with the date and consequence stated. Fake scarcity is a timer that resets or a false '
              'low-stock claim. Influence is not the enemy; concealed manufacture is. Source: '
              'https://www.harpercollins.com/products/influence-new-and-expanded-robert-b-cialdini',
              "<b>Kant is a disclosure test, not a slogan.</b> No. 02 Day 24's means-only test asks whether you are using a buyer merely "
              'as a tool for revenue, or engaging them as a person whose informed choice matters. A proposal can be persuasive and still '
              'respect autonomy if its evidence, limits, price, alternatives and exit are visible. A hidden fee or invented deadline fails '
              'because the buyer would reasonably reject the method if it were revealed. Source: '
              'https://plato.stanford.edu/entries/kant-moral/',
              "<b>Gandhi's satyagraha is persuasion through truth and cost.</b> In Gandhi's account, satyagraha is not passive aggression "
              'or a clever sales close. It asks the actor to refuse falsehood and coercion, accept suffering rather than inflict it, and '
              "appeal to the opponent's conscience. The parallel for you are modest but real: state what is true, make a fair request, "
              'accept no without punishment, and let the quality of delivery carry the argument. Source: '
              'https://www.mkgandhi.org/satyagraha/satyagraha.htm',
              '<b>Write the code before the pressure arrives.</b> your minimum code can say: I claim only what I can evidence; I label '
              'estimates and uncertainty; I use real proof with permission; I state real scarcity and full conditions; I make refusal '
              'easy; I trade scope, not hidden concessions; I protect private data; I log complaints and repair harm; I do not train '
              'callers to exploit fear, language, age or medical anxiety. Review it after every lost or won deal. Source: '
              'https://doi.org/10.1017/S0031819119000209'],
  'deeper': "<p><b>Cialdini, Kant and Gandhi answer different questions.</b> Cialdini's <i>Influence</i> (1984, expanded 2021) is a "
            'descriptive and practical map of recurring social influence principles, including reciprocity, commitment, social proof, '
            'authority, liking, scarcity and unity. Its ethical value depends on whether you detect a genuine condition or fabricates one. '
            "Kant's <i>Groundwork of the Metaphysics of Morals</i> (1785) supplies a harder constraint: a person must never be treated "
            "merely as a means. Gandhi's <i>Hind Swaraj</i> (1909) and writings on satyagraha make persuasion a moral practice of truth, "
            "self-discipline and nonviolence. None is a conversion formula.</p><p><b>Modern ethics sharpens the boundary.</b> Noggle's "
            'account treats manipulation as bypassing reason; Susser, Roessler and Nissenbaum emphasise hidden influence and asymmetric '
            "power. That debate matters in a sales call because a buyer may be time-poor, inexperienced or dependent on the seller's "
            'technical knowledge. The honest levers in the MTRX promise survive scrutiny: clarity reduces interpretation cost; proof makes '
            'a claim checkable; real scarcity informs capacity; real social proof reports relevant experience. They stop being honest when '
            'you hide conditions, cherry-picks results, pressures a vulnerable person or makes refusal costly.</p><p><b>The practical '
            'capstone is a code plus a counterfactual.</b> Before sending a proposal, ask: would I state this evidence and limitation if '
            'the buyer were my friend? Would I accept the same tactic if the seller knew less than I did? Could the buyer decline and '
            'still receive respectful treatment? A safari lodge should know what a $400 retainer includes, what it excludes, what proof is '
            'permissioned and what happens at cancellation. A dental clinic should not be frightened with invented patient-loss numbers or '
            'pressured through medical vulnerability. The code is not branding. It is a precommitment that protects judgement when a '
            'commission, cash-flow gap or impressive case study tempts exaggeration.</p><p><b>Non-Western does not mean decorative '
            'here.</b> Satyagraha gives you a genuine Indian model in which credibility is built by accepting limits and costs oneself '
            'rather than exporting them to an opponent. Its lesson is not that every commercial negotiation should become a protest. It is '
            "that persuasion can seek agreement without treating the other person's freedom as a defect. The final question is therefore "
            'not whether you can close. It is whether a buyer can say yes for reasons you would be willing to publish.</p>',
  'names': [('Robert Cialdini', '1945 to. Researcher and author of Influence, including the 2021 expanded account of seven principles.'),
            ('Mohandas K. Gandhi',
             '1869-1948. Developed satyagraha as truth-force and nonviolent resistance in ethical and political practice.')],
  'room': '"Here is the evidence, here is what I do not know, and here is the easiest way to say no."',
  'explain': ('In 60 words: what is ethical persuasion?',
              'Ethical persuasion helps another person understand a truthful option and choose freely. It can use clarity, proof, emotion, '
              'real scarcity and real social proof, but it does not hide material conditions, fabricate consensus, exploit vulnerability '
              'or punish refusal. You should disclose uncertainty, make exit easy, protect data, and review your code against every real '
              'deal.'),
  'recall': [('What is the difference between detecting and fabricating influence?',
              'Detecting makes a real condition visible, such as actual capacity or permissioned proof. Fabricating invents urgency, '
              'authority, consensus or obligation to steer a choice.'),
             ('What does the Kantian test ask?',
              'Whether you treat the buyer as a person with informed agency, or merely as a means to revenue. A useful counterfactual is '
              'whether you would disclose the tactic before the decision.'),
             ('What does satyagraha add to a sales ethic?',
              'A model of persuasion grounded in truth, self-restraint, nonviolence and willingness to bear costs oneself rather than '
              'impose hidden pressure on the other person.')],
  'use': ('Write three lines of your persuasion code for a safari lodge proposal.',
          'I will show only permissioned proof and label estimates as estimates. I will state the complete scope, price, capacity limit '
          'and cancellation terms, and I will not invent a deadline. I will make a no or not-yet easy, record what I learned, and '
          'recommend another provider when MTRX is not the fit.'),
  'further': [('Zoe Chance on Our Gator Brains',
               'https://www.youtube.com/watch?v=7SJ5c_xitGg',
               'Video · short · System 1, the gator brain and why ease wins'),
              ('Robert Cialdini, Influence, New and Expanded',
               'https://www.harpercollins.com/products/influence-new-and-expanded-robert-b-cialdini',
               'Book · detect principles, do not fabricate them'),
              ('S. Susser, B. Roessler and H. Nissenbaum, Online manipulation',
               'https://doi.org/10.1017/S0031819119000209',
               'Paper · hidden influence and asymmetric power')],
  'stop': 'Long workshop. Watch until Zoe Chance has covered asking, trust and the liking gap; the rest (System 1, ease, defaults) is a '
          'strong optional second sitting.'}]

IMAGES = {'d26_robot': {'file': 'File:THE TRANSFORMATIVE IMPACT OF ROBOTS AND AUTOMATION (IA gov.gpo.fdsys.CHRG-114shrg20442).pdf',
               'credit': 'United States Congress Joint Economic Committee, The Transformative Impact of Robots and Automation, 2016, '
                         'public domain',
               'alt': 'Public domain US Senate hearing document about robots and automation'},
 'd27_casino': {'file': 'File:Fontainebleau Las Vegas Casino Floor.jpg',
                'credit': 'Dialh, Fontainebleau Las Vegas Casino Floor, 2024, CC BY 4.0',
                'alt': 'Casino floor showing many simultaneous activities'},
 'd28_gandhi': {'file': 'File:Mahatma-Gandhi, studio, 1931.jpg',
                'credit': 'Elliott & Fry, Mahatma Gandhi studio photograph, 1931, public domain',
                'alt': 'Mahatma Gandhi in a 1931 studio portrait'}}

GLOSS = [('Personalised persuasion', 'Tailoring content to information about the recipient.', 'Persuasion'),
 ('Disclosure', 'Telling a recipient who or what generated a message.', 'Persuasion'),
 ('Pipeline stage', 'A defined buyer state with an entry rule and next action.', 'Sales'),
 ('Conversion rate', 'The share moving from one defined stage to the next.', 'Sales'),
 ('Customer acquisition cost', 'Relevant cost of acquiring a customer, including labour and tools.', 'Sales'),
 ('Honest scarcity', 'A real capacity or deadline stated with conditions.', 'Persuasion'),
 ('Kantian test', 'A check that a person is not being treated merely as a means.', 'Persuasion'),
 ('Satyagraha', 'Gandhian truth-force expressed through self-restraint and nonviolence.', 'Persuasion')]

TIEUP = {'title': 'Week 4: negotiate, defend, keep',
 'intro': 'The last week turns influence into a durable practice. Negotiate interests and alternatives, recognise power without '
          'worshipping tactics, defend against dark patterns, retain clients after the yes, understand AI persuasion, build a measurable '
          'system, and finish with a code that survives pressure.',
 'rows': [('Day 22',
           'Negotiation is preparation: BATNA, ZOPA, reservation price, anchors and tradeable scope.',
           '"What is our best alternative, and what would we trade rather than give away?"'),
          ('Day 23',
           'Power is relative to alternatives and process. Listen for interests, create options and do not confuse empathy with surrender.',
           '"What would make this workable for both sides, and what is our alternative if it is not?"'),
          ('Day 24',
           'Dark patterns exploit attention, defaults and pressure. Name the mechanism, refuse the trap and build the honest alternative.',
           '"Would this still be acceptable if the buyer saw the tactic before deciding?"'),
          ('Day 25',
           'The signed deal is a beginning. Baseline outcomes, define scope, repair service failures and earn referrals through value.',
           '"What did success mean at the start, and what evidence will show that we delivered it?"'),
          ('Day 26',
           'AI can scale tailored persuasion, but effect size is not ethical permission. Disclosure, consent, data minimisation and '
           'recourse are part of the product.',
           '"What does the model know, what will we disclose, and how can the buyer refuse?"'),
          ('Day 27',
           'A repeatable sales system has fit, stages, denominators, quality controls, learning and a founder judgement loop.',
           '"Which stage is leaking, and what evidence would make us change the process?"'),
          ('Day 28',
           'The honest levers are clarity, proof, real scarcity and real social proof, constrained by a personal code.',
           '"Here is the evidence, here is what I do not know, and here is the easiest way to say no."')],
 'boss': ('Can you take one realistic MTRX deal from first message to signed retainer and referral while using at least one idea from each '
          'week?',
          '<p><b>Model answer.</b> You choose a Kenyan eco-lodge with an active Instagram account and a public mobile booking path that is '
          'slow and confusing. <b>Week 1:</b> you separate persuasion from manipulation, state a truthful observation, and use ethos, '
          "logos and pathos without pretending to know the lodge's revenue. <b>Week 2:</b> you send one relevant, permission-based DM, ask "
          'for a short discovery call, and use SPIN questions to learn direct-booking goals, seasonal constraints, decision makers and the '
          "cost of missed enquiries. You record the lodge's BATNA, including its current agency and doing nothing.</p><p><b>Week 3:</b> "
          "you reframe the offer around the lodge's desired outcome, show a permissioned before-and-after case with limits, and present "
          'good, better and best scopes. You anchor with a complete price, not a fake discount, then agree a paid audit or small pilot '
          'with a mutual action plan. <b>Week 4:</b> you trade scope, speed and support rather than silently conceding work; answer '
          'objections by clarifying conditions; write onboarding, analytics and cancellation terms; and set a real capacity limit based on '
          'your delivery calendar. If AI helped draft the message, you remain accountable and do not infer private staff or guest '
          'data.</p><p>The lodge signs a three-month $400 monthly retainer with a defined mobile enquiry flow, analytics, two revision '
          'rounds and response times. You baseline enquiry clicks and completion before work, report what changed, and say what cannot yet '
          'be attributed. After a useful first month, you ask whether the owner would introduce one neighbouring lodge, make the referral '
          'request optional and supply a factual one-sentence description. The referral is earned social proof, not manufactured '
          'consensus. The deal is persuasive because the buyer can inspect the claim, compare alternatives, decline without punishment and '
          'still receive respect.</p>'),
 'calib': 'Return to your Day 1 baseline. Rate 1 to 10: how clearly can you separate persuasion, manipulation and coercion; how '
          'consistently do you show proof and uncertainty; how confidently can you ask for a decision without fake urgency; and how likely '
          'are you to make refusal easy? Write one behaviour that moved, one that did not, and one rule in your persuasion code you will '
          'test in the next MTRX deal.'}

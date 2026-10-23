from svg import box, t, arrow, line, svg

ROWS = [('RECIPROCITY', 'a free audit, no strings', 'a “gift” with a catch'),
        ('SOCIAL PROOF', 'real, named clients, with permission', 'invented testimonials'),
        ('AUTHORITY', 'your own work, shown openly', 'borrowed logos and badges'),
        ('SCARCITY', 'a genuinely full calendar', 'a fake countdown timer'),
        ('COMMITMENT', 'a small step with an easy exit', 'a contract that traps')]
def table():
    out = (box(20, 56, 260, 40, 's-box-j', 8) + t(150, 82, 'LEVER', 's-t-b') +
           box(300, 56, 420, 40, 's-box-j', 8) + t(510, 82, 'HONEST VERSION', 's-t-b') +
           box(740, 56, 420, 40, 's-box-j', 8) + t(950, 82, 'CON VERSION', 's-t-b'))
    for r, (lev, good, bad) in enumerate(ROWS):
        y = 108 + r * 56
        out += (box(20, y, 260, 46, 's-card', 8) + t(150, y + 29, lev, 's-t-b') +
                box(300, y, 420, 46, 's-card', 8) + t(510, y + 29, good, 's-t-sm') +
                box(740, y, 420, 46, 's-box-a', 8) + t(950, y + 29, bad, 's-t-sm'))
    return out
FIG = svg(1180, 440, 'Five persuasion levers, each with an honest version and a con version',
          t(590, 32, 'EVERY LEVER HAS AN HONEST VERSION AND A CON VERSION', 's-t') + table() +
          t(590, 420, 'The test for every row: can the buyer check it, and can they say no without losing face?', 's-t-sm'))

STOP = dict(
    id='7.5', day=46, title='Red-team your own pitch: honest influence for MTRX™',
    q='You have spent seven weeks learning how cons work. Could your own sales pitch survive the checks in this course?',
    why='This stop turns the whole course on your own business. MTRX™ sells websites and AI services through cold calls, Instagram and proposals, and each of those channels can slide into the tricks in this guide: fake urgency, borrowed authority, testimonials nobody can verify. The difference between honest persuasion and a con is not which levers you use. It is whether the buyer can check and leave. For a writer, the honest seller is a harder and better character than the hustler.',
    case=dict(k='The case', name='The rules that now police persuasion', role='India’s dark-pattern guidelines and the US fake-review rule',
              facts=[('India, 2023', 'Dark-pattern guidelines notified 30 November 2023: 13 patterns'),
                     ('India, penalty', 'Misleading ads: up to ₹10 lakh, ₹50 lakh for repeats'),
                     ('US, 2024', 'FTC rule on fake reviews and testimonials, in force 21 October 2024'),
                     ('The test', 'Can the buyer check the claim and leave without shame?')],
              stamp=('field', 'Field test: red-team your pitch')),
    cold=dict(q='India’s consumer regulator lists 13 dark patterns that websites and apps must not use. How many can you name before reading on?',
              a='The 2023 guidelines list false urgency, basket sneaking, confirm shaming, forced action, subscription traps, interface interference, bait and switch, drip pricing, disguised advertisements, nagging, trick wording, SaaS billing and rogue malware. Read that as a web developer and it is a checklist of things clients may one day ask you to build. Read it as a writer and it is the con’s toolkit from stop 4.1, translated into buttons.'),
    video=dict(id='fKK9nVLvhGM', title='How free games are designed to make money', who='Vox',
               watch=['Which design tricks the video shows, and which of India’s 13 dark patterns they match',
                      'How the design hides the real cost from the player',
                      'One feature you would refuse to build for a client']),
    story=['Start with the law, because it now draws part of the line for you. On 30 November 2023 India’s Central Consumer Protection Authority notified guidelines banning 13 dark patterns on websites and apps, from false urgency and confirm shaming to drip pricing and subscription traps. Under the Consumer Protection Act 2019, the regulator can fine a misleading advertisement up to ₹10 lakh, or ₹50 lakh for a repeat. In the United States, the FTC’s rule against fake reviews and testimonials, including AI-generated ones, took effect on 21 October 2024.',
           'Now red-team the MTRX™ pitch with the levers from stop 7.1, as the diagram does. Reciprocity is honest when the free thing is genuinely useful, like a quick audit of a clinic’s website, with no strings. Social proof is honest when the results are real, named and permitted, like HansWild. Authority is honest when you show your own work, not borrowed logos. Scarcity is honest only when your calendar really is full. Commitment is honest when a small first step, a discovery call, leaves the client free to stop. Each lever has a con twin: the fake audit, the invented testimonial, the borrowed badge, the countdown timer, the contract that traps.',
           'One test runs through this whole course and separates persuasion from a con: reversibility. A con makes checking costly and leaving shameful. Honest persuasion gives the buyer time, alternatives and records. So for every claim in a pitch, ask two questions: can the client check it, and can they say no without losing face? A proposal with scope, exclusions, timeline, price, risks and a clear way out passes. A call that says this price is only for today fails, and stop 7.1 showed that urgency barely works anyway.',
           'Your callers need the same rules, because commission creates pressure. They book discovery calls; they do not close. Give them a short honesty script: say who you are and why you are calling, never invent a deadline or a discount, never claim a result for a clinic you have not achieved, and accept no the first time. A caller who hears no politely today leaves the door open for yes in three months. A caller who pushes leaves behind a one-star story.',
           'For a writer, the honest salesperson is the harder character. A hustler only wants the sale. An honest seller wants the sale and the relationship, and the climax is the moment they must choose. That is the arc of Jerry Maguire and his mission statement, and of Jimmy McGill in reverse, who keeps choosing the shortcut until he becomes Saul. The drama of honest persuasion is the moment the truth might lose the deal.'],
    fig=(FIG, 'Five levers, each with an honest version and a con version. The test is whether the buyer can check and leave.'),
    specs=[('Dark pattern', 'A design trick that pushes users into choices they did not intend, such as false urgency or hidden costs.'),
           ('Drip pricing', 'Showing a low price first and adding fees step by step at checkout. One of India’s 13 listed patterns.'),
           ('Red-teaming', 'Attacking your own plan the way an opponent would, to find the weak spots before someone else does.')],
    tags=[('anti', '“A countdown timer boosts sales.”', 'Urgency cues do little on average, and India lists false urgency as a banned dark pattern.', ('PIB: the 13 dark patterns, 2023', 'https://www.pib.gov.in/PressRelease.aspx?PRID=2026257')),
          ('hold', '“Fake reviews are now illegal in the US.”', 'The FTC rule bans fake and AI-generated testimonials and fake social influence.', ('Federal Register: the FTC reviews rule', 'https://www.federalregister.gov/documents/2024/08/22/2024-18519/trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials')),
          ('field', '“My pitch is honest.”', 'Test it: can the client check every claim and say no without losing face?', ('FTC announcement, 14 August 2024', 'https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials'))],
    distil=[('CCPA: Guidelines for Prevention and Regulation of Dark Patterns, 2023', 'https://consumeraffairs.nic.in/sites/default/files/The%20Guidelines%20for%20Prevention%20and%20Regulation%20of%20Dark%20Patterns%2C%202023.pdf', 'The 13 patterns, officially'),
            ('PIB: the dark pattern guidelines explained', 'https://www.pib.gov.in/PressRelease.aspx?PRID=2026257', 'A plain-language summary'),
            ('FTC: final rule banning fake reviews and testimonials', 'https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials', 'The US rule')],
    writer=dict(notes=['The honest persuader is a two-goal character: the sale and the relationship. Build the climax around the moment those goals clash, and make the truth cost something.',
                       'Mirror scenes work: a hustler and an honest seller pitch the same client, line by line. The audience learns the difference without a lecture.'],
                drill='Write a one-page fictional scene where a young agency owner pitches a nervous dentist. Halfway through, the dentist asks a question whose honest answer might lose the deal. Write the honest answer and what happens next.'),
    biz='Run the red team on MTRX™ this week. Read your website, your Instagram bio, your callers’ script and your last proposal, and mark every claim: can a client check it? Cut anything that is not true today. Replace urgency with honest capacity, such as “I take four new clinic projects a month”. Get written permission before naming any client. Put scope, exclusions and an exit in every proposal. And refuse to build dark patterns for clients: it protects them, their customers and your name.',
    tryit='Take your callers’ opening script. Mark each line H for honest, C for could be a con, or ? for check. Rewrite every C line so the person on the other end can check it and say no.',
    room='Persuasion is honest when the buyer can inspect the bridge before crossing it.',
    deeper=[('PIB: penalties for misleading advertisements', 'https://www.pib.gov.in/PressReleasePage.aspx?PRID=1897389', '₹10 lakh and ₹50 lakh')],
    nextq='One task left: put the whole course into a story. Can you write a con film treatment that fools the audience fairly? Stop 7.6.',
    checks=[dict(q='Which of these is one of the 13 dark patterns listed in India’s 2023 guidelines?',
                 o=['Drip pricing', 'Free delivery', 'Verified reviews'], a=0,
                 w='Drip pricing reveals fees step by step at checkout. False urgency and confirm shaming are listed too.'),
            dict(q='What test separates honest persuasion from a con in this course?',
                 o=['Whether the buyer can check the claim and leave without shame',
                    'Whether the pitch uses any of Cialdini’s levers at all',
                    'Whether the seller personally believes in the product'], a=0,
                 w='Reversibility. Cons make checking costly and leaving shameful; honest pitches do the opposite.'),
            dict(q='What is the honest version of scarcity for an agency?',
                 o=['A genuinely limited number of projects each month',
                    'A countdown timer on the pricing page',
                    'A discount that expires at midnight'], a=0,
                 w='Scarcity is only honest when the limit is real. Fake deadlines also barely work.')],
)

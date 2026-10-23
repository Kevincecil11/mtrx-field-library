from svg import box, t, arrow, line, svg

COLS = [('PONZI', 'new investors’ deposits', 'nothing: returns are fake', 'losing most of it'),
        ('PYRAMID', 'recruits’ joining fees', 'recruiting more recruits', 'losing what they paid in'),
        ('MLM, IF LEGAL', 'sales to real customers', 'sales, yours and your team’s', 'earning little after costs')]
ROWS = ['MONEY FROM', 'PAID FOR', 'MOST END UP']
def col(i, c):
    x = 200 + i * 330
    out = box(x, 56, 310, 50, 's-box-j', 10) + t(x + 155, 87, c[0], 's-t-b')
    for r in range(3):
        y = 122 + r * 74
        out += box(x, y, 310, 60, 's-box-a' if r == 2 else 's-card', 10) + t(x + 155, y + 36, c[r + 1], 's-t-sm')
    return out
FIG = svg(1180, 420, 'Ponzi, pyramid and legal MLM compared: where the money comes from, what you are paid for, and how most people end up',
          t(590, 32, 'THREE MONEY MACHINES THAT CAN SOUND THE SAME', 's-t') +
          ''.join(t(100, 158 + r * 74, n, 's-t-b') for r, n in enumerate(ROWS)) +
          ''.join(col(i, c) for i, c in enumerate(COLS)) +
          line(80, 362, 1100, 362, True) +
          t(590, 396, 'One question sorts all three: who is the real customer, and where does the money come from?', 's-t-sm'))

STOP = dict(
    id='6.2', day=37, title='Ponzi, pyramid or MLM: telling them apart',
    q='An MLM recruiter and a pyramid scheme recruiter can use exactly the same words. So how do you tell a legal business from a scheme that is mathematically doomed?',
    why='Ponzi schemes hide behind a fake investment. Pyramid schemes hide behind a fake job, and they are often wrapped around a real product, which makes them harder to spot. Multi-level marketing sits right next door: legal, but with maths that leaves most members out of pocket. For a writer it is a rich setting for a story about hope and belonging. For a business owner it is a lesson in reading incentives: what are people actually paid for?',
    case=dict(k='The case', name='FTC v. Herbalife, July 2016', role='A settlement that forced a giant MLM to rebuild its pay plan',
              facts=[('The payment', '$200 million for consumers'),
                     ('The rule', 'Rewards must be driven by tracked, verified retail sales'),
                     ('The test', '“Rewarded for what they sell, not how many people they recruit”'),
                     ('The catch', 'The FTC did not label Herbalife a pyramid scheme')],
              stamp=('part', 'Partly: legal is not the same as fair')),
    cold=dict(q='If every member of a pyramid scheme must recruit six new members, how many levels does it take to need more people than live on Earth?',
              a='Thirteen. Six to the power of thirteen is about 13 billion, and there are roughly 8 billion people alive. Long before that the scheme hits a wall, because every town, college and family runs out of new recruits. That is why pyramid schemes are illegal: the people at the bottom, who are always the majority, are mathematically certain to lose. The FTC’s test turns this into one question: is the money coming from real customers or from new recruits?'),
    video=dict(id='SBGfHk91Vrk', title='How to spot a pyramid scheme', who='TED-Ed, Stacie Bosley',
               watch=['How the video separates a product business from a recruitment business',
                      'Why the maths always fails the people who join last',
                      'The question you would now ask a recruiter']),
    story=['Three schemes, one question. A Ponzi scheme says: give me your money and I will invest it. There is no real investment; returns come from newer investors. A pyramid scheme says: pay to join, then earn by recruiting others who pay to join. There may be a product, but the money really flows from recruits, not customers. A multi-level marketing company, or MLM, says: sell our products, recruit others to sell, and earn from both. That model is legal in many countries, including the United States and India, as long as the money comes mainly from real sales to real customers.',
           'Herbalife is the classic test case. In 2016 the US Federal Trade Commission charged that the company’s pay plan rewarded distributors for recruiting others and for buying product themselves, rather than for real retail demand, and that the overwhelming majority earned little or no money. Herbalife agreed to pay $200 million to consumers and to rebuild its US business so that rewards follow tracked, verified retail sales, watched by an independent auditor for seven years. The FTC’s chair put the test in one line: participants should be “rewarded for what they sell, not how many people they recruit”. Notice what the FTC did not do. It did not call Herbalife a pyramid scheme. Legal and fair to most members are two different claims.',
           'The numbers for ordinary members are grim even when everything is legal. A 2018 AARP Foundation survey found that about 7.7 percent of American adults had joined an MLM at some point. Nearly half said they lost money and about a quarter broke even. Of the quarter who made a profit, more than half made less than $5,000. In 2024 the FTC reviewed 70 MLM income disclosure statements and found that most participants received $1,000 or less a year, often before expenses. The pitch shows the top of the pyramid. The disclosure shows the base.',
           'So why do people stay? Because an MLM sells more than products. It sells a community, a boss-free identity and a story in which you are one recruit away from freedom, which is why the meetings can sound like the recruitment you met in File 1. Losses get framed as your fault: you did not work hard enough or believe enough. That is the tell. A business that blames you for its maths is protecting the maths. The FTC’s own consumer guide is blunt: most people who join legitimate MLMs make little or no money.',
           'For a writer this world is gold, because everyone in it has a reason. Showtime’s On Becoming a God in Central Florida (2019) stars Kirsten Dunst as a water-park worker who joins the very scheme that ruined her family, hoping to beat it from the inside. The documentary series LuLaRich (2021) shows the same hope and debt in real life. Both work because they treat members as people with reasons, not fools. The real villain is the incentive plan.'],
    fig=(FIG, 'Ponzi, pyramid and legal MLM side by side. The test is always the same: who is the real customer?'),
    specs=[('Pyramid scheme', 'A scheme where members earn mainly by recruiting others who pay to join, not by selling to real customers.'),
           ('Multi-level marketing (MLM)', 'Selling through a network of distributors who earn from their own sales and from their recruits’ sales.'),
           ('Income disclosure statement', 'A document some MLMs publish showing what members actually earned. Read the typical figure, not the top.')],
    tags=[('myth', '“If there is a real product, it cannot be a pyramid scheme.”', 'A product can be a cover. The test is whether the money comes from real customers or from recruits.', ('FTC consumer guide: MLMs and pyramid schemes', 'https://consumer.ftc.gov/articles/multi-level-marketing-businesses-and-pyramid-schemes')),
          ('part', '“MLMs are just pyramid schemes.”', 'Not legally, if real retail sales drive the pay. But most members still earn little or nothing.', ('FTC review of 70 MLM income disclosures', 'https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-staff-report-analyzes-70-mlm-income-disclosure-statements')),
          ('hold', '“Most people who join an MLM do not make money.”', 'AARP Foundation 2018: 47% lost money and 27% broke even.', ('AARP Foundation MLM study summary', 'https://www.aarp.org/content/dam/aarp/aarp_foundation/2018/pdf/AARPFResearchExecutiveSummaryFINAL101018.pdf'))],
    distil=[('FTC: Herbalife settlement, 15 July 2016', 'https://www.ftc.gov/news-events/news/press-releases/2016/07/herbalife-will-restructure-its-multi-level-marketing-operations-pay-200-million-consumer-redress', 'The retail-sales test'),
            ('FTC staff report on MLM income disclosures, 2024', 'https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-staff-report-analyzes-70-mlm-income-disclosure-statements', 'What members really earn'),
            ('AARP Foundation MLM research report, 2018', 'https://www.aarp.org/content/dam/aarp/aarp_foundation/2018/pdf/AARP%20Foundation%20MLM%20Research%20Study%20Report%2010.8.18.pdf', 'Who joins, and who profits')],
    writer=dict(notes=['In an MLM story the antagonist is the pay plan. Show it early, in a bright meeting with music and testimonials, and let the audience work out the maths before the hero does.',
                       'Give the recruiter a real reason. The best MLM characters are not liars. They believe, because believing is the only way their own losses make sense: the dissonance from stop 1.5 in a branded polo shirt.'],
                drill='Write a one-page fictional scene where a character pitches an MLM opportunity to an old school friend over coffee. Every line must be something a real recruiter could say honestly. The friend wins the scene with one question about money.'),
    biz='MTRX™ will meet this world from the other side: members asking for websites, funnels and chatbots for their business. Build carefully. Do not build pages that promise income or a lavish lifestyle; the Herbalife order banned exactly those claims. Price for the client’s real budget, because most members earn little, and take payment upfront.',
    tryit='Search any MLM company’s name plus “income disclosure”. Write down the typical yearly earnings, then compare it with the figure in their best-known testimonial.',
    room='Follow the money to the real customer. If the customer is the next recruit, it is a pyramid.',
    deeper=[('FTC consumer guide: MLMs and pyramid schemes', 'https://consumer.ftc.gov/articles/multi-level-marketing-businesses-and-pyramid-schemes', 'The questions to ask before joining')],
    nextq='Theranos promised more than 240 tests from a few drops of blood, and investors valued it at $9 billion. How did a story get that far ahead of the science? Stop 6.3.',
    checks=[dict(q='What is the FTC’s key test for whether an MLM pays people legitimately?',
                 o=['Whether rewards come from real retail sales, not recruiting',
                    'Whether the company sells a real product',
                    'Whether the founder is personally wealthy'], a=0,
                 w='A product can be a cover. What matters is who the real customer is and where the money comes from.'),
            dict(q='If each member must recruit six people, roughly how many levels until a pyramid needs more people than exist?',
                 o=['Thirteen levels', 'Thirty levels', 'A hundred levels'], a=0,
                 w='Six to the thirteenth power is about 13 billion, more than everyone alive. The base always loses.'),
            dict(q='What did the AARP Foundation’s 2018 survey find about MLM participants?',
                 o=['Nearly half lost money and about a quarter broke even',
                    'Most made a steady part-time income',
                    'About half earned over $10,000 a year'], a=0,
                 w='Only about a quarter made a profit, and more than half of those made under $5,000.')],
)

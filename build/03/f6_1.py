from svg import box, t, arrow, line, svg

LOOP = [(60, 70, 'NEW MONEY IN', 'from new investors'), (420, 70, 'PAID AS RETURNS', 'old investors get paid'),
        (420, 230, 'RETURNS AS PROOF', 'payouts become adverts'), (60, 230, 'TRUST SPREADS', 'friends and word of mouth')]
FIG = svg(1180, 420, 'The Ponzi engine: new money pays old investors, payouts become proof, trust spreads, and the loop dies when withdrawals beat deposits',
          t(590, 32, 'THE PONZI ENGINE: WHY IT PAYS, AND WHY IT DIES', 's-t') +
          ''.join(box(x, y, 270, 90, 's-card', 12) + t(x + 135, y + 38, a, 's-t-b') + t(x + 135, y + 68, b, 's-t-sm')
                  for x, y, a, b in LOOP) +
          arrow(332, 115, 418, 115) + arrow(555, 162, 555, 228) + arrow(418, 275, 332, 275) + arrow(195, 228, 195, 162) +
          arrow(575, 195, 776, 195, True) + t(676, 183, 'when it stops', 's-t-sm') +
          box(780, 100, 340, 190, 's-box-a', 12) + t(950, 140, 'THE KILL SWITCH', 's-t-b') +
          t(950, 176, 'withdrawals beat new money', 's-t-sm') + t(950, 214, '1920: a newspaper asks', 's-t-sm') +
          t(950, 244, '2008: a market crash', 's-t-sm') +
          line(80, 352, 1100, 352, True) +
          t(590, 388, 'There is no business inside the loop. The only fuel is the next investor.', 's-t-sm'))

STOP = dict(
    id='6.1', day=36, title='Ponzi and affinity fraud: from Charles Ponzi to Madoff',
    q='Bernie Madoff ran the largest Ponzi scheme in history for decades, and his clients queued to get in. What exactly were they trusting?',
    why='Every con so far needed a story and a mark. A Ponzi scheme needs one more thing: a steady flow of new cash. It can run for years because it really does pay people, at least the early ones. For a writer it is a ticking clock built into the plot, because the scheme dies the day withdrawals beat deposits. For a business owner it teaches the most useful money question there is: where, exactly, does the return come from?',
    case=dict(k='The case', name='Bernard L. Madoff, December 2008', role='A Wall Street insider whose advisory business was a Ponzi scheme',
              facts=[('The insider', 'Former NASD vice chairman and Nasdaq board member (SEC)'),
                     ('The size', 'More than $17bn under management at the start of 2008'),
                     ('The confession', '“Basically, a giant Ponzi scheme”, he told two senior employees'),
                     ('The clean-up', 'About $15.5bn recovered or agreed for customers by September 2026')],
              stamp=('hold', 'Holds: the classic Ponzi')),
    cold=dict(q='Charles Ponzi really did pay his first investors what he promised. Why is paying people back the most dangerous thing a fraud can do?',
              a='Because the payment is the advert. Every investor who got their money back with interest became a walking testimonial, and their neighbours queued with their savings. Ponzi’s notes promised 50 percent in 90 days, and the New York Times reported in July 1920 that he usually paid in 45. The money for those payments came from later investors. A Ponzi scheme does not hide its returns. It shows them off, because the returns are what recruit the next wave.'),
    video=dict(id='s68FR1MXT8Q', title='The Man Who Knew', who='CBS News',
               watch=['What first made Harry Markopolos suspicious of Madoff’s numbers',
                      'Why smooth, steady returns were a warning sign, not a comfort',
                      'How his warnings were received, and what that tells you about checking']),
    story=['Start in Boston, 1920. Charles Ponzi, an Italian immigrant, told investors he had found a loophole. International reply coupons, a kind of prepaid postage voucher, could be bought cheaply in post-war Europe and swapped for more valuable stamps in the United States. His Securities Exchange Company promised 50 percent in 90 days. Early investors were paid, word spread, and over about eight months he took in roughly $15 million, according to the US National Archives. Postal inspectors found the flaw: worldwide sales of the coupons were nowhere near big enough to support his story. The Boston Post’s reporting on him won the 1921 Pulitzer Prize for public service.',
           'The engine has not changed in a century, and the diagram shows it. New money comes in. Some of it goes out as returns to earlier investors. Those returns become proof, the proof becomes advertising, and trust spreads to new investors. There is no business inside the loop. The scheme dies only when withdrawals beat new deposits, which is why a Ponzi scheme fears a bad headline or a market crash more than it fears a regulator.',
           'Now jump to New York, December 2008. Bernard Madoff was not a stranger with a loophole. He was an insider: a former vice chairman of the NASD, the industry’s own regulator, and a member of Nasdaq’s board of governors. His advisory business reported steady gains in good years and bad, and being let in felt like a privilege. Clients came through trusted networks: friends, charities, country clubs and feeder funds that passed their clients’ money on to him. When the 2008 crash brought a wave of withdrawal requests, the loop stalled. He told two senior employees that it was “all just one big lie” and “basically, a giant Ponzi scheme”, and the SEC charged him on 11 December 2008.',
           'This is affinity fraud: a con that borrows trust from a group. The SEC warns that these schemes target religious and ethnic communities, the elderly and professional groups, and that promoters are often, or pretend to be, members themselves. Respected members who believe in the scheme then vouch for it in good faith. The trust is real; it is just pointed at the wrong thing. People trusted the man, the community and the friend who introduced them, so nobody asked how the returns were made. One analyst who did ask, Harry Markopolos, sent the SEC a memo in November 2005 titled “The World’s Largest Hedge Fund is a Fraud”. Stop 7.4 follows what happened to it.',
           'Madoff pleaded guilty in 2009, was sentenced to 150 years and died in prison in 2021. The court-appointed trustee has since recovered or agreed to recover about $15.5 billion for customers, a record for any Ponzi case. For a writer, the scheme hands you a clock that ticks louder in every scene: the next withdrawal request. HBO’s The Wizard of Lies (2017), with Robert De Niro as Madoff, plays the collapse as a family drama, because the people closest to a Ponzi scheme are often the last to see it.'],
    fig=(FIG, 'The Ponzi engine: new money pays old investors, payouts become proof, trust spreads, and the loop dies when withdrawals beat deposits.'),
    specs=[('Ponzi scheme', 'A fraud that pays earlier investors with money from newer investors, not from real profits.'),
           ('Affinity fraud', 'A fraud aimed at a community, which borrows the trust members already have in each other.'),
           ('Feeder fund', 'A fund that collects clients’ money and invests it with another manager, as many did with Madoff.')],
    tags=[('myth', '“If it pays out on time, it must be real.”', 'Ponzi paid early investors on time. A payment proves money moved, not that profits exist.', ('National Archives: When Ponzi’s Bubble Burst', 'https://www.archives.gov/publications/prologue/2010/summer/ponzi-inmate-case-file')),
          ('hold', '“Madoff paid returns out of other investors’ money.”', 'The SEC said he admitted paying returns from the principal of other, different investors.', ('SEC release 2008-293', 'https://www.sec.gov/news/press/2008/2008-293.htm')),
          ('part', '“Affinity fraudsters are outsiders pretending to belong.”', 'Some pretend. Many are real members, and respected insiders often vouch for the scheme in good faith.', ('SEC on affinity fraud', 'https://www.sec.gov/about/divisions-offices/division-enforcement/affinity-fraud'))],
    distil=[('National Archives: When Ponzi’s Bubble Burst', 'https://www.archives.gov/publications/prologue/2010/summer/ponzi-inmate-case-file', 'The original scheme'),
            ('SEC: Madoff charged, 11 December 2008', 'https://www.sec.gov/news/press/2008/2008-293.htm', 'The confession and the size'),
            ('Madoff trustee: recoveries to date', 'https://www.madofftrustee.com/recoveries-04.html', 'What came back')],
    writer=dict(notes=['A Ponzi scheme is a built-in ticking clock. Every scene can ask the same question: what happens when someone asks for their money back? Put a withdrawal request in act one and the audience will feel every later one.',
                       'The richest victim is the introducer: the friend or community leader who brought others in and believed it. They lose money and standing at once, and then they have to face the people they recruited.'],
                drill='Write a one-page fictional scene at a family dinner where a respected guest describes an investment that “never has a bad month”. One quiet person asks how the returns are made. Write the table’s reaction, not the answer.'),
    biz='Use Madoff’s lesson on any deal that promises steady returns, including the passive-income offers that find agency owners on Instagram. Ask three questions: where does the return come from, who holds the money, and who checks it independently? If the answer is a person you trust rather than a document you can verify, walk away. And never let client money sit mixed with yours: a separate account and a clean invoice trail.',
    tryit='Watch the video above and write down, in one sentence, what first made Markopolos suspicious. Then find any online offer with guaranteed monthly returns and write the one question that would test it.',
    room='The first payment proves only that money moved, not why it moved.',
    deeper=[('Smithsonian Postal Museum: the Ponzi scheme', 'https://postalmuseum.si.edu/exhibition/behind-the-badge-case-histories-scams-and-schemes/ponzi-scheme', 'How the inspectors saw through it'),
            ('Pulitzer Prizes: The Boston Post, 1921', 'https://www.pulitzer.org/winners/boston-post', 'The newspaper that exposed him')],
    nextq='Ponzi schemes are illegal everywhere, yet multi-level marketing companies recruit in the open. Where exactly is the line between a pyramid scheme and a legal business? Stop 6.2.',
    checks=[dict(q='What keeps a Ponzi scheme alive?',
                 o=['New investors’ money paying earlier investors',
                    'Profits from a real but secret trading strategy',
                    'Government insurance on the deposits'], a=0,
                 w='There is no business inside the loop. The fuel is the next investor, and it dies when withdrawals beat deposits.'),
            dict(q='What makes affinity fraud so effective?',
                 o=['It borrows the trust members of a group already have in each other',
                    'It only targets people with no investing experience',
                    'It always uses complex financial products'], a=0,
                 w='The trust is real but pointed at the wrong thing. People trust the introducer and skip the checks.'),
            dict(q='What did Madoff tell two senior employees before the SEC charged him?',
                 o=['That it was “basically, a giant Ponzi scheme”',
                    'That a rogue trader had lost the money',
                    'That hackers had emptied the accounts'], a=0,
                 w='The SEC’s December 2008 release quotes him. He also said it was “all just one big lie”.')],
)

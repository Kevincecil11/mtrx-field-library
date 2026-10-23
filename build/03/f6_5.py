from svg import box, t, arrow, line, svg

CORNERS = [(200, 60, 'PRESSURE', 'a problem I cannot share'), (30, 250, 'OPPORTUNITY', 'a way to fix it quietly'),
           (370, 250, 'RATIONALISATION', 'words that keep me honest')]
FIXES = ['Pressure: honest targets, safe to ask for help', 'Opportunity: two people for every payment',
         'Rationalisation: name the excuses out loud', 'Capability: rotate roles, check the trusted']
FIG = svg(1180, 440, 'The fraud triangle of pressure, opportunity and rationalisation, with capability from the fraud diamond, and the control that breaks each corner',
          t(590, 32, 'THE FRAUD TRIANGLE, AND THE CONTROL THAT BREAKS EACH CORNER', 's-t') +
          line(250, 136, 160, 250) + line(410, 136, 500, 250) + line(290, 288, 370, 288) +
          ''.join(box(x, y, 260, 76, 's-box-a', 12) + t(x + 130, y + 32, a, 's-t-b') + t(x + 130, y + 60, b, 's-t-sm')
                  for x, y, a, b in CORNERS) +
          t(330, 200, 'CAPABILITY', 's-t-b') + t(330, 226, 'the diamond adds it', 's-t-sm') +
          t(920, 80, 'THE CONTROL THAT BREAKS IT', 's-t-b') +
          ''.join(box(680, 100 + i * 76, 480, 60, 's-card', 10) + t(920, 136 + i * 76, s, 's-t-sm') for i, s in enumerate(FIXES)) +
          t(590, 424, 'You cannot see inside a person. You can close the open door and make the problem shareable.', 's-t-sm'))

STOP = dict(
    id='6.5', day=40, title='The fraud triangle, and why good people cook the books',
    q='Satyam’s founder confessed to India’s biggest accounting fraud in a letter to his own board, and insisted he had not taken “even one rupee/dollar”. How does a respected businessman end up faking ₹5,040 crore of cash?',
    why='Ponzi, Madoff and Holmes are dramatic. Most fraud is not. It is a trusted manager adjusting a number, once, to get through a bad quarter. Criminologists have studied that moment for seventy years, and their best-known model, the fraud triangle, works for writers and founders alike. For a writer it gives motive, means and self-justification in one shape. For a business owner it shows where to put the locks.',
    case=dict(k='The case', name='Satyam Computer Services, January 2009', role='Once India’s fourth-largest software services firm',
              facts=[('The letter', '7 January 2009, to the board, copied to SEBI'),
                     ('The hole', '₹5,040 crore of cash and bank balances that did not exist'),
                     ('His words', '“Like riding a tiger, not knowing how to get off”'),
                     ('The verdict', 'April 2015: Raju and nine others sentenced to seven years')],
              stamp=('hold', 'Holds: a small gap that grew')),
    cold=dict(q='Raju’s letter says the fraud began as something small. What do you think it was?',
              a='A gap. In his words: “What started as a marginal gap between actual operating profit and the one reflected in the books of accounts continued to grow over the years.” Each quarter the fake profit needed fake cash to match, and the gap grew as the company grew. He wrote that he feared weak results would invite a takeover that would expose it. That is how most fraud feels from the inside: not a heist, but a hole you keep digging so nobody sees you in it.'),
    video=dict(id='Tb6QX9Yy1GM', title='How people rationalize fraud', who='TED-Ed, Kelly Richmond Pope',
               watch=['The three corners of the fraud triangle, and which is hardest to see',
                      'The everyday excuses people use before they cross the line',
                      'Which corner a company can actually control']),
    story=['In the late 1940s an American criminologist, Donald Cressey, interviewed 133 men in prison for embezzlement: trusted employees who had stolen from their employers. In Other People’s Money (1953) he proposed that trusted people become trust violators when three things meet. They have a financial problem they feel they cannot share. They see that their position lets them solve it secretly. And they find words that let them still see themselves as honest: borrowing, not stealing; everyone does it; the company owes me.',
           'Later teachers turned this into the fraud triangle: pressure, opportunity and rationalisation, now standard in fraud examiners’ training. Two cautions. Cressey himself never used the phrase, and two of his three factors built on earlier work by Svend Riemer, according to a 2021 paper by Peter Tickner and Mark Button. And when Paul Klenowski and Heith Copes repeated Cressey’s study with 25 imprisoned offenders, they found only weak support for the secret money problem, since about half never mentioned one, but strong support for the self-justifying words. The triangle is a useful lens, not a law of nature.',
           'A fourth corner helps. In 2004 David Wolfe and Dana Hermanson proposed the fraud diamond, which adds capability: the position, skill, confidence and nerve to carry a fraud off and keep the story straight for years. Plenty of people feel pressure and see an open door. Few can sustain the lie. Those who do are usually senior, clever and trusted, which is exactly why nobody checks them.',
           'Now read Raju’s letter with the diamond. Pressure: a gap between real and reported profit that grew every quarter, and the fear that a takeover would expose it. Opportunity: as founder and chairman he controlled what the books said, and the checks around him failed for years. Rationalisation: “neither me, nor the Managing Director took even one rupee/dollar from the company”. Capability: by his own count, a company of 53,000 people with 185 Fortune 500 clients. In April 2015 a special court in Hyderabad sentenced him and nine others, including two former PwC auditors, to seven years.',
           'For a writer the triangle is a character arc in disguise. Pressure is the inciting incident. Opportunity is the door left open. Rationalisation is the line the character says to the mirror, and capability is why we believe they can pull it off. The great sales and money stories, from Glengarry Glen Ross to The Wolf of Wall Street, spend most of their time on that third corner: the words people use to stay the hero of their own story. For an organisation, the defence works on the corners you can reach: close the open doors, set honest targets, and make it normal to say “I have a problem” before it becomes a secret.'],
    fig=(FIG, 'The fraud triangle, the fourth corner from the fraud diamond, and the control that breaks each one.'),
    specs=[('Fraud triangle', 'Pressure, opportunity and rationalisation: three conditions linked to fraud, adapted from Cressey.'),
           ('Rationalisation', 'The story a person tells themselves to feel honest while doing something dishonest.'),
           ('Segregation of duties', 'Splitting a task so no single person can both make and approve a payment.')],
    tags=[('myth', '“Cressey named the fraud triangle.”', 'He never used the phrase. The label came later, and two of his factors built on Riemer (1941).', ('Tickner and Button, 2021', 'https://doi.org/10.1108/jfc-10-2020-0204')),
          ('hold', '“The excuse comes before the crime.”', 'A replication found strong support for self-justifying words and weaker support for secret money problems.', ('Klenowski and Copes: a test of Cressey', 'https://doi.org/10.21428/88de04a1.9f45b3c4')),
          ('part', '“Fraud is always about greed.”', 'Often it starts as fear of exposure. Raju’s letter blames a growing gap and a takeover threat.', ('Raju’s letter, filed with the SEC', 'https://www.sec.gov/Archives/edgar/data/1106056/000114554909000025/u00107exv99w2.htm'))],
    distil=[('Raju’s letter to the Satyam board, 7 January 2009', 'https://www.sec.gov/Archives/edgar/data/1106056/000114554909000025/u00107exv99w2.htm', 'The primary source'),
            ('Tickner and Button: the origins of the fraud triangle', 'https://doi.org/10.1108/jfc-10-2020-0204', 'What Cressey really said'),
            ('Wolfe and Hermanson: the fraud diamond', 'https://digitalcommons.kennesaw.edu/facpubs/1537', 'The fourth corner')],
    writer=dict(notes=['Use the triangle as an arc. Pressure is the inciting incident, opportunity the open door, rationalisation the line said to the mirror. Write the first small step so the audience half agrees with it.',
                       'The best fraud scenes are quiet: one person, one spreadsheet, one number. Raju’s phrase, a marginal gap that grew, is a whole structure: a small lie, a bigger lie, no way back.'],
                drill='Write a one-page fictional monologue for an accountant the night before an audit. She moved one number, once, two years ago. Let her justify it three different ways, and let the audience watch each excuse fail.'),
    biz='Close the corners you can reach. At MTRX™ that means one person creates an invoice and another checks it, even if the other person is your accountant. Your callers’ commission is paid only on money actually collected, which already removes an open door. Add a monthly ten-minute look at what was billed, paid and promised. Most of all, make it normal for your team to say “I made a mistake” early, because hidden problems are where fraud starts.',
    tryit='Think of a time you bent a small rule at work or college. Write the exact words you used to justify it. Then label them: which part was pressure, which was opportunity, which was the excuse? Self-reflection only.',
    room='Fraud rarely starts with greed. It starts with a gap someone is ashamed to share.',
    deeper=[('The Hindu: all ten accused found guilty in the Satyam case', 'https://www.thehindu.com/business/All-10-accused-found-guilty-in-Satyam-case/article60344158.ece', 'The 2015 verdict')],
    nextq='The biggest frauds now arrive on your phone: a wrong-number text, a WhatsApp job, a caller in uniform, a client who overpays. What do they share, and how do you shut them down? Stop 6.6.',
    checks=[dict(q='What are the three corners of the fraud triangle?',
                 o=['Pressure, opportunity and rationalisation',
                    'Greed, secrecy and luck',
                    'Motive, weapon and alibi'], a=0,
                 w='Adapted from Cressey’s 1953 study of embezzlers. The fraud diamond adds a fourth: capability.'),
            dict(q='How did Raju describe the start of the Satyam fraud?',
                 o=['A marginal gap between real and reported profit that kept growing',
                    'A plan to steal from investors from day one',
                    'A single bad deal hidden by a junior employee'], a=0,
                 w='His letter says the gap grew as the company grew, and that he feared a takeover would expose it.'),
            dict(q='Which corner of the triangle can a business most directly control?',
                 o=['Opportunity, through checks like two-person approval',
                    'Rationalisation, by hiring only honest people',
                    'Pressure, by removing all targets'], a=0,
                 w='You cannot see inside a person. You can close the open door and make problems safe to share.')],
)

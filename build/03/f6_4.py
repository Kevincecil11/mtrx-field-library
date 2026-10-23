from svg import box, t, arrow, line, svg

ROWS = [('THE AUDITOR', 'most statements unaudited', 'clean sign-offs for years'),
        ('THE INSIDE', 'payments approved by emoji', 'cash that did not exist'),
        ('THE REGULATOR', 'run from the Bahamas', 'banned short selling'),
        ('THE OUTSIDERS', 'a news site read the books', 'the FT kept digging')]
def grid():
    out = ''
    for j, h in enumerate(['FTX, 2022', 'WIRECARD, 2020']):
        x = 270 + j * 450
        out += box(x, 56, 430, 46, 's-box-j', 10) + t(x + 215, 85, h, 's-t-b')
    for r, (lab, a, b) in enumerate(ROWS):
        y = 116 + r * 62
        cls = 's-box-a' if r == 3 else 's-card'
        out += t(135, y + 31, lab, 's-t-b')
        out += box(270, y, 430, 50, cls, 10) + t(485, y + 31, a, 's-t-sm')
        out += box(720, y, 430, 50, cls, 10) + t(935, y + 31, b, 's-t-sm')
    return out
FIG = svg(1180, 420, 'Who was supposed to check FTX and Wirecard: auditors, insiders and regulators failed; outsiders who did the arithmetic got it right',
          t(590, 32, 'WHO WAS SUPPOSED TO CHECK?', 's-t') + grid() +
          t(590, 396, 'Every inside check assumed another one was working. The outsiders who did the sums were treated as the enemy.', 's-t-sm'))

STOP = dict(
    id='6.4', day=39, title='FTX and Wirecard: when nobody checks',
    q='At FTX, managers approved payments with emoji. At Wirecard, the regulator went after the journalists instead of the company. What happens when everyone paid to check decides someone else is checking?',
    why='Theranos fooled people who could not check the science. FTX and Wirecard fooled people whose job was to check. Together they show how fraud survives inside institutions: auditors, boards, regulators and investors each assume the others are watching. For a writer this is the everyone-is-complicit story. For a business owner it is the case for boring controls.',
    case=dict(k='The cases', name='FTX, 2022, and Wirecard, 2020', role='A crypto exchange and a German payments giant, each gone within days',
              facts=[('FTX', 'Bankrupt 11 November 2022; founder later sentenced to 25 years'),
                     ('FTX’s new boss', '“Such a complete failure of corporate controls”'),
                     ('Wirecard', '€1.9bn that could not be verified; insolvent 25 June 2020'),
                     ('The twist', 'In 2019 the German regulator banned short selling of its shares')],
              stamp=('hold', 'Holds: the checks failed in layers')),
    cold=dict(q='In February 2019, after critical press reports about Wirecard, Germany’s financial regulator stepped in. Who do you think it targeted?',
              a='Not the company. BaFin banned new short positions in Wirecard shares for two months, and in April 2019 it filed a criminal complaint against two Financial Times journalists who had reported on it. The journalists were right. In June 2020 Wirecard said that €1.9 billion it claimed to hold in trust accounts probably did not exist, and it filed for insolvency on 25 June. The people raising the alarm had been treated as the threat.'),
    video=dict(id='AbgRB3arCpY', title='The FTX Collapse, Explained', who='The Wall Street Journal',
               watch=['How customer deposits ended up at Alameda Research',
                      'Which report started the rush of withdrawals in November 2022',
                      'Who, in theory, should have caught it earlier']),
    story=['Sam Bankman-Fried founded the crypto exchange FTX in 2019 and became the friendly face of crypto: shorts, messy hair, celebrity adverts and talk of giving his fortune away. Behind the brand, customer deposits were flowing to Alameda Research, his trading firm. In early November 2022 a news report on Alameda’s balance sheet, then a rival exchange’s decision to dump its FTX tokens, set off a rush of withdrawals that FTX could not pay. It filed for bankruptcy on 11 November 2022.',
           'The man brought in to clean up, John J. Ray III, had overseen the end of Enron. In his first court filing he wrote: “Never in my career have I seen such a complete failure of corporate controls and such a complete absence of trustworthy financial information as occurred here.” Reuters reported details from that filing: staff requested payments in an online chat and supervisors approved them with personalised emoji, and most of the financial statements Ray reviewed had never been audited. In November 2023 a jury convicted Bankman-Fried on seven counts of fraud and conspiracy. In March 2024 he was sentenced to 25 years.',
           'Wirecard was a German payments company that joined the DAX, Germany’s top share index, in 2018. For years the Financial Times, led by the reporter Dan McCrum, published evidence that its Asian business was not what it seemed. The response was ferocious. In February 2019 Germany’s regulator, BaFin, banned short selling in the shares, and it later filed a criminal complaint against two of the FT’s journalists. Then in June 2020 the auditor EY could not verify €1.9 billion said to sit in trust accounts in Asia. Wirecard admitted the money probably did not exist and filed for insolvency. Its chief executive, Markus Braun, was arrested. Its chief operating officer, Jan Marsalek, fled.',
           'Put the two side by side and the pattern matches. Each check assumed another check was working. Auditors relied on documents from third parties. Boards relied on charismatic founders. Regulators protected a national champion, or had little reach offshore. Investors relied on all of the above. The people who actually checked, a crypto news site reading a balance sheet, a newspaper reading documents, short sellers doing arithmetic, were treated as attackers until the end. Stop 7.4 meets them properly.',
           'For a writer this needs an ensemble, not a lone villain: the founder, the believer, the auditor who signs, the official who protects, the reporter who will not stop. Michael Lewis’s book Going Infinite (2023) shows how charming the founder could be up close. Netflix’s Skandal! Bringing Down Wirecard (2022) tells it from the journalists’ side. Even the ending has a twist: FTX’s bankruptcy plan aims to repay most customers at least 118 percent of their account values as of November 2022, yet many feel short-changed, because crypto prices rose far more after the collapse.'],
    fig=(FIG, 'Who was supposed to check FTX and Wirecard. The inside checks failed in layers; the outsiders got it right.'),
    specs=[('Short selling', 'Betting a share price will fall by selling borrowed shares and buying them back later.'),
           ('Audit', 'An independent check that accounts are true and fair. It relies on evidence, so faked evidence can fool it.'),
           ('Commingling', 'Mixing customer money with the company’s own, which makes it easy to spend what is not yours.')],
    tags=[('myth', '“A big-name auditor means the numbers are real.”', 'EY signed off on Wirecard for years. In 2020 it could not verify €1.9bn.', ('FT: Wirecard’s missing €1.9bn', 'https://www.ft.com/content/574ca70f-1d1e-4ade-b02b-9b846ea88d14')),
          ('hold', '“FTX had almost no real controls.”', 'Its new chief executive told the court he had never seen such a complete failure of controls.', ('Reuters on Ray’s first filing', 'https://www.reuters.com/technology/new-ftx-ceo-slams-complete-failure-corporate-control-2022-11-17/')),
          ('part', '“FTX customers got all their money back.”', 'The plan aims at 118% of November 2022 values, but customers missed the crypto rebound.', ('Reuters: FTX plan approved', 'https://www.reuters.com/legal/crypto-exchange-ftxs-liquidation-plan-receives-court-approval-2024-10-07/'))],
    distil=[('DOJ: Bankman-Fried sentenced to 25 years', 'https://www.justice.gov/archives/opa/pr/samuel-bankman-fried-sentenced-25-years-his-orchestration-multiple-fraudulent-schemes', 'Counts, sentence, forfeiture'),
            ('Reuters: FTX’s new chief on a complete failure of controls', 'https://www.reuters.com/technology/new-ftx-ceo-slams-complete-failure-corporate-control-2022-11-17/', 'Emoji approvals and missing records'),
            ('BaFin: the 2019 short-selling ban on Wirecard', 'https://www.bafin.de/SharedDocs/Veroeffentlichungen/EN/Aufsichtsrecht/Verfuegung/vf_190218_leerverkaufsmassnahme_en.html', 'The regulator’s own order')],
    writer=dict(notes=['Institutional fraud needs an ensemble. Give each checker a reason to look away that the audience understands: a fee, a deadline, national pride, a friendship. When everyone has a small excuse, the big lie becomes believable.',
                       'Let the outsider be wrong about something. Reporters and short sellers are more interesting when they doubt themselves, and their persistence matters more when it costs them.'],
                drill='Write a one-page fictional boardroom scene where four people each notice one small problem and each decides someone else will deal with it. End on the one person who does not.'),
    biz='MTRX™ is small, but the rule scales down: never mix money that is not yours with your own. If a client pays you for ad spend, hosting or a domain, keep it in a separate account or ledger, with receipts. Write three simple controls: who can approve a payment, where invoices live, and a monthly check of what came in against what was promised. Boring controls are what make you trustworthy at scale.',
    tryit='List every check in your own work: who sees your accounts, who would spot a mistake, what happens if you are wrong. Where is there no second pair of eyes? Write one check you will add this month.',
    room='Every check thought another check was working. Be the one who actually looks.',
    deeper=[('FT: Wirecard files for insolvency', 'https://www.ft.com/content/6a660a5f-4e8c-41d5-b129-ad5bf9782256', 'The collapse')],
    nextq='Most fraudsters are not career criminals. Satyam’s founder swore he never took a rupee. So why do ordinary, trusted people start cooking the books? Stop 6.5.',
    checks=[dict(q='What did FTX’s new chief executive say he had never seen in his career?',
                 o=['Such a complete failure of corporate controls',
                    'A crypto exchange with so many customers',
                    'A founder who cooperated so fully'], a=0,
                 w='Ray, who had handled Enron, also found no trustworthy financial information and payments approved by emoji.'),
            dict(q='How did Germany’s regulator respond to critical reports about Wirecard in 2019?',
                 o=['It banned short selling and filed a complaint against FT reporters',
                    'It ordered an immediate audit of the Asian accounts',
                    'It suspended the chief executive pending an inquiry'], a=0,
                 w='BaFin protected the company and pursued the journalists. The journalists were right.'),
            dict(q='What is the main lesson FTX and Wirecard share?',
                 o=['Each check assumed another check was working',
                    'Crypto is always riskier than payments',
                    'Short sellers cause company collapses'], a=0,
                 w='Auditors, boards, regulators and investors each relied on the others. The outsiders who checked were attacked.')],
)

from svg import box, t, arrow, line, svg

STEPS = [('WARMTH', 'intense attention'), ('ISOLATION', 'fewer friends'), ('MONITORING', 'phone, time, money'),
         ('RULES', 'dress, food, sleep'), ('PUNISHMENT', 'shame and threats'), ('DEPENDENCE', 'no exit left')]
FIG = svg(1180, 410, 'How coercive control builds a cage in small steps, from warmth to dependence, and where to get help in India',
          t(590, 32, 'SMALL RULES THAT BUILD A CAGE', 's-t') +
          ''.join(box(20 + i * 193, 60, 170, 110, 's-box-a' if i == 5 else 's-card', 12) + t(105 + i * 193, 104, a, 's-t-b') +
                  t(105 + i * 193, 138, b, 's-t-sm') for i, (a, b) in enumerate(STEPS)) +
          ''.join(arrow(192 + i * 193, 115, 211 + i * 193, 115) for i in range(5)) +
          t(105, 214, 'looks like care', 's-t-sm') + arrow(200, 209, 975, 209, True) + t(1070, 214, 'feels like a cage', 's-t-sm') +
          box(240, 246, 700, 84, 's-box-j', 12) + t(590, 280, 'IN INDIA, HELP IS ONE CALL AWAY', 's-t-b') +
          t(590, 312, 'Women Helpline 181  ·  NCW 24x7 helpline 14490  ·  Emergency 112', 's-t-sm') +
          t(590, 382, 'Each step can be explained away. The pattern is what the law now punishes.', 's-t-sm'))

STOP = dict(
    id='7.3', day=44, title='Coercive control: when influence becomes captivity',
    q='There may be no bruise, no single crime and no locked door, yet a person can lose almost all their freedom inside a relationship. How did the law learn to see that?',
    why='Everything in this course, love bombing, isolation, information control, the thumbscrew of stop 7.2, can happen inside one home. Sociologists call the pattern coercive control, and since 2015 several countries have made it a crime. For a writer, it is the most common and most realistic version of the cult story. For anyone, it is the most important set of warning signs in this guide, because it happens to people we know.',
    case=dict(k='The case', name='Coercive control in law', role='From a sociologist’s idea to a criminal offence',
              facts=[('The idea', 'Evan Stark, Coercive Control (2007)'),
                     ('England and Wales', 'A crime since 29 December 2015; up to five years'),
                     ('Scotland and Ireland', 'Laws in force from 1 April 2019 and 1 January 2019'),
                     ('India', 'PWDVA 2005 covers verbal, emotional and economic abuse')],
              stamp=('hold', 'Holds: a pattern, not one incident')),
    cold=dict(q='How many coercive control offences did police in England and Wales record in the year to March 2025?',
              a='49,557, up from 45,310 the year before, according to the Office for National Statistics. The offence is young: it came into force on 29 December 2015 and carries up to five years in prison. The ONS warns that changes in how police record crime affect comparisons, so part of the rise is better recognition. Either way, tens of thousands of cases a year in one country tells you this is not rare.'),
    video=dict(id='Miu7MNjqaYg', title='Real-Life Red Flags: Coercive Control Explained by Jess Phillips & Alice Liveing', who='Home Office',
               watch=['The everyday behaviours the video names as red flags',
                      'Why each one can look like care or love at first',
                      'Where the video says people can get help']),
    story=['The idea came from the American sociologist Evan Stark. In Coercive Control (2007) he argued that the core harm in many abusive relationships is not any single assault but the steady removal of a person’s freedom: isolating them, monitoring them, controlling their money, time and appearance, and making rules they must obey. Violence may or may not be part of it. The pattern is the point, which is why a list of separate incidents can make a controlling relationship look harmless.',
           'The law caught up slowly. In England and Wales, section 76 of the Serious Crime Act 2015 made controlling or coercive behaviour in an intimate or family relationship a crime from 29 December 2015, with a maximum of five years. The behaviour must be repeated or continuous and have a serious effect, such as fear of violence or serious alarm and distress that changes daily life. Scotland’s Domestic Abuse Act came into force on 1 April 2019 and Ireland’s offence on 1 January 2019. In the United States, Hawaii added coercive control to its domestic abuse law from 2021, and California’s family code covers conduct that “unreasonably interferes with a person’s free will and personal liberty”.',
           'India has no offence with that name, but its law reaches much of the pattern. The Protection of Women from Domestic Violence Act 2005 defines domestic violence to include “physical abuse, sexual abuse, verbal and emotional abuse and economic abuse”, and allows protection, residence and money orders. Cruelty by a husband or his relatives is a crime under section 85 of the Bharatiya Nyaya Sanhita 2023, which replaced section 498A of the old Penal Code. Help is a call away: the Women Helpline 181, the National Commission for Women’s 24-hour helpline 14490, and 112 in an emergency.',
           'The warning signs are ordinary-looking behaviours that add up. The UK’s Crown Prosecution Service lists examples such as cutting a person off from friends and family, monitoring their time or online activity, controlling where they go, who they see, what they wear and when they sleep, depriving them of basic needs, taking control of their money or work, repeated humiliation, and threats to share private information. Notice the overlap with File 1: isolation, information control and dependency are the cult toolkit at the scale of a couple or a family.',
           'For a writer, coercive control is the hardest version to tell well, because it is slow. The drama lives in small rules that each seem reasonable. BBC Radio 4’s The Archers ran a storyline about Helen Titchener and her husband Rob from 2014 to 2016 that helped millions of listeners recognise the pattern just as the new law arrived. On screen, Maid (Netflix, 2021) follows a young mother leaving an emotionally abusive partner. Both keep us with the person inside, which is where the audience belongs: inside the shrinking walls.'],
    fig=(FIG, 'Coercive control builds a cage in small steps. Each step can look like care; the pattern is the harm.'),
    specs=[('Coercive control', 'A pattern of behaviour that removes a person’s freedom through isolation, monitoring, rules and fear.'),
           ('Economic abuse', 'Controlling someone’s money, work or resources so they cannot decide or leave.'),
           ('Protection order', 'A court order forbidding an abuser from contacting or harming a person, available under India’s PWDVA.')],
    tags=[('myth', '“If there is no violence, it is not abuse.”', 'Stark’s point, and now the law’s: the pattern of control is the harm.', ('Serious Crime Act 2015, section 76', 'https://www.legislation.gov.uk/ukpga/2015/9/section/76')),
          ('hold', '“Indian law covers emotional and economic abuse.”', 'PWDVA 2005, section 3, includes verbal, emotional and economic abuse.', ('India Code: PWDVA 2005', 'https://www.indiacode.nic.in/bitstream/123456789/15436/1/protection_of_women_from_domestic_violence_act%2C_2005.pdf')),
          ('field', '“I would spot it straight away.”', 'Each step looks like care. Use the CPS list as a checklist, for friends as well as yourself.', ('CPS guidance on controlling or coercive behaviour', 'https://www.cps.gov.uk/prosecution-guidance/controlling-or-coercive-behaviour-intimate-or-family-relationship'))],
    distil=[('legislation.gov.uk: Serious Crime Act 2015, section 76', 'https://www.legislation.gov.uk/ukpga/2015/9/section/76', 'The offence'),
            ('CPS: controlling or coercive behaviour guidance', 'https://www.cps.gov.uk/prosecution-guidance/controlling-or-coercive-behaviour-intimate-or-family-relationship', 'The warning signs'),
            ('ONS: domestic abuse, year ending March 2025', 'https://www.ons.gov.uk/peoplepopulationandcommunity/crimeandjustice/articles/domesticabuseprevalenceandtrendsenglandandwales/yearendingmarch2025', 'The numbers')],
    writer=dict(notes=['Write it as escalation in small, reasonable steps. Each rule must make sense on its own, so the audience, like the victim, keeps excusing it.',
                       'Keep the camera with the person inside. The abuser’s motives matter less than the shrinking world: fewer friends, less money, more silence.'],
                drill='Write a one-page fictional scene in which a partner introduces a new rule, kindly. Show the other person agreeing, and the one detail that tells the audience this is a cage. Fiction only.'),
    biz='This touches MTRX™ in two ways. Your callers and clients are people first: if someone confides that a partner controls their phone or money, listen, believe them and share 181 or 112. And watch your own tools. AI receptionists, WhatsApp automation and location features can become monitoring tools in the wrong hands, so never build tracking that a person cannot see or switch off.',
    tryit='Read the CPS list of warning signs. Think of one relationship you know that once worried you, a friend’s or a relative’s. Which items fit? Write one kind thing you could say. Self-reflection only.',
    room='Abuse can be a pattern with no bruise. Watch the walls, not just the blows.',
    deeper=[('Ministry of Women and Child Development: Women Helpline 181', 'https://wcd.gov.in/women/help', 'One national number'),
            ('National Commission for Women: contact and helpline', 'https://www.ncw.gov.in/contact-us/', '24x7 helpline 14490')],
    nextq='Coercion thrives on silence. So who breaks it? Meet the analyst, the reporters and the short sellers who caught Madoff, Theranos and Wirecard. Stop 7.4.',
    checks=[dict(q='What was Evan Stark’s key point about coercive control?',
                 o=['The harm is the pattern of lost freedom, not one incident',
                    'It only counts as abuse if there is physical violence',
                    'It only happens inside religious cults'], a=0,
                 w='Isolation, monitoring and rules add up. A list of separate incidents can hide the cage.'),
            dict(q='When did coercive control become a crime in England and Wales?',
                 o=['In late 2015, under the Serious Crime Act',
                    'In the 1980s, under the old common law',
                    'Only in 2025, after a brand-new bill'], a=0,
                 w='Section 76 came into force on 29 December 2015, with up to five years in prison.'),
            dict(q='Which Indian law covers verbal, emotional and economic abuse at home?',
                 o=['The Protection of Women from Domestic Violence Act 2005',
                    'The Indecent Representation of Women (Prohibition) Act 1986',
                    'The Maintenance and Welfare of Parents and Senior Citizens Act 2007'], a=0,
                 w='Its section 3 definition includes all three, and it allows protection and residence orders.')],
)

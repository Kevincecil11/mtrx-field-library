from svg import box, t, arrow, line, svg

STEPS = [('1963', 'KUBARK warns pain', 'brings false stories'), ('1983', 'HRE manual taught', 'in Latin America'),
         ('2002', 'SERE resistance', 'training reversed'), ('2014', 'Senate finds the', 'methods ineffective'),
         ('2015', 'law: Army Field', 'Manual rules only')]
FIG = svg(1180, 400, 'How the coercive interrogation manuals travelled from 1963 to 2015, and how the Reid and PEACE police methods compare',
          t(590, 32, 'FROM THE MANUAL TO THE VERDICT', 's-t') +
          ''.join(box(20 + i * 232, 56, 210, 112, 's-box-a' if i == 3 else 's-card', 12) + t(125 + i * 232, 92, a, 's-t-b') +
                  t(125 + i * 232, 122, b, 's-t-sm') + t(125 + i * 232, 146, c, 's-t-sm') for i, (a, b, c) in enumerate(STEPS)) +
          ''.join(arrow(232 + i * 232, 112, 250 + i * 232, 112) for i in range(4)) +
          t(590, 206, 'IN THE POLICE ROOM', 's-t-b') +
          box(20, 222, 540, 112, 's-card', 12) + t(290, 256, 'REID TECHNIQUE (1962)', 's-t-b') +
          t(290, 286, 'accuse, cut off denials, minimise the crime', 's-t-sm') + t(290, 312, 'risk: false confessions', 's-t-sm') +
          t(590, 284, 'VS', 's-t-b') +
          box(620, 222, 540, 112, 's-box-j', 12) + t(890, 256, 'PEACE MODEL (1992)', 's-t-b') +
          t(890, 286, 'plan, engage, account, close, evaluate', 's-t-sm') + t(890, 312, 'aim: a full account you can check', 's-t-sm') +
          t(590, 374, 'Pressure produces words. Rapport produces accounts that can be checked against the evidence.', 's-t-sm'))

STOP = dict(
    id='8.4', day=51, title='Does coercion work? From KUBARK to the torture report',
    q='KUBARK warned in 1963 that pain produces false confessions. Four decades later the CIA used coercive techniques on detainees anyway. What does the evidence say coercion actually gets you?',
    why='This stop follows the manual out of the archive and into the world, then asks the only question that matters: does it work? The answer comes from an unusual alliance of sources: the CIA’s own 1963 warning, the Senate’s investigation of the CIA’s detention programme, and decades of research on police interviews and false confessions. It is the clearest case in this course of a story that is gripping, popular and wrong: that pressure breaks the truth loose.',
    case=dict(k='The case', name='The Senate torture report (2014)', role='The Senate Intelligence Committee’s study of CIA detention and interrogation',
              facts=[('Released', 'Findings published 9 December 2014'),
                     ('Finding 1', 'The techniques were “not an effective means of acquiring intelligence”'),
                     ('The law since', 'From 2015, detainee interrogation limited to the Army Field Manual'),
                     ('The science', '2016 review: rapport-based methods work best')],
              stamp=('hold', 'Holds: coercion fails the test')),
    cold=dict(q='The CIA used its “enhanced interrogation techniques” on 39 known detainees. According to the Senate study, how many of them produced no intelligence at all while in CIA custody?',
              a='Seven of the 39, according to the Senate Intelligence Committee’s 2014 findings. Others gave accurate information before the techniques were used, or without them, and several fabricated information under pressure, which produced faulty intelligence. The first finding is blunt: the techniques were “not an effective means of acquiring intelligence or gaining cooperation from detainees”. The CIA disputed many of the report’s conclusions. But KUBARK had named the core problem in 1963.'),
    video=dict(id='eOrl6rWHCP8', title='Interrogation Techniques Lead to False Confessions: Lindsay Malloy at TEDxFIU', who='Florida International University',
               watch=['Which pressures the speaker says make innocent people confess',
                      'Why young people are at special risk',
                      'What she says would protect them']),
    story=['KUBARK did not stay in its drawer. In 1983 the CIA produced a Human Resource Exploitation Training Manual that drew heavily on it, and CIA and Green Beret trainers used it in Latin America between 1983 and 1987. A senior CIA official later confirmed that the agency had trained Hondurans, and the Baltimore Sun linked that training to Battalion 316, a Honduran army unit accused of torture and disappearances. In 1984 and 1985 the manual was edited by hand to discourage abuse: “do not stress” became “deplore”, and “the proper way to use them” became “so that you may avoid them”. In 1996 the Pentagon released Spanish-language manuals used at the US Army’s School of the Americas that, the Washington Post reported, advocated executions, torture and blackmail.',
           'After 11 September 2001 the story repeated itself with a twist. US military SERE courses (Survival, Evasion, Resistance and Escape) train soldiers to resist captors who ignore the Geneva Conventions, and they drew partly on the Chinese methods of stop 8.2. Officials turned that training around and used it as a source for interrogating detainees. Two former Air Force psychologists linked to SERE, James Mitchell and Bruce Jessen, helped design the CIA’s programme, although, the Senate found, neither had experience as an interrogator. In 2017 they settled a lawsuit brought by former detainees and the family of Gul Rahman, who froze to death in a secret CIA prison. The terms are confidential.',
           'Then came the verdict. On 9 December 2014 the Senate Intelligence Committee released its findings. The first reads: “The CIA’s use of its enhanced interrogation techniques was not an effective means of acquiring intelligence or gaining cooperation from detainees.” Several detainees fabricated information, creating faulty intelligence. The CIA disputed many conclusions, and Congress acted anyway: since the defence law signed on 25 November 2015, interrogations of detainees by US agencies must stay within the Army Field Manual, which prohibits torture and cruel treatment. In 2016 the government’s High-Value Detainee Interrogation Group reviewed the science and concluded that the most effective methods are non-coercive and rapport-based.',
           'Police rooms tell the same story with ordinary suspects. The Reid technique, set out by Fred Inbau and John Reid in 1962, became the American standard: isolate the suspect, accuse, cut off denials and offer face-saving excuses. A 2010 scientific review led by Saul Kassin named the risk factors for false confession, including youth, intellectual disability, long interrogations, lying about evidence and minimising the crime, and called for every interrogation to be recorded. In 1989 five teenagers in New York confessed under pressure to an attack in Central Park. DNA excluded them, the real attacker confessed in 2002, their convictions were vacated that December, and the city settled for $41 million in 2014. In the Innocence Project’s cases, 29 percent involved a false confession.',
           'Britain took the other road. After the Guildford Four and Birmingham Six convictions collapsed, cases built on confessions obtained under police pressure, England and Wales adopted the PEACE model in 1992: Planning and preparation, Engage and explain, Account, Closure, Evaluation. Its aim is a full, checkable account, not a confession. A study of 142 real suspect interviews found that skilled PEACE interviewing produced fuller accounts, confessions included, and research on interviews with terrorist suspects found that rapport increased the information gained while even small amounts of hostility reduced it. India wrote a version of the lesson into law in 1872: a confession made to a police officer cannot be proved against the accused, a rule carried into the Bharatiya Sakshya Adhiniyam 2023, and in D.K. Basu v. State of West Bengal the Supreme Court set rules for arrest and custody to curb custodial torture.'],
    fig=(FIG, 'Top: the coercive manuals’ journey and the verdict. Bottom: two police methods, one built for confessions, one for accounts that can be checked.'),
    specs=[('Enhanced interrogation', 'The CIA’s term for the coercive techniques used on detainees after 2001. The Senate found them ineffective.'),
           ('False confession', 'An admission to a crime the person did not commit, often made to escape pressure.'),
           ('PEACE model', 'The interview method of England and Wales since 1992: plan, engage, get an account, close, evaluate.')],
    tags=[('myth', '“Torture gets results.”', 'Senate Finding 1: the techniques were “not an effective means of acquiring intelligence”.', ('Senate Intelligence Committee findings, 2014', 'https://www.intelligence.senate.gov/wp-content/uploads/2024/08/sites-default-files-press-findings-and-conclusions.pdf')),
          ('myth', '“Innocent people never confess.”', 'In the Innocence Project’s cases, 29% involved a false confession.', ('Innocence Project: exonerations data', 'https://innocenceproject.org/exonerations-data/')),
          ('hold', '“Rapport gets more than pressure.”', 'The US interrogation group’s 2016 science review found rapport-based methods most effective.', ('HIG: Interrogation, a review of the science (2016)', 'https://www.fbi.gov/file-repository/hig-report-interrogation-a-review-of-the-science-september-2016.pdf'))],
    distil=[('National Security Archive: the 1983 manual and its edits', 'https://nsarchive2.gwu.edu/NSAEBB/NSAEBB27/index.html', 'From “do not stress” to “deplore”'),
            ('Kassin et al. 2010: police-induced confessions', 'https://pubmed.ncbi.nlm.nih.gov/19603261/', 'The science of false confessions'),
            ('PBS: the Central Park Five, conviction and exoneration', 'https://www.pbs.org/kenburns/the-central-park-five/conviction-and-exoneration', 'A case that changed minds')],
    writer=dict(notes=['Retire the ticking-bomb scene, or turn it. Audiences have been taught that pressure breaks the truth loose. The braver scene shows a confession that is false, and lets the audience realise they believed it too.',
                       'Fiction shapes policy. Three senators, led by the Intelligence Committee chair Dianne Feinstein, called Zero Dark Thirty “grossly inaccurate and misleading in its suggestion that torture resulted in information” that found Osama bin Laden. Scott Z. Burns’s The Report (2019) tells the investigation instead. Know which film you are writing.'],
                drill='Write a one-page fictional interrogation in which a frightened young suspect confesses to something he did not do. Plant one detail that the audience can later use to prove the confession false.'),
    biz='The rapport research is free sales training. In a discovery call, pressure gets you a polite yes that never pays; rapport gets you the real problem. Use the PEACE shape: plan your questions, explain why you are calling, let the clinic owner give their own account, close by summarising it back, and evaluate afterwards. Callers who listen are more likely to book meetings that turn into clients.',
    tryit='Think of a time you said yes just to end an uncomfortable conversation. What pressure did it? Write two lines on what would have let you say no. Self-reflection only.',
    room='Pressure produces words, not truth. Rapport produces accounts you can check.',
    deeper=[('The Telegraph: the Senate interrogation report in 60 seconds', 'https://www.youtube.com/watch?v=XzLgzRIUhHQ', 'A one-minute summary'),
            ('Alison et al. 2013: rapport with terrorist suspects', 'https://doi.org/10.1037/a0034564', 'What works in real interviews')],
    nextq='Coercion fails as a truth machine but works as a control machine. One man built a church on confession, files and fear. Who was L. Ron Hubbard, and did his church really spy on the US government? Stop 8.5.',
    checks=[dict(q='What was the Senate Intelligence Committee’s first finding about the CIA’s techniques?',
                 o=['They were not an effective means of acquiring intelligence',
                    'They worked, but only on the most senior detainees',
                    'They were effective but too expensive to continue'], a=0,
                 w='Several detainees fabricated information under pressure. The CIA disputed the report; the law changed anyway.'),
            dict(q='Which of these is a known risk factor for false confessions?',
                 o=['Lying to the suspect about the evidence',
                    'Recording the whole interrogation on video',
                    'Letting the suspect speak to a lawyer first'], a=0,
                 w='Kassin’s 2010 review lists false evidence, youth and long sessions, and calls for recording every interrogation.'),
            dict(q='What does the PEACE model aim to get from a suspect?',
                 o=['A full account that can be checked',
                    'A confession as quickly as possible',
                    'A signed statement before a lawyer arrives'], a=0,
                 w='Adopted in 1992 after confessions in famous cases collapsed. Information first, confession optional.')],
)

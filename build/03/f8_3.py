from svg import box, t, arrow, line, svg

STEPS = [('1950 TO 1951', 'BLUEBIRD, then', 'ARTICHOKE'), ('1953', 'MKULTRA begins;', 'Frank Olson dies'),
         ('1954 TO 1963', 'secret dosing in', 'two safehouses'), ('1957', 'Montreal patients', 'as Subproject 68'),
         ('1973', 'Helms orders the', 'files destroyed'), ('1977', 'misfiled records', 'reach the Senate')]
FIG = svg(1180, 370, 'A timeline of the CIA’s behaviour-control programmes from BLUEBIRD to the 1977 Senate hearing, and what they found',
          t(590, 32, 'THE HUNT FOR MIND CONTROL, 1950 TO 1977', 's-t') +
          ''.join(box(20 + i * 193, 56, 170, 116, 's-box-a' if i in (1, 4) else 's-card', 12) + t(105 + i * 193, 92, a, 's-t-b') +
                  t(105 + i * 193, 122, b, 's-t-sm') + t(105 + i * 193, 146, c, 's-t-sm') for i, (a, b, c) in enumerate(STEPS)) +
          ''.join(arrow(192 + i * 193, 114, 211 + i * 193, 114) for i in range(5)) +
          box(140, 204, 400, 90, 's-box-j', 12) + t(340, 240, 'WHAT IT WAS AFTER', 's-t-b') + t(340, 270, 'a reliable way to control a mind', 's-t-sm') +
          arrow(548, 249, 632, 249) +
          box(640, 204, 400, 90, 's-box-a', 12) + t(840, 240, 'WHAT IT FOUND', 's-t-b') + t(840, 270, 'no switch, but real victims', 's-t-sm') +
          t(590, 340, '149 subprojects, 80 institutions, at least one death. Most of the files were destroyed.', 's-t-sm'))

STOP = dict(
    id='8.3', day=50, title='MKUltra and the hunt for mind control',
    q='Through the 1950s and 1960s the CIA drugged, hypnotised and isolated people, some of them without their knowledge, looking for a way to control the human mind. What did it find?',
    why='This is the stop where the conspiracy theories begin, so the documented history has to be exactly right. MKUltra was real. The CIA paid for experiments with drugs, hypnosis and sensory deprivation at universities, hospitals and prisons, some on people who never consented, and at least one man died. Then the agency destroyed most of the files. Real abuse plus missing records is the reason MKUltra powers so much conspiracy fiction, and the reason a careful writer separates what is proven from what is guessed.',
    case=dict(k='The case', name='Project MKULTRA (from 1953)', role='The CIA’s secret programme of behaviour-control research',
              facts=[('Before it', 'BLUEBIRD (from about 1950), renamed ARTICHOKE in 1951'),
                     ('Its size', '149 subprojects at 80 institutions, 44 of them colleges'),
                     ('The death', 'Frank Olson, given LSD without his knowledge, died in 1953'),
                     ('The cover-up', 'Director Richard Helms ordered the files destroyed in 1973')],
              stamp=('hold', 'Holds: real, abusive and a failure')),
    cold=dict(q='The CIA destroyed most of the MKUltra files in 1973. So how did investigators find out what the programme did?',
              a='By accident. In 1973 CIA Director Richard Helms ordered the MKUltra files destroyed. But in 1977 a Freedom of Information search turned up a set of financial records that had been filed in the wrong place. They named names: 149 subprojects, 185 non-government researchers and assistants, and 80 institutions, including 44 colleges and universities, 12 hospitals and three prisons. The Senate held a hearing on 3 August 1977. Much of what we know about MKUltra comes from that misfiling, which is also why so much will never be known.'),
    video=dict(id='NUW-frxo2X4', title='CIA Mind Control | CIA Secret Experiments', who='National Geographic',
               watch=['Which experiments the film says were done on people who did not know',
                      'What the CIA hoped to achieve, and what it actually got',
                      'Where the film separates documented facts from speculation']),
    story=['The hunt began in the panic of stop 8.2. If the communists could brainwash prisoners, the CIA reasoned, America needed the same power, and a defence against it. From about 1950 a project called BLUEBIRD tested drugs and hypnosis on interrogation subjects; in August 1951 it was renamed ARTICHOKE. In April 1953 the agency approved an umbrella project called MKULTRA, run for most of its life by a chemist, Sidney Gottlieb. Its money often flowed through front organisations, so many of the scientists it paid did not know the CIA was behind their grants.',
           'The subprojects covered LSD and other drugs, hypnosis, sensory deprivation and interrogation. Some subjects were volunteers. Others were not. In Operation Midnight Climax, which ran from 1954 to 1963, people taken to CIA-run apartments in San Francisco and New York were given drugs without their knowledge and watched through a two-way mirror. In November 1953 CIA employees secretly gave LSD to Frank Olson, an Army biochemist; about a week later he fell to his death from a tenth-floor hotel window in New York. In 1976 President Ford said the drugging appeared to have been “a proximate cause of his death”, and Congress paid his family $750,000.',
           'Some of the worst harm was done to psychiatric patients. At McGill University’s Allan Memorial Institute in Montreal, the psychiatrist Ewen Cameron tried to “depattern” patients with intensive electroshock, drug-induced sleep lasting days, sensory isolation and “psychic driving”, recorded messages played to them for hours. In 1957 the CIA, through a front called the Society for the Investigation of Human Ecology, funded his work as Subproject 68. Former patients sued. The CIA settled with nine Canadians for about $750,000 in 1988, Canada later paid former patients compensation without admitting legal responsibility, and in July 2025 a Quebec court authorised a class action against the Canadian government, McGill University and the Royal Victoria Hospital.',
           'Then came the cover-up and the reckoning. In 1973 Helms ordered the files destroyed. The Rockefeller Commission and the Church Committee exposed the programme in 1975, and the misfiled records surfaced in 1977. So what did two decades of secret research produce? Stephen Kinzer’s 2019 biography of Gottlieb, Poisoner in Chief, calls it a failure, and a scholarly review of the evidence concludes the programme never developed significant new chemical or behavioural methods of mind control. The CIA hunted for a switch in the human mind and found none. What it showed instead is how easily respected institutions will harm people when the work is secret and the subjects are powerless.',
           'For a writer, MKUltra is a gift and a trap. It gave screen fiction its favourite secret laboratory: Netflix’s own recap of Stranger Things says Dr Brenner “worked for years for the CIA on Project MKUltra”. Errol Morris’s Wormwood (2017) shows how to do it honestly: six chapters about Eric Olson’s decades-long search for the truth about his father, careful about what is known and what is suspected. The trap is the one that catches every conspiracy story: because some of it was real and the files were burned, anything can be claimed. Stop 8.6 tests one of the biggest claims.'],
    fig=(FIG, 'Two decades of searching, a destroyed archive and a misfiled box. The programme found no mind-control switch, and left real victims.'),
    specs=[('Subproject', 'One funded study under the MKULTRA umbrella. The surviving records list 149.'),
           ('Unwitting subject', 'A person tested without knowing it. MKUltra’s defining abuse.'),
           ('Informed consent', 'Agreeing to research after being told what it involves. The rule MKUltra broke, and a reason ethics boards exist.')],
    tags=[('hold', '“MKUltra drugged people without their consent.”', 'The 1977 Senate hearing documented LSD given to “unwitting subjects in social situations”.', ('Senate hearing on MKULTRA, 3 August 1977', 'https://www.intelligence.senate.gov/wp-content/uploads/2024/08/sites-default-files-hearings-95mkultra.pdf')),
          ('myth', '“MKUltra perfected mind control.”', 'A scholarly review finds it never developed significant new methods of mind control.', ('Journal of Cold War Studies review', 'https://doi.org/10.1162/jcws_r_00932')),
          ('hold', '“The drugging played a part in Frank Olson’s death.”', 'President Ford said it appeared to be “a proximate cause of his death”.', ('Ford’s statement on the Olson relief bill, 1976', 'https://www.presidency.ucsb.edu/documents/statement-signing-the-bill-providing-for-the-relief-the-survivors-dr-frank-r-olson'))],
    distil=[('Senate hearing: Project MKULTRA, 1977', 'https://www.intelligence.senate.gov/wp-content/uploads/2024/08/sites-default-files-hearings-95mkultra.pdf', 'The surviving record'),
            ('National Security Archive: CIA behaviour-control experiments', 'https://nsarchive.gwu.edu/briefing-book/dnsa-intelligence/2024-12-23/cia-behavior-control-experiments-focus-new-scholarly-collection', 'From BLUEBIRD to MKULTRA'),
            ('Orlikow v. United States (1988): the Montreal case', 'https://law.justia.com/cases/federal/district-courts/FSupp/682/77/1583126/', 'Cameron’s methods, in a court record')],
    writer=dict(notes=['Ground the conspiracy in a person. Wormwood works because it is about a son and a father, not a programme. Give the audience one victim to care about before you show them the machine.',
                       'Mark the line between known and suspected inside the story. A character who says “this part is documented, this part I believe” is more credible, and more haunting, than one who knows everything.'],
                drill='Write a one-page fictional scene in which a grown child finds one document about a parent’s death in a secret programme. Let them read it aloud. End on the one line that is blacked out.'),
    biz='MKUltra is a big part of why research ethics exist, and the lesson reaches MTRX™ directly. An AI receptionist, a voice note-taker or a WhatsApp bot collects people’s words. Tell them, get consent, and let them opt out. India’s Digital Personal Data Protection Act 2023 is built on consent, and so is trust. Never record or analyse a patient’s or customer’s voice or messages without telling them, however small the feature.',
    tryit='Pick one app you use every day. Find what its privacy page says about recording, data or experiments. Write two lines: what you agreed to, and what surprised you.',
    room='The CIA searched for a mind-control switch and found none. The harm was real anyway.',
    deeper=[('The Fifth Estate (CBC, 1980): MK Ultra in Canada', 'https://www.youtube.com/watch?v=990k-5Jm5aA', 'The Montreal patients'),
            ('Errol Morris: Wormwood (2017)', 'https://errolmorris.com/film/wormwood.html', 'One family’s search for the truth')],
    nextq='The CIA’s own manual said coercion produces false confessions. Did anyone listen? Follow KUBARK into Honduras, the war on terror and ordinary police stations. Stop 8.4.',
    checks=[dict(q='Why do we know as much as we do about MKUltra?',
                 o=['Misfiled financial records survived the order to destroy the files',
                    'The CIA published every file as soon as the programme ended',
                    'Sidney Gottlieb wrote a full public confession before he died'], a=0,
                 w='Helms ordered the files destroyed in 1973. A 1977 search found records filed in the wrong place.'),
            dict(q='What happened to Frank Olson in 1953?',
                 o=['CIA staff secretly gave him LSD, and about a week later he died',
                    'He ran the MKUltra programme for the CIA until he retired',
                    'He exposed MKUltra to newspapers and then fled to Canada'], a=0,
                 w='President Ford later called the drugging an apparent proximate cause of his death. Congress paid his family.'),
            dict(q='What did MKUltra’s search for mind control produce?',
                 o=['No reliable method, but real victims and lawsuits',
                    'A working technique that the CIA still keeps secret',
                    'The hypnotic triggers shown in The Manchurian Candidate'], a=0,
                 w='Real abuse, no switch. That gap is where the conspiracy theories grow.')],
)

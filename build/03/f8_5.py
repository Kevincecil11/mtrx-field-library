from svg import box, t, arrow, line, svg

EVENTS = [('1950', 'Dianetics,', 'a self-help bestseller'), ('1955', 'a fake Soviet', '“Brain-Washing” manual'),
          ('1963', 'the FDA seizes', 'E-meters'), ('1967', 'Sea Org and the', '“Fair Game” letter'),
          ('1973 TO 1977', 'Snow White spies', 'inside government'), ('1984', 'two courts condemn', 'Hubbard’s honesty'),
          ('1993', 'US tax exemption', 'for the church'), ('1995', 'Lisa McPherson dies', 'in church care')]
def cell(i, a, b, c):
    x, y = 20 + (i % 4) * 290, 56 + (i // 4) * 116
    return box(x, y, 270, 100, 's-box-a' if i in (3, 4) else 's-card', 12) + t(x + 135, y + 34, a, 's-t-b') + t(x + 135, y + 62, b, 's-t-sm') + t(x + 135, y + 84, c, 's-t-sm')
FIG = svg(1180, 410, 'A timeline of L. Ron Hubbard and Scientology from 1950 to 1995, and the CIA story sorted into true and false',
          t(590, 32, 'L. RON HUBBARD AND SCIENTOLOGY: THE RECORD', 's-t') +
          ''.join(cell(i, a, b, c) for i, (a, b, c) in enumerate(EVENTS)) +
          box(20, 292, 1140, 96, 's-box-j', 12) + t(590, 324, 'THE CIA STORY, SORTED', 's-t-b') +
          t(590, 350, 'False: Hubbard taught the CIA its methods, or worked as its agent.', 's-t-sm') +
          t(590, 374, 'True: his church spied on the government, and Scientologists ran CIA-funded psychic tests.', 's-t-sm'))

STOP = dict(
    id='8.5', day=52, title='Case file: L. Ron Hubbard and Scientology',
    q='A pulp science fiction writer founded a religion, and a British judge later called him “a charlatan and worse”. Who was L. Ron Hubbard, what did his church actually do, and is any of the CIA story true?',
    why='The CIA story you have heard about Hubbard is wrong, and the true one is stranger. Hubbard did not teach the CIA anything, and the Alice in Wonderland technique is the CIA’s own (stop 8.1). But his organisation really did run a covert operation that planted spies in US government agencies, and the CIA really did fund psychic research in which Scientologists played central roles. This case file uses the whole course: a leader’s story about himself, a system of confession and records, and a policy for punishing the people who leave.',
    case=dict(k='The case', name='L. Ron Hubbard (1911 to 1986)', role='Pulp writer, founder of Dianetics and Scientology',
              facts=[('Dianetics', 'Published 9 May 1950; a bestseller'),
                     ('The church', 'First Scientology churches incorporated in 1953 and 1954'),
                     ('Snow White', 'His wife and ten others indicted in 1978 for crimes against the government'),
                     ('The courts, 1984', 'A US judge: “virtually a pathological liar”; a UK judge: “a charlatan and worse”')],
              stamp=('anti', 'Anti-model: confession as control')),
    cold=dict(q='In the 1970s Scientology’s Guardian’s Office ran something called Operation Snow White. What do you think it did?',
              a='It planted spies inside the US government. Between 1973 and 1977 church operatives infiltrated agencies including the Internal Revenue Service and the Justice Department and stole documents, and the judge found a conspiracy that included bugging at least one IRS meeting. On 8 July 1977 the FBI raided church offices in Washington and Los Angeles. Eleven people were indicted in 1978, including Hubbard’s wife, Mary Sue, who was sentenced to five years in prison; Hubbard himself was named an unindicted co-conspirator. So there is a real Scientology spy story. It just runs in the opposite direction from the rumour.'),
    video=dict(id='ixgd38EZIR0', title='Going Clear: Scientology and the Prison of Belief, official trailer', who='Madman Films',
               watch=['Which former members speak, and what roles they held',
                      'How the trailer frames auditing and the Sea Org',
                      'One claim you would want to check against a court record']),
    story=['Lafayette Ronald Hubbard was born in Tilden, Nebraska, in 1911 and made his name in the 1930s and 1940s as a prolific pulp writer of science fiction, fantasy and adventure. He served in the US Navy in the Second World War. His later accounts of combat wounds and many medals do not match his Navy records: Lawrence Wright’s fact-checkers found no evidence he was wounded in battle. In May 1950 he published Dianetics: The Modern Science of Mental Health, a self-help therapy promising to clear painful memories he called engrams. It became a bestseller, and by 1954 the first Churches of Scientology had been incorporated.',
           'Scientology’s central practice is auditing: a trained auditor asks structured questions while the subject holds the electrodes of an E-meter, a skin galvanometer whose needle is read as a guide to spiritual distress. Lawrence Wright compared it to seeing a therapist with a lie detector between you. Auditing is confession, and confession leaves a record. In 1963 the US Food and Drug Administration seized E-meters, and in 1971 a federal judge ruled they could be used only with a label saying they had no proven medical or scientific value. In 1967 Hubbard created the Sea Organization, whose members sign a symbolic billion-year contract, and later its Rehabilitation Project Force, which the sociologist Stephen Kent describes as hard labour, forced confessions and intense study in a prison-like setting. The scholar J. Gordon Melton describes it as a programme for reforming members who committed serious offences.',
           'Then the punishments. A 1967 policy letter said a person declared an enemy “may be deprived of property or injured by any means by any Scientologist without any discipline of the Scientologist. May be tricked, sued or lied to or destroyed.” This was Fair Game. A 1968 letter ended the practice of declaring people fair game because it caused bad public relations, but in 1989 a California appeals court upheld a former member’s case, finding substantial evidence that auditing and other practices were conducted in a coercive environment, and that a fair game campaign followed him after he left. In 1984 two courts went further. In Los Angeles, Judge Paul Breckenridge called Hubbard “virtually a pathological liar when it comes to his history, background, and achievements”. In London, Mr Justice Latey called him “a charlatan and worse”.',
           'Now the intelligence links, sorted. True: from 1973 to 1977 the Guardian’s Office ran Operation Snow White, which ended in the 1977 FBI raids and prison for Mary Sue Hubbard. True: from 1972 the CIA funded “remote viewing” experiments at the Stanford Research Institute led by the physicists Harold Puthoff and Russell Targ, and two central figures, Puthoff and the psychic Ingo Swann, were Scientologists at the time. In 1995 an outside evaluation found remote viewing had not been shown useful for intelligence, and the programme ended. And Hubbard had a brainwashing text of his own: in 1955 his organisation published Brain-Washing, presented as a secret Soviet manual on “psychopolitics”, which the sociologist Stephen Kent concludes is fraudulent, with “all indicators” pointing to Hubbard as its author. False, as far as any evidence shows: that Hubbard taught the CIA, invented its interrogation methods or worked as its agent.',
           'Lisa McPherson’s death shows why the details matter. In December 1995 she died after 17 days in the care of church staff in Clearwater, Florida; criminal charges were dropped, and a civil suit was settled in 2004. Two years before her death, in 1993, the US tax authority had recognised Scientology as tax-exempt, and the church points to that as proof it is a bona fide religion. Both are facts, and holding both at once is the skill of this course. For a writer, Paul Thomas Anderson’s The Master (2012) shows the method from inside: Lancaster Dodd’s rapid-fire processing of Freddie Quell is a confession and a seduction at once. Wright’s book Going Clear (2013) and Alex Gibney’s 2015 film show the cost; the church called the film bigoted and full of falsehoods.'],
    fig=(FIG, 'Forty-five years in eight dates, and the CIA story sorted. The real links are stranger than the rumour.'),
    specs=[('Auditing', 'Scientology’s counselling practice: structured questions, often with an E-meter. It is also confession on the record.'),
           ('Fair Game', 'Hubbard’s 1967 policy for treating declared enemies. A 1968 letter cancelled the label.'),
           ('Suppressive person', 'Scientology’s label for someone it treats as an enemy, often a critic or a former member.')],
    tags=[('myth', '“Hubbard taught the CIA its interrogation techniques.”', 'No evidence. The Alice in Wonderland method is in the CIA’s own 1963 manual.', ('National Security Archive: KUBARK', 'https://nsarchive2.gwu.edu/NSAEBB/NSAEBB122/')),
          ('hold', '“Scientology spied on the US government.”', 'Operation Snow White: FBI raids in 1977, eleven indicted in 1978, Mary Sue Hubbard jailed.', ('United States v. Hubbard, 474 F. Supp. 64 (1979)', 'https://law.justia.com/cases/federal/district-courts/FSupp/474/64/1964219/')),
          ('hold', '“Scientologists ran CIA-funded psychic research.”', 'Puthoff and Swann, central to the remote viewing work from 1972, were Scientologists at the time.', ('Society for Psychical Research: review of Learn Remote Viewing', 'https://www.spr.ac.uk/node/19285'))],
    distil=[('Lawrence Wright: Going Clear (2013)', 'https://www.lawrencewright.com/books/going-clear-scientology-hollywood-the-prison-of-belief', 'More than two hundred interviews'),
            ('Wollersheim v. Church of Scientology (1989)', 'https://law.justia.com/cases/california/court-of-appeal/3d/212/872.html', 'A court on coercion and fair game'),
            ('Stephen Kent: brainwashing in the Rehabilitation Project Force', 'https://skent.ualberta.ca/contributions/scientology/brainwashing-in-scientologys-rehabilitation-project-force-rpf/', 'A sociologist’s study, and the fake 1955 manual')],
    writer=dict(notes=['Give the leader a biography he rewrote. Hubbard’s invented war wounds are a gift to a writer: the man who sells transformation has transformed his own past first. Let the audience find the real record halfway through.',
                       'Write confession as a hook. In The Master, processing feels like intimacy. Only later does the audience realise that every secret Freddie gives away is now leverage.'],
                drill='Write a one-page fictional scene in which a recruit confesses something private during a friendly session. Then write a half-page scene months later in which that confession is quietly used against them. Fiction only.'),
    biz='Two lessons for MTRX™. First, records are power: whatever clients tell you on calls, their finances, their staff problems, their patients’ data, must be protected and never used as leverage. Second, watch how any group or partner treats people who leave. A business network, coaching programme or agency partner that punishes exits, or calls former members traitors, is showing you its real contract.',
    tryit='Think of a group you have left: a job, a club, a class. How did the group talk about people who left? Write two lines. Did it make leaving easier or harder? Self-reflection only.',
    room='Watch how a group treats confession and exit. That tells you what it is.',
    deeper=[('The New Yorker: Hubbard leaves the Navy', 'https://www.newyorker.com/news/news-desk/primary-sources-l-ron-hubbard-leaves-the-navy', 'The war story, checked'),
            ('UPI, 1984: the Latey judgment', 'https://www.upi.com/Archives/1984/07/23/Judge-calls-Church-of-Scientology-sinister/7626459403200/', 'A British judge’s verdict'),
            ('Breckenridge decision, 1984', 'https://www.gerryarmstrong.org/50k/legal/a1/BreckenridgeDecision.pdf', 'The Los Angeles ruling in full')],
    nextq='One prisoner studied Scientology and Dale Carnegie in a federal penitentiary, walked out in 1967 and built a family that killed for him. How did Charles Manson do it? Stop 8.6.',
    checks=[dict(q='What was Operation Snow White?',
                 o=['A church operation that planted spies in US government agencies',
                    'A CIA mission to infiltrate the Church of Scientology in the 1970s',
                    'A Scientology course for training new auditors in confession'], a=0,
                 w='It ended in FBI raids in 1977 and convictions, including Hubbard’s wife. The spying ran toward the government.'),
            dict(q='What is true about Scientology and the CIA’s psychic research?',
                 o=['Two key researchers were Scientologists at the time',
                    'Hubbard personally ran the CIA’s psychic programme',
                    'The CIA used auditing to question its own agents'], a=0,
                 w='Puthoff and Swann were Scientologists. The programme ended in 1995 after an evaluation found no intelligence value.'),
            dict(q='What did Hubbard’s 1967 “Fair Game” letter say about declared enemies?',
                 o=['They could be tricked, sued, lied to or destroyed',
                    'They should be forgiven and invited back in',
                    'They must be reported to the police at once'], a=0,
                 w='A 1968 letter cancelled the label. In 1989 a court still found a fair game campaign against a former member.')],
)

from svg import box, t, arrow, line, svg

SECS = [('I TO III', 'purpose, terms', 'and the law'), ('IV AND V', 'the questioner', 'and the subject'),
        ('VI AND VII', 'screening', 'and planning'), ('VIII', 'non-coercive', 'pp. 52 to 81'),
        ('IX', 'coercive', 'pp. 82 to 104'), ('X TO XII', 'checklist, books', 'and index')]
FLOW = [('PRESSURE', 'isolation, fear, fatigue'), ('REGRESSION', 'adult defences fall away'),
        ('DEPENDENCE', 'only the questioner left'), ('COMPLIANCE', 'or a false confession')]
def cls(i):
    return 's-box-j' if i == 3 else ('s-box-a' if i == 4 else 's-card')
FIG = svg(1180, 380, 'The twelve sections of the 1963 KUBARK manual, and the theory of coercion in its section IX',
          t(590, 32, 'KUBARK, JULY 1963: WHAT IS INSIDE 128 PAGES', 's-t') +
          ''.join(box(20 + i * 193, 56, 170, 116, cls(i), 12) + t(105 + i * 193, 92, a, 's-t-b') +
                  t(105 + i * 193, 122, b, 's-t-sm') + t(105 + i * 193, 146, c, 's-t-sm') for i, (a, b, c) in enumerate(SECS)) +
          t(590, 206, 'THE THEORY IN SECTION IX', 's-t-b') +
          ''.join(box(20 + i * 290, 222, 250, 86, 's-box-a' if i == 3 else 's-card', 12) + t(145 + i * 290, 256, a, 's-t-b') +
                  t(145 + i * 290, 284, b, 's-t-sm') for i, (a, b) in enumerate(FLOW)) +
          ''.join(arrow(272 + i * 290, 265, 306 + i * 290, 265) for i in range(3)) +
          t(590, 352, 'The manual’s own warning: pain is “quite likely to produce false confessions”.', 's-t-sm'))

STOP = dict(
    id='8.1', day=48, title='KUBARK: inside the CIA’s 1963 manual',
    q='In 1963 the CIA wrote a 128-page manual on breaking the resistance of a prisoner. What did it actually say, and why does it matter to anyone who studies cults and cons?',
    why='File 8 is a bonus deep dive into the room where influence becomes force. It starts with the most famous document in that history, the CIA’s KUBARK manual, because it states plainly what cult leaders and abusers never write down: the theory of breaking a person. Reading it as history, not as instruction, shows you the mechanism, the manual’s own admission that it fails, and the line it draws from Cold War prisons to the cults of File 1.',
    case=dict(k='The document', name='KUBARK Counterintelligence Interrogation (July 1963)', role='The CIA’s manual on questioning “resistant sources”',
              facts=[('The name', 'KUBARK: a CIA codename for the CIA itself'),
                     ('The size', '128 pages in twelve sections'),
                     ('Made public', 'Baltimore Sun request, January 1997; fuller copy 2014'),
                     ('Its own warning', 'Pain is “quite likely to produce false confessions”')],
              stamp=('anti', 'Anti-model: coercion, by the book')),
    cold=dict(q='The manual has a section called the “Alice in Wonderland” technique. Before reading on, guess: what was it meant to do to a prisoner?',
              a='Confuse him. The manual calls it a “confusion technique” whose aim is “to confound the expectations and conditioned reactions of the interrogatee”. A prisoner clings to “a world of continuity and logic, a predictable world” to hold on to his identity, so the method sets out “not only to obliterate the familiar but to replace it with the weird”. When nothing makes sense, the person who controls the room becomes the only fixed point. Hold that idea: it explains a lot about cults, abusers and con artists too.'),
    video=dict(id='bWl8FXhdEio', title='Dark Persuasion: The History of Brainwashing from Pavlov to Social Media', who='University of California Television (UCTV)',
               watch=['Where the speaker places the CIA in the history of brainwashing',
                      'Which ideas came from Pavlov’s labs and Korean War prisons',
                      'How the speaker separates real coercion from the myth of mind control']),
    story=['In July 1963 the CIA finished a 128-page manual called KUBARK Counterintelligence Interrogation. KUBARK was not a technique; it was the agency’s codename for itself. The manual trained officers to question “resistant sources”, people suspected of working for hostile intelligence services, and it claimed to rest “largely upon the published results of extensive research”, the same Cold War research into prisoners, isolation and stress that you will meet in stops 8.2 and 8.3. It stayed secret for more than thirty years, until the Baltimore Sun obtained it under the Freedom of Information Act and reported on it in January 1997. A less censored copy followed in February 2014.',
           'It reads like a textbook. It opens with definitions and legal cautions: KUBARK had “no independent legal authority to detain anyone against his will”, and duress was “especially likely to involve illegality and to entail damaging consequences for KUBARK”, so headquarters had to approve in advance any plan to inflict bodily harm. Then come chapters on the interrogator, the types of subject, screening and planning. Section VIII describes non-coercive questioning in four phases: the opening, the reconnaissance, the detailed questioning and the conclusion. Section IX, on “the coercive counterintelligence interrogation of resistant sources”, covers arrest, detention, sensory deprivation, threats and fear, debility, pain, hypnosis and drugs.',
           'Its central idea fits in one sentence: “All coercive techniques are designed to induce regression.” The theory is that isolation, fear and exhaustion strip away the defences an adult has built until the prisoner falls back on the person who controls his world, as the diagram shows. That is the mechanism Albert Biderman described in Chinese prison camps (stop 8.2) and the one stop 7.3 described in coercive relationships: make the controller the only source of food, light, time and meaning, and dependence follows.',
           'The technique people remember sits in the non-coercive section. The “Alice in Wonderland or confusion technique” attacks a person’s sense that the world makes sense, so the questioner becomes the only fixed point. It is not Hubbard’s technique, and he never taught it to the CIA; stop 8.5 sorts out the real links. You will meet its cousins in every high-control group: rules that change without warning, praise and punishment for the same act, a story that explains everything except your doubts. Harold Pinter put a confusion interrogation on stage in The Birthday Party (1958), five years before the manual was finished.',
           'The most useful lines in KUBARK are its admissions. It warns that “intense pain is quite likely to produce false confessions, concocted as a means of escaping from distress”, and that people under heavy pressure lose the ability to recall and communicate accurately along with the will to resist. A method that breaks the will also breaks the memory. Stop 8.4 follows what happened when later interrogators ignored that warning. For a writer, the manual is a key to the great interrogation scenes, from O’Brien breaking Winston in Nineteen Eighty-Four to the Stasi lecture that opens The Lives of Others (2006). The power is in owning the world around the prisoner, not in the questions.'],
    fig=(FIG, 'What the 128 pages contain, and the theory at their centre: pressure, regression, dependence. The manual itself warns where it ends.'),
    specs=[('Resistant source', 'The manual’s term for a person who will not cooperate with questioning.'),
           ('Regression', 'In KUBARK’s theory, the falling away of adult defences under pressure, leaving a person dependent on the captor.'),
           ('Confusion technique', 'KUBARK’s “Alice in Wonderland” method: disorienting a person until the questioner seems the only fixed point.')],
    tags=[('myth', '“KUBARK is the name of a torture technique.”', 'KUBARK was a CIA codename for the agency itself. The manual is named after its owner.', ('National Security Archive: Prisoner Abuse, Patterns from the Past', 'https://nsarchive2.gwu.edu/NSAEBB/NSAEBB122/')),
          ('myth', '“The Alice in Wonderland technique came from L. Ron Hubbard.”', 'It is in the CIA’s own 1963 manual. Hubbard never taught the CIA; stop 8.5 has the real links.', ('KUBARK full text, Wikisource', 'https://en.wikisource.org/wiki/KUBARK_Counterintelligence_Interrogation')),
          ('hold', '“The manual admitted coercion produces bad information.”', 'It warns pain is “quite likely to produce false confessions” that waste time to disprove.', ('KUBARK, coercive section, National Security Archive', 'https://nsarchive2.gwu.edu/NSAEBB/NSAEBB27/docs/doc01.pdf'))],
    distil=[('National Security Archive: the KUBARK and 1983 manuals', 'https://nsarchive2.gwu.edu/NSAEBB/NSAEBB122/', 'The documents, with context'),
            ('KUBARK Counterintelligence Interrogation, full text', 'https://en.wikisource.org/wiki/KUBARK_Counterintelligence_Interrogation', 'Read the manual itself'),
            ('Baltimore Sun, 27 January 1997: the manuals made public', 'https://www.baltimoresun.com/1997/01/27/torture-was-taught-by-cia-declassified-manual-details-the-methods-used-in-honduras-agency-denials-refuted/', 'How it came out')],
    writer=dict(notes=['Control the world, not the dialogue. The strongest interrogation scenes are about who owns the clock, the light, the food and the facts. Let the questions be ordinary and let the room do the work.',
                       'Disorientation is a scene tool, but give the audience one anchor the prisoner can hold: a memory, a name, a fact. The scene becomes a fight over that anchor.'],
                drill='Write a one-page fictional scene in which a character is questioned by someone who keeps changing the rules of the conversation. Give the character one anchor, a name or a memory, and end on the moment they decide whether to let go of it.'),
    biz='Confusion is also a negotiation tactic. A client who keeps changing the brief, the deadline and the decision-maker puts you in a small Wonderland where agreeing feels like the only way out. The MTRX™ anchor is paper: a written scope, a change-request rule, one named decision-maker and a summary email after every call. When the world keeps shifting, the written record is your fixed point.',
    tryit='Recall a conversation that left you more confused than when it started, at work, with a seller or in a group. Write down what kept changing: facts, rules or tone. What would have been your anchor? Self-reflection only.',
    room='Coercion works by owning the world around a person. The defence is an anchor outside the room.',
    deeper=[('Terrifying laughter: Pinter’s The Birthday Party and the CIA’s Alice in Wonderland', 'https://www.tandfonline.com/doi/full/10.1080/0950236X.2021.1971753', 'A play that staged the method in 1958'),
            ('New York Times, 1997: the spy agency’s many mean ways', 'https://www.nytimes.com/1997/02/09/weekinreview/the-spy-agency-s-many-mean-ways-to-loosen-cold-war-tongues.html', 'How the manual was first read')],
    nextq='KUBARK says it rests on “extensive research”. Whose research? It starts with American prisoners in Korea, a newspaper word and one Air Force researcher’s chart. Stop 8.2.',
    checks=[dict(q='What does the word KUBARK actually mean?',
                 o=['A CIA codename for the agency itself',
                    'A Russian word for a type of interrogation',
                    'The surname of the officer who wrote it'], a=0,
                 w='It is a cryptonym. The manual is named after its owner, not after a technique.'),
            dict(q='What is the aim of the manual’s “Alice in Wonderland” technique?',
                 o=['To confuse a prisoner until the questioner seems the only fixed point',
                    'To relax a prisoner by reading him stories from children’s books',
                    'To hypnotise a prisoner so he forgets what he was asked'], a=0,
                 w='The manual calls it a confusion technique, designed to replace the familiar with the weird.'),
            dict(q='What did KUBARK itself warn about intense pain?',
                 o=['It is quite likely to produce false confessions',
                    'It is the fastest route to accurate information',
                    'It has no effect on trained intelligence officers'], a=0,
                 w='The manual’s own words. False confessions then waste time while investigators prove them untrue.')],
)

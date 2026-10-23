from svg import box, t, arrow, line, svg

METHODS = [('ISOLATION', 'no one else to lean on'), ('MONOPOLISED ATTENTION', 'only the captor’s world'),
           ('EXHAUSTION', 'too tired to resist'), ('THREATS', 'fear of what comes next'),
           ('OCCASIONAL INDULGENCES', 'hope keeps you complying'), ('SHOWING OMNIPOTENCE', 'resisting feels futile'),
           ('DEGRADATION', 'reduced to bare survival'), ('TRIVIAL DEMANDS', 'obedience becomes habit')]
def cell(i, name, eff):
    x, y = 20 + (i % 2) * 580, 56 + (i // 2) * 78
    return box(x, y, 560, 66, 's-box-a' if i == 4 else 's-card', 12) + t(x + 280, y + 28, name, 's-t-b') + t(x + 280, y + 52, eff, 's-t-sm')
FIG = svg(1180, 440, 'Albert Biderman’s 1957 chart of coercion: eight pressures that produced compliance in prisoners of war',
          t(590, 32, 'BIDERMAN’S CHART: EIGHT PRESSURES THAT PRODUCE COMPLIANCE', 's-t') +
          ''.join(cell(i, n, e) for i, (n, e) in enumerate(METHODS)) +
          box(20, 370, 1140, 50, 's-box-j', 12) +
          t(590, 401, 'Built from Korean War prisoners in 1957. Used today to explain control at home and in groups.', 's-t-sm'))

STOP = dict(
    id='8.2', day=49, title='Brainwashing and Biderman’s chart of coercion',
    q='In 1952 an American colonel and 35 other captured airmen confessed to germ warfare that never happened. Were they brainwashed, and what does that word even mean?',
    why='Brainwashing is the most famous idea in this course and the most misunderstood. The word entered English in 1950, grew into a Cold War panic, and fed both the CIA programmes of stop 8.3 and the courtroom fights of stop 3.3. The researchers who studied the returning prisoners found something less magical and more useful: a short list of pressures that make people comply. That list, Albert Biderman’s chart of coercion, is now used by some domestic abuse and cult recovery educators. Learn it once and you will see it everywhere.',
    case=dict(k='The case', name='Albert Biderman’s chart of coercion (1957)', role='Eight pressures that made prisoners comply',
              facts=[('The study', 'US Air Force prisoners of the Korean War'),
                     ('The paper', 'Bulletin of the New York Academy of Medicine, 1957'),
                     ('What it found', 'Methods built “to induce compliance”'),
                     ('Its second life', 'Used in domestic abuse and cult recovery training')],
              stamp=('hold', 'Holds: pressure, not magic')),
    cold=dict(q='The US feared that its prisoners in Korea had been turned into communists. When researchers examined the men who came home, how much real conversion did they find?',
              a='Almost none. Edgar Schein, who began studying the returning prisoners in 1953, later wrote that the problem was not ideological conversion, “of which there was virtually none”, but collaboration: signed statements, propaganda broadcasts and, most famously, false germ warfare confessions. Twenty-one Americans did refuse to come home, and that fed the panic. But what the evidence showed was people saying what their captors demanded under pressure. Saying is not believing, and that distinction is the key to every brainwashing claim you will ever hear.'),
    video=dict(id='Q6Bd-urzZQI', title='Chinese treatment of prisoners of war, from Korea: The Unknown War (1988)', who='Thames TV',
               watch=['How the former prisoner describes the daily indoctrination sessions',
                      'What the captors expected those sessions to achieve',
                      'Which of Biderman’s eight pressures you can hear in his account']),
    story=['The word came first. In September 1950, in the first year of the Korean War, the American journalist Edward Hunter wrote in the Miami News about “brain-washing” in Communist China, adapting a Chinese phrase, xǐ nǎo, literally “wash the brain”. His 1951 book Brain-Washing in Red China spread the idea worldwide. Then came the shock. In 1952 Colonel Frank Schwable and 35 other captured US airmen publicly confessed to waging germ warfare. The confessions were false. After the 1953 armistice, 21 American soldiers and one Briton refused to go home. To many Americans there seemed only one explanation: the enemy could rewrite minds.',
           'The researchers who examined the returning prisoners told a quieter story. Edgar Schein found collaboration under pressure but “virtually none” of the feared conversion. Robert Jay Lifton interviewed Westerners and Chinese who had been through thought reform and in 1961 published the eight criteria you met in stop 1.3. In 1957 the psychologists Farber and Harlow and the psychiatrist West explained the prisoners’ behaviour as the product of debility, dependency and dread, “DDD”: a predictable result of normal human behaviour under coercive conditions, they argued, not proof of some unnatural process of brainwashing.',
           'Albert Biderman, an Air Force social scientist, studied the airmen who had made false confessions. In 1957 he condensed what their captors did into a chart of eight methods, designed, as he put it, “to induce compliance”: isolation, monopolisation of perception, induced debilitation and exhaustion, threats, occasional indulgences, demonstrating “omnipotence” and “omniscience”, degradation, and enforcing trivial demands. None of it needs drugs, hypnosis or a secret machine. Each method is simple. The power is in the combination, kept up over time, with no way out.',
           'Read the chart again with partner, recruit or employee in place of prisoner, and it still works, which is why some domestic abuse and cult recovery educators teach it. Isolation is the move from stop 1.4. Occasional indulgences are the warmth that keeps people hoping, the pattern of stop 7.3. Trivial demands, a rule about what to wear or when to speak, train obedience long before anything big is asked. Some people overstate the chart as proof that every cult follows one playbook. It is not that. It is a map of how pressure works, and a map is enough to recognise the territory.',
           'For a writer, the Korean War panic produced a classic. Richard Condon’s novel The Manchurian Candidate (1959) and John Frankenheimer’s 1962 film imagine a captured American soldier programmed to kill on a trigger. It is gripping fiction and bad science, and it shaped what the public believed for decades. The truer story is harder to write and more chilling: not a man with a switch in his head, but ordinary people who say what they must, and slowly lose track of what they believe. Write that one.'],
    fig=(FIG, 'Biderman’s eight pressures. None needs a drug or a machine; the force is in the combination, kept up over time.'),
    specs=[('Brainwashing', 'A 1950 newspaper word for forced conversion. Researchers found compliance under pressure, not rewired minds.'),
           ('Compliance', 'Doing or saying what is demanded. Not the same as believing it, which is why forced confessions mislead.'),
           ('DDD', 'Debility, dependency and dread: the 1957 explanation by Farber, Harlow and West for prisoner collaboration.')],
    tags=[('myth', '“Korean War prisoners were turned into communists.”', 'Schein found collaboration under pressure but “virtually none” of the feared conversion.', ('Schein: the Korean POW research, MIT', 'http://hdl.handle.net/1721.1/83028')),
          ('hold', '“Coercion works through simple, ordinary pressures.”', 'Biderman’s eight methods need no drugs or machines. Their force is in the combination.', ('Biderman 1957, Bulletin of the New York Academy of Medicine', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC1806204/')),
          ('part', '“Biderman’s chart proves all cults use one playbook.”', 'It is a map drawn from prisoners of war and adapted by some educators. Useful for spotting, not proof of sameness.', ('Strathclyde: Biderman’s chart in social work training', 'https://www.strath.ac.uk/media/1newwebsite/departmentsubject/socialwork/documents/eshe/Bidermanschartofcoercion.pdf'))],
    distil=[('Wellcome Collection: the history of brainwashing', 'https://wellcomecollection.org/stories/the-history-of-brainwashing', 'Where the word came from'),
            ('Biderman 1957: Communist attempts to elicit false confessions', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC1806204/', 'The original chart'),
            ('Farber, Harlow and West 1957: debility, dependency and dread', 'https://psycnet.apa.org/record/1959-00653-001', 'Brainwashing explained without magic')],
    writer=dict(notes=['Write compliance, not conversion. The most frightening captive is not a programmed killer but someone who says the words and slowly stops noticing the gap between what they say and what they believe.',
                       'Use the indulgence. A single kindness from the captor, a cigarette or a letter from home, can do more dramatic work than a beating, because it gives the prisoner something to lose.'],
                drill='Write a one-page fictional scene in which a captor offers a prisoner a small kindness after days of hardship. Show what the prisoner must say to keep it. Fiction only.'),
    biz='Biderman’s chart is a good test for toxic workplaces and clients too. Isolation (“do not talk to the other vendors”), exhaustion (calls at midnight), occasional indulgences (praise after weeks of blame) and trivial demands (rules that change by the day) are the same pressures in a smaller room. If a client relationship ticks four boxes, it is costing MTRX™ more than it pays. Write the boundary into the contract, or walk away.',
    tryit='Read the eight methods and think of a group, job or relationship you have seen up close. Which ones appeared, and in what order? Write three lines. Self-reflection only.',
    room='Brainwashing is a myth of magic. Coercion is a set of ordinary pressures, combined.',
    deeper=[('SMU Center for Presidential History: The Interrogation Rooms of the Korean War', 'https://www.youtube.com/watch?v=Hu48J5RF9yM', 'A historian on the war inside the camps'),
            ('Library of Congress: The Manchurian Candidate (1962)', 'https://www.loc.gov/item/fi64001044/', 'The film that fixed the myth')],
    nextq='If brainwashing was mostly a myth, why did the CIA spend the 1950s and 1960s trying to build it? Stop 8.3.',
    checks=[dict(q='What did Edgar Schein find when he studied American prisoners returning from Korea?',
                 o=['Collaboration under pressure, but virtually no real conversion',
                    'Thousands of soldiers had become committed communists',
                    'The prisoners had been hypnotised with secret drugs'], a=0,
                 w='Saying is not believing. The feared mass conversion did not happen.'),
            dict(q='Which of these is one of the eight methods in Biderman’s chart?',
                 o=['Occasional indulgences', 'Hypnotic trigger words', 'Electric shock machines'], a=0,
                 w='Small kindnesses after hardship give the prisoner something to lose. None of the eight needs a machine.'),
            dict(q='Why do some domestic abuse and cult recovery educators use Biderman’s chart?',
                 o=['The same pressures work on partners and recruits as on prisoners',
                    'It proves every abuser follows the same written manual',
                    'It was originally written to describe religious groups'], a=0,
                 w='Isolation, exhaustion, indulgences and trivial demands work in any closed world. It is a map, not proof.')],
)

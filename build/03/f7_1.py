from svg import box, t, arrow, line, svg

ROWS = [('RECIPROCITY', 'a small favour, then the ask', 'holds: a chocolate raised tips', 'a'),
        ('FOOT IN THE DOOR', 'a small yes, then a big yes', 'weak: nearly half of studies null', 'j'),
        ('DOOR IN THE FACE', 'a big no, then the real ask', 'small: r = .14 said yes, .08 did it', 'j'),
        ('SOCIAL PROOF', 'most guests reuse their towels', 'depends: no better in German hotels', 'j'),
        ('AUTHORITY', 'ordinary people obey an expert', 'strong: 70% went past 150 volts', 'a'),
        ('SCARCITY', 'rare things feel more valuable', 'demand cues work, deadlines less', 'j')]
def table():
    out = (box(20, 56, 260, 40, 's-box-j', 8) + t(150, 82, 'LEVER', 's-t-b') +
           box(300, 56, 420, 40, 's-box-j', 8) + t(510, 82, 'THE CLASSIC CLAIM', 's-t-b') +
           box(740, 56, 420, 40, 's-box-j', 8) + t(950, 82, 'AFTER RE-TESTING', 's-t-b'))
    for r, (lev, claim, verdict, c) in enumerate(ROWS):
        y = 108 + r * 50
        out += (box(20, y, 260, 42, 's-card', 8) + t(150, y + 27, lev, 's-t-b') +
                box(300, y, 420, 42, 's-card', 8) + t(510, y + 27, claim, 's-t-sm') +
                box(740, y, 420, 42, 's-box-a' if c == 'a' else 's-box-j', 8) + t(950, y + 27, verdict, 's-t-sm'))
    return out
FIG = svg(1180, 440, 'Six of Cialdini’s levers, their classic claims, and what re-testing found',
          t(590, 32, 'SIX LEVERS AFTER THE REPLICATION CRISIS', 's-t') + table() +
          t(590, 424, 'Real levers, mostly small effects. Cons work by stacking them and removing the time to think.', 's-t-sm'))

STOP = dict(
    id='7.1', day=42, title='Cialdini’s levers: which survived replication',
    q='Every sales course teaches Robert Cialdini’s principles of persuasion. When scientists re-ran the classic experiments, which ones still worked?',
    why='File 7 is the reveal: the tools behind every con in this course, put to the test. Influence (1984) gave the world a vocabulary for persuasion, and con artists, marketers and cult recruiters all pull the same levers. But psychology has spent the last fifteen years re-running its famous experiments, and some effects shrank. For a writer, knowing which levers are real makes manipulation scenes believable. For a business owner, it separates honest persuasion from snake oil.',
    case=dict(k='The case', name='Robert Cialdini, Influence (1984)', role='The book that named the levers of persuasion',
              facts=[('The six', 'Reciprocity, commitment and consistency, social proof, liking, authority, scarcity'),
                     ('The seventh', 'Unity, added in the 2021 expanded edition'),
                     ('The author', 'A social psychologist at Arizona State University'),
                     ('The re-test', 'Some effects held; several shrank or depend on context')],
              stamp=('part', 'Partly: real levers, smaller effects')),
    cold=dict(q='A hotel card says most guests reuse their towels. When German researchers tried that famous nudge, did it beat a plain environmental message?',
              a='No. In 2008 Goldstein, Cialdini and Griskevicius reported that cards saying most guests reused their towels beat a standard environmental appeal. In 2014 Bohner and Schlüter ran the test in two German hotels. Both messages raised reuse compared with no message at all, but the “most guests” card did no better than the standard one. A real effect can depend on the place, the wording and the audience. That is the honest answer for almost every lever in this stop.'),
    video=dict(id='cFdCzN7RYbw', title='Science Of Persuasion', who='Team Cialdini',
               watch=['Which levers the video demonstrates, and with what examples',
                      'How small changes in wording are claimed to change behaviour',
                      'One claim you would want to see replicated before using it']),
    story=['Robert Cialdini, a social psychologist at Arizona State University, published Influence in 1984. It named six principles that move people to say yes: reciprocity (we repay favours), commitment and consistency (we stick with what we have said), social proof (we copy others), liking (we agree with people we like), authority (we defer to experts) and scarcity (we want what is rare). In the 2021 expanded edition he added a seventh, unity: we say yes to people we see as one of us. Every con in this course pulls at least two of them.',
           'Then psychology hit its replication crisis, and the levers were re-tested. Foot-in-the-door, getting a small yes before the big ask, had already been reviewed in 1983 by Beaman and colleagues: across 120 experimental groups the effect was real but weak, and nearly half the studies found no effect or one in the wrong direction. Door-in-the-face, a big request first and then the smaller real one, survived a direct replication in 2020. But a 2025 review put its average effect at r = .14 for saying yes and only r = .08 for actually doing the thing.',
           'Social proof is real but local, as the towel studies show. Scarcity is subtler than the slogan: a 2023 review found that signs of high demand, like selling fast, raised buying, while limited-time and limited-quantity urgency did not on average. Authority is the strongest of the old findings: across Milgram’s obedience studies about 44 percent of people went to the maximum shock, and in a 2009 partial replication Jerry Burger found 70 percent kept going past 150 volts. Reciprocity holds too: in a 2002 study a small chocolate with the bill raised restaurant tips.',
           'So what does that mean in practice? These are nudges, not mind control. An average across a group says little about one person, and effects shrink when people notice the technique. That is exactly why cons stack the levers. A con artist does not rely on scarcity alone; he layers a favour, a crowd, a uniform and a deadline until the small effects add up, and then he takes away the time to think. The defence is the one from File 6: slow down and check outside the frame.',
           'For a writer, the honest version is more frightening. A villain who hypnotises people with one magic sentence is a cartoon. A villain who wins with five small, ordinary pressures, a gift, a nod from a respected guest, a sense of being on the inside, a deadline, is terrifying, because the audience recognises every one from their own life. Watch any pitch scene in Mad Men and count the levers.'],
    fig=(FIG, 'Six of Cialdini’s levers after re-testing: real, mostly small, and dependent on context.'),
    specs=[('Replication', 'Re-running an experiment to see if its result holds. A failed replication does not always mean the effect is zero.'),
           ('Effect size', 'How big an effect is. A correlation of r = .1 is small; it matters across crowds more than for one person.'),
           ('Foot-in-the-door', 'Getting a small yes first to make a bigger yes more likely.')],
    tags=[('part', '“Cialdini’s principles are proven laws of persuasion.”', 'They are real tendencies with mostly small, context-dependent effects.', ('Beaman et al. 1983 meta-analysis', 'https://doi.org/10.1177/0146167283092002')),
          ('myth', '“The towel-card nudge works everywhere.”', 'In two German hotels the “most guests” card did no better than a standard message.', ('Bohner and Schlüter 2014, PLOS ONE', 'https://doi.org/10.1371/journal.pone.0104086')),
          ('hold', '“Authority pressure is powerful.”', 'About 44% went to the maximum across Milgram’s conditions; Burger found 70% past 150 volts.', ('Meta-Milgram, PLOS ONE 2014', 'https://doi.org/10.1371/journal.pone.0093927'))],
    distil=[('Cialdini: the seven principles', 'https://cialdini.com/books/influence', 'The source, in his words'),
            ('Genschow et al. 2020: door-in-the-face replicated', 'https://pubmed.ncbi.nlm.nih.gov/33030935/', 'A lever that survived'),
            ('2023 meta-analysis of scarcity cues', 'https://doi.org/10.1002/mar.21816', 'Demand beats deadlines')],
    writer=dict(notes=['Stack, do not hypnotise. Give the manipulator five small, ordinary pressures in one scene: a favour, a crowd, a credential, a sense of belonging, a deadline. The audience should recognise each from their own life.',
                       'Let one lever fail. A con where every trick works is a fantasy. When the mark shrugs off the scarcity pitch, the con artist has to improvise, and improvisation reveals character.'],
                drill='Write a one-page fictional scene in which a recruiter uses three of Cialdini’s levers on a hesitant newcomer. Mark each lever in the margin. Then rewrite the last line so the newcomer notices one of them.'),
    biz='Use the levers that hold, honestly. Reciprocity: give a clinic a genuinely useful free website audit. Social proof: real results from named clients, with permission. Authority: show your own work, not borrowed badges. Scarcity: only when your calendar really is full. And drop the fake countdown timers. The evidence says urgency cues do little, and in India false urgency is a banned dark pattern, as stop 7.5 shows.',
    tryit='Open one sales page or Instagram ad you saw this week. List every lever it uses. Which of them would survive the evidence in this stop?',
    room='The levers are real but small. Cons work by stacking them and stealing your time to think.',
    deeper=[('APA Monitor: Burger’s Milgram replication, 2009', 'https://www.apa.org/monitor/2009/03/milgram', 'Would people still obey today?'),
            ('Feeley 2025: door-in-the-face reviewed', 'https://doi.org/10.1080/03637751.2025.2594987', 'How big the effect really is')],
    nextq='If the science of persuasion is this modest, why does a book of “laws” built on historical stories sell millions and get banned in prisons? Stop 7.2.',
    checks=[dict(q='What did Beaman and colleagues find when they reviewed foot-in-the-door studies in 1983?',
                 o=['The effect was real but weak, and nearly half the studies found none',
                    'It was the most powerful influence technique ever measured',
                    'It only worked when people were paid to take part'], a=0,
                 w='Across 120 experimental groups the effect was small and unreliable. Real, but no magic key.'),
            dict(q='Which kind of scarcity cue raised buying in a 2023 review?',
                 o=['Signs of high demand, such as selling fast',
                    'Countdown timers and offers that expire tonight',
                    'Limited-quantity labels on every single product'], a=0,
                 w='Demand cues worked; urgency cues did not on average. Fake countdowns are weak and can be illegal.'),
            dict(q='Why do con artists stack several levers at once?',
                 o=['Each effect is small, so they add them up and remove the time to think',
                    'A single lever is illegal unless it is combined with others',
                    'Stacking makes the con easier to explain to the police later'], a=0,
                 w='Single levers are nudges. Stacked, with time pressure, they become a trap.')],
)

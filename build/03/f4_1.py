from svg import box, t, arrow, line, svg

STEPS = [('Put-up', 'pick the mark'), ('Play', 'set the scene'), ('Rope', 'win trust'), ('Tale', 'the opportunity'),
         ('Convincer', 'a taste of proof'), ('Breakdown', 'a crisis, act now'), ('Send', 'go get the money'),
         ('Touch', 'the money moves'), ('Blow-off', 'crew vanishes'), ('Fix', 'cover the exit')]
def _cell(i, s):
    x = 20 + (i % 5) * 230; y = 60 + (i // 5) * 150
    cls = 's-box-a' if s[0] in ('Convincer', 'Breakdown') else 's-card'
    return box(x, y, 210, 104, cls, 12) + t(x + 105, y + 30, '%d' % (i + 1), 's-t-sm') + t(x + 105, y + 62, s[0], 's-t-b') + t(x + 105, y + 88, s[1], 's-t-sm')
FIG = svg(1180, 420, "Maurer's ten steps of the big con, with the two steps where a defence works best highlighted",
          t(590, 34, 'THE BIG CON, AS MAURER RECORDED IT (1940)', 's-t') +
          ''.join(_cell(i, s) for i, s in enumerate(STEPS)) +
          ''.join(arrow(230 + k * 230, 112, 248 + k * 230, 112) for k in range(4)) +
          ''.join(arrow(230 + k * 230, 262, 248 + k * 230, 262) for k in range(4)) +
          line(1130, 166, 1130, 186) + line(1130, 186, 125, 186) + arrow(125, 186, 125, 208) +
          t(590, 352, 'ROPER: steps 1 to 3, the friendly stranger. INSIDE MAN: steps 4 to 8, the expert.', 's-t-sm') +
          t(590, 388, 'Orange = where defence is cheapest: check the proof and refuse the deadline.', 's-t-sm'))

STOP = dict(
    id='4.1', day=24, title="Anatomy of a con: Maurer's big con, step by step",
    q='If a con artist is just a liar, why did the professionals of the 1920s need a crew, a rented room, rehearsals and ten named steps?',
    why="Every con film you love, from The Sting to Better Call Saul, runs on a structure that a linguist wrote down in 1940 after interviewing real grifters. Learn the steps once and you will see them in scripts, in pitches and in the scam messages on your phone. For you as a writer it is a ready-made act structure. For MTRX\u2122 it is a map of exactly where a sensible process breaks a con.",
    case=dict(k='Field researcher', name='David W. Maurer', role='Linguist at the University of Louisville who studied the language of the American underworld',
              facts=[('Book', 'The Big Con: The Story of the Confidence Man (1940)'),
                     ('Method', 'Years of interviews with professional grifters, recorded in their own slang'),
                     ('Died', '1981, aged 75, reported by the New York Times as an expert on underworld slang'),
                     ('Afterlife', 'Sued over The Sting in 1974; the case settled in 1976 (stop 4.4)')],
              stamp=('hold', 'Holds up: a primary field study')),
    cold=dict(q='A con artist and a mark are about to close a deal. The mark is excited. Guess: does the professional want the mark to feel smart, or stupid, at this moment?',
              a="Smart. Maurer noticed that the mark's own appetite for profit, secrecy or status writes half the dialogue. A mark who feels clever stops checking, because checking would mean doubting his own judgement. Maria Konnikova puts it in modern terms in The Confidence Game (2016): the victim is a co-author of the story. That is why the best defence is not suspicion of people. It is a process that checks claims even when you feel brilliant."),
    video=dict(id='hSlBiMdlyyU', title='The Psychology of Con Artists, and How to Avoid Them', who='Maria Konnikova \u00b7 Big Think',
               watch=['Why a con is a story the mark helps to write',
                      'The moment Konnikova says the con moves from trust to commitment',
                      'Her practical defence, and how it maps onto the breakdown step']),
    story=["In the 1920s and 30s, American grifters ran two kinds of game. A short con is quick and local: one interaction, one lie, a few dollars. A big con is a production. It has a crew, a constructed world (a fake betting parlour or stockbroker's office, called the store), props, rehearsal and weeks of time. Maurer's book is the record of how those productions worked, written in the crew's own words.",
           "The sequence runs like this. The put-up picks a mark with money and an appetite. The play brings him into a believable situation. The roper, a friendly stranger, wins his trust and steers him to the inside man, the apparent expert who controls an opportunity. The tale is that opportunity. The convincer lets the mark win a little, so the story now has evidence. The breakdown is a crisis that demands action now. The send moves the mark to fetch more money. The touch takes it. The blow-off makes the crew disappear, often leaving the mark feeling guilty rather than robbed. The fix is the cover: a bribed official or a story that stops the complaint. Some summaries merge steps and count nine. That is a presentation choice, not a correction.",
           "Notice the division of labour. Trust is not built by one charismatic liar. It is passed from person to person: the roper vouches for the inside man, the store's extras make the room feel real, the convincer makes the money feel real. A screenwriter should read this as a cast list. Each role exists to make one kind of doubt feel unnecessary.",
           "The cognitive scientist Hugo Mercier adds a vital correction in Not Born Yesterday (2020). Humans are not naturally gullible. We evolved to be vigilant about what others tell us, and we reject most claims that conflict with our interests or come from unreliable sources. A con works not by switching off that vigilance but by arranging a world where checking feels rude, risky or pointless: the expert seems independent, the proof seems real, and the clock is running.",
           "That gives you the defence, and it is the same in 1925 and 2026. Two steps are where the con is most exposed. At the convincer, ask who controls the proof. If the person selling you the opportunity also supplied the evidence, it is not evidence. At the breakdown, refuse the deadline. Real opportunities survive a 24-hour pause and a second opinion. Almost every modern scam you will meet in stop 6.6 has a convincer (a fake dashboard, a small first payout) and a breakdown (a fee due today, an account about to freeze)."],
    fig=(FIG, 'The ten steps of the big con. The convincer and the breakdown are where a calm process breaks it.'),
    specs=[('Roper', 'The approach person. Friendly, apparently disinterested, steers the mark to the inside man.'),
           ('Inside man', 'The apparent expert who controls the opportunity. The mark trusts him because the roper did.'),
           ('Convincer', 'A small win or proof that turns the story into evidence in the mark\'s mind.'),
           ('Blow-off', 'Ending contact so the mark leaves quietly, often blaming himself.'),
           ('Store', 'The fake setting: a betting parlour, broker\'s office or, today, a website.')],
    tags=[('part', '"A big con has exactly nine stages."', 'Maurer lists ten; many summaries merge two. Count is a presentation choice.', ('Maurer, The Big Con (WorldCat)', 'https://search.worldcat.org/title/930462967')),
          ('myth', '"Marks are simply gullible people."', 'Mercier: humans are vigilant by default. Cons work by making checking feel costly.', ('Mercier, Not Born Yesterday', 'https://press.princeton.edu/books/hardcover/9780691178707/not-born-yesterday')),
          ('myth', '"The roper is the one with the expertise."', 'The roper approaches; the inside man plays the expert. Two roles, two kinds of trust.', ('Maurer excerpt', 'https://cse.iitk.ac.in/users/amit/books/maurer-1974-american-confidence-man.html')),
          ('hold', '"The fix is part of the con."', 'Maurer treats the cover story or bribed official as the final phase.', ('Maurer obituary, NYT 1981', 'https://www.nytimes.com/1981/06/14/obituaries/david-w-maurer-is-dead-at-75-an-expert-on-underworld-slang.html'))],
    distil=[('Maurer, The Big Con (1940)', 'https://search.worldcat.org/title/930462967', 'The field study every con film borrows from'),
            ('Konnikova, The Confidence Game (2016)', 'https://www.penguinrandomhouse.com/books/235443/the-confidence-game-by-maria-konnikova/', 'The psychology of each step'),
            ('Mercier, Not Born Yesterday (2020)', 'https://press.princeton.edu/books/hardcover/9780691178707/not-born-yesterday', 'Why people are less gullible than we think')],
    writer=dict(notes=["Maurer's ten steps are an act structure. Put-up to rope is your first act: we meet the mark and his want. Tale to breakdown is the second act, rising stakes and a midpoint convincer that makes the audience believe too. Send to fix is the third act. The best con scripts let one step go wrong, because the plan breaking is where character shows.",
                       "Give every crew member a different job of trust. The roper is warm, the inside man is aloof, the extras are bored. The contrast is what sells the world. If all your con artists are charming, the audience smells it."],
                drill="Write the same opportunity described three times: by the roper in a bar, by the inside man in his office, and by the mark to his wife a month later. Fiction only. Notice what each version leaves out."),
    biz="A client who brings secrecy (do not tell your team), urgency (decide today) and an unverifiable decision-maker is running a breakdown on your process, whether they mean to or not. MTRX\u2122 rules: written scope, a second approver for any change in payment details, staged payments, and a 24-hour pause on anything that cannot wait.",
    tryit="Open your phone and find one scam message, spam email or too-good offer. Label each part with Maurer's steps: who is the roper, what is the tale, what is the convincer, what is the breakdown. Then write the one check that would have broken it.",
    room='The mark is not stupid. The room has been designed so that checking feels like betrayal.',
    deeper=[('Maria Konnikova: We are all vulnerable to con artists (Charlie Rose)', 'https://www.youtube.com/watch?v=KjIpYiT8kjQ', 'A longer conversation on why expertise does not protect you'),
            ('Luc Sante introduces The Big Con', 'https://www.penguinrandomhouse.com/books/109418/the-big-con-by-david-maurer-introduction-by-luc-sante/', 'Why the book still matters')],
    nextq='You have the skeleton. Now watch it walk: how did one man in a Paris hotel use these steps to sell a monument that was never for sale? Stop 4.2.',
    checks=[dict(q='In Maurer\'s big con, which role makes the first friendly approach?',
                 o=['The roper, who wins trust and steers the mark onward',
                    'The inside man, who controls the opportunity',
                    'The fixer, who bribes officials after the touch'], a=0,
                 w='The roper approaches and vouches. The inside man plays the expert. Trust is passed between roles.'),
            dict(q='What makes a big con "big" rather than short?',
                 o=['A crew, a staged world, props and time',
                    'A louder promise of bigger riches',
                    'A victim with more education than usual'], a=0,
                 w='A short con is one quick interaction. A big con is a production with roles and a set.'),
            dict(q='Following Mercier, what is the best defence against a con?',
                 o=['Independent checking and a pause, even when you feel clever',
                    'Assuming that intelligent people rarely need checks',
                    'Treating every stranger you meet as dishonest'], a=0,
                 w='People are vigilant by default. Cons make checking feel costly, so build checks that run anyway.')],
)

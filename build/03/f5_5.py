from svg import box, t, arrow, line, svg

COLS = [('ANTWERP, 2003', 'Diamond Centre vault', 'beat layered alarms', 'rubbish dumped near a motorway'),
        ('HATTON GARDEN, 2015', 'safe deposit vault', 'drilled through a wall', 'a car on CCTV, talk on tape'),
        ('LOUVRE, 2025', 'Galerie d\'Apollon', 'in and out in minutes', 'arrests, but no jewels yet')]
ROWS = ['THE TARGET', 'THE SKILL', 'THE SLIP']
def col(i, c):
    x = 200 + i * 330
    out = box(x, 56, 310, 50, 's-box-j', 10) + t(x + 155, 87, c[0], 's-t-b')
    for r in range(3):
        y = 122 + r * 74
        out += box(x, y, 310, 60, 's-box-a' if r == 2 else 's-card', 10) + t(x + 155, y + 36, c[r + 1], 's-t-sm')
    return out
FIG = svg(1180, 420, 'Three real heists compared: the target, the skill, and the mundane slip that undid each crew',
          t(590, 32, 'THREE REAL HEISTS: WHERE THE SKILL WAS, AND WHERE IT BROKE', 's-t') +
          ''.join(t(100, 158 + r * 74, n, 's-t-b') for r, n in enumerate(ROWS)) +
          ''.join(col(i, c) for i, c in enumerate(COLS)) +
          line(80, 362, 1100, 362, True) +
          t(590, 396, 'The vault was the hard part on paper. The everyday part is where real crews get caught.', 's-t-sm'))

STOP = dict(
    id='5.5', day=34, title='Real heists: Antwerp, Hatton Garden, the Louvre 2025',
    q='Three of the most skilful heists of the century beat vaults, alarms and a world-famous museum. Why were the crews caught by a sandwich, a car and a phone call?',
    why="You now know how heist films work. Real heists are the control group. They show which parts of the genre are fantasy, which parts are true, and where the drama really lives. For a writer, the gap between the film and the case file is pure material: real crews are less glamorous, more human and far more likely to fail at something boring.",
    case=dict(k='The cases', name='Antwerp, Hatton Garden, the Louvre', role='Three vault and museum thefts from 2003, 2015 and 2025',
              facts=[('Antwerp', 'February 2003. The BBC reported 120 of 160 vaults emptied'),
                     ('Hatton Garden', 'Easter 2015. 73 boxes ransacked, worth just short of £14m'),
                     ('Louvre', '19 October 2025. Eight items worth €88m taken in minutes'),
                     ('Common thread', 'Skill beat the security. Ordinary mistakes beat the crews')],
              stamp=('field', 'Field test: compare film and file')),
    cold=dict(q='The Antwerp crew beat a vault with layers of protection. What do you think led police to them within days?',
              a="A bag of rubbish. It was dumped in woodland near the E19 motorway, and it was found and reported. Inside were documents and a half-eaten salami sandwich that investigators linked to the crew. Leonardo Notarbartolo was arrested on 21 February and later sentenced to ten years. The vault took years to plan; the getaway rubbish took a few minutes, and that was the part nobody planned."),
    video=dict(id='SASDkIQjouI', title="Louvre Heist: How Thieves Stole 'Priceless' Jewels in Broad Daylight", who='The Wall Street Journal',
               watch=['How the thieves used ordinary disguises and equipment instead of film gadgets',
                      'How short the time inside the gallery was',
                      'What went wrong for the thieves, even in a few minutes']),
    story=["Antwerp, February 2003. Over the weekend of 15 and 16 February, a crew got into the vault beneath the Antwerp Diamond Centre and opened most of the safe deposit boxes. The BBC reported that 120 of 160 vaults were emptied. On paper it was the perfect heist film: layered security, a crew of specialists, no violence. Then the rubbish was found near the motorway, with a half-eaten sandwich. Leonardo Notarbartolo was arrested on 21 February and sentenced to ten years. Years later he gave Wired (Joshua Davis, 2009) his own version of the story, which other investigators and the book Flawless dispute. Even the case file has a twist that nobody can fully verify.",
           "Hatton Garden, Easter 2015. A crew of veteran criminals climbed down a lift shaft into a London safe deposit vault and drilled three overlapping holes through its wall. The first night failed: a pump could not topple the cabinet blocking the hole. They came back two nights later and ransacked 73 boxes, worth just short of £14m according to the judge's sentencing remarks of March 2016. They had ditched their phones for walkie-talkies. What caught them was ordinary: a distinctive Mercedes picked up on CCTV, and conversations police later recorded. About £4.5m was recovered. One man, known only as Basil, was still at large when sentence was passed.",
           "The Louvre, 19 October 2025. Thieves dressed as workmen used a truck-mounted lift to reach a window of the Galerie d'Apollon, cut in with angle grinders, and were gone in around seven or eight minutes with eight items of the French crown jewels, valued at €88m. They dropped Empress Eugénie's crown on the way out; it was recovered, damaged. A year later, France24 reported that at least seven people had been arrested and four suspects were jailed awaiting trial, but the jewels themselves were still missing. The gallery reopened in July 2026, and the museum's director resigned in February 2026.",
           "Put the three side by side and the pattern is clear. The skill went into the target: the vault, the wall, the window. The failure came in the everyday parts nobody rehearses: getting rid of rubbish, using a car, talking afterwards, dropping something heavy while running. Films put their tension in the vault. Real cases put it in the aftermath. The loot is also a problem films skip: famous diamonds and crown jewels are hard to sell, which is why stolen art and jewellery are so often broken up or never seen again.",
           "For a writer, this is a gift. The most interesting scene in a real heist is rarely the break-in. It is the kitchen-table moment afterwards, when the crew has to trust each other with a secret, a share and a story. Stop 5.4 said the crew is the story. The case files agree: crews come apart through ordinary human things, and that is where the drama is."],
    fig=(FIG, 'Three real heists. The skill went into the target; the slip came in the everyday part of the job.'),
    specs=[('Safe deposit vault', 'A room of individually rented boxes; the bank often does not know what each box holds.'),
           ('Aftermath', 'The getaway, the selling and the silence: the part of a real heist most likely to fail.'),
           ('Sentencing remarks', 'The judge\'s written summary of a case; often the most reliable public account of what happened.')],
    tags=[('hold', '"The Antwerp crew was undone by its own rubbish."', 'Yes: documents and a half-eaten sandwich in a bag near the E19 led police to the crew.', ('Wired, Joshua Davis, 2009', 'https://www.wired.com/2009/03/ff-diamonds-2/')),
          ('part', '"Notarbartolo told the true story of Antwerp."', 'He told his story. Parts are disputed, so treat it as a source, not the record.', ('BBC report, February 2003', 'https://news.bbc.co.uk/2/hi/europe/2797897.stm')),
          ('myth', '"The Louvre case is solved."', 'Arrests have been made, but a year on the jewels were still missing.', ('France24, one year on', 'https://www.france24.com/en/france/20261019-louvre-100-million-crown-jewels-one-year-heist'))],
    distil=[('Hatton Garden sentencing remarks (2016)', 'https://www.judiciary.uk/wp-content/uploads/2016/03/r-v-collinsothers.pdf', 'The judge\'s account of the job'),
            ('Wired: the Antwerp heist (2009)', 'https://www.wired.com/2009/03/ff-diamonds-2/', 'Notarbartolo\'s version, read with care'),
            ('France24: the Louvre, one year on', 'https://www.france24.com/en/france/20261019-louvre-100-million-crown-jewels-one-year-heist', 'Where the case stands')],
    writer=dict(notes=["Put a real heist's tension where real heists fail: after the job. A crew that has already won is a crew with a secret to keep, and keeping it is harder than the vault.",
                       "Give the plan a boring weak point and plant it early: a car, a bag, a phone, a loose-lipped partner. The audience will forgive a clever vault but not an unearned mistake."],
                drill="Take a fictional heist of your own. Write the job in two lines, then write one full page set the morning after, where the crew discovers a mundane slip. No vault scenes allowed."),
    biz="Projects fail the same way. MTRX™ can nail the hard part (the design, the build) and still lose a client over the boring part: a missed invoice, an expired domain, a password nobody wrote down. Write a short handover checklist for every launch, because the aftermath is where trust breaks.",
    tryit="Pick any of the three cases. In three lines, write the moment you think was most dramatic for the crew, and why a film would probably skip it.",
    room='The vault is the hard part on paper. The everyday part is where real crews get caught.',
    deeper=[('INTERPOL: the Louvre jewels added to its stolen art database', 'https://www.interpol.int/en/News-and-Events/News/2025/Louvre-Museum-theft-Stolen-jewels-added-to-INTERPOL-s-Stolen-Works-of-Art-database', 'How stolen art is tracked'),
            ('Town and Country: the Louvre jewels, one year later', 'https://www.townandcountrymag.com/leisure/arts-and-culture/a73979169/louvre-heist-french-crown-jewels-missing-one-year-later/', 'The missing pieces')],
    nextq='Every heist above needed someone to get past people, not only locks. How do modern criminals talk their way past a help desk, and how do you stop it? Stop 5.6.',
    checks=[dict(q='What led police to the Antwerp crew?',
                 o=['A bag of rubbish dumped near the E19 motorway',
                    'An insider who confessed the morning after the job',
                    'A fingerprint left on the vault door'], a=0,
                 w='Documents and a half-eaten sandwich in the rubbish linked the crew. The getaway was the weak point.'),
            dict(q='Where does the pattern across the three cases put the failure?',
                 o=['In the everyday aftermath: cars, rubbish, talk, a dropped item',
                    'In the vault, which none of the crews could fully open',
                    'In the planning, which all three crews rushed'], a=0,
                 w='Skill went into the target. The mundane parts nobody rehearsed undid them.'),
            dict(q='A year after the Louvre theft, what was the state of the case?',
                 o=['Arrests made and suspects jailed, but the jewels still missing',
                    'All eight items recovered and returned to the gallery',
                    'No arrests and no suspects identified'], a=0,
                 w='France24 reported at least seven arrests and four jailed suspects, but no recovered jewels.')],
)

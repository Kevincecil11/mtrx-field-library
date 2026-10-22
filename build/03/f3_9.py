from svg import box, t, line, circle, svg

COLS = ['The need', 'Belonging', 'Charisma', 'Closed world', 'The after']
FILMS = [('The Wicker Man (1973)', [0, 0, 1, 2, 0]), ('The Master (2012)', [2, 1, 2, 1, 1]),
         ('Martha Marcy May Marlene (2011)', [2, 1, 2, 2, 2]), ('Midsommar (2019)', [2, 2, 0, 2, 0])]


def dot(cx, cy, v):
    if v == 2:
        return circle(cx, cy, 15, 's-box-a')
    if v == 1:
        return circle(cx, cy, 15, 's-card')
    return line(cx - 8, cy, cx + 8, cy)


FIG = svg(1180, 430, 'Four cult films scored against five mechanisms',
          box(20, 20, 1140, 390, 's-card') +
          ''.join(t(560 + i * 130, 64, c, 's-t-sm') for i, c in enumerate(COLS)) + line(40, 84, 1140, 84) +
          ''.join(t(50, 140 + r * 66, f, 's-t-b', 'start') + ''.join(dot(560 + i * 130, 134 + r * 66, v) for i, v in enumerate(vs)) +
                  (line(40, 168 + r * 66, 1140, 168 + r * 66, dash=True) if r < 3 else '') for r, (f, vs) in enumerate(FILMS)) +
          t(590, 396, 'Filled: the film\'s engine. Open: present. Dash: absent. These are readings of films, not research findings.', 's-t-sm'))

STOP = dict(
    id='3.9', day=23, title='On screen: The Master, Midsommar, The Wicker Man, Martha Marcy May Marlene',
    q='Four of the best cult films ever made each get something right that the headlines miss. What, exactly, and what do they get wrong?',
    why="This is the boss fight for File 3, and the 60% writer's half of this course in full. Each film puts one mechanism from Files 1 to 3 at its centre: the after, charisma as a relationship, belonging as a gift, and two closed worlds colliding. Reading them like a researcher is how you learn to write your own, and how you avoid the cliches that make most cult films feel fake.",
    case=dict(k='Field test', name='Four films, four engines', role='Read with everything from Files 1 to 3',
              facts=[('The Wicker Man', '1973, directed by Robin Hardy, written by Anthony Shaffer'),
                     ('Martha Marcy May Marlene', '2011, written and directed by Sean Durkin; Elizabeth Olsen\'s breakout'),
                     ('The Master', '2012, written and directed by Paul Thomas Anderson'),
                     ('Midsommar', '2019, written and directed by Ari Aster')],
              stamp=('field', 'Field test: boss fight')),
    cold=dict(q='One of these four films spends most of its running time after the character has already escaped the group. Which one, and why is that the braver choice?',
              a="Martha Marcy May Marlene. Martha flees a commune in the Catskills in the first minutes and spends the film at her sister's lake house, where the past keeps cutting into the present without warning. It is braver because it dramatises what stop 3.6 described, the after, which almost every other film skips. The escape is not the climax. The climax is realising the group came with her."),
    video=dict(id='a-tDnavDCwI', title='The Wicker Man (1973), official trailer', who='Rotten Tomatoes Classic Trailers',
               watch=['How the island is shown as warm, musical and united, never as obviously sinister',
                      'Which character is the true outsider, and how sure he is of his own faith',
                      'How the trailer sells a mystery while hiding that it is really a trap']),
    story=["Martha Marcy May Marlene is the film about the after. Patrick, the leader (John Hawkes), renames her Marcy May; Marlene is the name every woman uses on the commune's phone. The editing slides between the farm and the lake house with no signal, so the audience floats exactly as former members describe (stop 3.6). Patrick is never a ranting monster. He listens, he sings to her, he tells her she is a teacher and a leader. The film's insight is that the group's gentlest gifts are what make the abuse possible, and what make leaving feel like losing yourself.",
           "The Master is the film about charisma as a relationship, which is Weber's point from stop 2.3. Freddie Quell (Joaquin Phoenix) is a damaged Navy veteran, drifting after the Second World War. Lancaster Dodd (Philip Seymour Hoffman) leads a movement called the Cause, and the film is widely read as drawing on the early years of Scientology. Their first Processing session, a run of rapid personal questions where Freddie may not blink, is the most famous scene. Watch what each man gets. Freddie gets attention, a father and a structure. Dodd gets a test case, a disciple and a wild animal he can claim to tame. Charisma is something they make together.",
           "Midsommar is the film about belonging, and it is Durkheim's effervescence from stop 3.1 made into horror. Dani (Florence Pugh) has just lost her whole family, and her boyfriend cannot hold her grief. At a Swedish commune's midsummer festival, the women surround her as she sobs and wail with her, matching her breath. It is the first time anyone has felt her pain with her. The community gives her exactly what she lacks. That is why the ending lands as both horror and release, and why the film is about recruitment more than murder.",
           "The Wicker Man is the film about two closed worlds. Sergeant Howie (Edward Woodward), a devout Christian policeman from the mainland, flies to the island of Summerisle to find a missing girl. The islanders, led by Lord Summerisle (Christopher Lee), practise a revived paganism and treat him with polite mockery. He is certain he is the only rational person on the island. The twist is that his certainty was the bait. The islanders needed a particular kind of outsider for their ritual, and he walked in of his own free will. The film refuses to let either faith off the hook.",
           "Now the critic's half. These are readings of films, not research findings, and each film bends the truth for drama. Midsommar's commune is so visually perfect that it feels more like a machine than a society; real groups are messier, more boring and more internally divided. The Wicker Man's islanders have no doubters at all. The Master's Dodd is unusually self-aware. The best of them, MMMM above all, are honest about the most important fact in this course: the group gives something real. Weaker cult films fail precisely there, with recruits who are fools and leaders who are cartoon hypnotists.",
           "Distil it into one writer's rule. Make the belonging beautiful enough that the audience understands the loss, then show the price of keeping it. Every scene in a cult story should either give the character something she needs or raise the cost of walking away. If a scene does neither, cut it."],
    fig=(FIG, 'Each film has an engine. MMMM is the only one that scores on the after, which is why former members often name it as the truest.'),
    specs=[('Engine', 'The one mechanism a story is built around. Pick one; let the others support it.'),
           ('The gift', 'What the group gives the character that nobody else does. Without it, the audience cannot believe she stays.'),
           ('The price', 'What keeping the gift costs: relationships, money, safety, truth. Raise it scene by scene.'),
           ('Point of view', 'Whose eyes the audience sees the group through: recruit, leader, outsider or survivor. It decides the genre.')],
    tags=[('hold', '"The best cult films show the group giving something real."', 'Matches the research: members join for bonds and belonging, then pay later.', ('Barker 2011', 'https://researchonline.lse.ac.uk/id/eprint/50872/1/Barker_Stepping_ivory_tower_2011.pdf')),
          ('myth', '"A believable cult leader must be a hypnotic monster."', 'Attention, identity work and real care persuade more than theatrical evil.', ('Haslam et al.', 'https://doi.org/10.1016/j.copsyc.2018.08.006')),
          ('part', '"Midsommar shows how communes really work."', 'True to grief and synchrony; far too seamless and doubt-free for a real group.', ('Wiltermuth and Heath 2009', 'https://doi.org/10.1111/j.1467-9280.2008.02253.x'))],
    distil=[('Martha Marcy May Marlene, official trailer', 'https://www.youtube.com/watch?v=ERREgOobLOs', 'The after, and the floating edit'),
            ('The Master, official teaser', 'https://www.youtube.com/watch?v=1WTM8eO1Oec', 'Charisma as a relationship'),
            ('Midsommar, official trailer', 'https://www.youtube.com/watch?v=1Vnghdsjmd0', 'Belonging as the gift'),
            ('The Wicker Man, official trailer', 'https://www.youtube.com/watch?v=a-tDnavDCwI', 'Two closed worlds')],
    writer=dict(notes=["Choose your point of view first, because it decides the film. A recruit's view makes a drama of seduction (Midsommar). A survivor's view makes a drama of memory (MMMM). A follower and leader together make a love story (The Master). An outsider's view makes a thriller or a trap (The Wicker Man). Most weak cult scripts switch between all four and land in none.",
                       "Then build a recruit arc in beats: need, contact, relief, friendship, small commitment, new vocabulary, public investment, conflict with outsiders, and the moment exit becomes expensive. Keep the leader offscreen longer than feels comfortable. The group sells him before he ever has to sell himself."],
                drill="Write a six-beat outline for a fictional cult film: grief, welcome, friendship, first sacrifice, first contradiction, first lie told to an outsider. Keep the leader offscreen until the final beat. Fiction only, no real group."),
    biz="The same rule sells honestly: show the client what they gain (the gift) and be straight about what it costs (the price). A portfolio case study for MTRX\u2122 works like a good cult film in reverse. Open on the client's real need, show the relief, and put the full price on the page so nobody feels trapped later.",
    drill=dict(name='Read a cult film like a researcher', mins='20 min, then any film',
               steps=['Name the need: what is missing in the character\'s life in the first ten minutes?',
                      'Find the gift: what does the group give that nobody else does?',
                      'Mark the first small yes, and the first moment saying no would cost something.',
                      'Spot one of Lifton\'s eight (stop 1.3) on screen: milieu control, loaded language, confession, and so on.',
                      'Find the boundary: who is outside, and what is said about them?',
                      'Decide which myth the film believes: robot, free shopper, or bounded choice (stop 3.3).'],
               mistake='Judging the characters as stupid. If you would not have said yes in her place, the film failed, or you have not looked closely enough at the need.'),
    tryit="Pick any one of the four films (or any cult film you know) and run the six drill steps from memory, one line each. Then score it on the five mechanisms in the diagram. Which mechanism is its engine?",
    room='Make the belonging beautiful enough that the audience feels the loss, then show the price of keeping it.',
    deeper=[('Wild Wild Country, official trailer', 'https://www.youtube.com/watch?v=hBLS_OM6Puk', 'The documentary that plays like a thriller, about Rajneeshpuram'),
            ('The Vow, Part I trailer (HBO)', 'https://www.youtube.com/watch?v=eXKJyh_rl0I', 'NXIVM from inside, through former members\' own footage')],
    nextq='File 4 switches sides. A cult wants to keep you forever; a con wants your money and then wants you gone, ideally thanking him. How is a con built, beat by beat? Stop 4.1.',
    checks=[dict(q='Which mechanism is the engine of Martha Marcy May Marlene?',
                 o=['The after: the group keeps living in her once she has escaped',
                    'The siege: the police surround the farm and the group fights back',
                    'The recruitment: most of the film shows her first week inside'], a=0,
                 w='She escapes at the start. The film is about floating, memory and the gifts that made the abuse possible.'),
            dict(q='What does Midsommar\'s shared-wailing scene show in Durkheim\'s terms?',
                 o=['Collective emotion giving Dani the belonging nobody else offered',
                    'A hidden technique that erases Dani\'s memory of her own family',
                    'Proof that the commune is simply evil and gives her nothing real'], a=0,
                 w='The group feels her grief with her. The gift is real, which is why the horror works.'),
            dict(q='What is the writer\'s rule distilled from this stop?',
                 o=['Every scene gives her something she needs or raises the cost of leaving',
                    'Every scene shows the leader hypnotising someone in a new and scary way',
                    'Every scene explains the doctrine so the audience can judge its logic'], a=0,
                 w='Gift and price drive the story. Scenes that do neither can go.')],
)

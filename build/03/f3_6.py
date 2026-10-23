from svg import box, t, arrow, svg

EXITS = [('WALKAWAY', 'doubt, a contradiction, burnout'), ('CASTAWAY', 'expelled, shamed, cut off'), ('HELPED OUT', 'exit counselling, a family door')]
GAP = [('No money or papers', 'the practical gap'), ('No friends outside', 'the social gap'), ('Group words in your head', 'the floating gap')]
BUILD = [('Second source of truth', 'a friend who lets you disagree'), ('Own choices, small first', 'food, music, clothes, then opinions'),
         ('Keep the good parts', 'grief without defending the system')]
FIG = svg(1180, 420, 'Three ways out, the gap after leaving, and rebuilding',
          t(170, 32, 'HOW PEOPLE LEAVE', 's-t') + t(590, 32, 'THE GAP', 's-t') + t(1010, 32, 'REBUILDING', 's-t') +
          ''.join(box(20, 50 + i * 120, 300, 100, 's-card') + t(170, 92 + i * 120, a, 's-t') + t(170, 124 + i * 120, b, 's-t-sm') for i, (a, b) in enumerate(EXITS)) +
          ''.join(box(440, 50 + i * 120, 300, 100, 's-box-j') + t(590, 92 + i * 120, a, 's-t-b') + t(590, 124 + i * 120, b, 's-t-sm') for i, (a, b) in enumerate(GAP)) +
          ''.join(box(860, 50 + i * 120, 300, 100, 's-box-a' if i == 0 else 's-card') + t(1010, 92 + i * 120, a, 's-t-b') + t(1010, 124 + i * 120, b, 's-t-sm') for i, (a, b) in enumerate(BUILD)) +
          arrow(325, 220, 432, 220) + arrow(745, 220, 852, 220, True) +
          t(590, 412, 'Leaving is a process, not a door. Most of the work happens in the middle column.', 's-t-sm'))

STOP = dict(
    id='3.6', day=20, title='Leaving and after: exit costs and rebuilding a self',
    q='If a group is so harmful, why do people stay for years, and what is it actually like to walk out?',
    why="Films end when the character escapes. Real life starts there. Leaving a high-demand group can mean losing your friends, your job, your home, your language and the story that gave your life meaning, all at once. Understanding exit costs explains why smart people stay, and it tells you exactly how to help someone you love who is inside something.",
    case=dict(k='Former member', name='Janja Lalich', role='Nearly 11 years in the Democratic Workers Party, a Marxist cadre group; now a sociologist of cults',
              facts=[('Inside', 'From the mid-1970s to 1985, rising to the inner circle'),
                     ('Family', 'Saw her mother only twice in all those years'),
                     ('The end', 'In late 1985 members expelled the leader while she was abroad and voted to dissolve the party'),
                     ('After', 'Became a professor at California State University, Chico, and wrote Bounded Choice (2004)')],
              stamp=('hold', 'Holds up: exit is a process')),
    cold=dict(q='Most people picture leaving a cult as a rescue: a raid, a kidnapping, an escape at night. Lalich\'s group ended differently. Guess how.',
              a="From the inside. While the leader, Marlene Dixon, was travelling abroad, senior members started talking honestly to each other for the first time in years. Within weeks they had expelled her and voted to dissolve the party. Lalich says she had plenty of moments of clarity before that. What she lacked was anyone to say it to without being reported. Doubt is common inside high-demand groups. A safe person to share it with is rare."),
    video=dict(id='FghSUttp6Lc', title='Former cult member answers cult questions from Twitter', who='Janja Lalich, WIRED Tech Support',
               watch=['How she describes the moments of doubt while still inside',
                      'What she says about why people stay',
                      'Her advice for families who want to help']),
    story=["Start with why people stay, because it is not mainly belief. Lalich's bounded choice from stop 1.2 runs here in reverse. By year five, leaving costs your closest friends, often your partner, your work, your housing and your savings, which may have gone to the group. It costs your sense of having spent those years well. Many groups add phobias about the outside: that leavers go mad, get sick or betray the cause. Against all that, a private doubt has to be very strong to win. Most doubts are quietly folded back in.",
           "People leave in three broad ways. Walkaways leave on their own after a contradiction, burnout, a new relationship or a practical chance. Castaways are expelled, sometimes brutally, and may be shunned by everyone they know. And some are helped out. In the deprogramming era that meant abduction (stop 3.4). Today the respected approach is exit counselling: voluntary conversations, information about the group, and the person free to stop at any time.",
           "Then the gap. Former members describe a strange double life: the body has left, but the group's words still run in the head. Exit counsellors call the sudden slide back into group thinking floating. A song, a phrase or a smell can trigger it. Many people also face practical gaps: no savings, no CV that makes sense, sometimes no documents. And the cultural gap is real. People who spent a decade inside often missed films, music, slang and technology, and feel foreign in their own country.",
           "What does the research say about how people do afterwards? Less than you would hope, because samples are small and self-selected. Two interview studies point the same useful way. In 2008 Buxant and Saroglou interviewed 20 former members and found that membership had compensated for earlier vulnerabilities, a support that did not survive a destabilising exit. In 2012 Coates interviewed 23 former members from 11 groups and found that negative effects were often tied to losing the social world, not a universal brainwashing injury. Outcomes vary widely. Some people describe grief, shame, anxiety and trouble trusting. Others describe relief and a new sense of agency. Many describe both.",
           "Rebuilding follows a pattern. A second source of reality: at least one relationship that does not demand agreement. Small choices first, such as what to eat, what to wear and what music to play, before big opinions. Plain information about the group's methods, which turns personal shame into a recognisable pattern. And permission to keep the good memories. Many former members loved parts of their life inside. Saying so does not mean defending the system.",
           "If someone you love is inside something, the research and the exit counsellors agree on the basics. Keep the door open and keep in touch, whatever they say about you. Do not stage a debate on doctrine; ask curious questions instead. Remind them, without pressure, of who they were and what they loved. Have the practical help ready: a room, some money, a lift. People leave towards someone, not just away from something."],
    fig=(FIG, 'Three exits, three gaps, three rebuilding moves. The middle column is the one films skip and former members talk about most.'),
    specs=[('Exit costs', 'Everything a member would lose by leaving: friends, partner, home, savings, meaning. The real reason most stay.'),
           ('Floating', 'An exit-counselling term for sudden slides back into group thinking after leaving, often triggered by a word or song.'),
           ('Walkaway, castaway', 'Leaving on your own, versus being expelled. Castaways often face sudden shunning by everyone they know.'),
           ('Exit counselling', 'Voluntary talks with a former member or counsellor, with information instead of pressure. Replaced deprogramming.')],
    tags=[('myth', '"Leaving is just deciding to stop believing."', 'Social, material and identity costs can keep people inside long after doubt begins.', ('Lalich, CN&R interview', 'https://www.newsreview.com/chico/content/the-power-of-cults/31494/')),
          ('myth', '"Everyone who leaves is permanently damaged."', 'Interview studies find mixed outcomes, often tied to losing the social world.', ('Coates 2012', 'https://doi.org/10.1080/19349637.2012.697372')),
          ('part', '"Membership was pure loss."', 'Some found it met earlier needs, a support lost when exit was abrupt.', ('Buxant and Saroglou 2008', 'https://doi.org/10.1080/13674670701247528'))],
    distil=[('Lalich interview, Chico News and Review', 'https://www.newsreview.com/chico/content/the-power-of-cults/31494/', 'Her decade inside, in her own words'),
            ('Lalich, Bounded Choice, chapter on the DWP\'s fall', 'https://doi.org/10.1525/california/9780520231948.003.0009', 'How the party ended from inside'),
            ('Coates, interviews with 23 former members (2012)', 'https://doi.org/10.1080/19349637.2012.697372', 'What exit costs and what it resolves'),
            ('Buxant and Saroglou, 20 former members (2008)', 'https://doi.org/10.1080/13674670701247528', 'Why membership helped some, and exit hurt'),
            ('ICSA, Building Bridges: leaving and recovering', 'https://www.youtube.com/watch?v=b_wzgSdX_hQ', 'The practical side of rebuilding')],
    writer=dict(notes=["The richest material in this whole course is the after. Martha Marcy May Marlene knows it: the escape takes five minutes, the rest of the film is a woman who cannot stop speaking the group's language at her sister's dinner table. Write the small moments: hesitating before deleting a group chat, laughing at an old in-joke, a song that makes her float.",
                       "And give your former member a reason to miss it. The audience must understand that freedom can feel empty before it feels safe. If leaving is pure relief, there is no story."],
                drill="Write a scene where a fictional former member, six weeks out, has to choose what to order in a cafe. It is the first time in nine years nobody has told her what to want. Keep the group offscreen."),
    biz="Exit costs explain your clients too. A business stays with a bad agency or a bad tool because leaving costs data, habits, contracts and the pride of having chosen it. When you pitch a switch, MTRX\u2122 should lower exit costs on purpose: migration done for them, no lock-in, a clear way back. People leave towards someone.",
    tryit="Think of something you stayed in too long: a job, a course, a friendship, an app. List what leaving would have cost you at the time. Circle the costs that had nothing to do with whether it was good for you. That circle is what exit costs feel like from inside.",
    room='Leaving is not one event. It is rebuilding a life with more than one source of reality.',
    deeper=[('How cults rewire the brain, Diane Benscoter (TED)', 'https://www.youtube.com/watch?v=NL0uxDscjdo', 'A former Moonie on what leaving felt like'),
            ('The heart of cult recovery (ICSA)', 'https://www.youtube.com/watch?v=fBOqHAHL8dA', 'Self-compassion after leaving')],
    nextq='Everything here assumes there was a self before the group. What happens to someone born inside, who has no before to return to? Stop 3.7.',
    checks=[dict(q='Why do many members stay long after their first doubts?',
                 o=['Leaving would cost friends, home, savings and meaning all at once',
                    'Doubts never appear inside, because the group has removed them',
                    'Groups lock their doors, so walking out is physically impossible'], a=0,
                 w='Exit costs, not certainty, keep most people inside. Doubt is common; a safe place to share it is rare.'),
            dict(q='What does floating describe?',
                 o=['A sudden slide back into group thinking after leaving',
                    'A planned trial period before a member joins for good',
                    'A state of calm detachment that leaders train recruits in'], a=0,
                 w='Former members describe triggers, a phrase, a song, that pull the old frame back for a moment.'),
            dict(q='What is the best first move for a family member of someone inside?',
                 o=['Keep in touch, ask curious questions and have practical help ready',
                    'Win the argument about doctrine, so that they have to see the truth',
                    'Cut contact until they leave, so the group stops feeling worth it'], a=0,
                 w='People leave towards someone. Debate and ultimatums tend to confirm the group\'s story about outsiders.')],
)

from svg import box, t, arrow, svg

_B = [('ISOLATED YOUTH', 'inner world over friends'), ('CRISIS', 'breakdown, illness, exile'),
      ('REVELATION', 'private, then universal'), ('FIRST DISCIPLES', 'belief confirms the self')]
_inner = ''
for _i, (_a, _b) in enumerate(_B):
    _x = 20 + _i * 270
    _inner += box(_x, 40, 240, 128, 's-box-a' if _i == 3 else 's-card') + t(_x + 120, 92, _a, 's-t-b') + t(_x + 120, 122, _b, 's-t-sm')
    if _i < 3:
        _inner += arrow(_x + 240, 104, _x + 268, 104)
_inner += '<path class="s-line-m s-dash" d="M950,170 L950,240 L680,240 L680,174" marker-end="url(#ahm)"/>'
_inner += t(815, 230, 'each confirms the other', 's-t-sm') + t(550, 290, 'Storr: disciples, not equals, hold the guru together', 's-t-b')
FIG = svg(1100, 310, "Storr's guru pattern", _inner)

STOP = dict(
    id='2.2', day=9, title="The guru pattern: Storr's Feet of Clay and the narcissism question",
    q="What is a cult leader's personality like, how does a cult begin, and why does it so often end in sexual and financial abuse?",
    why="The psychiatrist Anthony Storr compared gurus from saints to mass murderers and found a pattern in how they are made. It explains how a cult begins. It also explains why so many end the same ugly way, and that part turns out to be about structure, not personality.",
    case=dict(k='Case file', name='Anthony Storr', role='Psychiatrist; Feet of Clay: Saints, Sinners, and Madmen (1996)',
              facts=[('Compared', 'Gurus from Ignatius Loyola and Gurdjieff to Rajneesh and David Koresh, and even Jung'),
                     ('Pattern', 'An isolated childhood, a crisis or breakdown, then a private revelation'),
                     ('Key trait', 'Extreme narcissism: disciples needed to confirm the self, not friends or equals'),
                     ('Caution', 'A pattern across famous cases, not a diagnosis of any one person')],
              stamp=('part', 'A pattern, not a test')),
    cold=dict(q='Storr compared dozens of gurus, good and terrible. What do you predict most had in common as children: popularity and many friends, or something else?',
              a="Something else. Storr found that many were isolated as children, seldom had close friends, and were more interested in their own minds than in other people. Many then passed through a crisis or breakdown, resolved it with a private revelation, and declared that personal answer true for everyone. Disciples, not equals, became the way they held themselves together."),
    video=dict(id='hBLS_OM6Puk', title='Wild Wild Country, official trailer', who='Netflix, 2018',
               watch=['How followers describe Rajneesh, and how the locals do',
                      'Where you hear a revelation story being told',
                      'What the money, cars and spectacle do for the group']),
    story=["Storr's pattern runs in three beats. First, a solitary youth: many gurus were isolated children who stayed isolated, more absorbed in their inner world than in relationships. Second, a crisis: a breakdown, an illness, an expulsion, a stretch of despair. Third, a revelation, usually reached alone, that resolves the crisis, and which the guru then declares true for everyone. Rajneesh was a sickly child who emerged from a long illness 'enlightened'. David Koresh's change followed his expulsion from the Seventh-day Adventist church.",
           "That is also how a cult begins. A private answer needs an audience to become real. The first followers are often friends, family or a small study circle moved by the founder's certainty. Their belief confirms the revelation, and the revelation explains their lives. A feedback loop forms before any organisation exists. Storr's sharpest point is that the guru needs disciples to confirm his sense of self. Friends and equals can disagree. Disciples cannot.",
           "Storr called extreme narcissism the guru's most defining trait. Use that carefully. It is a psychiatrist's pattern across famous cases, not a diagnosis you can make from a documentary, and plenty of narcissists never found anything. Describe behaviour instead: claims of unique access to truth, a demand for admiration, rage at criticism, expulsion of anyone who disagrees, rules for followers that the leader does not obey. Those are observable, and they are what matter.",
           "Why the sexual and financial abuse? Not because every guru is a predator from day one, but because the structure makes abuse cheap. The leader controls access to meaning, status, housing, work and salvation. If the group teaches that ordinary rules do not apply to the enlightened, sex can be framed as a blessing or a test of loyalty. If money is framed as sacrifice, asking to see the accounts becomes disloyalty. When nobody can say no and nobody can audit, appetite meets no friction.",
           "Gender does not change the structure. In Australia, the yoga teacher Anne Hamilton-Byrne founded The Family in the late 1960s; members believed she was the reincarnation of Jesus, and she recruited doctors, nurses and lawyers. Children in the group had their hair bleached blonde, were kept on sedatives, and lived behind barbed wire until a police raid in August 1987. Male gurus have more often held sexual power over women, because so many groups are patriarchal, but the engine is the same: concentrated, unaccountable power over people who depend on it.",
           "The defence is boring, and it works: independent boards, term limits, open books, safeguarding rules, an outside place to complain, and no private access to dependants. Every one of those is a way of letting someone say no."],
    fig=(FIG, "Storr's three beats, then the loop that starts a movement: the disciples' belief confirms the revelation, and the revelation confirms the guru."),
    specs=[('Revelation', 'A private insight the founder declares true for everyone.'),
           ('Unique access', 'The claim that only the leader can see or interpret the truth.'),
           ('Exemption', 'Rules for followers that the leader does not have to keep.'),
           ('Safeguarding', 'Rules that stop anyone with power from having private, unchecked access to dependants.')],
    tags=[('part', '"Every cult leader is a clinical narcissist."', 'Storr saw narcissism as the defining trait; still, describe behaviour rather than diagnosing at a distance.', ('Campbell, review of Feet of Clay', 'https://acampbell.uk/bookreviews/r/storr.html')),
          ('hold', '"Gurus often pass through a crisis before the revelation."', "A recurring pattern across Storr's cases, from Loyola to Rajneesh.", ('Independent, review of Feet of Clay', 'https://www.independent.co.uk/news/uk/truly-madly-deeply-1339159.html')),
          ('myth', '"Only men lead abusive cults."', 'Anne Hamilton-Byrne ran The Family in Australia until the 1987 raid.', ('BBC, The Family', 'https://www.bbc.com/news/stories-49400118')),
          ('myth', '"Abuse in cults is bad luck with one leader."', 'It follows structural impunity: nobody can refuse or audit.', ('United States v. Raniere (2nd Cir.)', 'https://caselaw.findlaw.com/court/us-2nd-circuit/2088518.html'))],
    distil=[('Storr, Feet of Clay (1996)', 'https://archive.org/details/feetofclaysaints0000stor', 'The guru pattern'),
            ('Storr, an extract on the guru personality', 'https://prem-rawat-bio.org/nrms/gurus/feetofclay.htm', 'Isolation, narcissism and revelation in his own words'),
            ('Independent, review of Feet of Clay (1996)', 'https://www.independent.co.uk/news/uk/truly-madly-deeply-1339159.html', 'The cases: Gurdjieff, Koresh, Rajneesh, Jung, Loyola'),
            ('BBC, raised in a doomsday cult (2019)', 'https://www.bbc.com/news/stories-49400118', 'The Family, from a child who grew up in it'),
            ('CBS 48 Hours, inside The Family (2018)', 'https://www.cbsnews.com/news/48-hours-inside-the-family-cult-australia-anne-hamilton-byrne-part-2/', 'How Hamilton-Byrne recruited and controlled')],
    writer=dict(notes=["Storr's three beats are a ready-made backstory: the lonely child, the breakdown, the revelation. Use them, but never explain them in dialogue. Show the revelation as a story the leader retells, and let it change a little each time. Followers will not notice. The audience will.",
                       "Make the leader charming with followers and small with equals. A scene where an old friend from before the revelation visits, and refuses to treat him as special, can reveal more than any monologue. Watch how he handles someone who knew him when he was ordinary."],
                drill="Write the leader's revelation story twice: once as he tells it to new recruits, once as an old school friend remembers that same year. Same events, two truths."),
    biz="The guru pattern is common in business: the founder whose personal breakthrough becomes a course, then a movement, then a team that cannot disagree. Admire expertise, but watch for unique access ('only I can teach this'), rage at criticism, and books nobody may see. MTRX\u2122 rule: open numbers with partners, and nobody, you included, above the process.",
    tryit='Think of a coach, guru or influencer you have seen up close or online. List three behaviours you can observe, not diagnoses: how they respond to criticism, who they let near them, and which rules they exempt themselves from.',
    room='A guru needs disciples, not friends. Friends can say no.',
    deeper=[('Storr, Feet of Clay (borrow free)', 'https://archive.org/details/feetofclaysaints0000stor', 'The full study'),
            ('The Cult of The Family (documentary site)', 'https://cultofthefamily.com/about/', 'How a yoga teacher recruited Melbourne doctors and lawyers'),
            ('Wild Wild Country (2018), trailer', 'https://www.youtube.com/watch?v=hBLS_OM6Puk', 'Rajneesh, a guru in Storr\'s gallery, at full scale')],
    nextq='Storr explains the leader\'s side of the bond. But charisma is a relationship. What do the followers put into it? Stop 2.3.',
    checks=[dict(q="In Storr's pattern, what usually comes just before a guru's revelation?",
                 o=['A crisis, such as a breakdown, an illness or an expulsion',
                    'A period of great popularity and many close friendships',
                    'Formal training in theology at a respected seminary'], a=0,
                 w='Isolated youth, then crisis, then a private revelation the guru declares true for everyone.'),
            dict(q='Why does Storr say gurus need disciples rather than friends?',
                 o=["Disciples confirm the guru's sense of self; friends can disagree",
                    'Disciples pay more money, which keeps the movement funded',
                    'Friends tend to drift away, while disciples stay for life'], a=0,
                 w="The guru's self-image depends on admiration, so equals who can say no are a threat."),
            dict(q='What best explains why sexual and financial abuse recur in cults?',
                 o=['Power that nobody can refuse or audit makes abuse cheap',
                    'Most leaders start as predators and found groups to hide it',
                    'Members come from backgrounds that make abuse feel normal'], a=0,
                 w='Structural impunity, not just personal appetite. The defences are audit, safeguarding and safe refusal.')],
)

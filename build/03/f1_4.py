from svg import box, t, line, circle, svg


def _node(x, y, label):
    return box(x - 62, y - 22, 124, 44, 's-card') + t(x, y + 6, label, 's-t-sm')


_L = [(110, 110, 'mother'), (250, 74, 'old friend'), (390, 110, 'own job'), (110, 300, 'own money'), (250, 338, 'flatmate'), (390, 300, 'news, books')]
_R = [(650, 74, 'mother'), (1050, 74, 'old friend'), (650, 210, 'own job'), (1050, 210, 'own money')]
FIG = svg(1120, 400, 'Relationship map before and after joining',
          t(250, 36, 'BEFORE', 's-t') + ''.join(line(250, 205, x, y) for x, y, _ in _L) + ''.join(_node(x, y, l) for x, y, l in _L) +
          circle(250, 205, 46, 's-box-a') + t(250, 211, 'her', 's-t-b') +
          line(550, 20, 550, 360, dash=True) +
          t(850, 36, 'AFTER', 's-t') + ''.join(line(x, y, 850, 170, dash=True) for x, y, _ in _R) + ''.join(_node(x, y, l) for x, y, l in _R) +
          box(760, 140, 180, 60, 's-box-a') + t(850, 177, 'THE GROUP', 's-t') + line(850, 200, 850, 260, m=True) +
          circle(850, 300, 40, 's-box-a') + t(850, 306, 'her', 's-t-b') +
          t(250, 388, 'many roads to rest, news and an exit', 's-t-sm') + t(850, 388, 'every tie now runs through one point', 's-t-sm'))

STOP = dict(
    id='1.4', day=4, title='Cutting the cord: why cults isolate you',
    q='Why do cults separate people from friends and family?',
    why="Isolation looks like cruelty, and sometimes it is. But mostly it is engineering. Every outside relationship is a rival source of information, a place to rest, and a road out. A coercive group needs all three closed, and it rarely has to lock a door to do it.",
    case=dict(k='Case file', name='Alexandra Stein', role='Social psychologist; Terror, Love and Brainwashing (2017)',
              facts=[('Inside', 'A 10-year involvement with a Minneapolis political cult known as the O.'),
                     ('Lens', 'Attachment theory: how bonds form under fear'),
                     ('Key idea', 'Fright without solution: the source of fear is also the only offered source of comfort'),
                     ('Why it matters', 'It explains why isolation and love bombing are two halves of one system')],
              stamp=('part', 'Strong model, thin data')),
    cold=dict(q='A new member\'s family calls every week, and the group never forbids it. Six months later she has stopped answering. Nobody told her to. What happened?',
              a="The group did not need a rule. Her schedule filled with meetings and service, her old friends were gently relabelled as negative or not ready, and every call home became a loyalty test she was expected to talk through with someone senior. Isolation is usually polite. That is what makes it work, and what makes it so hard for families to fight."),
    video=dict(id='fa7uN2vo6rc', title='How to spot a cult', who='Sarah Edmondson, TED',
               watch=['How contact with outsiders was reshaped rather than banned',
                      'What the group offered in place of the old relationships',
                      'The moment outside information finally got through']),
    story=["Start with the group's problem. Every independent relationship a member has does three things the group cannot control: it supplies rival information, it offers emotional refuge, and it is a road out. A parent who says 'this sounds wrong' is information. A friend's couch is refuge and an exit. A coercive group that wants total commitment has to neutralise all three.",
           "Lifton's milieu control is the information side. If the group fills the schedule and controls reading, phones, transport and conversation, outside criticism arrives late and sounds hostile. Better still, the group explains it in advance: your family will try to pull you back because they are not ready, or jealous, or spiritually blind. When the worried phone call comes, it confirms the prediction. Concern becomes persecution, because the group has changed what the signal means.",
           "Alexandra Stein, who spent ten years in a political cult before becoming a researcher, adds the emotional side using attachment theory. Humans under threat run to their attachment figures for safety. A coercive group can arrange to be both the source of fear (of failure, of the outside world, of the leader's anger) and the only offered source of comfort. Attachment researchers call that bind fright without solution. The more frightened the member gets, the tighter she clings to the very thing frightening her, and outside friends, who cannot share this world, start to feel far away.",
           "Then comes the cost of exit. Over time the group can come to hold your housing, income, marriage, social life, language and moral identity. Lalich's bounded choice applies again: leaving is still possible, but every alternative now has a price, and for many members the price is everything they have. If children or immigration status are tied to the group, exit stops being a change of opinion and becomes a whole life rebuilt from zero.",
           "Isolation is usually gradual and polite. A new member is simply busy: classes, service, sales targets, retreats. Old friends get relabelled. Family visits are kindly supervised by a senior member. Private doubts are confessed and discussed. Online groups can do the same without any compound, by flooding attention, rewarding constant posting and treating contact with critics as betrayal.",
           "This explains a painful fact for families: sending facts usually fails. Information travels through trusted channels, and the group has already marked yours as hostile. What helps is relational redundancy. Keep the bridge open, stay warm, ask concrete questions about sleep, money and health, never make it the group or us, and keep practical help (a room, a ticket, some money) ready for the day she asks. Many people do leave, and the bridge is often how."],
    fig=(FIG, 'Before: many independent ties, each one a source of news, rest or an exit. After: every tie runs through the group, which now holds the single point of failure.'),
    specs=[('Milieu control', 'Control over the information around a person, so outside views arrive late and sound hostile.'),
           ('Fright without solution', 'A bind where the source of fear is also the only offered source of safety.'),
           ('Exit cost', 'Everything a person would lose by leaving: home, money, marriage, friends, identity.'),
           ('Relational redundancy', 'Keeping several independent communities, so no single group holds every tie.')],
    tags=[('myth', '"Isolation means a locked compound."', 'Schedules, relabelling and loyalty tests isolate people who still live at home.', ('Lifton, chapter 22', 'https://cultrecovery101.com/chapter-22-ideological-totalism/')),
          ('part', '"Family confrontation helps people leave."', "Hostile ultimatums can confirm the group's us versus them story.", ('Dawson 1996', 'https://journals.sagepub.com/doi/10.1177/000842989602500202')),
          ('myth', '"Attachment theory proves every recruit had a bad childhood."', 'It explains how bonds form under fear, not a universal diagnosis.', ('Stein, Terror, Love and Brainwashing', 'https://www.routledge.com/Terror-Love-and-Brainwashing-Attachment-in-Cults-and-Totalitarian-Systems/Stein/p/book/9780367467715')),
          ('hold', '"Exit costs keep people in."', 'Bounded choice: every alternative is priced by the group.', ('Lalich, Bounded Choice (review)', 'https://www.journals.uchicago.edu/doi/reader/10.1086/499025'))],
    distil=[('Stein, Terror, Love and Brainwashing (2017)', 'https://www.routledge.com/Terror-Love-and-Brainwashing-Attachment-in-Cults-and-Totalitarian-Systems/Stein/p/book/9780367467715', 'Attachment under fear; fright without solution'),
            ('Stein, Inside Out (memoir)', 'https://www.alexandrastein.com/inside-out-a-memoir-of-entering-and-breaking-out-of-a-minneapolis-political-cult.html', 'Ten years inside, told from the inside'),
            ('Lifton, chapter 22', 'https://cultrecovery101.com/chapter-22-ideological-totalism/', 'Milieu control'),
            ('Lalich, Bounded Choice (review)', 'https://www.journals.uchicago.edu/doi/reader/10.1086/499025', 'Why exit gets priced out'),
            ('Baumeister and Leary, The need to belong (1995)', 'https://doi.org/10.1037/0033-2909.117.3.497', 'Why losing ties hurts so much')],
    writer=dict(notes=["The most chilling isolation scene is a polite one. Nobody forbids the call. The phone rings, she looks at it, a kind friend from the group says you don't have to answer if it drains you, and she lets it ring. Martha Marcy May Marlene is built on what is left afterwards: a young woman back with her sister, unable to explain a world that taught her to distrust everyone outside it.",
                       "Write the call home where the recruit defends the group in the group's own words, and the parent says exactly the wrong thing. Both are acting from love. That is the tragedy the audience should feel."],
                drill="Write that phone call in 12 lines. The daughter uses at least two of the group's words. The mother makes one mistake: an ultimatum, a sneer or a threat. End on the daughter's silence, not a speech."),
    biz="Watch for the business version: a consultant or guru who tells you not to ask other developers or advisers because they will confuse you. Anyone who wants to be your only source of advice is building milieu control. MTRX\u2122 does the opposite and invites clients to get a second opinion. Confidence that survives comparison is the honest kind.",
    tryit="Draw your own relationship map. Put yourself in the middle, and around you every source of money, affection, information, transport and a place to sleep. Does any single person or group hold three or more? That is your point of failure.",
    room='The real question is not who is forbidden to leave. It is what a person would lose by leaving.',
    deeper=[('How cults rewire the brain (Diane Benscoter, TED)', 'https://www.youtube.com/watch?v=NL0uxDscjdo', 'A former Moonie on what isolation does from the inside'),
            ('Martha Marcy May Marlene (2011), trailer', 'https://www.youtube.com/watch?v=ERREgOobLOs', 'A film about the days after leaving'),
            ('Building bridges: leaving and recovering (ICSA)', 'https://www.youtube.com/watch?v=b_wzgSdX_hQ', 'What families and leavers say actually helps')],
    nextq='So the group holds every tie. But why does a group that asks this much grow stronger instead of weaker? Stop 1.5.',
    checks=[dict(q='In organisational terms, why does isolation help a coercive group?',
                 o=['It removes rival information, emotional refuge and the road out',
                    'It keeps out journalists and spies who might expose its money',
                    'It saves the money members would otherwise spend on visits home'], a=0,
                 w='Outside ties supply information, rest and an exit. Closing all three is the point; secrecy and money are side effects.'),
            dict(q="What does 'fright without solution' describe?",
                 o=['Fear whose source is also the only offered source of safety',
                    'Fear of a danger with no fix, such as death or serious illness',
                    "Fear that fades once a member fully accepts the group's doctrine"], a=0,
                 w='The member runs toward the very thing frightening her, which is why fear deepens the bond instead of breaking it.'),
            dict(q="A friend's sister has joined an intense group. What is the best first move?",
                 o=['Keep the bridge open: stay warm, ask concrete questions, no ultimatums',
                    'Send her every critical article about the group as soon as you can',
                    'Give her a clear choice today: the group or the family, never both'], a=0,
                 w='Facts arrive through a channel the group has marked hostile. A warm bridge and practical help are what leavers say mattered.')],
)

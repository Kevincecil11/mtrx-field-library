from svg import box, t, arrow, svg

_B = [('SMALL YES', 'come to dinner'), ('PUBLIC ACT', 'tell your friends'), ('SACRIFICE', 'time, money, ties'),
      ('DOUBT', 'a prophecy fails'), ('REINTERPRET', 'it was a test')]
_inner = ''
for _i, (_a, _b) in enumerate(_B):
    _x = 20 + _i * 212
    _inner += box(_x, 40, 190, 128, 's-box-a' if _i == 4 else 's-card') + t(_x + 95, 92, _a, 's-t-b') + t(_x + 95, 122, _b, 's-t-sm')
    if _i < 4:
        _inner += arrow(_x + 190, 104, _x + 210, 104)
_inner += '<path class="s-line-m s-dash" d="M963,170 L963,250 L115,250 L115,174" marker-end="url(#ahm)"/>'
_inner += t(540, 240, 'and the next yes is bigger', 's-t-sm') + t(540, 292, 'each lap raises the price of saying "I was wrong"', 's-t-b')
FIG = svg(1100, 310, 'The commitment ratchet', _inner)

STOP = dict(
    id='1.5', day=5, title='Why cults work: strictness, sacrifice and dissonance',
    q='Why do cults work?',
    why="Here is a puzzle economists love. Groups that demand more, in money, time, rules and sacrifice, often grow faster and hold members longer than groups that ask for little. If people simply chased comfort, that should never happen. The answer explains cults, and also elite teams, startups and armies.",
    case=dict(k='Case file', name='Laurence Iannaccone', role='Economist of religion; "Why Strict Churches Are Strong" (1994)',
              facts=[('The puzzle', 'In 1972 Dean Kelley showed liberal US churches shrinking while the strictest ones grew'),
                     ('The model', 'Strictness screens out free riders and raises participation among those who stay'),
                     ('Big claim', 'Explains sects and cults without assuming members are irrational'),
                     ('Limit', 'It explains strength, not truth and not kindness')],
              stamp=('hold', 'Holds up, with limits')),
    cold=dict(q='From the 1960s on, liberal US churches that asked little of their members lost members fast, while strict, demanding churches grew. Why would asking more make a group stronger?',
              a="Because cost filters. Iannaccone's answer: strict rules and visible sacrifices screen out people who want the benefits of a community without contributing (free riders), and the people who stay give more. That makes the group richer in exactly what members came for: warmth, energy, certainty and help. Strictness is a price that buys a better club. It does not make the doctrine true."),
    video=dict(id='UGxGDdQnC1Y', title='Social Influence: Crash Course Psychology #38', who='CrashCourse',
               watch=['How a small yes makes the next, bigger yes easier',
                      'How the role a person plays reshapes what they come to believe',
                      'Which famous studies it presents as settled that later researchers have challenged']),
    story=["The economist Laurence Iannaccone started from a puzzle documented by Dean Kelley in 1972: after two centuries of growth, America's liberal mainline churches began losing members in the 1960s, while the strictest denominations grew. Iannaccone's 1994 paper, Why Strict Churches Are Strong, explained it without assuming anyone was irrational. Strictness, he argued, reduces free riding: it screens out members who lack commitment and stimulates participation among those who remain.",
           "Think of a community as a club good. Everyone benefits from the energy, warmth and help that others put in, and the problem is the free rider who takes the benefits and contributes nothing. A visible sacrifice (a dress code, a diet, a day each week, a tenth of your income, cutting ties with outsiders) is a costly signal. Only people who really value the group will pay it. So the people left are committed, the group feels intensely alive, and outsiders see a community that works. Seen this way, a strange rule is not a bug. It is a filter.",
           "The sociologist Rosabeth Moss Kanter found the same logic in nineteenth-century American communes. Comparing the ones that lasted with the ones that collapsed, she identified commitment mechanisms in three pairs: sacrifice and investment (you have put in too much to walk away), renunciation and communion (you have given up the outside and gained a we), and mortification and surrender (your old self is criticised away, and you hand your judgment to the group). The communes that used more of them survived longer.",
           "Then there is the mind's side. In 1954 the psychologists Leon Festinger, Henry Riecken and Stanley Schachter quietly joined a small group whose leader predicted that a flood would end the world on a set date and that believers would be rescued by a flying saucer. The date passed. Instead of quitting, the core believers began recruiting harder. The book, When Prophecy Fails (1956), launched cognitive dissonance theory: when a belief you have paid heavily for is contradicted, it can feel easier to reinterpret the evidence than to admit the cost was wasted.",
           "Treat that classic with care. It was one small group, observed covertly by researchers who were themselves part of the scene, and later critics have questioned both its method and how cleanly its predictions can be tested. What survives is the general mechanism, which is well supported elsewhere: commitment escalates. Every public act, donation, confession and recruitment pitch makes 'I was wrong' more expensive, because now it means 'I wasted all of that, and I misled my friends'.",
           "Put the three together and you have the engine of a high-demand group: costs that filter, mechanisms that bind, and a mind that defends what it has paid for. None of it needs a hypnotist. The same engine also powers good things, like a demanding sports team or a monastery people love. The difference is not the strength of the commitment. It is whether the costs were disclosed honestly, and whether you can still walk away."],
    fig=(FIG, 'The commitment ratchet. Each lap adds a cost, and a failed prediction gets reinterpreted instead of ending the loop.'),
    specs=[('Free rider', "Someone who takes a group's benefits without contributing. Strict rules screen them out."),
           ('Costly signal', 'A sacrifice only a committed person would pay, which makes commitment visible.'),
           ('Commitment mechanism', 'Kanter: sacrifice, investment, renunciation, communion, mortification, surrender.'),
           ('Cognitive dissonance', 'The discomfort of holding a belief that clashes with evidence, or with what you have done.')],
    tags=[('myth', '"Strictness proves a group is true."', 'It screens for commitment; it says nothing about truth.', ('Iannaccone 1994', 'https://doi.org/10.1086/230409')),
          ('part', '"When prophecy fails, belief always grows."', 'One covert case study; its method and predictions are contested.', ('Thompson and Oskamp 1974', 'https://doi.org/10.2466/pr0.1974.35.2.971')),
          ('hold', '"Groups that demand sacrifice hold members longer."', 'Kanter found the lasting communes used more commitment mechanisms.', ('Kanter 1968', 'https://doi.org/10.2307/2092438')),
          ('myth', '"Sunk costs trap everyone forever."', 'They raise the price of leaving; plenty of people still leave.', ('Iannaccone, sacrifice and stigma', 'https://doi.org/10.1086/261818'))],
    distil=[('Iannaccone, Why Strict Churches Are Strong (1994)', 'https://doi.org/10.1086/230409', 'Strictness as a filter against free riders'),
            ('Iannaccone, Sacrifice and Stigma (1992)', 'https://doi.org/10.1086/261818', 'Why stigma can strengthen a group'),
            ('Kanter, Commitment and Social Organization (1968)', 'https://doi.org/10.2307/2092438', 'Commitment mechanisms in communes that lasted'),
            ('Festinger, Riecken and Schachter, When Prophecy Fails (1956)', 'https://ia902802.us.archive.org/4/items/pdfy-eDNpDzTy_dR1b0iB/Festinger-Riecken-Schachter-When-Prophecy-Fails-1956.pdf', 'Dissonance after the flood that never came'),
            ('Thompson and Oskamp, a critique (1974)', 'https://doi.org/10.2466/pr0.1974.35.2.971', 'Why the classic case needs care')],
    writer=dict(notes=["Sacrifice is the engine of a second act. Each cost your character pays raises the price of walking away, so the audience feels the trap tighten without anyone locking a door. Plan the costs like a ladder: the first is tiny (an evening), the last would have been unthinkable in scene one (her savings, her child, her name).",
                       "The midpoint is often a public act that cannot be undone: a confession in front of everyone, a letter to her parents, a recruitment pitch to her best friend. After it, admitting she was wrong costs too much, and the audience knows it before she does. When the prophecy fails, let her double down, and let the audience understand exactly why."],
                drill="List the five escalating costs your fictional recruit pays, from an evening to something unthinkable. For each, write the group's stated reason and the real organisational function: filter, bind, or silence doubt."),
    biz="Healthy groups ask for commitment too: an elite team, a hard course, a demanding client. The honest version discloses the full cost up front and keeps exit easy. In MTRX\u2122 terms: never use sunk cost against a client ('you've already paid for half, so you have to continue'). Make each phase worth paying for on its own.",
    tryit='List five costs a group in your life asks for: a gym, a job, a faith, a fandom. For each, write its stated meaning and its real function. Which cost builds solidarity, and which builds dependency?',
    room='Sacrifice can signal commitment, but commitment is not evidence.',
    deeper=[('When Prophecy Fails (1956), full text', 'https://ia902802.us.archive.org/4/items/pdfy-eDNpDzTy_dR1b0iB/Festinger-Riecken-Schachter-When-Prophecy-Fails-1956.pdf', 'Read the chapter on the night the flood did not come'),
            ('Kanter, Commitment and Community (1972)', 'https://pdf.stafforini.com/kanter-1972-commitment-community-communes.pdf', 'The communes study, with every mechanism'),
            ('From cognitive dissonance to cognitive doubt (ICSA)', 'https://www.youtube.com/watch?v=T9UyHsShVbE', 'How dissonance shows up in leaving, not only staying')],
    nextq='Costs explain why people stay. But many former members say it was the happiest time of their lives. How can that be true as well? Stop 1.6.',
    checks=[dict(q="In Iannaccone's model, what do strict rules mainly do?",
                 o=['Screen out free riders, so the members who stay give more',
                    'Prove the doctrine true, since people only sacrifice for truth',
                    'Frighten members so much that nobody ever dares to leave'], a=0,
                 w='Strictness is a filter that makes the club better for those who stay. It is silent on whether the doctrine is true.'),
            dict(q='What is the fairest status of When Prophecy Fails today?',
                 o=['Influential, but a single covert case study with method problems',
                    'A replicated lab result showing belief always grows after failure',
                    'A hoax that its authors later admitted they had invented'], a=0,
                 w='The general idea of escalating commitment is well supported. The famous case itself is thin evidence.'),
            dict(q="Why does 'I was wrong' get harder to say the longer you stay?",
                 o=['Each sacrifice makes leaving mean that the costs were wasted',
                    'Members slowly lose the ability to think critically at all',
                    'The doctrine gets more convincing the longer it is studied'], a=0,
                 w='Escalation of commitment: every public act raises the price of admitting error. Thinking still works; it gets aimed at defending the cost.')],
)

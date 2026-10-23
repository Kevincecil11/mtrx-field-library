import math
from svg import box, t, arrow, line, svg

DATA = [('40', 1000, '1,000'), ('100', 7530, '7,530'), ('150', 40496, '40,496'), ('200', 217795, '217,795'),
        ('250', 1171356, '1.17 million'), ('300', 6299832, '6.3 million')]
BASE = 400


def bar(i, yr, v, lab):
    x = 110 + i * 175
    h = round((math.log10(v) - 2) * 62)
    return (box(x, BASE - h, 110, h, 's-box-a' if i == 5 else 's-card', 6) + t(x + 55, BASE - h - 14, lab, 's-t-sm') +
            t(x + 55, BASE + 30, 'AD ' + yr, 's-t'))


FIG = svg(1180, 470, "Stark's projection of early Christian growth at 40 percent a decade, log scale",
          t(590, 34, 'ONE STEADY RATE: 40% A DECADE, ABOUT 3.4% A YEAR', 's-t') +
          line(80, BASE, 1150, BASE) + ''.join(bar(i, *d) for i, d in enumerate(DATA)) +
          t(590, 460, 'Log scale: each bar step is the same multiplication, not the same addition. Figures from Stark (1996), table 1.1', 's-t-sm'))

STOP = dict(
    id='3.2', day=16, title='Recruitment runs on networks, and some cults become world religions',
    q='How does a tiny, mocked group of a few hundred people become a world religion?',
    why="Every large faith started small, mocked and in tension with its neighbours. The sociologist Rodney Stark tried to explain how without miracles or mass hypnosis, and his answer is the same one File 1 found inside cults: friendship networks, compounded patiently. It is the most important growth model you will meet in this course, and it works the same for religions, movements and businesses.",
    case=dict(k='Thinker', name='Rodney Stark and The Rise of Christianity', role='American sociologist of religion, 1934 to 2022; the book appeared in 1996',
              facts=[('The claim', 'Early Christianity could have grown by about 40% a decade, close to the Mormons in the 20th century (43%)'),
                     ('Start', 'About 1,000 Christians in the year 40'),
                     ('Projection', 'About 6.3 million by the year 300, roughly a tenth of the empire'),
                     ('Method', 'Arithmetic borrowed from modern movements, checked against scattered ancient estimates')],
              stamp=('part', 'Partly: brilliant and contested')),
    cold=dict(q='A movement of 1,000 people grows by 40% every decade, through ordinary friendships and family ties. No miracles, no mass rallies. Guess how many members it has 260 years later.',
              a="About 6.3 million. Forty percent a decade is only about 3.4% a year, which feels like nothing in any single year. Compounded over 26 decades, it turns a thousand people into millions. Stark's point was that you do not need mass conversions or spectacular events to explain the rise of a world religion. You need a steady rate and a network that keeps reaching the next person."),
    video=dict(id='2RVSmLxyDpM', title='What even IS a religion?', who='Crash Course Religions #1',
               watch=['Why scholars struggle to define religion at all',
                      'The difference between studying a religion and judging it',
                      'Which features make a tradition last across generations']),
    story=["Stark began where you began in stop 1.2. In the early 1960s he and John Lofland watched the first American converts to the Unification Church. Radio spots and public meetings yielded nothing. The converts were old friends and relatives of members, then people who had formed close friendships inside. In his own words, the only ones who joined were those whose attachments to members overbalanced their attachments to nonmembers. Conversion, he concluded, is less about embracing an ideology than about bringing your religious behaviour into line with your friends and family.",
           "Then he scaled it up. If movements grow through networks, they should grow at steady rates rather than in sudden waves. The Mormons, whose records are good, had grown by about 43% a decade across the 20th century. Stark asked what would happen if early Christianity grew at a similar 40%. Starting from about 1,000 believers in the year 40, the arithmetic gives 7,530 by 100, about 217,000 by 200 and about 6.3 million by 300. Those figures land surprisingly close to the scattered estimates historians already had, which is why the book made such a splash.",
           "Why does the network model beat the sermon model? Because each new member brings a ready-made audience: a spouse, siblings, coworkers, neighbours. A stranger's argument is easy to dismiss. A trusted friend who has visibly changed is not. That is also why open networks matter. A group that seals itself off, as the cults in File 1 did, can recruit intensely but eventually runs out of people to reach. Stark argued that successful movements keep strong ties inside while staying open to outsiders, with a strictness that is demanding but not alien.",
           "Stark later wrote this up as a model of why new religious movements succeed or fail. The features that recur: cultural continuity with the surrounding society, so the new faith does not feel foreign; a medium level of tension, strict enough to feel worth it, not so strict it repels everyone; leadership with real authority; a normal mix of ages and sexes, so the group can have children; and the ability to raise those children inside the faith. Most new movements fail most of those tests, and survivor bias hides the failures. The anthropologist Richard Sosis looked at 200 utopian communities from 19th-century America. The religious ones lasted 25 years on average, and nine in ten had disbanded within 80 years. The secular ones did worse, averaging 6.4 years. We only see the winners, so the winners look inevitable.",
           "Be careful with the slogan you will hear, that every world religion started as a cult. It flattens very different histories, and as stop 1.1 showed, cult is a contested label applied after the fact. The fairer statement is that every large tradition began as a small movement in tension with its world, and that the ones which survived solved the same problems: succession, money, teaching the next generation, and relations with the state. The Latter-day Saints began with a handful of people in 1830 and today report more than 17 million members. The Adventists grew from the disappointed Millerites of stop 2.6.",
           "Critics raise fair points. Stark's starting number is an assumption, the rate probably varied by region and decade, and borrowing a modern rate for an ancient world is a leap. Treat it as a model, not a census. But the core lesson survives every objection: growth that looks miraculous from far away usually looks like friendship up close."],
    fig=(FIG, "Stark's table, drawn on a log scale so a steady rate looks like a steady staircase. The last bar is the one that looks like a miracle; it is the same step as the first."),
    specs=[('Network recruitment', 'Joining through existing ties of friendship and family. The main road into almost every movement studied.'),
           ('Open network', 'Strong ties inside, but many ties still reaching outsiders. The shape that lets a group keep growing.'),
           ('Medium tension', 'Strict enough to feel valuable, not so strange that it repels the neighbours. Stark\'s sweet spot for growth.'),
           ('Compound growth', 'A steady percentage on a growing base. Invisible in one year, enormous over decades.')],
    tags=[('hold', '"People convert through friends and family."', 'Stark and Lofland saw it first among the early Moonies; study after study has found the same.', ('Stark 1996, chapter 1', 'https://www.humanscience.org/docs/Stark%20%281996%29%20Rise%20of%20Christianity%201-2.pdf')),
          ('part', '"Christianity grew 40% a decade for three centuries."', 'A plausible model that fits rough ancient estimates, not a measured fact.', ('Norenzayan, Big Gods, ch. 1', 'http://assets.press.princeton.edu/chapters/s10063.pdf')),
          ('myth', '"Every world religion started as a cult."', 'A slogan that flattens different histories. Small, high-tension movement is the fairer phrase.', ('Barker 2011', 'https://researchonline.lse.ac.uk/id/eprint/50872/1/Barker_Stepping_ivory_tower_2011.pdf'))],
    distil=[('Stark, The Rise of Christianity (1996), chapter 1', 'https://www.humanscience.org/docs/Stark%20%281996%29%20Rise%20of%20Christianity%201-2.pdf', 'Networks, the Moonie evidence and the 40% table'),
            ('Norenzayan, Big Gods (2013), chapter 1', 'http://assets.press.princeton.edu/chapters/s10063.pdf', 'Survivor bias, and how few movements last'),
            ('BYU Religious Studies Center, The Basis of Mormon Success', 'https://rsc.byu.edu/latter-day-saint-social-life/basis-mormon-success', 'Why personal referrals beat cold contact'),
            ('Stark and Bainbridge, Of Churches, Sects, and Cults (1979)', 'https://doi.org/10.2307/1385935', 'Tension as the axis of growth')],
    writer=dict(notes=["Network growth gives you a better recruitment story than any rally. The audience meets a character, then meets her best friend, then watches the friend's brother join because she did. Each step is small and warm. By the time the audience counts heads, the movement has a town.",
                       "It also gives you the classic second-act engine: the group is growing, everyone is winning, and the strain is invisible. Growth hides problems. Use it the way heist films use a plan going perfectly: the smoother it goes, the more the audience waits for the crack."],
                drill="Sketch a fictional movement's first ten members as a family tree of who brought whom. Then write one scene from the point of view of member number seven, who joined for a reason that has nothing to do with the doctrine."),
    biz="This is exactly how MTRX\u2122 will grow, and it is not a cult move. Referrals from happy clients are network recruitment. Stark's warning applies too: a closed network runs dry. Keep a steady habit of reaching new people (outreach, portfolio, posts) while making existing clients the kind of friends who bring you the next one.",
    tryit="Map how you found your last three clients, jobs or close friends. For each, write the chain of people: who introduced whom. Count how many came from a stranger with no link at all. That number is your personal evidence for the network model.",
    room="Growth that looks miraculous from far away usually looks like friendship up close.",
    deeper=[('BYU Religious Studies Center on Stark\'s model', 'https://rsc.byu.edu/latter-day-saint-social-life/basis-mormon-success', 'An insider\'s view of why the Latter-day Saints grew'),
            ('Lofland and Stark, the original 1965 paper', 'https://romolocapuano.com/wp-content/uploads/2016/01/Lofland-and-Stark-becoming-a-worldsaver.pdf', 'Where the network finding began')],
    nextq='If joining runs on friendship and ritual, why did so many people in the 1970s insist it was brainwashing? Stop 3.3 follows that word into the courts.',
    checks=[dict(q='What did Stark and Lofland notice about the first American converts they watched?',
                 o=['They were friends and relatives of members, not strangers moved by ads',
                    'They responded to radio spots and public meetings far more than to friends',
                    'They had studied the doctrine for years before ever meeting a member'], a=0,
                 w='Radio and public meetings yielded nothing. Converts came through ties to members.'),
            dict(q='Why does a 40% per decade growth rate matter so much in Stark\'s model?',
                 o=['A small steady rate compounds into millions without any miracle',
                    'It proves the ancient records counted every single member exactly',
                    'It shows growth came mostly from huge public conversion events'], a=0,
                 w='About 3.4% a year, compounded for centuries, turns 1,000 people into about 6.3 million.'),
            dict(q='Which statement about cults and world religions is the most careful?',
                 o=['Large faiths began as small movements in tension with their world',
                    'Every world religion began as a cult and simply grew out of it',
                    'World religions never began small; they started with state support'], a=0,
                 w='Cult is a contested label. Small, high-tension movement describes the start without the slogan.')],
)

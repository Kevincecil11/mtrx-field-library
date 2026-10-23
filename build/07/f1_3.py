from svg import box, t, svg

_G, _O = 'fill:#9A9DAA', 'fill:#ED691D'


def _dot(x, y, s):
    return '<circle cx="%d" cy="%d" r="15" style="%s"/>' % (x, y, s)


def _sq(x, y, s):
    return '<rect x="%d" y="%d" width="30" height="30" rx="3" style="%s"/>' % (x - 15, y - 15, s)


_inner = box(20, 20, 540, 400, 's-card') + box(620, 20, 540, 400, 's-card')
_inner += t(290, 60, 'ONE FEATURE: IT POPS OUT', 's-t-b') + t(890, 60, 'TWO FEATURES: YOU HUNT', 's-t-b')
for r in range(5):
    for c in range(7):
        x, y = 95 + c * 65, 110 + r * 52
        _inner += _dot(x, y, _O if (r, c) == (3, 5) else _G)
        x2 = 695 + c * 65
        k = (r * 7 + c * 3) % 2
        if (r, c) == (1, 2):
            _inner += _dot(x2, y, _O)
        else:
            _inner += _sq(x2, y, _O) if k else _dot(x2, y, _G)
_inner += t(290, 392, 'found in a glance, however many dots', 's-t-sm') + t(890, 392, 'find the orange circle: you search item by item', 's-t-sm')
FIG = svg(1180, 440, 'Pop-out versus search: a single orange dot among grey dots, and an orange circle hidden among orange squares and grey circles', _inner)

STOP = dict(
    id='1.3', day=3, title='What does the eye grab first, and what does it miss?',
    q='You put the booking button in the middle of the page, in orange. Will people see it? And what will they fail to see that is just as obvious?',
    why="Designers talk about the eye as if it were a camera that records everything and then reads in a fixed pattern. It is not. Attention is a narrow, hungry spotlight, steered partly by what stands out and mostly by what the viewer is trying to do. Once you understand that, hierarchy stops being a matter of taste and becomes a matter of engineering, and you start to see why directors can hide things in plain sight.",
    case=dict(k='Case file', name='Yarbus and the unexpected visitor', role='Alfred Yarbus, Eye Movements and Vision (Russian 1965, English 1967)',
              facts=[('Set-up', "One observer looks at Repin's painting several times, each time with a different question"),
                     ('Result', 'The eye paths change with the task: the family\'s wealth, their ages, their clothes, how long he was away'),
                     ('Correction', 'One observer with restraints; a 2009 replication with 17 people found the effect, smaller'),
                     ('Limit', 'A 2012 study could not reliably read the task back from scan paths alone')],
              stamp=('part', 'Partly: the task steers the gaze')),
    cold=dict(q="Before reading on, play the video in the Watch box and count how many times the players in white pass the ball. Then come back. How many passes, and did you notice anything else?",
              a="If you counted carefully, there is a good chance you missed the person in a gorilla suit who walks through the middle of the game. In the original 1999 study by Daniel Simons and Christopher Chabris, about half of the viewers who were counting passes failed to notice the gorilla. They were not careless. Their attention was doing exactly what it was told to do: follow white shirts and a ball. Everything else, even something huge in the centre, was filtered out."),
    video=dict(id='vJG698U2Mvo', title='Selective attention test', who='Daniel Simons',
               watch=['Do the counting task honestly before anything else',
                      'What you saw once you knew what to look for',
                      'Which part of a website your visitors are "counting passes" on']),
    story=["Start with what the eye does well. In 1980 the psychologist Anne Treisman, with Garry Gelade, showed that a target with one unique basic feature, such as a different colour, orientation or size, can be found almost instantly no matter how many distractors surround it. It pops out. But a target defined by a combination of features, such as an orange circle among orange squares and grey circles, has to be searched for, item by item, and the search slows as the crowd grows. The diagram shows both. Later researchers warn that there is no fixed official list of pop-out features, but the core finding holds: one difference is cheap, combinations are expensive.",
           "That is the bottom-up half of attention, sometimes called salience. In 2000 Laurent Itti and Christof Koch built a computer model that predicts where eyes go first from contrasts in brightness, colour and orientation. Salience really does bias the first glances. But reviews of the field stress that it is a nudge, not a command. After the first second or two, what people look at is driven mostly by what they are trying to do.",
           "Yarbus showed the top-down half with a painting. He tracked one observer's eyes looking at Ilya Repin's They Did Not Expect Him, a scene of a political exile returning home, with a different instruction each time: estimate how wealthy the family is, give their ages, remember their clothes, judge how long the man has been away. The scan paths changed dramatically. The famous figure comes from a single observer whose head was restrained, and later work found the effect real but smaller. The lesson for a designer is still sharp: there is no such thing as how people look at your page. There is only how they look at it while trying to do something.",
           "Now the unsettling part. Attention does not just steer, it deletes. The gorilla study shows inattentional blindness: an unexpected event in plain view goes unseen when attention is busy. Change blindness is its twin. In a 1998 experiment by Simons and Daniel Levin, a researcher asked a stranger for directions; two workers carried a door between them, and the researcher was swapped for a different person. About half the strangers did not notice they were now talking to someone else. Film editors live on this: continuity errors that seem obvious on a frozen frame pass unseen at speed.",
           "Two practical myths fall here. First, the F-pattern. A 2006 Nielsen Norman Group study of 232 users found that people often scan dense, badly formatted text in an F shape, and the finding became a rule. Their own 2017 update says the F is common, not universal, and that good design can prevent it: strong headings, front-loaded words, clear blocks. Second, the brightest thing does not automatically win. A bright orange button may take the first glance, but if the visitor is trying to find the price, their eyes will hunt for numbers, and a button they do not need stays invisible however loud it is."],
    plates=[dict(key='repin', after=2, cap="Repin's They Did Not Expect Him. Ask yourself one question at a time and notice where your eyes go: who is the man? Is the family rich? Who is pleased to see him and who is not? The painting does not change. Your task does, and so does the path your eyes take.")],
    fig=(FIG, 'Try it on yourself. On the left the orange dot finds you. On the right you have to look for the orange circle, because it shares one feature with each of its neighbours.'),
    specs=[('Pop-out', 'A target with one unique basic feature (colour, size, orientation, motion) that is found fast regardless of the crowd.'),
           ('Salience', 'How much something stands out from its surroundings. It biases the first glances; it does not guarantee they mean anything.'),
           ('Inattentional blindness', 'Missing something in plain view because attention is busy with a task. The gorilla.'),
           ('Change blindness', 'Failing to notice a change, even a big one, when it happens during a cut, a blink or a distraction.')],
    philo=dict(q='"The way we see things is affected by what we know or what we believe."', who='John Berger, Ways of Seeing (1972)',
               means='Berger was writing about art and power, but the eye-tracking evidence agrees with him at the level of the eyeball. Viewers bring a task and a set of beliefs, and those decide what they look at and what they never see.',
               argue='If seeing depends on what the viewer already knows, whose knowledge is your safari site designed for: a first-time tourist, a birder or a travel agent?'),
    tags=[('hold', '"People miss big things they are not looking for."', 'About half the viewers counting passes failed to see a gorilla walk through the game.', ('Simons and Chabris 1999', 'https://doi.org/10.1068/p281059')),
          ('part', '"Everyone reads the web in an F."', 'Common on dense text; the same researchers say good layout prevents it.', ('NN/g, F-shaped pattern, 2017 update', 'https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/')),
          ('part', '"The brightest thing always wins attention."', 'Salience biases the first glance; after that the task steers the eyes.', ('Itti and Koch 2000', 'https://doi.org/10.1016/S0042-6989(99)00163-7'))],
    distil=[('Treisman and Gelade 1980, feature integration theory', 'https://doi.org/10.1016/0010-0285(80)90005-5', 'Pop-out versus search'),
            ('Review of Yarbus and task dependence', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3563050/', 'What the famous figure shows, and its limits'),
            ('Simons and Levin 1998, the door study', 'https://doi.org/10.3758/BF03208840', 'Change blindness in a real conversation'),
            ('Wolfe and Utochkin 2018', 'https://doi.org/10.1016/j.copsyc.2018.11.005', 'Why there is no fixed list of pop-out features')],
    writer=dict(notes=["Directors steer attention with exactly these tools: one moving thing in a still frame, one lit face in a dark room, one colour in a grey world. And they hide things the same way. A clue placed in a frame while the audience is busy following a conversation is in plain view and unseen, which is what makes the second viewing feel like a revelation.",
                       "Change blindness is also why continuity is forgiving and why bold cuts work. Viewers track what the story asks them to track. If the scene gives them a task, who is lying, will he notice the gun, you can change almost everything else in the frame."],
                drill='Plan one shot in which an important object is in plain view for the whole shot but will not be noticed on first viewing. Write what the audience is busy watching instead, and what will make them see it later.'),
    biz="Test MTRX\u2122 pages with a task, never with \"what do you think?\" Give a friend five seconds on a lodge homepage and ask one question: how much is a three-night stay in June? Watch where they look and what they miss. Then give each screen one singleton: one orange element that the visitor's task actually needs. If four things are orange, nothing is.",
    tryit='Open one of your own sites on your phone. Set a task (find the price, find the contact number) and time how long it takes you to complete it from a cold start. Then list what you never looked at.',
    room='Attention is a spotlight steered by the task. Design for what people are trying to do, not for how you hope they will look.',
    deeper=[('Greene, Liu and Wolfe 2012', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC2856937/', 'Can you read a task from eye movements? Not reliably'),
            ('Wolfe and Horowitz 2004', 'https://doi.org/10.1038/nrn1411', 'What attracts attention, in a short review')],
    nextq="Attention grabs differences. But what is a design made of in the first place, before colour and type? What can a single line do? Stop 1.4.",
    checks=[dict(q='Why is an orange circle among orange squares and grey circles slow to find?',
                 o=['It shares one feature with each kind of neighbour',
                    'Orange is harder for the eye to see than grey is',
                    'Circles are always noticed more slowly than squares'], a=0,
                 w='A conjunction of features needs focused search. A single unique feature pops out.'),
            dict(q='What did Yarbus show with the Repin painting?',
                 o=['The scan path through a picture changes with the viewer\'s task',
                    'All viewers follow the same fixed path through any picture they see',
                    'People look mostly at the brightest part of any painting'], a=0,
                 w='The scan paths changed with each question. The original was one observer; replications found a smaller effect.'),
            dict(q='What does the NN/g 2017 update say about the F-pattern?',
                 o=['It is common on dense text, and good layout can prevent it',
                    'It is a fixed law of reading that every web page should be built around',
                    'It was disproved, so text layout has no effect on scanning'], a=0,
                 w='The F is a warning about walls of text, not an instruction to put everything top left.')],
)

"""Start stops for No. 03: how the course works, the question bank and the map."""
from svg import box, t, arrow, svg

SUB = ("Why intelligent people join cults, why the group cuts them off from family, why it works, and how a con is built "
       "beat by beat. Every stop starts from a real question, distils the best books on it, and ends in a writer's room.")

CUBE = [('#m1-1', 'What are cults', 'psXook7FyVQ', '1.1'), ('#m1-2', 'Why people join cults', 'kB-dJaCXAxA', '1.2'),
        ('#m1-3', 'The secret language of cults', 'c7wCbbmLtiI', '1.3'), ('#m1-4', 'How to spot a cult', 'fa7uN2vo6rc', '1.4'),
        ('#m1-5', 'Social influence', 'UGxGDdQnC1Y', '1.5'), ('#m1-6', 'Social groups', '_wFZ5Dbj8DA', '1.6'),
        ('#m1-7', 'Cults, explained', '6NWIfiV1_XQ', '1.7'), ('#s3', 'The Master', '1WTM8eO1Oec', '3.9'),
        ('#s4', 'The Sting', '_nAIb_J9T5M', '4.4')]


def spec(n, d):
    return '<div class="spec"><div class="spec-name">%s</div><p class="spec-def">%s</p></div>' % (n, d)


MAP = svg(1100, 470, 'The field map: cults, cons and power share one machinery',
          box(20, 20, 330, 150, 's-box-a') + t(185, 62, 'CULTS', 's-t-d') + t(185, 96, 'groups that capture a life', 's-t-sm') + t(185, 124, 'Files 1, 2, 3', 's-t') +
          box(385, 20, 330, 150, 's-box-a') + t(550, 62, 'CONS', 's-t-d') + t(550, 96, 'stories that capture a decision', 's-t-sm') + t(550, 124, 'Files 4, 5, 6', 's-t') +
          box(750, 20, 330, 150, 's-box-a') + t(915, 62, 'POWER', 's-t-d') + t(915, 96, 'levers that move people', 's-t-sm') + t(915, 124, 'Files 7, 8', 's-t') +
          arrow(185, 172, 420, 268) + arrow(550, 172, 550, 266) + arrow(915, 172, 680, 268) +
          box(150, 272, 800, 170, 's-box-j') + t(550, 312, 'THE SHARED MACHINERY', 's-t') +
          t(550, 348, 'trust that travels through friends \u00b7 small yeses that grow', 's-t-sm') +
          t(550, 378, 'cutting off rival information \u00b7 a story that explains everything', 's-t-sm') +
          t(550, 414, "and underneath it all: the target's own wants", 's-t-b'))

QB = [
    ('File 1 \u00b7 The members', [
        (1, 'Why do really intelligent people fall for cults?', '1.2'), (1, 'What techniques do cults use?', '1.3'),
        (1, 'Why do cults separate people from friends and family?', '1.4'), (1, 'Why do cults work?', '1.5'),
        (1, 'What does belonging in a group do to us?', '1.6'), (1, 'Where does identity come into it?', '1.6'),
        (0, 'What is a cult, really, and why do scholars fight over the word?', '1.1'), (0, 'Can a person choose and be pressured at the same time?', '1.2'),
        (0, 'How do love bombing and loaded language work together?', '1.3'), (0, 'Why does "just send her the facts" usually fail?', '1.4'),
        (0, 'Why do failed prophecies sometimes deepen belief?', '1.5'), (0, 'Can the best years of your life also be abuse?', '1.6'),
        (0, 'What did Jonestown reveal, and what does it not prove?', '1.7')]),
    ('File 2 \u00b7 The leader', [
        (1, 'What motivates the leader?', '2.1'), (1, "What is the leader's personality like?", '2.2'),
        (1, 'Where does the charisma come from?', '2.3'), (1, 'Why do we need leaders at all?', '2.4'),
        (0, 'Do leaders believe their own message?', '2.1'), (0, 'How does a cult begin?', '2.2'),
        (0, 'Why does it so often end in sexual and financial abuse?', '2.2'), (0, 'How does a leader build the "we"?', '2.5'),
        (0, 'What happens when the leader dies, fails or is exposed?', '2.6')]),
    ('File 3 \u00b7 The world around', [
        (1, 'What does the sociological lens add?', '3.1'), (0, 'How do some cults become world religions?', '3.2'),
        (0, 'Is brainwashing real?', '3.3'), (0, 'What did the 1980s cult panic get wrong?', '3.4'),
        (0, 'How does a peaceful group turn violent?', '3.5'), (0, 'Why do people stay when it turns bad, and how do they get out?', '3.6'),
        (0, 'How is it different for children born inside?', '3.7'), (0, 'Where is the line between a cult, an MLM, a startup and a fandom?', '3.8'),
        (0, 'Are online groups the new cults?', '3.8'), (0, 'Why do cults make such gripping films?', '3.9')]),
    ('Files 4 and 5 \u00b7 The con', [
        (0, 'What are the stages of a con?', '4.1'), (0, 'How did Victor Lustig sell the Eiffel Tower?', '4.2'),
        (0, 'Why do smart people fall for cons?', '4.3'), (0, 'How does a film make the audience the mark?', '4.4'),
        (0, "What makes Saul Goodman's slide believable?", '4.5'), (0, 'How do identity cons like Ripley work?', '5.1'),
        (0, 'Is a heist a con?', '5.4'), (0, 'How does social engineering open doors that locks protect?', '5.6')]),
    ('Files 6 and 7 \u00b7 Money and power', [
        (0, 'Ponzi, pyramid or MLM: what is the difference?', '6.2'), (0, 'How did Madoff last for decades?', '6.1'),
        (0, 'Why did nobody stop Theranos or FTX in time?', '6.4'), (0, 'Why do good people cook the books?', '6.5'),
        (0, 'How do pig butchering, task scams and fake clients work?', '6.6'), (0, 'Which persuasion levers survive replication?', '7.1'),
        (0, 'How should I read the 48 Laws of Power?', '7.2'), (0, 'What is coercive control?', '7.3'),
        (0, 'How do frauds get caught?', '7.4'), (0, 'Could I be recruited, and how do I persuade honestly?', '7.5')]),
    ('File 8 \u00b7 The interrogation room', [
        (1, 'What was the KUBARK manual, and what is its Alice in Wonderland technique?', '8.1'), (0, 'Is brainwashing real, and where did the word come from?', '8.2'),
        (0, 'What was MKUltra, and did it find a way to control minds?', '8.3'), (0, 'Does torture or pressure get the truth?', '8.4'),
        (1, 'Did L. Ron Hubbard teach the CIA anything?', '8.5'), (1, 'How did Charles Manson control the Family, and was the CIA behind it?', '8.6')]),
]


def qbank():
    cols = []
    for head, qs in QB:
        lis = ''.join('<li%s>%s<a href="#%s">%s</a></li>' % (' class="kev"' if k else '', q, ('m' + s.replace('.', '-')) if s.startswith('1.') else 's' + s.split('.')[0], s) for k, q, s in qs)
        cols.append('<div class="qb"><h4>%s</h4><ol>%s</ol></div>' % (head, lis))
    return '<div class="qbank">%s</div>' % ''.join(cols)


ROAD = [('1', 'Inside the cult', 'Week 1 \u00b7 7 stops', 'Built: read it now', True), ('2', 'The leader', 'Week 2 \u00b7 7 stops', 'Motive, personality, charisma', False),
        ('3', 'The world around', 'Week 3 \u00b7 9 stops', 'Sociology, violence, leaving, screen', False), ('4', 'The big con', 'Week 4 \u00b7 6 stops', 'Lustig, The Sting, Saul', False),
        ('5', 'Masks and crews', 'Week 5 \u00b7 6 stops', "Ripley, Lupin, Ocean's, real heists", False), ('6', 'Money fraud', 'Week 6 \u00b7 6 stops', 'Madoff, Theranos, FTX, scams', False),
        ('7', 'Power and the reveal', 'Week 7 \u00b7 6 stops', 'Cialdini, investigators, capstone', False),
        ('8', 'The interrogation room', 'Week 8 \u00b7 6 stops', 'KUBARK, MKUltra, Hubbard, Manson', False)]


def road():
    return '<div class="road">%s</div>' % ''.join('<a href="#s%s"%s><span>File %s \u00b7 %s</span><b>%s</b><em>%s</em></a>' % (
        n, ' class="now"' if now else '', n, wk, title, note) for n, title, wk, note, now in ROAD)


STOPS = [
    dict(id='0.1', mins=6, title='Why this course exists',
         why='You told me these subjects are your bread and butter for curiosity, and that work leaves little time for books. So this course does the reading for you: every stop starts from a real question, distils several of the best books and papers on it, and only then turns practical.',
         body=['<div class="mtrx"><p><b>Your why, in your words.</b> You want to be fed great knowledge first, with practical use second. You want the long, everything-important view that Crash Course gives, and you want it longer for the subjects about human behaviour. The questions you asked off the top of your head are the spine of File 1 and File 2. The rest came from the experts.</p></div>',
               '<h3>Five rules</h3><div class="specs">' +
               spec('1 \u00b7 Questions lead', 'Each stop answers one real question. Yours are marked in orange on the question bank. New questions you ask become new stops.') +
               spec('2 \u00b7 One stop, many books', 'The deep answer distils 3 to 5 books, papers or long articles, named and linked. The stop replaces the reading; the books stay optional.') +
               spec('3 \u00b7 Myths get replaced', 'Popular claims carry truth tags: holds up, partly, or myth. When a myth dies, you get the stranger true story in its place.') +
               spec('4 \u00b7 Writer first, business second', "About 60% of the practical layer is a writer's room (character, motive, the beat a scene plays). About 40% is business: red flags and the honest version for MTRX\u2122.") +
               spec('5 \u00b7 Mechanisms, not scripts', 'You learn how cults and cons work, how people get caught in them and how they get out. Nothing here is a recruitment or fraud script, and the drills are fiction or self-reflection.') + '</div>',
               '<h3>A 20-minute day</h3><div class="tbl-wrap"><table class="tbl"><thead><tr><th>Step</th><th>Time</th><th>What you do</th></tr></thead><tbody>'
               '<tr><td>Predict</td><td>2 min</td><td>Answer the cold open and rate how sure you are, 1 to 5</td></tr>'
               '<tr><td>Watch</td><td>6 min</td><td>One video, with three "watch for" cues</td></tr>'
               '<tr><td>Read</td><td>6 min</td><td>The deep answer, the diagram, the truth tags, the writer\'s room</td></tr>'
               '<tr><td>Try it</td><td>5 min</td><td>A short writing or observation task</td></tr>'
               '<tr><td>Check</td><td>1 min</td><td>Three quick checks, then mark the stop done and send progress to the bot</td></tr>'
               '</tbody></table></div><p>Got more time? Every stop ends with an optional <b>Go deeper</b> box of about 15 minutes.</p>'],
         room='Curiosity first: every stop answers a real question, and every answer has a source.'),
    dict(id='0.2', mins=8, title='The question bank and the map',
         why='Here is everything this course answers. Your questions are in orange; the others are the ones a cult researcher, a fraud examiner or a sociologist would add. Each one links to the stop that answers it.',
         body=['<figure class="fig"><div class="scroll">' + MAP + '</div><figcaption>The field map. Cults, cons and power plays look like three subjects, but they run on one machinery. That is why this course teaches them together.</figcaption></figure>',
               '<h3>The question bank</h3>', qbank(),
               '<h3>The road</h3>', road(),
               '<h3>The coverage audit</h3><p>This plan was not built from my memory. Before writing, a bottom-up audit pulled <b>188 concepts</b> from <b>35 sources</b> opened across <b>10 source families</b>: canonical books (Lifton, Barker, Maurer, Konnikova, Davies, Cialdini), university syllabi on new religious movements, white-collar crime and persuasion, the fraud examiners\' exam blueprint, encyclopedia entries, recent research reviews, regulators (FTC, FBI) and cult-recovery practitioners. It also collected <b>73 questions</b> experts ask, and checked 13 lenses (words, mechanisms, numbers, money, rules, people and history, the frontier, and more) for gaps.</p>'
               '<div class="specs">' + spec('What it proves', 'The plan covers what those sources treat as core, and every lens has at least one stop.') +
               spec('What it does not prove', 'That you understand it, that every concept is equally well established, or that no unknown unknowns remain. Your weak spots and new questions fix that over time.') + '</div>',
               '<h3>The optional shelf</h3><p>Every stop distils these, so none of them is homework: Barker, <i>The Making of a Moonie</i> (1984); Lifton, <i>Thought Reform and the Psychology of Totalism</i> (1961); Lalich, <i>Bounded Choice</i> (2004); Stein, <i>Terror, Love and Brainwashing</i> (2017); Montell, <i>Cultish</i> (2021); Maurer, <i>The Big Con</i> (1940); Konnikova, <i>The Confidence Game</i> (2016); Davies, <i>Lying for Money</i> (2018); Carreyrou, <i>Bad Blood</i> (2018); Mercier, <i>Not Born Yesterday</i> (2020).</p>'],
         room='This course answers questions, not chapters. If your question is not on the list, ask it and it becomes a stop.'),
]

SOURCES = [('Barker, New religious movements (LSE)', 'https://researchonline.lse.ac.uk/id/eprint/11887/1/__libfile_REPOSITORY_Content_Barker%2C%20E_New%20religious%20movements_Barker_New%20religious%20movements_2013.pdf', '0.2')]
COLOPHON = '<p class="prepared" style="margin-top:28px">v1.0 \u00b7 23 October 2026 \u00b7 Complete: the Start, Files 1 to 7 and the bonus File 8, 53 stops in all.</p>'

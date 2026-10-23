"""Start stops for No. 07: why the course starts with seeing, what design is, the question bank and the map."""
from svg import box, t, arrow, svg

SUB = ("How a designer actually sees and decides: the brief, the eye, the alphabet of form and value, then the principles, type, colour, "
       "composition, the makers, brand and taste. Every stop starts from a real question, distils the best books on it, and ends with a "
       "director's eye and a studio lens.")

CUBE = [('#m0-1', 'Art versus design', 'dZmkPmfW0XA', '0.1'), ('#m0-2', 'Eames: Design Q and A', 'bmgxDCujTUw', '0.2'),
        ('#m1-1', 'Bierut: think like a designer', 'RanfCx18gi4', '1.1'), ('#m1-2', 'Design thinking is bullsh*t', '_raleGrTdUg', '1.2'),
        ('#m1-3', 'The selective attention test', 'vJG698U2Mvo', '1.3'), ('#m1-4', 'Silhouettes in cinema', 'vqGnhDGnp7A', '1.4'),
        ('#m1-5', 'The elements of art: value', 'fKOJ2T4Die4', '1.5'), ('#s2', 'Composition and framing', 'hUmZldt0DTg', '2.11'),
        ('#s4', 'Colour in Breaking Bad', 'WK-KrQQYqUA', '4.8')]


def spec(n, d):
    return '<div class="spec"><div class="spec-name">%s</div><p class="spec-def">%s</p></div>' % (n, d)


def vid(v, title, who, watch):
    return ('<h3>Watch</h3><div class="watch3"><a class="vid" href="https://www.youtube.com/watch?v=%s" rel="noopener" target="_blank">'
            '<div class="vid-th"><span class="ph">%s</span><img alt="Still from %s" loading="lazy" onerror="this.remove()" src="https://i.ytimg.com/vi/%s/mqdefault.jpg"/>'
            '<span class="play"></span></div><div class="vid-b"><div class="vid-t">%s</div><div class="vid-m">%s</div></div></a>'
            '<div><div class="scene-wh">Watch for</div><ul class="scene-w">%s</ul></div></div>') % (
        v, title, title, v, title, who, ''.join('<li>%s</li>' % w for w in watch))


FIELDS = [(20, 'GRAPHIC AND TYPE', 'posters, pages, letters', 'Parts 2 and 3'), (290, 'BRAND IDENTITY', 'marks, systems, voice', 'Part 7'),
          (560, 'UX AND UI', 'screens you operate', 'Part 7'), (830, 'PRODUCT', 'objects in the hand', 'Part 6')]
FIELDS2 = [(20, 'ARCHITECTURE', 'spaces you walk', 'Part 6'), (290, 'FASHION', 'clothes as a system', 'Part 8'),
           (560, 'MOTION AND TITLES', 'design that moves', 'Parts 3 and 9'), (830, 'FILM: SETS, LIGHT', 'worlds a camera sees', 'Parts 5 and 9')]


def _fbox(x, y, a, b, c):
    return box(x, y, 250, 120, 's-card') + t(x + 125, y + 40, a, 's-t-b') + t(x + 125, y + 70, b, 's-t-sm') + t(x + 125, y + 98, c, 's-t-sm')


MAP = svg(1100, 540, 'The field map: eight design crafts around one shared eye',
          ''.join(_fbox(x, 20, a, b, c) for x, a, b, c in FIELDS) + ''.join(_fbox(x, 400, a, b, c) for x, a, b, c in FIELDS2) +
          ''.join(arrow(x + 125, 144, 380 + i * 113, 206) for i, (x, _, _, _) in enumerate(FIELDS)) +
          ''.join(arrow(x + 125, 396, 380 + i * 113, 336, True) for i, (x, _, _, _) in enumerate(FIELDS2)) +
          box(300, 210, 500, 122, 's-box-a') + t(550, 252, 'THE SHARED EYE', 's-t-d') +
          t(550, 284, 'purpose, attention, value, form', 's-t-sm') + t(550, 312, 'principles, and a test with real people', 's-t-sm'))

QB = [
    ('Your questions', [
        (1, 'How do I choose and pair fonts?', '3.4'), (1, "What is Sanzo Wada's colour dictionary, and how do I use it?", '4.6'),
        (1, 'Is the golden ratio real? And the rule of thirds?', '2.11'), (1, 'Minimal or bold: which is better?', '6.3'),
        (1, 'How do I build a brand identity?', '7.1'), (1, 'What did Apple, Jobs and Ive actually believe?', '6.5'),
        (1, 'How did Caravaggio use light?', '1.5'), (1, "What does Picasso's Bull teach?", '5.4'),
        (1, "Why do Kubrick's symmetrical frames feel the way they do?", '5.1'), (1, 'How do directors steer where I look?', '1.3'),
        (1, 'Which architects should I know, and what did they believe?', '6.7'), (1, 'Modern versus vintage, clothes included: what makes a style?', '8.1'),
        (1, 'Where is the design philosophy in each chapter?', '0.2'), (1, 'How do I actually use this, with real examples?', '1.1')]),
    ('Questions the experts add', [
        (0, 'What problem is the client actually paying to solve?', '1.1'), (0, 'How do designers move from fog to a decision?', '1.2'),
        (0, 'Why do people miss things right in front of them?', '1.3'), (0, 'What can a line do that a word cannot?', '1.4'),
        (0, 'Why do designers squint at their own work?', '1.5'), (0, 'Can beauty make a bad interface feel usable?', '2.9'),
        (0, 'Can one site speak Gujarati, Hindi and English?', '3.5'), (0, 'How much of colour psychology is real?', '4.7'),
        (0, 'How does data become a legible picture?', '5.7'), (0, 'Is it accessible by default?', '7.8'),
        (0, 'Is taste personal, trained or class power?', '8.5'), (0, 'What does an image say beyond what it shows?', '9.1')]),
]
BUILT = ('0.', '1.')


def qbank():
    cols = []
    for head, qs in QB:
        lis = ''.join('<li%s>%s<a href="#%s">%s</a></li>' % (' class="kev"' if k else '', q, ('m' + s.replace('.', '-')) if s.startswith(BUILT) else 's' + s.split('.')[0], s) for k, q, s in qs)
        cols.append('<div class="qb"><h4>%s</h4><ol>%s</ol></div>' % (head, lis))
    return '<div class="qbank">%s</div>' % ''.join(cols)


ROAD = [('1', 'Seeing like a designer', 'Week 1 \u00b7 5 stops', 'Built: read it now', True), ('2', 'Shared principles', 'Weeks 2 and 3 \u00b7 12 stops', 'Hierarchy, Gestalt, grids, the golden ratio', False),
        ('3', 'Type', 'Week 4 \u00b7 7 stops', 'Anatomy, pairing, Tanker and Nunito Sans', False), ('4', 'Colour', 'Weeks 5 and 6 \u00b7 11 stops', 'Theory, Sanzo Wada, film, brand', False),
        ('5', 'Composition, light and image', 'Week 7 \u00b7 8 stops', 'Kubrick, Caravaggio, Picasso, data', False), ('6', 'Philosophies and the makers', 'Week 8 \u00b7 9 stops', 'Bauhaus, Rams, Jobs and Ive, Kahn, Doshi', False),
        ('7', 'Brand identity and digital systems', 'Week 9 \u00b7 9 stops', 'Wheeler, rebrands, UX, accessibility', False), ('8', 'Aesthetics', 'Week 10 \u00b7 8 stops', 'Modern, vintage, clothes, taste', False),
        ('9', 'Storytelling and the capstone', 'Week 11 \u00b7 7 stops', 'Meaning, sequence, your manifesto', False)]


def road():
    return '<div class="road">%s</div>' % ''.join('<a href="#s%s"%s><span>Part %s \u00b7 %s</span><b>%s</b><em>%s</em></a>' % (
        n, ' class="now"' if now else '', n, wk, title, note) for n, title, wk, note, now in ROAD)


FIELDCARDS = ''.join('<div><b>%s</b><span>%s</span></div>' % x for x in [
    ('Graphic design and type', 'Arranges words and images on a surface so the right thing is read first.'),
    ('Brand identity', 'A system of marks, colours, type and voice that stays recognisable for years.'),
    ('UX and UI', 'Designs something people operate: the test is whether they can do the task.'),
    ('Product and industrial', 'Objects in the hand, where form meets materials, cost and the body.'),
    ('Architecture', 'Space you walk through in time, with light, climate and a budget.'),
    ('Fashion', 'Clothes as a design system: silhouette, texture, colour and signal.'),
    ('Motion and titles', 'Design with a clock: rhythm, reveal and sequence.'),
    ('Film: production design and cinematography', 'The world in front of the lens and the way the lens sees it.')])

STOPS = [
    dict(id='0.1', mins=8, title='Why do a safari website and a Kubrick frame need the same eye?',
         why="You build websites for wildlife and safari brands, and you want to direct films. Those look like two careers. Underneath, they use one skill: deciding what a person should see first, what they should feel, and what they should do next. That skill is design, and this course trains the eye before it teaches any style.",
         body=['<div class="mtrx"><p><b>Your brief, in your words.</b> Fonts and pairing first. Colour, with Sanzo Wada\'s combinations. Composition, with the truth about the golden ratio and the rule of thirds. Minimal versus bold. Brand identity. Apple, Jobs and Ive. Caravaggio and Picasso, Kubrick and Spielberg, great architects. And practical use, with real makers, real images and videos. All of it is on the map below.</p></div>',
               '<p>The research added one thing you did not ask for, and it comes first. Thirteen research passes, including two independent gap audits, found that the outline taught <b>what good design looks like</b> and almost nothing about <b>how designers get there</b>: the brief, how attention really works, value before colour, testing and critique. So Part 1 is the loop before the looks.</p>',
               vid('dZmkPmfW0XA', "What's the Difference Between Art and Design?", 'CrashCourse', [
                   'The line the video draws between expressing yourself and solving someone else\'s problem',
                   'Where it admits the line blurs',
                   'One example you could use with a client who says "just make it artistic"']),
               '<figure class="fig"><div class="scroll">' + MAP + '</div><figcaption>Eight crafts, one eye. Each craft has its own tools, but every one of them starts from a purpose, works on attention and value, and is judged by whether real people get what it was for.</figcaption></figure>',
               '<h3>The crafts this course visits</h3><div class="fields">' + FIELDCARDS + '</div>',
               '<h3>Where they split</h3><div class="specs">' +
               spec('Time', 'Film, motion and websites unfold in time; a poster or a painting is seen almost at once. Time adds sequence, reveal and rhythm.') +
               spec('Use', 'A painting is looked at. An interface is operated. Once someone has a task, usability beats beauty when they conflict.') +
               spec('The body', 'Architecture and product meet the body: you walk, hold, sit. Scale and material stop being metaphors.') +
               spec('Years', 'A brand must survive a decade of uses nobody has imagined yet. A film frame only has to work in its scene.') + '</div>',
               '<h3>The road</h3>', road()],
         room='Train the eye first. Every craft after it gets cheaper to learn.'),
    dict(id='0.2', mins=8, title='What is design, if it is not decoration?',
         why='In 1972 the Eames Office answered a list of questions about design on film. The first answer is still the best working definition, and it is the test every stop in this course uses.',
         body=['<div class="philo"><div class="philo-k">Philosophy \u00b7 the definition this course uses</div><blockquote>"One could describe Design as a plan for arranging elements to accomplish a particular purpose."</blockquote>'
               '<p class="philo-who">Charles Eames, Design Q and A (1972) \u00b7 <a href="https://vitra.com/en-us/magazine/details/what-is-your-definition-of-design-monsieur-eames" rel="noopener" target="_blank">Vitra transcript</a></p>'
               '<p>Three words do the work. <b>Plan</b>: design is decided before it is made. <b>Arranging</b>: the designer rarely invents the elements, they order them. <b>Purpose</b>: without one there is nothing to judge the work against, and that is when decoration takes over. In the same film Eames answers "What are the boundaries of Design?" with "What are the boundaries of problems?"</p>'
               '<p class="philo-q"><b>Argue with it.</b> Is a Caravaggio design by this definition? What was its purpose, and who set it?</p></div>',
               vid('bmgxDCujTUw', 'DESIGN Q and A (1972)', 'Eames Office', [
                   'The answer about constraints, and why Eames calls them an ethic',
                   'Whether design is "an expression of the purpose" or of the designer',
                   'The question you would most want to ask him back']),
               '<h3>How a stop works</h3><div class="tbl-wrap"><table class="tbl"><thead><tr><th>Step</th><th>Time</th><th>What you do</th></tr></thead><tbody>'
               '<tr><td>Predict</td><td>2 min</td><td>Answer the cold open and rate how sure you are, 1 to 5</td></tr>'
               '<tr><td>Watch</td><td>6 min</td><td>One video, with three "watch for" cues</td></tr>'
               '<tr><td>Read</td><td>6 min</td><td>The deep answer with real paintings and places (tap <b>Squint test</b> on any image), the diagram, the philosophy box and the truth tags</td></tr>'
               '<tr><td>Use</td><td>5 min</td><td>The director\'s eye for your films, the studio lens for MTRX\u2122, and a Try it task</td></tr>'
               '<tr><td>Check</td><td>1 min</td><td>Three quick checks, then mark the stop done and send progress to the bot</td></tr>'
               '</tbody></table></div>',
               '<h3>Truth tags</h3><ul class="legend"><li><span class="stamp st-hold">Holds up</span>the source supports it</li><li><span class="stamp st-part">Partly</span>real idea, popular version oversold</li>'
               '<li><span class="stamp st-myth">Myth</span>do not teach it as fact</li><li><span class="stamp st-thumb">Rule of thumb</span>a useful studio habit, not science</li>'
               '<li><span class="stamp st-unv">Unverified</span>no primary source found</li></ul>',
               '<h3>Famous lines you will not find here</h3><p>Design is full of quotes nobody can source. These four have no primary source that the research could locate, so the guide uses verified lines instead: "Design is thinking made visual" (credited to Saul Bass), "Design is the silent ambassador of your brand" (Paul Rand), "If you can design one thing, you can design everything" (Massimo Vignelli) and "The details are not the details. They make the design" (Charles Eames). The same goes for the statistic that colour increases brand recognition by 80%: no supporting study was found.</p>',
               '<h3>The question bank</h3><p>Your questions are in orange. Each one links to the stop that answers it; stops not built yet link to their part.</p>', qbank(),
               '<h3>The coverage audit</h3><p>This map was not drawn from memory. Before writing, two independent audits compared it against design school curricula (RISD and Parsons foundation years, the NID Ahmedabad foundation programme, the Bauhaus preliminary course), the tables of contents of the canon (Lidwell, Lupton and Phillips, Dondis, Arnheim, Berger, Norman, Tufte, Block, Albers), practitioner and job standards, and error sources such as accessibility guidelines. Topics that recurred in nine or more sources but were missing became new stops: the brief, perception, value, critique, accessibility, information design and semiotics.</p>'
               '<div class="specs">' + spec('What it proves', 'The plan covers what those sources treat as core, and the gaps they agreed on are now stops.') +
               spec('What it does not prove', 'That you can do it. Taste is trained by making and comparing, which is why every stop ends with a task.') + '</div>',
               '<h3>The optional shelf</h3><p>Every stop distils these, so none of them is homework: Lupton and Phillips, <i>Graphic Design: The New Basics</i>; Lidwell, Holden and Butler, <i>Universal Principles of Design</i>; Arnheim, <i>Art and Visual Perception</i> (1954); Dondis, <i>A Primer of Visual Literacy</i> (1973); Berger, <i>Ways of Seeing</i> (1972); Norman, <i>The Design of Everyday Things</i>; Albers, <i>Interaction of Color</i> (1963); Wheeler, <i>Designing Brand Identity</i> (6th edition, 2024).</p>'],
         room='Design is a plan with a purpose. Decoration is what you get when the purpose goes missing.'),
]

SOURCES = [('Vitra: what is your definition of design, Monsieur Eames?', 'https://vitra.com/en-us/magazine/details/what-is-your-definition-of-design-monsieur-eames', '0.2'),
           ('Eames Foundation: Design Q and A', 'https://eamesfoundation.org/work/design-qa/', '0.2')]

COLOPHON = ('<p class="meta" style="margin-top:22px">No. 07 v0.1 \u00b7 Start and Part 1 built 23 October 2026 \u00b7 Images: public-domain works via Wikimedia Commons, '
            'credited under each plate \u00b7 Film stills are never copied: films are linked and drawn as diagrams.</p>')

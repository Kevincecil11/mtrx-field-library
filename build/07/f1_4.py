from svg import box, t, svg

_inner = ''.join(box(20 + i * 290, 20, 270, 200, 's-card') for i in range(4))
_inner += '<circle cx="155" cy="105" r="12" style="fill:#151515"/>'
_inner += '<path d="M335,150 C390,40 450,170 540,70" style="fill:none;stroke:#151515;stroke-width:6;stroke-linecap:round"/>'
_inner += '<rect x="655" y="55" width="140" height="100" style="fill:#151515"/>'
_inner += ('<path d="M945,80 L1045,80 L1045,170 L945,170 Z" style="fill:#6E7180"/><path d="M945,80 L985,50 L1085,50 L1045,80 Z" style="fill:#BCBFCC"/>'
           '<path d="M1045,80 L1085,50 L1085,140 L1045,170 Z" style="fill:#2F3E46"/>')
_inner += t(155, 196, 'POINT: a place', 's-t-b') + t(445, 196, 'LINE: a movement', 's-t-b') + t(735, 196, 'PLANE: an area', 's-t-b') + t(1025, 196, 'FORM: a volume', 's-t-b')
_inner += ''.join(box(20 + i * 385, 250, 365, 200, 's-box-j') for i in range(3))
_inner += '<circle cx="110" cy="350" r="55" style="fill:#ED691D"/>'
_inner += '<rect x="450" y="295" width="110" height="110" style="fill:#2F3E46"/>'
_inner += '<path d="M845,405 L900,295 L955,405 Z" style="fill:#A44A3F"/>'
_inner += t(270, 330, 'CIRCLE', 's-t-b') + t(270, 360, 'soft, whole, safe', 's-t-sm')
_inner += t(655, 330, 'SQUARE', 's-t-b') + t(655, 360, 'stable, solid, still', 's-t-sm')
_inner += t(1060, 330, 'TRIANGLE', 's-t-b') + t(1060, 360, 'direction, tension', 's-t-sm')
FIG = svg(1180, 470, 'The visual alphabet: point, line, plane and form, and the three basic shapes with the feelings designers attach to them', _inner)

STOP = dict(
    id='1.4', day=4, title='What are point, line, plane, shape and form doing?',
    q='Before colour, type or photos, every design is made of a few dumb ingredients: dots, lines, flat areas, shapes, volumes. Can they really carry feeling on their own?',
    why="Most people describe designs by their content: a leopard, a headline, a price. Designers learn to see underneath, at the marks themselves, because that is where a lot of the feeling lives. A jagged line feels different from a slow curve before you know what either one depicts. This alphabet is what Kandinsky and Klee taught at the Bauhaus, and it is what animators and directors still use when they design a silhouette.",
    case=dict(k='Case file', name='Kandinsky, Point and Line to Plane', role='Bauhaus book number 9, 1926, from his teaching at the Bauhaus',
              facts=[('Chapters', 'Point, line, the basic plane'),
                     ('The claim', 'Each element carries a force; arrangement creates tension and counterforce'),
                     ('The partner', "Paul Klee's Pedagogical Sketchbook, 1925: drawing as movement"),
                     ('Status', "A maker's grammar, not experimental psychology")],
              stamp=('part', 'Partly: a grammar, not a law')),
    cold=dict(q='Two made-up words: bouba and kiki. Two shapes: one round and blobby, one spiky like a star. Which word belongs to which shape? Now guess: would people in Japan, Brazil and Romania mostly agree with you?',
              a='Almost everyone calls the round one bouba and the spiky one kiki. Wolfgang Köhler noticed a version of this in 1929, and in 2001 V. S. Ramachandran and Edward Hubbard gave it the names bouba and kiki. In 2021 a team led by Aleksandra Ćwiek tested speakers of 25 languages, from nine language families and ten writing systems, and found strong evidence for the effect across them. Shape and sound share a feeling that does not depend on your alphabet. That is the ground shape language stands on.'),
    video=dict(id='vqGnhDGnp7A', title='How silhouettes are used in cinema', who='CinemaHow',
               watch=['Which silhouettes you can recognise with no detail at all',
                      'How shape alone tells you who is dangerous',
                      'One shot you could rebuild with a single light behind the actor']),
    story=["Kandinsky taught at the Bauhaus from 1922, and in 1926 he published his course as Point and Line to Plane. Its structure is almost comically simple: a chapter on the point, one on the line, one on the basic plane, the flat surface everything sits on. His argument was that each element carries a force. A point is rest, a place. A line is a point set in motion, with direction and speed. A plane is a field of tensions, where a mark near the edge feels different from the same mark in the centre. Composition, for Kandinsky, is arranging those forces against each other.",
           "Paul Klee, his colleague, taught the same alphabet as time. His Pedagogical Sketchbook (1925) begins with a line going for a walk for its own sake, and then shows lines that bound planes, lines that balance, lines that fall. Klee asks not what a line represents but what action made it and what action it invites. That question is why his teaching still matters to animators, to camera movement and to interface designers: a swipe, a pan and a pencil stroke are all lines with a speed.",
           "Look at Kandinsky's Composition VIII from 1923, painted the year after he joined the Bauhaus. There is no subject to hide behind. Big circles sit heavy in the upper left; sharp triangles and crossing lines carry energy across the canvas; small dots pin points of rest. You can feel tension and calm without being able to name a single object, which is exactly what he wanted you to notice. Kandinsky went further and tried to make it a science: in 1923 he handed out a Bauhaus questionnaire asking people to colour a triangle, a square and a circle, expecting yellow, red and blue. Treat that as a hypothesis from a great painter, not as a law.",
           "The bouba and kiki evidence is where the alphabet meets science. Round shapes go with soft, rounded sounds and spiky shapes with sharp ones, across languages and writing systems. Animators turned that into shape language: the circle reads as soft, safe and friendly; the square as stable, solid and sometimes dull; the triangle as direction, tension and threat. It is a rule of thumb, not physics, but it works because it rides on correspondences that seem to be widely shared. Hokusai's Great Wave uses all of it: the claw-like triangles of foam, the huge enveloping curve, and Mount Fuji as a small, calm triangle at rest in the distance.",
           "Form is the last letter: a shape given volume by light, shading and perspective. Designers move between all five constantly. An icon is a shape that must survive being shrunk to a point. A logo has to work as a silhouette. A website hero is a plane with a few strong lines across it. When a design feels muddy, the problem is often here, below colour and type: too many weak marks and no strong ones."],
    plates=[dict(key='kandinsky', after=2, cap="Kandinsky's Composition VIII (1923). Circles, triangles, lines and points with no subject at all. Tap Squint test: the big masses that survive the blur are the ones carrying the composition."),
            dict(key='wave', after=3, cap="Hokusai's Under the Wave off Kanagawa. Triangles of spiky foam for threat, one vast curve for power, and Mount Fuji as a tiny stable triangle. The shapes tell the story before you find the boats.")],
    fig=(FIG, 'The visual alphabet. Top: the four basic elements. Bottom: the shape language animators and designers use, a strong habit rather than a law.'),
    specs=[('Point, line, plane', "Kandinsky's three elements: a place, a movement, an area. Form adds volume."),
           ('Shape language', 'Using circles, squares and triangles to suggest character: soft, stable or dangerous.'),
           ('Silhouette', 'A shape read with no internal detail. If a character or a logo works in silhouette, it will work almost anywhere.'),
           ('Visual weight', 'How strongly a mark pulls the eye: size, darkness, edge sharpness and isolation all add weight.')],
    philo=dict(quote=False, q='Klee taught drawing as time: a line is the trace of a movement, so ask what action made it and what action it invites.',
               who='Paul Klee, Pedagogical Sketchbook (1925)', src=('Bauhaus archive', 'https://www.bauhaus.de/en/research/publications/bauhausbuecher-2-paul-kleepedagogical-sketchbook/'),
               means='Seen this way, design is choreography. The line of a horizon, a scrolling page and a camera pan all have speed and direction, and the viewer feels them in the body.',
               argue='Is a straight line ever neutral, or does it always carry the action of the hand or machine that made it?'),
    tags=[('part', '"A line is a dot that went for a walk."', "A popular paraphrase of the opening of Klee's Pedagogical Sketchbook, not his exact words.", ('Klee, Pedagogical Sketchbook, 1953 English edition', 'https://archive.org/details/pedagogical-sketchbook-klee-1953')),
          ('hold', '"Round sounds go with round shapes."', 'Bouba and kiki matched shapes across speakers of 25 languages and 10 writing systems.', ('Ćwiek et al. 2021', 'https://doi.org/10.1098/rstb.2020.0390')),
          ('part', '"Yellow triangle, red square, blue circle is the true match."', "Kandinsky's 1923 Bauhaus questionnaire looked for it; it is a hypothesis, not a measured law.", ('Getty: Bauhaus form and colour', 'https://www.getty.edu/research/exhibitions_events/exhibitions/bauhaus/new_artist/form_color/interactive/'))],
    distil=[('Bauhaus archive: Point and Line to Plane', 'https://www.bauhaus.de/en/research/publications/bauhausbuecher-9-wassily-kandinsky-point-and-line-to-plane/', "Kandinsky's elements and forces"),
            ('Kandinsky, Point and Line to Plane, full text (1947 English edition)', 'https://archive.org/details/pointlinetoplane00kand', 'Read his chapter on the point'),
            ('Ćwiek et al. 2021, bouba and kiki across cultures', 'https://doi.org/10.1098/rstb.2020.0390', 'The strongest cross-cultural test so far'),
            ('Guggenheim: Composition 8', 'https://www.guggenheim.org/artwork/1924', 'The painting and its Bauhaus moment')],
    writer=dict(notes=["Directors design silhouettes on purpose. Backlight an actor in a doorway and the audience reads only shape: posture, hat, the line of a weapon. A strong silhouette carries character before a face appears, which is why heroes, villains and monsters are drawn and lit to be recognisable in black alone.",
                       "Lines in a frame move too. A horizon, a road, a corridor or a staircase is a line the eye travels along, and its direction sets the energy of the shot: level and wide for calm, steep diagonals for unease, a vanishing point for pull."],
                drill='Sketch one character from your film idea as a pure black silhouette. Show it to someone with no explanation and ask what kind of person it is. Change one shape and ask again.'),
    biz="Run the silhouette test on every MTRX\u2122 mark and icon: fill it solid black and shrink it to favicon size, 16 pixels. If it still reads, it will survive an app bar, a vehicle decal and a stamp on a safari brochure. For lodge and wildlife brands, choose a shape language on purpose: soft circles for family lodges, steadier squares for conservation trusts, sharper angles for adventure operators.",
    tryit='Draw three thumbnails of a safari website hero using only one circle, one square and one triangle each time, no text. Ask a friend which one feels calmest and which feels most adventurous, and why.',
    room='Feeling starts below the content: in the marks, their direction and their weight.',
    deeper=[('Paul Klee, Pedagogical Sketchbook (1953 translation)', 'https://archive.org/details/pedagogical-sketchbook-klee-1953', 'The line on a walk, in his own diagrams'),
            ('Getty: Kandinsky\'s questionnaire and the Bauhaus', 'https://www.getty.edu/research/exhibitions_events/exhibitions/bauhaus/new_artist/form_color/interactive/', 'Try the questionnaire yourself')],
    nextq='Squint at the Hokusai and most of the detail disappears, but the picture survives. What is left, and why do designers trust it more than colour? Stop 1.5.',
    checks=[dict(q="What were Kandinsky's three basic elements in his 1926 Bauhaus book?",
                 o=['Point, line and the basic plane',
                    'Colour, texture and the pattern grid',
                    'Hue, value and the colour wheel'], a=0,
                 w='Point and Line to Plane has chapters on the point, the line and the basic plane.'),
            dict(q='What did the 2021 study of bouba and kiki in 25 languages find?',
                 o=['Strong evidence that the match holds across languages and scripts',
                    'The effect appears only for speakers who grew up reading the Roman alphabet',
                    'People pair the words with shapes at random once tested fairly'], a=0,
                 w='Roman-script readers were only marginally more likely to show it. The effect did not depend on the shape of letters.'),
            dict(q='How should a designer treat shape language, such as triangles meaning danger?',
                 o=['As a strong rule of thumb, to test on real viewers',
                    'As a proven law of perception that works the same everywhere',
                    'As a myth with no connection to how people perceive shapes'], a=0,
                 w='It rides on real shape and sound correspondences, but context and culture still change the reading.')],
)

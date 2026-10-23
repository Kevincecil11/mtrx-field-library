from svg import box, t, svg

_V = ['#FFFFFF', '#D9D9D9', '#B3B3B3', '#8C8C8C', '#666666', '#404040', '#000000']
_inner = t(590, 34, 'A VALUE SCALE: LIGHTNESS ONLY, NO HUE', 's-t')
_inner += ''.join('<rect x="%d" y="50" width="150" height="80" style="fill:%s;stroke:#BCBFCC;stroke-width:1.5"/>' % (55 + i * 155, c) for i, c in enumerate(_V))
_inner += t(130, 152, 'white', 's-t-sm') + t(1060, 152, 'black', 's-t-sm')
_inner += box(20, 180, 560, 250, 's-card') + box(600, 180, 560, 250, 's-card')
_inner += t(300, 216, 'MARS ORANGE AND ITS GREY TWIN', 's-t-b')
_inner += '<rect x="70" y="236" width="200" height="120" rx="10" style="fill:#ED691D"/><rect x="330" y="236" width="200" height="120" rx="10" style="fill:#919191"/>'
_inner += t(170, 380, '#ED691D', 's-t-sm') + t(430, 380, 'same lightness, #919191', 's-t-sm')
_inner += t(300, 412, 'Hue changes; value, the thing legibility needs, does not', 's-t-sm')
_inner += t(880, 216, 'THE SAME ORANGE AS TEXT', 's-t-b')
_inner += '<rect x="640" y="236" width="230" height="120" rx="10" style="fill:#FFFFFF;stroke:#BCBFCC;stroke-width:1.5"/>'
_inner += '<text x="755" y="304" text-anchor="middle" style="font-size:22px;font-weight:800;fill:#ED691D">Book a safari</text>'
_inner += '<rect x="890" y="236" width="230" height="120" rx="10" style="fill:#ED691D"/>'
_inner += '<text x="1005" y="304" text-anchor="middle" style="font-size:22px;font-weight:800;fill:#000000">Book a safari</text>'
_inner += t(755, 380, 'on white: 3.16 to 1', 's-t-sm') + t(1005, 380, 'black on orange: 6.64 to 1', 's-t-sm')
_inner += t(880, 412, 'Body text needs 4.5 to 1. Only the right one passes', 's-t-sm')
FIG = svg(1180, 450, 'A value scale, the MTRX orange beside a grey of equal lightness, and orange text on white versus black text on orange with their contrast ratios', _inner)

STOP = dict(
    id='1.5', day=5, title='Why do designers squint?',
    q='Painters, art directors and cinematographers all squint at their own work, or look at it in black and white. What are they checking for that colour hides?',
    why="Value means lightness: how light or dark something is, with the colour taken away. It is the least glamorous idea in design and one of the most powerful. Value decides what reads first, whether text is legible, whether a photo has depth, and whether a dark-mode site works at all. Get value right and almost any palette will hold. Get it wrong and the most beautiful colours turn to mud. Caravaggio built a revolution on it.",
    case=dict(k='Case file', name='Arthur Wesley Dow and notan', role='American painter and teacher at Pratt Institute and Columbia\'s Teachers College; author of Composition (1899)',
              facts=[('The book', 'Composition: A Series of Exercises in Art Structure, 1899'),
                     ('Three powers', 'Line, notan (the pattern of dark and light), and colour'),
                     ('The source', 'Ideas he adapted from Japanese prints and brought into American art schools'),
                     ('The students', "Among them Georgia O'Keeffe")],
              stamp=('hold', 'Holds: value carries the picture')),
    cold=dict(q="MTRX\u2122's brand orange is #ED691D. Predict: is orange body text on a white page readable enough to pass the web's accessibility standard? And what about black text on an orange button?",
              a="Orange text on white comes out at about 3.16 to 1 in the standard contrast formula. That passes for large headings and for buttons, which need 3 to 1, but fails for body text, which needs 4.5 to 1. On your warm canvas colour #ECEAE4 it drops to about 2.63 to 1 and fails even for headings. Black on the orange scores about 6.64 to 1 and passes easily. The formula ignores hue completely. It measures only relative luminance, which is value. That is the whole lesson of this stop in one number."),
    video=dict(id='fKOJ2T4Die4', title='The Elements of Art: Value', who='Drawing and Painting, The Virtual Instructor',
               watch=['How a value scale is built, and how many steps the eye can use',
                      'Why value, not colour, creates the illusion of form',
                      'One value trick you could use on a website hero photo']),
    story=["Start with the eye, because this is physics as much as art. Your visual system carries fine detail, edges and depth mostly through a lightness signal, and colour through lower-resolution channels. Engineers exploit this every day: JPEG images and most video store colour at lower resolution than lightness, and almost nobody notices. The neuroscientist Margaret Livingstone showed what happens when two colours have the same lightness: edges wobble, depth flattens, shapes become hard to hold. She uses Monet's Impression, Sunrise as an example, where the orange sun has almost the same lightness as the grey sky around it and seems to shimmer.",
           "That is why designers squint. Squinting blurs detail and weakens colour, leaving the big masses of light and dark. If the most important thing is still the first thing you see when you squint, your hierarchy is working. If two things fight, or the subject dissolves into the background, no colour choice will save it. Turning a design grey does the same job more precisely. It is a studio rule of thumb, not a scientific test, but it is one of the oldest and most reliable in the trade.",
           "Arthur Wesley Dow gave the idea a name for American art schools. In Composition (1899) he taught three powers of design, line, notan and colour, and used notan, a Japanese word, for the pattern of dark and light masses. His students made the same picture again and again in two values, then three, before they were allowed colour. The point was to find the arrangement of masses that holds the whole picture, then let colour decorate a structure that already works.",
           "Caravaggio is the extreme case. In The Calling of Saint Matthew (1599 to 1600), painted for a chapel in Rome, most of the canvas is near black. A single shaft of light enters from the right, following Christ's pointing hand, and falls on the faces of the men at the table. Italian has a word for this, chiaroscuro, light and dark; its most dramatic form is called tenebrism. Look at the plate in grey and in two values: the story survives almost intact. Light is doing the work of a headline, telling you where to look and who matters.",
           "On a screen, value is also an accessibility question. The Web Content Accessibility Guidelines measure text contrast with a formula based on relative luminance, which is value, and nothing else. Normal text needs at least 4.5 to 1; large text and interface parts need 3 to 1. Two colours that look vividly different can fail completely if their lightness is close, which is why orange on white is a trap and why white text over a bright savannah photo needs a dark gradient behind it. Squint at your own site: if you can still read it, many more people can."],
    plates=[dict(key='caravaggio', after=3, cap="Caravaggio's The Calling of Saint Matthew, in colour, in grey and in two values. Even in two values you can find Christ's hand, the beam of light and the man it falls on. That is a composition built on value first.")],
    fig=(FIG, 'Value in three views: a lightness scale, your brand orange beside a grey of equal lightness, and the same orange as text. Contrast follows value, not hue.'),
    specs=[('Value', 'How light or dark a colour is, with hue and saturation ignored. Also called lightness or tone.'),
           ('Notan', "Dow's term for the pattern of dark and light masses in a design, studied in two or three values."),
           ('Chiaroscuro', 'Strong modelling with light and shade. Its most extreme form, near-black with a spotlight, is tenebrism.'),
           ('Contrast ratio', 'The WCAG measure of luminance difference between text and background, from 1 to 1 up to 21 to 1.')],
    philo=dict(quote=False, q='Dow taught that composition means putting together lines, masses and colours into a harmony, and that the dark-light pattern, notan, carries the whole before any detail.',
               who='Arthur Wesley Dow, Composition (1899)', src=('Project Gutenberg edition', 'https://www.gutenberg.org/files/45410/45410-h/45410-h.htm'),
               means='Structure first, surface second. Colour is chosen to serve a value pattern that already works, not to rescue one that does not.',
               argue='Some painters, Matisse among them, built pictures from colour with value pushed flat. Is "value first" a law or a taste?'),
    tags=[('myth', '"Notan is a Japanese word for good design."', 'Dow used it for the pattern of dark and light masses, a tool for structure.', ('Dow, Composition, Project Gutenberg', 'https://www.gutenberg.org/files/45410/45410-h/45410-h.htm')),
          ('hold', '"Contrast for reading is about lightness, not hue."', 'WCAG contrast is computed from relative luminance alone.', ('W3C: understanding contrast (minimum)', 'https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html')),
          ('thumb', '"The squint test proves a design works."', 'It checks the big masses. It says nothing about screen readers, keyboards or colour vision.', ('W3C: WCAG overview', 'https://www.w3.org/WAI/standards-guidelines/wcag/'))],
    distil=[('Dow, Composition (1899), Project Gutenberg', 'https://www.gutenberg.org/files/45410/45410-h/45410-h.htm', 'Line, notan and colour, with his exercises'),
            ('W3C: understanding contrast (minimum)', 'https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html', 'Why 4.5 to 1, and how it is computed'),
            ('Wolfe and Horowitz 2004', 'https://doi.org/10.1038/nrn1411', 'Luminance among the features that guide attention')],
    writer=dict(notes=["Cinematographers think in value before colour. A scene lit for mood is a value map: where the brightest point sits, how much of the frame falls into black, whether faces separate from walls. Film noir is Dow's notan with a camera, and Caravaggio's beam of light is a lighting plan any gaffer would recognise.",
                       "Grade or preview your shots in black and white. If the story still reads (who matters, where to look, what is hidden) the colour grade can only add to it. If it does not, more saturation will not help."],
                drill="Pick a still from your favourite film's opening scene. Squint at it, then sketch it in three values only: white, grey, black. Mark the brightest point and say why the director put it there."),
    biz="Make value checks part of every MTRX\u2122 handoff. Keep Mars Orange for large headings, buttons and accents, never for body text on white or canvas; set text in black or graphite (#6E7180 on white is 4.84 to 1, which passes). Put a dark gradient under any white text on a wildlife photo. Then turn the phone's greyscale setting on and check the hero, the price and the booking button still read first.",
    tryit="Turn on greyscale on your phone (accessibility settings) and open one of your sites and one competitor's. Squint at each. Write down what you see first in each, and whether it is the thing the brief says should win.",
    room='Value first. If it works in grey, colour can only make it better.',
    deeper=[('Getty: Bauhaus form and colour', 'https://www.getty.edu/research/exhibitions_events/exhibitions/bauhaus/new_artist/form_color/interactive/', 'How the Bauhaus taught colour after structure'),
            ('W3C: WCAG overview', 'https://www.w3.org/WAI/standards-guidelines/wcag/', 'The whole accessibility standard, briefly')],
    nextq="You can now see hierarchy, attention, marks and value. Part 2 asks the question every one of these stops has been circling: what does your eye see first, and who chose that? Stop 2.1.",
    checks=[dict(q='Why does a squint test help a designer?',
                 o=['It blurs detail and colour, leaving the masses of light and dark',
                    'It shows exactly where a typical visitor will look first and last',
                    'It proves that a design meets the web accessibility standard'], a=0,
                 w='It is a rule of thumb for value and hierarchy, not a measure of real gaze or accessibility.'),
            dict(q='MTRX orange on white scores about 3.16 to 1. Where can you use it?',
                 o=['Large headings and buttons, but not body text',
                    'Anywhere, because orange is a strong and vivid hue',
                    'Nowhere on a website, because it fails every test'], a=0,
                 w='Body text needs 4.5 to 1. Large text and interface parts need 3 to 1.'),
            dict(q='What did Dow mean by notan?',
                 o=['The pattern of dark and light masses in a design',
                    'A Japanese ideal of perfect simplicity, emptiness and calm',
                    'The order in which colours should be applied'], a=0,
                 w='Notan is the arrangement of dark and light, studied in two or three values before colour.')],
)

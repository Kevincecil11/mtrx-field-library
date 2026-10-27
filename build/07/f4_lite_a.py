IMAGES = {
    'p41_newton': dict(
        file="File:Newton's colour circle.png",
        credit='Isaac Newton, colour circle from Opticks, 1704 or 1730 edition',
        lic='Public domain',
        alt='A circular diagram dividing the spectrum into coloured sectors with white at the centre.'),
    'p41_goethe': dict(
        file='File:Qubodup-GoetheFarbkreis en.svg',
        credit='Dbachmann and qubodup, Goethe colour wheel, 2014, after Goethe',
        lic='CC BY-SA 3.0',
        alt='A translated diagram of Goethe\'s colour wheel linking colours with human qualities.'),
    'p42_munsell': dict(
        file='File:Atlas of the Munsell color system.djvu',
        credit='Albert Henry Munsell, Atlas of the Munsell Color System',
        lic='Public domain',
        alt='A scanned atlas page showing Munsell colour samples organised as a colour system.'),
    'p43_chevreul': dict(
        file='File:The laws of contrast of colour (IA lawsofcontrastof00chev).pdf',
        credit='M. E. Chevreul, The Laws of Contrast of Colour, 1839 scan',
        lic='Public domain',
        alt='A scanned nineteenth-century book on adjacent colours and simultaneous contrast.'),
    'p44_whistler': dict(
        file='File:Whistler-Nocturne in black and gold.jpg',
        credit='James McNeill Whistler, Nocturne in Black and Gold: The Falling Rocket, c. 1875, Detroit Institute of Arts',
        lic='Public domain',
        alt='A mostly black nocturne with small gold sparks and a smoky vertical atmosphere.'),
    'p44_starry': dict(
        file='File:Van Gogh - Starry Night - Google Art Project.jpg',
        credit='Vincent van Gogh, The Starry Night, 1889, Museum of Modern Art',
        lic='Public domain',
        alt='A night landscape dominated by deep blue, with swirling lighter blue and yellow stars.'),
    'p45_itten': dict(
        file='File:Farbkreis Itten 1961.svg',
        credit='SidShakal, vector version of Johannes Itten\'s 1961 colour circle',
        lic='Public domain',
        alt='A twelve-part colour circle based on Johannes Itten\'s 1961 model.'),
}

STOPS = [
    dict(
        id='4.1',
        title='What is colour before it is a design choice?',
        q='Is colour in the object, in the light, or in the eye that interprets both?',
        why='Before a palette becomes a mood board, it is a physical event: light meets a surface, then a visual system makes an estimate. That sounds abstract until a screen colour fails in print, or a lodge wall changes under sunset. Learn the chain first and every later wheel becomes a tool rather than a superstition.',
        plates=[
            dict(key='p41_newton', cap='Newton\'s circle is a historical map of spectral sectors and mixtures, not a modern perceptual coordinate system. Notice the unequal wedges: the spectrum is continuous, while the labels are chosen.'),
            dict(key='p41_goethe', cap='Goethe used a wheel to connect colour with appearance and human experience. It is valuable as a record of observation and symbolism, but it did not replace Newtonian optics.')
        ],
        story=[
            'Start with light. A source has a distribution of wavelengths. A surface absorbs some of that light and reflects or scatters the rest. The eye receives the result, and the brain estimates a stable surface colour from an ambiguous scene. That is why colour is not simply a property sitting inside a mango or a button. Change the lamp, paper, background or display and the appearance can move. Newton\'s prism work, published in <i>Opticks</i> in 1704, showed that white sunlight can be dispersed into a visible spectrum. His circular diagram was a powerful historical invention, not proof that nature contains seven neat colour boxes.',
            'The eye begins with three broad, overlapping cone classes, usually called L, M and S. They are not three little RGB sensors. Their signals are then compared in opponent channels, including red against green, blue against yellow, and light against dark. The two descriptions fit together: cones provide an early encoding, while later comparisons help explain afterimages and contrast. This is also why two physically different spectra can match under one illuminant, then fail to match under another. The technical name is <i>metamerism</i>. A hex code is a device instruction, not a universal physical colour.',
            'Now separate the two mixing jobs. <b>Additive mixing</b> combines emitted light, so red, green and blue channels can add toward white in an idealised display. <b>Subtractive mixing</b> uses colourants, filters or inks that remove parts of the illuminating light. Cyan, magenta and yellow are useful print primaries, with black in CMYK for economy and dark detail. Real pigments and inks have messy spectra, so textbook mixtures are approximations. Traditional red, yellow and blue wheels remain useful teaching maps, but they are not universal physical primaries.',
            'For a website, specify display colour in a managed RGB or CSS space, then check it on real devices. For print, use a profile, proof and viewing condition. For a film frame, separate production design, light, camera capture and grade: they are four different chances to change the colour. The director\'s practical question is not what blue means in general. Ask what light, material and contrast make this blue do its job here. The honest limit is that colour constancy makes the world usable, but never perfectly stable.'
        ],
        look=[
            ('Newton\'s Opticks colour circle', 'Look for the difference between a historical spectral diagram and a modern wheel. It places physical dispersion beside a chosen circular order.', 'https://commons.wikimedia.org/wiki/File:Newton%27s_colour_circle.png'),
            ('Goethe\'s colour wheel', 'Compare its emphasis on experience and symbolic oppositions with Newton\'s account of light. Do not treat the two as rival screen colour spaces.', 'https://commons.wikimedia.org/wiki/File:Qubodup-GoetheFarbkreis_en.svg'),
            ('The Dress, 2015', 'The same photograph exposes different assumptions about illumination. It is a useful warning about colour constancy, not evidence that colour is arbitrary.', 'https://www.cell.com/current-biology/fulltext/S0960-9822(15)00594-1'),
            ('StudioBinder, Color Theory in Film', 'Use the practical HSB primer, but remember that brightness in a filmmaking interface is not the whole of colour perception.', 'https://www.studiobinder.com/filmmaking-techniques-color-theory-in-film/')
        ],
        steal=[
            'Write a palette note as a production condition: source, surface, surround, display or print target, and intended contrast.',
            'Keep separate tokens for screen RGB, print references and material samples. Never promise that a hex swatch is the paint.',
            'Make a grayscale thumbnail before tuning hue. If the subject disappears in value, more saturation is not a rescue.'
        ],
        director='Treat colour as a chain of decisions from set light to grade. A warm practical lamp and a cool window can make a relationship visible before a single line of dialogue explains it.',
        studio='For a safari or clinic site, test the same accent under warm phone settings, daylight and a printout. Document which version is the source of truth for interface, social image and physical sign.',
        sources=[
            ('Newton Project, Opticks, Book I, Part II', 'https://www.newtonproject.ox.ac.uk/view/texts/normalized/NATP00034'),
            ('Conway et al., Color vision review', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6345392/'),
            ('Shevell and Martin, Color opponency', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6022826/'),
            ('W3C, CSS Color Module Level 4', 'https://www.w3.org/TR/css-color-4/'),
            ('Smithson, colour constancy review', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC1609194/')
        ]
    ),
    dict(
        id='4.2',
        title='Which three knobs do you actually turn?',
        q='When a colour feels wrong, is the problem its family, its intensity, or its lightness?',
        why='A named colour is too vague to hand to a developer, cinematographer or printer. Hue, chroma or saturation, and value or lightness turn a feeling into adjustable coordinates. Once you can move one knob at a time, you can diagnose why a palette is muddy, loud, unreadable or accidentally flat.',
        plates=[dict(key='p42_munsell', cap='Munsell arranges colour around three practical dimensions: hue, value and chroma. The branching shape matters: real colour does not fit a perfectly even cylinder because pigments reach different chroma limits.')],
        story=[
            '<b>Hue</b> is the family relationship: orange, green, violet, or a position between names. <b>Chroma</b> is colourfulness relative to a reference, while <b>saturation</b> is a term that changes meaning between models and is often used as a proportional purity measure. <b>Value</b> is the light-dark scale familiar in painting. <b>Lightness</b> is a perceptual quantity in colour models. <b>Brightness</b> can describe a display or a sensation. These words overlap in casual software talk, but they are not interchangeable when a precise match matters.',
            'Munsell\'s system made hue, value and chroma a useful language for art and materials. Its value axis is especially practical: convert a frame or landing page to grayscale and see whether the subject, headline and call to action still separate. A vivid orange can vanish if its value is too close to the background. A quiet grey can carry the hierarchy if its value is right. This is a priority, not a law. Hue and chroma still matter for identity, grouping and story, and skin or animal colour can be materially important.',
            'For the web, OKLCH gives a more predictable working space for generating steps. L is lightness, C is chroma, and H is hue. Hold a hue steady and move L to make a text scale; lower C to create quiet surfaces; shift H only when the relationship needs it. CSS Color 4 supports modern Lab, LCH, OKLab and OKLCH functions, but browser support, gamut mapping and the viewer\'s display still matter. An OKLCH number is a design coordinate, not a guarantee that every person sees the same patch.',
            'Use a two-pass workflow. First make a five-step value ladder in grayscale: background, surface, structure, text, accent. Then restore hue and chroma, checking contrast and gamut. In a film still, sample dominant, supporting and accent colours only as approximate screen values because grade, compression and display profile intervene. In a brand system, name semantic jobs such as surface warm, text strong and action accent, then store the numeric values and the conditions under which they were approved.'
        ],
        look=[
            ('Munsell, Atlas of the Munsell Color System', 'Notice how chroma branches outward unevenly instead of forming a perfect regular wheel. Material colour has limits.', 'https://commons.wikimedia.org/wiki/File:Atlas_of_the_Munsell_color_system.djvu'),
            ('OKLab and OKLCH by Björn Ottosson', 'The article shows why a perceptual working space can be useful for image and interface manipulation, while remaining an approximation.', 'https://bottosson.github.io/posts/oklab/'),
            ('CSS Color Module Level 4', 'Look up the OKLCH syntax and gamut discussions before shipping wide-gamut CSS. The specification is the implementation reference.', 'https://www.w3.org/TR/css-color-4/'),
            ('WCAG 2.2 contrast minimum', 'Contrast is a relationship between foreground and background, not a property of a brand swatch in isolation.', 'https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html')
        ],
        steal=[
            'Build every palette as a value ladder first, then choose hue and chroma within each semantic role.',
            'Use OKLCH to generate UI steps, but test sRGB fallbacks, gamut mapping and real screens before approval.',
            'Label saturation in a handoff with the exact colour model. If the job is perceptual colourfulness, say chroma.'
        ],
        director='A director can preserve a character\'s hue while lowering chroma as a world becomes exhausted, or keep the hue quiet and let value isolate a face. Ask which knob changed between shots.',
        studio='For MTRX, make Mars Yellow #ED691D an action accent, not a universal decoration. Pair it with a tested value contrast and a quieter chroma scale for cards, maps and clinic information.',
        sources=[
            ('Munsell, Atlas scan on Commons', 'https://commons.wikimedia.org/wiki/File:Atlas_of_the_Munsell_color_system.djvu'),
            ('Ottosson, A perceptual color space for image processing', 'https://bottosson.github.io/posts/oklab/'),
            ('W3C, CSS Color Module Level 4', 'https://www.w3.org/TR/css-color-4/'),
            ('W3C, WCAG 2.2 contrast minimum', 'https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html')
        ]
    ),
    dict(
        id='4.3',
        title='Why does the same grey look different twice?',
        q='How can one grey square look warm on blue and cool on orange when its pixels never changed?',
        why='Colour is relational, so an isolated swatch is a poor promise. Chevreul gave designers a nineteenth-century account of adjoining colours, and Josef Albers turned the problem into exercises that make your eye catch itself making an inference. This is the bridge from colour theory to a real interface or frame.',
        plates=[dict(key='p43_chevreul', cap='Chevreul studied how adjacent colours alter one another\'s appearance. Read the plate as a relationship between neighbours, not a catalogue of fixed emotional meanings.')],
        story=[
            'Michel Eugène Chevreul encountered the problem at the Gobelins dye works, where colours that looked fine in isolation could look dull or shifted when woven beside one another. His <i>The Laws of Contrast of Colour</i> argued that adjoining colours can appear more different in hue or intensity than they do alone. Put a neutral grey on saturated orange and it may appear bluish; put the same grey on saturated blue and it may appear warmer. The central patch is unchanged. The visual system is comparing it with its surround. That comparison is not an error added after seeing; it is part of seeing a surface at all. The surrounding field supplies a local reference for what counts as neutral, bright or dull.',
            'Josef Albers made that fact practical in <i>Interaction of Color</i> (1963). Instead of presenting harmony as a fixed recipe, he gave students controlled exercises: make one colour appear as two, make two colours appear as one, and reverse figure and ground. The point is not to memorise an optical trick. It is to train the designer to ask what a colour is doing beside this exact neighbour, at this size, under this light, with this material.',
            'The effect matters on screens. A warm grey card beside MTRX orange can become muddy, while the same card beside a cool blue image can look unexpectedly brown or violet. A pale label that passes a contrast checker against a flat background may disappear over a photograph. A film colourist has the same issue in a larger space: a face, wall and costume shift as the surrounding production design and grade change. Sample the composition, not just the chip.',
            'Try this: make two identical medium-grey rectangles. Surround one with saturated blue and the other with saturated orange. Look for the apparent shift, then move both centres onto a neutral background. Repeat with a proposed brand accent and its actual page canvas. If the hierarchy changes, do not call the viewer inconsistent. Change the surround, area, value or chroma, and retest. The honest limit is that simple wheel opposites predict some relationships, not every appearance.'
        ],
        look=[
            ('Chevreul, The Laws of Contrast of Colour', 'Use the scan as a historical source for adjacent contrast and the industrial problem that made the theory useful.', 'https://commons.wikimedia.org/wiki/File:The_laws_of_contrast_of_colour_(IA_lawsofcontrastof00chev).pdf'),
            ('Josef Albers, Interaction of Color', 'Try the exercises in the Albers Foundation account. Its key move is to test colour in context instead of trusting a swatch name.', 'https://www.albersfoundation.org/alberses/teaching/interaction-of-color'),
            ('Yale, Interaction of Color', 'Drag or compare fields when possible. The lesson is not that perception is unreliable, but that context is part of the input.', 'https://color.yale.edu/'),
            ('Smithsonian, Using colour', 'The museum resource connects Chevreul\'s textile problem with a visible demonstration of simultaneous contrast.', 'https://library.si.edu/exhibition/color-in-a-new-light/using')
        ],
        steal=[
            'Approve colours in their component context: card, page, image, hover state, print stock or lighting setup.',
            'Make a two-background test for every important neutral. If it shifts into an unwanted family, alter the surround before altering the centre.',
            'In a film palette, write the relationship as same grey against two worlds, not as a fixed hex value.'
        ],
        director='A character can carry the same costume colour into two rooms and appear to change allegiance because the surrounding palette changed. The cut supplies the comparison the audience needs.',
        studio='Put the MTRX orange button on warm canvas, cool white and a wildlife photograph. Check not only its numeric contrast but the apparent shift and whether the action still reads first.',
        sources=[
            ('Chevreul, Laws of Contrast scan', 'https://commons.wikimedia.org/wiki/File:The_laws_of_contrast_of_colour_(IA_lawsofcontrastof00chev).pdf'),
            ('Albers Foundation, Interaction of Color', 'https://www.albersfoundation.org/alberses/teaching/interaction-of-color'),
            ('Yale, Interaction of Color', 'https://color.yale.edu/'),
            ('Smithsonian, Using colour', 'https://library.si.edu/exhibition/color-in-a-new-light/using')
        ]
    ),
    dict(
        id='4.4',
        title='Which colour scheme gives the frame a job?',
        q='Do you want a palette to enclose a world, connect it, divide it, or make one thing announce itself?',
        why='A colour wheel is most useful when it narrows a story decision. Monochromatic, analogous, complementary, split-complementary and triadic relationships are not moods in a bottle. They are starting constraints that help you control attention, separation, atmosphere and change.',
        plates=[
            dict(key='p44_whistler', cap='Whistler\'s near-monochromatic nocturne uses a dark field and tiny gold sparks. The small accent has power because the larger value and hue world is so restricted.'),
            dict(key='p44_starry', cap='Van Gogh\'s Starry Night is a blue-dominant field with yellow accents and changing lightness. Notice how the scheme supports movement rather than behaving like a neat three-swatch formula.')
        ],
        story=[
            '<b>Monochromatic</b> keeps one hue family while varying value and chroma. It can make a world feel enclosed, controlled or coherent. <b>Analogous</b> uses neighbours on a wheel, often with one dominant and one or two supports, so the frame feels continuous. <b>Complementary</b> opposes two regions and can separate a subject from its ground. <b>Split-complementary</b> keeps the contrast but replaces one opposite with its neighbours. <b>Triadic</b> uses three roughly spaced hues and needs hierarchy, because equal saturation makes every colour compete.',
            'Take the scheme as a search constraint, then judge the frame. Value, area, saturation, skin or animal rendering, material and light may matter more than the nominal wheel relationship. Complementary is not automatically harmonious, and analogous is not automatically calm. Research on colour combinations distinguishes pair preference, perceived harmony and figure preference: the same contrast that makes a figure pop can make a pairing less liked. Use the wheel to generate candidates, not to certify them.',
            'Film gives these relationships a job over time. The green world of <i>The Matrix</i> is a memorable monochromatic example, while <i>Amélie</i> is often discussed through red and green relationships. Those labels are interpretations to test shot by shot, not authorial laws. A palette can also be associative, with a colour attached to a person or object; transitional, changing as the story changes; or discordant, breaking an established rule at a reveal. The frame earns its meaning through repetition.',
            'Try one still three ways. First keep one hue and vary value. Then build a neighbour palette. Then choose an opposite and lower one colour\'s chroma until the subject separates without looking like an advertisement. Make a five-second thumbnail and ask what the eye notices first, what recedes, and what has changed in the story. The practical StudioBinder loop is simple: name the variable, show the frame, state the narrative job, then test a second frame. If the story job cannot be stated, the scheme is probably serving the mood board more than the scene. A good palette leaves room for a face, prop or title to become the exception.'
        ],
        look=[
            ('Whistler, Nocturne in Black and Gold: The Falling Rocket', 'A near-monochromatic field proves that a restricted palette can still hold atmosphere, texture and a sharp accent.', 'https://commons.wikimedia.org/wiki/File:Whistler-Nocturne_in_black_and_gold.jpg'),
            ('Van Gogh, The Starry Night', 'Study blue as the dominant field and yellow as a high-contrast accent, while noticing that value and brushwork carry as much structure as hue.', 'https://commons.wikimedia.org/wiki/File:Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg'),
            ('Van Gogh, Bedroom in Arles', 'Compare the strong blue, yellow and red relationships with the actual spatial structure. It is a painting to inspect, not a proof that one triad always feels cheerful.', 'https://commons.wikimedia.org/wiki/File:Vincent_van_Gogh_-_The_Bedroom_-_Google_Art_Project.jpg'),
            ('StudioBinder, 50 plus movie colour palettes', 'Use its frame-by-frame case-study pattern, but phrase effects as contextual readings rather than universal psychology.', 'https://www.studiobinder.com/blog/how-to-use-color-in-film-50-examples-of-movie-color-palettes/')
        ],
        steal=[
            'Write one sentence for the palette job: connect the landscape, separate the face, or break the learned world at the reveal.',
            'Assign dominant, support and accent roles before choosing exact swatches. A scheme without area and value is unfinished.',
            'Keep a version with one deliberate discordant colour. It gives the next cut or interaction somewhere to go.'
        ],
        director='Think in sequences, not isolated colour boards. Let a recurring hue accumulate as a character cue, then break it at a choice, betrayal or change of world.',
        studio='For a safari homepage, try an analogous dusk palette for continuity, then reserve complementary orange for booking or a conservation action. Measure whether the accent helps the task instead of merely looking energetic.',
        sources=[
            ('StudioBinder, Color Theory in Film', 'https://www.studiobinder.com/filmmaking-techniques-color-theory-in-film/'),
            ('StudioBinder, movie colour palettes', 'https://www.studiobinder.com/blog/how-to-use-color-in-film-50-examples-of-movie-color-palettes/'),
            ('Schloss and Palmer, colour preference and harmony', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3037488/'),
            ('Van Gogh Letters, letter 676', 'https://vangoghletters.org/vg/letters/let676/letter.html'),
            ('Wikimedia Commons, The Starry Night', 'https://commons.wikimedia.org/wiki/File:Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg')
        ]
    ),
    dict(
        id='4.5',
        title="What are Itten's seven contrasts?",
        q='Which relationship is actually doing the work: hue, light-dark, warm-cool, complement, simultaneity, saturation, or area?',
        why='Johannes Itten\'s seven contrasts are a checklist for looking, not seven laws to obey. They give a director or designer a useful diagnosis when a frame feels weak: perhaps the hues agree but the values collapse, or a tiny accent wins because extension gives it leverage.',
        plates=[dict(key='p45_itten', cap='Itten\'s colour circle makes hue and complementary relationships easy to spot. Use it as a vocabulary, then test the other contrasts in the actual image: light-dark, warm-cool, saturation and extension.')],
        story=[
            'Itten\'s <i>The Art of Color</i> (1961) names seven contrasts: <b>hue</b>, a difference between colour families; <b>light-dark</b>, a difference in value; <b>cold-warm</b>, a relative temperature shift; <b>complementary</b>, opposing colour relationships; <b>simultaneous</b>, the apparent shift caused by a neighbour; <b>saturation</b>, vivid against muted; and <b>extension</b>, the relative area or quantity assigned to each colour. The list is valuable because it stops contrast from meaning only opposite hues.',
            'Use it diagnostically. If a poster is hard to read, light-dark may be failing even though the hue pair is fashionable. If a subject will not separate from the background, a small value or saturation change may work better than adding a third hue. If a frame feels too loud, extension can reduce the area of the vivid colour. Warm-cool is relative, not a fixed temperature label: blue-green may feel warm beside violet and cool beside orange. The same checklist works on a safari map, a title card and a face in a doorway because it asks about relationships rather than genre.',
            'Itten\'s teaching language belongs beside, not above, later experiments. The RYB mixing diagram in traditional colour education is not a reliable physical model for every paint, and the seven contrasts are not seven independent natural laws. Josef Albers pushed the learner toward experiments in context. That pairing is useful: Itten supplies names for what to notice, while Albers asks whether the intended relation is actually visible in this arrangement.',
            'Take a film frame or a web hero and make seven tiny notes. Circle the one contrast carrying the hierarchy, underline a supporting contrast, and mark one that is absent. Then make a grayscale version. If the composition survives, light-dark or extension may be doing the heavy lifting. If it dies, do not automatically add saturation. Rebuild the area and value structure first, then decide whether a hue contrast earns its place. This also makes collaboration easier: a developer can change a token, and a cinematographer can change a light, while both still understand the intended relationship.'
        ],
        look=[
            ('Johannes Itten, colour circle, 1961', 'Use the wheel to locate hue and complement, then look away from it and inspect value, temperature, chroma and area in a real composition.', 'https://commons.wikimedia.org/wiki/File:Farbkreis_Itten_1961.svg'),
            ('Getty Research Institute, Bauhaus colour resource', 'The resource explains Itten\'s contrast vocabulary and colour star in the teaching context where it was used.', 'https://www.getty.edu/research/exhibitions_events/exhibitions/bauhaus/new_artist/form_color/color/'),
            ('Josef Albers, Interaction of Color', 'Albers is the productive counterweight: make the claimed contrast happen in an exercise rather than accepting a label.', 'https://www.albersfoundation.org/alberses/teaching/interaction-of-color'),
            ('Kirchner, How Itten\'s color diagram fails', 'Read the physical critique before treating the RYB wheel as a paint recipe. A useful pedagogical diagram can still be a weak material model.', 'https://doi.org/10.1364/oe.492990')
        ],
        steal=[
            'Annotate a palette with the contrast doing the work, not only with colour names.',
            'Try light-dark and extension before adding another hue. They are often cheaper, clearer hierarchy controls.',
            'Use a vivid accent sparingly. Its area can be small and its visual effect large.'
        ],
        director='In a shot list, name the contrast that changes at the beat: same hue with lower saturation, a cool background with a warm face, or a small red object expanding to fill the frame.',
        studio='For MTRX, pair a quiet neutral system with one extension-controlled orange accent. Check that the accent is still legible when colour vision is limited and when the image is reduced to a phone thumbnail.',
        sources=[
            ('Itten, The Art of Color catalogue record', 'https://bvbr.bib-bvb.de/F?doc_library=BVB01&doc_number=022496993&func=service&func_code=DB_RECORDS&line_number=0001&local_base=BVB01&sequence=000002&service_type=MEDIA'),
            ('Getty, Bauhaus colour', 'https://www.getty.edu/research/exhibitions_events/exhibitions/bauhaus/new_artist/form_color/color/'),
            ('Kirchner, critique of Itten diagram', 'https://doi.org/10.1364/oe.492990'),
            ('Albers Foundation, Interaction of Color', 'https://www.albersfoundation.org/alberses/teaching/interaction-of-color')
        ]
    ),
    dict(
        id='4.6',
        title='Can a 1930s Japanese dictionary pick your palette?',
        q='What if your next brand palette came from a historical combination instead of a blank colour wheel?',
        why='Sanzo Wada\'s <i>A Dictionary of Color Combinations</i> is not a magic harmony engine. It is a rich archive of decisions, translated into compact pairs, trios and groups that can interrupt your habitual taste. The practical value is not copying history unchanged, but using a historical prompt and then testing it against a modern job.',
        plates=[],
        story=[
            'Sanzo Wada was a Japanese painter, teacher, colour researcher, costume designer and fashion designer. His <i>Haishoku Soukan</i>, commonly translated as <i>A Dictionary of Color Combinations</i>, was published in six volumes in 1933 and 1934. The 2010 Seigensha edition presents 348 combinations. Contemporary digital reconstructions describe 120 pairs, 120 trios and 108 groups of four, using 159 named colours. The numbers describe the reprint and digitisation record, not a scientific count of every possible Japanese colour relationship.',
            'Use the book as a search space. Choose a combination whose area balance or temperature surprises you, then rewrite it as a brand role system: base, surface, structure, action and optional signal. Do not assume that a translated name or online RGB conversion is the original physical colour. The community datasets are useful for exploration, but scans, transcription and colour conversion can introduce errors. Seigensha\'s scans, editorial writing and layout are not automatically free to copy.',
            'For MTRX, start with one Wada pair or trio, then make three versions. Version one keeps the historical proportions. Version two gives the darkest or quietest colour most of the interface area. Version three reserves the most vivid colour for one action or conservation signal. Convert candidates to OKLCH for a lightness check, to sRGB for the ordinary web, and to print or material references when the palette will leave the screen. The palette becomes yours through the decisions and tests, not through a claim that the old combination is universally harmonious. The historical source supplies a starting conversation, not permission to skip audience research or accessibility review.',
            'A useful handoff records the source plate, translated names, approximate digital values, semantic roles, area intentions, contrast results and exceptions. Test the palette in grayscale, on a wildlife photograph, in a dark theme and through a colour-vision simulator. Ask what survives when the accent is removed. The honest answer to the title is yes, as a prompt. A dictionary can widen your options, but the client, audience, medium and story still choose the final palette. That discipline turns browsing into design and gives later collaborators a reason for every token.'
        ],
        look=[
            ('Seigensha, A Dictionary of Color Combinations', 'Use the publisher page to identify the 2010 edition and its stated 348 combinations. Treat it as a book to consult, not a free scan to reproduce.', 'https://en.seigensha.com/books/978-4-86152-247-5/'),
            ('Sanzo Wada interactive archive', 'Browse the combination structure and colour names, then compare a pair, trio and four-colour group rather than selecting by a single favourite swatch.', 'https://colorcombinations.org/books/a-dictionary-of-color-combinations/'),
            ('Dain Blodorn Kim\'s interactive project', 'Use it to explore translated combinations, while keeping the project\'s own licence and conversion limits visible in your notes.', 'https://sanzo-wada.dmbk.io/'),
            ('Matt DesLauriers, dictionary dataset', 'The MIT-licensed dataset is a practical route for a palette prototype. Preserve attribution and note that RGB values are conversions.', 'https://github.com/mattdesl/dictionary-of-colour-combinations'),
            ('W3C, CSS Color Module Level 4', 'Use a web colour space only after choosing the story and semantic roles. Numeric consistency is not perceptual identity.', 'https://www.w3.org/TR/css-color-4/')
        ],
        steal=[
            'Start every palette workshop with three historical combinations before opening a random generator.',
            'Translate a chosen plate into semantic roles and area proportions, then test the roles in the real interface.',
            'Keep source, licence, conversion method and material target in the palette handoff so another maker can reproduce the decision.'
        ],
        director='A historical palette can become a production design constraint for a whole location: costume, wall, prop and practical light each take a role, then one colour breaks the system when the story changes.',
        studio='For a safari or eco-lodge client, use Wada as a prompt for earthy, mineral or botanical combinations, then check accessibility, photography, print samples and local audience associations before calling it the brand palette.',
        sources=[
            ('Seigensha publisher, 2010 edition', 'https://en.seigensha.com/books/978-4-86152-247-5/'),
            ('Dictionary of Color Combinations archive', 'https://colorcombinations.org/books/a-dictionary-of-color-combinations/'),
            ('Archive methodology and licence notes', 'https://colorcombinations.org/methodology/'),
            ('MIT-licensed dataset', 'https://github.com/mattdesl/dictionary-of-colour-combinations'),
            ('OKLCH and CSS Color 4', 'https://www.w3.org/TR/css-color-4/')
        ]
    )
]

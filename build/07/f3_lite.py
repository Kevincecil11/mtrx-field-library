IMAGES = {
    'p31_lines': dict(
        file='File:Typography Line Terms.svg',
        credit='Max Naylor, Typography Line Terms, 2007',
        lic='Public domain',
        alt='A typographic diagram marking baseline, x-height, cap height, ascenders and descenders in Garamond and Helvetica.'),
    'p32_caslon': dict(
        file='File:A Specimen by William Caslon.jpg',
        credit='William Caslon, A Specimen by William Caslon, circa 1734',
        lic='Public domain',
        alt='A large eighteenth-century specimen sheet showing many typefaces and writing systems.'),
    'p33_display': dict(
        file='File:1856 Display Types Specimen (27541236734).jpg',
        credit='James Puckett, 1856 Display Types Specimen, 2016 scan',
        lic='CC BY 2.0',
        alt='A nineteenth-century display type specimen sheet with ornate, high-impact letterforms.'),
    'p34_compare': dict(
        file='File:Futura Helvetica capitals comparison.png',
        credit='Blythwood, Futura Helvetica capitals comparison, 2016',
        lic='CC BY-SA 4.0',
        alt='A comparison of Futura and Helvetica capital proportions.'),
    'p35_deva': dict(
        file='File:Linotype - Devanagari.djvu',
        credit='Mergenthaler Linotype Company, Keyboard Operation - Devanagari Linotype, 1933',
        lic='Public domain',
        alt='A page from a 1933 manual showing the keyboard and composition of Devanagari type.'),
    'p36_bass': dict(
        file='File:The Man with the Golden Arm poster.jpg',
        credit='Saul Bass, The Man with the Golden Arm poster, 1955',
        lic='Public domain',
        alt='Saul Bass poster with a jagged black arm motif and compact, forceful film lettering.'),
    'p37_gutenberg': dict(
        file='File:Gutenberg Bible (page).JPG',
        credit='Johannes Gutenberg, Gutenberg Bible page, circa 1455',
        lic='Public domain',
        alt='A dense blackletter page from a Gutenberg Bible with rubrication and illuminated initials.'),
}

STOPS = [
    dict(
        id='3.1', title='What is a letter before it is a font?',
        q='How can you see the construction of a typeface before naming its mood?',
        why='A font menu gives you names. Anatomy gives you evidence. Read a letter as a small engineered object, and pairing becomes a decision about proportion, rhythm, and space rather than a guess at personality.',
        plates=[dict(key='p31_lines', cap='Start with the lines: baseline and x-height set the texture of a paragraph, while ascenders and descenders create its vertical rhythm.')],
        story=[
            'A <b>baseline</b> is the invisible floor most letters sit on. The <b>x-height</b> is the body of lowercase x, a useful proxy for apparent size. <b>Cap height</b> is the height of flat-topped capitals. An <b>ascender</b> rises above x-height, as in h or b; a <b>descender</b> drops below the baseline, as in p or g. Compare these first when two fonts claim to be the same size. A high x-height can feel sturdy on a phone. Long ascenders and descenders can feel more literary, but need breathing room between lines.',
            'Then inspect the inside and the edge. A <b>counter</b> is the negative space inside o, e, or a. An <b>aperture</b> is an opening, especially in c or e. A <b>serif</b> finishes a stroke; a <b>terminal</b> is a stroke ending without a serif. Stroke contrast is the difference between thick and thin. Low contrast often survives small screens; high contrast can bring editorial drama but can lose its hairlines. The crucial lesson is not that one anatomy is better. It is that every feature changes colour, density, and recognition.',
            'For MTRX, set the same sentence in Tanker and Nunito Sans, then mark baseline, x-height, counters, apertures, and terminals. Tanker compresses the word into a sign. Nunito Sans leaves more room around the counters. The first is a headline instrument, the second a reading instrument. Name the construction before you name the feeling.'
        ],
        look=[
            ('Typography Line Terms', 'Trace baseline, x-height, cap height, ascenders, and descenders. Notice that alignment is an optical system, not just a ruler.', 'https://commons.wikimedia.org/wiki/File:Typography_Line_Terms.svg'),
            ('Nunito Sans specimen', 'Compare its open counters and rounded terminals at 16 px and 48 px.', 'https://fonts.google.com/specimen/Nunito+Sans'),
            ('Tanker specimen', 'Look for compressed width and headline weight before deciding where it belongs.', 'https://www.fontshare.com/fonts/tanker')
        ],
        steal=['Make one annotated type specimen for every brand system.', 'Match apparent x-height, not nominal point size, when pairing faces.'],
        director='A director can make anatomy part of the world: a bureaucratic form with rigid alignment, or a damaged diary whose counters and edges become unstable.',
        studio='Use Tanker for the MTRX mark and rare display moments. Use Nunito Sans for body copy, navigation, forms, and captions, then test both at the smallest real viewport.',
        sources=[
            ('Commons anatomy diagram', 'https://commons.wikimedia.org/wiki/File:Typography_Line_Terms.svg'),
            ('Fontshare Tanker', 'https://www.fontshare.com/fonts/tanker'),
            ('Google Fonts Nunito Sans', 'https://fonts.google.com/specimen/Nunito+Sans'),
            ('Lupton, Thinking with Type', 'https://thinkingwithtype.com/')
        ]),
    dict(
        id='3.2', title='Why do type families sound different?',
        q='What history and construction sit behind a type classification?',
        why='A type family is not a mood board category. It is a record of tools, writing habits, printing technology, and visual corrections. History lets you predict what a face will do before you use it.',
        plates=[dict(key='p32_caslon', cap='Caslon makes classification tangible: compare the calligraphic movement, bracketed serifs, and text-sized rhythm rather than memorising a label.')],
        story=[
            'The broad story runs from Gutenberg\'s dense blackletter page, through Jenson\'s humanist roman, Garamond\'s Renaissance forms, Baskerville\'s transitional refinement, and Bodoni\'s vertical, high-contrast Didone. Later, Akzidenz-Grotesk brought the irregular energy of the grotesque sans; Futura turned geometry into a commercial modernist voice; Helvetica regularised the neo-grotesque into a powerful system. Each shift changed the relationship between hand, machine, ink, paper, and reader.',
            'Use classification as a search tool, not a verdict. <b>Humanist</b> faces carry calligraphic variation. <b>Transitional</b> faces are more regular and authoritative. <b>Didones</b> use vertical stress and hairline serifs. <b>Slabs</b> use sturdy serifs. <b>Grotesques</b> retain early sans irregularities; <b>neo-grotesques</b> smooth them into restrained systems. <b>Geometric</b> sans faces build from circles and shapes. <b>Humanist sans</b> faces keep open, calligraphic forms. <b>Script</b> and <b>display</b> faces foreground gesture or image. A face can be a hybrid, and a category says nothing by itself about cultural fit or accessibility.',
            'The useful question is physical: what action could have drawn this stroke? A broad nib explains diagonal stress; a rationalised geometric construction explains a circular o; a screen face may open its apertures for pixels. For a safari brand, a humanist text face can carry field notes, while a condensed display face can behave like a trail marker. Choose the role, then choose the history.'
        ],
        look=[
            ('Gutenberg Bible page', 'See how blackletter texture, two columns, rubrication, and illumination work as one page system.', 'https://commons.wikimedia.org/wiki/File:Gutenberg_Bible_(page).JPG'),
            ('A Specimen by William Caslon', 'Scan the sheet as a catalogue of construction, language support, and hierarchy, not as a list of pretty alphabets.', 'https://commons.wikimedia.org/wiki/File:A_Specimen_by_William_Caslon.jpg'),
            ('Futura and Helvetica capitals comparison', 'Compare the width and geometry of capitals. Similar subject matter does not mean similar skeleton.', 'https://commons.wikimedia.org/wiki/File:Futura_Helvetica_capitals_comparison.png'),
            ('ATypI on the Vox classification', 'Use the historical classification vocabulary, while remembering that it is Latin-centred and not a universal law.', 'https://atypi.org/2021/04/27/atypi-de-adopts-the-vox-atypi-typeface-classification-system/')
        ],
        steal=['Write one sentence about the stroke action before writing a mood adjective.', 'Build a two-column type brief: historical reference on one side, actual use and size on the other.'],
        director='Production design uses type history as period detail. A wrong grotesque, geometric face, or digital rendering can reveal that a supposedly 1970s sign was made by today\'s template.',
        studio='Let Tanker carry the contemporary sign or wordmark, and let Nunito Sans carry the explanatory layer. The contrast is useful only when their roles stay stable.',
        sources=[
            ('British Library, Gutenberg Bible', 'https://www.bl.uk/collection-items/gutenbergs-bible'),
            ('Birmingham Museums Trust, Baskerville', 'https://www.birminghammuseums.org.uk/explore/stories/john-baskerville'),
            ('Bodoni Museum', 'https://www.museobodoniano.it/'),
            ('ATypI classification history', 'https://atypi.org/2021/04/27/atypi-de-adopts-the-vox-atypi-typeface-classification-system/')
        ]),
    dict(
        id='3.3', title='Should good type be invisible?',
        q='When should typography disappear into reading, and when should it become an image?',
        why='Beatrice Warde argued for typography as a clear vessel for language. Expressive designers such as Wim Crouwel and David Carson show the counter-case: sometimes the disturbance is the message.',
        plates=[dict(key='p33_display', cap='A display specimen is not trying to be quiet. Its job is to make letterform, texture, and surprise visible at a distance.')],
        story=[
            'In The Crystal Goblet, Beatrice Warde compares transparent glass with ornate gold. Her point is functional and ethical: when the reader came for the wine, the vessel should not cloud it. In a long article, a quiet face, clear hierarchy, generous measure, and controlled leading can let the argument arrive without announcing every typographic decision. Invisible does not mean neutral or personality-free. It means the design is carrying attention toward the content.',
            'But a title, poster, warning, or film credit may be the content. Wim Crouwel used grids and modular letterforms to make visual communication visibly constructed. David Carson made damaged, fragmented type a signal of music culture, speed, and refusal. Kyle Cooper later etched and distressed type in <i>Se7en</i> so that the title sequence felt like the killer\'s handmade notebook. In those cases, difficulty is not an accident to repair. It is part of the narrative contract.',
            'The decision is about reading time. If someone must find a dosage, price, trail direction, or button, protect the message. If the viewer is meant to feel a world before decoding it, let type act as image, but give the image a deliberate limit. The honest rule is not invisible type. It is legible intent.'
        ],
        look=[
            ('The Crystal Goblet, Beatrice Warde', 'Read the metaphor as a philosophy of reading, then ask where the vessel itself becomes the subject.', 'https://press.uchicago.edu/Misc/Chicago/791599bw.html'),
            ('Visuele communicatie Nederland, Wim Crouwel, 1969', 'Notice how a grid can make the letterforms and their construction part of the subject.', 'https://www.rijksmuseum.nl/en/collection/object/Poster-for-Visuele-communicatie-Nederland--bc6c923f6fc914727a17e2690b40758f'),
            ('Se7en title sequence, Kyle Cooper', 'The hand-etched type, scratched film, and unstable reading make process itself feel like character.', 'https://www.artofthetitle.com/title/se7en/'),
            ('1856 Display Types Specimen', 'Compare display lettering as visual event with the modest texture needed for sustained prose.', 'https://commons.wikimedia.org/wiki/File:1856_Display_Types_Specimen_(27541236734).jpg')
        ],
        steal=['Give every typographic effect a narrative job: locate, reassure, warn, date, or unsettle.', 'Keep utility text calm when the hero type is loud.'],
        director='Use expressive type like production design or sound: a controlled disturbance can foreshadow a character, era, or threat. Do not make every title sequence shout.',
        studio='For MTRX, reserve Tanker\'s force for the identity voice. Let Nunito Sans make the service understandable, then use #ED691D as a measured signal rather than another competing voice.',
        sources=[
            ('Warde, The Crystal Goblet', 'https://press.uchicago.edu/Misc/Chicago/791599bw.html'),
            ('Rijksmuseum, Crouwel poster', 'https://www.rijksmuseum.nl/en/collection/object/Poster-for-Visuele-communicatie-Nederland--bc6c923f6fc914727a17e2690b40758f'),
            ('Art of the Title, Se7en', 'https://www.artofthetitle.com/title/se7en/'),
            ('David Carson design', 'https://www.davidcarsondesign.com/'),
            ('Commons display specimen', 'https://commons.wikimedia.org/wiki/File:1856_Display_Types_Specimen_(27541236734).jpg')
        ]),
    dict(
        id='3.4', title='How do Tanker and Nunito Sans become a system?',
        q='How can a display face and a text face share one brand without competing?',
        why='Kevin\'s fonts already contain a useful tension: Tanker is compressed and declarative; Nunito Sans is open, rounded, and serviceable. The system works when each face gets a job, a scale, and room to breathe.',
        plates=[dict(key='p34_compare', cap='A comparison of Futura and Helvetica shows why pairing is structural: width, terminals, and proportions matter more than a shared adjective such as modern.')],
        story=[
            'Tanker, designed by Ruosi Huang and published by Indian Type Foundry through Fontshare, is a single-style bold condensed display sans. It can name MTRX, a campaign, a section, or a film-like moment. It is not a paragraph face. Nunito Sans, developed from Vernon Adams\'s Nunito with Jacques Le Bailly and others, offers a broad weight range, italics, generous counters, and a practical text voice. It can explain the promise after Tanker has made the entrance.',
            'Pair by <b>role contrast</b>, then check <b>structural coherence</b>. Let Tanker handle the mark and rare display headings. Let Nunito Sans handle body text, navigation, forms, captions, and buttons. Start with one clear scale, for example 1rem body, 1.25rem section label, 2rem heading, and a larger Tanker display step. Set prose around 45 to 75 characters per line, usually beginning near 55 to 70, with line-height around 1.35 to 1.6. These are starting points, not laws.',
            'Test the pair in grayscale and in real content. Compare x-height, numerals, punctuation, uppercase, dark mode, 320 px width, and long headings. Keep tracking modest, never use Tanker to solve a paragraph, and do not let every button become a logo. Do not invent Tanker weights: it has one display style, so build its hierarchy through size, space, case, and colour. Nunito Sans supplies weight and emphasis. One face names the thing; the other helps a person use it.'
        ],
        look=[
            ('Tanker, Fontshare', 'Check the actual specimen and current license before embedding. Notice how much information its condensed width packs into a line.', 'https://www.fontshare.com/fonts/tanker'),
            ('Nunito Sans, Google Fonts', 'Compare its weights and italics with actual interface copy, not isolated alphabet mood boards.', 'https://fonts.google.com/specimen/Nunito+Sans'),
            ('Google Fonts type pairing guidance', 'Use role, superfamily, designer, and font-matrix comparisons as methods, not as an automatic answer.', 'https://fonts.google.com/knowledge/glossary/pairing_typefaces'),
            ('Futura and Helvetica capitals comparison', 'Use the structural contrast as a reminder that two sans faces can differ in width, stress, and rhythm.', 'https://commons.wikimedia.org/wiki/File:Futura_Helvetica_capitals_comparison.png')
        ],
        steal=['Write a one-line role contract: Tanker names, Nunito Sans explains.', 'Make a type scale token set and test the entire page in grayscale before adding orange.', 'Keep a fallback with similar metrics and test the swap, not just the ideal loaded state.'],
        director='Film titles often use a display voice for the world and a restrained credit system for comprehension. Borrow that hierarchy for a landing page: entrance, orientation, detail.',
        studio='On a safari site, Tanker can label the expedition or hero promise; Nunito Sans can carry dates, inclusions, safety details, and booking controls. On a clinic site, reduce Tanker to the identity and let Nunito Sans do nearly all the explaining.',
        sources=[
            ('Fontshare, Tanker', 'https://www.fontshare.com/fonts/tanker'),
            ('Google Fonts, Nunito Sans', 'https://fonts.google.com/specimen/Nunito+Sans'),
            ('Bringhurst, The Elements of Typographic Style', 'https://www.hachettebookgroup.com/titles/robert-bringhurst/the-elements-of-typographic-style/9780881792123/'),
            ('Dyson, line length review', 'https://doi.org/10.1080/01449290410001715714'),
            ('MDN, @font-face', 'https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face')
        ]),
    dict(
        id='3.5', title='Can one site speak Gujarati, Hindi and English?',
        q='How do you make a multilingual type system feel like one voice without flattening three scripts?',
        why='A Latin logo with an afterthought translation is not a multilingual system. Devanagari and Gujarati have their own histories, shaping rules, proportions, and reading textures, so the companion must be designed and tested as a first-class voice.',
        plates=[dict(key='p35_deva', cap='A Devanagari composition manual makes the hidden work visible: script support includes keyboard logic, conjuncts, marks, and shaping, not just a bigger character set.')],
        story=[
            'Devanagari and Gujarati are not Latin letters wearing different costumes. Devanagari uses a headline structure and complex conjunct shaping; Gujarati has its own forms and calligraphic history. Indian Type Foundry describes ITF Gujarati as a companion to its ITF Devanagari work, with weights designed for text and display and stroke contrast that can sit beside oldstyle Latin. That is a useful model: match <b>colour</b>, meaning the overall darkness and rhythm of a paragraph, rather than forcing identical letter shapes.',
            'For an MTRX site, test English, ગુજરાતી, and हिन्दी in the same components: navigation, buttons, prices, dates, error messages, cards, and long paragraphs. Compare apparent x-height or equivalent body height, line count, mark collisions, word breaks, numerals, and weight. Noto Sans, Mukta, Hind, and ITF families can be starting points, but a family name is not proof of coverage or quality. Inspect the actual glyphs and OpenType shaping in the browsers and devices your audience uses.',
            'Pair scripts by role and colour. The headline may use Tanker only when the script has a credible display companion; otherwise use a multilingual text family for the headline too. Give Devanagari and Gujarati enough line-height for marks, and let the longest language set the card height. A single brand voice means shared hierarchy, spacing, colour, and intent. It does not mean pretending every script has the same skeleton.'
        ],
        look=[
            ('Keyboard Operation - Devanagari Linotype, 1933', 'Look at the composition problem behind a script: shaping and keyboard workflow are part of type design.', 'https://commons.wikimedia.org/wiki/File:Linotype_-_Devanagari.djvu'),
            ('ITF Gujarati', 'Notice the explicit companion relationship, text weights, contrast, and attention to Gujarati conjuncts and marks.', 'https://www.indiantypefoundry.com/news/itf-gujarati'),
            ('Noto Fonts', 'Use Noto as a coverage reference, then test its actual texture and hierarchy beside the Latin system.', 'https://fonts.google.com/noto'),
            ('Mukta, Google Fonts', 'Compare the family across scripts and weights in real interface strings.', 'https://fonts.google.com/specimen/Mukta')
        ],
        steal=['Make a three-script specimen page before choosing a brand companion.', 'Use the same component states and content lengths across scripts, then fix the worst case first.', 'Match paragraph colour and hierarchy, not letterform geometry.'],
        director='A fictional city, institution, or family can reveal itself through which script is dominant, how signs mix languages, and whether translations were made with care.',
        studio='For Ahmedabad clients, keep English, Gujarati, and Hindi in the first content review. A booking button that wraps or a Gujarati headline with the wrong line-height is a brand failure, not a translation footnote.',
        sources=[
            ('Indian Type Foundry, ITF Gujarati', 'https://www.indiantypefoundry.com/news/itf-gujarati'),
            ('Google Fonts Noto', 'https://fonts.google.com/noto'),
            ('Google Fonts Mukta', 'https://fonts.google.com/specimen/Mukta'),
            ('University of Reading, Devanagari type history', 'https://centaur.reading.ac.uk/101230/1/FR_PHS_DevArticle_29Aug21_02.pdf'),
            ('Commons Devanagari manual', 'https://commons.wikimedia.org/wiki/File:Linotype_-_Devanagari.djvu')
        ]),
    dict(
        id='3.6', title='How does type enter film?',
        q='How can titles, signs, and credits make typography part of a film world?',
        why='Film typography is not decoration added after the image. It establishes era, class, technology, threat, and rhythm before the story has fully begun.',
        plates=[dict(key='p36_bass', cap='Saul Bass turns a jagged arm into a visual verb. The poster shows how a title can belong to the film\'s movement, not merely label it.')],
        story=[
            'Saul Bass made title design behave like editing: simple shapes, strong contrast, and a mark that carries the film\'s central anxiety. Pablo Ferro brought hand lettering, rapid cuts, and kinetic energy to titles including <i>Dr. Strangelove</i>. Kyle Cooper\'s <i>Se7en</i> pushed in the opposite direction, using hand-etched type, scratched film, unstable scale, and the serial killer\'s notebooks so the title sequence feels made by the character. Wes Anderson uses Futura and related geometric voices as part of a controlled, artificial world. The <i>Alien</i> and <i>Blade Runner</i> title systems make spacing, emergence, and atmosphere do narrative work.',
            'Think in layers. First define the world: year, institution, class, technology, wear, and distance from camera. Then choose a letter behaviour: official, improvised, industrial, elegant, damaged, or unreadable. Finally decide how type moves with image and sound. A sign in the set must work at a glance. A main title can take longer, because its job may be to withhold, foreshadow, or create a physical sensation.',
            'The production rule is simple: every visible word has a maker. A receipt, motel sign, medical label, newspaper, interface, and end credit should have a reason for its shape. Borrow Bass\'s economy, Cooper\'s process, Ferro\'s timing, or Anderson\'s consistency, but do not borrow a surface without the story logic underneath it.'
        ],
        look=[
            ('The Man with the Golden Arm, Saul Bass, 1955', 'See how one jagged shape and a compact typographic lock-up create motion and menace.', 'https://commons.wikimedia.org/wiki/File:The_Man_with_the_Golden_Arm_poster.jpg'),
            ('Saul Bass title work', 'Compare how Bass changes the graphic idea for each film instead of applying one universal style.', 'https://www.artofthetitle.com/designer/saul-bass/'),
            ('Se7en, Kyle Cooper, 1995', 'Study type etched into the material of the image, then notice how the process tells us who made it.', 'https://www.artofthetitle.com/title/se7en/'),
            ('Alien title sequence', 'Watch the title emerge by fragments. Spacing and reveal create suspense before the word is complete.', 'https://www.artofthetitle.com/title/alien/'),
            ('Blade Runner title sequence', 'Look for how restrained typography and atmosphere make a future feel industrial rather than shiny.', 'https://www.artofthetitle.com/title/blade-runner/')
        ],
        steal=['Write a fictional type brief for the world before opening a font menu.', 'Make the title behaviour obey the character or institution that made it.', 'Keep a continuity sheet for every visible word in a scene.'],
        director='Use type as a prop with provenance. The right letterform can reveal a decade, budget, bureaucracy, or private obsession before dialogue explains any of it.',
        studio='A safari film or lodge site can treat wayfinding, species labels, and booking confirmations as one believable world. MTRX can make the hero title cinematic while keeping operational copy plain and calm.',
        sources=[
            ('Commons, Saul Bass poster', 'https://commons.wikimedia.org/wiki/File:The_Man_with_the_Golden_Arm_poster.jpg'),
            ('Art of the Title, Saul Bass', 'https://www.artofthetitle.com/designer/saul-bass/'),
            ('Art of the Title, Se7en', 'https://www.artofthetitle.com/title/se7en/'),
            ('Art of the Title, Alien', 'https://www.artofthetitle.com/title/alien/'),
            ('Art of the Title, Blade Runner', 'https://www.artofthetitle.com/title/blade-runner/')
        ]),
    dict(
        id='3.7', title='What makes a type decision safe to ship?',
        q='How do you move from a beautiful specimen to a reliable production font system?',
        why='A typeface can look perfect in a mock-up and fail in the browser, on a low-contrast screen, in Gujarati, or under a license you cannot use. Shipping means checking the whole chain, not just the screenshot.',
        plates=[dict(key='p37_gutenberg', cap='A printed page is a production system: type, material, ink, spacing, correction, and hierarchy all have to survive the journey to the reader.')],
        story=[
            'Start with rights. Confirm the current license for each family, especially when you self-host, subset, modify, embed in an app, or pass files to a client. Tanker is distributed through Fontshare under the Indian Type Foundry free font terms; Nunito Sans is distributed under the SIL Open Font License. Keep the license files and record the version. Then build the web path: licensed WOFF2, only the language ranges you truly need, a deliberate <code>font-display</code> strategy, and a metrically compatible fallback so a late font does not move buttons and headings around.',
            'Check accessibility with real text. Let users resize and zoom; preserve reflow; keep body text large enough for the task; test contrast for text, links, focus states, and disabled states; and do not rely on orange alone to signal meaning. Compare the loaded face and fallback at 320 px, desktop width, dark mode, and slow connection. Test numerals, punctuation, italics, long words, mixed scripts, and the longest translation. A variable font can reduce duplicated files, but it still needs a payload and axis budget.',
            'Use this pre-launch pass: license and version recorded; glyph coverage verified; shaping checked in English, Gujarati, and Hindi; body measure near 45 to 75 characters; leading checked at 1.35 to 1.6; contrast and focus states audited; zoom and reflow tested; fallback metrics checked; WOFF2 size measured; font loading observed on a slow device; and screenshots reviewed in grayscale. If a type decision fails one of these, it is not safe because it is pretty. Fix the system, or choose a less glamorous face that survives.'
        ],
        look=[
            ('Gutenberg Bible page', 'Notice that durable typography depends on the complete production context, not an isolated glyph.', 'https://commons.wikimedia.org/wiki/File:Gutenberg_Bible_(page).JPG'),
            ('MDN, @font-face', 'Use it for the practical loading, format, and fallback decisions behind a web font.', 'https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face'),
            ('W3C, CSS Fonts 4', 'Check the standards vocabulary for font matching, loading, and variation.', 'https://www.w3.org/TR/css-fonts-4/'),
            ('Nunito Sans OFL text', 'Keep the license with the project and read the current terms rather than trusting a remembered summary.', 'https://github.com/googlefonts/NunitoSans/blob/main/OFL.txt')
        ],
        steal=['Keep a font manifest: family, version, license, files, supported scripts, fallback, and owner.', 'Review typography on a slow phone and at 200 percent zoom before launch.', 'Test the worst translation and the longest button, not only the showcase headline.'],
        director='On a film set, type safety is continuity: a sign must be readable at the intended distance, period-credible, and consistent across angles. In post, a title must survive compression, projection, and subtitles.',
        studio='For MTRX, make this checklist part of handoff. A client should receive the licensed font files or links, CSS tokens, fallback stack, script coverage notes, and screenshots of the tested states.',
        sources=[
            ('Fontshare, Tanker', 'https://www.fontshare.com/fonts/tanker'),
            ('Nunito Sans OFL', 'https://github.com/googlefonts/NunitoSans/blob/main/OFL.txt'),
            ('MDN, @font-face', 'https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face'),
            ('W3C, CSS Fonts 4', 'https://www.w3.org/TR/css-fonts-4/'),
            ('Web.dev, variable fonts', 'https://web.dev/articles/variable-fonts')
        ])
]

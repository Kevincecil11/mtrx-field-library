"""No. 07, Part 2, Shared principles, lite stops 2.1 to 2.6.
Research checked 27 Oct 2026. ASCII punctuation is intentional: the guide rejects
em and en dashes. Commons file titles were checked against public file records.
"""

IMAGES = {
    'p21_caravaggio': dict(
        file='File:The Calling of Saint Matthew-Caravaggo (1599-1600).jpg',
        credit='Caravaggio, The Calling of Saint Matthew, circa 1599 to 1600, Contarelli Chapel, Rome',
        lic='Public domain',
        alt='A dark room of seated figures, crossed by a bright diagonal beam and a pointing hand.'),
    'p22_seurat': dict(
        file='File:A Sunday on La Grande Jatte, Georges Seurat, 1884.jpg',
        credit='Georges Seurat, A Sunday Afternoon on the Island of La Grande Jatte, 1884 to 1886, Art Institute of Chicago',
        lic='Public domain',
        alt='A riverside park filled with still figures built from many small painted marks.'),
    'p23_hasegawa': dict(
        file='File:Hasegawa Tohaku - Pine Trees (Shōrin-zu byōbu) - left hand screen.jpg',
        credit='Hasegawa Tohaku, Pine Trees, left hand screen, 16th century, Tokyo National Museum',
        lic='Public domain',
        alt='Mist and pale paper hold a few ink-painted pine trees, with large quiet areas between them.'),
    'p24_muller': dict(
        file='File:SVP Toni Brunner Zuerich HB 171015.jpg',
        credit='NAC, Swiss Peoples Party election poster at Zurich Main Station, 2015',
        lic='CC BY-SA 4.0',
        alt='A Swiss election poster in a railway station uses a large portrait, strong type, and open surrounding space.'),
    'p25_hokusai': dict(
        file='File:The Great Wave off Kanagawa.jpg',
        credit='After Katsushika Hokusai, The Great Wave off Kanagawa, circa 1930, Wikimedia Commons',
        lic='Public domain',
        alt='A giant blue wave curls over small boats, with Mount Fuji in the distant opening.'),
    'p26_mondrian': dict(
        file='File:Composition-with-red-yellow-and-blue.jpg',
        credit='Piet Mondrian, Composition with Yellow, Blue and Red, 1942, Tate',
        lic='Public domain',
        alt='A white field is divided by black lines and a few uneven blocks of red, yellow, and blue.'),
}

STOPS = [
    dict(
        id='2.1',
        title='Who chose the first look?',
        q='What does your eye see first, and who chose that?',
        why=('Every frame and page has a first read, even when the maker did not plan one. '
             'Hierarchy is the quiet act of deciding what arrives first, second, and third, so a safari site can sell a landscape and a film can reveal a face at the right instant.'),
        plates=[dict(key='p21_caravaggio', cap='Follow the first read: a shaft of light, the pointing hand, then the faces that answer it. Contrast, position, and direction make an order without numbered instructions.')],
        story=[
            ('Visual hierarchy is not one magic feature. Size, contrast, position, isolation, sharpness, colour, and the direction of an edge all change the relative weight of an element. A large pale image may lose to a small black mark. A face near the centre may lose to a bright hand at the edge. The useful question is not where the eye must go, but which element is most likely to win attention under this task, distance, and screen size.'),
            ('Caravaggio makes the mechanism easy to see in <i>The Calling of Saint Matthew</i>. A bright diagonal enters from the upper right, continues through a pointing hand, and lands in a cluster of faces. The painting does not put a headline above the scene. It builds a chain of salience: light separates the event from the room, gesture supplies direction, and the seated group supplies the answer. The reading is an interpretation of the work, not proof that the painter used a modern design label.'),
            ('Checked Oct 2026: hierarchy holds up as a design need, but a fixed eye path does not. NN/g treats scale, contrast, colour, placement, and spacing as controls; attention research also warns that salience and importance are different. Start with the job, make one variable dominant, then blur the page or shrink the frame. If the wrong thing wins, lower its contrast or give the intended subject more isolation. On a web page, let image, promise, evidence, and action have visibly different jobs.'),
            ('A useful audit is brutally simple. Open the design at the size people will actually use it, look away, then look back for two seconds and name the first three things you saw. Repeat in grayscale and with the hero image hidden. If the page has no stable first read, do not add more decoration. Reassign weight: enlarge the subject, quieten the badge, move the action closer to the decision, or increase the gap around the crucial line. The same audit works on a film frame: pause at the intended cut point and ask what information the viewer received before the shot ended. Repeat the test with sound removed, because sound can redirect attention.'),
        ],
        look=[
            ('The Calling of Saint Matthew, Caravaggio', 'Trace light to hand to faces. Notice how a directional cue can also be a story cue.', 'https://commons.wikimedia.org/wiki/File:The_Calling_of_Saint_Matthew-Caravaggo_(1599-1600).jpg'),
            ('The Calling of Saint Matthew, Contarelli Chapel', 'Look at the painting at full scale if possible, then as a thumbnail. The hierarchy survives reduction because the value pattern is strong.', 'https://www.sanluigidifrancesi.org/en/church/the-contarelli-chapel'),
            ('Vermeer exhibition text, Rijksmuseum', 'Compare Caravaggio with Vermeer: a controlled patch of light can organise attention without outlining every subject.', 'https://www.rijksmuseum.nl/en/whats-on/exhibitions/past/vermeer/vermeer-exhibition-text'),
            ('Citizen Kane, deep staging', 'Watch how foreground, middle ground, and background can compete for narrative priority instead of flattening a scene.', 'https://www.bfi.org.uk/features/citizen-kane-deep-focus'),
        ],
        steal=[
            'Write the intended first, second, and third reads beside a hero layout before styling it.',
            'Use one dominant contrast, then mute competing text, badges, and decoration.',
            'Test the page at thumbnail size and on a low contrast display, not only on your design monitor.',
        ],
        director=('Block the frame so the emotional fact needed for the next beat has the clearest first read. '
                  'Then hide or delay that hierarchy when suspense depends on the audience noticing the wrong thing first.'),
        studio=('For a safari landing page, make the animal or landscape the first read, the place and season the second, and the booking action the third. '
                'Do not let a large logo or a bright cookie prompt steal the subject.'),
        sources=[
            ('Wagemans et al., grouping and figure-ground review', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3482144/'),
            ('NN/g, principles of visual design', 'https://www.nngroup.com/articles/principles-visual-design/'),
            ('Treisman and Souther, visual search', 'https://doi.org/10.1037/0096-3445.114.3.285'),
            ('Rijksmuseum, Vermeer exhibition text', 'https://www.rijksmuseum.nl/en/whats-on/exhibitions/past/vermeer/vermeer-exhibition-text'),
        ],
    ),
    dict(
        id='2.2',
        title='When dots become a group',
        q='Why do scattered dots become a group?',
        why=('A crowd can become a pattern before it becomes a picture. Gestalt research gives a vocabulary for that jump, useful whenever a designer turns data into a map or a director turns many bodies into one force.'),
        plates=[dict(key='p22_seurat', cap='Stand back, then move close. At distance, neighbouring marks merge into colour and figures; up close, the separate dots remain visible. Proximity and similarity cooperate.')],
        story=[
            ('In 1923, Max Wertheimer described classic grouping tendencies including proximity, similarity, good continuation, closure, common fate, and symmetry. They are not six commands or a complete theory of vision. They are recurring relationships: things near one another, alike, aligned along a path, moving together, or enclosed in one region can be experienced as belonging together. Common region is especially useful in layouts, even though it was developed as a later grouping principle rather than one of the original short lists.'),
            ('Seurat\'s <i>A Sunday Afternoon on the Island of La Grande Jatte</i> is a good looking lesson because the work changes with distance. Small marks of related colour sit near one another, so the visual system combines them into larger fields. Similarity helps, proximity helps, and the bodies and umbrellas form larger social units through placement. This is not a claim that one Gestalt law explains the painting. It is a way to inspect what the marks are doing together.'),
            ('Checked Oct 2026: grouping holds up as a robust perceptual regularity, with boundary conditions. Wagemans and colleagues stress that stimulus structure interacts with attention, experience, and context. On a website, use the lightest cue that makes the relationship clear: a gap before a box, a shared shape for repeated controls, or one pale region around related content. A border is not automatically clearer. In a film, synchronized movement can group a herd, a crowd, or a line of dancers, but animate only what really belongs together, and preserve a reduced-motion alternative.'),
            ('The laws can also compete. Similar colour may group two distant items, while proximity may group two unlike items. Closure can let a cropped animal remain legible, but too much omission becomes a guessing task. Common region can gather a heading and image even when their colours differ. Design is the choice of which cue should win when cues disagree. For a chart, use position and labels first, colour second, because colour alone can fail for some viewers. For a director, ask whether bodies are a crowd, a family, or separate witnesses, then give the block a relationship that can be seen before it is explained.'),
        ],
        look=[
            ('A Sunday Afternoon on the Island of La Grande Jatte, Georges Seurat', 'Switch between thumbnail and close view. The whole and the marks are both part of the experience.', 'https://commons.wikimedia.org/wiki/File:A_Sunday_on_La_Grande_Jatte,_Georges_Seurat,_1884.jpg'),
            ('Otl Aicher Olympic pictograms, Munich 1972', 'Similarity of stroke, proportion, and pose lets a family of signs read as one system.', 'https://www.smithsonianmag.com/arts-culture/the-history-of-the-olympic-pictograms-how-designers-hurdled-the-language-barrier-4661102/'),
            ('Wes Anderson, The Grand Budapest Hotel', 'Look for repeated costume, colour, and spatial cues that turn separate characters into social units.', 'https://www.bfi.org.uk/features/grand-budapest-hotel-wes-anderson'),
            ('Wagemans et al., Gestalt grouping review', 'Read the evidence behind the familiar laws, including where simple law lists become too neat.', 'https://doi.org/10.1037/a0029333'),
        ],
        steal=[
            'Group a booking form with spacing first, then add a border only if the task still needs enclosure.',
            'Give primary controls a shared visual grammar, but keep one contrast cue for the current or most important state.',
            'For a film frame, place bodies close or align their movement when you want one social unit, and isolate one body when you want rupture.',
        ],
        director=('A crowd becomes a character when blocking gives it common direction, tempo, or shape. '
                  'Cut against that grouping when one person stops, turns, or refuses the shared movement.'),
        studio=('A safari itinerary can group drive times, sightings, and lodge nights by a shared region and rhythm rather than putting every item in a separate card. '
                'Similarity should tell the visitor what belongs together, not merely make the page look consistent.'),
        sources=[
            ('Wagemans et al., A century of Gestalt psychology I', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3482144/'),
            ('APA Dictionary, Gestalt principles', 'https://dictionary.apa.org/gestalt-principles-of-organization'),
            ('Wertheimer, 1923 discussion via Oxford Research Encyclopedia', 'https://academic.oup.com/edited-volume/62246/chapter/550959844'),
            ('Smithsonian, Olympic pictograms', 'https://www.smithsonianmag.com/arts-culture/the-history-of-the-olympic-pictograms-how-designers-hurdled-the-language-barrier-4661102/'),
        ],
    ),
    dict(
        id='2.3',
        title='When the empty shape speaks',
        q='Can an empty shape become the subject?',
        why=('The blank around a form can be as active as the form itself. Figure-ground and negative space let a logo, page, or frame make the viewer complete a second subject without adding another object.'),
        plates=[dict(key='p23_hasegawa', cap='The trees are not the whole picture. Mist, paper, and the intervals between trunks hold the depth, pace, and scale of the scene.')],
        story=[
            ('Figure-ground is the perceptual separation between a salient figure and its supporting field. Edgar Rubin\'s 1915 demonstrations made the reversal memorable: one outline can become either a vase or two facing profiles, depending on which side owns the border. The important design lesson is not the puzzle itself. It is that an apparently empty field has a contour, a weight, and a possible subject. Negative space is not leftover background; it is a shape that can frame, separate, imply, or reverse.'),
            ('The white arrow in the FedEx wordmark is a compact modern example. It is not drawn as an extra icon. The counterform between the E and x makes the arrow available when the viewer notices the relationship. In Hasegawa Tohaku\'s <i>Pine Trees</i>, pale intervals and mist do a different job: they withhold detail while making the sparse ink forms feel distant and atmospheric. Japanese <i>ma</i> is more than minimalism or unused space. It names an interval whose presence is part of the experience, so do not reduce it to a Western formula.'),
            ('Checked Oct 2026: figure-ground is well supported, but reversals depend on border ownership, shape, depth, attention, and experience. Make the primary figure stable when a task must be easy, and let the ground become ambiguous only when ambiguity is the point. For a website, try removing a border and increasing the gap around the action. For a frame, let a doorway, pool of light, or patch of mist turn the surrounding field into a participant.'),
            ('There is a practical safety check here. A clever counterform is useless if people cannot tell what is clickable, readable, or important. Test a logo at small size, test text against its real image background, and do not make the only state change depend on a subtle reversal. In a clinic site, the appointment action must remain a stable figure even if the brand system enjoys ambiguity. In a film, ambiguity can be held for a beat because time and sound can supply context; in a form, the user should not have to solve a visual riddle before submitting. Clarity is not the enemy of a memorable mark; it is the condition that lets the memory land.'),
        ],
        look=[
            ('Rubin vase', 'Find the reversible outline. Ask which side owns the edge, and how quickly the subject changes when you reverse the reading.', 'https://www.bps.org.uk/psychologist/looking-back-figure-and-ground-100'),
            ('FedEx Corporation logo', 'Look between the letters, not only at the letters. The arrow is a counterform, not a separately drawn object.', 'https://www.artcenter.edu/about/alumni/alumni-stories/lindon-leader.html'),
            ('Pine Trees, Hasegawa Tohaku', 'Treat mist as a designed interval. It separates trunks, suggests distance, and keeps the screen from becoming a catalogue of marks.', 'https://commons.wikimedia.org/wiki/File:Hasegawa_Tohaku_-_Pine_Trees_(Sh%C5%8Drin-zu_by%C5%8Dbu)_-_left_hand_screen.jpg'),
            ('Rei Kawakubo, Art of the In-Between', 'Use the museum\'s account of in-between space as a prompt, not as a claim that all empty space is Japanese ma.', 'https://www.metmuseum.org/exhibitions/listings/2017/rei-kawakubo/exhibition-galleries'),
        ],
        steal=[
            'Draw the surrounding shape around a logo or hero subject before adding another graphic element.',
            'Give one key action a quiet field so its boundary can be read without a heavy box.',
            'In a film frame, use a doorway, silhouette, or mist to make the ground carry a second possibility.',
        ],
        director=('Suspense often begins when the ground is not neutral. Keep the actor readable when you need identification, then let the background threaten to become the subject before the reveal.'),
        studio=('A lodge page can let sky, water, or a quiet margin give an animal scale. An empty state can be a calm pause with a clear next action, not a dead screen full of filler.'),
        sources=[
            ('British Psychological Society, history of figure and ground', 'https://www.bps.org.uk/psychologist/looking-back-figure-and-ground-100'),
            ('Wagemans et al., grouping and figure-ground review', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3482144/'),
            ('ArtCenter, Lindon Leader and the FedEx arrow', 'https://www.artcenter.edu/about/alumni/alumni-stories/lindon-leader.html'),
            ('Iliescu, account of Japanese ma', 'https://doi.org/10.4324/9781003007654-5'),
        ],
    ),
    dict(
        id='2.4',
        title='Spacing can be a border',
        q='Can spacing beat a border?',
        why=('A gap can group one thing and separate another without adding visual noise. This is the quiet craft behind readable Swiss posters, good forms, and web pages that feel organised without turning every module into a card.'),
        plates=[dict(key='p24_muller', cap='Even a busy station poster needs a first read. The large portrait and type form a tight unit, while surrounding station space keeps the message from dissolving into the background.')],
        story=[
            ('Whitespace has at least three jobs: it separates, groups, and gives a form room to register. A small gap inside a label and input says they belong together; a larger gap before the next label says a new group begins. This is proximity in practice, and it is why a page with identical gaps everywhere can feel oddly ambiguous. Space is not a premium decoration. It is a relationship between objects.'),
            ('Swiss and International Typographic Style makes the relationship visible through alignment, modular placement, photography, and controlled hierarchy. Josef Muller-Brockmann\'s <i>Musica Viva</i> poster is not calm because it lacks energy. Its circles, diagonal movement, type, and margins sit in a repeatable order. The eye can feel a beat because distances recur, then notice the exceptions. A visible border would add another line and another decision; the gaps already do the grouping.'),
            ('Checked Oct 2026: spacing as a grouping cue holds up, but there is no universal amount of whitespace. Reading measure, touch targets, language, screen size, and content density change the answer. Start with a small spacing scale, make related things closer than unrelated things, and test at the actual viewport. On the web, let CSS grid or flexbox preserve the relations rather than nudging each object by eye. In a film frame, a gap between two characters can be social distance, not merely composition.'),
            ('The border is not the enemy. It is a strong grouping signal, so use it when the boundary itself matters: a selected plan, a dangerous destructive action, a map region, or a form error. But if every paragraph receives a rectangle, the page loses its larger rhythm and the eye must decode too many competing containers. A soft background field, a shared alignment edge, or a change in vertical interval can be enough. Compare the same page with borders removed, then add back only the ones that carry information. The lighter version often reveals the actual hierarchy. On small screens, recompose the spacing rather than merely shrinking the desktop layout. The thumb is part of the composition, so spacing must survive touch. Check both hands.'),
        ],
        look=[
            ('Musica Viva, Josef Muller-Brockmann', 'Look for recurring intervals and aligned structures. The order is felt in the empty field as much as in the circles.', 'https://commons.wikimedia.org/wiki/File:Musica_Viva._M%C3%BCller-Brockmann.jpg'),
            ('Grid systems in graphic design, Josef Muller-Brockmann', 'Inspect the construction diagrams and notice that a grid is a repeatable coordinate system, not a requirement to show lines.', 'https://ia902309.us.archive.org/4/items/GridSystemsInGraphicDesignJosefMullerBrockmann/Grid%20systems%20in%20graphic%20design%20-%20Josef%20Muller-Brockmann.pdf'),
            ('Swiss International Typographic Style overview', 'Compare asymmetric type, photography, and modular order rather than copying a narrow visual stereotype.', 'https://pages.gseis.ucla.edu/faculty/drucker/HoB_Site/Resources/Kope_Reference.html'),
            ('A well-grouped web form', 'Observe how label, field, help, and error message need proximity, while sections need larger intervals.', 'https://www.nngroup.com/articles/principles-visual-design/'),
        ],
        steal=[
            'Make related label, image, and action a tight cluster, then use a visibly larger gap before the next cluster.',
            'Try removing every card border from a page and keep only alignment, background regions, and spacing that carry real meaning.',
            'Choose four or five spacing tokens and let exceptions be deliberate, documented, and rare.',
        ],
        director=('Leave a measured gap in blocking and the audience will read a relationship before anyone speaks. A character outside the group can be separated by space alone.'),
        studio=('Use whitespace around a lodge promise and between itinerary groups so the visitor can scan without a wall of cards. Keep tap targets generous even when the visual gaps are tight.'),
        sources=[
            ('Smashing Magazine, space and figure-ground', 'https://www.smashingmagazine.com/2014/05/design-principles-space-figure-ground-relationship/'),
            ('Smashing Magazine, layout grids', 'https://www.smashingmagazine.com/2017/12/building-better-ui-designs-layout-grids/'),
            ('Muller-Brockmann, Grid Systems in Graphic Design', 'https://ia902309.us.archive.org/4/items/GridSystemsInGraphicDesignJosefMullerBrockmann/Grid%20systems%20in%20graphic%20design%20-%20Josef%20Muller-Brockmann.pdf'),
            ('NN/g, principles of visual design', 'https://www.nngroup.com/articles/principles-visual-design/'),
        ],
    ),
    dict(
        id='2.5',
        title='Give the eye a next move',
        q='Where will the gaze go next?',
        why=('A composition is not only a set of objects; it is a route through them. Leading lines, eyelines, perspective, and reading order can make the next beat available, but honest design treats gaze patterns as tendencies to test, not laws to obey.'),
        plates=[dict(key='p25_hokusai', cap='The wave curves around the boats and opens toward Mount Fuji. Opposing arcs, tiny figures, and the distant triangle create a route through scale and danger.')],
        story=[
            ('Leading lines are edges, curves, gaze directions, perspective lines, shadows, or moving objects that suggest where attention could travel. Good continuation helps a smooth contour feel connected, while common fate groups things that move together. A face looking off screen can lend its direction to an empty region. These cues are invitations, not ropes. Contrast, task, culture, language direction, and prior knowledge can override them.'),
            ('In Hokusai\'s <i>The Great Wave off Kanagawa</i>, the curling wave encloses tiny boats and sends the eye along its arc toward the pale opening and Mount Fuji. That is a visual reading, not a documented statement of Hokusai\'s intention. In film, an eyeline or road can point to the next story beat; in a web page, image crop, heading order, and the sequence from promise to evidence to action can make scrolling feel like a path rather than a pile.'),
            ('Checked Oct 2026: web scan patterns need honesty. NN/g found a common F-shaped pattern in an early study of text-heavy pages, then clarified that F is not universal and that good structure can change it. Its later synthesis includes layer cake, spotted, commitment, exhaustive, bypassing, zigzag, and sequential patterns. Do not make a page worse to imitate a heatmap. Put essential information in headings, labels, bullets, and meaningful first words, then watch real users at the real duration and viewport.'),
            ('Leading lines should end somewhere useful. A road that exits behind the subject can create openness; a bright diagonal that ends on an irrelevant badge is just a leak in the composition. For a web page, the next move may be a scroll, a comparison, a caption, or an action, so make that destination visible and accessible. For a film shot, a gaze cue can be broken by an actor looking toward something the cut withholds. That delay creates curiosity because the viewer understands the route but not the destination. Test the shot at its real duration, not only as a still. A line that works in a poster may vanish during a fast cut. Direction needs time as well as geometry. Hold the cue long enough.'),
        ],
        look=[
            ('The Great Wave off Kanagawa, after Hokusai', 'Trace the wave curve, boats, white space, and Mount Fuji. The path alternates between near danger and distant stillness.', 'https://commons.wikimedia.org/wiki/File:The_Great_Wave_off_Kanagawa.jpg'),
            ('North by Northwest, Alfred Hitchcock', 'Watch how roads, glances, and screen direction continue motion across cuts and make the next space legible.', 'https://www.bfi.org.uk/features/north-northwest'),
            ('F-shaped pattern for reading web content, NN/g', 'Read both the original finding and the later correction. A common scan is not a reading commandment.', 'https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/'),
            ('How people read online, NN/g', 'Compare F, layer cake, spotted, and sequential patterns, and ask which one your content task invites.', 'https://www.nngroup.com/articles/how-people-read-online/'),
        ],
        steal=[
            'Draw three arrows on a hero layout: first look, next evidence, then action. Remove any arrow that lands on irrelevant decoration.',
            'Use meaningful first words in headings and captions, not a beautiful line that hides the point.',
            'Match screen direction and eyelines across cuts unless the break is the story.',
        ],
        director=('Give the viewer an eyeline, road, gesture, or moving body that points toward the next piece of information. Then let a withheld look or a wrong direction create suspense.'),
        studio=('Order a safari page as promise, proof, practical detail, and booking action. Use the animal\'s gaze or the trail of a landscape to invite the next scroll, never to conceal essential labels.'),
        sources=[
            ('Wagemans et al., good continuation and grouping', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3482144/'),
            ('NN/g, original F-shaped study', 'https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content-discovered/'),
            ('NN/g, update on F-shaped reading', 'https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/'),
            ('NN/g, how people read online', 'https://www.nngroup.com/articles/how-people-read-online/'),
            ('The Met, Hokusai Great Wave', 'https://www.metmuseum.org/art/collection/search/45434'),
        ],
    ),
    dict(
        id='2.6',
        title='Make order breathe',
        q='What makes order feel alive instead of boring?',
        why=('A system becomes expressive when repetition creates expectation and variation gives that expectation something to notice. Grids, alignment, and rhythm let a page or frame feel coherent without making every unit identical.'),
        plates=[dict(key='p26_mondrian', cap='Mondrian repeats verticals, horizontals, white fields, and a small colour vocabulary, but the cells are not equal. The order feels alive because the pattern has pressure and variation.')],
        story=[
            ('Repetition makes a family: the same type roles, icon stroke, shot size, or spacing unit can tell the viewer that separate moments belong to one world. Rhythm is repetition with change over space or time. It can vary interval, scale, density, direction, or duration. Alignment gives the family a spine. Variation tells the viewer where to look. Without repetition, everything competes. Without variation, nothing matters more than anything else.'),
            ('Mondrian\'s <i>Composition with Yellow, Blue and Red</i> is a useful still object for this balance. Black lines and a limited colour vocabulary establish the system, but the rectangles do not repeat like wallpaper. Uneven fields create weight, pause, and asymmetrical tension. A grid is similarly a scaffold, not a visible prison. Müller-Brockmann used modular systems to make coherent families of posters, while Sol LeWitt made a system generate many different outcomes. The named makers illustrate practices; do not assume one rule explains their whole work.'),
            ('Checked Oct 2026: grids hold up as production and consistency tools, not as a universal aesthetic law. Use a grid to make alignment, responsiveness, and collaboration easier, then break it at a meaningful point: a hero image crossing columns, a title that interrupts the baseline, or a film frame that breaks a visual rule when the story changes. On a safari site, repeat the design-system tokens and card logic, but vary the crop, scale, and density to distinguish habitat, season, and action.'),
            ('A useful break has a before and after. First show the viewer a stable unit, such as a repeated card, centred portrait, regular beat, or aligned title. Then change one variable and let that change carry meaning. If every card is an exception, none is an exception. If a film begins with loose handheld fragments, a sudden perfect alignment may feel less like a break and more like a continuation of the established language. Name the rule in plain language before you violate it: what repeats, what changes, and why the viewer needs to feel that difference now. Variation is strongest when it changes a decision, not only the surface texture. Let the content earn the exception.'),
        ],
        look=[
            ('Composition with Yellow, Blue and Red, Piet Mondrian', 'Find the repeated rules, then find the unequal cells that make the field breathe instead of becoming wallpaper.', 'https://commons.wikimedia.org/wiki/File:Composition-with-red-yellow-and-blue.jpg'),
            ('Musica Viva, Josef Muller-Brockmann', 'See how circles, diagonal movement, type, and a modular order produce intensity without random placement.', 'https://commons.wikimedia.org/wiki/File:Musica_Viva._M%C3%BCller-Brockmann.jpg'),
            ('Sol LeWitt wall drawings', 'Compare a rule that generates many outcomes with a template that merely repeats one answer.', 'https://massmoca.org/sol-lewitt/'),
            ('Wes Anderson, centred symmetry and repetition', 'Notice how repeated framing, props, palettes, and entrances become a voice, then vary at the moment the story needs friction.', 'https://www.studiobinder.com/blog/wes-anderson-symmetry/'),
        ],
        steal=[
            'Define a small design system for type, spacing, image crops, and action states, then reserve one controlled anomaly per screen.',
            'Break the grid only where the content has a reason to become louder, closer, or less stable.',
            'For a film, repeat a shot size, sound, object, or blocking pattern until its variation carries story meaning.',
        ],
        director=('Give a film a visual grammar, then let a broken alignment, changed rhythm, or unexpected scale announce that the character or world has changed. The violation works because the audience has learned the rule.'),
        studio=('Use repeated modules to make safari offerings easy to compare, but let a flagship habitat, a rare sighting, or a booking moment cross the usual pattern. The exception should be meaningful, not a decorative stunt.'),
        sources=[
            ('Lupton and Phillips, Graphic Design: The New Basics contents', 'https://catdir.loc.gov/catdir/toc/ecip0725/2007033805.html'),
            ('Muller-Brockmann, Grid Systems in Graphic Design', 'https://ia902309.us.archive.org/4/items/GridSystemsInGraphicDesignJosefMullerBrockmann/Grid%20systems%20in%20graphic%20design%20-%20Josef%20Muller-Brockmann.pdf'),
            ('Wong, Principles of Form and Design', 'https://www.wongwucius.com/publication'),
            ('Wagemans et al., grouping and whole properties', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3482144/'),
            ('StudioBinder, Wes Anderson symmetry', 'https://www.studiobinder.com/blog/wes-anderson-symmetry/'),
        ],
    ),
]

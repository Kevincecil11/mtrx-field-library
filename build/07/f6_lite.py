IMAGES = {
    'p61_wainwright': dict(
        file='File:Louis Sullivan - Wainwright Building, Seventh + Chestnut Streets, Saint Louis, St. Louis City County, MO.jpg',
        credit='Paul Piaget for Historic American Buildings Survey, Wainwright Building, 1967',
        lic='Public domain',
        alt='The tall red brick Wainwright Building, with a tripartite base, shaft and richly ornamented crown.'),
    'p62_jali': dict(
        file='File:Sidi Saiyyed jali.jpg',
        credit='Saket K. Lakhia, Sidi Saiyyed jali, 2017',
        lic='CC BY-SA 4.0',
        alt='The intricate stone tree-of-life lattice window inside Sidi Saiyyed Mosque in Ahmedabad.'),
    'p64_bauhaus': dict(
        file='File:Bauhaus building in Dessau.jpg',
        credit='Marczoutendijk, Bauhaus building in Dessau, 2011',
        lic='CC BY-SA 4.0',
        alt='The Bauhaus building in Dessau, a long modernist complex with a glass curtain wall.'),
    'p65_braun': dict(
        file='File:Braun SK 4.1.jpg',
        credit='With Associates, Braun SK 4.1 by Dieter Rams and Hans Gugelot, 2008',
        lic='CC BY-SA 2.0',
        alt='A cream and grey Braun SK 4 radio and record player with a clear lid and restrained controls.'),
    'p66_church': dict(
        file='File:Church of the Light.jpg',
        credit='Chun-Hung Eric Cheng, Church of the Light, 2013',
        lic='CC BY 2.0',
        alt='Tadao Ando Church of the Light, showing a dark concrete interior cut by a cross-shaped opening.'),
    'p67_salk': dict(
        file='File:Salk Institute.jpg',
        credit='TheNose, Salk Institute courtyard, 2006',
        lic='CC BY-SA 2.0',
        alt='The Salk Institute courtyard, with monumental concrete buildings and a narrow water channel facing the sea.'),
    'p68_iima': dict(
        file='File:Indian Institute of Management Ahmedabad, panorama.jpg',
        credit='Mahargh Shah, Louis Kahn Plaza, IIM Ahmedabad, 2011',
        lic='CC BY-SA 3.0',
        alt='A panoramic view of Louis Kahn Plaza at the Indian Institute of Management Ahmedabad, surrounded by brick buildings.'),
    'p69_papanek': dict(
        file='File:Victor Papanek, RIT NandE Vol13Num3 1981 Jan22 Complete.jpg',
        credit='Rochester Institute of Technology, portrait of Victor Papanek, 1981',
        lic='Public domain',
        alt='A black and white portrait of designer and design critic Victor Papanek.'),
}

STOPS = [
    dict(
        id='6.1',
        title='When does form actually follow function?',
        q='What did Louis Sullivan mean by form following function, and what happens when a website has more than one function?',
        why='The slogan sounds like a command to make everything plain. The original argument is more interesting: a new building type needs a form that can express its changing life, which is a useful way to think about interfaces, services and films too.',
        plates=[dict(key='p61_wainwright', cap='Louis Sullivan and Dankmar Adler, Wainwright Building, 1891. Read the facade as a vertical sentence: a public base, a repetitive office shaft, and a crown that gives the height a finish. The ornament is not the opposite of function here; it helps the building explain its scale.')],
        story=[
            'In his 1896 essay on the tall office building, Louis Sullivan wrote, "Whether it be the sweeping eagle in his flight, or the open apple-blossom, the toiling work-horse, the blithe swan, the branching oak, the winding stream at its base, the drifting cloud over all the sun, the form ever follows the function, and this is the law." The short slogan is a compression. Sullivan was looking at a genuinely new type, the steel-framed office tower, and asking how its outward form could grow from its inner life rather than pretend it was a low classical building. The Wainwright Building makes that legible through base, shaft and crown.',
            'The Bauhaus later made function more practical and more social: understand materials, production, users and the work an object must do before styling it. But function is not a single mechanical answer. A clinic website must help a patient find a doctor, reassure a worried family, support staff and protect privacy. A safari site must sell a booking while also setting honest expectations about wildlife, weather and local livelihoods. Those functions change with context, technology and time. A memorial, temple or film title also has emotional and symbolic functions. The useful question is not, "Is this decorative?" It is, "Which human job is this formal choice doing?"',
            'Try a five-minute audit. Hide the logo, colour and photography on a landing page, then write the five actions that remain. Restore one expressive choice at a time and say what it adds: trust, orientation, memory, delight or place. A design fails Sullivan when its form ignores the work. It also fails when it reduces the work to a button and forgets that people need meaning. Function is a moving target, so the form has to be a responsive system, not a frozen slogan. The same test works on a film set. A prop, camera move or cut should answer what the audience needs to know now, while leaving enough ambiguity for the scene to remain alive. A useful interface and a memorable frame are not opposites: both guide attention while giving the person on the other side a reason to continue.'
        ],
        look=[
            ('Wainwright Building, Louis Sullivan and Dankmar Adler, 1891', 'Notice how natural ornament and vertical structure cooperate rather than cancel each other.', 'https://commons.wikimedia.org/wiki/File:Louis_Sullivan_-_Wainwright_Building,_Seventh_%2B_Chestnut_Streets,_Saint_Louis,_St._Louis_City_County,_MO.jpg'),
            ('Braun SK 4, Dieter Rams and Hans Gugelot, 1956', 'Controls, lid and proportions make the user task readable without making the object mute.', 'https://www.moma.org/collection/works/3441'),
            ('GOV.UK design system', 'A live example of function as changing service work: content, accessibility, search and transactions share one system.', 'https://design-system.service.gov.uk/'),
            ('The Sagrada Família, Antoni Gaudí', 'A reminder that a building can function as structure, ritual, symbol and civic memory at once.', 'https://sagradafamilia.org/'),
        ],
        steal=['Write the user actions and the service promises before choosing a visual direction.', 'Give each major visual choice a job, then remove the choices whose job you cannot name.', 'Design a site that can absorb new content and changing user needs instead of treating the first launch as its final form.'],
        director='A director treats form as behaviour: the camera, cut and set should reveal what a character wants and what the scene withholds. Let a formal rule change when the character\'s function in the story changes.',
        studio='For a safari or clinic site, put dates, availability, price, access and trust where the eye can find them, then let Ahmedabad light, wildlife and local material supply the mood.',
        sources=[('Sullivan, The Tall Office Building Artistically Considered, 1896', 'https://archive.org/details/tallofficebuildi00sull'), ('Getty, Bauhaus curriculum', 'https://www.getty.edu/research/exhibitions_events/exhibitions/bauhaus/new_artist/history/principles_curriculum/'), ('GOV.UK design system', 'https://design-system.service.gov.uk/'), ('MoMA, Braun SK 4', 'https://www.moma.org/collection/works/3441')]
    ),
    dict(
        id='6.2',
        title='Is ornament a crime or a meaning?',
        q='When does decoration waste attention, and when does a pattern carry identity, memory or climate?',
        why='Adolf Loos made anti-ornament a modernist weapon, while William Morris defended useful beauty and dignified making. Ahmedabad\'s Sidi Saiyyed jali makes the argument tactile: the pattern is not an added sticker, but stone, shade, craft and civic memory together.',
        plates=[dict(key='p62_jali', cap='Sidi Saiyyed jali, Ahmedabad, built 1572 to 1573. Follow the branches, but also notice their work: the perforated stone filters light and air, turns a wall into a threshold, and makes a local story visible. Its meaning is material, environmental and cultural at once.')],
        story=[
            'Adolf Loos\'s lecture "Ornament and Crime" was delivered in 1910, although he later dated the essay 1908; its publication history is complicated and English translations vary. His target was applied ornament on utilitarian objects, which he saw as wasteful and tied to a regressive culture of consumption. The useful part of the argument is lifecycle reasoning: a surface that costs time, material and maintenance should earn its place. The dangerous part is treating one culture\'s restraint as a universal measure of progress, especially when the polemic contains racist and demeaning claims.',
            'William Morris offers a wider test. In "The Beauty of Life" he urged people to have nothing in their houses that they do not know to be useful or believe to be beautiful. Useful can include comfort, orientation, ritual and joy, not only mechanical efficiency. The Sidi Saiyyed jali in Ahmedabad shows why this matters. Its tree-like stone lattice is ornament, but it is also a filter for sun, a skilled construction, an image of place and a remembered civic sign. Calling it merely decoration would miss the work it does. Ornament becomes a problem when it hides a fee, imitates a material dishonestly or consumes attention without giving anything back.',
            'Use an intentionality audit. Remove every decorative element from a page or object, then restore only what carries information, tactility, identity, delight or cultural meaning. Ask who gets to label a visual language excessive, and who paid for the labour behind it. A quiet interface can still have a signature, and a richly patterned one can still have hierarchy. The aim is not to choose Loos or Morris forever. It is to make the reason for the mark visible. That reason can be modest. A line may protect a fragile edge, a colour may identify a neighbourhood, and a repeated motif may help someone recognise home. The test is whether the detail survives contact with real use, real maintenance and the people whose history it invokes. A borrowed motif needs the same care as a borrowed sentence: name its source, understand its context and do not flatten a living tradition into a brand shortcut.'
        ],
        look=[
            ('Sidi Saiyyed Mosque jali, Ahmedabad', 'Look through the stone, not just at its outline: shade, air, craft and symbol are one detail.', 'https://commons.wikimedia.org/wiki/File:Sidi_Saiyyed_jali.jpg'),
            ('William Morris, Arts and Crafts', 'Compare pattern as skilled labour and cultural pleasure with pattern used only as surface branding.', 'https://www.vam.ac.uk/articles/arts-and-crafts-an-introduction'),
            ('Adolf Loos, Ornament and Crime', 'Read the date and translation notes before accepting the slogan as a neutral law.', 'https://depts.washington.edu/vienna/documents/Loos/Loos_Ornament.htm'),
            ('Memphis design, postmodern pattern', 'A deliberate excess can signal play and plurality, provided the visual hierarchy survives.', 'https://www.moma.org/collection/terms/memphis'),
        ],
        steal=['Make pattern do one concrete job, such as filtering attention, marking a place or encoding a category.', 'Show the making or maintenance cost of a decorative choice before calling it free.', 'Pair a restrained navigation system with one local, memorable visual gesture instead of applying motifs everywhere.'],
        director='Production design uses ornament to tell us who has money, what a room remembers and what a character refuses. Let a repeated pattern change meaning when the scene changes, rather than using it as wallpaper.',
        studio='On an Ahmedabad-facing brand, use local pattern with attribution and context, not as an exotic texture pack. On a clinic site, reserve ornament for warmth and wayfinding so critical information remains calm.',
        sources=[('DLA Marbach, Loos publication history', 'https://www.dla-marbach.de/find/opac/id/AK00238737'), ('University of Washington, Loos translation', 'https://depts.washington.edu/vienna/documents/Loos/Loos_Ornament.htm'), ('William Morris Archive', 'https://morrisarchive.lib.uiowa.edu/items/show/2483'), ('V&A, Arts and Crafts', 'https://www.vam.ac.uk/articles/arts-and-crafts-an-introduction')]
    ),
    dict(
        id='6.4',
        title='What did the Bauhaus teach before it taught a style?',
        q='Why did the Bauhaus make students handle materials and test perception before giving them a recognisable visual language?',
        why='The Bauhaus is often reduced to white walls, primary colours and geometric furniture. Its more durable invention was a first-semester laboratory where seeing, making, craft and industry met before a student settled into a style.',
        plates=[dict(key='p64_bauhaus', cap='Bauhaus Building, Dessau, designed by Walter Gropius, 1925 to 1926. Do not copy the curtain wall as a logo. Read it as the visible result of workshops, teaching, production, circulation and collective work.')],
        story=[
            'The Vorkurs, or Preliminary Course, was compulsory for first-semester Bauhaus students. Getty\'s curriculum history describes it as a half-year study of colour, form, composition, materiality, life drawing and visual analysis. Johannes Itten began it; László Moholy-Nagy and Josef Albers later led different versions. That sequence matters because there was no single Bauhaus method. Itten emphasised sensitivity to texture, colour and natural form. Moholy-Nagy brought light, technology and industrial experiment. Albers made material studies and colour relationships rigorous. The school taught students to notice before it taught them to signal "Bauhaus."',
            'The course joined craft to industry without pretending they were enemies. Students handled wood, glass, fibre, paper and metal, learning what each material could do and where it failed. Workshops then connected that knowledge to repeatable production. Marianne Brandt\'s metal objects, Anni Albers\' textiles and the school\'s furniture are not just geometric style exercises; they are investigations into hand, process, material and scale. Even the famous triangle, square and circle colour questionnaire was an experiment, not a universal code. A rule can start attention, but viewers and materials get the final say.',
            'Steal the pedagogy. Before opening Figma, give a design team one circle, one rectangle and one line, then ask for ten compositions using only scale, spacing and repetition. Make a second round from paper, wire or a phone camera. Compare what the material revealed. The point is not nostalgia for a school that had exclusions and contradictions. It is a working habit: perception first, prototypes second, style last. That habit is useful whether the output is a website, a film set or a product that must survive a factory. It also keeps a beginner from confusing confidence with competence. A polished reference gives you an answer; a small experiment gives you information. Build enough experiments that your eventual style is a consequence of seeing, handling and choosing, not a costume borrowed from a famous image. The school\'s most useful lesson is therefore not a particular palette. It is permission to be changed by evidence before claiming a signature. That is especially valuable for a studio, where a shared experiment can make critique less personal and decisions more legible.'
        ],
        look=[
            ('Bauhaus Building, Dessau, Walter Gropius, 1925 to 1926', 'See workshops, circulation and structure before seeing a modernist postcard.', 'https://commons.wikimedia.org/wiki/File:Bauhaus_building_in_Dessau.jpg'),
            ('Marianne Brandt, Teapot, 1924', 'Geometry is constrained by pouring, gripping, cleaning and serial production.', 'https://www.moma.org/collection/works/2438'),
            ('Anni Albers, textile studies', 'A grid can be tactile, variable and handmade, not only a screen layout.', 'https://www.moma.org/artists/116'),
            ('Josef Albers, Interaction of Color', 'Test a colour beside its neighbours because colour is relational, not a fixed swatch.', 'https://yalebooks.yale.edu/book/9780300179354/interaction-of-color/'),
        ],
        steal=['Start a project with material and contrast experiments, not a moodboard assembled from finished work.', 'Separate the exercise that trains perception from the component library that ships production.', 'Record failed prototypes because they reveal the constraints a polished reference hides.'],
        director='A film crew can run a Vorkurs with light, texture, lens distance and movement before choosing a look. Give the same scene three material and lighting experiments, then keep the rule that changes the audience\'s attention.',
        studio='For MTRX, make a short workshop sprint where design, copy and development build one real booking or enquiry prototype together. The shared object is more useful than a deck of adjectives.',
        sources=[('Getty, Principles and Curriculum', 'https://www.getty.edu/research/exhibitions_events/exhibitions/bauhaus/new_artist/history/principles_curriculum/'), ('Getty, Learning with Itten', 'https://www.getty.edu/research/exhibitions_events/exhibitions/bauhaus/new_artist/matter_materials/itten/'), ('Getty, Matter and Materials', 'https://www.getty.edu/research/exhibitions_events/exhibitions/bauhaus/new_artist/matter_materials/'), ('MoMA, Marianne Brandt teapot', 'https://www.moma.org/collection/works/2438')]
    ),
    dict(
        id='6.5',
        title='Does good design disappear?',
        q='What does Dieter Rams mean by good design, and how should we compare Braun, Apple and Jony Ive without reducing influence to copying?',
        why='A Braun radio can look quiet because its hierarchy is doing the talking. Rams gives that quietness a checklist, while Apple shows how restraint becomes behaviour, software and a whole product system rather than a surface resemblance.',
        plates=[dict(key='p65_braun', cap='Braun SK 4, Dieter Rams and Hans Gugelot, 1956. Notice the hierarchy: transparent lid, simple body, legible controls, and very little branding. The object does not disappear; it makes the task easier to see.')],
        story=[
            'Vitsœ publishes Dieter Rams\'s ten principles: good design is innovative; makes a product useful; is aesthetic; makes a product understandable; is unobtrusive; is honest; is long-lasting; is thorough down to the last detail; is environmentally friendly; and is as little design as possible. Rams\'s own foundation warns that these are not incontrovertible rules because technology and culture evolve. So "as little design as possible" is not a command to remove information. It is a demand that every remaining choice earn its cost.',
            'The Braun to Apple story is influence, not proof that Apple copied one Braun object. Compare tasks and systems. Braun\'s SK 4 makes tuning and playing a record legible through physical controls and a clear lid. The iPod made a larger library navigable through a central scroll wheel, software and an ecosystem. Jony Ive described his practice as inseparable from making, which explains why materials, manufacturing and use matter together. Steve Jobs made the same deeper point in a New York Times interview: "Design is how it works." A beautiful hero screen that fails at loading, error recovery, keyboard focus or privacy is not finished design.',
            'Run a ten-principle critique, but write one tradeoff beside every score. Innovation can add complexity. Unobtrusive can hide a necessary warning. Long-lasting can conflict with repair access or a changing platform. The goal is not to make every MTRX project look like Braun. It is to make the promise and the behaviour agree, then remove decoration that competes with that agreement. Good design may feel quiet because the user is busy doing the thing. The disappearance is conditional, not absolute. When a battery is low, a payment fails or consent matters, the interface should become visible and plain. Rams\'s restraint is therefore a discipline of timing: stay out of the way during ordinary use, then speak clearly when the user needs a warning, explanation or choice. That is a richer definition of disappearance than visual minimalism: the interface recedes, but responsibility does not. A good critique therefore asks not only what is visible, but what work has been made invisible and whether the user can still understand the consequences.'
        ],
        look=[
            ('Braun SK 4, Dieter Rams and Hans Gugelot, 1956', 'Compare the visual hierarchy with the physical sequence of play, tune and close.', 'https://commons.wikimedia.org/wiki/File:Braun_SK_4.1.jpg'),
            ('Vitsœ 606 Universal Shelving System', 'A product family shows how restraint can survive new arrangements rather than depend on a single pose.', 'https://www.vitsoe.com/'),
            ('Original iPod, 2001', 'Study the wheel, screen hierarchy and software context, not just the white silhouette.', 'https://americanhistory.si.edu/collections/object/nmah_1199666'),
            ('Apple Human Interface Guidelines', 'The current system makes good design a question of behaviour, consistency and accessibility.', 'https://developer.apple.com/design/human-interface-guidelines/'),
        ],
        steal=['Use Rams as a critique sheet, not a moodboard: score usefulness, clarity, honesty, detail and environmental cost.', 'Prototype the failure state and the next action after success before polishing the hero screen.', 'If you remove a visual element, write down the information or feeling it was carrying so the subtraction is accountable.'],
        director='In cinema, invisible design is blocking, sound perspective, production detail and an edit that feels inevitable. Let the audience notice the character and the consequence, not the machinery, until the story needs the machinery revealed.',
        studio='A safari booking flow should make availability, cancellation, payment and probability clear. Restraint is valuable only when it reduces cognitive work rather than hiding conditions.',
        sources=[('Vitsœ, Good design', 'https://www.vitsoe.com/us/about/good-design'), ('Rams Foundation, theses', 'https://rams-foundation.org/foundation/design-comprehension/theses/'), ('New York Times, The Guts of a New Machine', 'https://www.nytimes.com/2003/11/30/magazine/the-guts-of-a-new-machine.html'), ('Apple Human Interface Guidelines', 'https://developer.apple.com/design/human-interface-guidelines/')]
    ),
    dict(
        id='6.6',
        title='What does emptiness give the user?',
        q='When is an empty space a usable invitation rather than a blank page pretending to be minimal?',
        why='A pause can make a user feel lost, or give them room to act. Japanese ma, Tadao Ando\'s choreographed light and Kenya Hara\'s MUJI philosophy all treat absence as an active design material, not a lack of content.',
        plates=[dict(key='p66_church', cap='Tadao Ando, Church of the Light, 1989. The cross-shaped opening is powerful because the concrete has first made a dark, quiet field. Emptiness here is a sequence: approach, compression, pause, then light.')],
        story=[
            'Ma is best approached as interval or charged space between things, not as a decorative label for anything sparse. A pause can be a line of silence, a threshold, a shadow, an empty seat or a margin that lets a sentence breathe. Tadao Ando makes the pause bodily. In the Church of the Light, concrete, darkness, geometry and a controlled opening choreograph arrival and release. The lesson is not to copy exposed concrete. It is to decide what the user should notice before and after the reveal.',
            'Kenya Hara gives the idea a product and communication language through MUJI. He distinguishes Western simplicity from an emptiness that leaves room for users to handle an object in their own ways. MUJI\'s mattress with legs can become a bed, sofa or elevated floor. That is not blankness; it is a framework with spare capacity. A website can do the same with a calm information architecture, predictable type and enough margin for content, translation, accessibility and an unhurried decision. Apple\'s whitespace can clarify hierarchy, but whitespace around a hidden price or a vague button is not generosity.',
            'Prototype the gap. Remove one panel, delay one reveal, add one second of silence or increase line-height, then ask what the user does in the space. If they orient, imagine, compare or recover, the empty space is working. If they simply wonder whether the page is broken, the design has withheld a signifier. Emptiness is a gift only when the user has something to do with it. The best quiet designs are not empty of intention; they are full of room for another person\'s intention. This also explains why whitespace cannot rescue weak content. The page needs a clear promise, a readable route and a useful next move before it can offer contemplation. Remove noise, not orientation. In film terms, a held look can be generous when the viewer understands the question it is holding. Give the gap a beginning and an exit, just as you give a room a door and a page a next step. Otherwise the pause becomes a mood imposed on the user rather than a choice offered to them.'
        ],
        look=[
            ('Church of the Light, Tadao Ando, 1989', 'The opening has force because the route and the dark field prepare it.', 'https://commons.wikimedia.org/wiki/File:Church_of_the_Light.jpg'),
            ('MUJI, Kenya Hara, Visualize the philosophy of MUJI', 'Read emptiness as user freedom and product versatility, not as beige minimalism.', 'https://www.muji.com/us/flagship/huaihai755/archive/hara.html'),
            ('Water Temple, Tadao Ando, 1991', 'Watch how a concealed entrance and a descending path make the reveal an event.', 'https://www.tadao-ando.com/'),
            ('Apple Human Interface Guidelines, layout', 'Whitespace is a hierarchy tool only when controls, labels and feedback remain discoverable.', 'https://developer.apple.com/design/human-interface-guidelines/layout'),
        ],
        steal=['Name the action a pause should make possible: breathe, compare, orient, remember or choose.', 'Use one deliberate reveal in a landing page instead of exposing every section at once.', 'Treat empty states as invitations with a next step, not decorative screens with no content.'],
        director='A director uses offscreen space, silence and a held frame to let the viewer supply fear, desire or memory. The pause must change the audience\'s expectation, not merely slow the scene.',
        studio='For an eco-lodge site, let one landscape image and one sentence breathe, but keep booking, accessibility and weather information close at hand. Calm is compatible with clarity.',
        sources=[('MUJI, Kenya Hara, Visualize the philosophy of MUJI', 'https://www.muji.com/us/flagship/huaihai755/archive/hara.html'), ('Benesse Art Site, Tadao Ando', 'https://benesse-artsite.jp/en/'), ('Tadao Ando Architect', 'https://www.tadao-ando.com/'), ('Apple Human Interface Guidelines, Layout', 'https://developer.apple.com/design/human-interface-guidelines/layout')]
    ),
    dict(
        id='6.7',
        title='What does the brick want?',
        q='How can a material change the design rather than merely receive a shape chosen in advance?',
        why='Louis Kahn\'s brick conversation is a memorable metaphor, but it also points to a real practice: listen to structure, climate, labour and ageing. IIM Ahmedabad and the Salk Institute show how material can carry learning, ritual and light.',
        plates=[dict(key='p67_salk', cap='Louis Kahn, Salk Institute, 1959 to 1965. The narrow water rill pulls the eye through the courtyard toward the Pacific. Concrete, brick, light and silence turn a research institution into a place with a civic presence.')],
        story=[
            'The brick story is not a verified supernatural conversation. It is a teaching anecdote preserved in Kahn\'s talks and transcripts. In one recorded version, Kahn asks brick what it wants to be; the brick answers, "I like an arch." When Kahn proposes a cheaper concrete lintel, the brick repeats its preference. The point is not that materials have opinions. It is that design gets better when the properties, limits and dignity of a material are allowed to influence the form. A brick arch has different labour, span, weathering and meaning from a concrete beam faced with brick.',
            'At IIM Ahmedabad, Kahn used red brick, deep arches, courtyards and heavy apertures to make movement and learning memorable. The campus was developed from 1962 to 1974, with B.V. Doshi as Indian consulting architect and local interpreter. It is not simply a case of a foreign master exporting a look. Climate, construction, institution, patronage and Ahmedabad\'s material culture negotiated the result. At the Salk Institute, the courtyard, concrete and water channel make a research complex feel ordered and contemplative. Material is doing structural, sensory and institutional work at once.',
            'Use a material conversation on the next project. Ask the medium what it can do well, what it makes expensive, how it ages, who maintains it and what it asks the user to feel. For a website, material includes latency, sound, touch, data and the honesty of a loading state. Do not fake instant response if the system is thinking. The web equivalent of an arch is a form that respects its medium instead of dressing one medium up as another. A loading state that tells the truth, a keyboard route that works and a compressed image that still communicates are material decisions. They may not appear in a screenshot, but they determine whether the work is generous or merely impressive in a presentation room. A material-led process also makes collaboration easier: developers, fabricators and editors can argue from what the medium permits instead of from personal taste alone. It also gives the client something more durable than a trend: a reasoned relationship between the thing, its users and the conditions of its use.'
        ],
        look=[
            ('IIM Ahmedabad, Louis Kahn, 1962 to 1974', 'Track the arches, shadow, brick thickness and courtyards as a learning environment, not a facade style.', 'https://archives.iima.ac.in/article/4/2022-Issue-1-Louis-Kahn-and-the-IIMA-Campus.html'),
            ('Salk Institute, Louis Kahn, 1959 to 1965', 'The water line, horizon and monumental concrete give research a public and almost ritual frame.', 'https://commons.wikimedia.org/wiki/File:Salk_Institute.jpg'),
            ('Louis Kahn on brick, Facsimile Project', 'Read the recorded wording and its context rather than treating a meme version as a primary quote.', 'https://www.louisikahn.com/quotations'),
            ('Kahn on Learning, 1972', 'Kahn\'s wider account connects material, wonder, learning and the beginning of a design.', 'https://architecture-history.org/library/AJ/Louis%20Kahn%20on%20Learning.pdf'),
        ],
        steal=['Add a material and maintenance column to every design brief.', 'Let one medium-specific behaviour become the signature instead of importing a visual effect from somewhere else.', 'Show the operational system honestly, then frame the user\'s served moment with as much care as the surface.'],
        director='Production design begins with what a room is made of and what sound travels through it. Let brick, concrete, water or dust alter blocking and performance, then use the material\'s limits as narrative pressure.',
        studio='For a safari site, make bandwidth, heat, touch and image loading part of the design brief. A fast, truthful page is more material-honest than a cinematic mockup that collapses on a phone.',
        sources=[('Louis Kahn Facsimile Project, quotations', 'https://www.louisikahn.com/quotations'), ('IIMA Archives, Louis Kahn and the Campus', 'https://archives.iima.ac.in/article/4/2022-Issue-1-Louis-Kahn-and-the-Campus-Architecture.html'), ('Salk Institute, architecture', 'https://www.salk.edu/about/salk-architecture/'), ('IIM Ahmedabad, Commons panorama', 'https://commons.wikimedia.org/wiki/File:Indian_Institute_of_Management_Ahmedabad,_panorama.jpg')]
    ),
    dict(
        id='6.8',
        title='Can architecture be a social framework?',
        q='How can a building support dignity, adaptation and collective life instead of merely providing an impressive photograph?',
        why='Ahmedabad makes the question concrete. B.V. Doshi, Charles Correa and Le Corbusier built different answers through shade, courtyards, thresholds, brick, water and social programme, with climate and local clients pushing modernism into new forms.',
        plates=[dict(key='p68_iima', cap='Louis Kahn Plaza at IIM Ahmedabad. Use it as a visual bridge into Doshi\'s Ahmedabad: architecture is not only an object, but a system of routes, pauses, shade, gathering and institutional memory.')],
        story=[
            'Balkrishna V. Doshi\'s work is a strong answer to architecture as social framework. Sangath, his Ahmedabad studio, uses vaults, grass, water, shade and sunken spaces to make work feel like a shared landscape. The Pritzker citation records his description of it as an ongoing school where one learns, unlearns and relearns. Aranya Low Cost Housing in Indore scales the question up: mixed incomes, courtyards, streets and incremental homes allow residents to adapt a framework over time. The project was designed for thousands of dwellings and a large population, so the unit is not the whole design; relationships are.',
            'Charles Correa\'s Gandhi Smarak Sangrahalaya at Sabarmati Ashram uses repeated 6 by 6 metre pavilions, courtyards, water and shaded circulation to turn memory into a walkable system. Le Corbusier\'s Ahmedabad projects are another living case study, but not a single imported style. The Mill Owners\' Association Building, Sanskar Kendra, Villa Sarabhai and Villa Shodhan were negotiated with textile wealth, Indian patrons, climate, monsoon, family life and local collaboration. The deep shade, brise-soleil, terraces and open plans show how a global grammar can change when the place is allowed to answer back.',
            'Look for the social framework before the facade. Who can enter, pause, work, repair, grow, meet and change the space? Who is protected from heat, cost or surveillance, and who is excluded? A website has the same questions: can a user recover from an error, use a slow connection, read the content in bright light and ask for help? Design the relationships and future adaptations first. The beautiful photograph should be evidence of a life the system supports, not the system\'s only success metric. This is why Doshi\'s work matters for a digital maker who may never draw a building. A strong system leaves room for people to improvise without asking them to become architects. It creates a common ground, then lets different lives make it their own. That is a better definition of inclusion than adding a token image after the architecture is fixed: the structure changes because more people were considered at the beginning. Social design is not charity added to architecture after the plan is complete. It is the plan.'
        ],
        look=[
            ('Sangath, B.V. Doshi, Ahmedabad, 1980', 'Study the sequence of vaults, water, grass and shaded movement as a community of work.', 'https://www.pritzkerprize.com/laureates/balkrishna-doshi'),
            ('Aranya Low Cost Housing, B.V. Doshi, Indore, 1989', 'See mixed income, incremental growth and streets as design materials.', 'https://www.archnet.org/sites/870'),
            ('Gandhi Smarak Sangrahalaya, Charles Correa, Ahmedabad, 1963', 'A modular grid becomes humane through water, shade, thresholds and pauses.', 'https://www.gandhiashramsabarmati.org/en/visitor-information/ashram-tour-sites/ashramlocation/MTQ2.html'),
            ('Le Corbusier\'s Ahmedabad works', 'Compare four commissions and ask how patron, programme and climate alter the common vocabulary.', 'https://www.fondationlecorbusier.fr/en/work-architecture/achievements-mills-owners-association-building-ahmedabad-india-1951/'),
            ('IIM Ahmedabad, Louis Kahn and Doshi', 'A building programme becomes a negotiation among institution, local practice and material.', 'https://archives.iima.ac.in/article/4/2022-Issue-1-Louis-Kahn-and-the-Campus-Architecture.html'),
        ],
        steal=['Map a user journey as places to arrive, pause, meet, act and recover, not just as screens.', 'Design a modest base framework that residents, editors or clients can adapt without breaking the whole system.', 'Include heat, bandwidth, maintenance, cost and local knowledge in the brief before choosing the visual language.'],
        director='A director builds social architecture through entrances, corridors, thresholds and who is allowed to occupy the frame. Block a scene so the power relationship is visible in movement, not only in dialogue.',
        studio='For an eco-lodge or clinic, design the whole service ecology: arrival, accessibility, staff work, booking, uncertainty, follow-up and maintenance. Ahmedabad is a reminder that local climate and community are generative constraints, not afterthoughts.',
        sources=[('Pritzker, Balkrishna Doshi', 'https://www.pritzkerprize.com/laureates/balkrishna-doshi'), ('Archnet, Aranya Community Housing', 'https://www.archnet.org/sites/870'), ('Sabarmati Ashram, Gandhi Smarak Sangrahalaya', 'https://www.gandhiashramsabarmati.org/en/visitor-information/ashram-tour-sites/ashramlocation/MTQ2.html'), ('Fondation Le Corbusier, Ahmedabad works', 'https://www.fondationlecorbusier.fr/en/work-architecture/achievements-museum-of-the-city-ahmedabad-india-1951-1957/'), ('IIMA Archives, campus history', 'https://archives.iima.ac.in/article/4/2022-Issue-1-Louis-Kahn-and-the-Campus-Architecture.html')]
    ),
    dict(
        id='6.9',
        title='When should a designer refuse?',
        q='What does a responsible designer do when a client asks for deception, harm or a beautiful cover for a bad system?',
        why='Design decisions distribute attention, money, privacy and dignity. Papanek made social consequence central, Monteiro makes refusal a professional duty, and the First Things First manifestos ask what kinds of work deserve our limited time.',
        plates=[dict(key='p69_papanek', cap='Victor Papanek, photographed in an RIT newsletter, 1981. Papanek\'s challenge was not to make design less skilled; it was to point skill toward real needs, ecological limits and people usually ignored by the market.')],
        story=[
            'Victor Papanek\'s Design for the Real World, first published in 1971, argues that design has social and ecological consequences and should address real needs rather than only stimulate consumption. Mike Monteiro\'s Ruined by Design updates the pressure for digital work: designers help choose what enters the world, and therefore carry responsibility for what it does. This is not a purity test. A client can persuade people honestly. The refusal begins when the work depends on deception, coercion, exclusion or harm, such as hidden fees, fake scarcity, a maze to cancel, a false wildlife guarantee or a sustainability claim with no evidence.',
            'The First Things First manifesto of 1964, written by Ken Garland and signed by 22 practitioners, questioned graphic design\'s drift toward high-pressure consumer advertising and called for time to be used for education, culture and public purposes. First Things First 2000 renewed the argument with 33 signatories in a media environment more saturated by commercial messages. Neither manifesto says all commercial work is evil; both ask designers to examine priorities and power. The FTC\'s 2022 dark-patterns report gives the operational test: disguised ads, buried terms, difficult cancellation and tricks to obtain data are not merely ugly interfaces. They impair choice.',
            'Refusal should be specific and constructive. Name the harm, show the evidence, propose an honest alternative, document the decision and be ready to leave if the core request does not change. For MTRX, add an ethics gate to the brief: audience impact, accessibility, privacy, environmental claim, image rights, community representation and failure consequence. A designer is not the only decision-maker, but silence is still a design decision. The strongest boundary is often a sentence: we can help you make this clearer and more effective, but not by making the user less informed or less free. Refusal is easier when the team has agreed on the boundary before the deadline and invoice arrive. Put the rule in the proposal, share the evidence with the client and give the client a face-saving alternative. Ethics becomes practical when it is designed into the process, not saved for a heroic argument at the end.'
        ],
        look=[
            ('Design for the Real World, Victor Papanek, 1971', 'Read the critique as a demand to account for users, resources, labour and consequences.', 'https://papanek.org/archivelibrary/'),
            ('Ruined by Design, Mike Monteiro', 'Focus on the responsibility and gatekeeping argument, then test it against a real client brief.', 'https://www.ruinedby.design/'),
            ('First Things First 1964', 'The original manifesto asks whether commercial priorities are the only worthwhile use of design talent.', 'https://www.eyemagazine.com/blog/post/design-for-life'),
            ('First Things First Manifesto 2000', 'The renewal makes the same priority question explicit for a global commercial culture.', 'https://eyemagazine.com/feature/article/first-things-first-manifesto-2000'),
            ('FTC, Bringing Dark Patterns to Light, 2022', 'A practical catalogue of disguised ads, hidden costs, coercive data requests and hard-to-cancel subscriptions.', 'https://www.ftc.gov/reports/bringing-dark-patterns-light'),
        ],
        steal=['Put an ethics gate in the brief before the first visual: users, access, privacy, evidence, labour, environment and exit conditions.', 'When refusing, identify the harmful mechanism and offer a truthful route to the client\'s legitimate goal.', 'Keep a decision log so the person who approved a dark pattern cannot later call it an accidental detail.'],
        director='A director refuses a shot, performance or production practice when it harms people or falsifies the story. Ethical authorship is not the absence of conflict; it is making the boundary and its cost visible.',
        studio='For wildlife and eco-lodge clients, refuse guaranteed sightings, stock images presented as local evidence and earthy palettes used to disguise emissions. Build trust with probability, provenance, accessibility and a clear correction path.',
        sources=[('Papanek Foundation, Archive and Library', 'https://papanek.org/archivelibrary/'), ('Monteiro, Ruined by Design', 'https://www.ruinedby.design/'), ('Eye Magazine, First Things First 1964', 'https://www.eyemagazine.com/blog/post/design-for-life'), ('Eye Magazine, First Things First 2000', 'https://eyemagazine.com/feature/article/first-things-first-manifesto-2000'), ('FTC, Bringing Dark Patterns to Light', 'https://www.ftc.gov/reports/bringing-dark-patterns-light')]
    ),
]

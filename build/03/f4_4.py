from svg import box, t, arrow, line, svg

CARDS = ['The Players', 'The Set-Up', 'The Hook', 'The Tale', 'The Wire', 'The Shut-Out', 'The Sting']
FIG = svg(1180, 430, 'Three tracks through The Sting: what Lonnegan believes, what the audience believes, and what is really happening',
          t(590, 32, "THE STING'S SEVEN TITLE CARDS, AND THREE LAYERS OF BELIEF", 's-t') +
          ''.join(box(20 + i * 163, 52, 150, 52, 's-box-j', 8) + t(95 + i * 163, 84, c, 's-t-sm') for i, c in enumerate(CARDS)) +
          t(20, 146, 'LONNEGAN (the mark)', 's-t-b', 'start') + box(20, 156, 1140, 50, 's-card', 8) +
          t(590, 188, 'believes he is betting on fixed races through a crooked insider. Fooled from start to finish.', 's-t-sm') +
          t(20, 246, 'THE AUDIENCE (the second mark)', 's-t-b', 'start') + box(20, 256, 1140, 50, 's-box-a', 8) +
          t(590, 288, 'believes it is backstage with the crew, so it relaxes. Fooled about one thing: the ending.', 's-t-sm') +
          t(20, 346, 'THE CREW (the truth)', 's-t-b', 'start') + box(20, 356, 1140, 50, 's-card', 8) +
          t(590, 388, 'has a plan inside the plan. The film shows its pieces; it never shows how they fit.', 's-t-sm'))

STOP = dict(
    id='4.4', day=27, title='The Sting: making the audience the mark',
    q='Why does a film that explains its con step by step, with chapter cards, still fool almost everyone who watches it for the first time?',
    why="The Sting is the template for every con film since. It takes Maurer's real structure from stop 4.1, puts it on screen as chapter titles, invites you backstage with the crew, and then uses your feeling of being an insider against you. For a future director this is the most important lesson in the genre: the best twist does not hide facts from the audience. It hides their meaning.",
    case=dict(k='The film', name='The Sting (1973)', role='Directed by George Roy Hill, written by David S. Ward; Paul Newman, Robert Redford, Robert Shaw',
              facts=[('Setting', 'September 1936, Joliet and Chicago, during the Great Depression'),
                     ('Oscars', '7 wins from 10 nominations, including Best Picture, Director and Original Screenplay'),
                     ('Structure', 'Seven chapter cards in Saturday Evening Post style, drawn by Jaroslav Gebr'),
                     ('Lawsuit', 'Maurer sued for $10 million in 1974; settled out of court in 1976')],
              stamp=('part', 'Partly: original, but in debt to Maurer')),
    cold=dict(q='The Sting won the Oscar for a screenplay category with a very specific name. Given the lawsuit that followed, guess why the name is ironic.',
              a="The 1974 category was Writing, Story and Screenplay based on factual material or material not previously published or produced. David Maurer, whose 1940 book recorded the wire con, its slang and its crew roles, argued that the film borrowed too closely from it and sued Ward and Universal. The case settled in 1976. Settling is not a ruling of plagiarism, and Ward disputed any wrongdoing. But the honest lesson for a writer is simple: when your structure comes from a real source, say so."),
    video=dict(id='_nAIb_J9T5M', title='The Sting Official Trailer #1 (1973)', who='Rotten Tomatoes Classic Trailers',
               watch=['How the trailer sells charm and friendship more than plot',
                      'The ragtime music: Scott Joplin\'s The Entertainer, from 1902, set in 1936',
                      'Which character the trailer makes you trust, and why']),
    story=["The plot is pure Maurer. In 1936, a young grifter, Johnny Hooker, unknowingly cons a courier working for the gangster Doyle Lonnegan. Lonnegan has Hooker's partner killed. Hooker goes to Chicago to find Henry Gondorff, a legendary big-con man, and together they build a big store: a fake off-track betting parlour, staffed by dozens of grifters playing clerks and gamblers, to take Lonnegan in a wire con, where the mark believes he is getting race results before the bookmakers do. Roper, inside man, tale, convincer, breakdown, send, touch, blow-off: they are all there.",
           "Then the film does something clever with its form. It divides itself into seven chapters with painted title cards: The Players, The Set-Up, The Hook, The Tale, The Wire, The Shut-Out, The Sting. That looks like a gift to the audience, a map. It is actually a roper. By explaining the con's vocabulary and taking us backstage to watch the crew rehearse, the film makes us feel like members of the crew. Insiders do not check. We stop asking what the crew is not telling us.",
           "And there is something it is not telling us. The film runs three layers of belief at once, shown in the diagram. Lonnegan believes he is cheating a bookmaker. The audience believes it is watching the crew cheat Lonnegan, and also watching an FBI agent close in on Gondorff and an assassin close in on Hooker. The crew has a plan inside the plan that covers those threats too. When the final scene reclassifies everything we have seen, the pleasure is not surprise alone. It is the double feeling of being conned and admiring the con.",
           "Is that fair? The rule that separates a great twist from a cheat is whether the film showed you the facts. The Sting does: the characters, the danger, the relationship between Hooker and Gondorff and the pieces of the final scheme are all on screen. What it withholds is the connection between them. A cheat twist introduces a new fact after the reveal, or has a character lie to the audience in a way that no in-world person could see. You will build a checklist for this in stop 4.6.",
           "The craft around the plot sells the world. Hill, art director Henry Bumstead and cinematographer Robert Surtees used a muted palette of browns and maroons and old-fashioned lighting. Edith Head's costumes won an Oscar. Marvin Hamlisch's adaptation of Scott Joplin's ragtime, music from around 1902 in a film set in 1936, is historically wrong and emotionally perfect: it says playful, old-fashioned and harmless, which is exactly how the con wants you to feel."],
    fig=(FIG, "The Sting's seven chapters and three layers of belief. The audience is fooled about one thing only, and that is the point."),
    specs=[('Wire con', 'A big con where the mark is told he is getting race results before the bookmakers, and bets on that edge.'),
           ('Big store', 'The fake setting of a big con, here a betting parlour staffed by grifters.'),
           ('Reclassification', 'The moment a reveal makes the audience re-read earlier scenes with a new meaning.'),
           ('Second mark', 'The audience, when a film uses the con\'s own tools on its viewers.')],
    tags=[('part', '"The Sting was wholly independent of Maurer."', 'Credited as original, but Maurer sued and the case settled.', ('Maurer obituary, NYT 1981', 'https://www.nytimes.com/1981/06/14/obituaries/david-w-maurer-is-dead-at-75-an-expert-on-underworld-slang.html')),
          ('myth', '"Maurer won a plagiarism judgment."', 'The case settled out of court in 1976. A settlement is not a finding.', ('CrimeReads on Maurer', 'https://crimereads.com/david-maurer-the-dean-of-criminal-language/')),
          ('hold', '"The Sting won seven Oscars, including Best Picture."', 'Seven of ten nominations at the 46th Academy Awards.', ('Oscars.org, 46th Academy Awards', 'https://www.oscars.org/oscars/ceremonies/1974/memorable-moments')),
          ('myth', '"A fair twist hides the facts."', 'A fair twist shows the facts and hides how they connect.', ('AFI catalogue, The Sting', 'https://www.afi.com/film/the-sting/'))],
    distil=[('Maurer, The Big Con (1940)', 'https://search.worldcat.org/title/930462967', 'The wire con the film dramatises'),
            ('CrimeReads: David Maurer, the dean of criminal language', 'https://crimereads.com/david-maurer-the-dean-of-criminal-language/', 'The lawsuit and its context'),
            ('Oscars.org: 46th Academy Awards', 'https://www.oscars.org/oscars/ceremonies/1974/memorable-moments', 'What the film won')],
    writer=dict(notes=["Steal the chapter-card trick for a short film, but understand why it works. Each card promises the audience a map. The map is true. It is just not complete. Give your audience a structure they can follow and they will stop looking for the structure you are hiding.",
                       "The emotional spine is friendship, not money. Hooker wants revenge; Gondorff wants to prove he still has it. The final reveal lands because it resolves their relationship as well as the plot. If your twist only changes the plot, it is a trick. If it also changes a relationship, it is a story."],
                drill="Write a two-page fictional scene in which one character explains a scheme's logic to another, while the action description gives the reader one honest detail that will mean something else at the end. Then list three earlier moments that would support the reversal without announcing it."),
    biz="The Sting's lawsuit is a business lesson. If an MTRX\u2122 pitch deck, case study or site structure is built on someone else's framework, credit it. Keep a source file for every claim and image you use. A settlement is more expensive than a footnote.",
    tryit="Watch the trailer above. Then write down the one character you trusted most and the exact moment that made you trust them. That moment is your own roper. Now name one place in your life, a feed, a brand or a person, that earns your trust the same way.",
    room='A twist is fair when the audience was given the truth but not the confidence to read it.',
    deeper=[('Filmsite: The Sting, scene by scene', 'https://www.filmsite.org/sting.html', 'A detailed walk through the chapters'),
            ('David Maurer obituary, New York Times 1981', 'https://www.nytimes.com/1981/06/14/obituaries/david-w-maurer-is-dead-at-75-an-expert-on-underworld-slang.html', 'The man behind the slang')],
    nextq='The Sting\'s grifters are charming outlaws. What happens when the con artist has a law degree, a brother he worships, and a talent that keeps winning for the wrong reasons? Stop 4.5.',
    checks=[dict(q='How did David Maurer\'s lawsuit over The Sting end?',
                 o=['It was settled out of court in 1976',
                    'A jury found the film guilty of plagiarism',
                    'The court dismissed it and ordered Maurer to pay costs'], a=0,
                 w='Maurer sued in 1974 and the case settled in 1976. A settlement is not a finding of plagiarism.'),
            dict(q='What do The Sting\'s chapter cards do to the audience?',
                 o=['Make viewers feel like insiders, so they stop looking for a hidden plan',
                    'Reveal the final twist early so viewers can enjoy the craft',
                    'Replace the need for any visual clues in the story'], a=0,
                 w='A map that is true but incomplete works like a roper: it earns trust and lowers your guard.'),
            dict(q='What separates a fair twist from a cheat?',
                 o=['The facts were shown earlier; only their meaning was hidden',
                    'The audience is never shown any of the key facts',
                    'A new piece of evidence is introduced after the reveal'], a=0,
                 w='Seed the fact, let the audience misread it, then reclassify. A late new fact is a cheat.')],
)

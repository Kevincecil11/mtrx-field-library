from svg import box, t, arrow, line, svg

BE = [('THE JOB', 'an impossible target'), ('THE CREW', 'one skill per person'), ('THE PLAN', 'told to us, or half told'),
      ('THE HICCUP', 'something goes wrong'), ('THE REVEAL', 'the plan behind the plan')]
FIG = svg(1180, 400, 'The five beats of the crew film, and the emotional question underneath each one',
          t(590, 32, 'THE CREW FILM IN FIVE BEATS', 's-t') +
          ''.join(box(20 + i * 232, 60, 212, 120, 's-box-a' if i == 4 else 's-card', 12) + t(126 + i * 232, 106, n, 's-t-b') +
                  t(126 + i * 232, 142, d, 's-t-sm') for i, (n, d) in enumerate(BE)) +
          ''.join(arrow(232 + i * 232, 120, 250 + i * 232, 120) for i in range(4)) +
          t(590, 238, 'UNDERNEATH: can this group trust each other?', 's-t-b') +
          t(590, 280, 'Every specialist is a promise of competence. Every hiccup tests it. The reveal pays it off.', 's-t-sm') +
          line(80, 312, 1100, 312, True) +
          t(590, 356, 'The heist is the plot. The crew is the story. That is why the genre survives remakes.', 's-t-sm'))

STOP = dict(
    id='5.4', day=33, title="Ocean's and the crew film",
    q='Ocean\'s Eleven is a film about robbing three casinos. Why is the most enjoyable part watching George Clooney hire people?',
    why="The crew film is one of the most reliable structures in cinema, and Ocean's Eleven (2001) is its cleanest modern version. Understanding why it works teaches you how to introduce an ensemble fast, how to make competence itself entertaining, and how to hide a twist inside a plan the audience thinks it already knows. These are skills you will use in almost any genre.",
    case=dict(k='The film', name="Ocean's Eleven (2001)", role='Directed by Steven Soderbergh from Ted Griffin\'s screenplay; a remake of the 1960 Rat Pack film',
              facts=[('Original', "Ocean's 11 (1960), Lewis Milestone, with Frank Sinatra and Dean Martin"),
                     ('Remake', 'George Clooney, Brad Pitt, Matt Damon, Julia Roberts, Andy Garcia'),
                     ('Target', 'The vault beneath the Bellagio, which serves three casinos owned by Terry Benedict'),
                     ('Legacy', "Two sequels (2004, 2007) and Ocean's 8 (2018)")],
              stamp=('field', 'Field test: watch the recruitment')),
    cold=dict(q='Danny Ocean\'s crew are thieves, but the film asks the audience to care about one relationship more than the money. Guess which one.',
              a="Danny and his ex-wife Tess, who is now with the casino owner, Terry Benedict. The heist is also a test of whether Tess will see Benedict for who he is. It gives the money a heart and the plan a second target. This is the pattern from stop 4.4: the best twist resolves a relationship as well as a plot. A heist without a personal stake is a puzzle; with one, it is a story."),
    video=dict(id='C6vD5cRhw14', title="Ocean's Eleven (2001) Trailer", who='Warner Bros.',
               watch=['How fast each crew member is introduced, and by what one trait',
                      'How the trailer sells the crew\'s confidence more than the vault',
                      'What the music tells you about the risk (very little danger, lots of style)']),
    story=["The crew film runs on five beats, shown in the diagram. The job: an impossible target. The crew: one specialist per skill. The plan: explained to us in full, or in part. The hiccup: something goes wrong. The reveal: the plan had another layer we were not shown. Ocean's Eleven, from Ted Griffin's script, hits every beat with style. Danny Ocean, just out of prison, recruits a team to rob the vault that serves the Bellagio, the Mirage and the MGM Grand on the night of a boxing match.",
           "The recruitment section is the genre's secret pleasure. In a few minutes each, we meet a pickpocket, a demolitions expert, an acrobat, an electronics man, a pair of bickering drivers, a retired con man and a banker. Each is introduced doing the thing he is best at, often in a tiny self-contained scene. It is efficient character writing: one trait, one skill, one joke. By the time the plan begins, the audience has met eleven people and believes in all of them. Competence on screen is its own kind of suspense, because we want to watch it work.",
           "The plan is where the film plays the Sting trick from stop 4.4. It walks us through the scheme so we feel like members of the crew. Then the hiccups arrive, and finally the reveal shows a layer we did not see, including a fake SWAT team and a replica vault filmed on a set. The facts were there; we were looking at the wrong ones. Notice, too, what the genre leaves out: the victims are a smug casino boss and an insurance company. Nobody we care about loses anything.",
           "Why does it survive remakes? Because the heist is the plot but the crew is the story. Each sequel changes the job and keeps the pleasure of watching a group of experts trust each other. Ocean's 8 (2018) swapped in an all-female crew and the Met Gala, and the structure held. It is the same reason teams work in sports films, war films and startup films: a group of misfits becoming a unit is one of the oldest satisfactions in storytelling.",
           "Real heists, which you meet next, look very different. They rarely have eleven specialists, they almost never involve charm, and they are usually caught. That contrast is the point: the crew film is a fantasy of competence and trust, and it works because, in real life, crews are where heists fall apart."],
    fig=(FIG, 'The five beats of the crew film. The heist is the plot; whether the crew can trust each other is the story.'),
    specs=[('Crew film', 'A story built around assembling specialists for one job; heist, war and sports films all use it.'),
           ('Recruitment montage', 'Fast scenes that introduce each specialist doing the one thing they are best at.'),
           ('Plan behind the plan', 'A hidden layer of the scheme revealed at the end, which reclassifies the hiccups.')],
    tags=[('hold', '"Ocean\'s Eleven (2001) is a remake."', 'It remakes the 1960 Rat Pack film directed by Lewis Milestone.', ('AFI catalogue, Ocean\'s 11 (1960)', 'https://catalog.afi.com/Catalog/moviedetails/53237')),
          ('myth', '"Heist films show how real heists work."', 'They show a fantasy of competence; real cases (stop 5.5) look nothing like it.', ('BBC on the Antwerp heist', 'https://news.bbc.co.uk/2/hi/europe/2797897.stm')),
          ('part', '"The crew film is about the money."', 'The money is the plot; trust inside the crew is the story. Swap the crew and it still works.', ('Variety, Ocean\'s 8 review', 'https://variety.com/2018/film/reviews/oceans-8-review-sandra-bullock-1202830271/'))],
    distil=[('AFI catalogue: Ocean\'s 11 (1960)', 'https://catalog.afi.com/Catalog/moviedetails/53237', 'The Rat Pack original'),
            ('Lupin trailer (for comparison)', 'https://www.youtube.com/watch?v=ga0iTWXCGa0', 'A lone thief versus a crew')],
    writer=dict(notes=["Introduce each crew member doing the one thing they are best at, in a scene that would work as a short film. If you need dialogue to tell us someone is good at their job, the scene is not working yet.",
                       "Give the plan a personal second target, the way Tess is Danny's. A heist that only wins money ends when the vault opens. A heist that wins something back for a person ends when that person decides."],
                drill="Write a one-page fictional recruitment scene for a five-person crew (any job, legal or not: a wedding, a film shoot, a startup launch). Introduce each person in three lines or fewer, through action."),
    biz="A small agency is a crew film. When MTRX™ pitches a bigger project, introduce the team the way Ocean's does: one person, one proven skill, one example of work. Clients buy confidence in the crew before they buy the plan.",
    tryit="Watch the trailer above. Write down each crew member you can identify and the one trait the trailer gives them. Then do the same for the team of a real project you are on. Who has no clear trait? That is your weakest introduction.",
    room='The heist is the plot. Whether the crew can trust each other is the story.',
    deeper=[('Ocean\'s 8 and the remake question (Variety review)', 'https://variety.com/2018/film/reviews/oceans-8-review-sandra-bullock-1202830271/', 'Same structure, new crew')],
    nextq='Films make heists look elegant and nearly bloodless. What did the real ones in Antwerp, London and the Louvre actually look like, and how were they caught? Stop 5.5.',
    checks=[dict(q='What is the genre\'s "plan behind the plan"?',
                 o=['A hidden layer of the scheme revealed at the end',
                    'The backup plan the crew writes down before the job',
                    'The police plan to catch the crew in the sequel'], a=0,
                 w='The film explains a plan, then reveals another layer. The Sting\'s trick, made into a genre.'),
            dict(q='Why does the recruitment section work so well?',
                 o=['Each specialist is shown doing the one thing they do best',
                    'It explains every step of the heist in technical detail',
                    'It gives every crew member a long backstory monologue'], a=0,
                 w='One trait, one skill, one joke. Competence on screen is its own suspense.'),
            dict(q='What gives the money in Ocean\'s Eleven a personal stake?',
                 o=['Danny\'s ex-wife Tess is with the casino owner',
                    'Danny owes the money to the boxing promoter',
                    'The crew plans to donate the money to charity'], a=0,
                 w='A heist with a relationship at stake ends when a person decides, not when a vault opens.')],
)

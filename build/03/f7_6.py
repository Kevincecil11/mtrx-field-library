from svg import box, t, arrow, line, svg

ROW1 = [('1 LOGLINE', 'one sentence:', 'who, which con, what stakes'), ('2 CHARACTERS', 'mark, roper, insider,', 'and the one who checks'),
        ('3 SET-UP', 'the world and the want', 'from File 1 or File 6'), ('4 THE CON', 'Maurer’s beats,', 'put-up to touch')]
ROW2 = [('5 THE TURN', 'the convincer cracks,', 'or someone checks'), ('6 THE REVEAL', 'every clue shown', 'before the twist'),
        ('7 THE COST', 'what the con takes', 'from everyone'), ('8 FAIR TEST', 'when did a reader', 'guess it? was it fair?')]
def row(items, y, last_orange=False):
    out = ''
    for i, (a, b, c) in enumerate(items):
        x = 20 + i * 290
        cls = 's-box-a' if (last_orange and i == 3) else 's-card'
        out += box(x, y, 270, 120, cls, 12) + t(x + 135, y + 40, a, 's-t-b') + t(x + 135, y + 72, b, 's-t-sm') + t(x + 135, y + 98, c, 's-t-sm')
    out += ''.join(arrow(292 + i * 290, y + 60, 308 + i * 290, y + 60) for i in range(3))
    return out
FIG = svg(1180, 400, 'A con film treatment skeleton in eight blocks, from logline to the fairness test',
          t(590, 32, 'TREATMENT SKELETON: EIGHT BLOCKS, THREE TO FIVE PAGES', 's-t') +
          row(ROW1, 56) + row(ROW2, 206, True) +
          t(590, 372, 'Third person, present tense. If the twist fails on paper, it will fail on screen.', 's-t-sm'))

STOP = dict(
    id='7.6', day=47, title='Capstone: write a con film treatment',
    q='You have studied cons, cults, frauds and the people who catch them. Can you turn it all into a story that fools the audience fairly?',
    why='This is the capstone: a film treatment for an original con story, built from everything in Files 1 to 7. A treatment is the document writers use to develop and sell a film before the script exists. It forces you to know your story, your twist and your characters in a few pages. Done well, it is also a portfolio piece: proof that you can turn research into drama.',
    case=dict(k='The form', name='The film treatment', role='A short prose version of a film, written before the script',
              facts=[('Voice', 'Third person, present tense'),
                     ('Length', 'StudioBinder: under ten pages; Script Magazine: 3 to 20'),
                     ('Contents', 'Logline, characters, story beats, tone and the twist'),
                     ('Models', 'Paper Moon, The Spanish Prisoner, Matchstick Men, American Hustle')],
              stamp=('field', 'Field test: write your own')),
    cold=dict(q='Why do writers bother with a treatment instead of going straight to the script?',
              a='Because a treatment tests the story before you spend months on scenes. In a few pages of third-person, present-tense prose it shows whether the plot works, whether the characters change and whether the twist plays fair. Producers read treatments to decide what to develop. For a con story it matters even more: if the reveal does not work in three pages, it will not work in a hundred and ten.'),
    video=dict(id='231en2UptyE', title='How to Write a TV Show Treatment (with Examples)', who='StudioBinder',
               watch=['What sections a treatment needs, and in what order',
                      'How the examples set the tone in only a few lines',
                      'What you would change for a film rather than a series']),
    story=['A treatment is a short prose version of your film: third person, present tense, no camera directions, written to be read in one sitting. StudioBinder suggests keeping a general film treatment under ten pages, and Script Magazine puts the usual range at three to twenty. For this capstone, aim for three to five. Open with a logline, one sentence that names the protagonist, the con and the stakes. Then introduce the main characters, tell the story in beats, and end with the reveal and what it costs.',
           'Build it from the course, as the skeleton in the diagram shows. From stop 4.1, Maurer’s big con gives you the beats: the put-up, the play, the rope, the tale, the convincer, the breakdown, the send, the touch, the blow-off and the fix. From File 5, the masks: who is pretending to be whom. From File 6, the money engine: where the money really comes from. From Files 1 to 3 and stop 7.3, how a group or a relationship traps a person. From stop 7.4, the one who checks. Choose a few, not all of them.',
           'The reveal must play fair, as stop 4.6 showed. Every fact the twist depends on should appear before it, hidden in plain sight, so a second viewing feels inevitable. Study four models. Paper Moon (1973, directed by Peter Bogdanovich, written by Alvin Sargent) plays its cons as a father-and-daughter story. David Mamet’s The Spanish Prisoner (1997) makes the audience the mark. Matchstick Men (2003, directed by Ridley Scott, written by Nicholas and Ted Griffin) hides its biggest con inside a family drama. American Hustle (2013), loosely based on the FBI’s Abscam sting, puts con artists to work for the FBI.',
           'One rule from this course carries into fiction: dark mechanisms, handled responsibly. Your treatment can show a con in detail as drama, but it should not work as a manual for a real scam. If it touches cults, abuse or trafficking, keep the victims human and the harm real. The best con films let the audience enjoy the game and feel the cost at the same time.',
           'Treat the result as a real document. Put your name, the title, the logline and the date on the first page. Read it aloud. Then give it to one person who has not seen this course and ask them two questions: when did you guess the twist, and did it feel fair? Their answers tell you what to fix. A finished treatment is a writing sample you can show, and the first step toward a screenplay.'],
    fig=(FIG, 'The treatment skeleton: eight blocks, three to five pages, ending with a fairness test.'),
    specs=[('Treatment', 'A short prose version of a film or series, in present tense, used to develop and sell the story.'),
           ('Logline', 'One sentence that names the protagonist, the goal or con, and what is at stake.'),
           ('Beat', 'A single story event that changes the situation. A treatment tells the story beat by beat.')],
    tags=[('hold', '“Treatments are written in the present tense.”', 'Standard guidance: a succinct, third-person, present-tense summary.', ('Film Scriptwriting (O’Reilly), chapter 3', 'https://www.oreilly.com/library/view/film-scriptwriting-2nd/9781136056857/xhtml/10_Chapter03.xhtml')),
          ('part', '“A treatment must be a set length.”', 'There is no fixed rule: StudioBinder says under ten pages; Script Magazine gives 3 to 20.', ('StudioBinder: how to write a film treatment', 'https://www.studiobinder.com/blog/how-to-write-a-film-treatment/')),
          ('field', '“My twist is fair.”', 'Test it on a reader who has not seen this course: when did they guess, and did it feel earned?', ('Script Magazine: writing a treatment', 'https://scriptmag.com/features/writers-edge-writing-a-treatment'))],
    distil=[('StudioBinder: how to write a film treatment', 'https://www.studiobinder.com/blog/how-to-write-a-film-treatment/', 'Structure and length'),
            ('Script Magazine: writing a treatment', 'https://scriptmag.com/features/writers-edge-writing-a-treatment', 'What producers expect'),
            ('AFI Catalog: Paper Moon (1973)', 'https://catalog.afi.com/Film/54836-PAPER-MOON', 'A model con film')],
    writer=dict(notes=['Write the logline first and last. If you cannot state the con and the stakes in one sentence, the treatment will wander.',
                       'Plant three clues for the twist in the first third and note where each one is. In a draft you can even underline them for your reader, then remove the underlines for the final version.'],
                drill='Before anything else, write the logline and a one-paragraph reveal for your con film. If the reveal does not surprise and satisfy in one paragraph, change the con.'),
    drill=dict(name='Capstone: your con film treatment', mins='3 to 5 hours across the week',
               steps=['Write a logline: protagonist, con, stakes. One sentence.',
                      'Cast four roles: the mark, the roper, the insider and the one who checks. Give each a want and a need.',
                      'Choose the money engine (File 6) or the group (Files 1 to 3) at the heart of the con.',
                      'Outline the beats with Maurer’s steps from stop 4.1, then write them as present-tense prose, three to five pages.',
                      'Plant every clue the twist needs before it, and list where each one appears.',
                      'Give it to one reader. Ask when they guessed the twist and whether it felt fair. Revise once.'],
               mistake='Writing a heist of gadgets instead of a con of people. The best treatments are about why the mark wants to believe, and what the reveal costs each character.'),
    biz='A treatment is also a sales document, so this is practice for MTRX™ too. A proposal and a treatment share a shape: a one-line promise, the people involved, the problem, the plan in steps, the turning point and the result. If you can make a producer see a film in five pages, you can make a clinic owner see their new website in one.',
    tryit='Today, write only the title and the logline. Tomorrow, the four characters. By the end of the week, the full treatment. Send it to one person you trust.',
    room='A good con film fools the audience fairly: every clue on screen, every cost felt.',
    deeper=[('AFI Catalog: The Spanish Prisoner (1997)', 'https://catalog.afi.com/Film/61585-THE-SPANISH-PRISONER', 'The audience as the mark'),
            ('AFI Catalog: Matchstick Men (2003)', 'https://catalog.afi.com/Film/62830-MATCHSTICK-MEN', 'A con inside a family story')],
    nextq='File 8 is a bonus deep dive. In 1963 the CIA wrote a manual on breaking a prisoner’s resistance. What did KUBARK say, and what did it get wrong? Stop 8.1.',
    checks=[dict(q='In what person and tense is a film treatment usually written?',
                 o=['Third person, present tense', 'First person, past tense', 'Second person, future tense'], a=0,
                 w='Standard guidance: a succinct, third-person, present-tense summary of the story.'),
            dict(q='What should a logline contain?',
                 o=['The protagonist, the con or goal, and the stakes',
                    'The full cast list with every actor’s age',
                    'Every twist, in the order it happens'], a=0,
                 w='One sentence. If you cannot write it, you do not know your story yet.'),
            dict(q='What makes a twist play fair?',
                 o=['Every clue it needs is shown before the reveal',
                    'Nobody in the audience could possibly guess it',
                    'A new character explains it all at the end'], a=0,
                 w='A fair twist feels inevitable on a second viewing. That is the test from stop 4.6.')],
)

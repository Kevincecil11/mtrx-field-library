"""No. 06 Part II, File 1: The Spotlight (stops 2.1 to 2.7). Content as data.
Rendered by build.py. Quotes were checked against the linked sources on
14 Oct 2026. No em or en dashes anywhere (the lint fails on them)."""

FILE = dict(
    n=1, sec='4', part='4', title='The Spotlight',
    kicker='Part II · The Spotlight Files · File 1 of 5 · 7 stops',
    promise=('Charm is attention people can feel. Seven moves, each taught through one person who owned it, '
             'checked against the evidence, and tried on a real person the same day.'),
)


def A(label, url):
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (url, label)


U = dict(
    jfk_paris='https://www.jfklibrary.org/archives/other-resources/john-f-kennedy-press-conferences/news-conference-12',
    jfk_pt109='https://www.jfklibrary.org/learn/about-jfk/jfk-in-history/john-f-kennedy-and-pt-109',
    jfk_quotes='https://www.jfklibrary.org/learn/about-jfk/life-of-john-f-kennedy/john-f-kennedy-quotations',
    jfk_nobel_files='https://www.jfklibrary.org/asset-viewer/archives/jfkpof-037-042',
    tamir='https://doi.org/10.1073/pnas.1202129109',
    binetti='https://doi.org/10.1098/rsos.160086',
    langlog='https://languagelog.ldc.upenn.edu/nll/?p=2630',
    rayner='https://doi.org/10.1177/1529100615623267',
    reeves='https://alacartescholar.substack.com/p/the-titans-of-reading',
    gladstone='https://www.gladstoneslibrary.org/blog/the-great-rivalry-as-told-by-punch/',
    carnegie='https://en.wikipedia.org/wiki/How_to_Win_Friends_and_Influence_People',
    howard='https://doi.org/10.1086/209445',
    mcweeny='https://doi.org/10.1111/j.2044-8295.1987.tb02235.x',
    cohen='https://doi.org/10.1111/j.2044-8295.1990.tb02362.x',
    huang='https://doi.org/10.1037/pspi0000097',
    boomer='https://doi.org/10.1037/xge0001693',
    kardas='https://doi.org/10.1037/pspa0000281',
    heritage='https://doi.org/10.1007/s11606-007-0279-0',
    snopes='https://www.snopes.com/fact-check/be-curious-not-judgmental-walt-whitman/',
    king='https://www.newsweek.com/best-quotes-larry-king-i-never-learned-anything-while-i-was-talking-1563928',
    gable='https://doi.org/10.1037/0022-3514.87.2.228',
    derber='https://books.google.com/books/about/The_Pursuit_of_Attention.html?id=r_SRv3Yrmx4C',
    zhao='https://doi.org/10.1037/pspa0000277',
    kumar='https://doi.org/10.1177/0956797618772506',
    gordon='https://psycnet.apa.org/record/1996-01782-004',
    maraniss='https://www.spokesman.com/stories/1995/feb/12/clinton-ambition-biographer-recounts-the/',
    debate='https://www.debates.org/voter-education/debate-transcripts/october-15-1992-second-half-debate-transcript/',
    mackay='https://harveymackay.com/knowing-something-about-your-customer-is-just-as-important-as-knowing-your-product/',
    murre='https://doi.org/10.1371/journal.pone.0120644',
    antonakis='https://doi.org/10.5465/amle.2010.0012',
)

# Colophon cards: (label, url key, stop)
SOURCES = [
    ('JFK Library, News Conference 12, Paris 1961', 'jfk_paris', '2.1'), ('JFK Library, PT-109', 'jfk_pt109', '2.1'),
    ('Tamir and Mitchell 2012', 'tamir', '2.1'), ('Binetti et al. 2016', 'binetti', '2.1'),
    ('Language Log 2010, citing TIME 1961', 'langlog', '2.1'), ('Rayner et al. 2016', 'rayner', '2.1'),
    ('Fischer 2025, on Reeves\'s account of the 1,200 figure', 'reeves', '2.1'), ('Gladstone\'s Library 2017', 'gladstone', '2.1'),
    ('Carnegie 1936', 'carnegie', '2.2'), ('Howard, Gengler and Jain 1995', 'howard', '2.2'),
    ('McWeeny, Young, Hay and Ellis 1987', 'mcweeny', '2.2'), ('Cohen 1990', 'cohen', '2.2'),
    ('Huang, Yeomans, Brooks, Minson and Gino 2017', 'huang', '2.3'), ('Brooks and Yeomans 2025', 'boomer', '2.3'),
    ('Kardas, Kumar and Epley 2022', 'kardas', '2.3'), ('Heritage et al. 2007', 'heritage', '2.3'),
    ('Snopes 2021, Whitman misattribution', 'snopes', '2.3'), ('Larry King quotes, Newsweek 2021', 'king', '2.3'),
    ('Gable, Reis, Impett and Asher 2004', 'gable', '2.4'), ('Derber, The Pursuit of Attention', 'derber', '2.4'),
    ('Zhao and Epley 2021', 'zhao', '2.5'), ('Kumar and Epley 2018', 'kumar', '2.5'), ('Gordon 1996', 'gordon', '2.5'),
    ('JFK Library, Nobel dinner files', 'jfk_nobel_files', '2.5'), ('Maraniss 1995, via NYT review', 'maraniss', '2.6'),
    ('Debate transcript, 15 Oct 1992', 'debate', '2.6'), ('Mackay 66', 'mackay', '2.6'), ('Murre and Dros 2015', 'murre', '2.6'),
    ('Antonakis, Fenley and Liechti 2011', 'antonakis', '2.7'),
]

INTRO = dict(
    lede=('Part I taught you to read people. The Spotlight Files teach you to be the person they remember. '
          'Each stop is a case file: one subject, one named move, the scene that shows it, the science that '
          'checks it, and a truth tag on every famous claim (holds up, partly, or myth).'),
    anatomy=['Cold open: predict first', 'The subject', 'The story', 'The move', 'The scenes',
             'Why it works', 'Truth tags', 'Do it today'],
    files=[
        dict(n=1, title='The Spotlight', stops='2.1 to 2.7', note='Attention, names, questions, compliments, callbacks. Here now.', href='#m2-1', now=True, c='var(--jane)'),
        dict(n=2, title='The Read', stops='2.8 to 2.13', note='What people hunger for, how directors read actors, reading a group. Next drop.', href='#s4', c='var(--graphite)'),
        dict(n=3, title='George Newman', stops='2.14 to 2.22', note='Voice, walk, stance, calm, the long take. Plates and scenes ready to watch.', href='#s2', c='var(--gun)'),
        dict(n=4, title='Pitch and network', stops='2.23 to 2.30', note='Known for one thing, the one-minute pitch, favours, dormant ties.', href='#s3', c='var(--moss)'),
        dict(n=5, title='The Line', stops='2.31 to 2.34', note='Influence vs manipulation, Belfort, Barry Seal, the mask.', href='#s5', c='var(--red)'),
    ],
    coverage=('<p><b>What File 1 covers.</b> Attention as a reward (Tamir and Mitchell), gaze in short bouts (Binetti), '
              'why names slip and how to make them stick (McWeeny, Cohen), name remembrance as a compliment (Howard), '
              'follow-up questions and responsiveness (Huang), boomerasking (Brooks and Yeomans), deeper talk with '
              'strangers (Kardas), the one-word "something else" close (Heritage), shift and support responses (Derber), '
              'responding to good news (Gable), compliments and gratitude (Zhao and Epley, Kumar and Epley), the '
              'forgetting curve (Murre and Dros) and people files (Mackay, Clinton).</p>'
              '<p><b>Where it came from.</b> The Part I audit flagged self-presentation and applied influence for Part II. '
              'This file adds a fresh pass on conversation science (Brooks, Epley, Gable, Reis) and the workspace docs you '
              'liked (the JFK Spotlight file, the Bureau Method, the Saul Goodman file), with their myths corrected.</p>'
              '<p><b>Deliberately elsewhere.</b> Mimicry, humour and voice (File 3), gifts, favours and the 48 Laws (File 4), '
              'flattery as a weapon (File 5). <b>What this does not prove:</b> that every move lands the same way in every '
              'culture you sell into. Your scorecard in Stop 2.7 will tell you.</p>'),
)

STOPS = []

# ---------------------------------------------------------------- 2.1
STOPS.append(dict(
    id='2.1', day=13, title='The Spotlight',
    why=('Paris, 2 June 1961. The most powerful man on earth stands up in front of the press and introduces himself as '
         'his wife\'s plus-one. The room loves him for it. The first move of charm is the strangest one: you win the light '
         'by handing it away.'),
    dossier=dict(name='John F. Kennedy', role='35th US President · press luncheon, Palais de Chaillot, Paris, 2 June 1961',
                 facts=[('Known for', 'Wit that made other people the hero of the sentence'),
                        ('The move', 'Hand them the light'),
                        ('Steal it for', 'Group intros, client meetings, any room where you are "the website guy"')],
                 stamp=('hold', 'Holds up')),
    cold=dict(q=('A Harvard lab let people choose: answer a question about yourself, or answer one about someone else for '
                 'slightly more money. On average, how much of their possible earnings did people give up just to talk '
                 'about themselves: 0%, 5%, 17% or 40%? Pick one and rate your confidence from 1 to 5.'),
              a=('<b>17%.</b> People paid to talk about themselves, and doing it lit up the brain\'s reward system '
                 '(Tamir and Mitchell 2012). The same paper notes that 30 to 40% of what people say is about their own '
                 'experiences. Attention on someone is a reward their brain will pay for. Charm is giving it away free.')),
    story=[
        ('On his first big trip abroad as president, Kennedy went to Paris to meet Charles de Gaulle. The French had already '
         'fallen for someone else: his wife, Jacqueline, who spoke French and was the star of the visit. At the press '
         'luncheon on 2 June he opened with two sentences: <i>"I do not think it altogether inappropriate to introduce myself '
         'to this audience. I am the man who accompanied Jacqueline Kennedy to Paris, and I have enjoyed it."</i>'),
        ('Look at what those two sentences do. He names the star, and it isn\'t him. He casts himself as the side character, '
         'which only a secure man can afford. He tells the room its taste is right. Then, before a word of policy, he thanks '
         'his hosts, President and Mrs. de Gaulle. The light keeps moving outward, and the room warms to the man holding it.'),
        ('It was his habit, not a one-off. Asked how he had become a war hero after his boat was cut in half in 1943, he said: '
         '<i>"It was involuntary. They sank my boat."</i> He shrinks himself, the crew and the story get bigger, and you like '
         'him more.'),
        ('The catch, and it matters for you: status lets self-deprecation land as confidence. A president who jokes about '
         'himself looks secure. A junior who does it all evening looks small. One light line, then the light goes to them, '
         'and your competence shows in the questions you ask.'),
    ],
    move=dict(line='Hand them the light.', steps=[
        ('Find the star.', 'Who in this room, or what about this person, deserves the headline?'),
        ('Take the side role.', 'One line that makes you the supporting character. Light, not grovelling.'),
        ('Point the room at them.', 'A credit or a question, then stop talking and let them shine.')]),
    scenes=[dict(id='9ecrMlwLBWI', title='JFK in Paris', year='1961', who='John F. Kennedy', role='real', dur='',
                 key='Press luncheon, Palais de Chaillot · John F. Kennedy',
                 line='"I am the man who accompanied Jacqueline Kennedy to Paris, and I have enjoyed it."',
                 watch=['The setup is two sentences. He lets the laugh land before moving on',
                        'The very next lines thank his hosts: the light keeps travelling',
                        'Only then does he get to business, with the room already on his side'],
                 read='Kennedy reads the room\'s obsession (Jackie) and joins it instead of competing with it.',
                 steal='When someone else is the room\'s favourite, name them first. You lose nothing and gain the room.',
                 rc='He was the US President, so self-deprecation read as confidence. With less status, keep it to one line and follow with competence.',
                 note='Content: archive footage of a speech. Clip on HelmerReenberg.')],
    specs=[('Talking about yourself is a reward', 'People gave up 17% of their earnings to talk about themselves, and the brain\'s reward system lit up when they did (Tamir and Mitchell 2012).'),
           ('Attention you can see', 'Questions and follow-ups are the visible proof you are listening; they predict being liked (Huang et al. 2017, Stop 2.3).'),
           ('Eyes in bouts, not a stare', 'In a large lab study, people preferred mutual gaze of about 3.3 seconds at a time on average, with big differences between people (Binetti et al. 2016).')],
    fig=('2.1', 'Pitch first puts the light on you and your list. The Spotlight puts it on them, with you holding the lamp.'),
    evidence=[('Self-disclosure is intrinsically rewarding; people forgo money for it', 's', 'Tamir and Mitchell 2012', 'tamir'),
              ('Preferred mutual gaze averages about 3.3 seconds and varies widely', 'm', 'Binetti et al. 2016', 'binetti'),
              ('Kennedy\'s Paris opener, verbatim', 's', 'JFK Library, News Conference 12', 'jfk_paris'),
              ('"It was involuntary. They sank my boat."', 's', 'JFK Library, PT-109', 'jfk_pt109')],
    tags=[('myth', '"Kennedy held eye contact 70 to 80% of the time."', 'No study measured Kennedy\'s gaze. What exists: people prefer mutual gaze in bouts of about 3.3 seconds on average (Binetti et al. 2016). Look, look away, look back.', 'binetti'),
          ('myth', '"Kennedy spoke at a calm 120 to 130 words a minute."', 'TIME clocked him in bursts of 327 words a minute in 1961 when he left his script. He had a range, not a number. Slow down for the line that matters.', 'langlog'),
          ('myth', '"He read 1,200 words a minute."', 'Biographer Richard Reeves traces the figure to a chat between Kennedy and TIME\'s Hugh Sidey, not a test. Speed reading trades away comprehension (Rayner et al. 2016).', 'reeves'),
          ('part', '"Gladstone made you think he was the cleverest man in England; Disraeli made you think you were the cleverest woman."', 'Usually credited to Jennie Jerome, Churchill\'s mother. I could not find a primary source, so treat the quote as folklore. The lesson holds (Tamir and Mitchell).', 'gladstone')],
    world=('Someone introduces you at an event: "This is Kevin, the website guy." Don\'t launch the services list. Try: '
           '"Guilty. But Rhea\'s the reason I came tonight, she\'s built the best clinic brand in town. How did you two meet?" '
           'One line of you, then the light goes back out. Your competence shows up later, in the questions you ask.'),
    drill=dict(name='The light handoff', mins='2 min', steps=['Name the star in your first sentence.',
               'Cast yourself as the side character in one light line.', 'End with a question that puts them back on stage.'],
               mistake='Self-deprecating so hard you look small. One light line, then competence.'),
    tryit=('In one conversation today (a client call counts), make your first sentence about the other person: a credit or a '
           'question about their work. Then time how long they talk. Write the number down; you will beat it in Stop 2.3.'),
    writer=('Charmers in great scripts rarely talk about themselves on entrance. Write an entrance where your character makes '
            'someone else the subject, and let the audience work out later who held the power.'),
    room='"Charm isn\'t being interesting, it\'s making the other person feel interesting. I hand them the light first, then I talk shop."',
    nextq='If attention is the gift, what is the cheapest way to prove you were paying it? Stop 2.2.',
    checks=[dict(q='In Tamir and Mitchell 2012, how much of their possible earnings did people give up to talk about themselves?',
                 o=['About 2%', 'About 17%', 'About 50%'], a=1, w='17%. Talking about yourself is rewarding enough that people pay for it.'),
            dict(q='What made Kennedy\'s Paris opener work?', o=['He listed his achievements', 'He made his wife the star and himself the side character', 'He spoke fast to fill the room'],
                 a=1, w='He named the room\'s favourite, cast himself as her plus-one, then thanked his hosts.'),
            dict(q='The "70 to 80% eye contact" rule...', o=['Comes from a study of Kennedy', 'Has no source; people prefer gaze in bouts of about 3 seconds', 'Is the minimum for trust'],
                 a=1, w='Binetti et al. 2016: preferred mutual gaze averaged 3.3 seconds and varied a lot.')],
))

# ---------------------------------------------------------------- 2.2
STOPS.append(dict(
    id='2.2', day=14, title='The Name',
    why=('Walter White wanted one thing from the man in the desert: say my name. Everyone you meet wants the same thing, '
         'minus the menace. Jim Farley said he could call fifty thousand people by their first names, and Dale Carnegie '
         'credits that habit with helping him put Franklin Roosevelt in the White House.'),
    dossier=dict(name='Jim Farley', role='Franklin Roosevelt\'s campaign manager, 1932 · as told by Dale Carnegie, 1936',
                 facts=[('Known for', 'Names, plus personal letters to thousands, all signed "Jim"'),
                        ('The move', 'Catch it, link it, keep it'),
                        ('Steal it for', 'Discovery calls, events, and the people everyone else ignores')],
                 stamp=('hold', 'Holds up')),
    cold=dict(q=('In a lab, people learned faces with two labels each: a job and a surname. Some labels were the same word: '
                 'a man who is a baker, a man called Baker. Which did people forget more: the job, the name, or neither? '
                 'Confidence 1 to 5.'),
              a=('<b>The name, by a long way.</b> It is much harder to recall that a man is called Baker than that he is a baker '
                 '(McWeeny et al. 1987). A job connects to everything you know; a name connects to nothing. When a later study '
                 'made names meaningful, the gap disappeared (Cohen 1990). Forgetting names is a memory design problem, not a '
                 'character flaw, and design problems have fixes.')),
    story=[
        ('Carnegie tells it like this. He asked Farley the secret of his success. "Hard work," said Farley. "Don\'t be funny," '
         'said Carnegie. So Farley asked what Carnegie thought it was. "I understand you can call ten thousand people by their '
         'first names." "No. You are wrong," said Farley. "I can call fifty thousand people by their first names."'),
        ('The number is Farley\'s own boast, so hold it loosely. The habit behind it is the lesson. Every time he met '
         'someone, he got the full name and a few facts about their family, work and politics, and filed them in his head. '
         'After a long campaign trip he wrote to one person in each town, asked for a list of everyone he had talked to, then '
         'sent each of them a personal letter that began "Dear Bill" or "Dear Jane" and was signed "Jim".'),
        ('Carnegie turned it into Principle 6: <i>"Remember that a person\'s name is to that person the sweetest and most '
         'important sound in any language."</i> Sixty years later, three experiments tested it. When someone remembered a '
         'person\'s name, that person was more likely to agree to buy from them, because it felt like a compliment. '
         'Forgetting a name did not lower compliance, so trying costs you little (Howard, Gengler and Jain 1995).'),
        ('Now the dark mirror. Miranda Priestly calls every assistant "Emily". When Andy corrects her, it does not even '
         'register. In films, refusing to learn a name is how writers tell you someone is disposable. Walter White\'s '
         '"Say my name" is the same hunger turned into a threat: he wants the name with the fear attached.'),
    ],
    move=dict(line='Catch it, link it, keep it.', steps=[
        ('Catch it.', 'Say it back on the first hear ("Rhea? Hi, Rhea."). Missed it? Ask again now; it only gets worse later.'),
        ('Link it.', 'Give it meaning: a friend with the same name, an image, their business.'),
        ('Keep it.', 'Write it with one detail within the hour, and use it once at goodbye.')]),
    scenes=[dict(id='MPYlxeG-8_w', title='Breaking Bad', year='2012', who='Bryan Cranston', role='anti-hero', dur='',
                 key='Say my name · Walter White', line='"Say my name."',
                 watch=['Walt makes the other man say the name. Whoever says it first concedes',
                        'The long silence before the name lands',
                        'How one word rearranges who holds power in the scene'],
                 read='Walt turns a name into a status test. The name carries his whole reputation.',
                 steal='Notice how much weight a name carries, then use that weight to give respect, not take it.',
                 rc='Menace is not charisma; it is fear. Copy the pause, never the threat.',
                 note='Content: drug crime, menace, strong language. Clip on Rotten Tomatoes TV.'),
            dict(id='jjiJ-aeBj9Y', title='The Devil Wears Prada', year='2006', who='Meryl Streep and Anne Hathaway', role='villain', dur='',
                 key='"There you are, Emily" · Miranda Priestly',
                 line='"There you are, Emily. How many times do I have to scream your name?"',
                 watch=['Andy\'s correction: "Actually, it\'s Andy."', 'Miranda does not even register it',
                        'How small Andy looks for the rest of the scene'],
                 read='Miranda signals that Andy is interchangeable. One wrong name does the work of a speech.',
                 steal='Do the opposite with the people others ignore: the receptionist, the driver, the junior designer. They notice, and they talk.',
                 rc='Comedy exaggerates, but real bosses who never learn juniors\' names send the same signal.',
                 note='Content: workplace humiliation, mild. Clip on JoBlo Movie Clips.')],
    specs=[('Names are hard by design', 'Surnames were far harder to recall than jobs, even the same word (McWeeny et al. 1987). Make the name mean something and the gap closes (Cohen 1990).'),
           ('Remembered means complimented', 'Three experiments: remembering a name raised compliance with a purchase request, and people felt complimented (Howard, Gengler and Jain 1995).'),
           ('The emperor\'s routine', 'Carnegie says Napoleon III remembered names by asking again when he missed one, asking the spelling, repeating it, and writing it down when alone. Old trick, same mechanism: repetition plus meaning.')],
    fig=('2.2', 'The name loop. Most people stop after hearing it once. Saying it back, linking it and writing it are what make it stick.'),
    evidence=[('Names are harder to recall than occupations (Baker/baker)', 's', 'McWeeny, Young, Hay and Ellis 1987', 'mcweeny'),
              ('Meaningful names lose the recall penalty', 'm', 'Cohen 1990', 'cohen'),
              ('Name remembrance raises compliance, read as a compliment', 'm', 'Howard, Gengler and Jain 1995', 'howard'),
              ('Farley\'s 50,000 names and letters', 'h', 'Carnegie 1936 (his account)', 'carnegie')],
    tags=[('part', '"A person\'s name is the sweetest sound in any language."', 'Remembering it works like a compliment (Howard et al. 1995). Overusing it is another matter: a name in every sentence sounds like a sales script. My rule, not a study: hello, goodbye, maybe once in the middle.', 'howard'),
          ('part', '"Farley knew 50,000 names."', 'That is Farley\'s own claim, reported by Carnegie. Treat the number as legend and the habit as real.', 'carnegie'),
          ('myth', '"Some people just aren\'t good with names."', 'Names are harder than other facts for everyone (McWeeny et al. 1987), and giving them meaning closes the gap in the lab (Cohen 1990). It is a technique gap, not a personality.', 'mcweeny')],
    world=('Before any discovery call, write the owner\'s name and the receptionist\'s name at the top of your notes. Use the '
           'owner\'s once in the first minute and once at the close. Say the receptionist\'s name next time you call: in a '
           'clinic, she decides whether you get through. And ask, don\'t assume: in Ahmedabad "Dr. Shah" or "Rakeshbhai" may '
           'be the respectful version, while a UK or Australian lodge owner will want first names fast. "What should I call '
           'you?" is never wrong.'),
    drill=dict(name='Catch, link, keep', mins='2 min', steps=['Say the name back on the first hear; ask the spelling if it is unusual.',
               'Link it to an image, a friend with the same name, or their business.', 'Write it with one detail within the hour, then use it once at goodbye.'],
               mistake='Saying it ten times like a sales script. Hello, goodbye, maybe once in the middle.'),
    tryit=('Today, learn one name you usually skip: the guard, the chai seller, a clinic receptionist, your caller\'s colleague. '
           'Use it once. Save it in your phone with one detail.'),
    writer=('What a character calls someone is characterisation. Miranda\'s "Emily" tells you everything in one word. Write a '
            'scene where a nickname, a wrong name or a title shows the power between two people.'),
    room='"Names are hard for everyone because they mean nothing. So I make them mean something: say it back, link it, write it down. Remembering a name is the cheapest respect there is."',
    nextq='You have their name. Now, what do you ask once the small talk runs out? Stop 2.3.',
    checks=[dict(q='Why is a name harder to remember than a job (the Baker/baker paradox)?', o=['Names are longer', 'A name connects to nothing you know; a job connects to lots', 'People don\'t listen'],
                 a=1, w='McWeeny et al. 1987. Give the name meaning and recall improves (Cohen 1990).'),
            dict(q='In Howard, Gengler and Jain 1995, remembering someone\'s name...', o=['Raised compliance with a purchase request', 'Had no effect', 'Felt manipulative and lowered compliance'],
                 a=0, w='It worked like a compliment. Forgetting did not lower compliance.'),
            dict(q='Miranda calling Andy "Emily" shows...', o=['She is busy', 'Andy is replaceable to her', 'Names don\'t matter in fashion'],
                 a=1, w='Refusing to learn a name is how fiction, and bad bosses, signal you are interchangeable.')],
))

# ---------------------------------------------------------------- 2.3
STOPS.append(dict(
    id='2.3', day=15, title='The Second Question',
    why=('Larry King interviewed presidents, film stars and total unknowns on CNN for 25 years, and his rule sounds almost '
         'childish: <i>"I remind myself every morning: Nothing I say this day will teach me anything. So if I\'m going to '
         'learn, I must do it by listening."</i> The first question is manners. The second one is where people decide '
         'whether you actually care.'),
    dossier=dict(name='Larry King', role='Host, Larry King Live, CNN, 1985 to 2010',
                 facts=[('Known for', 'Short, plain questions like "What\'s the biggest mistake you made?"'),
                        ('The move', 'Go three deep'),
                        ('Steal it for', 'Discovery calls, first meetings, anyone who underestimates you')],
                 stamp=('hold', 'Holds up')),
    cold=dict(q=('Researchers recorded speed dates. Which behaviour predicted that a partner said yes to a second date: '
                 '(a) talking more about yourself, (b) asking more follow-up questions, or (c) agreeing with everything? '
                 'Confidence 1 to 5.'),
              a=('<b>(b) Follow-up questions.</b> Speed daters who asked more follow-ups got more second-date yeses, and in the '
                 'same research people did not expect questions to make them more liked (Huang et al. 2017). A 2025 '
                 'independent audit of the paper corrected minor reporting errors and confirmed every conclusion.')),
    story=[
        ('King\'s questions were short and plain on purpose. In a 1995 interview he explained that he did not ask a president '
         'about Geneva or Cuba. He asked, <i>"Mr. President, what don\'t you like about this job?"</i> or <i>"What\'s the biggest '
         'mistake you made?"</i> Plain questions hand the other person the floor. Clever questions keep it for you.'),
        ('Now the scene you need, Kevin. In <i>Ted Lasso</i>, Rupert, the slick ex-owner, hustles Ted into a game of darts for '
         'high stakes. He has decided the folksy American coach is a mark. Ted keeps throwing and tells a story: people have '
         'underestimated him his whole life, and none of them ever asked him a single question, like whether he had played '
         'a lot of darts. He had, for years, with his dad. Then he hits exactly what he needs.'),
        ('Ted credits the line he lives by, "Be curious, not judgmental", to Walt Whitman. Whitman never wrote it (the truth '
         'tags have the receipt). The idea still holds. Rupert judged; Ted got curious and got underestimated; the missing '
         'question cost Rupert the game.'),
        ('This is your edge with the curly hair and the young face. People who judge you on sight will underestimate you. '
         'Curiosity flips it: while they are busy assuming, you ask the second and third question, and by the time they look '
         'up, you understand their business better than they understand yours.'),
    ],
    move=dict(line='Go three deep.', steps=[
        ('The door.', '"What are you working on?" Easy, open, about them.'),
        ('About their answer.', '"What\'s the hardest part of that?" Build on what they said, not on your next topic.'),
        ('One more.', '"What would fixing it change for you?" Then, and only then, talk. Close with "Is there something else?"')]),
    scenes=[dict(id='3S16b-x5mRA', title='Ted Lasso', year='2020', who='Jason Sudeikis', role='hero', dur='04:41',
                 key='Darts with Rupert · Ted Lasso', line='"Be curious, not judgmental."',
                 watch=['Rupert\'s assumptions in his first lines', 'Ted keeps his tone light while the stakes rise',
                        'The payoff names the exact question nobody asked'],
                 read='Rupert judged; Ted got underestimated; the unasked question decided the game.',
                 steal='Before you judge a prospect\'s website or a person\'s skill, ask the question that would prove you wrong.',
                 rc='Television pays off the underdog on cue. In real rooms, curiosity wins over months, not in one throw.',
                 note='Content: mild language. Clip on CinemaGalaxy (fan upload).')],
    specs=[('Follow-ups get you liked', 'Especially follow-ups, because they prove you listened. People also underestimate this effect, so most under-ask (Huang et al. 2017).'),
           ('Don\'t boomerask', 'Asking "How was your weekend?" so you can say "Mine was amazing!" reads as insincere and less likeable, though askers think it is fine. Eight studies (Brooks and Yeomans 2025).'),
           ('Go deeper sooner', 'Strangers\' deep conversations felt less awkward and more connecting than people predicted; they underestimated how much others cared (Kardas, Kumar and Epley 2022).'),
           ('"Something", not "anything"', 'In a clinic trial, "Is there something else you want to address today?" eliminated 78% of unmet concerns; "anything else" did no better than not asking (Heritage et al. 2007).')],
    fig=('2.3', 'Three deep, then the close. The red branch is the boomerask: a question asked only to tell your own story.'),
    evidence=[('Question-asking, especially follow-ups, increases liking', 'm', 'Huang et al. 2017 (audited 2025)', 'huang'),
              ('Boomerasking reads as insincere', 'm', 'Brooks and Yeomans 2025', 'boomer'),
              ('People underestimate how much strangers enjoy deep talk', 'm', 'Kardas, Kumar and Epley 2022', 'kardas'),
              ('"Something else?" beats "anything else?" (one trial)', 'm', 'Heritage et al. 2007', 'heritage'),
              ('King\'s listening rule (widely quoted; primary not located)', 'h', 'Newsweek 2021', 'king')],
    tags=[('myth', '"Walt Whitman said: Be curious, not judgmental."', 'The co-director of the Walt Whitman Archive says Whitman never wrote or said it. The earliest known print is a 1986 syndicated advice column. Good line, wrong author.', 'snopes'),
          ('hold', '"People like people who ask questions."', 'Yes, especially follow-ups (Huang et al. 2017). But only real ones: a question used as a launchpad for your own story backfires.', 'huang'),
          ('part', '"Small talk first, deep talk much later."', 'Start light, but go one level deeper sooner than feels comfortable. Strangers enjoy it more than you expect (Kardas et al. 2022).', 'kardas')],
    world=('Discovery call with a safari operator. Door: "How do most guests find you now?" Deeper: "What happens to the ones who '
           'find you on Instagram?" Deepest: "If that worked twice as well, what would you do with the extra bookings?" Close: '
           '"Is there something else you want the website to fix?" Now pitch, and build the pitch out of their words.'),
    drill=dict(name='Three deep', mins='2 min', steps=['Ask a door question about them.', 'Ask about their last answer.',
               'Ask one more about that answer.', 'Close with "Is there something else...?"'],
               mistake='Boomerasking: asking so you can tell your own story.'),
    tryit=('In your next conversation, go three deep before you say anything about yourself or MTRX™. Tally your follow-ups on a '
           'sticky note. End with "something else?" and note whether it surfaced anything new.'),
    writer=('Questions are characterisation. A character who asks the second question is listening; one who boomerasks is a '
            'narcissist the audience spots in a line. Write a two-person scene where power shifts because one of them asks a '
            'follow-up the other did not expect.'),
    room='"The first question is manners. The second one is interest. I go three deep before I pitch, so my pitch is built from their words."',
    nextq='They tell you some good news. Most people ruin this moment without noticing. How? Stop 2.4.',
    checks=[dict(q='Speed daters who did what got more second-date yeses?', o=['Talked about themselves more', 'Asked more follow-up questions', 'Agreed more'],
                 a=1, w='Huang et al. 2017. And people did not predict it.'),
            dict(q='You ask "How was your weekend?" then say "Mine was amazing!" Researchers call this...', o=['Mirroring', 'Boomerasking', 'Active listening'],
                 a=1, w='Brooks and Yeomans 2025: it reads as insincere, even though askers think it is fine.'),
            dict(q='Which closing question surfaced the most unmet concerns in a clinic trial?', o=['"Anything else?"', '"Is there something else you want to address today?"', '"Are we done?"'],
                 a=1, w='Heritage et al. 2007: "something" eliminated 78% of unmet concerns; "anything" did no better than not asking.')],
))

# ---------------------------------------------------------------- 2.4
STOPS.append(dict(
    id='2.4', day=16, title='The Support Response',
    why=('Peggy Olson tells Don Draper he never says thank you. He snaps: <i>"That\'s what the money is for!"</i> One of the '
         'best characters on television, and in that moment the worst possible answer. When someone brings you their news, '
         'good or bad, it is a test: do you keep the ball in their court, or take it?'),
    dossier=dict(name='Don Draper', role='Creative director, Mad Men · "The Suitcase", season 4, 2010',
                 facts=[('Known for', 'The best pitches on TV, and the worst thank-yous'),
                        ('The move', 'Keep the ball in their court'),
                        ('Steal it for', 'Your callers, your clients\' wins, anyone who shares news with you')],
                 stamp=('anti', 'Anti-model')),
    cold=dict(q=('Your client messages: "We just got featured in a travel magazine!" Which reply best predicts a stronger '
                 'relationship over time? (a) "Congrats." (b) "Hope the site can handle the traffic." (c) "That\'s huge! How did '
                 'they find you?" (d) "Nice. Quick one about the invoice..." Confidence 1 to 5.'),
              a=('<b>(c).</b> Researchers sorted responses to good news into four kinds. Only the enthusiastic, engaged one (active '
                 'and constructive) went with better relationships; the quiet "congrats" did not carry the benefit (Gable et al. '
                 '2004). The most polite answer is not the best one.')),
    story=[
        ('Late at night in "The Suitcase", Peggy, whose ideas keep turning up in Don\'s pitches, tells him he never says '
         'thank you. Don answers the logic and misses the feeling: <i>"That\'s what the money is for!"</i> It is funny, it is '
         'iconic, and it is exactly how bosses lose their best people.'),
        ('Sociologist Charles Derber named the two moves in his book <i>The Pursuit of Attention</i>. A <b>shift response</b> '
         'turns the conversation to you: "I feel lousy today." "Same here, I barely slept." A <b>support response</b> keeps it '
         'on them: "Oh no. What\'s going on?" He called the shifting habit conversational narcissism, and most of us do it '
         'while trying to relate.'),
        ('Shelly Gable\'s team then asked what happens when people share good news. There are four ways to answer: '
         'active-constructive (excited, asks about it), passive-constructive ("nice"), active-destructive (finds the problem) '
         'and passive-destructive (ignores it, changes topic). Across four studies, sharing good news lifted people\'s day '
         'beyond the event itself, and more so when the listener responded actively and constructively. Couples who usually '
         'responded that way reported more intimacy and satisfaction.'),
        ('Relating with your own story is not the crime. Keeping the ball is. One line, then hand it back: "Same thing happened '
         'with my first client. How did you handle it?"'),
    ],
    move=dict(line='Keep the ball in their court.', steps=[
        ('Match the energy.', 'Big news gets a big reaction. "That\'s huge!"'),
        ('Make them relive it.', '"How did it happen? What did they say? Which photo did they use?"'),
        ('Relate in one line, then hand it back.', 'Your story is a bridge, not a destination.')]),
    scenes=[dict(id='77Y6CIyyBcI', title='Mad Men', year='2010', who='Jon Hamm and Elisabeth Moss', role='anti-hero', dur='00:33',
                 key='"That\'s what the money is for!" · Don Draper', line='"That\'s what the money is for!"',
                 watch=['Peggy\'s bid is small: she wants acknowledgement, not money', 'Don answers the logic and misses the feeling',
                        'Watch Peggy\'s face after the line: that is the cost'],
                 read='Don treats a bid for recognition as a pay dispute. It is a destructive response delivered with charisma.',
                 steal='When someone on your team brings you a win, name what they did and ask how they did it, before money or next steps.',
                 rc='Don says it out loud for drama. Most real bosses say it with silence, which is worse.',
                 note='Content: workplace conflict. Clip on Marinatin (fan upload).')],
    specs=[('Good news needs a good listener', 'Sharing positive events boosts well-being beyond the event, especially when the listener is active and constructive (Gable et al. 2004, four studies).'),
           ('Shift vs support', 'Derber\'s labels for taking the attention or giving it back. A descriptive framework from sociology, not an experiment, but you will hear shifts everywhere once you know it.'),
           ('Support usually holds a question', 'A good support response is a follow-up question in disguise, which is why it works (Huang et al. 2017, Stop 2.3).')],
    fig=('2.4', 'Four ways to answer good news. Only the top right builds the relationship. The polite top left is not enough.'),
    evidence=[('Active-constructive responding goes with relationship well-being', 's', 'Gable, Reis, Impett and Asher 2004', 'gable'),
              ('Shift and support responses; conversational narcissism', 'h', 'Derber, The Pursuit of Attention', 'derber'),
              ('Follow-ups signal responsiveness', 'm', 'Huang et al. 2017', 'huang')],
    tags=[('part', '"Sharing your own similar story shows empathy."', 'Sometimes. A one-line relate that hands the ball back is fine. A story that keeps the ball is a shift response (Derber).', 'derber'),
          ('myth', '"A quick congrats is enough."', 'The quiet supportive reply did not carry the relationship benefits in Gable et al. 2004; the enthusiastic, curious one did.', 'gable'),
          ('hold', '"How you handle good news matters, not just bad news."', 'Responses to good news predicted relationship quality in their own right (Gable et al. 2004).', 'gable')],
    world=('Your caller books a discovery call and messages you, buzzing. Don\'t reply "nice". Reply: "Massive! Which clinic? What did '
           'you say that made them agree?" Then use her answer in the next caller huddle. You get a better script, and a caller '
           'who wants to book the next one.'),
    drill=dict(name='Ball in their court', mins='2 min', steps=['Match the energy of their news.', 'Ask them to relive it: how, who, what did they say.',
               'If you relate, one line, then hand it back with a question.'],
               mistake='The one-word "congrats", then straight to your own topic.'),
    tryit=('Today, find one piece of someone\'s good news (a WhatsApp status, a client post, your caller\'s booking) and reply '
           'active-constructive: energy plus a question about how it happened. Note how long their reply is compared with usual.'),
    writer=('The shift response is a gift to writers: a character who turns every scene to himself reveals the wound without '
            'exposition. Write a dinner scene where one character shifts every topic to himself and nobody says it out loud.'),
    room='"When someone tells me good news, I don\'t say \'nice\' and move on. I ask how they pulled it off. Keeping the ball in their court is the whole trick."',
    nextq='Lighting up their win is reactive. Can you create the moment yourself, without sounding like a flatterer? Stop 2.5.',
    checks=[dict(q='"I feel lousy today." "Same here, I barely slept." This is a...', o=['Support response', 'Shift response', 'Callback'],
                 a=1, w='Derber\'s shift response: the attention moves to you.'),
            dict(q='In Gable et al. 2004, which response to good news went with better relationships?', o=['A quick, quiet "congrats"', 'Enthusiastic, with questions about it', 'Pointing out a risk, to be helpful'],
                 a=1, w='Active-constructive. The quiet version did not carry the benefit.'),
            dict(q='Peggy wants thanks; Don says "That\'s what the money is for!" What did he miss?', o=['She wanted a raise', 'She wanted recognition, not money', 'She wanted a new account'],
                 a=1, w='A bid for recognition answered with logistics is a destructive response.')],
))

# ---------------------------------------------------------------- 2.5
STOPS.append(dict(
    id='2.5', day=17, title='The Compliment',
    why=('Melvin Udall is rude, obsessive and impossible. Then he says one sentence to Carol and she calls it maybe the best '
         'compliment of her life: <i>"You make me want to be a better man."</i> The lesson is not to be Melvin. It is that the '
         'compliments people keep are not about how they look. They are about what they changed.'),
    dossier=dict(name='Melvin Udall', role='As Good as It Gets, 1997 · played by Jack Nicholson',
                 facts=[('Known for', 'Being awful for two hours, then landing one perfect line'),
                        ('The move', 'Compliment the change, not the trait'),
                        ('Steal it for', 'Thanking clients, praising callers, rooms full of people you admire')],
                 stamp=('hold', 'Holds up')),
    cold=dict(q=('People wrote a genuine compliment to someone they knew, then predicted how the recipient would feel. Did they '
                 '(a) overestimate how good it would feel, (b) get it about right, or (c) underestimate it? Confidence 1 to 5.'),
              a=('<b>(c), and they overestimated the awkwardness too.</b> Nine experiments, same result (Zhao and Epley 2021). '
                 'Thank-you letters show the same gap: writers underestimated how surprised and happy recipients would be '
                 '(Kumar and Epley 2018). You are almost certainly under-complimenting the people you rely on.')),
    story=[
        ('Carol demands it: pay me a compliment. Melvin fumbles, talks about himself and his pills, and nearly loses her. Then '
         'he explains that the morning after she turned him down, he started taking the medication he hated, and lands the line: '
         '<i>"You make me want to be a better man."</i> Seconds later he admits he may have overshot: he was only aiming to keep her from walking '
         'out. The honesty makes it land harder.'),
        ('Why it works: it is specific, it cost him something to say, and it is about her effect on him, not her face. That is '
         'the whole craft. "You look great" is about genes. "You make me want to be better" is about what she did.'),
        ('Kennedy had the version for a room. At a 1962 White House dinner for Nobel Prize winners he said: <i>"I think this is '
         'the most extraordinary collection of talent, of human knowledge, that has ever been gathered together at the White '
         'House, with the possible exception of when Thomas Jefferson dined alone."</i> A compliment to everyone present, '
         'wrapped in a joke so nobody had to answer it.'),
        ('And here is the part the legend skips: his office files for that dinner hold drafts by his speechwriter, Arthur '
         'Schlesinger Jr. Spontaneous charm is often prepared charm. Good news for you, Kevin: the gap you named, being '
         'unprepared, is fixable. Write the compliment before you walk in.'),
    ],
    move=dict(line='Compliment the change, not the trait.', steps=[
        ('Be specific.', 'Name exactly what they did: "the way you handled that angry patient".'),
        ('Credit the choice.', 'Effort, judgement, taste. Not looks, not talent they were born with.'),
        ('Say the impact, then stop.', '"I\'m teaching it to my callers." No request in the same breath.')]),
    scenes=[dict(id='A75AgrH5eqc', title='As Good as It Gets', year='1997', who='Jack Nicholson and Helen Hunt', role='anti-hero', dur='',
                 key='The better-man compliment · Melvin Udall', line='"You make me want to be a better man."',
                 watch=['The awful first attempt: he talks about himself', 'The turn: the compliment is about her effect on him',
                        'His honest admission afterwards: he was trying to keep her from leaving'],
                 read='It lands because it is specific, costly to say, and about what she changed.',
                 steal='Tell someone what they changed in you or your work. Effect beats adjectives.',
                 rc='It works because the film made him unlikeable first. In life, a flood of praise from someone you barely know reads as a setup.',
                 note='Content: references to mental illness, mild language. Clip on Movieclips.')],
    specs=[('You underrate your compliments', 'Expressers underestimated how positive recipients felt and overestimated the awkwardness, in nine experiments (Zhao and Epley 2021).'),
           ('Thanks lands harder than you think', 'Gratitude-letter writers underestimated recipients\' surprise and happiness (Kumar and Epley 2018).'),
           ('Obvious angles kill it', 'Across studies, ingratiation raises liking, but the more transparent the motive, the less it works (Gordon 1996). Hence: never compliment and ask in one breath.')],
    fig=('2.5', 'Generic, specific, specific plus impact. The bars are my scale, not data; the data say you underrate all three.'),
    evidence=[('People underestimate the positive impact of their compliments', 's', 'Zhao and Epley 2021', 'zhao'),
              ('People undervalue expressing gratitude', 'm', 'Kumar and Epley 2018', 'kumar'),
              ('Ingratiation works less when the motive is transparent', 'm', 'Gordon 1996 (meta-analysis)', 'gordon'),
              ('Kennedy\'s Nobel dinner line, verbatim', 's', 'JFK Library quotations', 'jfk_quotes'),
              ('Drafts for the dinner by Arthur Schlesinger Jr.', 's', 'JFK Library, President\'s Office files', 'jfk_nobel_files')],
    tags=[('myth', '"Compliments make people uncomfortable, so skip them."', 'Recipients feel better, and less awkward, than givers predict (Zhao and Epley 2021).', 'zhao'),
          ('part', '"Flattery always works."', 'It raises liking on average, but obvious motives undercut it (Gordon 1996). Genuine and specific beats lavish and strategic.', 'gordon'),
          ('hold', '"Thank-you notes are worth the effort."', 'Writers underestimated how surprised and happy recipients would be (Kumar and Epley 2018).', 'kumar')],
    world=('This week, send one gratitude message to a past client (HansWild counts): one specific thing they did that made the '
           'project better, and what it taught you. No ask, no link. People refer the person who made them feel seen, and you '
           'will be surprised by the reply.'),
    drill=dict(name='Change, not trait', mins='2 min', steps=['Name the specific action.', 'Credit the choice or effort, not looks or talent.',
               'Say the impact on you or others.', 'Stop. No request attached.'],
               mistake='Generic praise ("great job") or a compliment that is really a setup for a request.'),
    tryit=('Write one genuine, specific compliment to someone today (a caller, a client, a friend). Before you send it, rate from '
           '1 to 10 how happy you think it will make them. After they reply, rate how happy they seemed. Log the gap next to your '
           'calibration log from Stop 1.12.'),
    writer=('A compliment scene works when it costs the speaker something. Melvin\'s costs him his pride and his secret. Write a '
            'compliment that forces the speaker to reveal something he would rather hide.'),
    room='"I don\'t compliment looks, I compliment choices: what someone did and what it changed. And I never attach a request to it."',
    nextq='Compliments work in the moment. What makes someone remember you a year later? Stop 2.6.',
    checks=[dict(q='People who wrote genuine compliments predicted the recipient\'s reaction. They...', o=['Overestimated how good it felt', 'Underestimated how good it felt and overestimated the awkwardness', 'Were accurate'],
                 a=1, w='Zhao and Epley 2021, nine experiments.'),
            dict(q='Why does Melvin\'s "better man" line land?', o=['It is about her looks', 'It names her effect on him, and it cost him to say it', 'It is a joke'],
                 a=1, w='Effect beats adjectives, and it reveals something he would rather hide.'),
            dict(q='Kennedy\'s "...when Thomas Jefferson dined alone" line is an example of...', o=['Praising the room inside a joke', 'Self-promotion', 'A cold read'],
                 a=0, w='A compliment to everyone present, wrapped so no one had to answer. His files hold speechwriter drafts: charm can be prepared.')],
))

# ---------------------------------------------------------------- 2.6
STOPS.append(dict(
    id='2.6', day=18, title='The Callback',
    why=('As a young man, Bill Clinton started keeping an index card on almost everyone he met. By 1980 the file held more than '
         '10,000 names. Twelve years later, on a debate stage, a voter asked how the national debt had affected him personally. '
         'He asked her to tell him again, then said: <i>"In my state, when people lose their jobs, there\'s a good chance I\'ll '
         'know them by their names."</i>'),
    dossier=dict(name='Bill Clinton', role='42nd US President · card file kept from his twenties, per biographer David Maraniss',
                 facts=[('Known for', 'Remembering people, then proving it'),
                        ('The move', 'Bring it back'),
                        ('Steal it for', 'Follow-ups, repeat clients, the people you met once at an event')],
                 stamp=('hold', 'Holds up')),
    cold=dict(q=('Fresh information you have just learned, like the details from a networking event: how does it fade? (a) Slowly '
                 'and evenly over weeks, (b) steeply in the first hours and day, then slowly, or (c) hardly at all if you were '
                 'interested? Confidence 1 to 5.'),
              a=('<b>(b).</b> Ebbinghaus mapped the curve in the 1880s, and a 2015 replication found the same shape: steep early '
                 'loss, then a slow tail (Murre and Dros 2015). The card file is not old-fashioned. It is the fix for a design '
                 'flaw in your memory.')),
    story=[
        ('Biographer David Maraniss describes a cardboard box of alphabetised, annotated index cards: classmates, professors, '
         'political organisers, anyone who might matter. Each card logged the important conversations he had had with that '
         'person, plus the dates they received a "Glad to Meet You" letter. When he ran for Congress in 1974 he went through '
         'the file every night, making calls and writing notes. By 1980 it held more than 10,000 names, and by 1982 it was '
         'computerised.'),
        ('Now watch the system pay out. Richmond, Virginia, 15 October 1992, the first town hall presidential debate. A voter '
         'asks how the national debt has affected each candidate personally. George Bush struggles: "I\'m not sure I get it. Help '
         'me with the question and I\'ll try to answer it." Clinton turns to her: <i>"Tell me how it\'s affected you again. You know '
         'people who have lost their jobs and lost their homes?"</i> Then the callback line about knowing them by name.'),
        ('The salesman\'s version is the Mackay 66. Harvey Mackay, who built an envelope company, made every salesperson fill in '
         'a 66-question profile on each customer: family, education, interests, what they are proudest of. His advice: you will '
         'never fill all 66, but 30 beats 20. Question 66 asks whether your competitor knows more of these answers than you do.'),
        ('The line, before it matters: a callback is memory used in the person\'s service. The same file used to log favours owed '
         'and pressure points is the Godfather\'s ledger. File 5 covers that border.'),
    ],
    move=dict(line='Bring it back.', steps=[
        ('Capture in ten minutes.', 'Name, where you met, one personal detail, one business detail.'),
        ('Schedule the touch.', 'A date tied to the detail: their launch, the exam, the end of season.'),
        ('Open with the callback.', 'Your next message starts with it: "How did the second clinic open?"')]),
    scenes=[dict(id='7ffbFvKlWqE', title='Clinton vs. Bush', year='1992', who='Bill Clinton and George H. W. Bush', role='real', dur='',
                 key='Richmond town hall debate · Bill Clinton',
                 line='"In my state, when people lose their jobs, there\'s a good chance I\'ll know them by their names."',
                 watch=['Bush answers the question; Clinton asks her one first', '"Tell me how it\'s affected you again"',
                        'He answers with people he knows, not statistics'],
                 read='Clinton turns a policy question into a callback to real people. Years of cards and letters make the line believable.',
                 steal='Answer with a person you remember, not a statistic: "A clinic owner I spoke to last month said exactly this."',
                 rc='Debates reward performance, and this was a practised political move. Practice is fine; inventing the memories is not.',
                 note='Content: politics. Clip on Seth Masket.')],
    specs=[('Forgetting is front-loaded', 'The forgetting curve drops fastest early, a shape replicated in 2015 (Murre and Dros). Write the card that night, not that week.'),
           ('A callback is a delayed follow-up', 'Follow-ups signal responsiveness, and responsiveness explained why question-askers were liked (Huang et al. 2017). A callback is the same signal, weeks later.'),
           ('Systems beat talent', 'Clinton\'s card file and the Mackay 66 are case histories, not experiments. Weak evidence, but the mechanism matches the memory science above.')],
    fig=('2.6', 'One card, seven fields, ten minutes. The curve on the right is why you write it tonight: most of it is gone by tomorrow.'),
    evidence=[('Ebbinghaus forgetting curve replicated', 'm', 'Murre and Dros 2015', 'murre'),
              ('Clinton\'s card file: 10,000+ names by 1980', 'm', 'Maraniss 1995, via NYT review', 'maraniss'),
              ('The Richmond exchange, verbatim', 's', 'Commission on Presidential Debates transcript', 'debate'),
              ('Mackay 66 customer profile', 'h', 'Harvey Mackay', 'mackay')],
    tags=[('part', '"Clinton just remembered everyone."', 'He had a system: a card file that passed 10,000 names by 1980 and was later computerised (Maraniss). Memory plus system, not magic.', 'maraniss'),
          ('hold', '"You\'ll forget most of an event by tomorrow."', 'Forgetting is steepest in the first hours (Ebbinghaus, replicated by Murre and Dros 2015). Write it down that night.', 'murre'),
          ('part', '"Keeping notes on people is creepy."', 'Notes are fine; using them to pressure people is not. Test: would you be comfortable if they saw the card? That is the disclosure test from File 5.', 'mackay')],
    world=('Build the people file in ClickUp: a list called People, one task per person, custom fields for Met at, Personal '
           'detail, Business detail, Next touch (a date) and Callback line. Set a ClickUp reminder on the Next touch date. Ten '
           'people this month. When you message them, the first line is the callback.'),
    drill=dict(name='The ten-minute card', mins='2 min', steps=['Within ten minutes: name, where you met, one personal and one business detail.',
               'Set a next-touch date tied to a detail.', 'Open the next message with the callback.'],
               mistake='Collecting cards and never calling back. A file you never use is just guilt.'),
    tryit=('Make the People list in ClickUp now with the five fields. Add the last three people you met (your department head '
           'counts: what did she care about?). Set one next-touch date for this week.'),
    writer=('Callback is also a screenwriting term: a line or object planted early that returns later with new meaning. Plant one '
            'detail in act one that a character brings back in act three, and the audience feels he was listening all along.'),
    room='"Memory is a system, not a gift. I write one personal and one business detail within ten minutes, and my next message opens with it. People remember the person who remembered."',
    nextq='You have six moves. Can you run them all in one evening without looking like a man with a checklist? Stop 2.7.',
    checks=[dict(q='By 1980, roughly how many names were in Clinton\'s card file, per Maraniss?', o=['About 500', 'About 2,000', 'More than 10,000'],
                 a=2, w='Each card logged their conversations and when they got a "Glad to Meet You" letter.'),
            dict(q='After a networking event, forgetting is usually...', o=['Slow and steady', 'Steep in the first hours and day, then slower', 'Zero if you were interested'],
                 a=1, w='Ebbinghaus\'s curve, replicated by Murre and Dros 2015. Write it down that night.'),
            dict(q='Clinton\'s 1992 answer worked mainly because he...', o=['Quoted debt statistics', 'Asked her to say more, then answered with people he knew by name', 'Talked over Bush'],
                 a=1, w='A question first, then a callback to real people.')],
))

# ---------------------------------------------------------------- 2.7
STOPS.append(dict(
    id='2.7', day=19, title='Boss fight: Spotlight night',
    why=('Six moves, one night. Pick a real room this week: a networking event, a family function, a client meeting, a college '
         'event. Walk in as George Newman, run the Spotlight, then score yourself honestly. Charm is a skill, so it gets a '
         'scorecard.'),
    dossier=dict(name='George Newman', role='Your persona · first field test', k='Subject: you',
                 facts=[('Known for', 'Smiling a lot, getting things done, never failing to deliver'),
                        ('The move', 'All six, spread across one evening'),
                        ('Win condition', '8 points or more on the scorecard')],
                 stamp=('field', 'Field test')),
    cold=dict(q=('Before the event, predict: out of the six moves, how many will you actually use tonight? Write the number and '
                 'your confidence from 1 to 5.'),
              a=('<b>Most people predict more than they deliver.</b> That gap is the point. Score yourself afterwards, compare with '
                 'your prediction, and log it like the calibration log in Stop 1.12. Good news: charisma is trainable. In two '
                 'studies, coached managers and MBA students were rated more charismatic afterwards (Antonakis, Fenley and Liechti '
                 '2011, average d = .62).')),
    story=[
        ('How each subject would play your room. Kennedy hands the light to the host before saying a word about himself. Farley '
         'leaves with a dozen names and a plan to write to each one. Larry King asks the bartender the plainest question in the '
         'room and gets the best story. Ted asks the question nobody asked. Melvin, cleaned up, says one true thing to one '
         'person. Clinton writes the cards in the cab home.'),
        ('You do not need all six on one person. You need them spread across the evening, the way a good host moves through a '
         'party. The timeline below is the order most evenings run in.'),
    ],
    move=dict(line='Spotlight night.', steps=[
        ('Arrive: hand the light.', 'Your first sentence to the host is about them (2.1).'),
        ('Intros: catch the name, go three deep.', 'Say it back, link it, then door, deeper, deepest (2.2, 2.3).'),
        ('Good news, goodbye, the cab.', 'Ball in their court, one real compliment, cards within the hour (2.4, 2.5, 2.6).')]),
    extra=('<h3>The scorecard</h3><div class="tbl-wrap"><table class="tbl score"><thead><tr><th>Move</th><th>What counts</th><th>Points</th></tr></thead><tbody>'
           '<tr><td>Hand the light</td><td>Your first sentence to a new person was about them</td><td>1</td></tr>'
           '<tr><td>The name</td><td>One point per new name said back and used at goodbye</td><td>up to 3</td></tr>'
           '<tr><td>Three deep</td><td>One conversation with three linked questions before you talked about yourself</td><td>2</td></tr>'
           '<tr><td>Ball in their court</td><td>You met someone\'s news with energy plus a question</td><td>1</td></tr>'
           '<tr><td>The compliment</td><td>One specific compliment about a choice, no ask attached</td><td>1</td></tr>'
           '<tr><td>The callback</td><td>One point per card in your People list within the hour</td><td>up to 2</td></tr>'
           '</tbody></table></div><p><b>8 to 10:</b> George Newman showed up. <b>5 to 7:</b> solid, run it again next week. '
           '<b>0 to 4:</b> pick two moves only and try again. Send progress to the bot either way.</p>'),
    scenes=[],
    rewatch=True,
    specs=[('Charisma can be trained', 'Randomly assigned managers who got charisma training were rated more charismatic by coworkers three months later, and MBA speeches improved after coaching (Antonakis, Fenley and Liechti 2011).'),
           ('Prediction makes the practice count', 'Predicting, acting and scoring is the same loop as the calibration log in Stop 1.12. Feedback on your own calls is what improves them.')],
    fig=('2.7', 'One evening, six moves, in the order most rooms run. Spread them out; never run all six on one person.'),
    evidence=[('Charisma training raised observer-rated charisma (mean d = .62)', 's', 'Antonakis, Fenley and Liechti 2011', 'antonakis'),
              ('Moves 2.1 to 2.6', 'm', 'See each stop\'s evidence table', 'tamir')],
    tags=[('myth', '"Charisma is something you are born with."', 'Training raised charisma ratings in a field experiment and a lab study (Antonakis, Fenley and Liechti 2011).', 'antonakis'),
          ('part', '"Charm means being the most interesting person in the room."', 'The six moves all point the other way: you make other people feel interesting, and they credit you for it.', 'tamir')],
    world=('Best rooms in the next two weeks: a client meeting, a college or alumni event, a family function where someone asks what '
           'you do. The "website guy" intro comes after the Spotlight, never before. If someone asks, one line is enough: "I build '
           'websites and AI tools for clinics and safari companies. What do you do?"'),
    drill=dict(name='Spotlight night', mins='evening', steps=['Hand the light on arrival.', 'Catch three names and go three deep once.',
               'Answer good news actively, give one specific compliment, write the cards within the hour.'],
               mistake='Running all six moves on one person. Spread them across the room.'),
    tryit=('Pick the room now. Put it in your calendar with the six moves in the description. Afterwards, fill in the scorecard, '
           'compare it with your prediction, and send progress to the bot.'),
    writer=('Write the same party scene twice: once from the guest who talks about himself all night, once from the guest who runs '
            'the Spotlight. Same events, different film.'),
    room='"I walk in planning to learn three names and one story, not to be impressive. Somehow that is exactly what makes people remember me."',
    nextq='File 2 asks the harder question underneath all six moves: what do people actually hunger for, and how do you read it?',
    checks=[dict(q='"Guilty, I make the websites. But Rhea\'s the reason I\'m here, ask her about her clinic." Which move?', o=['The callback', 'Hand the light', 'The support response'],
                 a=1, w='Stop 2.1: one light line about you, then the light goes to her.'),
            dict(q='"How was your weekend?" ... "Mine was amazing, I went to..." Which mistake?', o=['A callback', 'Boomerasking', 'An active-constructive response'],
                 a=1, w='Stop 2.3: the question was only a launchpad for your own story.'),
            dict(q='You meet 12 people at an event. When should you write the cards?', o=['Next week', 'Within the hour, before the steep part of forgetting', 'Only for the important ones'],
                 a=1, w='Stop 2.6: forgetting is front-loaded.')],
))

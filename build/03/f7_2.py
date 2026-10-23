from svg import box, t, arrow, line, svg

LAWS = [('LAW 1', 'Never Outshine the Master', 'hide your talent from the boss', 'the clever deputy', 'you never get the credit'),
        ('LAW 4', 'Always Say Less Than Necessary', 'stay quiet and seem strong', 'the silent operator', 'nobody trusts a blank'),
        ('LAW 15', 'Crush Your Enemy Totally', 'leave enemies nothing', 'Michael Corleone', 'you end up alone'),
        ('LAW 33', 'Discover Each Man’s Thumbscrew', 'find their weakness, use it', 'the blackmailer', 'this is coercion')]
def table():
    out = ''.join(box(x, 56, w, 40, 's-box-j', 8) + t(x + w // 2, 82, h, 's-t-b')
                  for x, w, h in [(20, 300, 'THE LAW'), (340, 260, 'AS ADVICE'), (620, 260, 'AS A CHARACTER'), (900, 260, 'THE COST')])
    for r, (n, name, adv, ch, cost) in enumerate(LAWS):
        y = 108 + r * 76
        out += (box(20, y, 300, 64, 's-card', 8) + t(170, y + 26, n, 's-t-b') + t(170, y + 50, name, 's-t-sm') +
                box(340, y, 260, 64, 's-card', 8) + t(470, y + 38, adv, 's-t-sm') +
                box(620, y, 260, 64, 's-card', 8) + t(750, y + 38, ch, 's-t-sm') +
                box(900, y, 260, 64, 's-box-a', 8) + t(1030, y + 38, cost, 's-t-sm'))
    return out
FIG = svg(1180, 450, 'Four of the 48 Laws read three ways: as advice, as a character, and by what they cost',
          t(590, 32, 'FOUR LAWS, READ THREE WAYS', 's-t') + table() +
          t(590, 432, 'Read the laws as character, not conduct. A tactic that wins a scene can lose the story.', 's-t-sm'))

STOP = dict(
    id='7.2', day=43, title='The 48 Laws as story, not science',
    q='The 48 Laws of Power has more than two million copies in print and is banned in many US prisons. Is it a manual for manipulation, or a brilliant book of stories?',
    why='After Cialdini’s lab results comes the other famous book about influence, and it could not be more different. Robert Greene’s The 48 Laws of Power (1998) has no experiments, only history: courtiers, generals, kings and swindlers. For a writer it is one of the best character books ever made, if you read each law as a belief a character holds. For a business owner it is a test: which of these laws would destroy the trust your work depends on?',
    case=dict(k='The case', name='Robert Greene, The 48 Laws of Power (1998)', role='A bestseller of power tactics told through history',
              facts=[('The making', 'Viking, 1998, produced by Joost Elffers'),
                     ('The reach', '“Over 2 million copies in print” (Joost Elffers Books)'),
                     ('Law 1', '“Never Outshine the Master”'),
                     ('The ban', 'PEN America: Greene’s books are banned in 20 state prison systems')],
              stamp=('anti', 'Anti-model: brilliant stories, risky rules')),
    cold=dict(q='Law 33 is “Discover Each Man’s Thumbscrew”. What do you think it tells the reader to do?',
              a='Find each person’s weakness, an insecurity, a need, a secret pleasure, and use it to control them. Read as advice, that is a recipe for coercion. Read as character, it is a perfect villain’s worldview: the blackmailer in a noir, the cult leader who learns your shame in confession, the con artist from File 4 who finds your need. Greene illustrates each law with stories from history, not with studies. That is the key to reading the book well.'),
    video=dict(id='hwqveKLfpfg', title='Robert Greene on Reading, The Laws of Power, and Detecting Lies', who='The Knowledge Project Podcast',
               watch=['How Greene describes his own reasons for writing about power',
                      'Whether he presents the laws as advice, warning or observation',
                      'One idea you would give a character, and one you would never use yourself']),
    story=['Robert Greene’s The 48 Laws of Power was published by Viking in 1998, produced by Joost Elffers. Each law has a short command, a story from history of someone who obeyed it, a story of someone who broke it, and quotations running down the margins. Law 1 is “Never Outshine the Master”. Law 3 is “Conceal Your Intentions”. Law 15 is “Crush Your Enemy Totally”. Its producer reports more than 2 million copies in print, and PEN America reports that Greene’s books are banned in 20 US state prison systems.',
           'Why is it so gripping? Because it reads like a cast list. Each law is a belief a character might hold, shown through someone who lived or died by it: courtiers at Versailles, Chinese generals, Renaissance princes, swindlers and seducers. The stories are vivid and carefully chosen. That is exactly how good storytelling works, and it is exactly how evidence does not work.',
           'Is it science? No, and it does not claim to be. There are no controlled studies, only history picked to fit each law, and history can be found to fit almost any rule. The research that does exist points the other way for the long run. A 2012 meta-analysis led by Ernest O’Boyle, covering 245 samples and nearly 44,000 people, linked higher Machiavellianism to slightly worse job performance and more bad behaviour at work. Manipulation can win a moment. It rarely builds a career.',
           'So how should you read it? As a map of the territory, not a set of orders. Some laws are plain observation: people in power dislike being outshone, and saying less can make you seem stronger. Others, like Laws 15 and 33, describe domination and coercion. The dangerous move is treating a catalogue of tactics as a moral guide. In cults and cons, the book can read like the leader’s private notebook, which is exactly why it helps you recognise one.',
           'For a writer, the book is a character generator. Give a character one law as their core belief and let the plot test it. Michael Corleone in The Godfather Part II lives by “Crush Your Enemy Totally” and ends the film alone. Frank Underwood in House of Cards could be a walking illustration of a dozen laws. The tragedy is built in: the law that wins the midpoint destroys the relationships the character needs in the last act.'],
    fig=(FIG, 'Four of the 48 Laws read three ways. As advice they are risky; as character they are gold.'),
    specs=[('Machiavellianism', 'A personality trait marked by manipulation, cynicism and self-interest, named after Machiavelli.'),
           ('Anecdotal evidence', 'Stories chosen to illustrate a point. Vivid, but they cannot show how often something works.'),
           ('Dark Triad', 'Psychologists’ name for three linked traits: Machiavellianism, narcissism and psychopathy.')],
    tags=[('myth', '“The 48 Laws are proven rules of power.”', 'They are aphorisms illustrated with chosen history, not tested findings.', ('Penguin Random House: The 48 Laws of Power', 'https://www.penguinrandomhouse.com/books/330912/the-48-laws-of-power-by-robert-greene/')),
          ('hold', '“Manipulators do not do better at work in the long run.”', 'A 2012 meta-analysis linked Machiavellianism to slightly worse performance and more misconduct.', ('O’Boyle et al. 2012', 'https://pubmed.ncbi.nlm.nih.gov/22023075/')),
          ('hold', '“The book is banned in some prisons.”', 'PEN America reports Greene’s books are banned in 20 US state prison systems.', ('PEN America: Reading Between the Bars', 'https://pen.org/report/reading-between-the-bars/'))],
    distil=[('Joost Elffers Books: The 48 Laws of Power', 'https://www.joostelffersbooks.com/the-48-laws-of-power', 'The producer’s page and sales figure'),
            ('O’Boyle et al. 2012: the Dark Triad at work', 'https://pubmed.ncbi.nlm.nih.gov/22023075/', 'What manipulation costs'),
            ('PEN America: Reading Between the Bars', 'https://pen.org/report/reading-between-the-bars/', 'The prison bans')],
    writer=dict(notes=['Give a character one law as a core belief and let the plot test it. A law that wins the midpoint should cost them the ending.',
                       'Borrow the book’s structure: Greene shows a person who obeys each law and one who breaks it. That is a ready-made A-plot and B-plot.'],
                drill='Pick one law. Write a one-page fictional scene where a character obeys it perfectly and wins, then a half-page epilogue a year later showing what it cost them.'),
    biz='Run your MTRX™ habits past four laws. “Conceal your intentions” is poison for an agency that lives on trust: say what you will deliver and what you will not. “Always say less than necessary” helps in a negotiation, not in a proposal. “Discover each man’s thumbscrew” becomes “learn each client’s real problem” when you flip it from leverage to service. Read the book to recognise power games, not to play them.',
    tryit='Pick the law you most recognise in someone you have met. Write two lines: how they used it, and what it cost them or others. Self-reflection only.',
    room='Read the laws as character, not as conduct. A tactic that wins a scene can lose the story.',
    deeper=[('Penguin Random House: The 48 Laws of Power', 'https://www.penguinrandomhouse.com/books/330912/the-48-laws-of-power-by-robert-greene/', 'The publisher’s description')],
    nextq='Law 33 is a polite name for something the law now treats as a crime. When does influence inside a relationship become captivity? Stop 7.3.',
    checks=[dict(q='What kind of evidence does Greene use to support each law?',
                 o=['Stories from history chosen to illustrate it',
                    'Controlled experiments with large samples of volunteers',
                    'Surveys of hundreds of business leaders'], a=0,
                 w='Vivid anecdotes, not tests. History can be found to fit almost any rule.'),
            dict(q='What did a 2012 meta-analysis find about Machiavellian employees?',
                 o=['Slightly worse job performance and more bad behaviour at work',
                    'Much faster promotion and noticeably higher pay',
                    'No measurable difference from other employees'], a=0,
                 w='245 samples, nearly 44,000 people. Manipulation can win moments but rarely pays in the long run.'),
            dict(q='How does this course suggest a writer should use the 48 Laws?',
                 o=['As a character’s core belief, tested by the plot',
                    'As a list of tactics the hero should copy',
                    'As a scientific guide to human nature'], a=0,
                 w='A law that wins the midpoint should cost the character something by the end.')],
)

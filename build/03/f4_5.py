from svg import box, t, arrow, line, svg

ST = [('Slippin\' Jimmy', 'Cicero, fake falls'), ('Mailroom', 'going straight'), ('Jimmy McGill', 'Sandpiper'),
      ('Saul Goodman', 'the mask wins'), ('Gene Takovic', 'Omaha, hiding'), ('James McGill', 'the truth, at last')]
FIG = svg(1180, 400, "Jimmy McGill's six names: each identity is a con, and the final scene is the only one that tells the truth",
          t(590, 32, 'SIX NAMES, ONE MAN: THE CON AS SELF-PORTRAIT', 's-t') +
          ''.join(box(16 + i * 194, 70, 178, 120, 's-box-a' if i == 5 else ('s-box-j' if i == 3 else 's-card'), 12) +
                  t(105 + i * 194, 116, n, 's-t-b') + t(105 + i * 194, 150, d, 's-t-sm') for i, (n, d) in enumerate(ST)) +
          ''.join(arrow(194 + i * 194, 130, 210 + i * 194, 130) for i in range(5)) +
          t(590, 240, 'WANT: his brother Chuck\'s respect, and to be taken seriously as a lawyer', 's-t-sm') +
          t(590, 276, 'NEED: to stop treating every relationship as a room he has to win', 's-t-sm') +
          line(80, 312, 1100, 312, True) +
          t(590, 352, 'His talent never changes. What changes is who it serves, and whether he can stop performing.', 's-t-sm'))

STOP = dict(
    id='4.5', day=28, title="Slippin' Jimmy to Saul Goodman",
    q='Better Call Saul shows dozens of cons, many of them funny. Why is it really a tragedy about a man whose best talent keeps winning for the wrong reasons?',
    why="Most con films are about the con. Better Call Saul is about the con artist: what the talent costs him, the brother who cannot forgive it, and the woman who loves it a little too much. For No. 08 it is the best long-form study of character want versus need you will find. For MTRX\u2122 it is a warning about the shortcut that works today and costs you tomorrow.",
    case=dict(k='The series', name='Better Call Saul (2015 to 2022)', role='AMC, created by Vince Gilligan and Peter Gould; Bob Odenkirk as Jimmy McGill',
              facts=[('Run', '6 seasons, 63 episodes, 8 February 2015 to 15 August 2022'),
                     ('Brother', 'Chuck McGill (Michael McKean), a brilliant lawyer who never forgives Slippin\' Jimmy'),
                     ('Partner', 'Kim Wexler (Rhea Seehorn), who enjoys the cons as much as he does'),
                     ('Emmys', '53 nominations over six seasons, and not a single win')],
              stamp=('field', 'Field test: watch Season 1')),
    cold=dict(q='In Season 1 Jimmy builds a genuine case for elderly residents who were being overbilled. His brother Chuck secretly blocks him from it. Guess Chuck\'s reason.',
              a="Chuck believes Jimmy cannot change. In the episode Pimento (aired 30 March 2015) he finally says it: \"Slippin' Jimmy with a law degree is like a chimp with a machine gun!\" The twist is that Chuck uses lies and sabotage to stop a brother he thinks is a liar. The New York Times recap put it neatly: Chuck demonstrated the very flaws he bemoans in his younger brother. That is the engine of the whole show."),
    video=dict(id='MLnVqBi8LmU', title='Better Call Saul: Ranking Every Jimmy McGill Scam', who='Slip Maker \u00b7 2020',
               watch=['Which scams are short cons and which are big cons, in Maurer\'s terms',
                      'How many scams depend on Jimmy reading what the mark wants',
                      'The point where the scams stop being funny']),
    story=["Jimmy McGill grew up in Cicero, Illinois, as Slippin' Jimmy, a small-time grifter who faked falls on icy pavements for compensation. His older brother Chuck, a partner at a respected law firm, bailed him out of a bad scrape, and Jimmy moved to Albuquerque, worked in the firm's mailroom and secretly earned a law degree by correspondence. The series asks one question for 63 episodes: can a man with a con artist's gifts do honest work, and does anyone around him want him to?",
           "The early cons are comic and precise, and they map straight onto Maurer. Jimmy picks a mark by his want, plays a role, stages a convincer and gets out before the fix is needed. But even in Season 1 the show plants the cost. When he tracks down the Kettlemans, a couple who faked their own kidnapping amid accusations over county money, he cannot turn the leverage into an honest retainer. When he uncovers the Sandpiper case, a real injustice where elderly residents are overbilled, his methods (recruiting clients through stunts, cutting corners) keep contaminating a good cause. Lawyers who reviewed the show praised its texture, the paperwork, small-practice poverty and courthouse bargaining, while flagging stunts no real lawyer could get away with.",
           "Screenwriters talk about want versus need. Jimmy wants Chuck's respect and to be taken seriously as a lawyer. He needs to stop treating every relationship as a room he has to win. Every time he chooses the clever shortcut, he gets what he wants for a day and moves further from what he needs. Kim Wexler is the show's masterstroke: a disciplined lawyer who loves the thrill of the con with him, which makes her both his best partner and his most dangerous enabler.",
           "Saul Goodman, the loud lawyer from Breaking Bad, is the last mask: a character Jimmy builds to sell himself, which slowly becomes the person. The show's final chapters, shot in black and white, follow him hiding in Omaha as Gene Takovic, managing a mall cinnamon-roll shop and relapsing into cons. Then the finale, Saul Gone (2022), stages one more con. He talks prosecutors down to a deal of about seven years by playing Walter White's victim. And then, in front of Kim, he throws it away, confesses everything and corrects the court: \"The name's McGill.\" He is sentenced to 86 years.",
           "Read that ending in this guide's terms. Every earlier identity was a con about who he was. The last performance is the only one that tells the truth, and it costs him everything a con usually wins. That is why the show is a tragedy with a moral ending: the talent was never the problem. The problem was what he used it for, and whether he could stop performing for long enough to be seen."],
    fig=(FIG, "Jimmy McGill's six names. The cons change; the talent does not. The last one is the only honest performance."),
    specs=[('Want versus need', 'What a character pursues (respect, money) versus what would actually heal them (honesty, connection).'),
           ('Enabler', 'A character who rewards the protagonist\'s flaw because they enjoy it too. Kim Wexler.'),
           ('Mask that becomes the face', 'A role played to win something, which slowly replaces the self.')],
    tags=[('part', '"Jimmy is just a criminal lawyer."', 'A licensed lawyer whose cons become ethical and criminal misconduct over time.', ('Above the Law review', 'https://abovethelaw.com/2015/03/standard-of-review-better-call-saul-is-better-than-most-in-depicting-life-as-a-lawyer/')),
          ('hold', '"The show gets small-practice texture right."', 'Legal critics praised its paperwork, poverty and bargaining.', ('Current Affairs, 2015', 'https://www.currentaffairs.org/news/2015/12/tvs-only-accurate-law-show')),
          ('myth', '"Real lawyers could use Jimmy\'s courtroom tricks."', 'Critics list them as unethical or implausible.', ('Looper, lawyers on the show', 'https://www.looper.com/280307/things-on-better-call-saul-that-real-lawyers-would-never-do/')),
          ('hold', '"He ends with an 86-year sentence."', 'He confesses and rejects a deal of about seven years.', ('Variety, 2022', 'https://variety.com/2022/tv/news/better-call-saul-peter-gould-interview-ending-finale-1235341919/'))],
    distil=[('NYT recap of Pimento: A Chimp With a Machine Gun', 'https://archive.nytimes.com/artsbeat.blogs.nytimes.com/2015/03/30/better-call-saul-recap-pimento/', 'The brother who becomes what he hates'),
            ('Peter Gould on the finale (Variety)', 'https://variety.com/2022/tv/news/better-call-saul-peter-gould-interview-ending-finale-1235341919/', 'Why Jimmy confesses'),
            ('Foster PC on the Sandpiper RICO case', 'https://www.fosterpc.com/blog/when-it-comes-to-rico-better-not-call-saul-an-admiring-tongue-in-cheek-critique-of-season-one-episode-eight/', 'A lawyer reads the overbilling plot')],
    writer=dict(notes=["Let a good cause tempt a bad method. Sandpiper works because Jimmy is right about the injustice and wrong about how to fight it. An audience will forgive a character almost anything except being boring, and will grieve for one whose virtues and flaws are the same trait.",
                       "Give the con artist a witness who refuses to be charmed. Chuck is that witness. Every scene between them is a con that does not work, which tells us more about Jimmy than any con that does."],
                drill="Write a fictional client meeting where Jimmy could tell the truth and win slowly. Then give him one funny shortcut that wins today and costs him tomorrow. Let the reader see the cost before he does."),
    biz="Slippin' Jimmy risks are real in a small agency: inflating a case study, a fake testimonial, quietly expanding scope to justify a bigger invoice, or a clever growth hack that a client later discovers. Each wins today and costs trust. MTRX\u2122 rule: only truthful case studies with written client approval, and every change of scope in writing before the work starts.",
    tryit="Write down your own Slippin' Jimmy talent: the skill that wins rooms for you (talking, design speed, reading people). Then write one time it won for the wrong reason, and one rule that keeps it pointed at the right one.",
    room='The con becomes a tragedy when it works for the wrong reason.',
    deeper=[('Why scams work: the Better Call Saul coin scam', 'https://www.youtube.com/watch?v=J0qouBLaCXg', 'One short con, broken down beat by beat'),
            ('Extended trailer: Better Call Saul', 'https://www.youtube.com/watch?v=l1xIGfVFb-U', 'How AMC sold the show in 2015')],
    nextq='Jimmy\'s finale works because the audience had every fact. How do the great con films hide a twist in plain sight without cheating? Stop 4.6 is the boss fight.',
    checks=[dict(q='Why does Chuck secretly block Jimmy from the Sandpiper case?',
                 o=['He believes Slippin\' Jimmy can never change',
                    'He thinks the overbilling case has no legal merit',
                    'He wants Kim Wexler to lead the case instead'], a=0,
                 w='"Slippin\' Jimmy with a law degree is like a chimp with a machine gun." Chuck uses deceit to stop a man he calls deceitful.'),
            dict(q='Which best describes Jimmy\'s want versus his need?',
                 o=['Want: respect as a lawyer. Need: to stop performing to win every room',
                    'Want: to quit law. Need: to earn far more money',
                    'Want: to be left alone. Need: to become famous'], a=0,
                 w='Every clever shortcut gets him the want for a day and moves him further from the need.'),
            dict(q='What happens in the finale, Saul Gone?',
                 o=['He rejects a deal of about seven years, confesses, and gets 86',
                    'He wins the case and returns to practise law in Albuquerque',
                    'He escapes to Omaha and is never caught'], a=0,
                 w='The last performance is the truth. "The name\'s McGill." It costs him everything a con usually wins.')],
)

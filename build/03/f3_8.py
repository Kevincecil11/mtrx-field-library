from svg import box, t, arrow, line, svg

SPEC = ['Fandom', 'Brand tribe', 'Wellness circle', 'MLM team', 'High-demand', 'Coercive group']
QS = [('1', 'Disagree out loud?'), ('2', 'Leave and keep friends?'), ('3', 'Know where money goes?'),
      ('4', 'Outside sources OK?'), ('5', 'Doubt is not a flaw?')]
FIG = svg(1180, 400, 'The cultish spectrum and five questions that place any group on it',
          t(590, 32, 'INTENSITY IS NOT THE TEST. CONTROL IS.', 's-t') +
          ''.join(box(20 + i * 192, 52, 178, 76, 's-box-a' if i >= 4 else ('s-box-j' if i in (2, 3) else 's-card'), 10) +
                  t(109 + i * 192, 98, s, 's-t-b') for i, s in enumerate(SPEC)) +
          arrow(30, 150, 1150, 150, True) + t(30, 178, 'free to leave, free to argue', 's-t-sm', 'start') + t(1150, 178, 'leaving and arguing cost you', 's-t-sm', 'end') +
          t(590, 228, 'FIVE QUESTIONS THAT PLACE ANY GROUP', 's-t') +
          ''.join(box(20 + i * 230, 248, 216, 110, 's-card') + t(128 + i * 230, 290, n, 's-t-d') + t(128 + i * 230, 332, q, 's-t-sm')
                  for i, (n, q) in enumerate(QS)) +
          t(590, 390, 'Each "no" moves a group to the right. A run of noes is the warning sign, whatever the brand looks like.', 's-t-sm'))

STOP = dict(
    id='3.8', day=22, title='Cultish: online groups, wellness, MLMs and startups',
    q='If cults work through belonging, ritual and a special language, how much of ordinary life is cultish, and where is the line?',
    why="You will never live in a compound. You already live inside dozens of groups that borrow cult tools: fan communities, fitness brands, founder-led startups, wellness influencers, multi-level marketing teams and online movements. Most are fine. A few are not. This stop gives you a calm way to tell them apart, without calling everything you dislike a cult.",
    case=dict(k='Case file', name='QAnon and conspirituality', role='An online movement born in October 2017, and the wellness world it travelled through',
              facts=[('Began', 'October 2017: anonymous posts on 4chan by "Q", claiming to be a government insider'),
                     ('Spread', 'From fringe boards to mainstream platforms, then into yoga, wellness and spiritual spaces'),
                     ('Ended?', 'Q\'s posts stopped in December 2020; the movement did not stop with them'),
                     ('The word', 'Conspirituality: a blend of conspiracy theory and New Age spirituality, named by Ward and Voas in 2011')],
              stamp=('part', 'Partly: cultish, not a classic cult')),
    cold=dict(q='Researchers who traced how QAnon reached ordinary people found some surprising entry points. Guess one of the places it spread through, other than politics.',
              a="Wellness and spirituality: yoga studios, healers, alternative-health influencers and psychic communities. A 2023 study by Conner traced how QAnon ideas travelled through these spaces, wrapped in the language of awakening, intuition and protecting children. That is the conspirituality pattern. It shows the modern shape of cultish influence: no compound, no single leader in a robe, just a feed, a vocabulary and a community that rewards certainty."),
    video=dict(id='_RqNe5IrpP8', title='How online conspiracy groups compare to cults', who='WIRED',
               watch=['Which classic cult features show up online, and which do not',
                      'How a feed can do the work of a compound',
                      'Why an online movement can outlive its anonymous leader']),
    story=["The linguist Amanda Montell's book Cultish: The Language of Fanaticism (2021) makes a simple point: cult language is everywhere. Insider jargon, us-versus-them labels, special names for outsiders and thought-terminating clich\u00e9s (Lifton's phrase from stop 1.3, a slogan that ends a conversation) run through boutique fitness brands, MLM teams, startup all-hands and influencer comment sections. Language is how a group draws its circle. Most circles are harmless. The question is what the circle costs the people inside it.",
           "Online movements change the shape. A phone can carry the whole milieu: the doctrine, the rituals (daily drops, live streams, decoding sessions), the community, the surveillance and the punishment. Algorithms reward certainty and outrage. An anonymous leader can claim insider knowledge nobody can check. And unlike a compound, there is no single door to walk out of. Scholars who studied QAnon argue about whether to call it a new religious movement, a conspiracy movement, a political movement or something like an MLM of ideas, and warn that cult can become a weapon rather than an analysis. The useful lens is the same one as always: power, harm and exit.",
           "Multi-level marketing is the most common cultish structure an ordinary person meets. Recruiters sell an opportunity, a family, a self-improvement journey and a lifestyle, with ranks named diamond and president. The numbers tell a plainer story. In a September 2024 staff report, the US Federal Trade Commission reviewed 70 MLM income disclosure statements and found that many participants received no payments at all, and the vast majority received $1,000 or less a year, under $84 a month, before expenses. AARP found that 7.7% of US adults had joined at least one MLM. Doubts are often reframed as a mindset problem, and leaving can cost the friendships that recruited you.",
           "Startups and wellness brands borrow the toolkit for honest reasons. A shared mission, rituals, a charismatic founder and long hours together really do make teams work harder, which is Durkheim's effervescence from stop 3.1. The trouble starts when the founder becomes the only interpreter of truth, criticism is reframed as disloyalty or negativity, and buying more (courses, retreats, equipment, equity) is treated as proof of commitment. Theranos, which you will meet in stop 6.3, was a company whose culture punished questions about the science.",
           "So where is the line? Not intensity. Intense fans, devoted runners and passionate founders are not a cult. The line is control. This guide boils the research of Lifton, Lalich and the coercive control literature into five plain questions, drawn in the diagram. Can you disagree out loud without punishment? Can you leave and keep your friends? Do you know where the money goes? Are outside sources welcome? Are doubts treated as information rather than as your personal flaw? A group that passes all five is a community. A group that fails most of them is cultish, whatever its branding.",
           "Notice what this does for you. It lets you enjoy belonging, which File 1 showed is a real human need, without losing the right to check. And it gives you a calmer vocabulary than cult for most of what you will meet. Cultish is a useful adjective for a style. Cult, in the strong sense, is a claim about power and harm that needs evidence."],
    fig=(FIG, 'The cultish spectrum. Intensity can sit anywhere on it; the five questions decide where a group actually lands.'),
    specs=[('Cultish', 'Montell\'s term for groups that use cult-like language and rituals without necessarily being coercive.'),
           ('Thought-terminating cliche', 'Lifton: a stock phrase that ends thinking. "Trust the plan." "Haters gonna hate." "That is just your fear."'),
           ('Conspirituality', 'Ward and Voas (2011): the blend of conspiracy theory and New Age spirituality.'),
           ('Income disclosure statement', 'An MLM\'s published earnings figures. The FTC found most hide the many who earn little or nothing.')],
    tags=[('hold', '"Most MLM participants make little or nothing."', 'The FTC\'s 2024 review: most received $1,000 or less a year, before expenses.', ('FTC staff report, Sept 2024', 'https://www.ftc.gov/system/files/ftc_gov/pdf/mlm-ids-report.pdf')),
          ('myth', '"An online group cannot be cultic; nobody lives together."', 'Information, time, money and identity can all be controlled through a feed.', ('Conner 2023', 'https://doi.org/10.3389/fsoc.2023.1136333')),
          ('part', '"QAnon is a religion."', 'Scholars compare it across religious, conspiracy, political and MLM-like categories.', ('Amarasingam et al.', 'https://doi.org/10.1017/9781009052061.022')),
          ('myth', '"Every intense fandom is a cult."', 'Intensity is not control. The test is power, harm and the cost of leaving.', ('Montell, Cultish (2021)', 'https://www.harpercollins.com/products/cultish-amanda-montell'))],
    distil=[('Montell, Cultish: The Language of Fanaticism (2021)', 'https://www.harpercollins.com/products/cultish-amanda-montell', 'Cult language in fitness, MLMs and startups'),
            ('FTC staff report on MLM income disclosures (2024)', 'https://www.ftc.gov/system/files/ftc_gov/pdf/mlm-ids-report.pdf', 'What 70 MLMs reveal in the fine print'),
            ('Conner, QAnon and alternative spirituality (2023)', 'https://doi.org/10.3389/fsoc.2023.1136333', 'How the movement travelled through wellness'),
            ('Amarasingam et al., Categorizing QAnon', 'https://doi.org/10.1017/9781009052061.022', 'Religion, conspiracy, movement or MLM?')],
    writer=dict(notes=["The modern cult story does not need a compound. It needs a phone screen. Show the feed as the ritual: the notification sound, the late-night scroll, the in-jokes, the dopamine of being right together. The isolation is quiet. She is sitting at the family dinner, physically present, living somewhere else.",
                       "MLM is one of the richest untapped settings for drama, because the recruiter is usually a victim too. Every rank above her is a person she trusts. Write the scene where she pitches her best friend, believing every word, and the audience knows the numbers."],
                drill="Write a fictional family dinner where one character has been deep in an online movement for six months. Nobody mentions it until the last line. Show the distance only through what she notices, says and checks on her phone."),
    biz="This is the most practical stop for MTRX\u2122. You will be pitched by cultish programmes (coaching circles, agency-growth masterminds, course funnels) and you will be tempted to build a cultish brand. Run the five questions both ways. Can a client disagree with you without being made to feel stupid? Can they leave cleanly and still recommend you? If yes, you are building a community, not a funnel.",
    tryit="Pick one group you belong to online or offline: a community, a brand, a team, a course. Run the five questions honestly. Score each yes as 1. Then do the same for one group you are suspicious of. Write one sentence on what the scores showed that your gut had not.",
    room='Intensity is not the test. Ask whether people can disagree, leave and follow the money without paying for it.',
    deeper=[('How to spot a pyramid scheme, Stacie Bosley (TED-Ed)', 'https://www.youtube.com/watch?v=SBGfHk91Vrk', 'The maths of recruitment-based income in five minutes'),
            ('Building your pyramid, Knowing Better', 'https://www.youtube.com/watch?v=LhHhZ3b9akU', 'A long, fair look at how MLMs work in practice')],
    nextq='You have the sociology. Now the art: how have the best films put all this on screen, and what did they get right that the headlines missed? Stop 3.9 is the boss fight.',
    checks=[dict(q='What did the FTC\'s 2024 review of 70 MLM income disclosures find?',
                 o=['Most participants received $1,000 or less a year, before expenses',
                    'Most participants earned a full-time wage within their first year',
                    'Income figures were clear, complete and included all expenses'], a=0,
                 w='Many received nothing. The statements tended to hide the low earners and ignore costs.'),
            dict(q='What is the best test for whether a group is cultish in a harmful way?',
                 o=['Whether people can disagree, leave and see the money without cost',
                    'Whether members are very enthusiastic and talk about it constantly',
                    'Whether the group has a logo, a slogan and a charismatic founder'], a=0,
                 w='Intensity and branding are everywhere. Control over exit, money and dissent is the line.'),
            dict(q='What does conspirituality describe?',
                 o=['A blend of conspiracy theory and New Age spirituality',
                    'A scholarly method for studying secret religious groups',
                    'A rule that bans spiritual leaders from running for office'], a=0,
                 w='Ward and Voas named it in 2011. QAnon travelled through these spaces.')],
)

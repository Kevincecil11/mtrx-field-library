from svg import box, t, arrow, line, svg

FIG = svg(1180, 400, 'How the Eiffel Tower con turned four pressures into one payment, with the fake bribe as the convincer',
          t(590, 34, 'FOUR PRESSURES, ONE PAYMENT', 's-t') +
          box(30, 64, 250, 110, 's-card') + t(155, 104, 'STATUS', 's-t-b') + t(155, 138, 'a ministry invitation', 's-t-sm') +
          box(320, 64, 250, 110, 's-card') + t(445, 104, 'SECRECY', 's-t-b') + t(445, 138, '"tell no one"', 's-t-sm') +
          box(610, 64, 250, 110, 's-card') + t(735, 104, 'COMPETITION', 's-t-b') + t(735, 138, 'rival dealers bidding', 's-t-sm') +
          box(900, 64, 250, 110, 's-card') + t(1025, 104, 'PROFIT', 's-t-b') + t(1025, 138, 'tonnes of scrap iron', 's-t-sm') +
          ''.join(arrow(155 + k * 290, 176, 590, 226) for k in range(4)) +
          box(400, 228, 380, 86, 's-box-a') + t(590, 264, 'THE "BRIBE" = THE CONVINCER', 's-t-b') + t(590, 292, 'corruption feels real', 's-t-sm') +
          arrow(590, 316, 590, 346, True) +
          t(590, 374, 'Payment made. Then shame becomes the fix: a buyer who thought he paid a bribe does not call the police.', 's-t-sm'))

STOP = dict(
    id='4.2', day=25, title='The man who sold the Eiffel Tower: Victor Lustig',
    q='How do you sell a 300-metre iron tower that everyone in Paris can see, and why did the buyer never go to the police?',
    why="This is the most famous con in history, and it is famous for a reason: it uses every step from stop 4.1 in a single week, with a twist a screenwriter would kill for. The sale was impossible. The buyer believed it because the con artist made him think he was the one doing something crooked. Learn this case and you understand why shame is a con artist's best accomplice.",
    case=dict(k='Con artist', name='Victor Lustig, "the Count"', role='Claimed to be born in Bohemia in 1890; used 47 aliases, and even his birth record has never been found',
              facts=[('The con', 'Paris, 1925: posed as a government official selling the Eiffel Tower for scrap'),
                     ('The room', 'The Hotel de Crillon, with forged government stationery'),
                     ('The mark', 'Andre Poisson, a scrap-metal dealer who wanted status'),
                     ('The end', 'Arrested in New York in 1935 over counterfeit money; died in federal custody in 1947')],
              stamp=('part', 'Partly: "sold it twice" is overstated')),
    cold=dict(q='After Poisson paid, Lustig asked for one more thing, and that request is what made the con work. Guess what it was.',
              a="A bribe. In the classic retelling, playing a junior official complaining about his low pay, Lustig hinted that he needed a little extra to make sure Poisson won the contract. A real swindler, Poisson reasoned, would never ask for a bribe; a corrupt bureaucrat would. The bribe made the official feel real. And when Poisson realised he had been robbed, reporting it meant admitting he had tried to bribe a government official. Shame did the cover-up for free."),
    video=dict(id='9gG-aEfkSQ0', title='Meet the man who sold the Eiffel Tower...twice', who='Smithsonian Magazine',
               watch=['Why the tower being expensive to maintain made the lie believable',
                      'How a fake official makes a whole room feel real',
                      'Whether the second sale really happened, or only the attempt']),
    story=["The lie worked because it grew out of a real argument. The Eiffel Tower was built for the 1889 World's Fair and was never meant to be permanent. By the 1920s it needed costly maintenance, and Parisians had argued about its future for years. The official Eiffel Tower history notes that its use as a radio transmitter helped save it. So when a man claiming to be a senior official told scrap dealers that the government had quietly decided to dismantle it, the story fitted something they had already read in the papers.",
           "Lustig built the store from paper and furniture. He rented rooms at the Hotel de Crillon, one of the grandest hotels in Paris, used forged government stationery, and wrote to leading scrap dealers inviting them to a confidential meeting. According to Smithsonian, he blamed \"engineering faults, costly repairs, and political problems I cannot discuss\" and said the tower would go to the highest bidder. Secrecy explained everything strange: this was politically sensitive, so tell no one. Competition did the rest. Each dealer wanted to win, which meant none of them wanted to ask awkward questions.",
           "He picked Andre Poisson, and retellings agree on why: Poisson was not the grandest dealer, he was the one most eager to be taken seriously by the Paris business elite. That is Maurer's put-up: choose the mark by his want, not his wallet. Then came the bribe, the convincer of the whole operation. It made the official feel human and corrupt, which felt more real than honest. Poisson paid for the contract and for the favour.",
           "Lustig left for Austria with the money. The blow-off and the fix were done by Poisson himself: according to the official Eiffel Tower account, he realised the fraud after paying and was too embarrassed to press charges. Lustig later came back and tried the same scheme again. The tower's own history says that attempt failed. So sold it twice is a better headline than fact: one completed sale, one failed attempt. Even the amount Poisson paid is reported inconsistently, so this guide does not repeat a figure.",
           "His end was less elegant. Lustig moved into counterfeiting in America. Secret Service agents arrested him in New York in May 1935, and a Library of Congress press photo records about $52,000 in fake bills found in a Times Square subway locker. On 1 September he escaped from the federal detention centre on a rope of bed sheets, pretending to be a window cleaner when people pointed. He was caught in Pittsburgh four weeks later, sentenced to 20 years, sent to Alcatraz, and died of pneumonia in the prison medical centre at Springfield, Missouri, on 11 March 1947. His death certificate gave his occupation as apprentice salesman. The Ten Commandments for Con Men often credited to him (be a patient listener, never look bored, never boast) circulate without a verified signed source, so read them as legend, not as his words."],
    fig=(FIG, 'The Eiffel Tower con. Four ordinary business pressures, one fake bribe, and a buyer whose shame became the cover-up.'),
    specs=[('Put-up by want', 'Choosing a mark for what he wants (status, belonging) rather than for how much he has.'),
           ('Complicity trap', 'Making the mark do something slightly wrong, so reporting the con means confessing.'),
           ('Borrowed truth', 'A lie that grows from a real, public debate, so it feels like news rather than invention.')],
    tags=[('part', '"Lustig sold the Eiffel Tower twice."', 'One completed sale to Poisson; the second attempt failed.', ('Eiffel Tower official history', 'https://www.toureiffel.paris/en/news/history-and-culture/who-sold-eiffel-tower')),
          ('hold', '"The meeting was at the Hotel de Crillon."', 'Smithsonian\'s reconstruction places it there in 1925 with forged stationery.', ('Smithsonian, 2016', 'https://www.smithsonianmag.com/history/man-who-sold-eiffel-tower-twice-180958370/')),
          ('myth', '"Poisson went straight to the police."', 'Embarrassment and apparent complicity kept him quiet.', ('Eiffel Tower official history', 'https://www.toureiffel.paris/en/news/history-and-culture/who-sold-eiffel-tower')),
          ('part', '"Lustig wrote the Ten Commandments for Con Men."', 'Widely attributed, but no verified signed source. Treat as folklore.', ('Smithsonian, 2016', 'https://www.smithsonianmag.com/history/man-who-sold-eiffel-tower-twice-180958370/'))],
    distil=[('Who sold the Eiffel Tower? (official history)', 'https://www.toureiffel.paris/en/news/history-and-culture/who-sold-eiffel-tower', 'The tower\'s own account of the con'),
            ('Smithsonian: The Man Who Sold the Eiffel Tower. Twice.', 'https://www.smithsonianmag.com/history/man-who-sold-eiffel-tower-twice-180958370/', 'The reconstruction of 1925'),
            ('Smithsonian: The Smoothest Con Man That Ever Lived', 'https://www.smithsonianmag.com/history/the-smoothest-con-man-that-ever-lived-29861908/', 'Counterfeiting, escape and capture'),
            ('Library of Congress press photo, 1935', 'https://www.loc.gov/item/2015650694/', 'The arrest and the subway locker')],
    writer=dict(notes=["The bribe is the scene. Write it as the moment the con artist seems to lose control, embarrassed, asking for a favour. The audience should feel the mark relax at exactly the moment he should panic. That reversal of power, where the predator plays weak, is one of the most reusable beats in the genre.",
                       "Poisson is the more interesting character. He is not greedy so much as hungry to belong. Give your mark a want the audience recognises in themselves, and the con becomes a tragedy instead of a joke."],
                drill="Stage a fictional silence that follows the word confidential. Write it three ways: the listener is afraid, the listener is greedy, the listener is professionally cautious. Fiction only. Change nothing but his next action."),
    biz="Any client or partner who says a deal needs a secret fee, a cash facilitation payment or a quiet favour is building a complicity trap, even if they do not know the term. MTRX\u2122 rule: every payment goes through the company account, against a tax invoice, with written authority. If it cannot be written down, it does not happen.",
    tryit="Think of one time you hesitated to report or admit a mistake because it would make you look foolish. Write three sentences: what you were protecting, who benefited from your silence, and what a rule written in advance would have made you do.",
    room='The bribe is not extra plot. It is the mark\'s exit from embarrassment, and the con man\'s insurance.',
    deeper=[('El Pais: the man who sold the Eiffel Tower twice (2024)', 'https://english.elpais.com/international/2024-10-22/the-incredible-story-of-the-man-who-sold-the-eiffel-tower-twice.html', 'A modern retelling that flags what is uncertain')],
    nextq='Lustig picked an insecure man. But clever, careful people fall too, including doctors, lawyers and engineers. If not stupidity, what is it? Stop 4.3.',
    checks=[dict(q='Why did the Eiffel Tower story feel believable to the scrap dealers?',
                 o=['The tower\'s costly upkeep and future were already publicly debated',
                    'The French government had announced a real public auction',
                    'Gustave Eiffel personally wrote to the dealers in 1925'], a=0,
                 w='Borrowed truth. The lie grew out of a real argument, so it felt like inside news.'),
            dict(q='What did the "bribe" do for the con?',
                 o=['Made the official feel real, and made reporting it shameful',
                    'Covered Lustig\'s hotel bill at the Hotel de Crillon',
                    'Proved to the police that the sale had been legal'], a=0,
                 w='It worked as the convincer and the fix at once: real-seeming corruption, then a silent victim.'),
            dict(q='How accurate is the headline that Lustig "sold it twice"?',
                 o=['Partly: one sale succeeded and a later attempt failed',
                    'Fully accurate: two buyers paid in full for the tower',
                    'False: Lustig never went to Paris at all'], a=0,
                 w='The tower\'s own history records one completed sale and a failed second attempt.')],
)

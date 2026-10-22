from svg import box, t, arrow, line, svg

ATK = [('PRETEXT', 'a believable role'), ('PRESSURE', 'urgency or authority'), ('THE ASK', 'reset, access, payment'), ('THE BYPASS', 'a person skips a check')]
DEF = [('CALL BACK', 'on a number you hold'), ('SLOW DOWN', 'urgency is a signal'), ('NAMED ACCESS', 'who may approve what'), ('REPORT', 'no blame for asking')]
def row(items, y, cls):
    return ''.join(box(20 + i * 290, y, 270, 96, cls, 12) + t(155 + i * 290, y + 40, n, 's-t-b') +
                   t(155 + i * 290, y + 72, d, 's-t-sm') for i, (n, d) in enumerate(items))
FIG = svg(1180, 420, 'How a social engineering attack moves, and the four habits that break each step',
          t(590, 32, 'THE CON INSIDE THE HACK, AND HOW TO BREAK IT', 's-t') +
          row(ATK, 56, 's-card') + ''.join(arrow(290 + i * 290, 104, 310 + i * 290, 104) for i in range(3)) +
          ''.join(arrow(155 + i * 290, 160, 155 + i * 290, 224) for i in range(4)) +
          row(DEF, 228, 's-box-a') +
          line(80, 352, 1100, 352, True) +
          t(590, 388, 'The attacker needs one person to skip one check. Defence is a habit, not a gadget.', 's-t-sm'))

STOP = dict(
    id='5.6', day=35, title='Social engineering: the con inside the heist',
    q='In 2023 a casino giant reportedly lost around $100 million after a phone call to its own help desk. How do you hack a company by talking?',
    why="Every con in this file, from Ripley to Hatton Garden, needed someone to get past a person. Social engineering is the modern name for that skill, and it is how most breaches start. For a writer it is the most realistic heist scene you can put on screen. For a business owner it is the risk you can actually reduce, because the fix is habits, not money.",
    case=dict(k='The case', name='MGM Resorts, September 2023', role='A cyberattack on the Las Vegas casino and hotel group',
              facts=[('The entry', 'Attackers reportedly called the IT help desk posing as an employee'),
                     ('The group', 'Reported as Scattered Spider'),
                     ('The cost', 'MGM expected a roughly $100m hit to its third quarter (Reuters)'),
                     ('The wider picture', 'Verizon: 68% of 2024 breaches involved a non-malicious human element')],
              stamp=('hold', 'Holds: people are the entry point')),
    cold=dict(q='Why would a help desk agent, whose job includes security, help an attacker?',
              a="Because the agent is measured on something else too: speed. As one security expert told NBC News, help desks \"have metrics on being able to resolve an incident quickly\". The attacker sounds like a stressed colleague with a real problem, and the agent is rewarded for solving problems fast. That is the con from stop 4.1 in a new costume: a believable role, a little pressure, and a person who wants to be helpful."),
    video=dict(id='yIG4kTJTZuY', title='Watch a CNN reporter get hacked', who='CNN Business',
               watch=['How the ethical hacker, Rachel Tobac, builds a believable role before asking for anything',
                      'Which piece of public information makes the role convincing',
                      'The one check that would have stopped it']),
    story=["Kevin Mitnick, once the most famous hacker in the United States, spent his later career teaching companies to defend themselves, and his book The Art of Deception (2002) made one point famous: the easiest way into a system is often a person who wants to help. Social engineering is the con applied to an organisation. It is Maurer's big con from stop 4.1 compressed into a single phone call or email.",
           "The pattern has four steps, shown in the diagram. A pretext: a believable role, such as a new employee, a supplier or a manager. Pressure: urgency, authority or sympathy, so the target acts before thinking. The ask: a password reset, a code, a payment, a door held open. And the bypass: one person skips one check because the story felt real. This is the con's put-up, tale, convincer and touch in modern clothes, and it is why Verizon's 2024 report found a non-malicious human element in 68% of breaches.",
           "MGM Resorts, September 2023, is the case study. Reports say the attackers called the company's IT help desk pretending to be an employee and got access that led to a wide outage of systems across its casinos and hotels. MGM told investors it expected a roughly $100 million hit to its third quarter. Nothing in that story needed a genius programmer. It needed a plausible voice and a process that rewarded speed over verification.",
           "Defence follows the same four steps, and none of it costs much. Call back on a number you already hold, never the one the caller gives you. Treat urgency as a warning sign: real emergencies survive a two-minute check. Write down who is allowed to approve what, so no voice alone can reset an account or move money. And make it safe to report, so a person who pauses to check is praised, not blamed. The attacker needs one person to skip one check. The defence is making the check a habit.",
           "For a writer, this is the most realistic heist scene available. A character talking past a receptionist, a guard or a help desk is more believable than any laser grid, because audiences have all been that helpful person. The best versions, from Catch Me If You Can to Lupin, play it as character: the con works because of who the target is, not because of a gadget."],
    fig=(FIG, 'Social engineering in four steps, and the four habits that break them. One skipped check is enough for the attacker.'),
    specs=[('Social engineering', 'Manipulating people into giving access, information or money, instead of attacking the technology.'),
           ('Pretext', 'The false role and story the attacker uses to make the request seem normal.'),
           ('Call-back verification', 'Ending the call and ringing the person back on a number you already hold.')],
    tags=[('hold', '"Most breaches involve a human element."', 'Verizon\'s 2024 report: a non-malicious human element in 68% of breaches.', ('Verizon DBIR 2024', 'https://www.verizon.com/about/news/2024-data-breach-investigations-report-vulnerability-exploitation-boom')),
          ('myth', '"Hacking is mostly genius code."', 'MGM was reportedly breached through a help desk call, not an exotic exploit.', ('NBC News on the MGM attack', 'https://www.nbcnews.com/tech/security/mgm-las-vegas-hackers-scattered-spider-rcna105238')),
          ('part', '"Training stops social engineering."', 'Training helps, but process matters more: call-backs and named approvals remove the judgement call.', ('Mitnick Security on social engineering', 'https://www.mitnicksecurity.com/blog/social-engineering'))],
    distil=[('Reuters: MGM expects cyberattack to hit quarter', 'https://www.reuters.com/business/mgm-expects-cybersecurity-issue-negatively-impact-third-quarter-earnings-2023-10-05/', 'The cost of one call'),
            ('Verizon DBIR 2024 summary', 'https://www.verizon.com/about/news/2024-data-breach-investigations-report-vulnerability-exploitation-boom', 'The 68% figure'),
            ('Mitnick Security: social engineering', 'https://www.mitnicksecurity.com/blog/social-engineering', 'A defender\'s overview')],
    writer=dict(notes=["Write the social engineering scene from the target's side. The tension is not whether the lie is clever but whether this tired, kind, busy person will make the check. That is a character choice, and it makes the scene human.",
                       "Plant the process early. If the audience has seen the receptionist's rule in act one, the moment she breaks it in act two lands as a turn, not a coincidence."],
                drill="Write a one-page fictional scene in which a character tries to talk past a front desk, and the person on the desk makes the check. The scene should be about the desk person, not the trick."),
    drill=dict(name='Boss fight: the masks audit', mins='25 min',
               steps=['Pick one con or heist from File 5 (Ripley, Delvey, Lupin, Ocean\'s, Antwerp, Hatton Garden, the Louvre or MGM).',
                      'Name the mask: the role the con artist or crew played, and who it was played for.',
                      'Name the moment a single person could have broken it with one check.',
                      'Now turn it on yourself: list three accounts or payments in your own work that a convincing voice could reach.',
                      'For each, write the check you will use from now on: call-back, named approver or a written rule.'],
               mistake='Thinking you are too sharp to fall for it. The cases in this file beat banks, casinos and a museum. The defence is a habit you use when you feel sure, not a feeling of being clever.'),
    biz="MTRX™ holds client domains, hosting, logins and payments. Set three rules today: never reset a client login or change a domain on a call or message alone; confirm any change of bank details by calling back a number you already have; and keep a short written list of who at each client may approve what.",
    tryit="Watch the video above. Write down the moment the reporter could have stopped it and the single sentence they could have said. Then write the sentence you would use on a call that felt urgent.",
    room='The attacker needs one person to skip one check. Defence is a habit, not a gadget.',
    deeper=[('NBC News: how the MGM hackers got in', 'https://www.nbcnews.com/tech/security/mgm-las-vegas-hackers-scattered-spider-rcna105238', 'The help desk angle')],
    nextq='File 6 follows the money. How did a respected Wall Street figure run the largest Ponzi scheme in history for decades, and why did his victims trust him? Stop 6.1.',
    checks=[dict(q='How was MGM Resorts reportedly breached in September 2023?',
                 o=['A call to its IT help desk by someone posing as an employee',
                    'A flaw in the casino slot machine software',
                    'A stolen laptop left in a hotel room'], a=0,
                 w='A plausible voice and a process that rewarded speed. No exotic code needed.'),
            dict(q='What is the strongest defence against a convincing urgent call?',
                 o=['Call back on a number you already hold',
                    'Ask the caller to confirm their name twice',
                    'Trust your gut about how they sound'], a=0,
                 w='A call-back removes the judgement call. Voices and names can be faked; your own number cannot.'),
            dict(q='What share of 2024 breaches did Verizon link to a non-malicious human element?',
                 o=['68%', '18%', '98%'], a=0,
                 w='Verizon\'s 2024 report put it at 68%. People, not code, are the usual entry point.')],
)

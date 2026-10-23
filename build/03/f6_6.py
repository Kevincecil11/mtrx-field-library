from svg import box, t, arrow, line, svg

COLS = [('ROMANCE BAITING', 'a friend or lover', 'profits on a fake app', 'deposit more to withdraw'),
        ('TASK SCAM', 'an online employer', 'small early payouts', 'pay to unlock earnings'),
        ('DIGITAL ARREST', 'police or customs', 'uniforms on a video call', 'pay to clear your name'),
        ('FAKE CLIENT', 'a keen new client', 'a payment that overpays', 'refund the difference')]
ROWS = ['THE MASK', 'CONVINCER', 'THE ASK']
def col(i, c):
    x = 180 + i * 250
    out = box(x, 56, 240, 50, 's-box-j', 10) + t(x + 120, 87, c[0], 's-t-b')
    for r in range(3):
        y = 120 + r * 66
        out += box(x, y, 240, 54, 's-card', 10) + t(x + 120, y + 33, c[r + 1], 's-t-sm')
    return out
FIG = svg(1180, 420, 'Four modern scams compared: the mask, the convincer and the ask, with one defence that beats all four',
          t(590, 32, 'FOUR COSTUMES, ONE CON', 's-t') +
          ''.join(t(92, 153 + r * 66, n, 's-t-b') for r, n in enumerate(ROWS)) +
          ''.join(col(i, c) for i, c in enumerate(COLS)) +
          t(92, 352, 'DEFENCE', 's-t-b') + box(180, 322, 990, 50, 's-box-a', 10) +
          t(675, 353, 'Stop. Verify on a channel you choose. Never pay to get paid. Tell someone outside the chat.', 's-t-sm') +
          t(590, 404, 'A mask, a convincer, some pressure, and money that cannot come back. Every scam in this stop is the old con.', 's-t-sm'))

STOP = dict(
    id='6.6', day=41, title='Scams that target you: pig butchering, task scams and fake clients',
    q='Americans reported nearly $21 billion lost to online crime in 2025, and India’s “digital arrest” cases tripled in two years. Most began with one friendly or frightening message. What does that message look like when it reaches you?',
    why='Everything in this course meets here: the con’s steps, the masks, the money engines and the excuses. Modern scams industrialise all of it, run from compounds with scripts and quotas, and they aim at ordinary people: job seekers, lonely people, retirees and small businesses like MTRX™. This is the stop where knowing becomes defending.',
    case=dict(k='The cases', name='Romance baiting, task scams, digital arrests and fake clients', role='Four modern scams, all built on the old con',
              facts=[('FBI, 2025', 'Nearly $21bn reported lost; crypto-related complaints over $11bn'),
                     ('FTC, 2024', 'About 20,000 task-scam reports in six months, up from 5,000 in all of 2023'),
                     ('India, 2024', '1,23,672 digital arrest and related cases, ₹1,935.51 crore lost'),
                     ('UN, 2023', 'At least 120,000 people in Myanmar may be forced to run online scams')],
              stamp=('field', 'Field test: check your own inbox')),
    cold=dict(q='A stranger texts you by mistake, apologises, and becomes a friendly contact for weeks. Nothing is asked for. When does the scam start?',
              a='It already has. In romance baiting, the scam INTERPOL wants us to stop calling pig butchering, the weeks of friendship are the work: the put-up and the tale from stop 4.1. Only once trust is built does the contact mention a trading app that made them rich, share screenshots of profits, and help you make a small deposit that seems to grow. Then withdrawals are blocked by taxes or fees. The FBI says Americans who reported crypto-related complaints lost more than $11 billion in 2025.'),
    video=dict(id='K7Gm40-Cv48', title='‘Pig butchering’ scammers target BBC reporter', who='BBC World Service',
               watch=['How the first message is made to look like an innocent mistake',
                      'When the conversation turns to money, and how gently it happens',
                      'What the fake profits on screen are for']),
    story=['Start with the scam INTERPOL asked the world to rename in December 2024. The criminals called it pig butchering, because victims are fattened with attention before the slaughter. INTERPOL now says romance baiting, because the old term shames victims into silence. It begins with a wrong-number text or a dating match, grows into weeks of friendship, then turns to a trading platform that shows fake profits. The UN human rights office reported in 2023 that at least 120,000 people in Myanmar and around 100,000 in Cambodia may be held in compounds and forced to run these scams. Often there are victims at both ends of the chat.',
           'Task scams are the job version. A WhatsApp message or text offers easy online work: liking videos or rating products to boost them. The app shows commissions piling up, and early on it may even pay out a little, which the FTC says is how it builds trust. Then you must deposit your own money, usually crypto, to unlock the next set of tasks or withdraw your earnings. The FTC counted about 20,000 task-scam reports in the first half of 2024, up from about 5,000 in all of 2023. Its rule is old and simple: never pay to get paid.',
           'India has its own industrial version: the digital arrest. A caller poses as police, customs, the CBI or a regulator, says your parcel or bank account is linked to a crime, keeps you on a video call for hours, and demands money to clear your name. The Ministry of Home Affairs told Parliament that digital arrest and related cases reported on the national portal rose from 39,925 in 2022 to 1,23,672 in 2024, with ₹1,935.51 crore reported lost. Real agencies do not hold people under arrest on video calls, and they do not settle cases by bank transfer.',
           'Then there is the one aimed at small agencies. A new client wants a website fast, accepts your price at once, and sends a cheque or transfer for more than the invoice. Then the request: please refund the difference, or pay our designer or supplier out of the extra. The payment later bounces or is reversed; your refund does not. Close cousins are fake purchase orders, lookalike email domains and sudden changes of bank details. The FBI’s 2025 report puts business email compromise second only to investment fraud for losses.',
           'Lay the four side by side, as the diagram does, and every lesson from this course shows. A mask: a lover, an employer, an officer, a client. A convincer: profits on a screen, a small payout, a uniform, a real payment. Pressure: affection, ambition or fear. And a one-way door for the money: crypto, gift cards, transfers that cannot be reversed. The defence is the same for all four: slow down, verify through a channel you choose, never pay to receive money, and talk to someone outside the conversation before you send anything.'],
    fig=(FIG, 'Four modern scams, one structure: a mask, a convincer and an ask. One defence beats all four.'),
    specs=[('Romance baiting', 'INTERPOL’s term for scams that build a fake relationship, then steer the victim into a fake investment.'),
           ('Task scam', 'A fake online job that shows rising earnings, then demands deposits to unlock them.'),
           ('Overpayment scam', 'A fake buyer or client overpays, asks for the difference back, and the original payment later fails.')],
    tags=[('myth', '“A small payout proves the platform is real.”', 'The FTC says early small payouts are how task scams build trust before the deposits.', ('FTC: gamified job scams drive record losses', 'https://www.ftc.gov/news-events/data-visualizations/data-spotlight/2024/12/paying-get-paid-gamified-job-scams-drive-record-losses')),
          ('hold', '“Many scam workers are victims too.”', 'The UN says at least 120,000 people in Myanmar may be held and forced to run online scams.', ('UN Human Rights Office, August 2023', 'https://www.ohchr.org/en/press-releases/2023/08/hundreds-thousands-trafficked-work-online-scammers-se-asia-says-un-report')),
          ('anti', '“Call it pig butchering.”', 'INTERPOL asks for romance baiting: the old term shames victims and stops them reporting.', ('INTERPOL, 17 December 2024', 'https://www.interpol.int/en/News-and-Events/News/2024/INTERPOL-urges-end-to-Pig-Butchering-term-cites-harm-to-online-victims'))],
    distil=[('FBI: the 2025 Internet Crime Report', 'https://www.fbi.gov/news/press-releases/cryptocurrency-and-ai-scams-bilk-americans-of-billions', 'The $21 billion year'),
            ('FTC: task scams data spotlight, December 2024', 'https://www.ftc.gov/news-events/data-visualizations/data-spotlight/2024/12/paying-get-paid-gamified-job-scams-drive-record-losses', 'Never pay to get paid'),
            ('Business Standard (PTI): digital arrest cases tripled, 2022 to 2024', 'https://www.business-standard.com/india-news/digital-arrests-cyber-crimes-tripled-during-2022-24-govt-tells-parliament-125031200978_1.html', 'India’s numbers, from Parliament')],
    writer=dict(notes=['A modern scam story has victims at both ends of the chat. The person typing the sweet messages may be trafficked and punished for missing a quota. Cut between the two rooms and you have a story about two prisoners, not a con artist and a mark.',
                       'Show the script. A character reading warm lines to a stranger they are hurting is pure drama: the words are kind, the room is cold.'],
                drill='Write a fictional two-room scene: a lonely retiree texting a new friend, and a young trafficked worker typing the replies from a script while a supervisor watches. Neither knows the other’s real life. Fiction only.'),
    drill=dict(name='Boss fight: the money audit', mins='30 min',
               steps=['Pick one case from File 6: Ponzi or Madoff, Herbalife, Theranos, FTX, Wirecard, Satyam, or one of the four modern scams.',
                      'Map its engine in three lines: where the money came from, what the story was, and what stopped people checking.',
                      'Name the person who checked, or who could have, and the one question they asked or should have asked.',
                      'Now audit MTRX™: list every way money enters and leaves (clients, callers’ commission, hosting, ads, tools).',
                      'For each, write your rule: verify new clients, never refund before funds clear, confirm bank changes by call-back, keep client money separate.'],
               mistake='Treating these rules as rudeness. Real clients and partners will not mind a call-back or a cleared payment. Only a scam needs you to hurry.'),
    biz='Write this into the MTRX™ process today. New clients: a video call and a verified business email or website before work starts. Payments: never refund or forward money until it has fully cleared, and never pay a supplier on a client’s behalf. Bank details: confirm any change by calling a number you already hold. Your callers: warn them about task-scam jobs and fake officers, and tell them who to call. In India, report fraud fast on the 1930 helpline or cybercrime.gov.in.',
    tryit='Open your messages and email from the last month. Find one that used a mask, a convincer or urgency, and note which and what you did. If you find none, write the rule you will use when one arrives.',
    room='Only a scam needs you to hurry. Verify on a channel you choose, and never pay to get paid.',
    deeper=[('UN Human Rights Office: online scam operations and trafficking (report)', 'https://bangkok.ohchr.org/sites/default/files/wp_files/2023/08/ONLINE-SCAM-OPERATIONS-2582023.pdf', 'The forced labour behind the chats')],
    nextq='File 7 is the reveal. Cialdini’s principles of influence are taught in every sales course. When scientists try to repeat the classic experiments, which ones survive? Stop 7.1.',
    checks=[dict(q='What does INTERPOL now call the scam criminals nicknamed pig butchering?',
                 o=['Romance baiting', 'Love trading', 'Crypto catfishing'], a=0,
                 w='INTERPOL says the old term shames victims and discourages them from reporting.'),
            dict(q='A new client overpays and asks you to refund the difference. What should you do?',
                 o=['Wait for the money to fully clear and verify the client independently',
                    'Refund quickly to keep the client happy',
                    'Pay their supplier directly from the extra'], a=0,
                 w='The original payment can bounce or be reversed. Your refund cannot. Real clients will wait.'),
            dict(q='What single rule defeats every task scam?',
                 o=['Never pay money to get paid',
                    'Only accept tasks from well-known apps',
                    'Withdraw your earnings every day'], a=0,
                 w='The FTC’s rule. Early payouts are bait; the deposit to unlock earnings is the scam.')],
)

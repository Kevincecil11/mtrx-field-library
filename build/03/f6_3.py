from svg import box, t, arrow, line, svg

LEFT = ['a few drops, 240+ tests', 'famous names on the board', 'valued at $9 billion']
RIGHT = ['mostly other makers’ machines', 'results staff did not trust', 'staff who raised alarms']
FIG = svg(1180, 420, 'Theranos: what investors saw, the wall of secrecy in the middle, and what the lab knew',
          t(590, 32, 'THE WALL BETWEEN THE STORY AND THE LAB', 's-t') +
          t(200, 76, 'WHAT INVESTORS SAW', 's-t-b') + t(980, 76, 'WHAT THE LAB KNEW', 's-t-b') +
          ''.join(box(60, 92 + i * 70, 280, 56, 's-card', 10) + t(200, 126 + i * 70, s, 's-t-sm') for i, s in enumerate(LEFT)) +
          ''.join(box(840, 92 + i * 70, 280, 56, 's-box-a', 10) + t(980, 126 + i * 70, s, 's-t-sm') for i, s in enumerate(RIGHT)) +
          box(450, 92, 280, 196, 's-box-j', 12) + t(590, 138, 'THE WALL', 's-t-b') +
          t(590, 178, 'secrecy and strict NDAs', 's-t-sm') + t(590, 210, 'teams kept apart', 's-t-sm') +
          t(590, 242, 'lawyers for critics', 's-t-sm') +
          t(590, 326, 'What broke the wall: two employees who spoke up, one reporter, and regulators who inspected.', 's-t-sm') +
          line(80, 352, 1100, 352, True) +
          t(590, 388, 'The money followed the left column. Patients lived with the right one.', 's-t-sm'))

STOP = dict(
    id='6.3', day=38, title='Theranos: the story that outran the science',
    q='Elizabeth Holmes raised more than $700 million for blood tests that did not work as claimed, with statesmen and a general on her board. Why did so many smart people believe a story nobody could check?',
    why='Ponzi and pyramid schemes fake the money. Theranos faked the product, and that is the kind of fraud most likely to tempt a founder, because it starts as optimism. For a writer, Holmes is a study in a character who may have believed her own pitch. For anyone selling technology, including an AI agency, it is the clearest warning there is about the gap between a demo and a product.',
    case=dict(k='The case', name='Theranos, 2003 to 2018', role='A blood-testing start-up that promised lab tests from a finger prick',
              facts=[('The promise', 'More than 240 tests from a few drops of blood'),
                     ('The money', 'More than $700m raised from investors (SEC)'),
                     ('The break', 'John Carreyrou’s Wall Street Journal story, 15 October 2015'),
                     ('The sentences', 'Holmes 135 months; Ramesh Balwani 155 months')],
              stamp=('hold', 'Holds: the story outran the science')),
    cold=dict(q='Holmes was convicted of defrauding investors. Was she also convicted of defrauding patients?',
              a='No. In January 2022 a jury convicted her on four counts of defrauding investors and acquitted her on the counts involving patients, even though patients were the people handed unreliable results. That is a lesson about what courts can prove: investor losses leave a paper trail of pitch decks and wire transfers. Her former business partner, Ramesh Balwani, was convicted on all twelve counts he faced, and received the longer sentence.'),
    video=dict(id='WOi8-tM1gvQ', title='“Bad Blood” author on the unraveling of Theranos fraud', who='CBS Mornings',
               watch=['How Carreyrou found his first sources inside the company',
                      'What the company did to people who raised concerns',
                      'The moment the story moved from rumour to proof']),
    story=['Elizabeth Holmes founded Theranos in 2003, at 19, and left Stanford to build it. The pitch was beautiful: a few drops of blood from a finger prick, run on a compact device, could replace the needles and vials of a normal lab test. Cheaper, faster, less frightening. Its website claimed the full range of lab tests from a few drops, and the company offered more than 240 of them. It signed a deal with Walgreens to put testing centres in its pharmacies, and by 2015 the Wall Street Journal reported it was valued at $9 billion. Holmes, in a black turtleneck, drew comparisons to Steve Jobs.',
           'The science did not match the story. Carreyrou reported that by the end of 2014 the company’s own device handled only a small fraction of the tests it sold to consumers; most ran on machines bought from other makers. In 2018 the SEC charged the company, Holmes and Balwani, saying Theranos had raised more than $700 million through false statements about its technology, business and performance. Inside, teams were kept apart, staff signed strict confidentiality agreements, and people who raised concerns were pushed out or threatened with lawyers.',
           'So why did smart people believe it? Because the story came with borrowed authority. The board included two former US secretaries of state, George Shultz and Henry Kissinger, and the general and future defence secretary James Mattis. Their names reassured investors who could not judge the science themselves. Secrecy was presented as protecting trade secrets, so the lack of outside checks looked like strength. This is the convincer from File 4 in a boardroom: not proof, but signals that feel like proof.',
           'What broke it were people who checked. Tyler Shultz, a young employee and George Shultz’s grandson, and his lab colleague Erika Cheung raised the alarm, and Cheung reported the lab to regulators. Carreyrou’s story, “Hot Startup Theranos Has Struggled With Its Blood-Test Technology”, ran on 15 October 2015. Regulators inspected the lab, partners walked away, and the company collapsed. In January 2022 Holmes was convicted on four counts of investor fraud and was later sentenced to 135 months. Balwani got 155.',
           'Writers love Holmes because nobody can be sure what she believed. Hulu’s The Dropout (2022), with Amanda Seyfried in an Emmy-winning performance, plays her as someone who slowly turned into her own pitch: the voice, the clothes, the certainty. That is the most unsettling kind of con artist, one who fooled herself first. Fake it till you make it is fine advice for nerves. It is fraud when the thing you are faking is a medical result.'],
    fig=(FIG, 'What investors saw, what the lab knew, and the wall of secrecy between them. People who checked broke it.'),
    specs=[('Due diligence', 'The checks an investor or partner makes before committing: documents, data and independent tests.'),
           ('Vapourware', 'A product that is announced or sold before it exists or works as described.'),
           ('Whistleblower', 'An insider who reports wrongdoing to regulators, the press or the company’s own channels.')],
    tags=[('part', '“Theranos had no technology at all.”', 'It had devices and ran tests. The SEC said its claims about them were false or exaggerated.', ('SEC charges Theranos, Holmes and Balwani', 'https://www.sec.gov/newsroom/press-releases/2018-41')),
          ('myth', '“Holmes was convicted of defrauding patients.”', 'She was convicted on four investor counts and acquitted on the patient counts.', ('US Attorney: Holmes sentenced', 'https://www.justice.gov/usao-ndca/pr/elizabeth-holmes-sentenced-more-11-years-defrauding-theranos-investors-hundreds')),
          ('hold', '“A famous board is not a check on the science.”', 'Statesmen and generals sat on the board while the device ran only a fraction of the tests.', ('WSJ: Theranos has struggled with its blood tests', 'https://www.wsj.com/articles/theranos-has-struggled-with-blood-tests-1444881901'))],
    distil=[('WSJ, 15 October 2015: the story that broke it', 'https://www.wsj.com/articles/theranos-has-struggled-with-blood-tests-1444881901', 'The original reporting'),
            ('SEC: Theranos charged with massive fraud, 2018', 'https://www.sec.gov/newsroom/press-releases/2018-41', 'The $700 million charge'),
            ('US Attorney: Holmes sentenced to 135 months', 'https://www.justice.gov/usao-ndca/pr/elizabeth-holmes-sentenced-more-11-years-defrauding-theranos-investors-hundreds', 'Counts, verdicts and sentence')],
    writer=dict(notes=['Theranos is a two-column story: what the room sees and what the lab knows. Cut between them. Every time the pitch gets bigger on the left, show the cost growing on the right, and let the audience feel the gap widen.',
                       'Write the self-deceiver with care. A character who lies knowingly is a villain. One who half believes the lie is a tragedy. Give her a private moment where the truth nearly gets in, and let her refuse it.'],
                drill='Write a one-page fictional scene where a junior lab worker shows her manager results that contradict the company’s big claim. The manager never says no. He uses praise, loyalty and the mission to make her doubt herself. Fiction only.'),
    biz='This is the AI agency trap. A demo that works once is not a product that works for every client. Never show a demo built on hand-picked inputs without saying so, and never promise accuracy you have not measured. Write down what your AI receptionist or chatbot actually handles, test it on real calls, and put the limits in the proposal. A promise you can prove beats a vision you cannot.',
    tryit='Pick one claim on your own website or in your last pitch. Write the evidence you could show a sceptical client tomorrow. If you have none, test it this week or soften the claim.',
    room='A demo that worked once is not a product. Show the evidence, not the vision.',
    deeper=[('Big Think: Carreyrou on secrecy and hype at Theranos', 'https://www.youtube.com/watch?v=ONuoeVdB0Ww', 'Founder worship and the mechanics of the fraud')],
    nextq='Theranos fooled people who could not check the science. FTX and Wirecard fooled people whose job was to check. How did every safeguard fail at once? Stop 6.4.',
    checks=[dict(q='What did Carreyrou report about Theranos’s own device by the end of 2014?',
                 o=['It handled only a small fraction of the tests sold to consumers',
                    'It ran every test it claimed, only slower than a commercial lab',
                    'It had been banned by federal regulators before reaching a store'], a=0,
                 w='Most tests ran on machines bought from other makers. The story was far ahead of the science.'),
            dict(q='On which counts was Elizabeth Holmes convicted in January 2022?',
                 o=['Four counts of defrauding investors',
                    'All counts, including those about patients',
                    'Only counts about patients'], a=0,
                 w='She was acquitted on the patient counts. Balwani was convicted on all twelve counts he faced.'),
            dict(q='Why did a board of famous statesmen reassure investors?',
                 o=['Their names felt like proof, though none of them tested the science',
                    'They had personally run and checked the blood tests in the lab',
                    'They had signed personal guarantees covering the investors’ money'], a=0,
                 w='Borrowed authority is a convincer. It feels like evidence without being evidence.')],
)

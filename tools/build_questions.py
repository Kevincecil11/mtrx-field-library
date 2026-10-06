#!/usr/bin/env python3
"""Build the review-bot question banks from the guides.

Reads guides/NN-*.html and writes bot/questions/NN.json. Run it after adding or
editing a guide (the bot workflow also runs it on every run). Stdlib only.

Card sources, per stop (data-mod on button.done):
  quiz   : every quick check inside the stop (<div class="check"><script type="application/json">)
  recall : the stop's "Say it in the room" line, as a free-recall prompt
  recall : No. 02 style day guides: every Q and A block (<div class="qa"> with details.ans) and use case
Stop order = document order of <button class="done" data-mod>, which is what the
guide's "Send progress" button encodes, so never reorder without rebuilding.
"""
import glob, html, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUIDES = os.path.join(ROOT, 'guides')
OUT = os.path.join(ROOT, 'bot', 'questions')


def clean(s):
    s = re.sub(r'<br\s*/?>', ' ', s or '')
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s).replace('\u2014', ', ').replace('\u2013', ' to ').replace('\xa0', ' ')
    return re.sub(r'\s+', ' ', s).strip()


def attrs(tag):
    return dict(re.findall(r'([\w-]+)="([^"]*)"', tag))


def build(path):
    s = open(path, encoding='utf-8').read()
    g = os.path.basename(path)[:2]
    title = clean((re.search(r'<title>(.*?)</title>', s, re.S) or [None, ''])[1])
    stops = []
    for tag in re.findall(r'<button\b[^>]*>', s):
        a = attrs(tag)
        if 'data-mod' in a and re.search(r'(^|\s)done(\s|$)', a.get('class', '')) and a['data-mod'] not in stops:
            stops.append(a['data-mod'])
    day = bool(re.search(r'<article class="mod day"', s))
    cards = []
    for m in re.finditer(r'<article\b([^>]*)>', s):
        a = attrs(m.group(1))
        stop, aid = a.get('data-mod'), a.get('id')
        if not stop or stop not in stops:
            continue
        end = s.find('</article>', m.end())
        art = s[m.end():end]
        name = clean((re.search(r'class="mod-title"[^>]*>(.*?)</h2>', art, re.S) or [None, ''])[1])
        link = 'guides/%s#%s' % (os.path.basename(path), aid)
        base = dict(guide=g, stop=stop, name=name, link=link)
        n = 0
        for j in re.findall(r'<div class="check"><script type="application/json">(.*?)</script>', art, re.S):
            try:
                d = json.loads(j)
            except ValueError:
                continue
            n += 1
            cards.append(dict(base, id='%s-%s-q%d' % (g, stop, n), type='quiz', q=clean(d['q']),
                              options=[clean(o) for o in d['o']], answer=int(d['a']), why=clean(d.get('w', ''))))
        r = 0
        if day:
            blocks = re.findall(r'<div class="(?:qa|usecase)"[^>]*>(.*?)</details>', art, re.S)  # skips "rv qa" warm-ups (repeats of earlier days)
            pairs = [re.search(r'<p class="q">(.*?)</p>.*?<div class="a">(.*)', b, re.S) for b in blocks]
            for q, ans in [x.groups() for x in pairs if x]:
                label = clean((re.search(r'<small>(.*?)</small>', q) or [None, ''])[1])
                if label.lower() == 'baseline' or re.match(r'Day \d+ ·', label):  # warm-ups repeat earlier days
                    continue
                q = clean(re.sub(r'<small>.*?</small>', '', q))
                if not q or 'class="q"' in q:
                    continue
                r += 1
                cards.append(dict(base, id='%s-%s-r%d' % (g, stop, r), type='recall', q=q, answer=clean(ans), label=label))
        else:
            for dname, steps, mistake in re.findall(r'<div class="drill"[^>]*><div class="drill-h"><b>(.*?)</b>.*?<ol>(.*?)</ol>.*?<p class="drill-x"><b>[^<]*</b>(.*?)</p>', art, re.S):
                r += 1
                st = ' '.join('%d) %s' % (i + 1, clean(x)) for i, x in enumerate(re.findall(r'<li>(.*?)</li>', steps, re.S)))
                cards.append(dict(base, id='%s-%s-r%d' % (g, stop, r), type='recall',
                                  q='Drill "%s": what are the steps, and the usual mistake?' % clean(dname),
                                  answer=st + ' Usual mistake: ' + clean(mistake), label='Drill'))
            room = re.search(r'class="room"[^>]*>(.*?)</(?:p|div)>', art, re.S)
            if room and name:
                r += 1
                cards.append(dict(base, id='%s-%s-r%d' % (g, stop, r), type='recall',
                                  q='Page closed: explain "%s" in two or three lines, as you would to a client.' % name,
                                  answer=clean(room.group(1)), label='Say it in the room'))
    return dict(guide=g, title=title, file=os.path.basename(path), day=day, stops=stops, cards=cards)


def main():
    os.makedirs(OUT, exist_ok=True)
    summary = []
    for path in sorted(glob.glob(os.path.join(GUIDES, '[0-9][0-9]-*.html'))):
        b = build(path)
        open(os.path.join(OUT, b['guide'] + '.json'), 'w', encoding='utf-8').write(
            json.dumps(b, ensure_ascii=False, indent=1) + '\n')
        covered = len({c['stop'] for c in b['cards']})
        summary.append('%s: %d stops, %d cards (%d quiz, %d recall), %d stops with no card' % (
            b['guide'], len(b['stops']), len(b['cards']), sum(c['type'] == 'quiz' for c in b['cards']),
            sum(c['type'] == 'recall' for c in b['cards']), len(b['stops']) - covered))
    print('\n'.join(summary))


if __name__ == '__main__':
    sys.exit(main())

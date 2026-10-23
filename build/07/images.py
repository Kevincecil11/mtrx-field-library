"""Images for No. 07, by exact Wikimedia Commons file title (checked 23 Oct 2026).
Only public-domain works or openly licensed photos. build.py fetches each once in CI,
caches it in build/out/07-img/ and inlines it. values=True adds greyscale and notan versions."""

IMAGES = {
    'snow': dict(file='File:Snow-cholera-map-1.jpg',
                 credit='John Snow, map of the 1854 cholera deaths around Broad Street, London', lic='Public domain',
                 alt='John Snow\'s map of Soho with black bars marking cholera deaths clustered around the Broad Street pump'),
    'repin': dict(file='File:Ilya Repin Unexpected visitors.jpg',
                  credit='Ilya Repin, They Did Not Expect Him (Unexpected Visitors), 1884 to 1888, Tretyakov Gallery', lic='Public domain',
                  alt='Repin painting: a gaunt man in a long coat walks into a family room and the family turns to stare'),
    'kandinsky': dict(file='File:Kandinsky - Composition 8, 1923.jpg',
                      credit='Wassily Kandinsky, Composition VIII, 1923, Solomon R. Guggenheim Museum', lic='Public domain',
                      alt='Kandinsky abstract painting of circles, triangles, crossing lines and grids on a pale ground'),
    'wave': dict(file='File:Great Wave off Kanagawa2.jpg',
                 credit='Katsushika Hokusai, Under the Wave off Kanagawa, about 1830 to 1832, woodblock print', lic='Public domain',
                 alt='Hokusai print: a huge clawed wave curls over three boats while small Mount Fuji sits in the distance'),
    'caravaggio': dict(file='File:Caravaggio \u2014 The Calling of Saint Matthew.jpg', values=True,
                       credit='Caravaggio, The Calling of Saint Matthew, 1599 to 1600, Contarelli Chapel, San Luigi dei Francesi, Rome', lic='Public domain',
                       alt='Caravaggio painting: a beam of light crosses a dark room from Christ, pointing, to Matthew at a table of men'),
}

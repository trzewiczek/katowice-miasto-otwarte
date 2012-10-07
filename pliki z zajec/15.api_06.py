# -*- coding: utf-8 -*-
from urllib import urlopen, quote
import json

for i in range(30):
    print ''

wiki_host   = 'http://pl.wikipedia.org/w/api.php?'
wiki_params = 'action=query&srsearch=%s&list=search&format=json'

sejm_url = 'http://api.sejmometr.pl/poslowie'

sejm_list = json.loads(urlopen(sejm_url).read())

for posel in sejm_list:
    posel_url = 'http://api.sejmometr.pl/posel/%s/info' % posel
    metryczka = json.loads(urlopen(posel_url).read())

    posel_id = metryczka['id']
    nazwisko = metryczka['nazwa']
    zawod    = metryczka['pkw_zawod']

    wiki_url = wiki_host + (wiki_params % nazwisko)
    wiki_search = json.loads(urlopen(wiki_url.encode('utf-8')).read())

    # weź pierwszy na liście
    if len(wiki_search['query']['search']) == 0:
        strona = 'Nie ma strony'
    else:
        strona = 'http://pl.wikipedia.org/wiki/%s' % wiki_search['query']['search'][0]['title']

        # sprawdź pozostałe czy nie mają dopisków parlamentarnych
        for wiki_wynik in wiki_search['query']['search']:
            if u'(polityk)' in wiki_wynik['title']:
                strona = 'http://pl.wikipedia.org/wiki/%s' % wiki_wynik['title']

            if u'(poseł)' in wiki_wynik['title']:
                strona = 'http://pl.wikipedia.org/wiki/%s' % wiki_wynik['title']
                                 
            if u'(posłanka)' in wiki_wynik['title']:
                strona = 'http://pl.wikipedia.org/wiki/%s' % wiki_wynik['title']

    print '_' * 80
    print '>>> %3s: %s (%s)' % (posel_id, nazwisko, zawod)
    print strona

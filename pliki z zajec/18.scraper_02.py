# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
from urllib import urlopen

url = 'http://oslislo.pl/ostryga/'

page = bs(urlopen(url).read())

klocki = page.find_all('div', 'box')

for klocek in klocki:
    # tytul posta
    titel = klocek.find('h1').text

    # stopka posta (data i komentarze)
    stopka = klocek.find('div', 'posted')
    # data posta
    data = stopka.find('span', 'entry-date').text
    # treść komentarza
    komment = stopka.find('a').text

    if not komment.startswith('No'):
        print "%s: %s" % (data.replace('/', '-'), titel)
        print komment
        print '-' * 50

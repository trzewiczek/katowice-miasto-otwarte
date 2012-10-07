# -*- coding: utf-8 -*-
from urllib import urlopen
import json

host   = 'http://pl.wikipedia.org/w/api.php?'
params = 'action=query&srsearch=%s&list=search&format=json'

co = raw_input('Czego szukasz, wędrowcze? ')

url = host + (params % co)

wyniki_searcha = urlopen(url).read()
wyniki_dane = json.loads(wyniki_searcha)

for licznik, wynik in enumerate(wyniki_dane['query']['search'], 1):
    print "%2s: %s" % (licznik, wynik['title'])

numerek = raw_input("Które ci pokazać? ")
indeks = int(numerek) - 1
tytul_wybrany = wyniki_dane['query']['search'][indeks]['title']

print wyniki_dane['query']['search'][indeks]['title']
print 'http://pl.wikipedia.org/wiki/%s' % tytul_wybrany
print wyniki_dane['query']['search'][indeks]['snippet']
print '-' * 80



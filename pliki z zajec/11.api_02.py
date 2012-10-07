# -*- coding: utf-8 -*-
from urllib import urlopen
import json

host   = 'http://pl.wikipedia.org/w/api.php?'
params = 'action=query&srsearch=%s&list=search&format=json&sroffset=%s'

lista_miast = ['katowice', 'będzin', 'krobia']

for miasto in ['katowice', 'będzin', 'krobia']:
    url    = host + (params % (miasto, '0'))
    strona = urlopen(url).read()
    dane   = json.loads(strona)

    ilosc = dane['query']['searchinfo']['totalhits']

    for licznik in range(0, ilosc+1, 10):
        wypenione_paramy = params % (miasto, licznik)
        url = host + wypenione_paramy

        strona = urlopen(url).read()
        dane = json.loads(strona)

        for liczydlo, wynik in enumerate(dane['query']['search']):
            print "%2s --> http://pl.wikipedia.org/wiki/%s" % (liczydlo, wynik['title'])

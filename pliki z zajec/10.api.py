# z biblioteki urllib wciągamy funkcję urlopen
from urllib import urlopen
# wciągamy całość biblioteki json
import json

katalog_danych = 'http://katalog.katowiceotwarte.pl/api/datasets' 
# wczytuję dane w postaci tekstowe...
tekst_strony   = urlopen(katalog_danych).read()
# ...i przerabiam to na pythonowe słowniki, listy itp
dane = json.loads(tekst_strony)

lista_kolekcji = dane['data']

for kolekcja in lista_kolekcji:
    data  = kolekcja['date'].split('.')
    dzien = int(data[0])

    if dzien > 4:
        print "%s: %s" % (kolekcja['date'], kolekcja['name'])

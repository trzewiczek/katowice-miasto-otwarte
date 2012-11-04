# coding: utf-8

# importowanie regexu i meerkata
import re
import json
from meerkat import Table

#importowanie bazy danych
tabelka = Table('dane.csv', delimiter=',')

#nazywanie kolumn do pozniejszego uzytku
numery_rejestrowe = tabelka.column('register_number')
identyfikatory_zabytkow= tabelka.column('relic_id')
datowanie_zabytku = tabelka.column('dating')

#definiowane funkcji do pozniejszego uzytku
def wyczysc_ino_date(data):

    #slownik o tym, jak czyscic dane z datowaniem
    czyscik = {
         'ok.'      : '',
         'kon.'     : 'koniec',
        u'2 poł.'   : '2 polowa',
        u'1 ćw.'    : '1 cwiercwiecze',
         'pocz.'    : 'poczatek',
        u'w połowie': 'w polowie',
     'w lowowie XIX': 'w polowie',
         'IX-08'    : '1908-1909',
         'VII-03'   : '1903-1907',
         '1095'     : '1905',
         'XIX/XX'   : '1900',
         'XVII'     : '1650',
         '1908-1915, 1922-1924' : '1916'
    } 

    raw_data = data
    
    for skrot, podmianka in czyscik.items():
        data = data.replace(skrot, podmianka)
        
    data = data.strip()

    if len(data) == 4 and data.isdigit():
        return data

    elif 7 <= len(data) <= 9 and ('-' in data or '/' in data):
        if '-' in data:
            poczatek, koniec = data.split('-')
        elif '/' in data:
            poczatek, koniec = data.split('/')
            
        wiek = poczatek[:2]

        if len(koniec) == 2:
            koniec = wiek + koniec
            
        return ((int(poczatek) + int(koniec)) / 2)

    elif '1 polowa' in data:
        data = data.replace('1 polowa', '').strip()
        rzymskie = {
            'XVII' : 1625,
            'XVIII': 1725,
            'XIX'  : 1825,
            'XX'   : 1925
        }

        return rzymskie[data]


    elif 'w polowie' in data:
        data = data.replace('w polowie', '').strip()
        rzymskie = {
            'XVII' : 1650,
            'XVIII': 1750,
            'XIX'  : 1850,
            'XX'   : 1950
        }

        return rzymskie[data]


    elif '2 polowa' in data:
        data = data.replace('2 polowa', '').strip()
        rzymskie = {
            'XVII' : 1675,
            'XVIII': 1775,
            'XIX'  : 1875,
            'XX'   : 1975
        }

        return rzymskie[data]


    elif '1 cwiercwiecze' in data:
        data = data.replace('1 cwiercwiecze', '').strip()
        rzymskie = {
            'XVII' : 1612,
            'XVIII': 1712,
            'XIX'  : 1812,
            'XX'   : 1912
        }

        return rzymskie[data]


    elif 'poczatek' in data:
        data = data.replace('poczatek', '').strip()
        rzymskie = {
            'XVII' : 1612,
            'XVIII': 1712,
            'XIX'  : 1812,
            'XX'   : 1912
        }

        return rzymskie[data]


    elif 'koniec' in data:
        data = data.replace('koniec', '').strip()
        rzymskie = {
            'XVII' : 1687,
            'XVIII': 1787,
            'XIX'  : 1887,
            'XX'   : 1987
        }

        return rzymskie[data]

    elif 'po' in data:
        data = data.replace('po', '').strip()

        return (int(data)+10)

    elif len(data) > 4:
        return data[:4]

def dej_mi_date(rid):
    for numer_wiersza, wartosc_komorki in enumerate(identyfikatory_zabytkow):
        if rid == wartosc_komorki:
            data = tabelka.value(numer_wiersza, 'dating')

    return data

def pogrupuj_dekady():
    wyniki = {}
    for rid, numer in zip(identyfikatory_zabytkow, numery_rejestrowe):
        if numer:
            rocznik = numer.strip()[-4:]
            dekada  = rocznik[:3] + '0'

            wyniki.setdefault(dekada, [])
            wyniki[dekada].append(rid)

    return wyniki        



# --------------------------------------------------------------
# W Ł A S C I W Y   P R O G R A M 
dekady_wpisow = range(1940, 2012, 10)
dekady_powstania = range(1850, 1955, 10)

'''
{
  '1970': [ 75463, 82735, 65287 ],
  '1980': [ 54637, 95763 ],
  ...
}
'''
wpisy_dekadami = pogrupuj_dekady()

# ----------------------------------------------
'''
{
  '1970': 3,
  '1980': 2,
  ...
}
'''
liczba_wpisow = {}
for dekada in dekady_wpisow:
    ids = wpisy_dekadami.get(str(dekada), [])
    liczba_wpisow[dekada] = len(ids)

# ----------------------------------------------
'''
{
  '1850': 3,
  '1860': 2,
  ...
}
'''
liczba_zabytkow = {}
for surowa_data in datowanie_zabytku :
    if not surowa_data:
        continue

    data = wyczysc_ino_date(surowa_data)
    # dzielenie całkowite daje całkowity wynik ;)
    dekada = (int(data) / 10) * 10
    if dekada < 1850:
        dekada = 1850

    liczba_zabytkow.setdefault(dekada, 0)
    liczba_zabytkow[dekada] += 1

# ----------------------------------------------
'''
{
    '1970': {
        '1850': 4,
        '1860': 6,
        '1870': 12,
        ...
    },
    '1980': {
        '1850': 6,
        '1860': 8,
        '1870': 16,
        ...
    },
}
'''
liczba_wpisow_dekadami = {}
for dekada in dekady_wpisow:
    liczba_wpisow_dekadami[dekada] = {}

    for dekada2 in dekady_powstania:
        liczba_wpisow_dekadami[dekada][dekada2] = 0
    
    ids = wpisy_dekadami.get(str(dekada), [])
    for rid in ids:
        surowa_data = dej_mi_date(rid)
        if surowa_data:
            data = wyczysc_ino_date(surowa_data)
            dekada2 = (int(data) / 10) * 10

            if dekada2 < 1850:
                dekada2 = 1850

            liczba_wpisow_dekadami[dekada][dekada2] += 1

# --------------------------------------------------------------
# W Y K R E S Y

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# --------------------------------------------------------------
# posortowane dekadami liczby wpisow
dane = []
for dekada in sorted(liczba_wpisow.keys()):
    dane.append(liczba_wpisow[dekada])

f = plt.figure(1)
plt.bar(range(len(dane)), dane, align='center')
plt.title(u'Liczba wpisów w każdej dekadzie')
plt.axis([-1, len(dane), 0, max(dane)*1.1])
plt.xticks(range(len(dekady_wpisow)), dekady_wpisow)
for i, wartosc in enumerate(dane):
    plt.annotate(wartosc, xy=(i, wartosc+1), horizontalalignment='center')
f.savefig('wpisy_w_dekadach.pdf')

# --------------------------------------------------------------
# posortowane dekadami zabytki
dane = []
for dekada in dekady_powstania:
    liczba_obiektow = liczba_zabytkow.get(dekada, 0)
    dane.append(liczba_obiektow)

f = plt.figure(2)
plt.bar(range(len(dane)), dane, align='center')
plt.title(u'Liczba obiektów w każdej dekadzie')
plt.axis([-1, len(dane), 0, max(dane)*1.1])
plt.xticks(range(len(dekady_powstania)), dekady_powstania)
for i, wartosc in enumerate(dane):
    plt.annotate(wartosc, xy=(i, wartosc+1), horizontalalignment='center')
f.savefig('zabytki_w_dekadach.pdf')

# --------------------------------------------------------------
# liczba zabytków dekadami, dla każdej dekady wpisów z osobna
for i, dekada in enumerate(dekady_wpisow):
    f = plt.figure(3+i)
    
    dane = []
    for dekada2 in dekady_powstania:
        liczba_obiektow = liczba_wpisow_dekadami[dekada].get(dekada2, 0)
        dane.append(liczba_obiektow)

    plt.bar(range(len(dane)), dane, align='center')
    plt.title(u'Liczba obiektów wpisanych w %s' % dekada)
    plt.axis([-1, len(dane), 0, 150])
    plt.xticks(range(len(dekady_powstania)), dekady_powstania)
    for i, wartosc in enumerate(dane):
        plt.annotate(wartosc, xy=(i, wartosc+1), horizontalalignment='center')
    f.savefig('grid_%s.pdf' % dekada)

# --------------------------------------------------------------
# liczba obiektów w rejestrze w kolejnych dekadach 

# zerujemy liczbę obiektów w rejestrze
dane = []
for dekada in dekady_powstania:
    dane.append(0)

for i, dekada in enumerate(dekady_wpisow):
    f = plt.figure(12+i)

    # dodajemy liczbę zabytków wpisanych w danej dekadzie
    for j, dekada2 in enumerate(dekady_powstania):
        liczba_obiektow = liczba_wpisow_dekadami[dekada].get(dekada2, 0)
        dane[j] += liczba_obiektow

    plt.bar(range(len(dane)), dane, align='center')
    plt.title(u'Liczba obiektów w rejestrze w %s' % dekada)
    plt.axis([-1, len(dane), 0, 200])
    plt.xticks(range(len(dekady_powstania)), dekady_powstania)
    for i, wartosc in enumerate(dane):
        plt.annotate(wartosc, xy=(i, wartosc+1), horizontalalignment='center')
    f.savefig('grid_przyrostowy_%s.pdf' % dekada)

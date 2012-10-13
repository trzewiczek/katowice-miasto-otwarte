# -*- coding: utf-8 -*-
# zobaczmy, jak w naszych kilku przykładowych projektach
# rozkładają się finanse!

from meerkat import Table

# wczytujemy tabelkę
tabelka = Table('dane.csv')

# słownik, w którym będziemy zbierali informacje, ile kasy 
# dostał z UE każdy z beneficjentów na naszej liście
wyniki = {}

# na chwilę wyjmujemy sobie z tabelki dwie kolumny
# tę zawierającą kwoty dofinansowania z UE oraz
# tę z nazwami beneficjentów
dofinansowania = tabelka.column('Dofinansowanie UE') 
beneficjenci   = tabelka.column('Nazwa beneficjenta')

# używamy funkcji zip(lista, lista), dzięki której 
# będziemy mogli przejechać przez naszą tabelę równolegle
# po kolumnie z dofinansowaniem oraz z nazwą beneficjenta
for kasa, nazwa in zip(dofinansowania, beneficjenci):
    # jeśli nie widzieliśmy jeszcze takiego beneficjenta to 
    # stwórzmy dla niego miejsce w słowniku z wynikami
    # zaczynając od kwoty dofinansowania równej zero!
    wyniki.setdefault(nazwa, 0.0)
    # dodajemy do kwoty zebranej przez danego beneficjenta
    # nowo napotkaną kwotę ( x += 3 to skrót od x = x + 3)
    wyniki[nazwa] += kasa

# tak jak możemy ze slownika wydobyć klucze funkcją keys,
# a wartości funkcją values, tak możemy wydobyć ich pary
# funkcją items --> [(klucz1, wartość1), (klucz2, wartość2)...]
# dzięki temu łatwo i przyjemnie wydrukujemy sobie nasze
# wyniki w postaci - kasa: nazwa beneficjenta
print '-' * 80
for nazwa, kasa in wyniki.items():
    print "%12.2f: %s" % (kasa, nazwa)
    
print '-' * 80

# wydobędziemy teraz same wartości dofinansowania
kasa = wyniki.values()
# i je posortujemy dla lepszego oglądu sytuacji
kasa.sort()

# zaimportujemy sobie bibliotekę do rysowania wykresów
import matplotlib.pyplot as plt

# by poprosić ją o wykres dofinansowań za pomocą
# niebieskich (b) kółek (o) - będzie ślicznie
plt.plot(kasa, 'bo')

# określimy by skala pozioma była taka jak liczba
# naszych wartości (pamiętamy o liczeniu od zera!)
# a skala pionowa od 0 do najwiekszej wartości na liście
plt.axis([0, len(kasa)-1, 0, max(kasa)])

# no i sobie zobaczymy, jak to się rozkłada! :)
plt.show()

# możemy sobie zapisać to jako jeden z kilku formatów
# graficznych, wydrukować na koszulce i cieszyć się!

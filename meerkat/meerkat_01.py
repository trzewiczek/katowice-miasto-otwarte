# -*- coding: utf-8 -*-
# importujemy klasę tabela z biblioteki meerkat
# klasa to nowy typ - tak jak napisy, listy czy słowniki
# miały swoje specyficzne cechy i możliwości, tak
# będzie miała nasz tabela. wszysto wyjdzie w praktyce
from meerkat import Table

# wczytujemy plik csv do zmiennej tabelka
# przyjmujemy to kilka założeń:
#   - kolumny oddzielone są średnikami (delimiter=';')
#   - używamy cudzysłowów do oznaczenia tekstu (quotechar='"')
#   - plik posiada nagłówek w pierwszym wierszu (header=True)
#   - badamy typy kolumn (numeryczna/tekstowa) w calym pliku (how_deep=0)
# wszystkie te parametry mogą być zmianione i gdybyśmy nie
# mieli nagłówka to napisalibyśmy:
#
#   tabelka = Table('dane.csv', header=False)
#
# podobnie postąpilibyśmy z pozostałymi parametrami.
# jeśli to wszystko nie jest do końca jasne - stanie się
# w praktyce - zrozumienie jest wprost proporcjonalne
# do ilości czerwonego na ekranie ;)
print "Wczytuję tabelkę"
tabelka = Table('dane.csv')
print "Tabelka wczytana!"
print ""
# czasmi zobaczymy ostrzeżenie: znaleziono puste komórki
# w tabeli. będzie to ważne dla obliczeń, które będziemy
# wykonywali na tej tabeli. to nie błąd, ale trzeba mieć
# to w pamięci wyliczając np. średnią wartość kolumny

# możemy odpytać naszą tabelkę o podstawowe rzeczy, np.:
print "Liczba wierszy: %s" % tabelka.rows_count
print "Liczba kolumn: %s" % tabelka.cols_count
print ""

# nagłówek przechowywany w zmiennej tabelka.header to
# lista słowników - po jednym dla każdej kolumny.
# każdy słownik posiada cztery klucze. Np.:
#
#   {
#     'name': 'Pełna nazwa kolumny',
#     'slug': 'pelna-nazwa-kolumny',
#     'type': <type 'float'>,
#     'index': 4
#   }
#
# slug to nazwa kolumny bez polskich znaków, napisana
# małymi literami z zamienionymi wszystkimi znakami,
# które nie są alfanumeryczne na myślniki.

# znaczy się, że nasze nagłówki wyglądaja tak:
for naglowek in tabelka.header:
  print '-' * 80
  print naglowek['name']
  print "\tname : %s" % naglowek['name']
  print "\tslug : %s" % naglowek['slug']
  print "\ttype : %s" % naglowek['type']
  print "\tindex: %s" % naglowek['index']

# okaze się, że nie jednokrotnie te nagłówki bardzo
# nam się przydadzą. jeśli plik nie zawiera prawdziwego
# nagłówka zostanie dla niego stworzony nagłówek z 
# nazwami kolumn "Column 0", "Column 1" itd.

# tabelka pozwala nam również na wydrukowanie malego
# podsumowania kolumn numerycznych:
print ''
print "Drukujemy podsumowanie"
tabelka.summary()

print ''
print "Do rzeczy!"

# najfajniejsze w tabelce są funkcje pozwalające nam
# na wydobycie wiersza, calumny lub wartości z tabeli:
print ''
print 'Przykładowy wiersz'
print tabelka.row(0)

print ''
print 'Przykładowa kolumna'
print tabelka.column(5)

print ''
print 'Przykładowa wartość'
print tabelka.value(0, 5)

# co więcej, za każdym razem, gdy odwołujemy się do 
# kolumny, nie ma znaczenia, czy będziemy wołać ją
# po indeksie, jak w powyższych przykladach, czy 
# po nazwie, czy po slugu
print ''
print 'Kolumna wolana po indeksie'
print tabelka.column(4)
print ''
print 'Kolumna wolana po nazwie'
print tabelka.column('Dofinansowanie UE')
print ''
print 'Kolumna wolana po slugu'
print tabelka.column('dofinansowanie-ue')
print ''
print 'Wartość wołana po nazwie kolumny'
print tabelka.value(0, 'Dofinansowanie UE')

# inną cechą meerkata jest możliwość uzyskiwania
# danych nie w postaci bezpośredniej, ale opakowanych
# w słowniki zawierające trochę więcej informacji
# dotyczących kolumny, z której pochodzi dana
# wartość, czyli jej nazwę, slug, typ, indeks
# w tym celu do funkcji row, column lub value
# musimy dodać parametr as_dict=True
print ''
print 'Pojedyncza wartość w postaci słownika'
print tabelka.value(0, 'Dofinansowanie UE', as_dict=True)
print ''
print 'Wiersz w postaci słownika'
print tabelka.row(0, as_dict=True)
print ''
print 'Kolumna w postaci słownika'
print tabelka.column('Dofinansowanie UE', as_dict=True)

# dla odważnych jest jeszcze opcja wydobycia wszystkich 
# wierszzy lub kolumn na raz (oczywiście z opcjonalną
# postacią słownikową). 
print ''
print 'Wszystkie wiersze'
print tabelka.rows()
print ''
print 'Wszystkie kolumny'
print tabelka.columns()

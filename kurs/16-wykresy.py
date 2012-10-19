# coding: utf-8

# importujemy pakiet pyplot z biblioteki matplotlib
# i nadajemy mu tymczasową nazwę plt, żeby było łatwiej
import matplotlib.pyplot as plt

# mamy dwie listy wartości --> to mogłyby byc prawdziwe dane ;)
x = [1, 2, 3, 4, 5]
y = [4, 2, 5, 3, 1]

# rysujemy wykres zaznaczający kółeczkami wartości
# 
#     x i y            --> wartości odpowiednio dla osi x i y
#     'o'              --> typ markera (kółko)
#     color            --> kolor markera
#     markeredgecolor  --> kolor obwódki markerów
#     label            --> nazwa tego jednego wykresu
#
plt.plot(x, y, 'o', color='#ff6000', markeredgecolor='#ff6000', label='Pierwszy')

# rysujemy drugi wykres tym razem słupkowy
# 
#     y i x      --> wartości odpowiednio dla osi x i y
#     color      --> kolor słupków
#     edgecolor  --> kolor obwódki markerów
#     label      --> nazwa tego jednego wykresu
#     width      --> szerokość słupka
#     align      --> położenie słupka wobec wartości na osi x
#
plt.bar(y, x, color='#cccccc', edgecolor='#cccccc', label='Drugi', width=0.5, align='center')

# zakres wartości na osi x i na osi y
plt.axis([0, 6, 0, 6])

# opisy wartości na osiach x i y
# pierwsza lista to określenie w których miejscach osi powinny się
# znaleźć opisy (bo przecież nie wszędzie jest to obowiązkowe!)
# druga lista to lista etykietek dla każdej z pozycji wymienionej
# w pierwszej liście - listy muszą mieść tę samą długość
plt.xticks([1, 2, 3, 4, 5], ['2001', '2002', '2003', '2004', '2005'])
plt.yticks([1, 3, 5], [1, 3, 5])

# stwórz legendę w górnym prawym rogu
plt.legend(loc='upper right')

# opis osi x
plt.xlabel('iksy')
# opis osi y
plt.ylabel('igreki')
# ogólny tytuł całego wykresu
plt.title('iksy na igrekach')

# pokaż wykres
plt.show()

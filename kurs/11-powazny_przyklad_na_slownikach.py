# coding: utf-8
# Te same dane, co w przykładzie 08!
# Tabela posiada następujące kolumny:
#   - nazwa miejscowości
#   - rok
#   - miesiac
#   - wilgotność (%)
#   - temperatura
# Dane pochodzą ze strony: http://stacje.katowice.pios.gov.pl/monitoring/
dane = [
    ["Dąbrowa Górnicza", 2009,  1, 92, -5.6],
    ["Dąbrowa Górnicza", 2009,  2, 94, -3.7],
    ["Dąbrowa Górnicza", 2009,  3, 88, -0.1],
    ["Dąbrowa Górnicza", 2009,  4, 55, 10.3],
    ["Dąbrowa Górnicza", 2009,  5, 68, 11.9],
    ["Dąbrowa Górnicza", 2009,  6, 82, 13.1],
    ["Dąbrowa Górnicza", 2009,  7, 73, 17.4],
    ["Dąbrowa Górnicza", 2009,  8, 77, 16.6],
    ["Dąbrowa Górnicza", 2009,  9, 84, 13.1],
    ["Dąbrowa Górnicza", 2009, 10, 93, 5.0],
    ["Dąbrowa Górnicza", 2009, 11, 92, 3.4],
    ["Dąbrowa Górnicza", 2009, 12, 94, -2.7],
    ["Dąbrowa Górnicza", 2010,  1, 95, -8.1],
    ["Dąbrowa Górnicza", 2010,  2, 91, -3.5],
    ["Dąbrowa Górnicza", 2010,  3, 77, 1.3],
    ["Dąbrowa Górnicza", 2010,  4, 75, 6.6],
    ["Dąbrowa Górnicza", 2010,  5, 92, 9.9],
    ["Dąbrowa Górnicza", 2010,  6, 77, 15.1],
    ["Dąbrowa Górnicza", 2010,  7, 79, 18.4],
    ["Dąbrowa Górnicza", 2010,  8, 87, 15.9],
    ["Dąbrowa Górnicza", 2010,  9, 91, 9.4],
    ["Dąbrowa Górnicza", 2010, 10, 89, 3.4],
    ["Dąbrowa Górnicza", 2010, 11, 94, 4.3],
    ["Dąbrowa Górnicza", 2010, 12, 98, -6.6],
    ["Dąbrowa Górnicza", 2011,  1, 97, -2.7],
    ["Dąbrowa Górnicza", 2011,  2, 89, -4.4],
    ["Dąbrowa Górnicza", 2011,  3, 77, 1.9],
    ["Dąbrowa Górnicza", 2011,  4, 72, 9.0],
    ["Dąbrowa Górnicza", 2011,  5, 74, 12.0],
    ["Dąbrowa Górnicza", 2011,  6, 81, 16.4],
    ["Dąbrowa Górnicza", 2011,  7, 89, 15.3],
    ["Dąbrowa Górnicza", 2011,  8, 84, 17.3],
    ["Dąbrowa Górnicza", 2011,  9, 85, 13.4],
    ["Dąbrowa Górnicza", 2011, 10, 92, 6.7],
    ["Dąbrowa Górnicza", 2011, 11, 93, 0.9],
    ["Dąbrowa Górnicza", 2011, 12, 97, -0.1],
]

# tym razem chcielibyśmy pozbierać średnie temperatury oraz poziomy
# wilgotności w kolejnych latach. W tym celu każdy rocznik to będzie
# słownik posiadający trzy klucze: 'rok', 'temp' i 'wilg'. Wartościami 
# dla tych kluczy będą "nawa roku" (2009, 2010...) oraz dwie listy 
# odpowiednio temperatur i poziomów wilgotności w każdym miesiącu roku. 
#
#   roczniki = [
#       {
#         'rok': 2009,
#         'temp': [ -5.6, -3.7, -0.1, ... -2.7 ],
#         'wilg': [ 92, 94, 88 ... 94 ]
#       },
#       {
#         'rok': 2010,
#         'temp': [ -8.1, -3.5, 1.3 ... -6.6 ],
#         'wilg': [ 95, 91, 77 ... 98 ]
#       }
#       {
#         'rok': 2011,
#         'temp': [ -2.7, -4.4, 1.9 ... -0.1 ],
#         'wilg': [ 97, 89, 77 ... 97 ]
#       }
#   ]

# zaczynamy od pustej listy roczników, bo nie wiemy, ile ich będzie
roczniki = []

# i teraz dla każdego pomiaru na liście naszych danych
# sprawdzimy z jakiego roku są to dane i pogrupujemy temperatury
# w odpowiednie listy dla każdego roku
for pomiar in dane:
  # żeby nie używać głupich nazw z indeksami, nadamy sobie tymczasowe
  # nazwy dla wartości, które nas interesują: rok, wilgotność i temperatura
  rok  = pomiar[1]
  wilg = pomiar[3]
  temp = pomiar[4]

  # jeśli lista roczników jest pusta (znaczy, że dopiero zaczęliśmy) lub
  # jeśli nazwa (liczba?) roku ostatniego rocznika na liście to nie 
  # jest rok aktualnie analizowanego wiersza z tabeli to...
  if len(roczniki) == 0 or roczniki[-1]['rok'] != rok:
      # ...stwórz taki pusty jeszcze słownik dla aktualnego rocznika...
      pusty_rocznik = {
          'rok' : rok,
          'temp': [],
          'wilg': []
      }
      # ...i dodaj go do listy dotychczas przeanalizowanych roczników
      roczniki.append(pusty_rocznik)

  # do ostatniego rocznika na liście dodaj w odpowiednie miejsca
  # średnie wartości temperatury i poziomu wilgotności
  roczniki[-1]['temp'].append(temp)
  roczniki[-1]['wilg'].append(wilg)


# liczymy średnie temperatur i poziomu wilgotności dla każdego rocznika
for rocznik in roczniki:
  # policz średnią temperaturę w danym roku
  srednia_temp = sum(rocznik['temp']) / len(rocznik['temp'])
  # policz średnią wilgotnośc w danym roku
  srednia_wilg = sum(rocznik['wilg']) / len(rocznik['wilg'])

  # wydrukuj ładnie pamiętając, by zmienić liczby na napisy funkcją str
  print str(rocznik['rok']) 
  print "  Temp: " + str(srednia_temp) + " °C"
  print "  Wilg: " + str(srednia_wilg) + "%"
  print ""

# coding: utf-8

# lista list, czyli pudlo z zabawkami
# każda zabawka to lista jej trzech atrybutów
pudlo = [
  ["Miś",         "maskotka", "szary"   ],
  ["Samochodzik", "zabawka",  "zielony" ],
  ["Kochajek",    "maskotka", "śliwkowy"],
  ["Piłka",       "zabawka",  "w paćki" ],
  ["Bąk",         "zabawka",  "czerwony"],
]

# dwie grupy zabawek
maskotki  = []
pozostale = []

# przechodzimy zabawka po zabawce, żeby
# podzielić je na dwie kategorie
for zabawka in pudlo:
  # pod lepszą nazwą zapiszemy sobie nazwę...
  nazwa = zabawka[0]
  # ...i typ każdej zabawki
  typ = zabawka[1]

  # dzielimy na dwie kategorie 
  if typ == 'maskotka':
    # zapisz nazwę zabawki na liście maskotek
    maskotki.append(nazwa)
  else:
    # zapisz nazwę zabawki na liście pozostałych
    pozostale.append(nazwa)


# ładnie wydrukuj nazwy maskotek...
print 'Maskotki: ' + ', '.join(maskotki)
# ...oraz tych pozostałych
print 'Pozostałe: ' + ', '.join(pozostale)

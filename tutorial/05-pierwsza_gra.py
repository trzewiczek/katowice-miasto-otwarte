# -*- coding: utf-8 -*-
# z biblioteki (modułu) random weź funkcję randint
# funkcja randint losuje liczbę losową z zakresu
# od x do y włączając obie liczby 
from random import randint

# definiujemy sobie listę różnych fajnych zabawek
zabawki = ["Miś", "Samochodzik", "Kotek", "Balonik",
           "Cymbałki", "Piłka", "Lisek"]

# definiujemy sobie różne odpowiedzi tatusia
# zarówno te na tak, jak i te na nie
tata_na_tak = ["Świetnie!", "Pysznie!", "Wyśmienicie!", "Znakomicie!"]
tata_na_nie = ["Ja też za nią nie przepadam", "Naprawdę? A to zaskoczenie"]

# zaczynamy zabawę
print "- Chodź, powiesz mi, które zabawki lubisz, a których nie."
print "- Dobrze, tatusi."

# wybieramy numerek zabawki pamiętając, że indeksy
# elementów w liście zaczynają się od zera, więc kończą
# się na numerze "liczba elementów na liście minus jeden"
losowanie = randint(0, len(zabawki)-1)
# i pokazujemy wylosowaną zabawkę
print "- O, " + zabawki[losowanie] + ". Lubisz tę zabawkę
# czekamy na odpowiedź od gracza
odpowiedz = raw_input()

# no i tak
if odpowiedz == 'Tak' or odpowiedz == 'tak':
    # wylosujemy sobie pozytywną odpowiedź tatusia
    losowanie = randint(0, len(tata_na_tak)-1)
    print "- " + tata_na_tak[losowanie]
elif odpowiedz == 'Nie' or odpowiedz == 'nie':
    # wylosujemy sobie negatywną odpowiedź tatusia
    losowanie = randint(0, len(tata_na_nie)-1)
    print "- " + tata_na_nie[losowanie]
else:
    print "- Chyba nie zrozumiałem, o co ci chodzi..."

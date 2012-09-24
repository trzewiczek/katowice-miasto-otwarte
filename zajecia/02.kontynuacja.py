# coding: utf-8

# tworzymy pięć teczek dla pięciu osób
# każda osoba opisana jest za pomocą takich atrybutów:
#   0 --> imię
#   1 --> nazwisko
#   2 --> wiek
#   3 --> lista imion dzieci
#   4 --> zawód
osoba1 = ['Jan'      , 'Kowalski'  , 23, ['Jasio']                         , 'Programista']
osoba2 = ['Anna'     , 'Nowak'     , 50, ['Kasia', 'Wiola']                , 'Programistka']
osoba3 = ['Stanisław', 'Wiśniewski', 54, []                                , 'Malarz']
osoba4 = ['Wioletta' , 'Hałas'     , 63, ['Zbigniew']                      , 'Wiolonczelistka']
osoba5 = ['Frania'   , 'Guzik'     , 28, ['Jagna', 'Magda', "Dorota"]      , 'Architektka']

# zbieramy wszystkie te osoby w jedną listę ziomów
ziomy = [ osoba1, osoba2, osoba3, osoba4, osoba5 ]

# przyjrzyjmy się każdemu ziomów
for ziomek in ziomy:
    # wyjmujemy sobie listę dzieci danego ziomka
    dzieci = ziomek[3]

    # jeśli dzieci więcej niż jedno, wypisz wszystkie ich imiona
    if len(dzieci) > 1:
        print "Niezły urodzaj: " + ", ".join(dzieci)
    # w przeciwnym razie, jeśli (elif) ma jedno dziecko, wypisz jego imię
    elif len(ziomek[3]) is 1:
        print "O masz dziecko: " + dzieci[0]
    # jeśli w ogóle nie ma dzieci, to powiedz, jak ma na nazwisko
    else:
        print "Kto nie ma dzieci? " + ziomek[1]

print '_' * 50

urodzaj = []
dwoje   = []
jedno   = []
zero    = []

for ziomek in ziomy:
    dzieci = len(ziomek[3])
    wiek   = ziomek[2]

    if dzieci > 2 and wiek < 30:
        urodzaj.append( ziomek )
    elif dzieci is 2:
        dwoje.append(ziomek)        
    elif dzieci is 1:
        jedno.append(ziomek)
    else:
        zero.append(ziomek)

posortowane = [ urodzaj, dwoje, jedno, zero ]

for grupa in posortowane:
    print "|" * 50

    for ziomek in grupa:
        print ziomek



print '_' * 50

for ziomek in ziomy:
    dzieci = ziomek[3]

    for dziecko in dzieci:
        if 'g' in dziecko:
            print ziomek[1] + ": " + dziecko
            

# coding: utf-8

osoba1 = ['Jan'      , 'Kowalski'  , 23, ['Jasio']                         , 'Programista']
osoba2 = ['Anna'     , 'Nowak'     , 50, ['Kasia', 'Wiola']                , 'Programistka']
osoba3 = ['Stanisław', 'Wiśniewski', 54, []                                , 'Malarz']
osoba4 = ['Wioletta' , 'Hałas'     , 63, ['Zbigniew']                      , 'Wiolonczelistka']
osoba5 = ['Frania'   , 'Guzik'     , 28, ['Jagna', 'Magda', "Dorota"]      , 'Architektka']

ziomy = [ osoba1, osoba2, osoba3, osoba4, osoba5 ]

for ziomek in ziomy:
    if len(ziomek[3]) > 1:
        print "Niezły urodzaj: " + str(ziomek[3])
    elif len(ziomek[3]) is 1:
        print "O masz dziecko: " + str(ziomek[3])
    else:
        print "Kto nie ma dzieci? " + str(ziomek[3])

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
            

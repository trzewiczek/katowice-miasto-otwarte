# -*- coding: utf-8 -*-

# Podziel pracowników na dwie grupy wiekowe:
# starzy --> 30+
# mlodzi --> <30
pracownicy = [
    {
        'imie': 'Anna',
        'nazwisko': 'Kowalska',
        'wiek': 23
    },
    {
        'imie': 'Marek',
        'nazwisko': 'Aureliusz',
        'wiek': 54
    },
    {
        'imie': 'Hermenegilda',
        'nazwisko': 'Hałas',
        'wiek': 39
    },
    {
        'imie': 'Tomasz',
        'nazwisko': 'Święty',
        'wiek': 36
    },
    {
        'imie': 'Jan',
        'nazwisko': 'Nowak',
        'wiek': 45
    },
    {
        'imie': 'Wanda',
        'nazwisko': 'Chotomska',
        'wiek': 98
    }
]

wiek_progowy       = 40
drugi_wiek_progowy = 30

wyniki = {
    'stary': [],
    'mlody': []
}

for osoba in pracownicy:
    # przesiewamy osoby
    if osoba['wiek'] > wiek_progowy:
        wyniki['stary'].append(osoba['nazwisko'])
    elif osoba['wiek'] > drugi_wiek_progowy:
        print "Hm...."
    else:
        wyniki['mlody'].append(osoba['nazwisko'])

    
for kluczyk in wyniki.keys():
    print kluczyk + ": " + ", ".join(wyniki[kluczyk])


print "*" * 50

for kluczyk in wyniki.keys():
    print kluczyk
    print wyniki[ kluczyk ]
    print " | ".join(wyniki[ kluczyk ])
    print "*" * 30


# -*- coding: utf-8 -*-
pracownicy = {
    'na_urlopie': [
        {
            'imie': "anna",
            'nazwisko': "kowal",
            'wiek': 23,
            'dzieci': ['Janek', 'Staszek']
        },
        {
            'imie': "jan",
            'nazwisko': "nowak",
            'wiek': 23,
            'dzieci': []
        }
    ],
    'w_robocie': [
        {
            'imie': 'staszek',
            'nazwisko': 'wisniewski',
            'wiek': 23,
            'dzieci': ['Franek']
        },
        {
            'imie': "tomek",
            'nazwisko': "hałas",
            'wiek': 23,
            'dzieci': []
        }
    ]
}

wyniki = {
    'ma_dzieci' : [],
    'bez_dzieci': []
}

wszystkie_grupy = pracownicy.keys()
print wszystkie_grupy
print ""

# dla tych na urlopie i tych w robocie
for grupa in wszystkie_grupy:

    # dla każdej osoby w tej grupie (na urlopie i w robocie)
    for ziomek in pracownicy[ grupa ]:

        # wypisz mi tę osobę
        print ziomek
        # wypisz mi czy ma dzieci, czy nie
        print len(ziomek['dzieci']) > 0

        # dodaj do wyników odpowiednio:
        # ma dzieci --> ma_dzieci
        # nie ma dzieci --> bez_dzieci
        if len(ziomek['dzieci']) > 0:
            wyniki['ma_dzieci'].append(ziomek['nazwisko'])
        else:
            wyniki['bez_dzieci'].append(ziomek['nazwisko'])

    print '-- KONIEC GRUPY --'

print wyniki
















'''
wynik = {
    'ma_dzieci': [
        {
            'nazwisko': 'Kowal',
            'urlop': True
        }
    ],
    'bez_dzieci': [
        {
            'nazwisko': 'Kowal',
            'urlop': True
        }
    ]
}
'''

# -*- coding: utf-8 -*-

# definiujemy listę naszych pracowników. Każdy pracownik 
# opisany jest za pomocą trzech atrybutów:
#   'imie'
#   'nazwisko'
#   'wiek'
# każdy atrybut to klucz w słowniku. Nasza lista
# pracowników to zatem lista słowników o kluczach
# 'imie', 'nazwisko', 'wiek'
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

# wyznaczamy dwa progi wiekowe 
prog_I  = 60
prog_II = 40

# przygotowujemy sobie trzy kubełki,
# za pomocą których podzielimy pracowników
# na trzy grupy statusu zawodowego
wyniki = {
    'przed_emerytura': [],
    'doswiadczeni'   : [],
    'mlodziaki'      : []
}

# przyjrzymy się każdemu z pracowników
# po kolei sprawdzając ile ma lat
for osoba in pracownicy:
    # szukamy osób najstarszych
    if osoba['wiek'] > prog_I:
        # i dokładamy ich nazwiska do kubełka 'przed_emerytura'
        wyniki['przed_emerytura'].append(osoba['nazwisko'])
    # jeśli to nie osoby najstarsze to sprawdźmy czy to nie
    # osoby z doświadczeniem 
    elif osoba['wiek'] > prog_II:
        # i dokładamy ich nazwiska do kubełka 'doswiadczeni'
        wyniki['doswiadczeni'].append(osoba['nazwisko'])
    # w przeciwnym razie to mlodzi pracownicy
    else:
        # więc dokładamy ich nazwiska do kubełka 'mlodziaki'
        wyniki['mlodziaki'].append(osoba['nazwisko'])

    
# kubełek po kubełku wypiszemy pogrupowane nazwiska na ekranie
for kluczyk in wyniki.keys():
    # nazwa kubełka: nazwisko1, nazwisko2, nazwisko3...
    print kluczyk + ": " + ", ".join(wyniki[kluczyk])



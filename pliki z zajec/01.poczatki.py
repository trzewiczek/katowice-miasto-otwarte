# coding: utf-8

# lista zabawek do zabawy
zabawki = ["Miś", "Wiewórka", "Kotek", "Lisek", "Krokodyl"]

print "- To, co? Bawimy się dalej maskotkami?"
print "- Taaaaak!!"

# dla każdej maskotki wśród tych zabawek
for maskotka in zabawki:
    print "- Proszę, oto następna zabawka"

    # jeśli nazwa tej maskotki zaczyna się od 'K', cieszymy się!
    if maskotka.startswith('K'):
        print "- Hurra: " + maskotka

    # w przeciwnym razie, jeśli (elif) nazwa zaczyna się od 'M', jest ok.
    elif maskotka.startswith('M'):
        print "- " + maskotka + ", niech będzie..."

    # w przeciwnym razie (else) nie podoba nam się taka maskotka
    else:
        print "- Łeeeee to tylko " + maskotka

    print "- Chcesz następną?"
    print "- Tak!"
    
# na koniec przykra konstatacja, że zabawki się skonczyły
print "- Ale już nie mam zabawek...."    
print "- Jak to?!"


## WYNIK DZIAŁANIA PROGRAMU
#
#  - To, co? Bawimy się dalej maskotkami?
#  - Taaaaak!!
#  - Proszę, oto następna zabawka
#  - Miś, niech będzie...
#  - Chcesz następną?
#  - Tak!
#  - Proszę, oto następna zabawka
#  - Łeeeee to tylko Wiewórka
#  - Chcesz następną?
#  - Tak!
#  - Proszę, oto następna zabawka
#  - Hurra: Kotek
#  - Chcesz następną?
#  - Tak!
#  - Proszę, oto następna zabawka
#  - Łeeeee to tylko Lisek
#  - Chcesz następną?
#  - Tak!
#  - Proszę, oto następna zabawka
#  - Hurra: Krokodyl
#  - Chcesz następną?
#  - Tak!
#  - Ale już nie mam zabawek....
#  - Jak to?!

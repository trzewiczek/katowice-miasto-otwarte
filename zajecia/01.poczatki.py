# coding: utf-8

zabawki = ["Miś", "Wiewórka", "Kotek", "Lisek", "Krokodyl"]

print "- To, co? Bawimy się dalej maskotkami?"
print "- Taaaaak!!"

for maskotka in zabawki:
    print "- Proszę, oto następna zabawka"
    if maskotka.startswith('K'):
        print "- Hurra: " + maskotka
    elif maskotka.startswith('M'):
        print "- " + maskotka + ", niech będzie..."
    else:
        print "- Łeeeee to tylko " + maskotka
    print "- Chcesz następną?"
    print "- Tak!"
    
print "- Ale już nie mam zabawek...."    
print "- Jak to?!"


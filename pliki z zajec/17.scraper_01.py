from bs4 import BeautifulSoup as bs
from urllib import urlopen

url = 'http://www.slaska.policja.gov.pl/staystyka-zdarzen/go:data:2012_01_%s/'

for licznik in range(1, 32):
    if licznik < 10:
        dzien = '0%s' % licznik
    else:
        dzien = licznik

    pejdz = urlopen(url % dzien).read()
    page  = bs(pejdz)

    staty = page.find_all('div', 'sRow')

    print "2012-01-%s" % dzien
    for element in staty:
        wartosc = element.text
        if wartosc[-1].isdigit():
            kategoria, liczba = element.text.rsplit(' ', 1)
            print "%3s: %s" % (liczba, kategoria)

    print '_' * 80

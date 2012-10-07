# -*- coding: utf-8 -*-
import json
from bs4 import BeautifulSoup as bs
from random import randint
from urllib import urlopen, quote

for i in range(50):
    print ''

zlosliwe = [u"Yahoo tam nie sięga", u"Tam nie ma pogody", u"Czyli gdzie?!"]

sejm_url = 'http://api.sejmometr.pl/poslowie'
sejm_list = json.loads(urlopen(sejm_url).read())

geo_url = 'http://where.yahooapis.com/geocode?q=%s&flags=J'
wea_url = 'http://weather.yahooapis.com/forecastrss?w=%s'

for posel in sejm_list[5:25]:
    posel_url = 'http://api.sejmometr.pl/posel/%s/info' % posel
    metryczka = json.loads(urlopen(posel_url).read())

    nazwisko = metryczka['nazwa']
    miejsce  = metryczka['miejsce_urodzenia']

    geo_data = json.loads(urlopen(geo_url % miejsce.encode('utf-8')).read())
    woeid    = geo_data['ResultSet']['Results'][0]['woeid']

    weather   = bs(urlopen(wea_url % woeid).read())
    condition = weather.find('yweather:condition')

    if condition:
        celcius = 5/9.0 * (float(condition['temp']) - 32)
        
        print '-' * 50
        print nazwisko
        print miejsce
        print condition['date']
        print "Temp: %2.0f°C, %s" % (celcius, condition['text'])
        print '-' * 50
        print ''
    else:
        print '-' * 50
        print u"%s mieszka w miejscowości %s." % (nazwisko, miejsce)
        print zlosliwe[randint(0, len(zlosliwe)-1)]
        print '-' * 50
        print ''

from urllib import urlopen
import json

host   = 'http://pl.wikipedia.org/w/api.php?'
params = 'action=query&srsearch=%s&list=search&format=json'


haslo = raw_input("Czego szukamy? ")

url = host + (params % haslo)
print url

strona = urlopen(url).read()
dane = json.loads(strona)

#print dane['query']

print "!!! Znalazłem %s stron" % dane['query']['searchinfo']['totalhits']
for wynik in dane['query']['search']:
    if wynik['wordcount']> 500:
        print ">>> %s" % wynik['title']

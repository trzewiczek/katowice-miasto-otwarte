from urllib import urlopen
import json

url = 'http://api.sejmometr.pl/poslowie'

data = json.loads(urlopen(url).read())

zawody = {}

for posel in data[:5]:
    posel_url = 'http://api.sejmometr.pl/posel/%s/info' % posel
    metryczka = json.loads(urlopen(posel_url).read())

    zawod    = metryczka['pkw_zawod']
    osoba = {
        'id'      : metryczka['id'],
        'nazwisko': metryczka['nazwa']
    }

    zawody.setdefault(zawod, [])
    zawody[zawod].append(osoba)
    
    print metryczka['id']

print len(zawody.keys())
for zz in zawody.keys():
    print "%5s: %s" % (len(zawody[zz]), zz)


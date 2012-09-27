napis = open('tekst.txt').read()

histo = {}
for litera in napis:
    histo[ litera ] = histo.get( litera, 0 ) + 1

print histo

for literka in histo.keys():
    print literka + ": " + ('|' * histo[ literka ])


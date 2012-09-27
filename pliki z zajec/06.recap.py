import csv

czytnik = csv.reader(open('czyste_dane.csv'), delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

tabelka = []
for wiersz in czytnik:
    tabelka.append( wiersz )

maks = tabelka[1][1]
mini = tabelka[1][1]

for wiersz in tabelka[1:]:
    if wiersz[1] > maks:
        maks = wiersz[1]

    if wiersz[1] < mini:
        mini = wiersz[1]

        
print "Maks dla jedzenia to: " + str(maks)
print "Mini dla jedzenia to: " + str(mini)        


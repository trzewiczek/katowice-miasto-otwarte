import cclab
import math

tabelka = cclab.Table('czyste_dane.csv', header=True)

for wiersz in tabelka.rows(as_dict=True):
    if wiersz['Meat Price Index'] > wiersz['Sugar Price Index']:
        ilosc = int( abs(math.sin( wiersz['Sugar Price Index'] )) * 100 )
        print wiersz['Date'] + ": " + ("|" * ilosc)


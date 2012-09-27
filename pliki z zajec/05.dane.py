dane = open('dane.csv').readlines()

header = dane[0].strip().split(',')
data = []

for wiersz in dane[1:]:
    data.append( wiersz.strip().replace('"', '').split(',') )

tabela = []

for row in data:
    tmp = {}
    
    for head, cell in zip(header, row):
        h = head.replace('"', '')
        tmp[ h ] = cell.replace('"', '')

    tabela.append( tmp )

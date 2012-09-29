# coding: utf-8
print "--- Uwaga: lista list, czyli lista z listami w roli elementów"
print "--- Deklarujemy listę list, czyli pudło z zabawkami, przy czym"
print "--- każda zabawka opisana jest nie tylko nazwą, ale też typem"
print "--- i kolorem. Można powiedzieć, że w pudle mamy zabawki, a"
print "--- każda zabawka to lista jej atrybutów"
print '>>> pudlo = ['
print '        ["Miś", "maskotka", "szary"],'
print '        ["Samochodzik", "zabawka", "czerwony"],'
print '        ["Kochajek", "maskotka", "śliwkowy"],'
print '        ["Piłka", "zabawka", "w paćki"]'
print '    ]'

# deklarujemy listę list
pudlo = [
  ["Miś", "maskotka", "szary"],
  ["Samochodzik", "zabawka", "czerwony"],
  ["Kochajek", "maskotka", "śliwkowy"],
  ["Piłka", "zabawka", "w paćki"]
]

print ""
print "--- Przejedźmy się po tej liście list pętlą, a poniżej"
print "--- przyjrzymy się temu, co się stało krok po kroku"
print '>>> for zabawka in pudlo:'
print '        print zabawka[0] + " " + zabawka[2]'

# drukujemy nazwę i kolor każdej zabawki
for zabawka in pudlo:
  print zabawka[0] + " " + zabawka[2]

print ""
print "--- Zaglądamy do listy list krok po kroku"
print "--- Pierwszy element w pudle2 to lista opisująca misia:"
print ">>> print pudlo[0]"
print pudlo[0]
print ""
print "--- Skoro pierwszy element to lista, to wydrukujmy go"
print "--- ładnie za pomocą łączenia elementów listy pałeczkami:"
print '>>> print " | ".join(pudlo[0])'
print " | ".join(pudlo[0])
print ""
print "--- I idąc dalej, skoro pudlo[0] to lista atrybutów misia"
print "--- to możemy zajrzeć do pierwszego elementu za pomocą"
print "--- normalnego indeksu zerowego [0]. Nazwa misia to:"
print ">>> print pudlo[0][0]"
print pudlo[0][0]
print ""
print "--- Moglibyśmy powyższy przykład napisać w takich krokach:"
print "---   print pudlo[0][0]"
print "---   daje nam:"
print '---   print ["Miś", "maskotka", "szary"][0]'
print "---   daje nam:"
print '---   print "Miś"'
print "---   daje nam:"
print "Miś"
print ""
print "--- Pod indeksem 1 (druga pozycja na liście) w pudle"
print "--- znajduje się lista atrybutów drugiej zabawki. Zobaczmy:"
print ">>> print pudlo[1]"
print pudlo[1]
print ""
print "--- Czyli możemy z tej listy wyjąć nazwę zabawki odwołując"
print "--- się do indeksu 0 tej wydobytej z pudla listy:"
print ">>> print pudlo[1][0]"
print pudlo[1][0]
print ""
print "--- W ten sposób możemy wydobywać różne informacje z list list"
print "--- Np. nazwę zabawki i jej kolor"
print '>>> print pudlo[0][0] + " " + pudlo[0][2]'
print pudlo[0][0] + " " + pudlo[0][2]
print '>>> print pudlo[1][0] + " " + pudlo[1][2]'
print pudlo[1][0] + " " + pudlo[1][2]
print '>>> print pudlo[2][0] + " " + pudlo[2][2]'
print pudlo[2][0] + " " + pudlo[2][2]
print '>>> print pudlo[3][0] + " " + pudlo[3][2]'
print pudlo[3][0] + " " + pudlo[3][2]
print ""
print "--- Jak widać z powyższego przykładu przepis korzystania"
print "--- z list w listach jest taki sam dla każdej zabawki"
print "--- czyli możemy zrobić to w pętli podmieniając każdorazowo"
print "--- pudlo[X] tymczasową nazwą, np. zabawka"
print '>>> for zabawka in pudlo:'
print '        print zabawka[0] + " " + zabawka[2]'
for zabawka in pudlo:
  print zabawka[0] + " " + zabawka[2]

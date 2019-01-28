import re

Töne = ["c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "h"]
Tonal = ["dur", "moll"]
def durdreiklang(x):
    print(Töne[x] + " " + Töne[x+4] + " " + Töne[x+7])
def molldreiklang(x):
    print(Töne[x] + " " + Töne[x+3] + " " + Töne[x+7])

eingabe = input()
liste = re.split("I", eingabe)
eingabeGrundton = liste[0]
eingabeTonalitaet = liste[1]

for e in Töne:
    if e == eingabeGrundton:
        global Grundton
        Grundton = Töne.index(e)
        break
    else:
        pass

for e in Tonal:
    if e == eingabeTonalitaet:
        global Tonalitaet
        Tonalitaet = Tonal.index(e)
        break
    else:
        pass

if Tonalitaet == 0:
    print(durdreiklang(Grundton))
else:
    print(molldreiklang(Grundton))
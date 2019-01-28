import re

Töne = ["c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "h"]
TöneEX = ["C","Cis","D","Dis", "E", "F","Fis","G","Gis","A","Ais","H","B","c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "h", "c'" , "cis'", "d'", "dis'", "e'", "f'", "fis'", "g'", "gis'", "a'", "ais'", "h'"]
Tonal = ["dur", "moll"]
def Prime(x):
    return x
def kleineSekunde(x):
    return x + 1
def großeSekunde(x):
    return x + 2
def kleineTerz(x):
    return x + 3
def großeTerz(x):
    return x + 4
def reineQuarte(x):
    return x + 5
def übermäßigeQuarte(x):
    return x + 6
def verminderteQuinte(x):
    return x + 6
def reineQuinte(x):
    return x + 7
def kleineSexte(x):
    return x + 8
def großeSexte(x):
    return x + 9
def kleineSeptime(x):
    return x + 10
def großeSeptime(x):
    return x + 11
def reineOktave(x):
    return x + 12
def durdreiklang(x):
    print(Töne[x] + " " + Töne[großeTerz(x)] + " " + Töne[reineQuarte(x)])
def molldreiklang(x):
    print(Töne[x] + " " + Töne[kleineTerz(x)] + " " + Töne[reineQuinte(x)])
def Dominantseptakkord(x):
    durdreiklang(x)
    print(Töne[kleineSeptime(x)])
def großerSeptakkord(x):
    durdreiklang(x)
    print(großeSeptime(x))
def Mollseptakkord(x):
    molldreiklang(x)
    print(Töne[kleineSeptime(x)])
def Mollseptakkord_mit_großerSeptime(x):
    molldreiklang(x)
    print(Töne[großeSeptime(x)])

userinput = input("Grundton Tonalität")
liste = re.split(" ", userinput)
eingabeGrundton = liste[0]
eingabeTonalität = liste[1]

for e in Töne:
    if e == eingabeGrundton:
        global Grundton
        Grundton = Töne.index(e)
        break
    else:
        pass

for e in Tonal:
    if e == eingabeTonalität:
        global Tonalität
        Tonalität = Tonal.index(e)
        break
    else:
        pass

if Tonalität == 0:
    print(durdreiklang(Grundton))
elif Tonalität == 1:
    print(molldreiklang(Grundton))
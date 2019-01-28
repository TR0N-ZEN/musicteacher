import re

Töne = ["C","Cis","D","Dis", "E", "F","Fis","G","Gis","A","Ais","H","B","c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "h", "c'" , "cis'", "d'", "dis'", "e'", "f'", "fis'", "g'", "gis'", "a'", "ais'", "h'"]
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
    return(Töne[x] + " " + Töne[großeTerz(x)] + " " + Töne[reineQuarte(x)])
def molldreiklang(x):
    return(Töne[x] + " " + Töne[kleineTerz(x)] + " " + Töne[reineQuinte(x)])
def Dominantseptakkord(x):
    return durdreiklang(x) + " " + Töne[kleineSeptime(x)]
def großerSeptakkord(x):
    return durdreiklang(x) + " " + großeSeptime(x)
def Mollseptakkord(x):
    return molldreiklang(x) + " " + Töne[kleineSeptime(x)]
def Mollseptakkord_mit_großerSeptime(x):
    return molldreiklang(x) + " " + Töne[großeSeptime(x)]

userinput = input("Grundton Tonalität")
liste = re.split(" ", userinput)
eingabeGrundton = liste[0]
eingabeTonalität = liste[1]

if eingabeGrundton in Töne:
    Grundton = eingabeGrundton
else:
    print("Tonname falsch")

if eingabeTonalität in Tonal:
    Tonalität = eingabeTonalität
else:
    print("eigegebene Tonalität falsch")

if Tonalität == "dur":
    print(durdreiklang(Grundton))
elif Tonalität == "moll":
    print(molldreiklang(Grundton))
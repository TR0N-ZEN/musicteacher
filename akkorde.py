import re

Töne = ["C","Cis","D","Dis", "E", "F","Fis","G","Gis","A","Ais","H","B","c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "h", "c'" , "cis'", "d'", "dis'", "e'", "f'", "fis'", "g'", "gis'", "a'", "ais'", "h'"]
Tonalitäten = ["dur", "moll"]

##################################################
#INTERVALLE#
##################################################
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

##################################################
#AKKORDE#
##################################################
def durdreiklang(x):
    return Töne[x] + " " + Töne[großeTerz(x)] + " " + Töne[reineQuinte(x)]
def molldreiklang(x):
    return Töne[x] + " " + Töne[kleineTerz(x)] + " " + Töne[reineQuinte(x)]
def Dominantseptakkord(x):
    return durdreiklang(x) + " " + Töne[kleineSeptime(x)]
def großerSeptakkord(x):
    return durdreiklang(x) + " " + Töne[großeSeptime(x)]
def Mollseptakkord(x):
    return molldreiklang(x) + " " + Töne[kleineSeptime(x)]
def Mollseptakkord_mit_großerSeptime(x):
    return molldreiklang(x) + " " + Töne[großeSeptime(x)]

userinput = input("Eingabeformatierungsbeispiele: \n 'c moll' oder 'c dur 7' oder 'c dur maj7' \n")
liste = re.split(" ", userinput)
eingabeGrundton = liste[0]
eingabeTonalität = liste[1]
eingabeVierterTon = liste[2]

if eingabeGrundton in Töne:
    Grundtonindex = Töne.index(eingabeGrundton)
    if eingabeTonalität in Tonalitäten:
        Tonalitätsindex = Tonalitäten.index(eingabeTonalität)
        if Tonalitätsindex == Tonalitäten.index("dur"):
            print(durdreiklang(Grundtonindex))
        elif Tonalitätsindex == Tonalitäten.index("moll"):
            print(molldreiklang(Grundtonindex))
    else:
        print("eingegebene Tonalität nicht gültig")
elif len(eingabeGrundton) == 2:
    for i in Töne:
        if eingabeGrundton == i + "7":
            print(Dominantseptakkord(Töne.index(eingabeGrundton[0])))
        # elif eingabeGrundton == i + "5":
        # elif eingabeGrundton == i + "4":
        # elif eingabeGrundton == i + "3":
        # elif eingabeGrundton == i + "9":
# elif len(eingabeGrundton) == 5:
#     if eingabeGrundton == i + maj + "7":
else:
    print("Tonname nicht gültig")
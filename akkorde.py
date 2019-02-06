import re

Töne = ["C","Cis","D","Dis", "E", "F","Fis","G","Gis","A","Ais","H","B","c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "h", "c'" , "cis'", "d'", "dis'", "e'", "f'", "fis'", "g'", "gis'", "a'", "ais'", "h'"]
Tonalitäten = ["dur", "moll"]
vierterTon = ["3", "4", "5", "7b5", "7", "maj7", "9"]

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
def verminderteQuarte(x):
    return x + 4 
def reineQuarte(x):
    return x + 5
def übermäßigeQuarte(x):
    return x + 6
def verminderteQuinte(x):
    return x + 6
def reineQuinte(x):
    return x + 7
def übermäßigeQuinte(x):
    return x + 8
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
def verminderterdreiklang(x):
    return Töne[x] + " " + Töne[kleineTerz(x)] + " " Töne[verminderteQuinte(x)]
def übermäßigerdreiklang(x):
    return Töne[x] + " " + Töne[großeTerz(x)] + " " + Töne[übermäßigeQuinte(x)]
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
else:
    print("Tonname nicht gültig")
if eingabeTonalität in Tonalitäten:
    Tonalitätesindex = Tonalitäten.index(Tonalitäten)
else:
    print("Tonalitätenname nicht gültig")
if eingabeVierterTon in vierterTon:
    vierterTonindex = vierterTon.index(eingabeVierterTon)

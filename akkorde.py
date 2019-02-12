import re
import tones
import intervals



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
eingabeextensions = liste[2]

if eingabeGrundton in Töne: 
    Grundtonindex = Töne.index(eingabeGrundton)
else:
    print("Tonname nicht gültig")
if eingabeTonalität in Tonalitäten:
    Tonalitätesindex = Tonalitäten.index(Tonalitäten)
else:
    print("Tonalitätenname nicht gültig")

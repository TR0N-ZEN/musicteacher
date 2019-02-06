import re
import tones
import intervals


##################################################
#INTERVALLE#
##################################################


#######################################
#Intervall dictonary
#######################################
x = 0
i = { 
    "1": Prime(x),
    "b2": kleineSekunde(x),
    "2": großeSekunde(x),
    "b3": kleineTerz(x),
    "3": großeTerz(x),
    "4": reineQuarte(x),
    "5": reineQuinte(x),
    "b6": kleineSexte(x),
    "6": großeSexte(x),
    "b7": kleineSeptime(x),
    "7": kleineSeptime(x),
    "8": reineOktave(x)
}

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

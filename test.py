someList = [5, 2, "a"]
if "a" or "b" or "c" in "helloc":
    print("found")

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
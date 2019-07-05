import chords

tones = ["C", "Cis", "D", "Dis", "E", "F", "Fis", "G", "Gis", "A", "Ais", "B", "c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b", "c'" , "cis'", "d'", "dis'", "e'", "f'", "fis'", "g'", "gis'", "a'", "ais'", "b'"]

root = input("Type a root: ")
rootinteger = tones.index(root)

print("\t\t" + tones[rootinteger + 0] + "\t" + tones[rootinteger + 1]+ "\n")
print("\t" + tones[rootinteger + 11] + "\t\t\t" + tones[rootinteger + 2]+ "\n")
print(tones[rootinteger + 10] + "\t\t\t\t\t" + tones[rootinteger + 3]+ "\n")
print(tones[rootinteger + 9] + "\t\t\t\t\t" + tones[rootinteger + 4]+ "\n")
print("\t" + tones[rootinteger + 8] + "\t\t\t" + tones[rootinteger + 5]+ "\n")
print("\t\t" + tones[rootinteger + 7] + "\t" + tones[rootinteger + 6])


i = input("\nready\n")


print("\t\t" + tones[rootinteger + 0] + "\t" + tones[rootinteger + 1]+ "\n")
print("\t" + tones[rootinteger + 11] + "\t\t\t" + tones[rootinteger + 2]+ "\n")
print(tones[rootinteger + 10] + "\t\t\t\t\t" + tones[rootinteger + 3]+ "\n")
print("--------------------------------------------")
print(tones[rootinteger + 9] + "\t\t\t\t\t" + tones[rootinteger + 4]+ "\n")
print("\t" + tones[rootinteger + 8] + "\t\t\t" + tones[rootinteger + 5]+ "\n")
print("\t\t" + tones[rootinteger + 7] + "\t" + tones[rootinteger + 6])

print("\nWe draw a horizontal axis between the tones which are two and three halfsteps before the root and three and four halfsteps after the root respectively.")


i = input("\nready\n")


print("\t\t" + tones[rootinteger + 0] + "\t" + tones[rootinteger + 1]+ "\n\t\t|\t|")
print("\t" + tones[rootinteger + 11] + "\t|\t|\t" + tones[rootinteger + 2]+ "\n\t|\t|\t|\t|")
print(tones[rootinteger + 10] + "\t|\t|\t|\t|\t" + tones[rootinteger + 3])
print("|-------|-------|-------|-------|-------|")
print(tones[rootinteger + 9] + "\t|\t|\t|\t|\t" + tones[rootinteger + 4]+ "\n\t|\t|\t|\t|")
print("\t" + tones[rootinteger + 8] + "\t|\t|\t" + tones[rootinteger + 5]+ "\n\t\t|\t|")
print("\t\t" + tones[rootinteger + 7] + "\t" + tones[rootinteger + 6])

print("Each tone is connected to another tone. Connected tones are exchangable.\nThis means you have totally different chords for your backing.")


i = input("\nready\n")


print("Lets take the chord on the tonic you chose (" + tones[rootinteger] + ") in a major heptatonic scale.\nWhich is " + tones[rootinteger] + " major.\n")

def translator(tupleofintegers): # translates index number to according tones in the list named tones
    # listoftonesrequested = []
    for e in tupleofintegers:
        print(tones[e])
        # listoftonesrequested.append(tones[e])
    # return list listoftonesrequested

translator(chords.major(rootinteger))

print("\nNow think of the negative tones of the chord you would get.\n") 
print(tones[rootinteger + 7])
print(tones[rootinteger + 3])
print(tones[rootinteger])
print("\n It is just an inversion of " + tones[rootinteger] + " minor.")
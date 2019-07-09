import  chords

tones = ["C", "Cis", "D", "Dis", "E", "F", "Fis", "G", "Gis", "A", "Ais", "B", "c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b", "c'" , "cis'", "d'", "dis'", "e'", "f'", "fis'", "g'", "gis'", "a'", "ais'", "b'"]

def translator(tupleofintegers): # translates index number to according tones in the list named tones
    # listoftonesrequested = []
    for e in tupleofintegers:
        print(tones[e])
        # listoftonesrequested.append(tones[e])
    # return list listoftonesrequested

root = input("Type a root: ")
rootinteger = tones.index(root)

ic = {
    0: 7,
    1: 6,
    2: 5,
    3: 4,
    4: 3,
    5: 2,
    6: 1,
    7: 0,
    8: 11,
    9: 10
}

chords.major(rootinteger)


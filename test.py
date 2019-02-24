tones = ["C", "Cis", "D", "Dis", "E", "F", "Fis", "G", "Gis", "A", "Ais", "H", "c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "h", "c'" , "cis'", "d'", "dis'", "e'", "f'", "fis'", "g'", "gis'", "a'", "ais'", "h'"]

def major_scale(x):
    return x, x+2, x+4, x+5, x+7, x+9, x+11, x+12

i = input()
rootinteger = tones.index(i)
for e in major_scale(rootinteger):
    print(tones[e])
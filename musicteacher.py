import os

tones = ["C", "Cis", "D", "Dis", "E", "F", "Fis", "G", "Gis", "A", "Ais", "B", "c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b", "c'" , "cis'", "d'", "dis'", "e'", "f'", "fis'", "g'", "gis'", "a'", "ais'", "b'"]
tonalities = ["dur", "moll"]
extension = ["1", "b2", "2", "b3", "3", "4", "5", "b6", "6", "b7", "7", "8"]

#intervals
def prime(x):
    return x
def minor_second(x):
    return x + 1
def major_second(x):
    return x + 2
def minor_fourth(x):
    return x + 3
def major_third(x):
    return x + 4
def diminished_fourth(x):
    return x + 4 
def perfect_fourth(x):
    return x + 5
def augmented_fourth(x):
    return x + 6
def diminished_fifth(x):
    return x + 6
def perfect_fifth(x):
    return x + 7
def augmented_fifth(x):
    return x + 8
def minor_sixth(x):
    return x + 8
def major_sixth(x):
    return x + 9
def minor_seventh(x):
    return x + 10
def major_seventh(x):
    return x + 11
def perfect_eighth(x):
    return x + 12

#scales
def major_scale(x):
    return x, x+2, x+4, x+5, x+7, x+9, x+11, x+12
def natural_minor_scale(x):
    return x, x+2, x+3, x+5, x+7, x+8, x+10, x+12
def harmonic_minor_scale(x):
    return x, x+2, x+3, x+5, x+7, x+8, x+11, x+12
def melodic_minor_scale(x):
    return x, x+2, x+3, x+5, x+7, x+9, x+11, x+12

# class scales:
#     def __init__(self, x):
#         self.major(x) = [x, (x+2), (x+4), (x+5), (x+7), (x+9), (x+11), (x+12)]
#         self.natural_minor(x) = [x, x+2, x+3, x+5, x+6, x+8, x+10 , x+12]
#         self.harmonic_minor(x) =  [x, x+2, x+3, x+5, x+6, x+8, x+11 , x+12]


#chords
def major_chord(x):
    return x, x+4, x+7
def minor_chord(x):
    return x, x+3, x+7
def augmented_chord(x):
    return x, x+4, x+8
def diminished_chord(x):
    return x, x+3, x+6

def intervals_interactice():
    i1 = input("Type in the first tone: ")
    i2 = input("Type in the second tone: ")
    first_tone_int = tones.index(i1)
    second_tone_int = tones.index(i2)
    difference = second_tone_int - first_tone_int
    if difference > 12:
        difference = difference % 12
    intervals = {
        0 : "prime",
        1 : "minor second",
        2 : "major second",
        3 : "minor third",
        4 : "major third",
        5 : "perferct fourth",
        6 : "augmented fourth / diminished fifth / tri-tonus",
        7 : "perfect fifth",
        8 : "minor sixth",
        9 : "major sixth",
        10 : "minor seventh",
        11 : "major seventh",
        12 : "perfect eighth"
    }
    print(intervals[difference])

def scales_heptatonics():
    ri = input("You can now enter a root and get the tones of its later queried scale.\n root: ")
    rootinteger = tones.index(ri)
    si = input("Input a scale type: ")
    if si.find("major")!=-1:
        for e in major_scale(rootinteger):
            print(tones[e])
    if si.find("natural minor")!=-1:
        for e in natural_minor_scale(rootinteger):
            print(tones[e])
    if si.find("harmonic minor")!=-1:
        for e in harmonic_minor_scale(rootinteger):
            print(tones[e])
    if si.find("melodic minor")!=-1:
        for e in melodic_minor_scale(rootinteger):
            print(tones[e])

def wholetone_pentatonic(r,count):
        if r - legacy > 12:
            r = r - 12
        print(tones[perfect_fifth(r)])
        if count < 3:
            count = count + 1
            wholetone_pentatonic(perfect_fifth(r),count)
        count = 0

def scales_pentatonics():
    ri = input("You can now enter a root and get the tones of its pentatonic scale.\n root: ")
    rootinteger = tones.index(ri)
    global legacy
    legacy = rootinteger
    wholetone_pentatonic(rootinteger, 0)

def chords_interactice():
    i = input("You can now enter a root and get the tones of its later queried chord.\n root: ")
    o = input("Enter chord type: ")
    rootinteger = tones.index(i)
    if o.find("diminished") != -1:
        c = diminished_chord(rootinteger)
    elif o.find("augmented") != -1:
        c = augmented_chord(rootinteger)
    elif o.find("major") != -1:
        c = major_chord(rootinteger)
    elif o.find("minor") != -1:    
        c = minor_chord(rootinteger)
    for e in c:
        print(tones[e])

def lesson_text(origin):
    textobject = open(origin ,"r")
    text = textobject.read()
    print(text + "\n")

print("What do you want to do \noptions are: \n 1 tones\n 2 intervals\n 3 scales\n 4 chords\n ")
i = input("please enter the accoring number: ")
if i == "1":
    lesson_text("tones_lesson.txt")
elif i == "2":
    lesson_text("intervals_lesson.txt")
    intervals_interactice()
elif i == "3":
    lesson_text("scales.txt")
    i = input(" 1 heptatonics\n 2 pentatonics\n")
    if i == "1":
        lesson_text("scales_heptatonics.txt")
        scales_heptatonics()
    elif i == "2":
        lesson_text("scales_pentatonics.txt")
        scales_pentatonics()
elif i == "4":
    lesson_text("chords_lesson.txt")
    chords_interactice()

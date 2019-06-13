import os
import intervals
import scales
import chords
from instruments import guitar

tones = ["C", "Cis", "D", "Dis", "E", "F", "Fis", "G", "Gis", "A", "Ais", "B", "c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b", "c'" , "cis'", "d'", "dis'", "e'", "f'", "fis'", "g'", "gis'", "a'", "ais'", "b'"]
tonalities = ["minor", "major"]
extension = ["1", "b2", "2", "b3", "3", "4", "5", "b6", "6", "b7", "7", "8"]

def translator(tupleofintegers): # translates index number to according tones in the list named tones
    # listoftonesrequested = []
    for e in tupleofintegers:
        print(tones[e])
        # listoftonesrequested.append(tones[e])
    # return list listoftonesrequested

def intervals_interactive():
    i1 = input("Type in the first tone: ")
    i2 = input("Type in the second tone: ")
    first_tone_int = tones.index(i1)
    second_tone_int = tones.index(i2)
    difference = second_tone_int - first_tone_int
    if difference > 12:
        octaves = difference / 12
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
    print(str(octaves) + "octaves plus" +  intervals[difference])

def heptatonics():
    root = input("You can now enter a root and get the tones of its later queried scale.\n root: ")
    rootinteger = tones.index(root)
    scaletype = input("Input a scale type: ")
    scale_dicto = {
        "major": scales.heptatonics().major(rootinteger),
        "natural minor": scales.heptatonics().natural_minor(rootinteger),
        "harmonic minor": scales.heptatonics().harmonic_minor(rootinteger),
        "melodic minor": scales.heptatonics().melodic_minor(rootinteger)
    }
    translator(scale_dicto.get(scaletype))

def pentatonics():
    root = input("You can now enter a root and get the tones of its later queried scale.\n root: ")
    rootinteger = tones.index(root)
    scaletype = input("Input a scale type (\"major\" or \"minor\"): ")
    scale_dicto = {
        "major": scales.pentatonics().major(rootinteger),
        "minor": scales.pentatonics().minor(rootinteger)
    }
    translator(scale_dicto.get(scaletype))
    i = input("\nWanna get the patter for guitar? y/n")
    if i == "y":
        guitar.pattern(scale_dicto.get(scaletype))

def chords_interactive():
    root = input("You can now enter a root and get the tones of its later queried chord.\n root: ")
    chord_type = input("Enter chord type: ")
    rootinteger = tones.index(root)
    dicto = {
        "diminished": chords.diminished(rootinteger),
        "augmented": chords.augmented(rootinteger),
        "major": chords.major(rootinteger),
        "minor": chords.minor(rootinteger)
    }
    translator(dicto.get(chord_type))

def lesson_text(origin):
    textobject = open(origin ,"r")
    text = textobject.read()
    print(text + "\n")

# def wait():
#     c = input(" 1 heptatonics\n 2 pentatonics\n\n")
#     if c == "1":
#         lesson_text("scales_heptatonics.txt")
#         heptatonics()
#     elif c == "2":
#         lesson_text("scales_pentatonics.txt")
#         pentatonics()

# print("What do you want to do \noptions are: \n 1 tones\n 2 intervals\n 3 scales\n 4 chords\n ")
# i = input("please enter the accoring number: ")
# decision_dicto = {
#     "1": lesson_text("tones_lesson.txt"), 
#     "2": lesson_text("intervals_lesson.txt") and intervals_interactive(),
#     "3": lesson_text("scales.txt") and wait(),
#     "4": lesson_text("chords_lesson.txt") and chords_interactive() 
# }

print("What do you want to do \noptions are: \n 1 tones\n 2 intervals\n 3 scales\n 4 chords\n ")
i = input("please enter the accoring number: ")
if i == "1":
    lesson_text("tones_lesson.txt")
elif i == "2":
    lesson_text("intervals_lesson.txt")
    intervals_interactive()
elif i == "3":
    lesson_text("scales_lesson.txt")
    i = input(" 1 heptatonics\n 2 pentatonics\n\n")
    if i == "1":
        lesson_text("scales_heptatonics.txt")
        heptatonics()
    elif i == "2":
        lesson_text("scales_pentatonics.txt")
        pentatonics()
elif i == "4":
    lesson_text("chords_lesson.txt")
    chords_interactive()
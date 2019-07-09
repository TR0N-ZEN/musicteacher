import os
import intervals
import scales
import chords
import harmony
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


def melody_interactive():
    root = input("Type a root: ")
    rootinteger = tones.index(root)
    scaletypes = {
        1: scales.heptatonics().major(rootinteger),
        2: scales.heptatonics().natural_minor(rootinteger),
        3: scales.heptatonics().harmonic_minor(rootinteger),
        4: scales.heptatonics().melodic_minor(rootinteger),
        5: scales.pentatonics().major(rootinteger),
        6: scales.pentatonics().minor(rootinteger)
    }
    scaletype = input("\t1 - heptatonics major\n\t2 - heptatonics natural minor\n\t3 - hepatonics harmonic minor\n\t4 - heptatonics melodic minor\n\t5 - pentatonics major\n\t6 - pentatonics minor\n\n")
    translator(scaletypes[scaletype])


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

def harmony_interactive():
    melody_interactive()

def lesson_text(origin):
    textobject = open(origin ,"r")
    text = textobject.read()
    print(text + "\n")


print("What do you want to do \noptions are: \n 1 tones\n 2 intervals\n 3 scales\n 4 chords\n ")
i = input("please enter the accoring number: ")
decision_dicto = {
    "1": lesson_text("tones_lesson.txt"), 
    "2": lesson_text("intervals_lesson.txt") and intervals_interactive(),
    "3": lesson_text("scales.txt") and melody_interactive(),
    "4": lesson_text("chords_lesson.txt") and chords_interactive(),
    "5": lesson_text("harmony_lesson.txt") and harmony_interactive()
}
import os

tones = ["C", "Cis", "D", "Dis", "E", "F", "Fis", "G", "Gis", "A", "Ais", "H", "c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "h", "c'" , "cis'", "d'", "dis'", "e'", "f'", "fis'", "g'", "gis'", "a'", "ais'", "h'"]
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

def lesson(origin):
    textobject = open(origin ,"r")
    text = textobject.read()
    print(text + "\n")

print("What do you want to do \noptions are: \n 1 - tones\n 2 - intervals\n 3 - scales\n 4 - chords ")
i = input("please enter the accoring number: ")
if i == "1":
    lesson("tones_lesson.txt")
elif i == "2":
    lesson("intervals_lesson.txt")
elif i == "3":
    lesson("scales_lesson.txt")
    i = input("You can now enter a root and get the tones of its scale.\n root: ")
    rootinteger = tones.index(i)
    for e in major_scale(rootinteger):
        print(tones[e])
elif i == "4":
    lesson("chords_lesson.txt")

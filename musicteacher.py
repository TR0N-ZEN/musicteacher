#import tone
#import intervals
#import scales

tones = ["C", "Cis", "D", "Dis", "E", "F", "Fis", "G", "Gis", "A", "Ais", "H", "B", "c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "h", "c'" , "cis'", "d'", "dis'", "e'", "f'", "fis'", "g'", "gis'", "a'", "ais'", "h'"]
tonalities = ["dur", "moll"]
extension = ["1", "b2", "2", "b3", "3", "4", "5", "b6", "6", "b7", "7", "8"]

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

####################################################
#or written in classes
####################################################

class perfect:
    def __init__(self, x, prime, fourth, fifth, eighth):
        self.prime = x
        self.fourth = x + 5
        self.fifth = x + 7
        self.eighth = x + 12
class major:
    def __init__(self, x, second, third, sixth, seventh):
        self.second  = x + 2
        self.third = x + 4
        self.sixth = x + 9
        self.seventh = x + 11
class minor:
    def __init__(self, x, second, third, sixth, seventh):
        self.second = x + 1
        self.third = x + 3
        self.sixth = x + 8
        self.seventh = x + 10
class augmented:
    def __init__(self, x, fourth, fifth):
        self.fourth = x + 6
        self.fifth = x + 8
class diminished:
    def __init__(self, x, fourth, fifth):
        self.fourth = x + 4
        self.fifth = x + 6
mydict:
def lesson(origin):
    textobject = open(origin,"r")
    text = textobject.read()
    print(text + "\n")

class scales:
    def __init__(self, x):
        self.major(x) = tones[x] + tones[x+2] + tones[x+4] + tones[x+5] + tones[x+7] + tones[x+9] + tones[x+11] + tones[x+12]
        # equivalent would be: 
        # return tones[prime(x)] + tones[major_second(x)] + tones[major_third(x)] + tones[perfect_fourth(x)] + tones[perfect_fifth(x)] + tones[major_sixth(x)] + tones[major_seventh(x)]
        # return tones[perfect.prime(x) + tones[major.second(x)] + tones[major.third(x)] + tones[perfect_fourth(x)] + tones[perfect.fifth(x)] + tones[major.sixth(x)] + tones[major.seventh(x)] + tones[perfect.eighth(x)]
        self.natural_minor(x) = tones[x] + tones[x+2] + tones[x+3] + tones[x+5] + tones[x+6] + tones[x+8] + tones[x+10] + tones[x+12]
        self.harmonic_minor(x) =  tones[x] + tones[x+2] + tones[x+3] + tones[x+5] + tones[x+6] + tones[x+8] + tones[x+11] + tones[x+12]

print("What do you want to do \noptions are: \n 1 - tones\n 2 - intervals\n 3 - scales ")
i = input("please enter the accoring number: ")

if i == "1":
    tone.lesson()
elif i == "2":
    intervals.lesson()
elif i == "3":
    
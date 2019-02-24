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

def lesson():
    textobject = open("intervals_lesson.txt","r")
    text = textobject.read()
    print(text + "\n")
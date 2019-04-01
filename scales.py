from intervals import *

tones = ["C", "Cis", "D", "Dis", "E", "F", "Fis", "G", "Gis", "A", "Ais", "B", "c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b", "c'" , "cis'", "d'", "dis'", "e'", "f'", "fis'", "g'", "gis'", "a'", "ais'", "b'"]

#scales
class heptatonics:
    def __init__(self):
        global count
        count = 0
    def major(self,x):
        if r - legacy > 12:
            r = r - 12
            print(tones[perfect_fifth(r)])
            if count < 5:
                count = count + 1
                heptatonics.major(self,perfect_fifth(r))
            count = 0
        # or
        # return x, x+2, x+4, x+5, x+7, x+9, x+11, x+12
    def natural_minor(self,x):
        return x, x+2, x+3, x+5, x+7, x+8, x+10, x+12
    def harmonic_minor(self,x):
        return x, x+2, x+3, x+5, x+7, x+8, x+11, x+12
    def melodic_minor(self,x):
        return x, x+2, x+3, x+5, x+7, x+9, x+11, x+12

class pentatonics:
    def __init__(self):
        global count
        count = 0
    def wholetone(self,x):
        if r - legacy > 12:
            r = r - 12
        print(tones[perfect_fifth(r)])
        if count < 3:
            count = count + 1
            pentatonics.wholetone(self,perfect_fifth(r))
        count = 0
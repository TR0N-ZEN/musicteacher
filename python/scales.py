#scales
class heptatonics:
    def __init__(self):
        global count
        count = 0
    def major(self,x):
        return x, x+2, x+4, x+5, x+7, x+9, x+11, x+12
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
    def major(self,x):
        return x, x+2, x+4, x+7, x+9
    def minor(self,x):
        return x, x+3, x+5, x+7, x+10
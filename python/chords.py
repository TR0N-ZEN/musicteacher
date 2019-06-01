#chords
def major(x):
    return x, x+4, x+7 # Grundton großeTerz Quinte
def minor(x):
    return x, x+3, x+7 # Grundton kleineTerz Quinte
def augmented(x): # x#5 oder x+
    return x, x+4, x+8 # Grundton großeTerz übermäßigeQuinte
def diminished(x): # auch x0 genannt, Bsp.: C0 -> C Es Ges
    return x, x+3, x+6 # Grundton kleineTerz vermidnerteQuinte
def major_sus4(x):
    return x, x+5, x+7 # Grundton + Quarte + Quinte
def powerchord_5(x):
    return x, x+7 # Grundton + Quinte
def major_6(x):
    return x, x+4, x+7, x+8 # major + kleineSexte
def minor_6(x):
    return x, x+3, x+7, x+8 # minor + kleineSexte
def major_7(x):
    return x, x+4, x+7, x+10 # major + kleineSeptime
def minor_7(x):
    return x, x+3, x+7, x+10 # minor + kleineSeptime
def major_maj7(x):
    return x, x+4, x+7, x+11 # major + großeSeptime
def minor_maj7(x):
    return x, x+3, x+7, x+11 # minor + großeSeptime
def minor_7_b5(x):
    return x, x+3, x+6, x+10
def major_sus4_7(x):
    return x, x+5, x+7, x+10
def major_7_hash5(x): # x+7, xaug
    return x, x+4, x+8, x+10
def diminished_7(x):
    return x, x+3, x+6, x+9

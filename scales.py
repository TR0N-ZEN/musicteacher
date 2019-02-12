from tones import tones

def dur(x):
    return  tones[x] + tones[x+2] + tones[x+4] + tones[x+5] + tones[x+7] + tones[x+9] + tones[x+11] + tones[x+12]
    # equivalent would be: return tones[prime(x)] + tones[major_second(x)] + tones[major_third(x)] + tones[perfect_fourth(x)] + tones[perfect_fifth(x)] + tones[major_sixth(x)] + tones[major_seventh(x)]

i = int(input("enter index number"))
print(dur(i))
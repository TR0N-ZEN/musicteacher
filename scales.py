from tone import tones
# import intervals

def dur(x):
    return  tones[x] + tones[x+2] + tones[x+4] + tones[x+5] + tones[x+7] + tones[x+9] + tones[x+11] + tones[x+12]
    # equivalent would be: 
    # return tones[prime(x)] + tones[major_second(x)] + tones[major_third(x)] + tones[perfect_fourth(x)] + tones[perfect_fifth(x)] + tones[major_sixth(x)] + tones[major_seventh(x)]
    # return tones[perfect.prime(x) + tones[major.second(x)] + tones[major.third(x)] + tones[perfect_fourth(x)] + tones[perfect.fifth(x)] + tones[major.sixth(x)] + tones[major.seventh(x)] + tones[perfect.eighth(x)]
def minor(x):
    return tones[x] + tones[x+2] + tones[x+3] + tones[x+5] + tones[x+7] + tones[x+8] + tones[x+10] + tones[x+12]

def lesson():
    textobject = open("intervals_lesson.txt","r")
    text = textobject.read()
    print(text)
    i = input("enter root")
    try:
        o = tones.index(i)
        print(i + "dur scale: " + dur(o))
        print(i + "minor scale: " + minor(o))
    except:
        print("fuckin dumbass type in a real root, u know a ground color, tonic keynote")

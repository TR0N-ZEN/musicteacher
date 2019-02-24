def lesson():
    textobject = open("intervals_lesson.txt","r")
    text = textobject.read()
    print(text)
    i = input("enter root")
    try:
        o = tones.index(i)
        print(dur(o))
    except:
        print("fuckin dumbass type in a real root, u know a ground color, tonic keynote")
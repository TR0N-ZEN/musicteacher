import tone
import intervals
import scales

print("What do you want to do \noptions are: \n 1 - tones\n 2 - intervals\n 3 - scales ")
i = input("please enter the accoring number: ")
if i == "1":
    tone.lesson()
elif i == "2":
    intervals.lesson()
elif i == "3":
    scales.lesson()

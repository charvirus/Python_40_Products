import tkinter
import tkinter.font
import random

lotto_num = range(1,46)

def buttonClick():
    for i in range(5):
        lottoPick = map(str,random.sample(lotto_num,6))
        lottoPick = ','.join(lottoPick)
        lottoPick = str(i+1) + "회 : "+lottoPick
        print(lottoPick)


buttonClick()

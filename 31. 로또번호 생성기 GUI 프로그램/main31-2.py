import tkinter
import tkinter.font
import random

lotto_num = range(1, 46)


def buttonClick():
    print(random.sample(lotto_num, 6))


window = tkinter.Tk()
window.title("Lotto")
window.geometry("400x200+800+300")
window.resizable(False, False)


button = tkinter.Button(window, overrelief="solid",text="번호 확인", width=15, command=buttonClick)
button.pack()

window.mainloop()
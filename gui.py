from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("400x200")
window.title("계산기")

window.config(padx=30, pady=30)

lbl_input_x = Label(window, text="Input X")
lbl_input_x.grid(column=0, row=0)
edt_input_x = Entry(window, width=12, borderwidth=1, relief="raised")
edt_input_x.grid(column=1, row=0, columnspan=2)

lbl_input_y = Label(window, text="Input Y")
lbl_input_y.grid(column=3, row=0)
edt_input_y = Entry(window, width=12, borderwidth=1, relief="raised")
edt_input_y.grid(column=4, row=0, columnspan=2)

lbl_operator = Label(window, text="Operator")
lbl_operator.grid(column=0, row=1, pady=20, columnspan=2)
btn_op_1 = Button(window, text="+", fg="blue", width=4)
btn_op_1.grid(column=2, row=1, padx=10, sticky=E)
btn_op_2 = Button(window, text="-", fg="blue", width=4)
btn_op_2.grid(column=3, row=1, padx=10, sticky=E)
btn_op_3 = Button(window, text="X", fg="blue", width=4)
btn_op_3.grid(column=4, row=1, padx=10, sticky=E)
btn_op_4 = Button(window, text="÷", fg="blue", width=4)
btn_op_4.grid(column=5, row=1, padx=10, sticky=E)

btn_exe = Button(window, text="실행", width=15)
btn_exe.grid(column=0, row=2, columnspan=6)

lbl_output = Label(window, text="Output")
lbl_output.grid(column=0, row=3, pady=10, columnspan=2)
lbl_result = Label(window, text="")
lbl_result.grid(column=1, row=3, columnspan=4)

window.mainloop()

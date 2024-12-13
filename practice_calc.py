from tkinter import *
from functools import partial

# window initialization
win = Tk()
win.geometry("1320x610+300+200")
win.title("Medyo Calculator v2")

# operand 1
num1Lbl = Label(win, text="Operand 1:", font=('cascadia code', 20)).place(x=20, y=10)
num1TxBx = (Entry(win, width=30, font=("cascadia code", 10)))
num1TxBx.place(x=220, y=25)

# operand 2
num2Lbl = Label(win, text="Operand 2:", font=('cascadia code', 20)).place(x=20, y=85)
num2TxBx = (Entry(win, width=30, font=("cascadia code", 10)))
num2TxBx.place(x=220, y=100)

# result    
resultLbl = Label(win, text="Result:", fg='green', font=('cascadia code', 20)).place(x=20, y=170)
printResult = (Label(win, text="___________", fg='green', font=('cascadia code', 20)))
printResult.place(x=200, y=170)

# operators
def get_result(operator):
    printResult.config(text=eval(str(num1TxBx.get() + operator + num2TxBx.get())))

operators = ["+", "-", "*", "/", "//", "**", "%"]
x = 20
for i in operators:
    Button(win, width=10, height=7, text=i, fg='white', bg='grey', font=("cascadia code", 20), command=partial(get_result, i)).place(x=x, y=250)
    x += 180

# window rendering
win.mainloop()

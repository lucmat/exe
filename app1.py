from tkinter import *
import tkinter
from tkinter import messagebox
def proces():
    number1 =Entry.get(E1)
    number2 =float(number1)/3
    number3 =float(number1)/3
    number4 =float(number1)/3
    Entry.insert(E2,0,number2)                                           \

    Entry.insert(E3,0,number3)
    Entry.insert(E4,0,number4)
    print(number2)
    print(number3)
    print(number4)

top = tkinter.Tk()
L1 = Label(top, text="RENT",).grid(row=0,column=1)
L2 = Label(top, text="Value",).grid(row=1,column=0)
L3 = Label(top, text="Ju",).grid(row=2,column=0)
L4 = Label(top, text="Pe",).grid(row=3,column=0)
L5 = Label(top, text="Lu",).grid(row=4,column=0)

E1 = Entry(top, bd =5)
E1.grid(row=1,column=1)
E2 = Entry(top, bd =5)
E2.grid(row=2,column=1)
E3 = Entry(top, bd =5)
E3.grid(row=3,column=1)
E4 = Entry(top, bd =5)
E4.grid(row=4,column=1)
B=Button(top, text ="Submit",command = proces).grid(row=5,column=1,)

top.mainloop()

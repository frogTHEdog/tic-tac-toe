#!/usr/bin/env python3

from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("Tic Tac Toe")

btns = list()

for i in range(9) :
    btn = Button(text = "", background="#555555", foreground="#ffffff", width=10, height=10)
    xx = (i % 3)*100
    yy = int(i/3)*100 
    btn.place(x = xx, y = yy ) 

    btns.append(btn)
 
for btn in btns :
    #btn.pack()
    pass

root.mainloop()
#!/usr/bin/env python3

from tkinter import *
from functools import partial

# our field
field = dict()

for i in range(3):
    field[i] = dict()
    for j in range(3) :
        field[i][j] = "~"

next_turn = "X"

def print_field() :
    for i in range(3):
        for j in range(3) :
            print(f"{field[i][j]}", end='')
        print("")

def change_next_turn():
    global next_turn
    if next_turn == "X" :
        next_turn = "0"
    else :
        next_turn = "X"

def btn_click(idx) :
    if btns[idx]["state"] == "disabled" :
        return
    btns[idx]["text"] = next_turn
    btns[idx]["state"] = "disabled"
    field[int(idx/3)][idx%3] = next_turn ; print_field()
    change_next_turn()


## INITIALIZE

root = Tk()
root.geometry("300x300")
root.title("Tic Tac Toe")

btns = list()

for i in range(9):
    btn = Button(
        text=f"",
        background="#555555",
        foreground="#ffffff",
        width="8",
        height="5",
        font="10",
        padx="10",
        pady="5",
        command = partial(btn_click, i),
    )
    xx = (i % 3) * 100
    yy = int(i / 3) * 100
    btn.place(x=xx, y=yy)

    btns.append(btn)

# Binding 
#idx = 0
#for btn in btns:
#    btn.bind("<Button-1>", eval("btn" + str(idx) + "_click"))
#    idx += 1

# play game


# RUN 
root.mainloop()

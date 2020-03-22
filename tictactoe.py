#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
from functools import partial

# our field
field = dict()

for i in range(3):
    field[i] = dict()
    for j in range(3) :
        field[i][j] = "~"

next_turn = "X"

def check_win():
    """Check if somebody win the game."""
    for i in range(3):
        if field[i][0] != "~" and field[i][0] == field[i][1] and field[i][0] == field[i][2] :
            messagebox.showinfo(title = 'Game over', message = f"{field[i][0]} win the game!")
            return 
        if field[0][i] != "~" and field[0][i] == field[1][i] and field[0][i] == field[2][i] :
            messagebox.showinfo(title = 'Game over', message = f"{field[0][i]} win the game!")
            return 

    if field[0][0] != "~" and field[0][0] == field[1][1] and field[0][0] == field[2][2] :
        messagebox.showinfo(title = 'Game over', message = f"{field[0][0]} win the game!")
        return 

    if field[0][2] != "~" and field[0][2] == field[1][1] and field[0][2] == field[2][0] :
        messagebox.showinfo(title = 'Game over', message = f"{field[0][2]} win the game!")
        return 
    
    # check if nobody win
    nobody_win = True
    for i in range(3):
        for j in range(3):
            if field[i][j] == "~" :
                nobody_win = False
                break
    if nobody_win == True :
       messagebox.showinfo(title = 'Game over', message = f"Friendship forever!") 
       return 



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
    # we must check if somebody win the game
    check_win()


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

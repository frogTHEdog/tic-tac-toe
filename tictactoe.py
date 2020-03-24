#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
from functools import partial
from random import randrange
from time import sleep

# our field
btns = list()
field = dict()
root = Tk()

for i in range(3):
    field[i] = dict()
    for j in range(3):
        field[i][j] = "~"

next_turn = "X"
win_the_game = False


def start_new_game():
    """Start a new game"""
    global field
    global next_turn
    global win_the_game
    global btns
    global root

    for i in range(3):
        field[i] = dict()
        for j in range(3):
            field[i][j] = "~"

    next_turn = "X"
    win_the_game = False

    # clear buttons
    for idx in range(9):
        btns[idx]["text"] = ""
        btns[idx]["state"] = "normal"
    root.update_idletasks()


def init_game():
    """Initialize game"""
    global field
    global btns
    global root

    root.geometry("300x300")
    root.title("Tic Tac Toe")

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
            command=partial(btn_click, i),
        )
        xx = (i % 3) * 100
        yy = int(i / 3) * 100
        btn.place(x=xx, y=yy)

        btns.append(btn)

    start_new_game()

    # RUN
    root.mainloop()


def check_win():
    global win_the_game
    """Check if somebody win the game."""
    for i in range(3):
        if (
            field[i][0] != "~"
            and field[i][0] == field[i][1]
            and field[i][0] == field[i][2]
        ):
            result = messagebox.askyesno(
                title="Game Over",
                message=f"{field[i][0]} win the game!\nDo you wanna play again?",
            )
            win_the_game = True
            if result == True:
                start_new_game()
            else:
                root.destroy()

        if (
            field[0][i] != "~"
            and field[0][i] == field[1][i]
            and field[0][i] == field[2][i]
        ):
            result = messagebox.askyesno(
                title="Game Over",
                message=f"{field[0][i]} win the game!\nDo you wanna play again?",
            )
            win_the_game = True
            if result == True:
                start_new_game()
            else:
                root.destroy()

    if field[0][0] != "~" and field[0][0] == field[1][1] and field[0][0] == field[2][2]:
        result = messagebox.askyesno(
            title="Game Over",
            message=f"{field[0][0]} win the game!\nDo you wanna play again?",
        )
        win_the_game = True
        if result == True:
            start_new_game()
        else:
            root.destroy()

    if field[0][2] != "~" and field[0][2] == field[1][1] and field[0][2] == field[2][0]:
        result = messagebox.askyesno(
            title="Game Over",
            message=f"{field[0][2]} win the game!\nDo you wanna play again?",
        )
        win_the_game = True
        if result == True:
            start_new_game()
        else:
            root.destroy()

    # check if nobody win
    nobody_win = True
    for i in range(3):
        for j in range(3):
            if field[i][j] == "~":
                nobody_win = False
                break
    if nobody_win == True:
        result = messagebox.askyesno(
            title="Game Over", message=f"Friendship forever!\nDo you wanna play again?"
        )
        win_the_game = True
        if result == True:
            start_new_game()
        else:
            root.destroy()


def print_field():
    for i in range(3):
        for j in range(3):
            print(f"{field[i][j]}", end="")
        print("")


def change_next_turn():
    global next_turn
    if next_turn == "X":
        next_turn = "0"
    else:
        next_turn = "X"


def btn_click(idx):
    if btns[idx]["state"] == "disabled":
        return
    if next_turn == "0":
        return

    btns[idx]["text"] = next_turn
    btns[idx]["state"] = "disabled"
    root.update_idletasks()
    field[int(idx / 3)][idx % 3] = next_turn
    print_field()
    change_next_turn()
    # we must check if somebody win the game
    check_win()
    # AI
    do_next_turn()


def do_next_turn():
    """AI tic tac toe algorithm"""
    global win_the_game

    if next_turn == "X":
        return

    if win_the_game:
        return

    for i in range(3):
        x = 0  # number of X
        o = 0  # number of 0
        s = 0  # field empty
        for j in range(3):
            if field[i][j] == "~":
                s = s + 1
            elif field[i][j] == "X":
                x = x + 1
            else:
                o = o + 1
        # 
        print(f"i = {i} | x = {x} o = {o} s = {s}")
        # atack
        if o == 2 and s == 1:
            # turn AI
            if field[i][0] == '~' :
                y = 0
            elif field[i][1] == '~' : 
                y = 1
            else :
                y = 2
            field[i][y] = next_turn

            num = i * 3 + y
            btns[num]["text"] = next_turn
            btns[num]["state"] = "disabled"
            root.update_idletasks()

            change_next_turn()
            check_win()

            return



        # defence
        if x == 2 and s == 1:
            # turn AI
            if field[i][0] == '~' :
                y = 0
            elif field[i][1] == '~' : 
                y = 1
            else :
                y = 2
            field[i][y] = next_turn

            num = i * 3 + y
            btns[num]["text"] = next_turn
            btns[num]["state"] = "disabled"
            root.update_idletasks()

            change_next_turn()
            check_win()

            return


    ### random turn
    is_field_empty = False

    while is_field_empty == False:
        x = randrange(0, 3)
        y = randrange(0, 3)
        if field[x][y] == "~":
            is_field_empty = True
            # we can do our turn

            field[x][y] = next_turn

            num = x * 3 + y
            btns[num]["text"] = next_turn
            btns[num]["state"] = "disabled"
            root.update_idletasks()

            change_next_turn()
            check_win()


## INITIALIZE

init_game()

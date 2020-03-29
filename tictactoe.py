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

bg_imgs = list()
for i in range(9):
    tmp = PhotoImage(file = f'media/neon/blank/btn-~-{i}.png')
    bg_imgs.append(tmp)

bg_imgs_x = list()
for i in range(9):
    tmp = PhotoImage(file = f'media/neon/X/btn-x-{i}.png')
    bg_imgs_x.append(tmp)

bg_imgs_o = list()
for i in range(9):
    tmp = PhotoImage(file = f'media/neon/O/btn-0-{i}.png')
    bg_imgs_o.append(tmp)



def start_new_game():
    """Start a new game"""
    global field
    global next_turn
    global win_the_game
    global btns
    global root
    global bg_imgs

    for i in range(3):
        field[i] = dict()
        for j in range(3):
            field[i][j] = "~"

    next_turn = "X"
    win_the_game = False

    # clear buttons
    for idx in range(9):
        btns[idx]['image'] = bg_imgs[idx]
        btns[idx]["state"] = "normal"
    root.update_idletasks()


def init_game():
    """Initialize game"""
    global field
    global btns
    global root
    global bg_imgs

    root.geometry("300x300")
    root.title("Tic Tac Toe")

    for i in range(9):
        btn = Button(
            text=f"",
            background="#555555",
            foreground="#ffffff",
            width="100",
            height="100",
            font="10",
            padx="0",
            pady="0",
            image = bg_imgs[i],
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
    global bg_imgs_x

    # secure 

    if field[int(idx / 3)][idx % 3] == "~" :
        pass
    else :
        return

    if next_turn == '':
        return

    btns[idx]["image"] = bg_imgs_x[idx]
    #btns[idx]["state"] = "disabled"
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
    global bg_imgs_o

    if next_turn == "X":
        return

    if win_the_game:
        return

    # AI LINE
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
            #btns[num]["text"] = next_turn
            btns[num]["image"] = bg_imgs_o[num]
            #btns[num]["state"] = "disabled"
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
            #btns[num]["text"] = next_turn
            btns[num]["image"] = bg_imgs_o[num]
            #btns[num]["state"] = "disabled"
            root.update_idletasks()

            change_next_turn()
            check_win()

            return

    # AI COL
    for j in range(3):
        x = 0  # number of X
        o = 0  # number of 0
        s = 0  # field empty
        for i in range(3):
            if field[i][j] == "~":
                s = s + 1
            elif field[i][j] == "X":
                x = x + 1
            else:
                o = o + 1
        # 
        print(f"j = {j} | x = {x} o = {o} s = {s}")
        # atack
        if o == 2 and s == 1:
            # turn AI
            if field[0][j] == '~' :
                y = 0
            elif field[1][j] == '~' : 
                y = 1
            else :
                y = 2

            field[y][j] = next_turn

            num = y * 3 + j
            #btns[num]["text"] = next_turn
            btns[num]["image"] = bg_imgs_o[num]
            #btns[num]["state"] = "disabled"
            root.update_idletasks()

            change_next_turn()
            check_win()

            return

        # defence
        if x == 2 and s == 1:
            # turn AI
            if field[0][j] == '~' :
                y = 0
            elif field[1][j] == '~' : 
                y = 1
            else :
                y = 2

            field[y][j] = next_turn

            num = y * 3 + j
            #btns[num]["text"] = next_turn
            btns[num]["image"] = bg_imgs_o[num]
            #btns[num]["state"] = "disabled"
            root.update_idletasks()

            change_next_turn()
            check_win()

            return

    # AI DIAG 1

    x = 0  # number of X
    o = 0  # number of 0
    s = 0  # field empty
    for j in range(3):
        if field[j][j] == "~":
            s = s + 1
        elif field[j][j] == "X":
            x = x + 1
        else:
            o = o + 1
    # 
    print(f"d1  | x = {x} o = {o} s = {s}")
    # atack
    if o == 2 and s == 1:
        # turn AI
        if field[0][0] == '~' :
            y = 0
        elif field[1][1] == '~' : 
            y = 1
        else :
            y = 2
        field[y][y] = next_turn

        num = y * 3 + y
        #btns[num]["text"] = next_turn
        btns[num]["image"] = bg_imgs_o[num]
        #btns[num]["state"] = "disabled"
        root.update_idletasks()

        change_next_turn()
        check_win()

        return

    # defence
    if x == 2 and s == 1:
        # turn AI
        if field[0][0] == '~' :
            y = 0
        elif field[1][1] == '~' : 
            y = 1
        else :
            y = 2
        field[y][y] = next_turn

        num = y * 3 + y
        #btns[num]["text"] = next_turn
        btns[num]["image"] = bg_imgs_o[num]
        #btns[num]["state"] = "disabled"
        root.update_idletasks()

        change_next_turn()
        check_win()

        return

    # AI DIAG 2

    x = 0  # number of X
    o = 0  # number of 0
    s = 0  # field empty
    for j in range(3):
        if field[j][2-j] == "~":
            s = s + 1
        elif field[j][2-j] == "X":
            x = x + 1
        else:
            o = o + 1
    # 
    print(f"d2  | x = {x} o = {o} s = {s}")
    # atack
    if o == 2 and s == 1:
        # turn AI
        if field[0][2] == '~' :
            y = 0
        elif field[1][1] == '~' : 
            y = 1
        else :
            y = 2
        field[y][2-y] = next_turn

        num = y * 3 + (2-y)
        #btns[num]["text"] = next_turn
        btns[num]["image"] = bg_imgs_o[num]
        #btns[num]["state"] = "disabled"
        root.update_idletasks()

        change_next_turn()
        check_win()

        return

    # defence
    if x == 2 and s == 1:
        # turn AI
        if field[0][2] == '~' :
            y = 0
        elif field[1][1] == '~' : 
            y = 1
        else :
            y = 2
        field[y][2-y] = next_turn

        num = y * 3 + (2-y)
        #btns[num]["text"] = next_turn
        btns[num]["image"] = bg_imgs_o[num]
        #btns[num]["state"] = "disabled"
        root.update_idletasks()

        change_next_turn()
        check_win()

        return


    ### random turn
    is_field_empty = False
    print (f"Random turn")
    while is_field_empty == False:
        x = randrange(0, 3)
        y = randrange(0, 3)
        if field[x][y] == "~":
            is_field_empty = True
            # we can do our turn
            field[x][y] = next_turn

            num = x * 3 + y
            #btns[num]["text"] = next_turn
            btns[num]["image"] = bg_imgs_o[num]
            #btns[num]["state"] = "disabled"
            root.update_idletasks()

            change_next_turn()
            check_win()


## INITIALIZE

init_game()

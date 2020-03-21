#!/usr/bin/env python3

from tkinter import *

# our field
field = dict()

for i in range(3):
    field[i] = dict()
    for j in range(3) :
        field[i][j] = ""

next_turn = "X"

def change_next_turn():
    global next_turn
    if next_turn == "X" :
        next_turn = "0"
    else :
        next_turn = "X"

def btn0_click(event):
    idx = 0
    if btns[idx]["state"] == "disabled" :
        return
    btns[idx]["text"] = next_turn
    btns[idx]["state"] = "disabled"
    change_next_turn()


def btn1_click(event):
    idx = 1
    if btns[idx]["state"] == "disabled" :
        return
    btns[idx]["text"] = next_turn
    btns[idx]["state"] = "disabled"
    change_next_turn()


def btn2_click(event):
    idx = 2
    if btns[idx]["state"] == "disabled" :
        return
    btns[idx]["text"] = next_turn
    btns[idx]["state"] = "disabled"
    change_next_turn()


def btn3_click(event):
    idx = 3
    if btns[idx]["state"] == "disabled" :
        return
    btns[idx]["text"] = next_turn
    btns[idx]["state"] = "disabled"
    change_next_turn()


def btn4_click(event):
    idx = 4
    if btns[idx]["state"] == "disabled" :
        return
    btns[idx]["text"] = next_turn
    btns[idx]["state"] = "disabled"
    change_next_turn()


def btn5_click(event):
    idx = 5
    if btns[idx]["state"] == "disabled" :
        return
    btns[idx]["text"] = next_turn
    btns[idx]["state"] = "disabled"
    change_next_turn()


def btn6_click(event):
    idx = 6
    if btns[idx]["state"] == "disabled" :
        return
    btns[idx]["text"] = next_turn
    btns[idx]["state"] = "disabled"
    change_next_turn()


def btn7_click(event):
    idx = 7
    if btns[idx]["state"] == "disabled" :
        return
    btns[idx]["text"] = next_turn
    btns[idx]["state"] = "disabled"
    change_next_turn()


def btn8_click(event):
    idx = 8
    if btns[idx]["state"] == "disabled" :
        return
    btns[idx]["text"] = next_turn
    btns[idx]["state"] = "disabled"
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
    )
    xx = (i % 3) * 100
    yy = int(i / 3) * 100
    btn.place(x=xx, y=yy)

    btns.append(btn)

# Binding 
idx = 0
for btn in btns:
    btn.bind("<Button-1>", eval("btn" + str(idx) + "_click"))
    idx += 1

# play game


# RUN 
root.mainloop()

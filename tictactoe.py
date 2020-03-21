#!/usr/bin/env python3

from tkinter import *


def btn0_click(event):
    root.title("0")


def btn1_click(event):
    root.title("1")


def btn2_click(event):
    root.title("2")


def btn3_click(event):
    root.title("3")


def btn4_click(event):
    root.title("4")


def btn5_click(event):
    root.title("5")


def btn6_click(event):
    root.title("6")


def btn7_click(event):
    root.title("7")


def btn8_click(event):
    root.title("8")


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

idx = 0
for btn in btns:
    btn.bind("<Button-1>", eval("btn" + str(idx) + "_click"))
    idx += 1

root.mainloop()

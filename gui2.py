from argparse import Action
from cgitb import text
import tkinter as tk
from tkinter import *
from tkinter import ttk

win = tk.Tk()
win.title('test gui')
a_label = ttk.Label(win, text='Your name ?')
a_label.grid(column=0, row=0)

def get_click():
    action.configure(text='get clicked!')
    a_label.configure(foreground='red')
    a_label.configure(text='got it!')
    ttk.Label(win, text='').grid(column=0,row=2)
    ttk.Label(win, text='hello!' + name.get()).grid(column=0,row=2)

action = ttk.Button(win, text="send!", command=get_click)
action.grid(column=1, row=1)

exitButton = ttk.Button(win, text='Exit',command=lambda:win.destroy())
exitButton.grid(column=0, row=3)

name = tk.StringVar()
name_get = ttk.Entry(win, width=12, textvariable=name)
name_get.grid(column=0, row=1)

win.mainloop()
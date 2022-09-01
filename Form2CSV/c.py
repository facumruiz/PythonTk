from cProfile import label
from tkinter import *
from ast import Delete
from distutils.command.config import config
from operator import length_hint
from sre_parse import State
import tkinter as tk

from tkinter import DISABLED, NW, W, Tk, Label, Button, Entry, Frame, END
from tkinter.font import NORMAL
import pandas as pd

root = Tk()
root.geometry("600x400")
root.configure(bg="white")
root.attributes("-fullscreen", True)
root.bind("<F11>", lambda event: root.attributes("-fullscreen", not root.attributes("-fullscreen")))

centro_num=5

for i in range(9):
    root.grid_rowconfigure(i, weight=1)
    for j in range(11):
        root.grid_columnconfigure(j, weight=1)

        Entry(root, text=f'Button {i}-{j}').grid(row=i, column=j, sticky=NSEW)
        nombre = Label(root, text=f'Nombre', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold')).grid(row=2, column=centro_num, sticky=NSEW)
        dato1 = Entry(root, width=80,  bd=0, borderwidth=17, relief=tk.FLAT, font=('Arial', 12), bg='gray95').grid(row=2, column=centro_num, sticky=W)

        apellido = Label(root, text=f'Apellido', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold')).grid(row=3, column=centro_num, sticky=NSEW)
        dato1 = Entry(root, width=80,  bd=0, borderwidth=17, relief=tk.FLAT, font=('Arial', 12), bg='gray95').grid(row=3, column=centro_num, sticky=W)

        
        edad = Label(root, text=f'Edad', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold')).grid(row=4, column=centro_num, sticky=NSEW)
        dato1 = Entry(root, width=80,  bd=0, borderwidth=17, relief=tk.FLAT, font=('Arial', 12), bg='gray95').grid(row=4, column=centro_num, sticky=W)

        
        correo = Label(root, text=f'Correo', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold')).grid(row=5, column=centro_num, sticky=NSEW)
        dato1 = Entry(root, width=80,  bd=0, borderwidth=17, relief=tk.FLAT, font=('Arial', 12), bg='gray95').grid(row=5, column=centro_num, sticky=W)

        
        telefono = Label(root, text=f'Telefono', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold')).grid(row=6, column=centro_num, sticky=NSEW)
        dato1 = Entry(root, width=80,  bd=0, borderwidth=17, relief=tk.FLAT, font=('Arial', 12), bg='gray95').grid(row=6, column=centro_num, sticky=W)

root.mainloop()
root.mainloop()
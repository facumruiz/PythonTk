from ast import Delete
from distutils.command.config import config
from operator import length_hint
from sre_parse import State
import tkinter as tk
import tkinter
from tkinter import *

from tkinter.font import NORMAL
import pandas as pd



root = Tk()
root.geometry("600x400")
root.configure(bg="white")
root.attributes("-fullscreen", True)
root.bind("<F11>", lambda event: root.attributes("-fullscreen", not root.attributes("-fullscreen")))

centro_num=5


d1, d2, d3, d4, d5 = [], [], [], [], []
def agregar_datos():
	global d1, d2, d3, d4, d5

	d1.append(dato1.get())
	d2.append(dato2.get())
	d3.append(dato3.get())
	d4.append(dato4.get())
	d5.append(dato5.get())

	dato1.delete(0, END)
	dato2.delete(0, END)
	dato3.delete(0, END)
	dato4.delete(0, END)
	dato5.delete(0, END)

	datos = {'Dato1': d1, 'Dato2': d2, 'Dato3': d3, 'Dato4': d4, 'Dato5': d5}
	nom_excel = str("data.xlsx")
	df = pd.DataFrame(
		datos, columns=['Dato1', 'Dato2', 'Dato3', 'Dato4', 'Dato5'])
	df.to_excel(nom_excel)  # index=False

              
for i in range(9):
    root.grid_rowconfigure(i, weight=1)
    for j in range(11):
        root.grid_columnconfigure(j, weight=1)
        

Label(root, text=f'FOMRULARIO', anchor=N, width=10, bg='white', font=('Arial', 12, 'bold')).grid(row=1, column=5, sticky=EW)


nombre = Label(root, text='Nombre', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold')).grid(row=2, column=5, sticky=NSEW)
dato1 = Entry(root, width=80,  bd=0, borderwidth=17, relief=tk.FLAT, font=('Arial', 12), bg='gray95')
dato1.grid(row=2, column=5, sticky=W)

   

apellido = Label(root, text='Apellido', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold')).grid(row=3, column=centro_num, sticky=NSEW)
dato2 = Entry(root, width=80,  bd=0, borderwidth=17, relief=tk.FLAT, font=('Arial', 12), bg='gray95')
dato2.grid(row=3, column=centro_num, sticky=W)
        
edad = Label(root, text='Edad', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold')).grid(row=4, column=centro_num, sticky=NSEW)
dato3 = Entry(root, width=80,  bd=0, borderwidth=17, relief=tk.FLAT, font=('Arial', 12), bg='gray95')
dato3.grid(row=4, column=centro_num, sticky=W)
        
        
correo = Label(root, text='Correo', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold')).grid(row=5, column=centro_num, sticky=NSEW)
dato4 = Entry(root, width=80,  bd=0, borderwidth=17, relief=tk.FLAT, font=('Arial', 12), bg='gray95')
dato4.grid(row=5, column=centro_num, sticky=W)
        
        
telefono = Label(root, text='Telefono', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold')).grid(row=6, column=centro_num, sticky=NSEW)
dato5 = Entry(root, width=80,  bd=0, borderwidth=17, relief=tk.FLAT, font=('Arial', 12), bg='gray95')
dato5.grid(row=6, column=centro_num, sticky=W)

agregar = Button(root, width=0,fg='white',  bd=0, font=('Arial', 15),text='Agregar', bg='dodger blue',command=agregar_datos).grid(column=5, row=7,pady=10, sticky="EW")


root.mainloop()


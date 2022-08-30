from ast import Delete
from distutils.command.config import config
from operator import length_hint
from sre_parse import State
import tkinter as tk

from tkinter import DISABLED, NW, W, Tk, Label, Button, Entry, Frame, END
from tkinter.font import NORMAL
import pandas as pd

root = tk.Tk()
root.geometry("600x400")
root.configure(bg="white")
root.attributes("-fullscreen", True)
root.bind("<F11>", lambda event: root.attributes("-fullscreen", not root.attributes("-fullscreen")))


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

root.rowconfigure(1, weight=1)

#seccion code
seccion1 = tk.Label(root, text="Rectangle 1", bg="white", fg="white")
seccion1.grid(column=0, row=0, columnspan=5, ipadx=20, ipady=100, sticky="NSEW")

seccion2 = tk.Label(root, bg="white", fg="white")
seccion2.grid(row=1, ipadx=250, sticky="NSEW")

seccion3 = tk.Label(root, text="Rectangle 3", bg="white", fg="white")
seccion3.grid(column=1, row=1, sticky="NSEW")

seccion4 = tk.Label(root, text="Rectangle 3", bg="white", fg="white")
seccion4.grid(column=2, row=1,ipadx=100, sticky="NSEW")

def click1(event):
	dato1.config(state=NORMAL)
	dato1.delete(0, END)
	
def click2(event):
	dato2.config(state=NORMAL)
	dato2.delete(0, END)

def click3(event):
	dato3.config(state=NORMAL)
	dato3.delete(0, END)

def click4(event):
	dato4.config(state=NORMAL)
	dato4.delete(0, END)

def click5(event):
	dato5.config(state=NORMAL)
	dato5.delete(0, END)

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


nombre = Label(seccion3, text='Nombre', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold'))
nombre.grid(column=0, row=0, ipady=0, padx=0, sticky="NW")

dato1 = Entry(seccion3, width=80,  bd=0, borderwidth=13, relief=tk.FLAT, font=('Arial', 12), bg='gray95')
dato1.insert(0, 'Nombre')
dato1.config(state=DISABLED)
dato1.bind("<Button-1>", click1)
dato1.grid(column=0, row=1, ipady=5, pady=10)

apellido = Label(seccion3, text='Apellido', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold'))
apellido.grid(column=0, row=2, pady=0, padx=0, sticky="NW")

dato2 = Entry(seccion3, width=80, bd=0, borderwidth=13, relief=tk.FLAT, font=('Arial', 12), bg='gray95')
dato2.insert(0, 'Apellido')
dato2.config(state=DISABLED)
dato2.bind("<Button-1>", click2)
dato2.grid(column=0,row=3,ipady=5,pady=10)

edad = Label(seccion3, text='dato1', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold'))
edad.grid(column=0, row=4, pady=0, padx=0, sticky="NW")

dato3 = Entry(seccion3, width=80, bd=0, borderwidth=13, relief=tk.FLAT, font=('Arial', 12), bg='gray95')
dato3.insert(0, 'dato1')
dato3.config(state=DISABLED)
dato3.bind("<Button-1>", click3)
dato3.grid(column=0, row=5, ipady=5, pady=10)

correo = Label(seccion3, text='dato2', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold'))
correo.grid(column=0, row=6, pady=0, padx=0, sticky="NW")

dato4 = Entry(seccion3, width=80, bd=0, borderwidth=13, relief=tk.FLAT, font=('Arial', 12), bg='gray95')
dato4.insert(0, 'dato2')
dato4.config(state=DISABLED)
dato4.bind("<Button-1>", click4)
dato4.grid(column=0, row=7, ipady=5, pady=10)

telefono = Label(seccion3, text='dato3', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold'))
telefono.grid(column=0, row=8, pady=0, padx=0, sticky="NW")

dato5 = Entry(seccion3, width=80, bd=0, borderwidth=13, relief=tk.FLAT, font=('Arial', 12), bg='gray95')
dato5.insert(0, 'dato3')
dato5.config(state=DISABLED)
dato5.bind("<Button-1>", click5)
dato5.grid(column=0, row=9, ipady=5, pady=10)

agregar = Button(seccion3, width=10,fg='white',  bd=0, font=('Arial', 15),
                 text='Agregar', bg='dodger blue', command=agregar_datos)
agregar.grid(column=0, row=10,pady=10, sticky="NW")

root.mainloop()

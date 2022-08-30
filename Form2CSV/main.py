from ast import Delete
from distutils.command.config import config
from sre_parse import State
import tkinter as tk

from tkinter import DISABLED, NW, W, Tk, Label, Button, Entry, Frame, END
from tkinter.font import NORMAL
import pandas as pd

root = tk.Tk()
root.geometry("600x400")
root.configure(bg="white")
root.attributes("-fullscreen", True)
root.bind("<F11>", lambda event: root.attributes("-fullscreen",
                                                 not root.attributes("-fullscreen")))


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

root.rowconfigure(1, weight=1)

#seccion code
seccion1 = tk.Label(root, text="Rectangle 1", bg="gray", fg="white")
seccion1.grid(column=0, row=0, columnspan=2, ipadx=20, ipady=20, sticky="NSEW")

seccion2 = tk.Label(root, text="Rectangle 2", bg="white", fg="white")
seccion2.grid(column=0, row=1, ipadx=900, ipady=10, padx=500, pady=20, sticky="NSEW")

#seccion3 = tk.Label(root, text="Rectangle 3", bg="red", fg="white")
#seccion3.grid(column=1, row=1, ipadx=10, ipady=10, sticky="NSEW")
def click(event):
	dato1.config(state=NORMAL)
	dato1.delete(0, END)


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


nombre = Label(seccion2,
               text='Nombre',
               anchor=NW,
               width=10,
               bg='white',
               font=('Arial', 12, 'bold'))

nombre.grid(column=0,
            row=0,
            pady=0,
            padx=0,
            sticky="NW")

dato1 = Entry(seccion2,
              width=100,
			  bd=0,
			  borderwidth=13,
			  relief=tk.FLAT,
              font=('Arial', 12),
              bg='gray95')

dato1.insert(0, 'Nombre')
dato1.config(state=DISABLED)
dato1.bind("<Button-1>", click)


dato1.grid(column=0,
           row=1,
           ipady=5)
"""
apellido = Label(seccion2, text='Apellido', width=10).grid(
	column=0, row=1, pady=20, padx=10)
dato2 = Entry(seccion2, width=20, font=('Arial', 12))
dato2.grid(column=1, row=1)

edad = Label(seccion2, text='Edad', width=10).grid(
	column=0, row=2, pady=20, padx=10)
dato3 = Entry(seccion2,  width=20, font=('Arial', 12))
dato3.grid(column=1, row=2)

correo = Label(seccion2, text='Correo', width=10).grid(
	column=0, row=3, pady=20, padx=10)
dato4 = Entry(seccion2,  width=20, font=('Arial', 12))
dato4.grid(column=1, row=3)

telefono = Label(seccion2, text='Telefono', width=10).grid(
	column=0, row=4, pady=20, padx=10)
dato5 = Entry(seccion2, width=20, font=('Arial', 12))
dato5.grid(column=1, row=4)

agregar = Button(seccion2, width=20, font=('Arial', 12, 'bold'),
                 text='Agregar', bg='orange', bd=5, command=agregar_datos)
agregar.grid(columnspan=2, row=5, pady=20, padx=10)

"""
root.mainloop()

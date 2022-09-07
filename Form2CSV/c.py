import tkinter as tk
from tkinter import ttk, filedialog, messagebox, ttk
from tkinter.messagebox import showinfo
import tkinter as tk
from tkinter import *
import pandas as pd


root = Tk()
root.geometry("600x400")
root.configure(bg="white")
root.attributes("-fullscreen", True)
root.bind("<F11>", lambda event: root.attributes(
	"-fullscreen", not root.attributes("-fullscreen")))

centro_num = 2


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







def Load_excel_data():
    filename = filedialog.askopenfilename(initialdir="/data.xlsx",
                                          title="Select A File",
                                          filetype=(("xlsx files", "*.xlsx"), ("All Files", "*.*")))
    label_file["text"] = filename
	
	
    """If the file selected is valid this will load the file into the Treeview"""
    file_path = label_file["text"]
    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == "data.xlsx":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)

    except ValueError:
        tk.messagebox.showerror(
            "Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
        return None

    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:

        tv1.heading(column, text=column)

    df_rows = df.to_numpy().tolist()  
    for row in df_rows:
        # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
        tv1.insert("", "end", values=row)
    return None


def clear_data():
    tv1.delete(*tv1.get_children())
    return None


              
for i in range(10):
    root.grid_rowconfigure(i, weight=1)
    for j in range(10):
        root.grid_columnconfigure(j, weight=1)
        Entry(root, text=f'Button {i}-{j}').grid(row=i, column=j, sticky=NSEW)
        


frame1 = tk.LabelFrame(root, text="Excel Data")
frame1.grid(row=2, column=4, rowspan=5, columnspan=5,sticky='nsew')


label_file = ttk.Label(root, text="No File Selected")
label_file.place(rely=0, relx=0)


tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1)
treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) 
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) 
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) 
treescrollx.pack(side="bottom", fill="x")
treescrolly.pack(side="right", fill="y")



Label(root, text=f'FOMRULARIO', anchor=N, width=10, bg='white', font=('Arial', 12, 'bold')).grid(row=1, column=centro_num, sticky=N)


nombre = Label(root, text='Nombre', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold')).grid(row=1, column=centro_num, sticky=SW)
dato1 = Entry(root, width=80,  bd=0, borderwidth=17, relief=tk.FLAT, font=('Arial', 12), bg='gray95')
dato1.grid(row=2, column=centro_num, sticky=NW)

   

apellido = Label(root, text='Apellido', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold')).grid(row=2, column=centro_num, sticky=SW)
dato2 = Entry(root, width=80,  bd=0, borderwidth=17, relief=tk.FLAT, font=('Arial', 12), bg='gray95')
dato2.grid(row=3, column=centro_num, sticky=NW)
    
edad = Label(root, text='Edad', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold')).grid(row=3, column=centro_num, sticky=SW)
dato3 = Entry(root, width=80,  bd=0, borderwidth=17, relief=tk.FLAT, font=('Arial', 12), bg='gray95')
dato3.grid(row=4, column=centro_num, sticky=NW)
        
        
correo = Label(root, text='Correo', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold')).grid(row=4, column=centro_num, sticky=SW)
dato4 = Entry(root, width=80,  bd=0, borderwidth=17, relief=tk.FLAT, font=('Arial', 12), bg='gray95')
dato4.grid(row=5, column=centro_num, sticky=NW)
        
        
telefono = Label(root, text='Telefono', anchor=NW, width=10, bg='white', font=('Arial', 12, 'bold')).grid(row=5, column=centro_num, sticky=SW)
dato5 = Entry(root, width=80,  bd=0, borderwidth=17, relief=tk.FLAT, font=('Arial', 12), bg='gray95')
dato5.grid(row=6, column=centro_num, sticky=NW)

agregar = Button(root, width=30,fg='white',  bd=0, font=('Arial', 15),text='Agregar', bg='dodger blue',command=agregar_datos).grid(column=centro_num, row=6,pady=10, sticky="Sw")
excel = Button(root, width=30,fg='white',  bd=0, font=('Arial', 15),text='Cargar', bg='green',command=Load_excel_data).grid(column=centro_num, row=6,pady=10, sticky="SE")

root.mainloop()
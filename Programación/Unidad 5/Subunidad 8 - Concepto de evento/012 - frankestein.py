import tkinter as tk
from tkinter import ttk
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)

cursor = conexion.cursor()

ventana = tk.Tk()

arbol = ttk.Treeview(ventana, columns=("dninie","nombre","apellidos","email","direccion"), show="headings")
arbol.heading("dninie", text="DNI/NIE del cliente")
arbol.heading("nombre", text="Nombre del cliente")
arbol.heading("apellidos", text="Apellidos del cliente")
arbol.heading("email", text="Email del cliente")
arbol.heading("direccion", text="Dirección del cliente")

cursor.execute('''SELECT * FROM Clientes;''')

filas = cursor.fetchall()

for fila in filas:
    arbol.insert("","end", values=(fila[1],fila[2],fila[3],fila[4],fila[5]))

arbol.pack(padx=20,pady=20)

ventana.mainloop()

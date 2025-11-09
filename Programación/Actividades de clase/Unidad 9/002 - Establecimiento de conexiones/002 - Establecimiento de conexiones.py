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
ventana.title("Restaurantes Favoritos")

arbol = ttk.Treeview(ventana, columns=("nombre", "ubicacion", "calificacion"), show="headings")
arbol.heading("nombre", text="Nombre del Restaurante")
arbol.heading("ubicacion", text="Ubicación")
arbol.heading("calificacion", text="Calificación")

cursor.execute('''SELECT * FROM restaurantes''')
filas = cursor.fetchall()

for fila in filas:
    arbol.insert("", "end", values=(fila[1], fila[2], fila[3]))

arbol.pack(padx=20, pady=20)

ventana.mainloop()

import tkinter as tk
from tkinter import ttk
import mysql.connector

# 1️⃣ Conectar con la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()

# 2️⃣ Crear la tabla restaurantes si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS restaurantes (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ubicacion VARCHAR(150) NOT NULL,
    calificacion INT NOT NULL
)
""")
conexion.commit()

# 3️⃣ Insertar algunos restaurantes (solo si no existen)
restaurantes = [
    ("La Bella Italia", "Calle Roma 12", 5),
    ("El Rincón del Sazón", "Avenida Central 45", 4),
    ("Café de la Esquina", "Plaza Mayor 3", 3)
]

for r in restaurantes:
    cursor.execute("""
    INSERT INTO restaurantes (nombre, ubicacion, calificacion)
    SELECT %s, %s, %s
    WHERE NOT EXISTS (
        SELECT 1 FROM restaurantes WHERE nombre=%s
    )
    """, (r[0], r[1], r[2], r[0]))

conexion.commit()

# 4️⃣ Crear ventana principal
ventana = tk.Tk()
ventana.title("Restaurantes Favoritos")

# 5️⃣ Crear tabla con Treeview
arbol = ttk.Treeview(ventana, columns=("nombre", "ubicacion", "calificacion"), show="headings")
arbol.heading("nombre", text="Nombre del Restaurante")
arbol.heading("ubicacion", text="Ubicación")
arbol.heading("calificacion", text="Calificación")

# 6️⃣ Consultar los restaurantes y llenar la tabla
cursor.execute("SELECT nombre, ubicacion, calificacion FROM restaurantes")
filas = cursor.fetchall()

for fila in filas:
    arbol.insert("", "end", values=(fila[0], fila[1], fila[2]))

arbol.pack(padx=20, pady=20)

# 7️⃣ Ejecutar la ventana
ventana.mainloop()

# 8️⃣ Cerrar la conexión al terminar
cursor.close()
conexion.close()


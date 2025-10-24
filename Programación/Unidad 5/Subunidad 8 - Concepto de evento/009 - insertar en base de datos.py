import tkinter as tk
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)

cursor = conexion.cursor()

ventana = tk.Tk()

def insertar():
    cursor.execute('''
        INSERT INTO Clientes
        VALUES(
            NULL,
            "'''+dninie.get()+'''",
            "'''+nombre.get()+'''",
            "'''+apellidos.get()+'''",
            "'''+email.get()+'''",
            "'''+direccion.get()+'''"
        );
    ''')
    conexion.commit()

marco = tk.Frame(ventana)

tk.Label(marco,text="Introduce el dni/nie del cliente").pack(padx=20,pady=20)
dninie = tk.Entry(marco)
dninie.pack(padx=20,pady=20)

tk.Label(marco,text="Introduce el nombre del cliente").pack(padx=20,pady=20)
nombre = tk.Entry(marco)
nombre.pack(padx=20,pady=20)

tk.Label(marco,text="Introduce los apellidos del cliente").pack(padx=20,pady=20)
apellidos = tk.Entry(marco)
apellidos.pack(padx=20,pady=20)

tk.Label(marco,text="Introduce el email del cliente").pack(padx=20,pady=20)
email = tk.Entry(marco)
email.pack(padx=20,pady=20)

tk.Label(marco,text="Introduce la dirección del cliente").pack(padx=20,pady=20)
direccion = tk.Entry(marco)
direccion.pack(padx=20,pady=20)

tk.Button(marco,text="Insertar cliente",command = insertar).pack(padx=20,pady=20)

marco.pack()

ventana.mainloop()

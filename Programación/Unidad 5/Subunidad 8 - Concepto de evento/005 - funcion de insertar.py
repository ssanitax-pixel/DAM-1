import tkinter as tk

ventana = tk.Tk()

def insertar():
    print("Vamos a insertar un cliente")

marco = tk.Frame(ventana)

# DNI NIE
tk.Label(marco,text="Introduce el dni/nie del cliente").pack(padx=20,pady=20)
dninie = tk.Entry(marco)
dninie.pack(padx=20,pady=20)

# Nombre
tk.Label(marco,text="Introduce el nombre del cliente").pack(padx=20,pady=20)
nombre = tk.Entry(marco)
nombre.pack(padx=20,pady=20)

# Apellidos
tk.Label(marco,text="Introduce los apellidos del cliente").pack(padx=20,pady=20)
apellidos = tk.Entry(marco)
apellidos.pack(padx=20,pady=20)

# Email
tk.Label(marco,text="Introduce el email del cliente").pack(padx=20,pady=20)
email = tk.Entry(marco)
email.pack(padx=20,pady=20)

# Botón
tk.Button(marco,text="Insertar cliente",command = insertar).pack(padx=20,pady=20)

marco.pack()

ventana.mainloop()

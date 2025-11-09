En este código creamos una **interfaz gráfica en Python** usando Tkinter para visualizar los clientes de una base de datos MySQL. La idea surge de la necesidad de poder **ver de forma clara y organizada los datos** de los clientes sin tener que usar la consola o ejecutar consultas SQL manualmente.
Para esto usamos un `Treeview`, que funciona como una tabla dentro de la ventana, mostrando columnas como DNI, nombre, apellidos y email. Además, nos conectamos a la base de datos usando `mysql.connector` y ejecutamos una consulta para traer todos los registros de la tabla `clientes`. Esta actividad nos permite unir la teoría vista en clase sobre conexión a bases de datos, consultas SQL y manejo de interfaces gráficas, aplicándola a un ejemplo práctico que se podría usar en cualquier empresa o proyecto real.

---

Importamos las librerías necesarias.

`tkinter` sirve para crear ventanas y elementos gráficos.

```
import tkinter as tk
```

`ttk` nos da widgets más avanzados, como el `Treeview` que usaremos para la tabla.

```
from tkinter import ttk
```

`mysql.connector` permite conectarnos a la base de datos MySQL para leer los clientes.

```
import mysql.connector
```

Conectamos con la base de datos. Creamos la conexión usando el host, usuario, contraseña y la base de datos.

```
conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
```

`cursor` nos permitirá ejecutar consultas SQL y traer resultados.

```
cursor = conexion.cursor()
```

Creamos la ventana principal.

```
ventana = tk.Tk()
```

Creamos la tabla con `Treeview`, definimos la columnas que tendrá en `columns`. `show="headings"` indica que solo queremos mostrar los títulos de las columnas. `headings()` pone los nombres visibles en cada columna.

```
arbol = ttk.Treeview(ventana, columns=("dni", "nombre", "apellidos", "email"), show="headings")
arbol.heading("dni", text="DNI del cliente")
arbol.heading("nombre", text="Nombre del cliente")
arbol.heading("apellidos", text="Apellidos del cliente")
arbol.heading("email", text="Email del cliente")
```

Ejecutamos la consulta para obtener los clientes. Devolviendo los resultados como una lista de filas.

```
cursor.execute('''SELECT * FROM clientes;''')

filas = cursor.fetchall()
```

Llenamos la tabla con los datos.

```
for fila in filas:
    arbol.insert("", "end", values=(fila[1], fila[2], fila[3], fila[4]))
```

Mostramos la tabla en la ventana.

```
arbol.pack(padx=20,pady=20)
```

Ejecutamos la ventana para que no se cierre.

```
ventana.mainloop()
```

---

El código completo se ve así:

```
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

arbol = ttk.Treeview(ventana, columns=("dni", "nombre", "apellidos", "email"), show="headings")
arbol.heading("dni", text="DNI del cliente")
arbol.heading("nombre", text="Nombre del cliente")
arbol.heading("apellidos", text="Apellidos del cliente")
arbol.heading("email", text="Email del cliente")

cursor.execute('''SELECT * FROM clientes;''')

filas = cursor.fetchall()
for fila in filas:
    arbol.insert("", "end", values=(fila[1], fila[2], fila[3], fila[4]))
    
arbol.pack(padx=20,pady=20)

ventana.mainloop()
```

---

Con este programa logramos crear una interfaz funcional que muestra todos los clientes de la base de datos de manera organizada. Aprendimos a conectar Python con MySQL, ejecutar consultas para obtener los registros y recorrer los resultados para insertarlos dinámicamente en una tabla visual. Además, practicamos cómo usar Tkinter y Treeview para construir interfaces gráficas claras y fáciles de usar. Este ejercicio combina teoría y práctica: comprendimos cómo manejar datos de bases de datos y cómo presentarlos de forma interactiva, sentando las bases para añadir funcionalidades adicionales en el futuro, como agregar, actualizar o eliminar clientes desde la interfaz.

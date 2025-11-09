En esta actividad trabajamos con bases de datos y programación en Python para crear una aplicación que muestra los restaurantes favoritos de manera organizada. Primero aprendimos a manejar MySQL desde el terminal: creamos la base de datos empresadam, la tabla restaurantes y añadimos algunos registros con nombre, ubicación y calificación. Esto nos permitió comprender cómo se estructuran los datos y cómo se insertan y consultan dentro de una base de datos.

A continuación, usamos Python para conectar con la base de datos y mostrar los datos en una interfaz gráfica con Tkinter y Treeview. Así combinamos la teoría de bases de datos con la programación de interfaces, permitiéndonos visualizar la información de manera clara y práctica.

---

Abrimos terminal y entramos como usurario.

```
mysql -u root -p
```

Creamos la base de datos.

```
CREATE DATABASE empresadam;
```

Nos metemos dentro de la base de datos que acabamos de crear.

```
USE empresadam;
```

Creamos la tabla restaurantes.

```
CREATE TABLE restaurantes (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ubicacion VARCHAR(150),
    calificacion INT
);
```

Nos aseguramos que se ha creado.

```
DESCRIBE restaurantes;
```

Insertamos los datos de los restaurantes en la tabla.

```
INSERT INTO restaurantes (nombre, ubicacion, calificacion) VALUES
('La Bella Italia', 'Calle Roma 12', 5),
('El Rincón del Sazón', 'Avenida Central 45', 4),
('Café de la Esquina', 'Plaza Mayor 3', 3);
```

Consultamos que se han implementado.

```
SELECT * FROM restaurantes;
```

---

Ahora nos vamos con la parte de Python.

Importamos las librerías necesarias.

```
import tkinter as tk
from tkinter import ttk
import mysql.connector
```

Conectamos con la base de datos.

```
conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()
```

Creamos la ventana principal.

```
ventana = tk.Tk()
ventana.title("Restaurantes Favoritos")
```

Creamos una tabla con Treeview.

```
arbol = ttk.Treeview(ventana, columns=("nombre", "ubicacion", "calificacion"), show="headings")
arbol.heading("nombre", text="Nombre del Restaurante")
arbol.heading("ubicacion", text="Ubicación")
arbol.heading("calificacion", text="Calificación")
```

Ejecutamos consulta para traer los restaurantes.

```
cursor.execute('''SELECT * FROM restaurantes''')
filas = cursor.fetchall()
```

Llenamos la tabla con los datos de la base de datos.

```
for fila in filas:
    arbol.insert("", "end", values=(fila[1], fila[2], fila[3]))
```

Colocamos la tabla en la ventana.

```
arbol.pack(padx=20, pady=20)
```

Mantenemos la ventana abierta.

```
ventana.mainloop()
```

Cerramos la conexión con la base de datos.

```
cursor.close()
conexion.close()
```

---

El código en SQL se verá así:

```
mysql -u root -p

CREATE DATABASE empresadam;

USE empresadam;

CREATE TABLE restaurantes (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ubicacion VARCHAR(150),
    calificacion INT
);

DESCRIBE restaurantes;

INSERT INTO restaurantes (nombre, ubicacion, calificacion) VALUES
('La Bella Italia', 'Calle Roma 12', 5),
('El Rincón del Sazón', 'Avenida Central 45', 4),
('Café de la Esquina', 'Plaza Mayor 3', 3);

SELECT * FROM restaurantes;
```

---

El código en Python completo se verá así:

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

cursor.close()
conexion.close()
```

Con este proyecto logramos integrar SQL y Python para gestionar y mostrar datos de forma visual. Aprendimos a crear bases de datos y tablas, insertar registros y consultarlos desde Python. Además, practicamos cómo usar Tkinter y Treeview para construir una interfaz gráfica funcional que muestra los datos de la base de datos en una tabla ordenada. Esta experiencia nos ayuda a entender cómo se pueden combinar la persistencia de datos con la programación de aplicaciones visuales, y sienta las bases para proyectos más complejos donde se necesite interactuar con bases de datos de manera dinámica y amigable.

En este ejercicio se practican las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) utilizando SQLite para la base de datos y Python como lenguaje de programación. El objetivo es interactuar con una base de datos mediante comandos SQL y gestionar los registros utilizando Python. El uso de SQL se enfoca en manipular los datos de la base, mientras que Python controla la lógica del programa, facilitando la interacción con el usuario.

---

Primero creamos la base de datos, en este caso la llamaremos 'practica'.

```
CREATE DATABASE practica;
```

Seguidamente utilizaremos el archivo '001-crear clientes.sql' del GitHub del profesor con las columnas que nos piden.

```
CREATE TABLE "clientes" (
	"Identificador"	INTEGER,
	"nombre"	TEXT,
	"apellidos"	TEXT,
	"email"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
);
```

Ahora utilizaremos el archivo 005-ahora leer.py como punto de partida y desarrollaremos un script completo que permita hacer CRUD.

Aquí nos conectamos a la base de datos.

```
import sqlite3
conexion = sqlite3.connect("practica.db")
cursor = conexion.cursor()
```

Aquí implementamos las funciones CRUD.


Creamos un bucle.

```
print("Programa agenda SQLite v0.1 Ana Sánchez Suárez")
while True:
  print("Escoge una opción:\n1.-Crear cliente\n2.-Listar clientes\n3.-Actualizar clientes\n4.-Eliminar clientes\n5.-Salir del programa")
  opcion = int(input("Selecciona una opción: "))
```

Desglosamos las opciones.

Creamos un nuevo cliente.

```
  if opcion == 1:
    nombre = input("Introduce el nombre del nuevo cliente: ")
    apellidos = input("Introduce los apellidos del nuevo cliente: ")
    email = input("Introduce el email del nuevo cliente: ")
    cursor.execute("""
      INSERT INTO clientes VALUES(
        NULL,'"""+nombre+"""','"""+apellidos+"""','"""+email+"""'
      );""")
    conexion.commit()
```

Listamos todos los clientes.

```
  elif opcion == 2:
    cursor.execute('''
      SELECT * FROM clientes;
    ''')
    filas = cursor.fetchall()
    for fila in filas:
      print(fila)
```

Actualizar los datos de un cliente.

```
  elif opcion == 3:
    identificador = input("Introduce el identificador a actualizar: ")
    nombre = input("Introduce el nombre del nuevo cliente: ")
    apellidos = input("Introduce los apellidos del nuevo cliente: ")
    email = input("Introduce el email del nuevo cliente: ")
    cursor.execute("""
      UPDATE clientes SET
        nombre = '"""+nombre+"""',
        apellidos = '"""+apellidos+"""',
        email = '"""+email+"""'
        WHERE Identificador = """+identificador+"""
      ;""")
```

Eliminar un cliente.

```
  elif opcion == 4:
    identificador = input("Introduce el identificador a eliminar: ")
    cursor.execute("""
      DELETE FROM clientes WHERE Identificador = """+identificador+"""
      ;""")
  elif opcion == 5:
    print("byebye")
    exit()
```

---

El código completo:

```
-- Esto se ejecuta en MySQL
CREATE DATABASE practica;

CREATE TABLE "clientes" (
	"Identificador"	INTEGER,
	"nombre"	TEXT,
	"apellidos"	TEXT,
	"email"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
);

-- Esto se ejecuta en Python
import sqlite3
conexion = sqlite3.connect("practica.db")
cursor = conexion.cursor()
print("Programa agenda SQLite v0.1 Ana Sánchez Suárez")
while True:
  print("Escoge una opción:\n1.-Crear cliente\n2.-Listar clientes\n3.-Actualizar clientes\n4.-Eliminar clientes\n5.-Salir del programa")
  opcion = int(input("Selecciona una opción: "))
  if opcion == 1:
    nombre = input("Introduce el nombre del nuevo cliente: ")
    apellidos = input("Introduce los apellidos del nuevo cliente: ")
    email = input("Introduce el email del nuevo cliente: ")
    cursor.execute("""
      INSERT INTO clientes VALUES(
        NULL,'"""+nombre+"""','"""+apellidos+"""','"""+email+"""'
      );""")
    conexion.commit()
  elif opcion == 2:
    cursor.execute('''
      SELECT * FROM clientes;
    ''')
    filas = cursor.fetchall()
    for fila in filas:
      print(fila)
  elif opcion == 3:
    identificador = input("Introduce el identificador a actualizar: ")
    nombre = input("Introduce el nombre del nuevo cliente: ")
    apellidos = input("Introduce los apellidos del nuevo cliente: ")
    email = input("Introduce el email del nuevo cliente: ")
    cursor.execute("""
      UPDATE clientes SET
        nombre = '"""+nombre+"""',
        apellidos = '"""+apellidos+"""',
        email = '"""+email+"""'
        WHERE Identificador = """+identificador+"""
      ;""")
  elif opcion == 4:
    identificador = input("Introduce el identificador a eliminar: ")
    cursor.execute("""
      DELETE FROM clientes WHERE Identificador = """+identificador+"""
      ;""")
  elif opcion == 5:
    print("byebye")
    exit()
```

---

Con este ejercicio he implementado un programa que interactúa con una base de datos SQLite utilizando Python. El script permite realizar operaciones CRUD sobre una tabla de clientes.
Este tipo de aplicaciones son fundamentales para entender cómo interactuar con bases de datos desde un lenguaje de programación, y cómo aplicar operaciones básicas de manipulación de datos.

Para mejorar el código, podría agregar validaciones adicionales para garantizar la calidad de los datos introducidos, y también mejorar la interfaz de usuario, por ejemplo, añadiendo menús más interactivos o manejo de excepciones.

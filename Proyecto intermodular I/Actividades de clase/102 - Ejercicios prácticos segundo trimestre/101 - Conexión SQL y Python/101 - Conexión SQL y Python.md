Vamos a practicar relaciones entre lenguajes de programación y sistemas de gestión de bases de datos relacionales. El objetivo es crear un entorno de datos, configurar accesos seguros y procesar la información mediante scripts de Python utilizando la biblioteca `mysql.connector`.
La conexión entre SQL y Python nos permite automatizar la gestión de grandes volúmenes de información. Mientras que SQL se encarga de la persistencia y estructura de los datos, Python actúa como el motor lógico que consulta, filtra y presenta esa información al usuario final.

---

Parte de SQL.
Entramos en la base de datos en MySQL como administrador.

```
sudo mysql -u root -p
```

Creamos la base de datos.

```
CREATE DATABASE clientes;
```

Usamos la base de datos que acabamos de crear.

```
USE clientes;
```

Creamos la tabla clientes.

```
CREATE TABLE clientes(
	nombre VARCHAR(255),
	apellidos VARCHAR(255),
	edad INT
);
```

Insertamos algunos datos.

```
INSERT INTO clientes VALUES ("Ana","Sánchez",25);
INSERT INTO clientes VALUES ("Fátima","Quiñones",20);
```

Creamos un usuario.

```
CREATE USER 
'clientes'@'localhost' 
IDENTIFIED BY 'Clientes123$';
```

Damos permisos y quitamos límites.

```
GRANT USAGE ON *.* TO 'clientes'@'localhost';

ALTER USER 'clientes'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON clientes.* 
TO 'clientes'@'localhost'
```

Aplicamos los cambios.

```
FLUSH PRIVILEGES;
```

Parte de Python.
Importamos las librerías necesarias para este caso.

```
import mysql.connector
import json
```

Creamos la conexión a la base de datos y usuario que acabamos de crear.

```
conexion = mysql.connector.connect(
  host="localhost",
  user="clientes",
  password="Clientes123$",
  database="clientes"
)
```

Creamos un cursor, que ejecutará las consultas SQL, el `dictionary=True` hará que los resultados sean diccionarios.

```
cursor = conexion.cursor(dictionary=True)
```

Ejecutamos la consulta. En este caso hemos pedido que se cambien el nombre de las columnas para que se vea con más claridad y que se ordene de mayor a menor edad.

```
cursor.execute('''
  SELECT
  nombre AS "Nombre del cliente",
  apellidos AS "Apellidos del cliente",
  edad AS "Edad del cliente"
  FROM clientes
  ORDER BY edad DESC;
''')
```

Guardamos todas las filas en una lista de diccionarios.

```
filas = cursor.fetchall()
```

Convertimos a JSON, `ensure_ascii=False` hace que se permitan acento y la letra ñ, además, con `indent=2` mejoraremos el formato y se verá más legible.

```
resultado_json = json.dumps(filas, ensure_ascii=False, indent=2)
```

Mostramos el resultado.

```
print(resultado_json)
```

Ejemplo de salida:

```
[
  {
    "Nombre del cliente": "Ana",
    "Apellidos del cliente": "Sánchez",
    "Edad del cliente": 25
  },
  {
    "Nombre del cliente": "Fátima",
    "Apellidos del cliente": "Quiñones",
    "Edad del cliente": 20
  }
]
```

Cerramos la conexión.

```
conexion.close()
```

---

Código de SQL:

```
-- sudo mysql -u root -p

CREATE DATABASE clientes;

USE clientes;

CREATE TABLE clientes(
	nombre VARCHAR(255),
	apellidos VARCHAR(255),
	edad INT
);

INSERT INTO clientes VALUES ("Ana","Sánchez",25);
INSERT INTO clientes VALUES ("Fátima","Quiñones",20);

CREATE USER 
'clientes'@'localhost' 
IDENTIFIED  BY 'Clientes123$';

GRANT USAGE ON *.* TO 'clientes'@'localhost';

ALTER USER 'clientes'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON clientes.* 
TO 'clientes'@'localhost';

FLUSH PRIVILEGES;
```

Código de Python:

```
import mysql.connector
import json

conexion = mysql.connector.connect(
  host="localhost",
  user="clientes",
  password="Clientes123$",
  database="clientes"
)

cursor = conexion.cursor(dictionary=True)
cursor.execute('''
  SELECT
  nombre AS "Nombre del cliente",
  apellidos AS "Apellidos del cliente",
  edad AS "Edad del cliente"
  FROM clientes
  ORDER BY edad DESC;
''')

filas = cursor.fetchall()

resultado_json = json.dumps(filas, ensure_ascii=False, indent=2)

print(resultado_json)

conexion.close()
```

---

Hemos comprobado que imprimir en JSON es mucho más limpio que "vomitar" los datos directamente de la base de datos. Este formato es el que usaremos cuando queramos conectar nuestro Backend con un Fronted dinámico o una aplicación de móvil.

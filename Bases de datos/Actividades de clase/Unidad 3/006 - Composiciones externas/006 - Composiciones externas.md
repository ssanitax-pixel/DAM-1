Las composiciones externas (como el `LEFT JOIN`) nos permiten combinar registros de varias tablas incluso cuando no hay una coincidencia exacta en todas ellas. En este ejercicio, nosotros unimos los datos de matrículas con los nombres de alumnos y asignaturas para que la información sea fácil de leer.

Al integrar esto con Flask, nosotros logramos que una base de datos se convierta en una aplicación interactiva. El servidor Python consulta los datos y los envía a una plantilla HTML para que se vean en el navegador.

---

Empezamos creando las tablas para gestionar la escuela. Definimos tablas para `alumnos`, `profesores`, `asignaturas` y `matriculas`. Usamos claves primarias para que cada registro sea único.

```
CREATE DATABASE composiciones;

USE composiciones;

CREATE TABLE alumnos(
    Identificador INT PRIMARY KEY,
    nombre VARCHAR(100),
    apellidos VARCHAR(100)
);

CREATE TABLE matriculas(
    Identificador INT PRIMARY KEY,
    id_asignatura INT,
    id_alumno INT
);
```

Usamos un `LEFT JOIN` para cruzar la tabla de matrículas con alumnos y asignaturas. Guardamos este cruce en una vista llamada `matriculas_join`. Así no tenemos que escribir el código de unión cada vez que hagamos una consulta.

```
CREATE VIEW matriculas_join AS 
SELECT 
    asignaturas.nombre AS 'Nombre de la asignatura',
    alumnos.nombre AS 'Nombre del alumno',
    alumnos.apellidos AS 'Apellidos del alumno'
FROM matriculas
LEFT JOIN asignaturas ON matriculas.id_asignatura = asignaturas.Identificador
LEFT JOIN alumnos ON matriculas.id_alumno = alumnos.Identificador;
```

Creamos un usuario específico llamado `TugaTita`. Le damos todos los permisos sobre la base de datos `composiciones`. También le quitamos cualquier límite de conexión para que la web funcione sin problemas.

```
CREATE USER 
'TugaTita'@'localhost' 
IDENTIFIED  BY 'TugatitaRexulona123$';

GRANT USAGE ON *.* TO 'TugaTita'@'localhost';

ALTER USER 'TugaTita'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON composiciones.* 
TO 'TugaTita'@'localhost';

FLUSH PRIVILEGES;
```

Conectamos Python con la base de datos usando `mysql.connector`. Usamos un cursor con la opción `dictionary=True`. Esto hace que cada fila de datos llegue a Python como un diccionario con nombres de columnas.

```
cursor = conexion.cursor(dictionary=True)
```

Definimos la ruta principal `/`. Ejecutamos la consulta a nuestra vista y guardamos los resultados en una variable. Por último, usamos `render_template` para enviar esos datos al archivo HTML.

```
@app.route("/")
def inicio():
  cursor.execute("SELECT * FROM matriculas_join;")  
  filas = cursor.fetchall()
  return render_template("index.html", datos=filas)
```

Usaremos el motor de plantillas de Flask para recorrer los datos. Usamos un bucle `{% for %}` que repite una tarjeta de alumno por cada registro que hay en la base de datos.

```
{% for linea in datos: %}
    <article>
        </article>
{% endfor %}
```

Mostraremos los datos con las llaves dobles `{{}}` para imprimir los valores. llamamos a cada campo usando los nombres que definimos antes en nuestra vista SQL.

```
<p>Asignatura: {{linea['Nombre de la asignatura']}}</p>
<p>Nombre: {{linea['Nombre del alumno']}}</p>
```

---

Código completo:

1. SQL.

```
CREATE DATABASE IF NOT EXISTS composiciones;
USE composiciones;

CREATE TABLE alumnos(Identificador INT PRIMARY KEY, nombre VARCHAR(100), apellidos VARCHAR(100));
CREATE TABLE asignaturas(Identificador INT PRIMARY KEY, nombre VARCHAR(100), id_profesor INT);
CREATE TABLE matriculas(Identificador INT PRIMARY KEY, id_asignatura INT, id_alumno INT);

CREATE VIEW matriculas_join AS 
SELECT 
asignaturas.nombre AS 'Nombre de la asignatura',
alumnos.nombre AS 'Nombre del alumno',
alumnos.apellidos AS 'Apellidos del alumno'
FROM matriculas
LEFT JOIN asignaturas ON matriculas.id_asignatura = asignaturas.Identificador
LEFT JOIN alumnos ON matriculas.id_alumno = alumnos.Identificador;
```

2. Python.

```
import mysql.connector 
from flask import Flask, render_template

# Conectamos con el usuario que hemos creado
conexion = mysql.connector.connect(
  host="localhost",
  user="TugaTita",
  password="TugatitaRexulona123$",
  database="composiciones"
)  

app = Flask(__name__)

@app.route("/")
def inicio():
  # Sacamos los datos como diccionarios
  cursor = conexion.cursor(dictionary=True) 
  cursor.execute("SELECT * FROM matriculas_join;")  
  filas = cursor.fetchall()
  return render_template("index.html", datos=filas)

if __name__ == "__main__":
  app.run(debug=True)
```

3. HTML.

```
<!doctype html>
<html lang="es">
  <head>
    <style>
      body{font-family:sans-serif;background:aliceblue;}
      section{display:grid;gap:20px;grid-template-columns:repeat(4,100fr);padding:20px;}
      article{border:1px solid indigo;padding:20px;background:white;display:flex;gap:20px;}
    </style>
  </head>
  <body>
    <header><h1>Gestión de escuela</h1></header>
    <section>
        {% for linea in datos: %}
        <article>
            <div class="texto">
                <p>Asignatura: {{linea['Nombre de la asignatura']}}</p>
                <p>Nombre: {{linea['Nombre del alumno']}}</p>
                <p>Apellidos: {{linea['Apellidos del alumno']}}</p>
            </div>
        </article>
        {% endfor %}
    </section>
  </body>
</html>
```

---

Hemos visto cómo las vistas de SQL nos facilitan mucho el trabajo en Python. En lugar de complicar el código del servidor, nosotros dejamos que la base de datos haga el trabajo difícil del cruce de datos.
Combinar Flask con plantillas HTML nos permite crear webs que se actualizan solas cuando cambiamos algo en MySQL. Como estamos en primero, aprender a conectar estas tecnologías es el primer paso para crear aplicaciones web reales y dinámicas.

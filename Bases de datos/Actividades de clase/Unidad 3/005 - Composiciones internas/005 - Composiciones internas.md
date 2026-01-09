En este ejercicio hemos montado un sistema completo que conecta una base de datos MySQL con una página web a través de Flask. Hemos usado la lógica de permisos en la base de datos para crear un usuario seguro y la capacidad de las peticiones web para devolver diferentes tipos de datos como tablas o clientes.
Lo más importante es que hemos conseguido que el Backend hable con el Fronted de forma dinámica, permitiendo que la página se dibuje sola según lo que hay en la base de datos.

---

1. Configuración de la Base de Datos (SQL):

Primero creamos la base de datos llamada `tiendaclase` y usamos el comando `USE` para decirle a MySQL que todas las órdenes siguientes var para ese contenedor.

```
CREATE DATABASE IF NOT EXISTS tiendaclase;
USE tiendaclase;
```

Creamos las tablas de `clientes` y `productos`. Usamos `AUTO_INCREMENT` en los identificadores para que el sistema asigne los números solos y `PRIMARY KEY` para que cada registro sea único.

```
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    fecha_registro VARCHAR(100)
);
```

```
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0
);
```

Insertamos datos de ejemplo para verificar que todo funciona.

```
INSERT INTO clientes (nombre, email, telefono)
VALUES
    ('Ana López', 'ana@example.com', '600123456'),
    ('Carlos Ruiz', 'carlos@example.com', '611987654'),
    ('María Gómez', 'maria@example.com', '622111222');
```

```
INSERT INTO productos (nombre, descripcion, precio, stock)
VALUES
    ('Portátil 15"', 'Portátil de 15 pulgadas con 16GB RAM', 899.99, 10),
    ('Ratón inalámbrico', 'Ratón óptico inalámbrico', 19.90, 50),
    ('Teclado mecánico', 'Teclado con switches azules', 59.95, 30);
```

Creamos un usuario nuevo, le ponemos una contraseña y le damos permisos totales pero solo sobre nuestra base de datos.

```
CREATE USER 'tiendaclase'@'localhost' IDENTIFIED BY 'tiendaclase123$';
GRANT ALL PRIVILEGES ON tiendaclase.* TO 'tiendaclase'@'localhost';
FLUSH PRIVILEGES;
```

2. Lógica del servidor (Python/Flask):

Usamos la variable `g` de Flask para guardar la conexión a la base de datos. Esto es mejor porque así la conexión solo se abre cuando hace falta y se cierra sola cuando termina la petición, evitando que el servidor se sature.

```def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(user="tiendaclase", ...)
    return g.db
```

Creamos rutas como /clientes que devuelven los datos. Usamos cursor.execute para lanzar la consulta de SQL y jsonify para que Python convierta los resultados en una lista que el navegador pueda leer.

```
@app.route("/clientes")
def clientes():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM clientes;")
    return jsonify(cursor.fetchall())
```

3. Interfaz dinámica (HTML/JavaScript):

En el HTML creamos un menú lateral (`nav`) y una zona principal (`main`). Les ponemos un `id` para poder seleccionarlos luego con JavaScript.

```
<nav id="menu"></nav>
<main id="contenido"></main>
```

Usamos `fetch` para llamar a la URL `/tablas`. Cuando recibimos la respuesta, usamos un bucle `forEach` para crear un botón por cada tabla que exista en la base de datos y lo metemos en el menú.

```
fetch("/tablas")
.then(function(res){ return res.json(); })
.then(function(tablas){
    tablas.forEach(function(nombre){
        let b = document.createElement("button");
        b.textContent = nombre;
        // Metemos el botón en el nav
    });
});
```

Hacemos lo mismo para los clientes. Por cada fila de datos que nos da el servidor, creamos una etiqueta `tr` (fila) y dentro tantas etiquetas `td` (celdas) como datos tenga ese cliente. Al final, añadimos toda esa tabla al hueco de `main`.

```
filas.forEach(function(linea){
    let tr = document.createElement("tr");
    linea.forEach(function(dato){
        let td = document.createElement("td");
        td.textContent = dato;
        tr.appendChild(td);
    });
    tabla.appendChild(tr);
});
```

---

El código:

1. SQL:

```
-- Creamos la base de datos si no existe y la seleccionamos
CREATE DATABASE IF NOT EXISTS tiendaclase;
USE tiendaclase;

-- Tabla para almacenar la información de los clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    fecha_registro VARCHAR(100)
);

-- Tabla para el catálogo de productos
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0
);

-- Insertamos datos de ejemplo para verificar que todo funciona
INSERT INTO clientes (nombre, email, telefono)
VALUES
    ('Ana López', 'ana@example.com', '600123456'),
    ('Carlos Ruiz', 'carlos@example.com', '611987654'),
    ('María Gómez', 'maria@example.com', '622111222');

INSERT INTO productos (nombre, descripcion, precio, stock)
VALUES
    ('Portátil 15"', 'Portátil de 15 pulgadas con 16GB RAM', 899.99, 10),
    ('Ratón inalámbrico', 'Ratón óptico inalámbrico', 19.90, 50),
    ('Teclado mecánico', 'Teclado con switches azules', 59.95, 30);
```

2. Python:

```
import mysql.connector 
from flask import Flask, render_template, jsonify, g

app = Flask(__name__)

# Función para obtener la conexión a la base de datos de forma segura
def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host="localhost",
            user="tiendaclase",
            password="tiendaclase123$",
            database="tiendaclase"
        )
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route("/")
def raiz():
    return render_template("index.html")

@app.route("/clientes")
def clientes():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM clientes;")
    filas = cursor.fetchall()
    cursor.close()
    return jsonify(filas)

@app.route("/tablas")
def tablas():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SHOW TABLES;")
    filas = cursor.fetchall()
    cursor.close()
    return jsonify([fila[0] for fila in filas])

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
```

3. HTML:

```
<!doctype html>
<html>
   <head>
       <style>
           html,body{height:100%;padding:0px;margin:0px;display:flex;width:100%;}
           nav{background:RebeccaPurple;flex:1;color:white;padding:20px;}
           main{flex:4;background:MediumPurple;padding:20px;}
       </style>
   </head>
   <body>
       <nav>ssanitax | panel</nav>
       <style>
           nav{display:flex;flex-direction:column;gap:20px;}
           nav button{border:none;background:white;color:RebeccaPurple;padding:20px;
           text-transform:uppercase;}
       </style>
       <script>
           // En primer lugar cargamos datos de un json
           fetch("http://127.0.0.1:5000/tablas")
           .then(function(respuesta){
               return respuesta.json(); // La resp viene en JSON
           })
           .then(function(datos){
               // Y luego creamos botones a partir de lo que hay en el json
           		let contenedor = document.querySelector("nav")
                datos.forEach(function(texto_boton){
                	let boton = document.createElement("button")
                    boton.textContent = texto_boton;
                    contenedor.appendChild(boton);
                })
           })
       </script>
       <main>2</main>
       <style>
           table{border:3px solid violet;border-collapse:collapse;background:white;}
           table tr:first-child{background:violet;color:white;}
           table tr td{padding:10px;border-right:1px solid violet;}
       </style>
       <script>
           // En primer lugar cargamos datos de un json
           fetch("http://127.0.0.1:5000/clientes")
           .then(function(respuesta){
               return respuesta.json(); // La resp viene en JSON
           })
           .then(function(datos){
               // Selecciono el contenedor de la tabla
               let contenedor = document.querySelector("main");
               // Primero creo una tabla en memoria
               let tabla = document.createElement("table");
               // Al cuerpo le añado la tabla
               contenedor.appendChild(tabla); 
               // Para cada una de las lineas del json:
               datos.forEach(function(linea){
               		// Primero creo una fila - table row
                   let fila = document.createElement("tr");
                   // Ahora creo tantas celdas como sea necesario
                   linea.forEach(function(celda){
                       	// Creo una celda vacia HTML
                   		let data = document.createElement("td");
                       	// Le pongo el texto a la celda
                       	data.textContent = celda
                       	// A la fila, le añado la celda
                       	fila.appendChild(data);
                   })
                   // A la tabla le añado esta fila
                   tabla.appendChild(fila)
               })
           })
       </script>
   </body>
</html>
```

---

Hemos logrado unir todo lo aprendido: el diseño de bases de datos, la seguridad de usuarios y la creación de interfaces web dinámicas. Como estamos en primero, esto nos enseña que el código no solo sirve para ver números en una terminal, sino para crear herramientas que la gente puede usar desde su navegador.

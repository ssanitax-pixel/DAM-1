En este ejericico hemos visto la aquitectura de las aplicaciones web dinámicas. La base de todo es la separación de respoonsabilidades.

Mientras que SQL se encarga de que los datos se guarden y la estruccturación de los datos, Python actúa como el motor lógico que procesa la información y HTML/CSS se encarga de la presentación visual.

---

Parte 1: SQL

Creamos una base de datos.

```
CREATE DATABASE tiendapatos;
```

Seleccionamos la base de datos, para meternos dentro de ella.

```
USE tiendapatos;
```

Creamos la tabla de `categorias`.

```
CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);
```

Creamos la tabla de `productos`.

```
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    id_categoria INT NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);
```

Insertamos los datos en las categorías, se tienen que insertar primero, ya que los productos dependen de las categorías.

```
INSERT INTO categorias (nombre) VALUES ('Profesiones'), ('Superhéroes');
```

Insertamos seguidamente los productos.

```
INSERT INTO productos (nombre, precio, id_categoria) VALUES 
('Pato Programador', 12.50, 1),
('Pato Batman', 15.99, 2),
...
```

Creamos una vista para facilitar más adelante ver los productos.

```
CREATE VIEW vw_patos AS
SELECT p.nombre, p.precio, c.nombre AS categoria
FROM productos p
JOIN categorias c ON p.id_categoria = c.id_categoria;
```

Creamos un usuario exclusivo para la tienda.

```
CREATE USER 'patos_user'@'localhost' IDENTIFIED BY 'Patos123$';
```

Eliminamos restricciones y damos permisos al usuario.

```
ALTER USER 'patos_user'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON tiendapatos.* TO 'patos_user'@'localhost';
```

Aplicamos los cambios.

```
FLUSH PRIVILEGES;
```

Parte 2: Python con Flask

Creamos las importaciones de las librerías que vamos a necesitar, para crear el servidor, enviar HTML al navegador y conectar Python con MySQL.

```
from flask import Flask, render_template
import mysql.connector
```

Abrimos una conexión con MySQL.

```
conexion = mysql.connector.connect(
    host="localhost",
    user="patos_user",      
    password="Patos123$",  
    database="tiendapatos"
)
```

Ejecutamos el cursor para poder realizar consultas SQL, y hacemos que cada fila sea un diccionario.

```
cursor = conexion.cursor(dictionary=True)
```

Creamos el servidor Flask, esto crea la aplicación web.

```
app = Flask(__name__)
```

Definimos cómo se va a llamar la ruta principal.

```
@app.route("/")
def inicio():
```

Que dentro de ella será donde se visualizará la vista que creamos anteriormente para ver los datos de los patos.

```
cursor.execute("SELECT * FROM vw_patos;")
```

Obtenemos los resultados.

```
resultados = cursor.fetchall()
```

Enviamos los datos al HTML.

```
return render_template("inicio.html", patos=resultados)
```

Creamos la ruta `sobremi`, esta será una página estática.

```
@app.route("/sobremi")
def sobremi():
    return render_template("sobremi.html")
```

Creamos la ruta `contacto`, que será un formulario.

```
@app.route("/contacto")
def contacto():
    return render_template("contacto.html")
```

Arrancamos el servidor.

```
if __name__ == "__main__":
    app.run(debug=True)
```

---

El código de todos los archivos quedará así.

tiendapatos.sql

```
-- Creamos el entorno para los patos
CREATE DATABASE tiendapatos;
USE tiendapatos;

CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    id_categoria INT NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

-- Insertamos datos de ejemplo siguiendo el orden jerárquico
INSERT INTO categorias (nombre) VALUES ('Profesiones'), ('Superhéroes');
INSERT INTO productos (nombre, precio, id_categoria) VALUES ('Pato Programador', 12.50, 1),
('Pato Batman', 15.99, 2),
('Pato Spiderman', 15.99, 2),
('Pato Wonder Woman', 16.50, 2),
('Pato Iron Man', 17.00, 2),
('Pato Hulk', 14.99, 2),
('Pato Joker', 15.00, 2);

-- Creamos la vista para facilitar la consulta desde Flask
CREATE VIEW vw_patos AS
SELECT p.nombre, p.precio, c.nombre AS categoria
FROM productos p
JOIN categorias c ON p.id_categoria = c.id_categoria;

-- 1. Creamos el usuario de la tienda
CREATE USER 'patos_user'@'localhost' IDENTIFIED BY 'Patos123$';

-- 2. Configuramos sus límites (opcional pero recomendado en el temario)
ALTER USER 'patos_user'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- 3. Le damos el control total sobre la base de datos de patos
GRANT ALL PRIVILEGES ON tiendapatos.* TO 'patos_user'@'localhost';

-- 4. Aplicamos los cambios inmediatamente
FLUSH PRIVILEGES;
```

103 - Jinja.py

```
from flask import Flask, render_template
import mysql.connector # Importamos el conector

conexion = mysql.connector.connect(
    host="localhost",
    user="patos_user",      
    password="Patos123$",  
    database="tiendapatos"
)

cursor = conexion.cursor(dictionary=True)

app = Flask(__name__)

# Definimos las tres rutas principales
@app.route("/")
def inicio():
    # Consultamos la vista de patos
    cursor.execute("SELECT * FROM vw_patos;")
    resultados = cursor.fetchall()
    return render_template("inicio.html", patos=resultados)

@app.route("/sobremi")
def sobremi():
    return render_template("sobremi.html") # Servimos la página de perfil

@app.route("/contacto")
def contacto():
    return render_template("contacto.html") # Servimos el formulario
    
if __name__ == "__main__":
    app.run(debug=True)
```

inicio.html

```
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>Tienda de Patos - Inicio</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; background: #f4f4f4; }
        header { background: PaleVioletRed; color: white; padding: 20px; text-align: center; }
        nav { background: #333; padding: 10px; text-align: center; }
        nav a { color: white; margin: 0 15px; text-decoration: none; font-weight: bold; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 20px; padding: 20px; }
        .pato { background: white; border-radius: 8px; padding: 15px; text-align: center; border: 1px solid #ddd; }
    </style>
</head>
<body>
    <header><h1>🦆 Cuac-Store 🦆</h1></header>
    <nav>
        <a href="/">Catálogo</a>
        <a href="/sobremi">Nuestra Historia</a>
        <a href="/contacto">Contacto</a>
    </nav>
    <main class="grid">
        {% for pato in patos %}
        <article class="pato">
            <h3>{{ pato.nombre }}</h3>
            <p>Precio: <strong>{{ pato.precio }}€</strong></p>
            <p>Colección: {{ pato.categoria }}</p>
        </article>
        {% endfor %}
    </main>
</body>
</html>
```

sobremi.html

```
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>Tienda de Patos - Inicio</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; background: #f4f4f4; }
        header { background: PaleVioletRed; color: white; padding: 20px; text-align: center; }
        nav { background: #333; padding: 10px; text-align: center; }
        nav a { color: white; margin: 0 15px; text-decoration: none; font-weight: bold; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 20px; padding: 20px; }
        .pato { background: white; border-radius: 8px; padding: 15px; text-align: center; border: 1px solid #ddd; }
    </style>
</head>
<body>
    <nav>
        <a href="/">Catálogo</a>
        <a href="/sobremi">Nuestra Historia</a>
        <a href="/contacto">Contacto</a>
    </nav>
    <main style="padding:40px; text-align:center;">
        <h2>Pasión por el caucho</h2>
        <p>En Cuac-Store empezamos como coleccionistas y ahora automatizamos la venta de patos dinámicamente.</p>
    </main>
</body>
</html>
```

contacto.html

```
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>Tienda de Patos - Inicio</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; background: #f4f4f4; }
        header { background: PaleVioletRed; color: white; padding: 20px; text-align: center; }
        nav { background: #333; padding: 10px; text-align: center; }
        nav a { color: white; margin: 0 15px; text-decoration: none; font-weight: bold; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 20px; padding: 20px; }
        .pato { background: white; border-radius: 8px; padding: 15px; text-align: center; border: 1px solid #ddd; }
    </style>
</head>
<body>
    <nav>
        <a href="/">Catálogo</a>
        <a href="/sobremi">Nuestra Historia</a>
        <a href="/contacto">Contacto</a>
    </nav>
    <main style="padding:40px;">
        <h2>¿Dudas sobre un pato?</h2>
        <form>
            <input type="text" placeholder="Tu nombre" style="display:block; margin-bottom:10px; width:300px;">
            <input type="email" placeholder="Email" style="display:block; margin-bottom:10px; width:300px;">
            <textarea placeholder="Mensaje" style="display:block; margin-bottom:10px; width:300px;"></textarea>
            <button type="submit" style="background:PaleVioletRed; color:white; border:none; padding:10px 20px;">Enviar</button>
        </form>
    </main>
</body>
</html>
```

---

Hemos practicado la creación de ecosistemas web profesionales y dinámicos. A través de la construcción de la Tienda de Patos de Goma, hemos demostrado cómo la arquitectura MVC permite una gestión eficiente al separar por completo el almacenamiento de los datos de su representación visual.

Hemos pasado de una idea de negocio a una implementación real donde la base de datos MySQL, protegida por un usuario con permisos específicos, alimenta un servidor Flask que procesa la lógica de negocio y sirve plantillas inteligentes en HTML. Al emplear Jinja2 para iterar sobre los registros de patos, hemos optimizado el desarrollo, reduciendo la carga de trabajo manual y asegurando que la interfaz no sea "tosca", sino fluida y escalable.

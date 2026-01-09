En este ejercicio se trabaja el concepto de **generación de contenido dinámico en aplicaciones web** mediante el uso del microframework **Flask**, una herramienta ligera y potente de Python. Flask permite crear servidores web y definir rutas que devuelven contenido HTML, lo que facilita la construcción de páginas dinámicas en lugar de estáticas.
Además, se emplea el manejo de archivos **JSON**, un formato muy utilizado para almacenar y transportar datos estructurados. En este caso, el archivo JSON actúa como la fuente de información del blog, conteniendo los artículos con sus respectivos títulos, fechas, autores y contenidos.
La práctica tiene como objetivo comprender cómo una aplicación web puede **leer datos externos**, procesarlos desde el servidor con Python y mostrarlos dinámicamente al usuario a través del navegador. Con ello, se integran conceptos fundamentales del desarrollo web backend, como la lectura de archivos, la manipulación de datos y la generación de código HTML desde un programa.

---

Importamos flask y json.

```
from flask import Flask
import json
```

Creamos una instancia de la aplicacion `Flask`.

```
aplicacion = Flask(__name__)
```

Definimos la ruta raiz para que devuelva un contenido HTML dinámico.

```
@aplicacion.route("/")
```

Abrimos el archivo JSON para leer los datos del blog.

```
    archivo = open("blog.json",'r')
    contenido = json.load(archivo)
```

Procesamos cada entrada del JSON y construimos una cadena HTML con ella.

```
    for linea in contenido:
        cadena+= '''
          <article>
            <h3>'''+linea['titulo']+'''</h3>
            <time>'''+linea['fecha']+'''</time>
            <p>'''+linea['autor']+'''</p>
            <p>'''+linea['contenido']+'''</p>
          </article>
```

Por último lo habrimos para asegurarnos que el código funciona correctamente.

---

Así queda el código completo:

```
# Abre una terminal e instala flask:
# pip install flask
# Flask es un microservidor web que nos permite genrear HTML desde Python

from flask import Flask
import json

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    ################# Bloque
    cadena = '''
    <!doctype html>
<html lang="es">
  <head>
    <title>AnaSSblog</title>
    <meta charset="utf-8">
    <style>
      body{background:steelblue;color:steelblue;font-family:sans-serif;}
      header,main,footer{background:white;padding:20px;margin:auto;width:600px;}
      header,footer{text-align:center;}
      main{color:black;}
    </style>
  </head>
  <body>
    <header><h1>Ana Sánchez Blog</h1></header>
    <main>
    '''
    ############## bloque
    archivo = open("blog.json",'r')
    contenido = json.load(archivo)
    for linea in contenido:
        cadena+= '''
          <article>
            <h3>'''+linea['titulo']+'''</h3>
            <time>'''+linea['fecha']+'''</time>
            <p>'''+linea['autor']+'''</p>
            <p>'''+linea['contenido']+'''</p>
          </article>
          '''
    ###################### bloque
    cadena += '''
    </main>
    <footer>(c)2025 Ana Sánchez Suárez</footer>
  </body>
</html>
    '''
    ####################### no olvidar return
    return cadena
    
# Ahora arranco el servidor
if __name__ == "__main__":
    aplicacion.run(debug=True)
```

---

Con la realización de este ejercicio, se ha creado una **aplicación web funcional** que muestra artículos de un blog almacenados en un archivo JSON, utilizando Flask como servidor web.
Durante el desarrollo, se aplicaron los pasos esenciales: importar las bibliotecas necesarias, crear la instancia de la aplicación Flask, definir la ruta principal y generar dinámicamente el contenido HTML a partir de los datos leídos del archivo JSON.
El resultado demuestra cómo Python puede interactuar con datos externos y transformarlos en contenido visible en una página web, sentando las bases para la creación de sitios más complejos y dinámicos.
Este ejercicio representa un ejemplo práctico de la conexión entre la **programación del lado del servidor** (backend) y la **presentación visual en el navegador** (frontend), reforzando los conocimientos sobre la generación dinámica de contenido web en el desarrollo de aplicaciones interactivas.

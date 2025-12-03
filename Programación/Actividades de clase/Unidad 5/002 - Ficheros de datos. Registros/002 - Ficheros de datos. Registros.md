En este ejercicio hemos desarrollado una aplicación web sencilla usando **Flask** y **JSON**.
El objetivo era aprender a leer información guardada en un fichero y mostrarla en una página web.
Para ello, hemos utilizado Flask para crear la aplicación y definir la ruta principal, y el módulo `json` para leer los datos del archivo `blog.json`.

El fichero JSON contiene varios artículos de un blog, cada uno con su título, fecha, autor y contenido.
La aplicación lee ese fichero, recorre todos los artículos y genera de forma dinámica el código HTML que se mostrará en el navegador.

---

Primero importamos las librerías que vamos a usar, en este caso serán Flask y json.

```
from flask import Flask
import json
```

Creamos la aplicación Flask.

```
app = Flask(__name__)
```

Definimos la ruta principal de la web. Con `@app.route('/')` indicamos que cuando entremos a la página principal `(/)` se va a ejecutar la función `mostrar_blog()`.

```
@app.route('/')
def mostrar_blog():
```

Dentro de la función, abrimos el archivo `blog.json` para leer los datos.
Usamos `with open` para abrir el archivo y que se cierre automáticamente después.
Con `json.load(archivo)` convertimos el contenido del fichero JSON en una lista de diccionarios de Python.

```
    with open('blog.json', 'r', encoding='utf-8') as archivo:
        articulos = json.load(archivo)
```

A continuación, creamos una cadena de texto que contendrá el código HTML de la página.
Esto es lo que Flask devolverá al navegador.

```
    cadena = '''
    <html>
        <head>
            <title>Mi Blog</title>
            <meta charset="UTF-8">
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f9f9f9;
                    margin: 40px;
                }
                h1 { color: #333; }
                .articulo {
                    background-color: white;
                    border-radius: 10px;
                    padding: 20px;
                    margin-bottom: 20px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                }
                .fecha, .autor {
                    color: gray;
                    font-size: 0.9em;
                }
            </style>
        </head>
        <body>
            <h1>Blog de Ana Sánchez Suárez</h1>
    '''
```

Usamos un bucle `for` para recorrer todos los artículos y los vamos añadiendo a la variable `cadena`.

```
    for articulo in articulos:
        cadena += '''
        <div class="articulo">
            <h2>'''+articulo['titulo']+'''</h2>
            <p class="fecha">'''+articulo['fecha']+'''</p>
            <p class="autor">'''+articulo['autor']+'''</p>
            <p>'''+articulo['contenido']+'''</p>
        </div>
        '''
```

Al final, cerramos las etiquetas `<body>` y `<html>` para completar la estructura.
La función `return` devuelve la cadena con todo el html, y eso es lo que se mostrará en el navegador.

```
    cadena += '''
        </body>
    </html>
    '''

    return cadena
```

Añadimos este bloque para que la aplicación se ejecute cuando lanzamos el archivo.

```
if __name__ == '__main__':
    app.run(debug=True)
```

---

El código completo quedará así:

```
from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def mostrar_blog():
    with open('blog.json', 'r', encoding='utf-8') as archivo:
        articulos = json.load(archivo)

    cadena = '''
    <html>
        <head>
            <title>Mi Blog</title>
            <meta charset="UTF-8">
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f9f9f9;
                    margin: 40px;
                }
                h1 { color: #333; }
                .articulo {
                    background-color: white;
                    border-radius: 10px;
                    padding: 20px;
                    margin-bottom: 20px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                }
                .fecha, .autor {
                    color: gray;
                    font-size: 0.9em;
                }
            </style>
        </head>
        <body>
            <h1>Blog de Ana Sánchez Suárez</h1>
    '''

    for articulo in articulos:
        cadena += '''
        <div class="articulo">
            <h2>'''+articulo['titulo']+'''</h2>
            <p class="fecha">'''+articulo['fecha']+'''</p>
            <p class="autor">'''+articulo['autor']+'''</p>
            <p>'''+articulo['contenido']+'''</p>
        </div>
        '''

    cadena += '''
        </body>
    </html>
    '''

    return cadena


if __name__ == '__main__':
    app.run(debug=True)
```

---

Hemos visto de forma práctica cómo se puede leer información desde un fichero JSON y mostrarla en una aplicación web creada con Flask.
Hemos manejado datos estructurados en formato JSON, a recorrerlos con un bucle for y a generar contenido HTML desde Python.

Además, este trabajo nos ayuda a comprender la relación entre el backend (donde se procesan los datos) y el frontend (lo que ve el usuario).

Importamos flask.

```
from flask import Flask
```

Importamos el conector a base de datos.

```
import mysql.connector
```

Nos conectamos a la base de datos.

```
conexion = mysql.connector.connect(
    host="localhost",
    user="usuario2",
    password="Portafolio123#",
    database="portafolioexamen"
    )
```

Creamos un cursor

```
cursor = conexion.cursor()
```

Creamos una aplicación de flask

```
app = Flask(__name__)
```

Atrapamos la ruta raiz.

```
@app.route("/")
```

Defino la función.

```
def raiz():
```

Pido el contenido de la vista.

```
    cursor.execute("SELECT * FROM vista_categorias;")
```

Lo guardo en una lista.

```
    resultados = cursor.fetchall()
```

Ponemos el inicio hasta el main.

```
    cadena = '''
    <!DOCTYPE html>
    <html lang="es">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Portafolio de Arte</title>
        <style>
          /* Reset general */
          * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
          }

          /* Body y fondo */
          body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            color: #333;
          }

          /* Header */
          header {
            background-color: PaleVioletRed;
            color: white;
            padding: 20px;
            text-align: center;
          }

          header h1 {
            margin: 10px 0;
          }

          header p {
            font-size: 1.1rem;
            margin-top: 5px;
          }

          /* Main */
          main {
            padding: 20px;
          }

          .portfolio {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
          }

          .piece {
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 15px;
          }

          .piece-title {
            font-size: 1.5rem;
            color: #333;
            margin-bottom: 10px;
          }

          .piece-description {
            font-size: 1rem;
            margin-bottom: 10px;
          }

          .piece-image {
            width: 100%;
            border-radius: 8px;
            margin-bottom: 10px;
          }

          .piece-category {
            font-weight: bold;
            font-size: 1.1rem;
          }

          /* Footer */
          footer {
            background-color: PaleVioletRed;
            color: white;
            text-align: center;
            padding: 15px;
            position: relative;
            width: 100%;
            bottom: 0;
          }
        </style>
      </head>
      <body>

        <!-- Header -->
        <header>
          <div class="header-content">
            <h1>Ana Sánchez Suárez - Portafolio</h1>
            <p>Email: ssanitax@gmail.com</p>
          </div>
        </header>

        <!-- Main -->
        <main>
          <section class="portfolio">
    '''
```

Para cada elemento de la lista.

```
    for fila in resultados:
```

Aquí ponemos lo que se repite.

```
        cadena += '''
        <article class="piece">
          <h2 class="piece-title">'''+fila[0]+'''</h2>
          <p class="piece-description">'''+fila[1]+'''</p>
          <p><strong>Fecha: </strong>'''+fila[2]+'''</p>
          <p class="piece-category"><strong>Categoría: </strong>'''+fila[3]+'''</p>
        </article>
        '''
```

Aqui ponemos el final.

```
    cadena += '''
    </section>
    </main>

    <!-- Footer -->
    <footer>
      <p>&copy; 2025 Ana Sánchez Suárez. Todos los derechos reservados.</p>
    </footer>

  </body>
</html>
    '''
    return cadena
```

Si este es el archivo principal, se ejecutará la web.

```
if __name__ == "__main__":
    app.run(debug=True)
```

---

El código completo nos quedará así:

```
from flask import Flask
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="usuario2",
    password="Portafolio123#",
    database="portafolioexamen"
    )
cursor = conexion.cursor()
app = Flask(__name__)

@app.route("/")
def raiz():
    cursor.execute("SELECT * FROM vista_categorias;")

    resultados = cursor.fetchall()

    cadena = '''
    <!DOCTYPE html>
    <html lang="es">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Portafolio de Arte</title>
        <style>
          /* Reset general */
          * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
          }

          /* Body y fondo */
          body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            color: #333;
          }

          /* Header */
          header {
            background-color: PaleVioletRed;
            color: white;
            padding: 20px;
            text-align: center;
          }

          header h1 {
            margin: 10px 0;
          }

          header p {
            font-size: 1.1rem;
            margin-top: 5px;
          }

          /* Main */
          main {
            padding: 20px;
          }

          .portfolio {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
          }

          .piece {
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 15px;
          }

          .piece-title {
            font-size: 1.5rem;
            color: #333;
            margin-bottom: 10px;
          }

          .piece-description {
            font-size: 1rem;
            margin-bottom: 10px;
          }

          .piece-image {
            width: 100%;
            border-radius: 8px;
            margin-bottom: 10px;
          }

          .piece-category {
            font-weight: bold;
            font-size: 1.1rem;
          }

          /* Footer */
          footer {
            background-color: PaleVioletRed;
            color: white;
            text-align: center;
            padding: 15px;
            position: relative;
            width: 100%;
            bottom: 0;
          }
        </style>
      </head>
      <body>

        <!-- Header -->
        <header>
          <div class="header-content">
            <h1>Ana Sánchez Suárez - Portafolio</h1>
            <p>Email: ssanitax@gmail.com</p>
          </div>
        </header>

        <!-- Main -->
        <main>
          <section class="portfolio">
    '''

    for fila in resultados: # Para cada elemento de la lista
        cadena += '''
        <article class="piece">
          <h2 class="piece-title">'''+fila[0]+'''</h2>
          <p class="piece-description">'''+fila[1]+'''</p>
          <p><strong>Fecha: </strong>'''+fila[2]+'''</p>
          <p class="piece-category"><strong>Categoría: </strong>'''+fila[3]+'''</p>
        </article>
        '''

    cadena += '''
    </section>
    </main>

    <!-- Footer -->
    <footer>
      <p>&copy; 2025 Ana Sánchez Suárez. Todos los derechos reservados.</p>
    </footer>

  </body>
</html>
    '''
    return cadena
      
if __name__ == "__main__":
    app.run(debug=True)
```

---

Este ejercicio demuestra cómo conectar una base de datos MySQL a una aplicación Flask, procesar datos y generar contenido dinámico en una página web. La estructura del proyecto permite que la información de la base de datos se muestre de manera interactiva, combinando backend y frontend de forma eficiente.

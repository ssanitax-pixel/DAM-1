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

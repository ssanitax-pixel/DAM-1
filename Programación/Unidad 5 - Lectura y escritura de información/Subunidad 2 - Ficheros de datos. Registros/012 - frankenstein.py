# Abre una terminal e instala flask:
# pip install flask
# Flask es un microservidor web que nos permite genrear HTML desde Python

from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    return '''
    <!doctype html>
<html lang="es">
  <head>
    <title>EL BLOG DE ANA</title>
    <meta charset="utf-8">
    <style>
      body{background:steelblue;color:steelblue;font-family:sans-serif;}
      header,main,footer{background:white;padding:20px;margin:auto;width:600px;}
      main{color:black;}
    </style>
  </head>
  <body>
    <header><h1>EL BLOG DE ANA</h1></header>
    <main>
      <article>
        <h3>Titulo del articulo</h3>
        <time>2025-11-01</time>
        <p>Ana Sánchez Suárez</p>
        <p>Este es el contenido de un artículo ficticio</p>
      </article>
    </main>
    <footer>(c)2025 Ana Sánchez Suárez</footer>
  </body>
</html>
    '''
    
# Ahora arranco el servidor
if __name__ == "__main__":
    aplicacion.run(debug=True)

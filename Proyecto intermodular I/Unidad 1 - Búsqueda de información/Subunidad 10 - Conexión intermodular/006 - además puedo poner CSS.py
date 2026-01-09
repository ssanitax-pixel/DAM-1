# Abre una terminal e instala Flask
# pip install flask
# Flask es un microservidor web que nos permite generar HTML desde Python

# Importo la librería Flask
from flask import Flask

# Creo una nueva aplicación
aplicacion = Flask(__name__)

# Defino que ocurre en una ruta inicial (/)
@aplicacion.route("/")
def raiz():
    return '''
        <!doctype html>
        <html>
            <head>
                <title>Hola Python</title>
                <style>
                    p{color:purple;}
                </style>
            </head>
            <body>
                <p>Si estás viendo esto, es que te lo está dando Python</p>
            </body>
        </html>
    '''
    
# Ahora arranco el servidor
if __name__ == "__main__":
    aplicacion.run(debug=True)

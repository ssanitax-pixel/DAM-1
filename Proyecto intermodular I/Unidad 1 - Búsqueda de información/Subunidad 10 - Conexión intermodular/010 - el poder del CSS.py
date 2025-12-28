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
    suma = 4+3
    cadena = '''
        <!doctype html>
        <html>
            <head>
                <title>Hola Python</title>
                <style>
                    .dia{
                        width:100px;
                        height:100px;
                        border:1px solid grey;
                    }
                </style>
            </head>
            <body>
                <div class="mes">
    '''
    
    for dia in range(1,31):
        cadena += '<div class="dia">'+str(dia)+'</div>'
    
    cadena += '''
                </div>
            </body>
        </html>
    '''
    return cadena
    
# Ahora arranco el servidor
if __name__ == "__main__":
    aplicacion.run(debug=True)

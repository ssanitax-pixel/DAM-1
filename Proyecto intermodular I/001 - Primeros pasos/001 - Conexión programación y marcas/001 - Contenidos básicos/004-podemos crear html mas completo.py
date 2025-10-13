# sudo apt install python3-pip - si no tenéis PIP en Ubuntu
# pip install flask - Windows
# pip install flask - Linux o macOS

from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    return '''
        <!doctype html>
        <html>
            <head>
                <title></title>
                <style>
                    h1{color:red;}
                </style>
            </head>
            <body>
                <h1>Esto es HTML a tope de power</h1>
            </body>
        </html>
    '''

if __name__ == "__main__":
    aplicacion.run(debug=True)

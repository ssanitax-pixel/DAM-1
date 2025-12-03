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
 

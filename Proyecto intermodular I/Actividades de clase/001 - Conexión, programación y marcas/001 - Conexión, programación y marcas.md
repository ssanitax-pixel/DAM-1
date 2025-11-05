Este ejercicio nos sirve para practicar el concepto impartido en clase sobre Flask y cómo crear aplicaciones web con HTML dinámico.

---

Abrimos nuestro terminal, para comenzar a instalar `flask`, y al estar en el sistema operativo Ubuntu pondremos el siguiente comando.

```
pip3 install flask
```

En la carpeta de nuestro proyecto, creamos un archivo llamado `app.py`. Y añadimos el código que nos han proporcionado.

```
from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  cadena = '''
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
  '''
          
  for dia in range(1,31):
    cadena += '<div>'+str(dia)+'</div>' 
        
         
  cadena += '''
      </body>
    </html>
  '''
  return cadena
  
if __name__ == "__main__":
  aplicacion.run(debug=True)
```

Ahora en la terminal, ejecutamos el archivo y podremos ver nuestra aplicación web en nuestro navegador visitando :`http://127.0.0.1:5000/`.

```
python3 app.py
```

---

Este ejercicio nos ayuda a entender cómo crear aplicaciones web dinámicas con Flask, manipulando HTML desde Python. Hemos probado a modificar el código para agregar más elementos o cambiar estilos según nuestras preferencias. 

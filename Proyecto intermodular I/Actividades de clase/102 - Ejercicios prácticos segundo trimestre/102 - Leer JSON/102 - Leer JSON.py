# Importamos las librerías necesarias para la web y los datos
from flask import Flask, render_template
import json

# Ceamos la aplicación
app = Flask(__name__)

# Definimos la ruta principal
@app.route("/")
def inicio():
    # Abrimos el JSON mejorado
    with open("static/curriculum.json", "r", encoding="utf-8") as file:
        datos = json.load(file)
    
    # Renderizamos la plantilla enviando los datos estructurados
    return render_template("index.html", info=datos)

# Arrancamos el servidor en modo desarrollo
if __name__ == "__main__":
    app.run(debug=True)

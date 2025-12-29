from flask import Flask, render_template
import mysql.connector # Importamos el conector

conexion = mysql.connector.connect(
    host="localhost",
    user="patos_user",      
    password="Patos123$",  
    database="tiendapatos"
)

cursor = conexion.cursor(dictionary=True)

app = Flask(__name__)

# Definimos las tres rutas principales
@app.route("/")
def inicio():
    # Consultamos la vista de patos
    cursor.execute("SELECT * FROM vw_patos;")
    resultados = cursor.fetchall()
    return render_template("inicio.html", patos=resultados)

@app.route("/sobremi")
def sobremi():
    return render_template("sobremi.html") # Servimos la página de perfil

@app.route("/contacto")
def contacto():
    return render_template("contacto.html") # Servimos el formulario
    
if __name__ == "__main__":
    app.run(debug=True)

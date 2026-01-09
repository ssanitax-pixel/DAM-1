import mysql.connector 
from flask import Flask, render_template

# Conectamos con el usuario que hemos creado
conexion = mysql.connector.connect(
  host="localhost",
  user="TugaTita",
  password="TugatitaRexulona123$",
  database="composiciones"
)  

app = Flask(__name__)

@app.route("/")
def inicio():
  # Sacamos los datos como diccionarios
  cursor = conexion.cursor(dictionary=True) 
  cursor.execute("SELECT * FROM matriculas_join;")  
  filas = cursor.fetchall()
  return render_template("index.html", datos=filas)

if __name__ == "__main__":
  app.run(debug=True)

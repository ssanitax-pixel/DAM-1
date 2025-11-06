from flask import Flask # Importo flask
import mysql.connector  # Importo el conector a base de datos

conexion = mysql.connector.connect(
    host="localhost",      
    user="usuario1",    
    password="Portafolio123#",  
    database="portafolio"      
    ) # Me conecto a la base de datos
cursor = conexion.cursor() # Creo un cursor
app = Flask(__name__) # creo una aplicacion flask (web)

@app.route("/") # Atrapo la ruta raiz (/)
def raiz(): # defino la funcion
    cursor.execute("SELECT * FROM vista_categorias;") # Pido el contenido de la vista

    resultados = cursor.fetchall() # Lo guardo en una lista
    cadena = "" # creo una cadena vacía
    for fila in resultados: # Para cada elemento de la lista
        cadena += str(fila) # Añado el registro a la cadena
    return cadena
      
if __name__ == "__main__": # si este es el archivo principal
    app.run(debug=True) # ejecuta la web

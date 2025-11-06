from flask import Flask # Importo flask
import mysql.connector                              # Importo el conector a base de datos


conexion = mysql.connector.connect(
    host="localhost",      
    user="usuario1",    
    password="Portafolio123#",  
    database="portafolio"      
) # Me conecto a la base de datos

cursor = conexion.cursor()                          # Creo un cursor

cursor.execute("SELECT * FROM vista_categorias;")   # Pido el contenido de la vista

resultados = cursor.fetchall()                      # Lo guardo en una lista

for fila in resultados:                             # Para cada elemento de la lista
    print(fila)                                       # Lo pinto en pantalla
  
app = Flask(__name__) # creo una aplicacion flask (web)

@app.route("/") # Atrapo la ruta raiz (/)
def holamundo(): # defino la funcion
    return "Hola mundo" # devuelvo algo
    
if __name__ == "__main__": # si este es el archivo principal
    app.run(debug=True) # ejecuta la web

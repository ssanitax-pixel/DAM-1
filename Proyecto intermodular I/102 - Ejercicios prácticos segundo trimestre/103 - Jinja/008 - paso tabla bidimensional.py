from flask import Flask, render_template
import mysql.connector  # Importo MySQL
####################### MySQL ###############################
conexion = mysql.connector.connect(
    host="localhost",user="usuario2",password="Portafolio123#",database="clientes") # datos de conexión a la base de datos
cursor = conexion.cursor() # Creo un cursor MySQL
#----------------- ESTO ENVÍA LAS TABLAS ----------
cursor.execute("SHOW TABLES;") # Muestra las tablas de la base de datos
tablas = [] # Creo una lista vacía
filas = cursor.fetchall() # Lo guardo en la lista
for fila in filas: # Recorro el resultado
    tablas.append(fila[0]) # Lo añado a la lista de tablas
#----------------- ESTO ENVÍA LAS CABECERAS DE LASTABLAS ----------
cursor.execute("SHOW COLUMNS in productos;") # Muestra las tablas de la base de datos
columnas = [] # Creo una lista vacía
filas = cursor.fetchall() # Lo guardo en la lista
for fila in filas: # Recorro el resultado
    columnas.append(fila[0]) # Lo añado a la lista de tablas
#----------------- ESTO ENVÍA TODA LA TABLA  ----------
cursor.execute("SELECT * FROM productos;") # Muestra las tablas de la base de datos
contenido_tabla = cursor.fetchall() # Lo guardo en la lista
####################### MySQL ###############################

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template(
        "backoffice.html",
        mis_tablas = tablas,
        mis_columnas = columnas,
        mi_contenido_tabla = contenido_tabla
    ) # Envío las tablas a HTML
    
if __name__ == "__main__":
    app.run(debug=True)

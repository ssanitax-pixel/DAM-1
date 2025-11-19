# sudo apt update
# sudo apt install python3-tk

import mysql.connector
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as pt

conexion = mysql.connector.connect(
    host="localhost",
    user="clientes",
    password="Clientes123$",
    database="clientes"
)

cursor = conexion.cursor()
cursor.execute(''' 
    SELECT
    COUNT(color) AS numero,
    color
    FROM productos
    GROUP BY color
    ORDER BY color ASC;
''')

filas = cursor.fetchall()

cantidades =[]
etiquetas = []

for fila in filas:
    cantidades.append(fila[0])
    etiquetas.append(fila[1])
    
print(cantidades)
print(etiquetas)

pt.pie(cantidades, labels=etiquetas)
pt.show()

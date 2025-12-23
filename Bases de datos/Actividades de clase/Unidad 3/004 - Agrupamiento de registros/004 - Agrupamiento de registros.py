'''
    Resolución: Agrupamiento de registros y gráficas
    v1.0 Nosotros & Co.
    Programa que cuenta productos por categoría y genera una gráfica de barras.
'''

import mysql.connector
import matplotlib.pyplot as pt

# 1. Conectamos a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="confirmacion123",
    database="clientes"
)

cursor = conexion.cursor()

# 2. Ejecutamos la consulta de agrupamiento
# Usamos ORDER BY para que la gráfica salga ordenada de más a menos
cursor.execute("SELECT categoria, COUNT(id) FROM productos GROUP BY categoria ORDER BY COUNT(id) DESC")
datos = cursor.fetchall()

# 3. Preparamos las listas para Matplotlib
eje_x = []
eje_y = []

for fila in datos:
    eje_x.append(fila[0])
    eje_y.append(fila[1])

# 4. Creamos la visualización
# Usamos bar para una gráfica de barras
pt.bar(eje_x, eje_y)

# Añadimos información visual básica
pt.title("Total de productos por categoria")
pt.xlabel("Categorias")
pt.ylabel("Cantidad")

# 5. Mostramos el resultado
print("Generando grafica...")
pt.show()

# 6. Cerramos todo
cursor.close()
conexion.close()

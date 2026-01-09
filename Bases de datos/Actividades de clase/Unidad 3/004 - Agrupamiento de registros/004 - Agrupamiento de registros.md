El agrupamiento de registros es una técnica de SQL que nos permite juntar filas que tienen el mismo valor en una columna específica. En lugar de ver cada producto por separado, usamos la cláusula `GROUP BY` para crear grupos, como por ejempli agrupar por "Categoría" o por "Color".
Esto es muy útil cuando queremos sacar estadísticas, como saber cuántos artículos tenemos de cada tipo en un almacén. Al combinarlo con funciones como `COUNT()`, la base de datos nos devuelve el total de cada grupo automáticamente.

---

Vamos a importas las librerías necesarias, primero llamamos a `mysql.connector` para entrar en la base de datos y a `matplotlib.pyplot` para dibujar las gráficas.

```
import mysql.connector
import matplotlib.pyplot as pt
```

Usamos nuestra plantilla habitual para conectar con el servidor local usando el usuario y la contraseña de nuestra base de datos.

```
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="confirmacion123$",
    database="clientes"
)
```

Creamos el cursor y preparamos la consulta. El cursor es el que ejecuta las órdenes en SQL. Vamos a pedirle que cuente los productos agrupándolos por su categoría.

```
cursor = conexion.cursor()

peticion = "SELECT categoria, COUNT(id) FROM productos GROUP BY categoria ORDER BY COUNT(id) DESC"
```

Ahora para ejecutar y recoger los datos, vamos a decirle al cursor que ejecute la frase anterior y guardamos todos los resultados en una variable.

```
cursor.execute(peticion)

filas = cursor.fetchall()
```

Preparamos las listas para la gráfica creando dos listas vacías para separar los nombres de las categorías y las cantidades totales.

```
nombres = []
cantidades = []
```

Recorremos los datos que nos ha dado MySQL y los vamos metiendo en nuestras listas para poder graficarlos.

```
for fila in filas:
    nombres.append(fila[0])
    cantidades.append(fila[1])
```

Usamos los datos de nuestras listas para crear una gráfica de barras. Le ponemos un título y la mostramos por pantalla.

```
pt.bar(nombres, cantidades)
pt.title("Productos por categoria")
pt.show()
```

Como siempre, al terminar cerramos el cursor y la conexión para no dejar procesos abiertos.

```
cursor.close()
conexion.close()
```

---

Así se verá el código:

```
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
```

---

Hacer estos agrupamientos nos ahorra muchísimo trabajo. En lugar de que nuestro programa de Python tenga que leer mil filas y contarlas una a una con un bucle, le pedimos a SQL que nos dé el trabajo ya hecho. Esto hace que nuestras aplicaciones funcionen mucho más rápido, especialmente cuando tenemos muchos datos.
Ver los resultados en una gráfica nos ayuda a entender mejor lo que pasa en nuestro negocio o proyecto. Al final, conectar Bases de Datos con Python y librerías visuales es lo que se hace en las empresas de verdad para crear paneles de control o informes automáticos. Es una forma de trabajar mucho más profesional que solo ver números en blanco y negro por la terminal.

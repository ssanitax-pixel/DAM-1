# Importamos librería
import sqlite3

# Nos conectamos a la base de datos
conexion = sqlite3.connect("empresa.db")

# Creamos un cursor
cursor = conexion.cursor()

# Ejecutamos una sentencia
cursor.execute('''
    INSERT INTO clientes VALUES(
        NULL,'Jorge','García López','jorge@jocarsa.com'
    );
''')

# Lanzamos la petición
conexion.commit()

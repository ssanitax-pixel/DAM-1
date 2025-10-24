# pip3 install mysql-connector-python
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()
cursor.execute('''
    INSERT INTO Clientes
    VALUES(
        NULL,
        "12345678Z",
        "Ana",
        "Sánchez",
        "ana@gmail.com"
    );
''')
conexion.commit()

cursor.close()
conexion.close()

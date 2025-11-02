# pip3 install mysql-connector-python
# sudo apt install libmysqlclient-dev python3-mysql.connector
# solo si da error de ssl en shocket:
# pip3 install --user --upgrade mysql-connector-python --break-system-packages
import mysql.connector
conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()
cursor.execute('''
    INSERT INTO clientes
    VALUES(
    NULL,
    "Ana",
    "Sánchez Suárez",
    "info@ana.es
);
''')
conexion.commit()
cursor.close()
conexion.close()

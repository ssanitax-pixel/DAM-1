import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",      
    user="usuario1",    
    password="Portafolio123#",  
    database="portafolio"      
)

cursor = conexion.cursor()

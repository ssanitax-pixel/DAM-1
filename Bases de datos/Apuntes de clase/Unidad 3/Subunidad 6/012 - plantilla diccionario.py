import mysql.connector 

conexion = mysql.connector.connect(
  host="localhost",
  user="TugaTita",
  password="TugatitaRexulona123$",
  database="composiciones"
)                                      
  
cursor = conexion.cursor(dictionary=True) 
cursor.execute("SELECT * FROM matriculas_join;")  

filas = cursor.fetchall()

print(filas)

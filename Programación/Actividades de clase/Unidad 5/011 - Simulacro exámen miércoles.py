import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",      
    user="usuario1",    
    password="Portafolio123#",  
    database="portafolio"      
)

cursor = conexion.cursor()
while True:
  print("Escoge una opcion:")
  print("1.-Insertar una pieza")
  print("2.-Listar piezas")
  print("3.-Actualizar piezas")
  print("4.-Borrar una pieza")
  print("5.-Salir")
  opcion = int(input("Escoge tu opción: "))

  if opcion == 1:
    print("Insertamos una pieza")
    titulop = input("Introduce el título de la pieza: ")
    descripcionp = input("Introduce la descripción de la pieza: ")
    imagen = input("Introduce el nombre de la imagen de la pieza: ")
    url = input("Introduce la url de la pieza: ")
    id_categoria = input("Introduce el id de la categoría: ")
    cursor.execute('''
      INSERT INTO Pieza
      VALUES (
        NULL,
        "'''+titulop+'''",
        "'''+descripcionp+'''",
        "'''+imagen+'''",
        "'''+url+'''",
        '''+id_categoria+'''
      )
    ''')
    conexion.commit()
  elif opcion == 2:
    print("Listamos las piezas")
    cursor.execute("SELECT * FROM Pieza")
    resultados = cursor.fetchall()
    for fila in resultados:
      print(fila)
  elif opcion == 3:
    print("Actualizamos una pieza")
    Identificador = input("Introduce el Identificador a actualizar: ")
    titulop = input("Introduce el nuevo título de la pieza: ")
    descripcionp = input("Introduce la descripción de la pieza: ")
    imagen = input("Introduce el nombre de la imagen de la pieza: ")
    url = input("Introduce la url de la pieza: ")
    id_categoria = input("Introduce el número de categoría: ")
    cursor.execute('''
        UPDATE Pieza
        SET
            titulop = "'''+titulop+'''",
            descripcionp = "'''+descripcionp+'''",
            imagen = "'''+imagen+'''",
            url = "'''+url+'''",
            id_categoria = '''+id_categoria+'''
        WHERE Identificador = '''+Identificador+'''
    ''')
    conexion.commit()
  elif opcion == 4:
    print("Eliminamos un cliente")
    Identificador = input("Introduce el Identificador de la pieza que quieres eliminar: ")
    cursor.execute('''
      DELETE FROM Pieza
      WHERE Identificador = '''+Identificador+'''
    ''')
    conexion.commit()
  elif opcion == 5:
    break
  
cursor.close() 

conexion.close()

import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",      
    user="usuario2",    
    password="Portafolio123#",  
    database="portafolioexamen"
)

cursor = conexion.cursor()

print("¡Bienvenido al programa que gestiona las piezas!")
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
        titulo = input("Introduce el título de la pieza: ")
        descripcion = input("Introduce la descripción de la pieza: ")
        fecha = input("Introduce la fecha de creación de la pieza: ")
        id_categoria = input("Introduce el ID de la categoría: ")
        cursor.execute('''
          INSERT INTO piezasportafolio
          VALUES (
            NULL,
            "'''+titulo+'''",
            "'''+descripcion+'''",
            "'''+fecha+'''",
            '''+id_categoria+'''
          )
        ''')
        conexion.commit()
        
    elif opcion == 2:
        print("Listamos las piezas")
        cursor.execute("SELECT * FROM piezasportafolio")
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)
    
    elif opcion == 3:
        print("Actualizamos una pieza")
        Identificador = input("Introduce el Identificador a actualizar: ")
        titulo = input("Introduce el nuevo título de la pieza: ")
        descripcion = input("Introduce la descripción de la pieza: ")
        fecha = input("Introduce la fecha de creación de la pieza: ")
        id_categoria = input("Introduce el número de categoría: ")
        cursor.execute('''
            UPDATE piezasportafolio
            SET
                titulo = "'''+titulo+'''",
                descripcion = "'''+descripcion+'''",
                fecha = "'''+fecha+'''",
                id_categoria = '''+id_categoria+'''
            WHERE Identificador = '''+Identificador+'''
        ''')
        conexion.commit()
    
    elif opcion == 4:
        print("Eliminamos un cliente")
        Identificador = input("Introduce el Identificador de la pieza que quieres eliminar: ")
        cursor.execute('''
          DELETE FROM piezasportafolio
          WHERE Identificador = '''+Identificador+'''
        ''')
        conexion.commit()
    
    elif opcion == 5:
        break
        
cursor.close()

conexion.close()

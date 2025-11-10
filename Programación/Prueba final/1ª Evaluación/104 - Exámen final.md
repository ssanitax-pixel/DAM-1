En este ejercicio hemos desarrollado una aplicación que interactúa con una base de datos MySQL para gestionar un portafolio de piezas de arte. Utilizando Python y el módulo `mysql.connector`, se establece una conexión con la base de datos y se proporciona un menú interactivo para que el usuario pueda realizar diversas operaciones como **insertar, listar, actualizar y eliminar** piezas de arte almacenadas en una tabla llamada `piezasportafolio`. Esta tabla almacena información sobre las piezas, como su título, descripción, fecha y la categoría a la que pertenece.

El código incluye operaciones básicas de bases de datos como INSERT, SELECT, UPDATE y DELETE, que permiten gestionar los datos de manera eficiente. Además, el menú interactivo permite al usuario realizar estas operaciones sin necesidad de escribir comandos SQL manualmente, facilitando la interacción con la base de datos.

---

Importamos `mysql.conector` para poder conectar Python con la base de datos llamada `porfolioexamen`.

```
import mysql.connector
```

Establecemos la conexión con MySQL utilizando las credenciales del usuario creado anteriormente.

```
conexion = mysql.connector.connect(
    host="localhost",
    user="usuario2",
    password="Portafolio123#",
    database="portafolioexamen"
)
```

El cursor nos permitirá ejecurar las sentencias SQL y manejar los resultados.

```
cursor = conexion.cursor()
```

Mensaje de bienvenida.

```
print("¡Bienvenido al programa que gestiona las piezas!")
```

Dentro del bucle `while` es donde solicitaremos al usuario que escoja una opción de un menú.

```
while True:
    print("Escoge una opcion:")
    print("1.-Insertar una pieza")
    print("2.-Listar piezas")
    print("3.-Actualizar piezas")
    print("4.-Borrar una pieza")
    print("5.-Salir")
    opcion = int(input("Escoge tu opción: "))
```

Definimos la opción de insertar, pedimos los valores necesarios para la pieza que se va a insertar.

```
    if opcion == 1:
        print("Insertamos una pieza")
        titulo = input("Introduce el título de la pieza: ")
        descripcion = input("Introduce la descripción de la pieza: ")
        fecha = input("Introduce la fecha de creación de la pieza: ")
        id_categoria = input("Introduce el ID de la categoría: ")
```

Luego ejecutamos una consulta SQL para insertar estos valores en la tabla `piezascategorias`.

```
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
```

Finalmente, conexion.commit() asegura que la inserción se guarde en la base de datos.

```
        conexion.commit()
```

Definimos la opción de listar las piezas. `SELECT * FROM piezasportafolio`: realiza una consulta para obtener todas las piezas de la tabla Pieza. `cursor.fetchall()`: Recupera todos los resultados de la consulta y los almacena en la variable resultados. Luego, recorre cada fila de los resultados y las imprime.

```
    elif opcion == 2:
        print("Listamos las piezas")
        cursor.execute("SELECT * FROM piezasportafolio")
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)
```

Ahora definimos la opción 3, actualizar una pieza, el programa pide el Identificador de la pieza que desea modificar, y luego solicita nuevos valores para esa pieza:

```
    elif opcion == 3:
        print("Actualizamos una pieza")
        Identificador = input("Introduce el Identificador a actualizar: ")
        titulo = input("Introduce el nuevo título de la pieza: ")
        descripcion = input("Introduce la descripción de la pieza: ")
        fecha = input("Introduce la fecha de creación de la pieza: ")
        id_categoria = input("Introduce el número de categoría: ")
```

Luego, la pieza especificada por el `Identificador` se actualiza con los nuevos valores usando una consulta SQL.

```
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
```

Para definir la opción número 4, que será borrar una pieza, el programa solicita el `Identificador` de la pieza a eliminar y luego ejecuta una consulta para eliminarla.

```
    elif opcion == 4:
        print("Eliminamos un cliente")
        Identificador = input("Introduce el Identificador de la pieza que quieres eliminar: ")
        cursor.execute('''
          DELETE FROM piezasportafolio
          WHERE Identificador = '''+Identificador+'''
        ''')
        conexion.commit()
```

Por último nos permitimos añadir un extra, que será cerrar el programa, lo haremos con la función break.

```
    elif opcion == 5:
        break
```

Al finalizar, el programa cierra el cursor y la conexión con la base de datos:

```
cursor.close()

conexion.close()
```

---

Así quedará el código completo:

```
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
```

---

Este ejercicio demuestra cómo interactuar con una base de datos MySQL utilizando Python y el módulo `mysql.connector`. A través de las operaciones básicas de manipulación de datos (insertar, listar, actualizar y eliminar), hemos creado un sistema sencillo pero funcional para gestionar un portafolio de piezas de arte.

Es importante destacar la importancia de seguir buenas prácticas de programación, como realizar una adecuada validación de entradas para asegurar que los datos ingresados sean correctos y consistentes. Además, la implementación de un manejo adecuado de errores puede mejorar la robustez del sistema.

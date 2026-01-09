En el entorno empresarial, la gestión eficiente de los clientes es un aspecto esencial para garantizar un control adecuado de la información y ofrecer un servicio de calidad. Utilizar una base de datos MySQL permite almacenar, consultar y modificar datos de manera segura y estructurada.
En esta práctica, desarrollo un programa interactivo en Python que se conecta a una base de datos llamada `empresarial`, con el objetivo de realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre una tabla de clientes. Además, se resalta la importancia de realizar copias de seguridad periódicas y de mantener un sistema estable que asegure la integridad de la información almacenada.

---

Llamamos a la libreía de `mysql.connector`

```
import mysql.connector
```

Conectamos a la base de datos.

```
conexion = mysql.connector.connect(
    host="localhost",
    user="usuarioempresarial",
    password="contraseña123",
    database="empresarial"
)

cursor = conexion.cursor()
```

Bucle principal del programa.

```
while True:
    print("\n-------------------------------")
    print("   GESTIÓN DE CLIENTES")
    print("-------------------------------")
    print("1.- Insertar un cliente")
    print("2.- Listar los clientes")
    print("3.- Actualizar un cliente")
    print("4.- Borrar un cliente")
    opcion = int(input("Escoge tu opción: "))
```

Insertamos cliente.

```
    if opcion == 1:
        print("\n--- Insertamos un cliente ---")
        nombre = input("Introduce el nombre del cliente: ")
        apellidos = input("Introduce los apellidos del cliente: ")
        telefono = input("Introduce el teléfono del cliente: ")
        email = input("Introduce el email del cliente: ")
        localidad = input("Introduce la localidad del cliente: ")

        cursor.execute('''
            INSERT INTO clientes VALUES (
                NULL,
                "''' + nombre + '''",
                "''' + apellidos + '''",
                "''' + telefono + '''",
                "''' + email + '''",
                "''' + localidad + '''"
            )
        ''')
        conexion.commit()
        print("Cliente insertado correctamente.")

```

Listamos clientes.

```
    elif opcion == 2:
        print("\n--- Listamos los clientes ---")
        cursor.execute("SELECT * FROM clientes")
        resultados = cursor.fetchall()
        for fila in resultados:
            print("ID:", fila[0], "| Nombre:", fila[1], "| Apellidos:", fila[2], "| Teléfono:", fila[3], "| Email:", fila[4], "| Localidad:", fila[5])
```

Actualizamos clientes.

```
    elif opcion == 3:
        print("\n--- Actualizamos un cliente ---")
        id = input("Introduce el ID del cliente que quieres actualizar: ")

        print("¿Qué dato quieres modificar?")
        print("1.- Teléfono")
        print("2.- Email")
        print("3.- Localidad")
        campo = int(input("Escoge una opción: "))

        if campo == 1:
            nuevo_valor = input("Introduce el nuevo teléfono: ")
            cursor.execute('''
                UPDATE clientes SET Telefono = "''' + nuevo_valor + '''"
                WHERE Identificador = ''' + id + '''
            ''')
        elif campo == 2:
            nuevo_valor = input("Introduce el nuevo email: ")
            cursor.execute('''
                UPDATE clientes SET Email = "''' + nuevo_valor + '''"
                WHERE Identificador = ''' + id + '''
            ''')
        elif campo == 3:
            nuevo_valor = input("Introduce la nueva localidad: ")
            cursor.execute('''
                UPDATE clientes SET Localidad = "''' + nuevo_valor + '''"
                WHERE Identificador = ''' + id + '''
            ''')
        else:
            print("Opción no válida.")
            continue

        conexion.commit()
        print("Cliente actualizado correctamente.")
```

Borrar cliente.

```
    elif opcion == 4:
        print("\n--- Eliminamos un cliente ---")
        id = input("Introduce el ID del cliente que quieres eliminar: ")

        confirmar = input("¿Seguro que deseas eliminar este cliente? (s/n): ")
        if confirmar.lower() == 's':
            cursor.execute('''
                DELETE FROM clientes WHERE Identificador = ''' + id + '''
            ''')
            conexion.commit()
            print("Cliente eliminado correctamente.")
        else:
            print("Operación cancelada.")
```

Cerramos conexiones.

```
cursor.close()
conexion.close()
```

---

Este programa permite gestionar los clientes de una base de datos de forma sencilla mediante un menú interactivo.
El usuario puede insertar, consultar, actualizar o eliminar clientes, manteniendo la información organizada.
En un contexto empresarial, este tipo de aplicación básica es el primer paso hacia un sistema de gestión de clientes (CRM), que puede ampliarse para incluir copias de seguridad automáticas, registro de pedidos, o control de usuarios.

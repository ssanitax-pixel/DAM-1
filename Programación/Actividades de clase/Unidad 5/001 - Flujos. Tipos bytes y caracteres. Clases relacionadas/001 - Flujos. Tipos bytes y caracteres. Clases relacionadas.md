En esta actividad aplicamos lo aprendido sobre **lectura y escritura de información en archivos** en Python.
A través de un pequeño programa, gestionamos una agenda de contactos que permite añadir nuevos amigos y consultar los existentes, combinando así una situación cotidiana con los conceptos de **flujos de datos**, **modos de apertura** y **manejo de archivos** (`open`, `write`, `readlines`, `close`).

---

Metemos el programa en un bucle infinito, lo que permite que el menú se repita hasta que el usuario quiera salir.

```
while True:
```

Dentro mostramos las opciones que puede usar el usuario.

```
    print("Elige la opción:")
    print("1.- Introducir un nuevo contacto")
    print("2.- Leer todos los contactos")
    print("3.- Salir")
```

Luego, el usuario podrá elegir una opción con `input`.

```
    opcion = int(input("Escoge tu opción: "))
```

Para añadir un nuevo contacto, el programa pedirá los datos de la persona que queremos añadir, después se abrirá el archivo `agenda.txt` o se creará en el caso de que no existiese antes. El modo `a`, significa añadir, eso significa que se escribirá al final de archivo existente, sin borrar lo anterior.

```
    if opcion == 1:
        nombre = input("Introduce el nombre de la persona: ")
        email = input("Introduce el email de la persona: ")
        archivo = open("agenda.txt", "a")
        archivo.write(nombre + ", " + email + "\n")
        archivo.close()
        print("Contacto añadido correctamente.\n")
```

Para leer los contactos, el archivo se abrirá en modo `r`, que significa lectura. Luego se usa `readlines()` para leer todas las líneas del archivo y guardadas en una lista, por último se recorrerá la lista con un bucle `for` y se mostrará cada línea.

```
elif opcion == 2:
        try:
            archivo = open("agenda.txt", "r")
            lineas = archivo.readlines()
            print("\nLista de contactos:\n")
            for linea in lineas:
                print(linea.strip())
            archivo.close()
            print()
        except FileNotFoundError:
            print("No existe el archivo agenda.txt. Agrega un contacto primero.\n")
```

Como extra, hemos añadido la opción de salir del programa, que saldremos del bucle con un `break`.

```
    elif opcion == 3:
        # Salir del programa
        print("Programa finalizado. ¡Hasta pronto!")
        break
```

---

El código completo quedará así:

```
while True:
    print("Elige la opción:")
    print("1.- Introducir un nuevo contacto")
    print("2.- Leer todos los contactos")
    print("3.- Salir")
    opcion = int(input("Escoge tu opción: "))

    if opcion == 1:
        nombre = input("Introduce el nombre de la persona: ")
        email = input("Introduce el email de la persona: ")
        archivo = open("agenda.txt", "a")
        archivo.write(nombre + ", " + email + "\n")
        archivo.close()
        print("Contacto añadido correctamente.\n")

    elif opcion == 2:
        try:
            archivo = open("agenda.txt", "r")
            lineas = archivo.readlines()
            print("\nLista de contactos:\n")
            for linea in lineas:
                print(linea.strip())
            archivo.close()
            print()
        except FileNotFoundError:
            print("No existe el archivo agenda.txt. Agrega un contacto primero.\n")

    elif opcion == 3:
        # Salir del programa
        print("Programa finalizado. ¡Hasta pronto!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.\n")
```

---

En este ejercicio hemos practicado cómo **escribir y leer información en archivos de texto** utilizando las funciones básicas `open`, `write`, `readlines` y `close`.
El programa permite al usuario **guardar nuevos contactos** y **consultar los existentes** de forma sencilla, aplicando los conceptos de **flujos de datos** y **tipos de apertura de archivos**.
Gracias a esta actividad comprendemos cómo la programación puede ayudarnos a **organizar información cotidiana**, como una agenda personal, reforzando las bases del manejo de entrada y salida de datos en Python.

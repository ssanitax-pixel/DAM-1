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


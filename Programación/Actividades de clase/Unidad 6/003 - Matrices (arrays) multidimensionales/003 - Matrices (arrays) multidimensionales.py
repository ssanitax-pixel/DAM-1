import pickle

agenda = []

while True:
    print("\nSelecciona una opción: ")
    print("1.- Insertar un registro")
    print("2.- Leer registros")
    print("3.- Guardar registros")
    print("4.- Salir")
    
    opcion = input("Opción escogida: ")

    if opcion == "1":
        # Insertar contacto
        nombre = input("Dime tu nombre: ")
        apellidos = input("Dime tus apellidos: ")
        email = input("Dime tu email: ")
        telefono = input("Dime tu teléfono: ")
        agenda.append([nombre, apellidos, email, telefono])
        print("Contacto añadido correctamente.")

    elif opcion == "2":
        # Leer contactos desde archivo
        try:
            with open("agenda.bin", "rb") as archivo:
                agenda_leida = pickle.load(archivo)
                print("\nContactos en la agenda:")
                for contacto in agenda_leida:
                    print("Nombre: " + contacto[0] + " " + contacto[1] + ", Email: " + contacto[2] + ", Teléfono: " + contacto[3])
        except FileNotFoundError:
            print("No hay registros guardados aún.")

    elif opcion == "3":
        # Guardar agenda en archivo
        with open("agenda.bin", "wb") as archivo:
            pickle.dump(agenda, archivo)
        print("Agenda guardada correctamente.")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")

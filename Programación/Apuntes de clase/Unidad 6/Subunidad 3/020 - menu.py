import pickle
agenda = []

while True:
    print("Selecciona una opción: ")
    print("1.-Insertar un registro")
    print("2.-Leer registros")
    print("3.-Guardar registros")
    print("4.-Cargar registros")
    opcion = int(input("Opción escogida: "))
    if opcion ==1:
        # insertar
        nombre = input("Dime tu nombre: ")
        apellidos = input("Dime tus dos apellidos: ")
        email = input("Dime tu email: ")
        telefono = input("Dime tu teléfono: ")
        agenda.append([nombre,apellidos,email,telefono])
    elif opcion == 2:
        # imprimir
        print(agenda)
    elif opcion == 3:
        # guardar
        archivo = open("agenda.bin",'wb')
        pickle.dump(agenda,archivo)
        archivo.close()
    elif opcion == 4:
        archivo = open("agenda.bin",'rb')
        agenda = pickle.load(archivo)
        archivo.close()

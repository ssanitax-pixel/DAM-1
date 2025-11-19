import pickle
agenda = []

while True:
    # insertar
    nombre = input("Dime tu nombre: ")
    apellidos = input("Dime tus dos apellidos: ")
    email = input("Dime tu email: ")
    telefono = input("Dime tu teléfono: ")
    agenda.append([nombre,apellidos,email,telefono])
    # imprimir
    print(agenda)
    # guardar
    archivo = open("agenda.bin",'wb')
    pickle.dump(agenda,archivo)
    archivo.close()

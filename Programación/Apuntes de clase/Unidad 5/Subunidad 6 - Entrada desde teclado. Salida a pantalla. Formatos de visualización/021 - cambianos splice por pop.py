class Cliente():
    def __init__(self,nombre,apellidos,email):
     self.nombre = nombre
     self.apellidos = apellidos
     self.email = email

print("### Gestión de clientes v0.1 ###")
print("###### Ana Sánchez Suárez ######")

clientes = []

while True:
    print("Escoge una opción: ")
    print("1.-Insertar cliente")
    print("2.-Listar clientes")
    print("3.-Actualizar cliente")
    print("4.-Eliminar un cliente")
    opcion = int(input("Escoge una opción: "))
    
    if opcion == 1:
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce los apellidos: ")
        email = input("Introduce el email: ")
        clientes.append(Cliente(nombre,apellidos,email))
    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print("Este es el cliente con id: ",identificador)
            print(cliente.nombre,cliente.apellidos,cliente.email)
            identificador += 1
    elif opcion == 3:
        identificador = int(input("Introduce id para identificar: "))
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce los apellidos: ")
        email = input("Introduce el email: ")
        clientes[identificador].nombre = nombre
        clientes[identificador].apellidos = apellidos
        clientes[identificador].email = email
    elif opcion == 4:
        identificador = int(input("Introduce id para identificar: "))
        confirmacion = (input("¿Estás seguro? (S/N): ")).lower()
        if confirmacion == "s":
            clientes.pop(identificador)
        elif confirmacion == "n":
            print("Cancelado")
        else:
            print("Opción no válida")

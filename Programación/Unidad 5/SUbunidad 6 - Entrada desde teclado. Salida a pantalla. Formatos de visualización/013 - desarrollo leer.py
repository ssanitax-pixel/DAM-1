class CLiente():
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
    opcion = int(input("Escoge una opción: ")
    
    if opcion == 1:
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce los apellidos: ")
        email = input("Introduce el email: ")
        clientes.append(Cliente(nombre,apellidos.email))
    elif opcion == 2:
        for cliente in clientes:
            print(cliente)
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass

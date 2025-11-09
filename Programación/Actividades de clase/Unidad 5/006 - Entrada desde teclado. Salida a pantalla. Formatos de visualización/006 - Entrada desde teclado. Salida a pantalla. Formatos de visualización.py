nombre_restaurante = "Bar Bara"

class Cliente():
    def __init__(self,nombre,apellidos,email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
    
print("¡Bienvenido al",nombre_restaurante)

clientes = []

while True:
    print("----Menú de opciones----")
    print("1.-Crear cliente.")
    print("2.-Listar clientes.")
    print("3.-Actualizar cliente.")
    print("4.-Eliminar cliente.")
    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        nombre = input("Dime el nombre del cliente: ")
        apellidos = input("Dime los apellidos del cliente: ")
        email = input("Dime el email del cliente: ")
        clientes.append(Cliente(nombre,apellidos,email))
        
    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print("Id: ",identificador,"|",cliente.nombre,"|",cliente.apellidos,"|",cliente.email)
            identificador += 1
    
    elif opcion == 3:
        identificador = int(input("Dime el identificador del cliente: "))
        nuevo_nombre = input("Dime el nuevo nombre del cliente: ")
        nuevos_apellidos = input("Dime los nuevos apellidos del cliente: ")
        nuevo_email = input("Dime el nuevo email del cliente: ")
        clientes[identificador].nombre = nuevo_nombre
        clientes[identificador].apellidos = nuevos_apellidos
        clientes[identificador].email = nuevo_email
        
    elif opcion == 4:
        identificador = int(input("Dime el identificador del cliente: "))
        confirmacion = input("¿Estás seguro? (s/n): ")
        if confirmacion == "s" or confirmacion == "S":
            clientes.pop(identificador)
        elif confirmacion == "n" or confirmacion == "N":
            print("Eliminación cancelada")
        else:
            print("Opción no válida")

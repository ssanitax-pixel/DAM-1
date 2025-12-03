class Cliente():
    def __init__(self):
        self.email = ""
        self.nombre = ""
        self.direccion = ""

clientes = []

print("Programa de gestión de clientes v1.0 Ana Sánchez Suárez")

while True:
    print("Elige una opción")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar clientes")
    print("4. Eliminar cliente")
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        print("Vamos a crear un cliente")
        nuevocliente = Cliente()
        nuevocliente.email = input("Dime el email del cliente: ")
        nuevocliente.nombre = input("Dime el nombre del cliente: ")
        nuevocliente.direccion = input("Dime la dirección del cliente: ")
        clientes.append(nuevocliente)
    elif opcion == 2 :
        print("Vamos a listar los clientes")
        for cliente in clientes:
            print(cliente.email,cliente.nombre,cliente.direccion)
    elif opcion == 3:
        print("Vamos a actualizar un cliente")
        nombreborrar = input("Introduce el nombre del usuario a actualizar: ")
        nuevoemail = input("Nuevo email: ")
        nuevonombre = input("Nuevo nombre: ")
        nuevadireccion = input("Nueva dirección: ")
        cliente.email = nuevoemail
        cliente.nombre = nuevonombre
        cliente.direccion = nuevadireccion
    elif opcion == 4:
        print("Vamos a borrar un cliente: ")
        nombreborrar = input("Introduce el nombre del usuario a borrar: ")
        nombreborrar = clientes.remove(cliente)
        
        

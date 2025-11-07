class Cliente():
    def __init__(self):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
        
clientes = []

while True:
    nombre = input("Dime el nombre del cliente: ")
    apellidos = input("Dime los apellidos del cliente: ")
    email = input("Dime el email del cliente: ")
    direccion = input("Dime dirección del cliente: ")

    clientes.append(Cliente())

    for cliente in clientes:
        print(cliente.nombre,"/",cliente.apellidos,"/",cliente.email,"/",cliente.direccion)


class Cliente():
    def __init__(self,nombre,apellidos,email,direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
        
nombre = input("Dime el nombre del cliente: ")
apellidos = input("Dime los apellidos del cliente: ")
email = input("Dime el email del cliente: ")
direccion = input("Dime la dirección del cliente: ")

cliente1 = Cliente(nombre,apellidos,email,direccion)


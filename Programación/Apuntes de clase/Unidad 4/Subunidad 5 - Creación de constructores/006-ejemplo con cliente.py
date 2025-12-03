class Cliente():
    def __init__(self,nombre,apellidos,email,direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
        
# Cliente1 = Cliente() # Instancia de objeto la primera en mayúscula
# cliente2 = 56 # Variable numérico

nombre = input("Introduce el nombre del cliente: ")
apellidos = input("Introduce los apellidos del cliente: ")
email = input("Introduce el email del cliente: ")
direccion = input("Introduce la dirección del cliente: ")

cliente1= Cliente(nombre,apellidos,email,direccion)

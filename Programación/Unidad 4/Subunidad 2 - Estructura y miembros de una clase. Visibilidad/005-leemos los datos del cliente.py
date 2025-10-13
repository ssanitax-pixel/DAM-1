# Declaramos una clase
class Cliente():
    def __init__(self):
        self.email = "" # Tambien vale poner None
        self.nombre = ""
        self.direccion = ""
  
# Usamos la clase instanciando en un objeto
cliente1 = Cliente()
cliente1.email = input("Introduce el correo del cliente: ")
cliente1.nombre = input("Introduce el nombre del cliente: ")
cliente1.direccion = input("Introduce la dirección del cliente: ")

print(cliente1)
print(cliente1.email)
print(cliente1.nombre)
print(cliente1.direccion)

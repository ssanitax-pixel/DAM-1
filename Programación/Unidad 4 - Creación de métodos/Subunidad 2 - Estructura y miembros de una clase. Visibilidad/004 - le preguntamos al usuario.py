# Declaramos una clase
class Cliente():
    def __init__(self):
        self.email = "" # También vale poner NONE, pero recomendable "", ya que damos el dato de que es una cadena de texto, con lo otro no
        self.nombre = ""
        self.direccion = ""

# Usamos la clase instanciando en un objeto
cliente1 = Cliente()
cliente1.email = input("Introduce el correo del cliente: ")
cliente1.nombre = input("Introduce el nombre del cliente: ")
cliente1.direccion = input("Introduce la direccion del cliente: ")

print(cliente) # Esto no funciona, se ve en la siguiente

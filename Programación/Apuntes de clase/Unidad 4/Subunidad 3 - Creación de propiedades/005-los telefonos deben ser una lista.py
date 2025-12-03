# Las propiedades son como las variables PERO dentro de una clase

class Cliente():
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.telefonos = ['493965','385032']

# Ahora instancio un nuevo objeto
cliente1 = Cliente()

# Ahora le escribo una propiedad

cliente1.nombre = "Jose Vicente" # No deberíamos de hacer esto de normal

print("El nombre del cliente es: ",cliente1.nombre)

cliente1.telefonos.append("446854346")
cliente1.telefonos.append("866756899")

print(cliente1.telefonos)

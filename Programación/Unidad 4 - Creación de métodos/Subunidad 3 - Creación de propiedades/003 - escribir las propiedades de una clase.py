# Las propiedades son como las variables PERO dentro de una clase

class Cliente():
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.telefonos = ['504958604','347106553']

# Ahora instancio un nuevo objeto
cliente1 = Cliente()

# Ahora le escribo una propiedad
cliente1.nombre = "Ana" # No deberíamosde hacer esto de normal

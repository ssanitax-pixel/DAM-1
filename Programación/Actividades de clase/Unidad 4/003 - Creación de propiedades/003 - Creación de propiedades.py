class Cliente():
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.telefonos = []
        
cliente1 = Cliente()
cliente1.nombre = "Ana"
cliente1.edad = 25
cliente1.telefonos = ["654038456","405639530"]

print("Nombre: ",cliente1.nombre)
print("Edad: ",cliente1.edad)
for telefono in cliente1.telefonos:
    print("Teléfono: ",telefono)

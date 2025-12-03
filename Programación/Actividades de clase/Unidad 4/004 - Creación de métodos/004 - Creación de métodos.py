class Cliente():
    def __init__(self):
        self.nombrecompleto = ""
        self.email = ""
    def setNombreCompleto(self,nuevonombre):
        self.nombrecompleto = nuevonombre
    def setEmail(self,nuevoemail):
        self.email = nuevoemail
    def getNombreCompleto(self):
        return self.nombrecompleto
    def getEmail(self):
        return self.email

cliente1 = Cliente()

cliente1.setNombreCompleto("Ana Sánchez Suárez")
cliente1.setEmail("ana@example.com")

print("Nombre:", cliente1.getNombreCompleto())
print("Email:", cliente1.getEmail())

amigo1 = Cliente()
amigo1.setNombreCompleto("Carlos López")
amigo1.setEmail("carlos.lopez@gmail.com")

amigo2 = Cliente()
amigo2.setNombreCompleto("María García")
amigo2.setEmail("maria.garcia@gmail.com")

amigo3 = Cliente()
amigo3.setNombreCompleto("Luis Fernández")
amigo3.setEmail("luis.fernandez@gmail.com")

print("Lista de invitados a la cena:")
print(amigo1.getNombreCompleto(), "-", amigo1.getEmail())
print(amigo2.getNombreCompleto(), "-", amigo2.getEmail())
print(amigo3.getNombreCompleto(), "-", amigo3.getEmail())

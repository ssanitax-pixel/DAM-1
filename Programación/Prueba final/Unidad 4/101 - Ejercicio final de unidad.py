class Cliente():
    def __init__(self,nombre,apellidos,email,direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
    def setNombre(self,nuevonombre):
        self.nombre = nuevonombre
    def setApellidos(self,nuevoapellidos):
        self.apellidos = nuevoapellidos
    def setEmail(self,nuevoemail):
        self.email = nuevoemail
    def setDireccion(self,nuevodireccion):
        self.direccion = nuevodireccion
    def getNombre(self):
        return self.nombre
    def getApellidos(self):
        return self.apellidos
    def getEmail(self):
        return self.email
    def getDireccion(self):
        return self.direccion
        
cliente1 = Cliente("Ana", "Sánchez Suárez", "ana@gmail.com", "Casa")
cliente2 = Cliente("María", "Sánchez Suárez", "maria@gmail.com", "Apartamento")
cliente3 = Cliente("Fátima", "Quiñones Torres", "fatima@gmail.com", "Chalet")

print("")
print("Email original del cliente1:", cliente1.getEmail())
cliente1.setEmail("anasanchezsuarez@email.com")
print("Email actualizado del cliente1:", cliente1.getEmail())

print("Email original del cliente2:", cliente2.getEmail())
cliente2.setEmail("mariasanchezsuarez@email.com")
print("Email actualizado del cliente2:", cliente2.getEmail())

print("Email original del cliente3:", cliente3.getEmail())
cliente3.setEmail("fatimaquinonestorres@email.com")
print("Email actualizado del cliente3:", cliente3.getEmail())
print("")

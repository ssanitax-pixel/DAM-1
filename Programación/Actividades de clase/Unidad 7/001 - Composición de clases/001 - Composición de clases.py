class Persona():
    def __init__(self, nombre, apellidos, email, direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
    def dameDatos(self):
        return self.nombre+" "+self.apellidos
        
class Profesor(Persona):
    def __init__(self, nombre, apellidos, email, direccion):
        super().__init__(nombre, apellidos, email, direccion)

class Alumno(Persona):
    def __init__(self, nombre, apellidos, email, direccion):
        super().__init__(nombre, apellidos, email, direccion)
        
profesor1 = Profesor("Juan","García","juan@jocarsa.com","Dirección")

alumno1 = Alumno("Jose Vicente","Carratalá","info@jocarsa.com","Dirección")

print(profesor1.dameDatos())
print(alumno1.dameDatos())

class Profesor():
    def __init__(self,nombre,apellidos,email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

class Alumno():
    def __init__(self,nombre,apellidos,email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

alumno1 = Alumno("Ana","Sánchez","ana@ana.com")
print(alumno1)

profesor1 = Profesor("Juan","Garcia","juan@jocarsa.com")
print(profesor1)

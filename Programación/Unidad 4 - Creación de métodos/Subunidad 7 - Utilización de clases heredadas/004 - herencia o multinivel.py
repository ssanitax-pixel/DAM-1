class Entidad():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

class Animal(Entidad):
    def __init__(self):
        super().__init__()
        self.edad = 0
        self.nombre = ""
        self.raza = ""
        
class Gato(Animal):
    def __init__(self):
        super().__init__()
        
class Perro(Animal):
    def __init__(self):
        super().__init__()

class Roca(Entidad):
    def __init__(self):
        super().__init__()

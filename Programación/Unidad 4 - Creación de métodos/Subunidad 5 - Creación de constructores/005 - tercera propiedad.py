class Gato():
    def __init__(self,edad,nombre,raza): # El constructor se ejecuta si o si
        self.edad = edad
        self.nombre = nombre
        self.raza = raza
        
    def maulla(self): # El resto de métodos sólo se ejecutan si los llamas
        return "El gato está maullando"
 
gato1 = Gato(9,"Jagger","Mezcla")
print(gato1.edad, gato1.nombre, gato1.raza)


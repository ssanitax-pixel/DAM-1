class Gato():
    def __init__(self,edad,nombre,raza): # El constructor se ejecuta si o si
        self.edad = edad
        self.nombre = nombre
        self.raza = raza
        
    def maulla(self): # El resto de métodos sólo se ejecuta si lo llamas
        return "El gato está maullando"
        

gato1 = Gato(5,"Jagger","Mainecoon")


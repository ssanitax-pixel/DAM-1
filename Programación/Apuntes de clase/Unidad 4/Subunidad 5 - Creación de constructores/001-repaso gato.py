class Gato():
    def __init__(self): # El constructor se ejecuta si o si
        self.edad = 0
        
    def maulla(self): # El resto de métodos sólo se ejecuta si lo llamas
        return "El gato está maullando"
        

gato1 = Gato()
print(gato1.edad)

print(gato1.maulla())

class Gato():
    def __init__(self,color,edad):
        self.color = color
        self.edad = edad
    def maulla(self):
        print("El gato de color",self.color,"y",self.edad,"años está maullando")
        
jaegger = Gato("Crema",9)
jaegger.maulla()

lana = Gato("Manchas",11)
lana.maulla()

# Declaramos una clase
class Cliente():
    def __init__(self):
        self.email = "" # También vale poner NONE, pero recomendable "", ya que damos el dato de que es una cadena de texto, con lo otro no
        self.nombre = ""
        self.direccion = ""

# Usamos la clase instanciando un objeto
cliente1 = Cliente()
cliente1.email = "ana@empresa.es"
cliente1.nombre = "Ana"
cliente1.direccion = "La calle de Ana"

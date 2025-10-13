# Declaramos una clase
class Cliente():
    def __init__(self):
        self.email = "" # Tambien vale poner None
        self.nombre = ""
        self.direccion = ""
  
# Usamos la clase instanciando en un objeto
cliente1 = Cliente()
cliente1.email = "jose@empresa.com"
cliente1.nombre = "Jose"
cliente1.direccion = "La calle de Jose"

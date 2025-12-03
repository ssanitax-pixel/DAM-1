# Poco escalable: uso de muchas variables

cliente1_email = "info@jocarsa.com"
cliente1_direccion = "La calle de Jose Vicente"
cliente1_nombre = "Jose Vicente"
cliente1_apellidos = "Carratalá Sanchis"

cliente2_email = "info@asasu.com"
cliente2_direccion = "La casa de Ana"
cliente2_nombre = "Ana"
cliente2_apellidos = "Sánchez Suárez"

# Mucho mejor: uso de clases

class Cliente()
    def __init__(self):
        self.email = ""
        self.direccion = ""
        self.nombre = ""
        self.apellidos = ""
        
cliente1 = Cliente()
cliente1_email = "info@jocarsa.com"
cliente1_direccion = "La calle de Jose Vicente"
cliente1_nombre = "Jose Vicente"
cliente1_apellidos = "Carratalá Sanchis"
 
cliente2 = Cliente()
cliente2_email = "info@asasu.com"
cliente2_direccion = "La casa de Ana"
cliente2_nombre = "Ana"
cliente2_apellidos = "Sánchez Suárez"

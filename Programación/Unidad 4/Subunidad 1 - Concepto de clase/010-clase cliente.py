# Poco escalable: uso de muchas variables

cliente1_email = "info@jocarsa.com"
cliente1_direccion = "La calle de Jose Vicente"
cliente1_nombre = "Jose Vicente"
cliente1_apellidos = "Carratala Sanchis"

cliente2_email = "info@cliente2.com"
cliente2_direccion = "La calle de cliente2"
cliente2_nombre = "Juan"
cliente2_apellidos = "García"

# Mucho mejor: uso de clases

class Cliente:
    def __int__(self):
        self.email = ""
        self.direccion ""
        self.nombre = ""
        self.apellidos = ""
        
cliente1 = Cliente()
cliente1_email = "info@jocarsa.com"
cliente1_direccion = "La calle de Jose Vicente"
cliente1_nombre = "Jose Vicente"
cliente1_apellidos = "Carratala Sanchis"

cliente2 = Cliente()
cliente2_email = "info@cliente2.com"
cliente2_direccion = "La calle de cliente2"
cliente2_nombre = "Juan"
cliente2_apellidos = "García"

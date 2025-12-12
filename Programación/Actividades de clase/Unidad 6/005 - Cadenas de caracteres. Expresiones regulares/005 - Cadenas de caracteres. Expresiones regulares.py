nombre_amigo = "Juan Pérez"
partido_nombre = nombre_amigo.split(" ")
print(partido_nombre)

import re
patron_direccion = r'^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+ \d+[A-Za-z]? \d{5}$'
direccion = "Calle Mayor 10 46001"
validacion = re.match(patron_direccion, direccion)
print(validacion)

texto = "Quedamos a las 19h"
nuevo_texto = texto.replace("19h","20h")
print(nuevo_texto)

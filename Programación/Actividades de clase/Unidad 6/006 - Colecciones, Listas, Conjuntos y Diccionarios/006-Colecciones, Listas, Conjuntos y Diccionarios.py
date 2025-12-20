persona = {
	"nombre":"Jose Vicente",
	"apellidos":"Carratalá Sanchis",
	"correo":"info@jocarsa.com",
	"edad":47,
	"teléfonos": [
		{
			"tipo":"fijo",
				"número":96123455
		},
		{
			"tipo":"móvil",
				"número":65456546
		}
	]
}

def bienvenida():
	print("Bienvenido!")
	
bienvenida()

print("Teléfono fijo:", persona["teléfonos"][0]["número"])
print("Teléfono móvil:", persona["teléfonos"][1]["número"])

persona["edad"] = 48
persona["teléfonos"].append({"tipo": "trabajo", "número": 12345678})

print("Lista completa de teléfonos:")
print("-", persona["teléfonos"][0]["tipo"], ":", persona["teléfonos"][0]["número"])
print("-", persona["teléfonos"][1]["tipo"], ":", persona["teléfonos"][1]["número"])
print("-", persona["teléfonos"][2]["tipo"], ":", persona["teléfonos"][2]["número"])

En Python, los diccionarios permiten organizar datos mediante etiquetas `clave-valor`, lo que facilita representar objetos reales de forma lógica. Al combinarlos con listas, creamos estructuras anidadas que permiten agrupar múltiples elementos complejos, como varios teléfonos  bajo una sola etiqueta.

---

Creamos un objeto llamado `persona`, es un diccionario que contendrá datos simples y un dato complejo.

```
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
```

Definimos una función de bienvenida para que se ejecute y aparezca el mensaje en pantalla antes de mostrar los datos.

```
def bienvenida():
	print("Bienvenido!")
	
bienvenida()
```

Entramos en el diccionario `persona`, buscamos la clave `teléfonos`. Como es una lista, cogemos el primer elemento con el índice `[0]`. Como ese elemento es otro diccionario, cogemos el valor de la clave `número`.

```
print("Teléfono fijo:", persona["teléfonos"][0]["número"])
```

Accedemos a la clave `edad` del diccionario y actualizamos su valor de 47 a 48.

```
persona["edad"] = 48
```

Usamos el método .append() para añadir un nuevo elemento (un diccionario de tipo trabajo) al final de la lista de teléfonos.

```
persona["teléfonos"].append({"tipo": "trabajo", "número": 12345678})
```

Imprimimos el tipo y el número del nuevo teléfono que acabamos de añadir, que ahora ocupa la posición `[2]` de la lista.

```
print("-", persona["teléfonos"][2]["tipo"], ":", persona["teléfonos"][2]["número"])
```

---

El código completo quedará así:

```
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
```

---

Este ejercicio demuestra cómo las estructuras de almacenamiento, listas y diccionarios, son esenciales para gestionar datos de forma jerárquica. Hemos practicado la mutabilidad al actualizar valores y la navegación por niveles de datos, habilidades críticas para el manejo de información en cualquier software moderno o bases de datos JSON.

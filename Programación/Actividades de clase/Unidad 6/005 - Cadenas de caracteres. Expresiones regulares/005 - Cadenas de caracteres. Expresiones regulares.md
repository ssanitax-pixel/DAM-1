En este ejercicio trabajamos con cadenas de texto en Python y expresiones regulares para aprender a procesar información de manera eficiente. Primero, usamos el método `split()` para dividir un nombre completo en palabras, lo que nos permite manejar cada parte de la cadena por separado. Luego, aplicamos expresiones regulares con el módulo `re` para validar el formato de una dirección postal, asegurándonos de que cumpla ciertas reglas como tener el nombre de la calle, número y código postal. Finalmente, usamos el método `replace()` para modificar partes de un texto, cambiando valores específicos sin afectar el resto del contenido. Estas técnicas son fundamentales para organizar información de manera automática y confiable.

---

1. Explorando cadenas

Definimos una variable con el nombre de un amigo.

```
nombre_amigo = "Juan Pérez"
```

Dividimos el nombre en palabras usando `split()` y lo guardamos en otra variable.

```
partido_nombre = nombre_amigo.split(" ")
```

Mostramos el resultado.

```
print(partido_nombre)
```

2. Validando direcciones

Importamos el módulo `re` para trabajar con expresiones regulares.

```
import re
```

Realizamos el patrón para validar la dirección, tiene que tener: nombre de la calle, número y código postal.

```
patron_direccion = r'^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+ \d+[A-Za-z]? \d{5}$'
```

Validamos la dirección utilizando `re.match()` y guardamos el resultado en validación.

```
validacion = re.match(patron_direccion, direccion)
```

Mostramos.

```
print(validacion)
```

3. Reemplazando texto

Guardamos una dirección de ejemplo en una variable de cadena.

```
texto = "Quedamos a las 19h"
```

Reemplazamos la hora y guardamos de nuevo el texto.

```
nuevo_texto = texto.replace("19h","20h")
```

Mostramos.

```
print(nuevo_texto)
```

---

El código completo quedará así:

```
nombre_amigo = "Juan Pérez"
partido_nombre = nombre_amigo.split(" ")
print(partido_nombre)
```

```
import re
patron_direccion = r'^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+ \d+[A-Za-z]? \d{5}$'
direccion = "Calle Mayor 10 46001"
validacion = re.match(patron_direccion, direccion)
print(validacion)
```

```
texto = "Quedamos a las 19h"
nuevo_texto = texto.replace("19h","20h")
print(nuevo_texto)
```

---

Hemos creado un programa que realiza tres tareas principales:
- Divide un nombre completo en palabras usando `split()`.
- Valida que una dirección tenga el formato correcto usando expresiones regulares y almacena el resultado en `validacion`.
- Reemplaza un valor dentro de un mensaje con `replace()` para modificar la hora de un encuentro.
Con esto, hemos aprendido a manipular cadenas de texto, comprobar formatos con patrones y actualizar información de manera automática, herramientas útiles para organizar actividades o procesar datos en Python de forma sencilla y práctica.

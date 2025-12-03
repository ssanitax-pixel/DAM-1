Vamos a realizar un programa que clasifique al usuario en una categoría de baloncesto dependiendo de la edad que tenga, entonces le mostraremos que edad tiene y en la categoría que se encuentra, además, si sobrepasa los 40 años se le alargará diciendole que tiene expreriencia.

---

Para empezar deberemos preguntarle la edad al usuario, de la siguiente forma:

```
	edad = int(input("¿Qué edad tienes?: "))
```

Con el valor dado de la edad utilizaremos las estructuras de control "if/elif/else" para poder saber en qué categoría se encuentra, lo que conseguimos así es no ejecutar todo el código para ahorrar rendimiento, esto lo conseguimos de la siguiente forma:

```
	if edad < 8:
		categoria = "pre-mini"
```
```
	elif edad >= 8 and edad < 12:
		categoria = "mini"
```
```
	else:
		categoria = "senior"
```

Después de conseguir en que categoría se encuentra se le muestra al usuario la edad que nos proporcionó y la categoría a la que corresponde según su edad, esto lo haremos mediante un "print" de la siguiente manera:

```
	print("Tu edad es",edad,", entonces estás en la categoría",categoria)
```

Y por último si el usuario sobrepasa la edad de 40 años le aparecerá otro mensaje más diciendo que tiene expreriencia en la cancha, igual que el procedimiento anterior.

---

A continuación se muestra un ejemplo del código del ejercicio resuelto:

´´´
'''
    Baloncesto y categorías
    v1.0 Ana Sánchez Suárez
    En este programa te dice en que categoría de baloncesto estás dependiendo de tu edad
'''
# Preguntamos la edad en números enteros
edad = int(input("¿Qué edad tienes?: "))

# Utilizamos las estructuras de control if/elif/else para saber que categoría corresponde al usuario
if edad < 8:
    categoria = "pre-mini"

elif edad >= 8 and edad < 12:
    categoria = "mini"

elif edad >= 12 and edad < 16:
    categoria = "infantil"

elif edad >= 16 and edad < 18:
    categoria = "cadete"

elif edad >= 18 and edad < 20:
    categoria = "junior"

else:
    categoria = "senior"

# Mostramos por pantalla la edad del usuario y su categoría
print("Tu edad es",edad,", entonces estás en la categoría",categoria)

# Además si el jugador sobrepasa los 40 mostraremos por pantalla lo siguiente:
if edad > 40:
    print("Además eres un veterano con experiencia en la cancha")
```

**Notas**

- Tener en cuenta que la variable de edad debe ser un número entero usando la función "int".
- Cuidado con el sangrado despues de las condiciones "if/elif/else".

---

Como hemos visto, las estructuras de control "if/elif/else" nos ayudan a identificar cosas en base a las condiciones que les damos proporcionando un mejor rendimiento al programa.

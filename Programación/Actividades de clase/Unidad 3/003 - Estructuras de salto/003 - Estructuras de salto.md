Este programa se ha creado con el objetivo de practicar la creación y el uso de funciones en Python, aplicándolo a una situación cotidiana: calcular el coste total de una comida compartida entre amigos.

---

Primero he creado una función llamada 'calculaCostoTotal', que recibe dos parámetros: 'costoComida1' y 'costoComida2'. Dentro de la función, simplemente se suman estos dos valores y se devuelve el resultado.

```
def calculaCostoTotal(costoComida1,costoComida2):
    costoTotal = costoComida1 + costoComida2
    return costoTotal
```

Después, fuera de la función, he definido dos variables con valores que simulan el coste de las comidas.

```
costoComida1 = 23
```

Luego he llamado a la función pasándole esas variables, y por último, he usado 'print()' para mostrar el resultado al usuario.

```
totalComida = calculaCostoTotal(costoComida1,costoComida2)

print("El costo total de la comida entre amigos es de: ",totalComida)
```

Así quedaría el programa completo:

```
'''
	Programa que calcula el costo total de una comida entre amigos sumando dos cantidades.
	Creado por Ana Sánchez Suárez
'''

# Definición de la función
def calculaCostoTotal(costoComida1,costoComida2):
    costoTotal = costoComida1 + costoComida2
    return costoTotal
    
# Variables
costoComida1 = 23
costoComida2 = 12

# Llamada a la función
totalComida = calculaCostoTotal(costoComida1,costoComida2)

# Mostramos el resultado
print("El costo total de la comida entre amigos es de: ",totalComida)
```

---

Este ejercicio me ha ayudado a entender mejor cómo crear funciones en Python, cómo pasarles parámetros y cómo usar el valor que devuelven. Bastante útil para organizar mejor gastos comunes con amigos y evitar confusiones. Además, usar funciones hace que el código sea más limpio y reutilizable.

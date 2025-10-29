Este programa se ha creado para calcular el precio medio de una cena dependiendo del número de asistentes, ayudándome así para cuando quede con amigos, que pueda calcular de forma rápida y sencilla el valor medio de la cena.

---

Para comenzar, vamos a definir la variable, que será el número de amigos que asistamos a esa cena. Y lo siguiente será definir la constante, que será el precio medio por persona.

```
numero_personas = 0
precio_por_persona = 25
```

A continuación, tendremos que ejecutar un 'input', para preguntar los asistentes. Ese 'input' es una cadena de texto, así que tendremos que usar 'int' para convetirlo en un número entero, ya que tendremos que hacer cálculos más adelante.

```
numero_personas = input("¿Cuántas personas van a ir a comer?: ")
numero_personas = int(numero_personas)
```

Crearemos una variable, en el que se indique el precio final de la cena, introduciendo ahí la multiplicación de asistentes por precio.

Y por último, crearemos un 'print' que enseñe el mensaje final en la pantalla, que sería algo así:

```
print("El precio total de la cena, teniendo en cuenta que hay",numero_personas,"asistentes, será de",precio_final,"Euros")
```

A continuación el programa completo:

```
'''
    Programa que calcula el precio de una cena basado en las personas que van.
    Creado por Ana Sánchez Suárez
'''

numero_personas = 0
precio_por_persona = 25

numero_personas = input("¿Cuántas personas van a ir a comer?: ")
numero_personas = int(numero_personas)

precio_final = (numero_personas * precio_por_persona)

print("¡Aviso! El precio por persona es de",precio_por_persona,"Euros")
print("El precio total de la cena, teniendo en cuenta que hay",numero_personas,"asistentes, será de",precio_final,"Euros")
```

---

Este programa me ayuda a calcular fácilmente el precio de una cena cuando salgo con amigos. Así, aplico lo que he aprendido para organizar mejor esos momentos y evitar problemas con el dinero.

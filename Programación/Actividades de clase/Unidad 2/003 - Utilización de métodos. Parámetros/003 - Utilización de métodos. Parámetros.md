En este ejercicio, utilizaremos una situación común, como el coste de una cena con amigos. Para aplicar conceptos de programación, específicamente el uso del módulo 'math' en Python.

El módulo 'math' contiene varias funciones matemáticas útiles. En particular, usaremos la función 'ceil' para redondear un número hacia el siguiente entero más cercano hacia arriba.

El objetivo del ejercicio es simular el costo de una cena con amigos y redondearlo utilizando la función ceil para asegurar que no se quede con decimales.

Primero importamos el módulo math para acceder a las funciones matemáticas.

```
import math
```

Definimos el coste de la cena, con una variable.

```
numero_comida = 7.2
```

Por último usaremos la función 'ceil' del módulo 'math' para redondear el número hacia arriba, el pondremos también un print para mostrar el resultado.

```
print(math.ceil(numero_comida))
```

Aquí está el código completo:

```
import math

numero_comida = 7.2

print(math.ceil(numero_comida))
```

Este ejercicio demuestra cómo usar funciones predefinidas en Python, como ceil, para resolver problemas prácticos, como redondear números. En este caso, el redondeo hacia arriba es útil en situaciones como dividir costos de manera justa.

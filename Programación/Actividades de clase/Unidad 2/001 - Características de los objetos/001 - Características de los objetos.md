Quedar con amigos para comer o cenar es divertido. Sin embargo, cuando salimos varias veces, los gastos pueden acumularse rápidamente. En este ejercicio, vamos a simular una serie de salidas a comer con amigos y calcular cuánto hemos gastado en total, aplicando un descuento del 10% por ser un plan grupal. Usaremos herramientas básicas del lenguaje de programación Python, como listas, funciones predefinidas '(sum())' y el módulo 'math'.

Importamos 'math':

```
import math
```

Realizamos una lista con todos los precios de la comida de cada amigo, y seguidamente los sumamos para saber cuál es el total:

```
costos_comidas = [15,44,32,12,4,34]
costo_total = sum(costos_comidas)
```

Aplicamos un descuento del 10% al costo total de la comida:

```
descuento = costo_total * 0.10
costo_final = costo_total - descuento
```

Y por último mostraremos el resultado final con un 'print'

A continuación, dejo el programa completo:

```
'''
    Programa para calcular el total de una cena de amigos con su descuento
    v1.0 Ana Sánchez Suárez
'''

import math

costos_comidas = [15,44,32,12,4,34]

costo_total = sum(costos_comidas)

descuento = costo_total * 0.10
costo_final = costo_total - descuento

print("El costo total de las comidas con amigos es: ",costo_final,"Euros")
```

Este ejercicio nos ha permitido ver cómo se utilizan funciones y objetos predefinidos en Python, como la lista y la función sum(), para realizar cálculos de forma sencilla. También hemos visto cómo importar módulos como math.

Relacionar la programación con actividades cotidianas, como salir a comer con amigos ayuda a entender cómo aplicar la lógica computacional en problemas reales, que es uno de los objetivos principales de esta unidad sobre objetos y métodos predeterminados.

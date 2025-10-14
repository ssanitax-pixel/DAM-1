En este ejercicio, instancio objetos utilizando clases predeterminadas disponibles en Python. Imagina que estás organizando una fiesta con tus amigos y necesitas organizar diferentes aspectos del evento, como la comida y el entretenimiento.

---

Vamos a explicar el código paso a paso:
Importamos el módulo 'math' para usar funciones y constantes matemáticas predeterminadas

```
import math
```

Instanciamos un objeto que calcula la raíz cuadrada de 16 usando 'math.sqrt'.

```
raiz_cuadrada = math.sqrt(16)
```

Instanciamos un objeto que almacena el valor de pi usando 'math.pi'.
```
numero_pi = math.pi
```

Creamos una función para calcular el área de un círculo usando el valor de pi instanciando .

```
def calcular_area_circulo(radio):
    area = numero_pi * radio ** 2
    return area
```

Calculamos el área de un círculo con radio 5.

```
area = calcular_area_circulo(5)
```

Por último, imprimimos el resultado:

```
print("El área del círculo con radio 5 es: ",area)
```

---

Este ejercicio demuestra cómo usar objetos predeterminados del módulo 'math' para facilitar cálculos importantes en la organización de eventos. La instanciación de objetos simplifica el uso de funciones y propiedades, haciendo la programación más eficiente y práctica.

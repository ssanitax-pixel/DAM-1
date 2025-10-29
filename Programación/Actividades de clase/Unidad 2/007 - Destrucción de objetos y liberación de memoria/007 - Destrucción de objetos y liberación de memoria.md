Este programa calcula cuántas cuadras son necesarias para albergar una cantidad específica de caballos, dado el número de caballos y la capacidad de cada cuadra. Utilizando operaciones matemáticas básicas y la función 'math.ceil', el programa redondea hacia arriba el resultado para asegurar que todos los caballos tengan una cuadra. Este tipo de cálculos es útil en la gestión de espacios en instalaciones para caballos.

---

Importamos la libraría math.

```
import math
```

Creamos las entradas de datos, tanto de los caballos como de cuántos caben en una cuadra.

```
numero_caballos = int(input("¿Cuántos caballos hay?: "))
```

Hacemos un pequeño cálculo matemático y al ser una división usaremos 'math.ceil' para redondear hacia arriba, ya que no tendría sentido que las cuadras que necesitamos salgan con decimales.

```
cuadras_necesarias = math.ceil(numero_caballos/caballos_por_cuadra)
```

Finalmente, realizaremos una salida con los datos finales.

```
print("Al tener",numero_caballos,"caballos y caber",caballos_por_cuadra,"por cuadra, necesitaremos",cuadras_necesarias,"cuadras en total")
```

El programa completo quedaría así:

```
'''
    Programa que calcula cuantas cuadras según los caballos que haya.
    v1.0 Ana Sánchez Suárez
'''

import math

numero_caballos = int(input("¿Cuántos caballos hay?: "))

caballos_por_cuadra = int(input("¿Cuántos caballos caben en cada cuadra?: "))

cuadras_necesarias = math.ceil(numero_caballos/caballos_por_cuadra)

print("Al tener",numero_caballos,"caballos y caber",caballos_por_cuadra,"por cuadra, necesitaremos",cuadras_necesarias,"cuadras en total")
```

---

En resumen, el programa calcula cuántas cuadras son necesarias para alojar los caballos, utilizando 'math.ceil' para redondear el resultado y asegurar suficiente espacio. Este ejercicio muestra cómo aplicar funciones matemáticas en Python para resolver problemas prácticos de distribución de recursos.

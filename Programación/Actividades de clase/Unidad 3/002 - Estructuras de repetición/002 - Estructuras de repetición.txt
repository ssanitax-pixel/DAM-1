Para contar los días de un mes, usar un bucle 'for' en Python es muy útil porque nos permite repetir una acción varias veces sin escribir mucho código.

---

Primero, definimos la variable 'dias_mes' con el número de días que tiene el mes actual. Luego, usamos un bucle 'for' para ver desde 1 hasta 'dias_mes', importante poner un día más de lo que queremos ya que ese no se reflejará, e imprimimos un mensaje que indica el día actual.

El ejercicio se vería así:

```
dias_mes = 0 

for dia_mes in range(1,32):
    print("Hoy es el día",dias_mes,"del mes")
```

Probemos con diferentes valores de 'dias_mes' para meses variados:

Para abril:
```
dias_mes = 0 

for dia_mes in range(1,31):
    print("Hoy es el día",dias_mes,"del mes")
```

Para febrero:
```
dias_mes = 0 

for dia_mes in range(1,29):
    print("Hoy es el día",dias_mes,"del mes")
```

---

Este ejercicio muestra cómo los bucles 'for' nos ayudan a repetir tareas fáciles, como contar días, de forma rápida y sin errores. Esto es básico para controlar el flujo en programas más grandes.

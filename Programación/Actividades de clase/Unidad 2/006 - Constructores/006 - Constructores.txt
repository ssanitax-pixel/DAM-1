En este ejercicio, usaremos el módulo 'datetime' en Python, especialmente el objeto 'date', que es una herramienta predeterminada para trabajar con fechas. Los constructores en Python permiten crear instancias de clases predeterminadas, como 'date', que proporcionan funcionalidades específicas para trabajar con fechas y tiempos. En este caso, nos centraremos en cómo obtener la fecha actual y realizar cálculos relacionados con fechas, como obtener el día de la semana y calcular la edad a partir de una fecha de nacimiento.

---

Importamos librría 'datetime'.

```
import datetime
```

Para obtener la fecha actual haremos lo siguiente, una variable, usando 'today' y un 'print'.

```
fecha_hoy = datetime.date.today()
print("Fecha actual: ",fecha_hoy)
```

Hacemos una lista con los dias de la semana, para lo siguiente imprimir el día de la semana correspondiente usando 'weekday'.

```
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print("Día de la semana:", dias[fecha_hoy.weekday()])
```

Introducimos en este caso mi fecha de nacimiento.

```
fecha_personal = datetime.date(2000, 5, 6)
```

Y para calcular la edad, restamos la fecha actual menos mi fecha de nacimiento, usando 'year' para que no salgan los días sino los años.

```
edad = fecha_hoy.year - fecha_personal.year
```

Aquí está el código completo:

```
import datetime

fecha_hoy = datetime.date.today()
print("Fecha actual: ",fecha_hoy)

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print("Día de la semana:", dias[fecha_hoy.weekday()])

fecha_personal = datetime.date(2000, 5, 6)

edad = fecha_hoy.year - fecha_personal.year

print("Mi edad actual es: ",edad)
```

---

En conclusión, he utilizado el objeto 'date' del módulo 'datetime' para trabajar con fechas en Python. Este objeto permite obtener la fecha actual, calcular el día de la semana y realizar operaciones como calcular la edad. Utilizar objetos predeterminados facilita la manipulación de fechas sin necesidad de crear clases personalizadas, lo que mejora la eficiencia en nuestros programas.

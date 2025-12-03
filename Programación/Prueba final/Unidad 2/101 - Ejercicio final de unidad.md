El "Planificador de Cuadras" calcula cuántas cuadras son necesarias para alojar una cantidad de caballos, según la capacidad de cada cuadra. Utiliza cálculos matemáticos con math.ceil() para redondear el número de cuadras hacia arriba y manejo de fechas con la biblioteca datetime para extraer información sobre el día de la semana. Esto permite organizar el espacio y programar actividades según si es un día de semana o fin de semana.

---

Primero importamos las bibliotecas que vamos a necesitar ya que usaremos cálculos matemáticos y de fechas.

```
import datetime
import math
```

Solicitamos datos en entrada y manejamos errores.

```
try:
    caballos = int(input("¿Cuántos caballos hay?: "))
    capacidad_por_cuadra = int(input("¿Cuántos caballos caben en la cuadra?: "))
except: 
    caballos < 0 or capacidad_por_cuadra <0
    print("ERROR: No se puede ejecutar si un valor es negativo")
    exit()
```

Calcular las cuadras necesarias, usamos math.ceil para redondear hacia arriba.

```
cuadras_necesarias = math.ceil(caballos/capacidad_por_cuadra)
```

Obtenemos las propiedades de la fecha.

```
anio = fecha.year
```

Listamos los días de la semana, para usarlos más adelante.

```
weekday = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
```

Obtenemos el nombre del día de la semana basado en el valor de weekday (de 0 a 6)

```
dia_semana = weekday[fecha.weekday()]
```

Por último enseñaremos todo lo recogido en un informe.

```
print("---------DATOS DE LA FECHA---------")
```

---

Aquí está el programa completo:

```
'''
    PLANIFICADOR DE CUADRAS
    
    Programa que calcula cuantas cuadras necesitas en una fecha dada, según el número de caballos y la capacidad de cada cuadra. Redondea al alza el número de cuadras, muestra propiedades de la fecha y presenta un pequeño informe.
'''

import datetime
import math

try:
    caballos = int(input("¿Cuántos caballos hay?: "))
    capacidad_por_cuadra = int(input("¿Cuántos caballos caben en la cuadra?: "))
except: 
    caballos < 0 or capacidad_por_cuadra <0
    print("ERROR: No se puede ejecutar si un valor es negativo")
    exit()
    
try:
    anio = int(input("Introduce el año (YYYY): "))
    mes = int(input("Introduce el mes (MM): "))
    dia = int(input("Introduce el día (DD): "))
    fecha = datetime.date(anio,mes,dia)
except:
    print("ERROR: No se puede ejecutar si un valor es negativo")
    exit()

cuadras_necesarias = math.ceil(caballos/capacidad_por_cuadra)

anio = fecha.year
mes = fecha.month
dia = fecha.day
weekday = fecha.weekday()
isoweekday = fecha.isoweekday()

weekday = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
dia_semana = weekday[fecha.weekday()]

print("")
print("------Planificador de cuadras------")
print("")
print("Al tener",caballos,"caballos y caber",capacidad_por_cuadra,"por cuadra, en total necesitaremos",cuadras_necesarias,"cuadras para que entren todos los caballos correctamente")
print("")
print("---------DATOS DE LA FECHA---------")
print("Fecha en formato YYYY-MM-DD :",fecha)
print("Año: ",anio)
print("Mes: ",mes)
print("Día: ",dia)
print("Día de la semana: ",dia_semana)

if isoweekday > 4:
    print("¡Es fin de semana!")
else:
    print("Es entre semana...")
```

---

El programa realiza cálculos matemáticos y maneja fechas de manera sencilla y eficiente. Permite determinar cuántas cuadras se requieren para una cantidad de caballos y verificar si la fecha proporcionada cae en fin de semana o entre semana. Es una herramienta práctica para gestionar espacios y organizar actividades de manera rápida y precisa.

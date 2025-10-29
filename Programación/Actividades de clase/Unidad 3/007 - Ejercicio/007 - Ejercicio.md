Organizar una cena implica varios pasos: decidir el menú, comprar los ingredientes, preparar los platos y servirlos. En este ejercicio, utilizamos bucles 'for' para repetir tareas como listar ingredientes, mostrar tiempos de preparación y contar los platos servidos. Los bucles 'for' nos permite ver listas de forma eficiente sin escribir código repetido. Además, las condicionales 'if/elif' personalizan la acción para cada plato, y las listas organizan los elementos del menú. Este ejercicio demuestra cómo aplicar estos conceptos de programación en situaciones cotidianas, como planificar una comida para amigos o familiares.

---

Declaramos una lista.

```
menu = ["Pizza","Tortilla de patatas","Fuet","Cerveza"]
```

Creamos un bucle que recorra la lista de comidas.

```
for comida in menu:
    if comida == "Pizza":
        print("Para la Pizza necesitas: masa, tomate, queso y jamón york.")
    elif comida == "Tortilla de patatas":
        print("Para la Tortilla de patatas necesitas: patatas, huevo, aceite y cebolla.")
```

Creamos otro bucle para imprimir el tiempo de preparación en cada plato.

```
for comida in menu:
    if comida == "Pizza":
        print("Para preparar la Pizza necesitas 30 minutos.")
    elif comida == "Tortilla de patatas":
        print("Para preparar la Tortilla de patatas necesitas 45 minutos.")
```

Declaramos una variable para el contador de platos servidos.

```
platos_servidos = 0
```

Por último, otro bucle para servir los platos y aumentar el contador

```
for comida in menu:
    platos_servidos += 1
    print("Se ha servido el plato de",comida,". Platos servidos hasta ahora: ",platos_servidos)
```

A continuación el código completo:

```
menu = ["Pizza","Tortilla de patatas","Fuet","Cerveza"]

for comida in menu:
    if comida == "Pizza":
        print("Para la Pizza necesitas: masa, tomate, queso y jamón york.")
    elif comida == "Tortilla de patatas":
        print("Para la Tortilla de patatas necesitas: patatas, huevo, aceite y cebolla.")
    elif comida == "Fuet":
        print("Para el Fuet necesitas: fuet y un cuchillo para cortarlo.")
    elif comida == "Cerveza":
        print("Para la Cerveza necesitas: cerveza Alhambra muy fría y un vaso congelado.")
    
for comida in menu:
    if comida == "Pizza":
        print("Para preparar la Pizza necesitas 30 minutos.")
    elif comida == "Tortilla de patatas":
        print("Para preparar la Tortilla de patatas necesitas 45 minutos.")
    elif comida == "Fuet":
        print("Para preparar el Fuet necesitas 5 minutos.")
    elif comida == "Cerveza":
        print("Para preparar la Cerveza necesitas 60 minutos.")

platos_servidos = 0

for comida in menu:
    platos_servidos += 1
    print("Se ha servido el plato de",comida,". Platos servidos hasta ahora: ",platos_servidos)
```

---

Este ejercicio muestra cómo los conceptos de programación, como los bucles 'for' y las condicionales, pueden aplicarse para organizar tareas cotidianas, como preparar y servir una cena. Utilizando estos conceptos, podemos gestionar procesos de manera más eficiente y automatizada.

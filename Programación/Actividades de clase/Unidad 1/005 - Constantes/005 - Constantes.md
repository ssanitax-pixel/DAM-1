Vamos a realizar un pequeño programa que realice cálculos, concretamente servirá para que utilicemos las especias correctas a la hora de hacer 10 platos para cenar con mis amigos en casa.

---

Primero será necesario declarar la constante, que en este caso serán las especias, ya que este número no va a cambiar en todo el proceso, concretamente serán 5 especias. Recalcar que las constantes se escriben siempre en mayúsculas.

```
ESPECIAS = 5
```

A continuación, realizamos el cálculo de las especias necesarias para 10 platos.

```
especias_totales = ESPECIAS * 10
```

Finalmente imprimiremos el mensaje en pantalla, indicando las especias finales necesarias.

```
print("Especias necesarias para 10 platos:",especias_totales)
```

Por último, aquí está el programa completo:

```
'''
    Programa para asegurar las especias necesarias para que el plato de mis amigos esté rico
    Creado por Ana Sánchez Suárez
'''

ESPECIAS = 5

especias_totales = ESPECIAS * 10

print("Especias necesarias para 10 platos:",especias_totales)
```
---

El uso de constantes, como 'ESPECIAS = 5', facilita la modificación y el mantenimiento del código porque permite cambiar un valor en un solo lugar, en lugar de buscarlo y reemplazarlo en todo el programa.

Por ejemplo, si en el futuro la receta cambia y se necesitan 6 especias en lugar de 5, solo sería necesario cambiar el valor de la constante 'ESPECIAS = 6', y automáticamente todos los cálculos que la usen se actualizarán.

En esta actividad, utilizamos la teoría de conjuntos para resolver la lógica del Sudoku. Los conjuntos `sets` son fundamentales porque garantizan la unicidad de los datos. Nuestra estrategia se basa en las operaciones agregadas de filtrado: para cada celda, realizamos una resta de conjuntos (Patrón `{1..9}` - Números usados), asegurando que cada fila, columna y cuadrante cumpla las reglas de validación sin duplicados.

---

Importamos la librería random para poder generar números aleatorios y seleccionar candidatos al azar.

```
import random
```

Definimos el conjunto `patron`. Los conjuntos son ideales porque nos aseguran que los números del 1 al 9 no se repitan.

```
patron = {1, 2, 3, 4, 5, 6, 7, 8, 9}
```

Creamos la función `generar_sudoku`. Dentro, inicializamos una matriz 9x9 llena de ceros que iremos rellenando.

```
def generar_sudoku():
    matriz = [[0 for _ in range(9)] for _ in range(9)]
```

Recorremos cada celda de la matriz con dos bucles `for`. Para cada posición, calculamos qué números ya están presentes en su fila, en su columna y en su cuadrante de 3x3 usando conjuntos.

```
    for f in range(9):
        for c in range(9):
            
            en_fila = set(matriz[f])
            en_columna = {matriz[i][c] for i in range(9)}
            
            f_inicio, c_inicio = (f // 3) * 3, (c // 3) * 3
            en_cuadrante = {
                matriz[i][j] 
                for i in range(f_inicio, f_inicio + 3) 
                for j in range(c_inicio, c_inicio + 3)
            }
```

Calculamos los números disponibles mediante la resta de conjuntos: al patrón original le quitamos lo que ya existe en la fila, columna y cuadrante. Si hay opciones, elegimos una al azar, si no, reiniciamos la función para evitar bloqueos.

```
            disponibles = list(patron - en_fila - en_columna - en_cuadrante)
            
            if disponibles:
                matriz[f][c] = random.choice(disponibles)
            else:
                return generar_sudoku()
    return matriz
```

Llamamos a nuestra función para generar el Sudoku completo y lo guardamos en la variable `sudoku`.

```
sudoku = generar_sudoku()
```

Creamos un bucle que se encarga de eliminar 5 números al azar de nuestra matriz, poniendo su valor a 0.

```
for _ in range(5):
    sudoku[random.randint(0,8)][random.randint(0,8)] = 0
```

Finalmente, recorremos la matriz resultante para imprimirla fila por fila en la consola.

```
for fila in sudoku:
    print(fila)
```

---

El código completo queda así:

```
import random

patron = {1, 2, 3, 4, 5, 6, 7, 8, 9}

def generar_sudoku():
    matriz = [[0 for _ in range(9)] for _ in range(9)]
    
    for f in range(9):
        for c in range(9):
            
            en_fila = set(matriz[f])
            en_columna = {matriz[i][c] for i in range(9)}
            
            f_inicio, c_inicio = (f // 3) * 3, (c // 3) * 3
            en_cuadrante = {
                matriz[i][j] 
                for i in range(f_inicio, f_inicio + 3) 
                for j in range(c_inicio, c_inicio + 3)
            }
          
            disponibles = list(patron - en_fila - en_columna - en_cuadrante)
            
            if disponibles:
                matriz[f][c] = random.choice(disponibles)
            else:
                return generar_sudoku()
    return matriz

sudoku = generar_sudoku()

for _ in range(5):
    sudoku[random.randint(0,8)][random.randint(0,8)] = 0

for fila in sudoku:
    print(fila)
```

---

Hemos realizado con éxito la generación de una matriz bidimensional y su posterior reducción al eliminar 5 elementos aleatorios. Este ejercicio nos ha permitido entender cómo el filtrado dinámico mediante conjuntos simplifica la gestión de restricciones complejas. Esta lógica es esencial en situaciones reales de organización, como la asignación de recursos o turnos, donde debemos evitar conflictos de forma eficiente y automatizada.

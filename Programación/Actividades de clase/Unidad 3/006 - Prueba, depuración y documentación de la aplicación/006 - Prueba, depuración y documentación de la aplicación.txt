He desarrollado una función que calcule la raíz cuadrada de un número de manera segura, validando que la entrada sea correcta y manejando posibles errores. Es útil cuando se trabaja con datos de entrada que pueden ser erróneos, como valores negativos o cadenas de texto que no representan números. Para ello, se implementa la validación de entradas utilizando 'try/except' y 'assert', garantizando que la raíz cuadrada solo se calcule si la entrada es válida. El código hace uso del módulo 'math' para calcular la raíz cuadrada y asegura que cualquier entrada no válida sea manejada correctamente.

---

Importamos 'math'.

```
import math
```

Empezamos a implementar la función.

```
def raizSegura(numero):
```

Ahora implementamos la validación y manejo de errores.
Primero, intentamos convertir la cadena a número.

```
try: 
        if isinstance(numero, str):
            numero = float(numero)
```

Validamos que el número sea igual o superior a 0.

```
assert numero >= 0
```

Aseguramos que sea un número válido.

```
assert isinstance(numero, (int, float))
```

Calculamos la raíz cuadrada en caso de que sea válido.

```
return matematicas.sqrt(numero)
```

Finalmente, si ocurre un error hacemos que devuelva 0.

```
except:
        return 0
```

El programa completo quedará de la siguiente forma:

```
'''
    Calcula la raíz cuadrada de un número de manera segura.
    
    Si el número es negativo, devuelve 0.
    Si el número es una cadena, intenta convertirlo a un valor numérico.
    Si la conversión falla, devuelve 0.
    
    v1.0 Ana Sánchez Suárez
'''

import math as matematicas

def raizSegura(numero):

    try: 
        if isinstance(numero, str):
            numero = float(numero)
        assert numero >= 0
        assert isinstance(numero, (int, float))
        return matematicas.sqrt(numero)
            
    except:
        return 0
    
print(raizSegura(4))
print(raizSegura(0))
print(raizSegura("9"))
print(raizSegura("-1"))
print(raizSegura("hola"))
```

---

En resumen, la función raizSegura permite calcular la raíz cuadrada de un número de manera segura, validando que la entrada sea correcta. Si el número es negativo, no es un número válido o no se puede convertir correctamente, la función retorna 0.

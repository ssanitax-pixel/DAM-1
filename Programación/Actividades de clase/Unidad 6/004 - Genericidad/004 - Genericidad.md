En este ejercicio usamos listas, que son estructuras de almacenamiento para guardar varios elementos, y vimos cómo pueden contener distintos tipos de datos como `int` y `str`. La idea es recorrer la lista de participantes, identificar el tipo de cada elemento y calcular el doble de su edad. Esto nos ayuda a practicar conceptos como estructuras de control, bucles y manejo de errores, que son fundamentales en Python para procesar información variada de forma segura.

---

Creamos la lista de participantes, donde algunos son números y otros son palabras, que en este caso también representan números.

```
lista_participantes = [25, "cinco", 30, "cuatro", "siete"]
```

Ahora creamos a parte una lista de etiquetas para convertir palabras en números.

```
numeros_etiquetas = ["cero","uno","dos","tres","cuatro","cinco","seis","siete"]
```

Definimos una función con `def` para recorrer la lista.

```
def calculaDoble():
```

Recorremos cada elemento.

```
    for participante in lista_participantes:
```

Si es un número directamente podremos multiplicarlo por 2.

```
        if isinstance(participante, int):
            print(participante * 2)
```

Pero si es una cadena, tendremos que verificar si está en la lista de etiquetas.

```
        else:
            if participante in numeros_etiquetas:
```

Ahora obtendremos su posición y ya podremos multiplicarlo por 2.

```
                indice = numeros_etiquetas.index(participante)
                print(indice * 2)
```

Por si acaso, si un número no coincide con ninguna etiqueta, pondremos un `else`, para salvar el problema.

```
            else:
                print("No es posible hacer eso")
```

Por último llamamos a la función para procesar la lista.

```
calculaDoble()
```

---

El código completo quedará así:

```
lista_participantes = [25, "cinco", 30, "cuatro", "siete"]

numeros_etiquetas = ["cero","uno","dos","tres","cuatro","cinco","seis","siete"]

def calculaDoble():
    for participante in lista_participantes:
        if isinstance(participante, int):
            print(participante * 2)
        else:
            if participante in numeros_etiquetas:
                indice = numeros_etiquetas.index(participante)
                print(indice * 2)
            else:
                print("No es posible hacer eso")

calculaDoble()
```

---

El programa recorre la lista y multiplica por dos los números. Si el elemento es una palabra, buscamos su posición en otra lista y multiplicamos esa posición por dos. Si no coincide con ninguna etiqueta, mostramos un mensaje. Con esto aprendimos a manejar listas con datos mezclados y a aplicar de forma práctica los conceptos de tipos de datos, bucles y condicionales en Python.

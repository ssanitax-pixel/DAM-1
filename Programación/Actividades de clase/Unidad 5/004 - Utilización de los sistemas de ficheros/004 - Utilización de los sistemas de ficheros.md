En este ejercicio hemos trabajado con sistemas de ficheros usando Python. El objetivo era crear un programa que permita explorar una carpeta y mostrar información sobre cada uno de sus elementos, incluyendo su ruta y tamaño en megabytes. Para ello utilizamos la librería `os`, que nos permitió acceder a los archivos y carpetas, formar rutas completas y obtener el tamaño de los archivos. Este ejercicio nos ayuda a comprender cómo podemos interactuar con el sistema de ficheros de manera práctica y cómo organizar y mostrar información que se encuentra en nuestro ordenador.

---

Primero importamos la librería `os`.

```
import os
```

Pedimos al usuario que escriba la ruta de la carpeta que quiere explorar.

```
carpeta = input("Introduce el nombre de la carpeta: ")
```

Usamos `os.listdir()` para obtener una lista de todos los elementos dentro de esa carpeta. Esto incluye archivos y subcarpetas.

```
elementos = os.listdir(carpeta)
```

Luego recorremos cada elemento de la lista con un bucle `for`.

```
for elemento in elementos:
```

Para cada elemento, usamos `os.path.join()` para crear su ruta completa. Esto es importante porque `os.listdir()` solo nos da el nombre, no la ruta completa.

```
    ruta_completa = os.path.join(carpeta, elemento)
```

Comprobamos si el elemento es un archivo usando `os.path.isfile()`. Si es un archivo, obtenemos su tamaño en bytes con `os.path.getsize()` y lo convertimos en megabytes.

```
    if os.path.isfile(ruta_completa):
        tamanio_bytes = os.path.getsize(ruta_completa)
        tamanio_mb = tamanio_bytes / (1024 * 1024)
```

Si no es un archivo, por ejemplo si es una carpeta, asignamos el tamaño 0 MB.

```
    else:
        tamanio_mb = 0
```

Finalmente, mostramos en pantalla la ruta completa y el tamaño en MB.

```
    print("Ruta: ",ruta_completa," | Tamaño: ",tamanio_mb,"MB")
```

---

El código completo se verá así:

```
import os

carpeta = input("Introduce el nombre de la carpeta: ")

elementos = os.listdir(carpeta)

for elemento in elementos:
    ruta_completa = os.path.join(carpeta, elemento)
    
    if os.path.isfile(ruta_completa):
        tamanio_bytes = os.path.getsize(ruta_completa)
        tamanio_mb = tamanio_bytes / (1024 * 1024)
    else:
        tamanio_mb = 0
    
    print("Ruta: ",ruta_completa," | Tamaño: ",tamanio_mb,"MB")
```

En pantalla saldrá algo así:

```
Introduce el nombre de la carpeta: /home/vboxuser/Documentos/GitHub/DAM-1/Programación/Unidad 5 - Lectura y escritura de información/Subunidad 7 - Interfaces gráficas
Ruta:  /home/vboxuser/Documentos/GitHub/DAM-1/Programación/Unidad 5 - Lectura y escritura de información/Subunidad 7 - Interfaces gráficas/004 - definimos acción.py  | Tamaño:  0.00024890899658203125 MB
Ruta:  /home/vboxuser/Documentos/GitHub/DAM-1/Programación/Unidad 5 - Lectura y escritura de información/Subunidad 7 - Interfaces gráficas/002 - creamos un botón.py  | Tamaño:  0.00018310546875 MB
Ruta:  /home/vboxuser/Documentos/GitHub/DAM-1/Programación/Unidad 5 - Lectura y escritura de información/Subunidad 7 - Interfaces gráficas/007 - microcalculadora.py  | Tamaño:  0.000362396240234375 MB
Ruta:  /home/vboxuser/Documentos/GitHub/DAM-1/Programación/Unidad 5 - Lectura y escritura de información/Subunidad 7 - Interfaces gráficas/005 - ponemos una etiqueta.py  | Tamaño:  0.0003299713134765625 MB
Ruta:  /home/vboxuser/Documentos/GitHub/DAM-1/Programación/Unidad 5 - Lectura y escritura de información/Subunidad 7 - Interfaces gráficas/003 - command en el botón.py  | Tamaño:  0.00019741058349609375 MB
Ruta:  /home/vboxuser/Documentos/GitHub/DAM-1/Programación/Unidad 5 - Lectura y escritura de información/Subunidad 7 - Interfaces gráficas/008 - calcular.py  | Tamaño:  0.0005321502685546875 MB
Ruta:  /home/vboxuser/Documentos/GitHub/DAM-1/Programación/Unidad 5 - Lectura y escritura de información/Subunidad 7 - Interfaces gráficas/006 - salida en pantalla.py  | Tamaño:  0.00035572052001953125 MB
Ruta:  /home/vboxuser/Documentos/GitHub/DAM-1/Programación/Unidad 5 - Lectura y escritura de información/Subunidad 7 - Interfaces gráficas/001 - tkinter.py  | Tamaño:  0.00011444091796875 MB
```

---

Con este ejercicio hemos aprendido a recorrer carpetas y a diferenciar archivos de carpetas, calculando el tamaño de los archivos en megabytes y mostrando la información en pantalla de manera clara. También comprendimos cómo utilizar las funciones de la librería os para explorar y manipular el sistema de ficheros, lo que es muy útil para proyectos que impliquen gestión de archivos, control de espacio en disco o automatización de tareas. Este trabajo nos permite unir conceptos de programación con aplicaciones prácticas en el día a día, reforzando nuestra comprensión sobre lectura y escritura de información en Python.

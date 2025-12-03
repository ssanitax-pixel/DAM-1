En este ejercicio hemos trabajado con las operaciones básicas de manejo de archivos en Python, una parte fundamental dentro de la programación cuando necesitamos almacenar información de manera permanente. A través del uso del módulo `os` y de las funciones que ya conocemos para abrir archivos, hemos aprendido a crear, escribir, leer y eliminar archivos dentro de una carpeta.

Estas acciones son esenciales en muchos programas que necesitan guardar datos, generar informes, registrar información o simplemente organizar documentación. Además, también hemos visto cómo utilizar bloques `try/except` para manejar errores de forma general, evitando que el programa se detenga si ocurre algún problema, como intentar crear un archivo que ya existe o intentar leer un archivo que no se encuentra disponible.

---

Importamos el módulo `os` para poder trabajar con archivos y directorios.

```
import os
```

Pedimos al usuario el nombre del archivo.

```
nombre = input("Introduce el nombre del archivo que deseas crear: ")
```

Creación del archivo.

```
try:
    if os.path.exists(nombre): # Verificamos si el archivo ya está en la carpeta.
        print("Error: el archivo ya existe.")
    else:
        archivo = open(nombre, "w") # Creamos el archivo en modo escritura.
        archivo.close() # Lo cerramos
        print("Archivo creado correctamente.")
except:
    print("Ocurrió un error al crear el archivo.")
```

Escribir en el archivo.

```
try:
    archivo = open(nombre, "a") # Abrimos el archivo en modo escribir.
    archivo.write("Texto de ejemplo dentro del archivo.\n") # Escribimos una línea.
    archivo.close() # Cerramos el archivo.
    print("Texto escrito correctamente.")
except:
    print("Ocurrió un error al escribir en el archivo.")
```

Leer el archivo.

```
try:
    archivo = open(nombre, "r") # Lo abrimos ahora en modo lectura.
    contenido = archivo.read() # Leemos todo su contenido.
    archivo.close() # Cerramos el archivo.
    print("Contenido del archivo:")
    print(contenido) # Mostramos el contenido por pantalla.
except:
    print("Ocurrió un error al leer el archivo.")
```

Eliminar el archivo.

```
try:
    os.remove(nombre) # Eliminamos el archivo.
    print("Archivo eliminado.")
except:
    print("Ocurrió un error al eliminar el archivo.")
```

---

El código completo queda así:

```
import os

nombre = input("Introduce el nombre del archivo que deseas crear: ")

try:
    if os.path.exists(nombre):
        print("Error: el archivo ya existe.")
    else:
        archivo = open(nombre, "w")
        archivo.close()
        print("Archivo creado correctamente.")
except:
    print("Ocurrió un error al crear el archivo.")

try:
    archivo = open(nombre, "a")
    archivo.write("Texto de ejemplo dentro del archivo.\n")
    archivo.close()
    print("Texto escrito correctamente.")
except:
    print("Ocurrió un error al escribir en el archivo.")

try:
    archivo = open(nombre, "r")
    contenido = archivo.read()
    archivo.close()
    print("Contenido del archivo:")
    print(contenido)
except:
    print("Ocurrió un error al leer el archivo.")
    
try:
    os.remove(nombre)
    print("Archivo eliminado.")
except:
    print("Ocurrió un error al eliminar el archivo.")
```

---

A lo largo de este ejercicio hemos aplicado varias operaciones básicas con archivos utilizando Python. Primero importamos el módulo `os`, necesario para comprobar la existencia de archivos y poder eliminarlos. Después pedimos al usuario el nombre del archivo y verificamos si ya existe antes de crearlo. Una vez creado, abrimos el archivo en modo escritura para añadir contenido y posteriormente lo leímos para mostrar su información por pantalla. Finalmente, eliminamos el archivo correctamente.

Todo el proceso estuvo protegido con bloques `try/except`, lo que nos permitió gestionar posibles errores de manera general sin que el programa se detenga inesperadamente. Con esto hemos reforzado la importancia de mantener seguros los accesos a los archivos y de comprobar siempre su existencia antes de trabajar con ellos.

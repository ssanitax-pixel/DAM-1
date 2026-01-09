En clase hemos aprendido a trabajar con listas para guardar varios datos juntos y a utilizar archivos para que la información pueda mantenerse incluso después de cerrar el programa. También hemos visto cómo guardar estos datos en formato binario usando la herramienta pickle, que permite almacenar estructuras como listas completas. En este ejercicio aplicamos todo esto creando un programa que gestiona un menú de comidas: añadimos elementos, los mostramos y finalmente los guardamos o cargamos desde un archivo binario. Esto nos ayuda a entender cómo se combina la manipulación de datos en memoria con la persistencia en archivos, conceptos básicos y muy importantes en programación.

---

Primero importamos `pickle` para poder guardar y cargar la lista en una archivo binario.

```
import pickle
```

Creamos una lista llamada `menu` donde se irán guardando las comidas que el usuario introduzca.

```
menu = []
```

Después, usamos un bucle infinito con `while True` para mostrar el menú de opciones continuadamente hasta que el programa se cierre.

```
while True:
    print("Opciones:")
    print("1.-Introducir nueva comida en el menú")
    print("2.-Listar comidas en el menú")
    print("3.-Guardar en archivo")
    print("4.-Cargar datos de archivo")
    opcion = int(input("Selecciona una opción: "))
```

Si el usuario selecciona la opción 1, pedirá el nombre de la comida y se añadirá a la lista usando `.append()`.

```
    if opcion == 1:
        comida = input("Introduce el nombre de la comida: ")
        menu.append(comida)
```

Si selecciona la opción 2, recorrerá la lista con un `for` para mostrar todas las comidas que se han añadido hasta el momento.

```
    elif opcion == 2:
        print("Tu comida hasta el momento es: ")
        for elemento in menu:
            print(elemento)
```

Si elige la opción 3, guardamos la lista en un archivo binario usando `pickle.dump()`. Abrimos el archivo con `"wb"` para escritura binaria y luego lo cerramos.

```
    elif opcion == 3:
        archivo = open("datos.bin","wb") # write binary
        pickle.dump(menu,archivo)
        archivo.close()
        print("Se ha guardado con éxito✅")
```

Por último, añadimos de extra la opción 4, que cargará los datos del archivo usando `pickle.load()` y asignaremos la lista recuperada a `menu`. Así podemos seguir trabajando con los datos guardados anteriormente.

```
    elif opcion == 4:
        archivo = open("datos.bin","rb")
        menu = pickle.load(archivo) # volcamos el archivo a la lista
        archivo.close()
```

---

El código completo quedará así:

```
import pickle

menu = []

while True:
    print("Opciones:")
    print("1.-Introducir nueva comida en el menú")
    print("2.-Listar comidas en el menú")
    print("3.-Guardar en archivo")
    print("4.-Cargar datos de archivo")
    opcion = int(input("Selecciona una opción: "))
    if opcion == 1:
        comida = input("Introduce el nombre de la comida: ")
        menu.append(comida)
    elif opcion == 2:
        print("Tu comida hasta el momento es: ")
        for elemento in menu:
            print(elemento)
    elif opcion == 3:
        archivo = open("datos.bin","wb") # write binary
        pickle.dump(menu,archivo)
        archivo.close()
        print("Se ha guardado con éxito✅")
    elif opcion == 4:
        archivo = open("datos.bin","rb")
        menu = pickle.load(archivo) # volcamos el archivo a la lista
        archivo.close()
```

---

En el programa hemos creado una lista donde se almacenan las comidas introducidas por el usuario. El programa permite añadir nuevas comidas, mostrar todas las que hay en el menú, guardar la lista en un archivo binario usando `pickle.dump()` y recuperar los datos guardados con `pickle.load()`. Gracias a este ejercicio hemos practicado el uso de listas, bucles, entrada por teclado y archivos binarios, aplicando todo lo aprendido en clase. Esta actividad demuestra cómo se puede gestionar información de forma sencilla y cómo guardar datos para usarlos más adelante, algo que será muy útil en ejercicios y proyectos más avanzados

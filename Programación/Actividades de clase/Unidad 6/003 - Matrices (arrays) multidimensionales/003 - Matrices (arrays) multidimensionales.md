En esta unidad hemos aprendido a trabajar con matrices multidimensionales en Python, estructuras que nos permiten almacenar y organizar datos de manera eficiente. Una aplicación práctica de estas estructuras es crear una agenda de contactos, donde cada contacto se almacena como un sub-array con su nombre, apellidos, email y teléfono.
Este ejercicio combina el aprendizaje técnico con algo cotidiano: gestionar información de amigos y conocidos, lo cual es útil para organizar actividades sociales o simplemente mantenernos en contacto.

---

Importamos pickle para guardar y leer la agenda en un archivo binario.

```
import pickle
```

Creamos una lista vacía que será nuestra matriz principal.

```
agenda = []
```

Creamos un bucle con `while True`, y dentro también meteremos las opciones del menú.

```
while True:
    print("\nSelecciona una opción: ")
    print("1.- Insertar un registro")
    print("2.- Leer registros")
    print("3.- Guardar registros")
    print("4.- Salir")
```

Pedimos al usuario que seleccione una opción.

```
    opcion = input("Opción escogida: ")
```

Para la opción 1, insertaremos un contacto. Que cada contacto se guardará como un sub-array dentro de la matriz principal.

```
    if opcion == "1":
        # Insertar contacto
        nombre = input("Dime tu nombre: ")
        apellidos = input("Dime tus apellidos: ")
        email = input("Dime tu email: ")
        telefono = input("Dime tu teléfono: ")
        agenda.append([nombre, apellidos, email, telefono])
        print("Contacto añadido correctamente.")
```

Para la opción 2, leeremos contactos desde el archivo binario. Recorremos cada sub-array para mostrar los datos de cada contacto.

```
    elif opcion == "2":
        # Leer contactos desde archivo
        try:
            with open("agenda.bin", "rb") as archivo:
                agenda_leida = pickle.load(archivo)
                print("\nContactos en la agenda:")
                for contacto in agenda_leida:
                    print("Nombre: " + contacto[0] + " " + contacto[1] + ", Email: " + contacto[2] + ", Teléfono: " + contacto[3])
        except FileNotFoundError:
            print("No hay registros guardados aún.")
```

Para la opción 3, guardaremos la agenda en un archivo binario, guardamos la matriz completa en el archivo.

```
    elif opcion == "3":
        # Guardar agenda en archivo
        with open("agenda.bin", "wb") as archivo:
            pickle.dump(agenda, archivo)
        print("Agenda guardada correctamente.")
```

Para la opción 4, saldremos del programa.

```
    elif opcion == "4":
        print("Saliendo del programa...")
        break
```

---

El código completo queda así:

```
import pickle

agenda = []

while True:
    print("\nSelecciona una opción: ")
    print("1.- Insertar un registro")
    print("2.- Leer registros")
    print("3.- Guardar registros")
    print("4.- Salir")
    
    opcion = input("Opción escogida: ")

    if opcion == "1":
        # Insertar contacto
        nombre = input("Dime tu nombre: ")
        apellidos = input("Dime tus apellidos: ")
        email = input("Dime tu email: ")
        telefono = input("Dime tu teléfono: ")
        agenda.append([nombre, apellidos, email, telefono])
        print("Contacto añadido correctamente.")

    elif opcion == "2":
        # Leer contactos desde archivo
        try:
            with open("agenda.bin", "rb") as archivo:
                agenda_leida = pickle.load(archivo)
                print("\nContactos en la agenda:")
                for contacto in agenda_leida:
                    print("Nombre: " + contacto[0] + " " + contacto[1] + ", Email: " + contacto[2] + ", Teléfono: " + contacto[3])
        except FileNotFoundError:
            print("No hay registros guardados aún.")

    elif opcion == "3":
        # Guardar agenda en archivo
        with open("agenda.bin", "wb") as archivo:
            pickle.dump(agenda, archivo)
        print("Agenda guardada correctamente.")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
```

---

Con este ejercicio hemos aplicado los conceptos de matrices multidimensionales para gestionar información de manera organizada y eficiente. Cada contacto se guarda como un sub-array dentro de la agenda, lo que facilita la inserción, visualización y almacenamiento en archivos binarios.
Además, hemos visto cómo Python permite combinar estructuras de datos con módulos como `pickle` para hacer programas prácticos, que podrían ayudarnos en la vida diaria, por ejemplo, organizando nuestros contactos de amigos y conocidos, lo cual es especialmente útil si disfrutamos de actividades sociales y queremos mantenernos conectados.

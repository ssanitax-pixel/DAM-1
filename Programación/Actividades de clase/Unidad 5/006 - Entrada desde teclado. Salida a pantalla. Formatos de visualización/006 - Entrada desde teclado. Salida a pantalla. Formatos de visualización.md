Este programa simula un pequeño sistema de gestión de clientes para un restaurante llamado **“Bar Bara”**.
Permite al usuario **crear, listar, actualizar y eliminar clientes** de manera sencilla, usando un menú interactivo en la consola.

Cada cliente se representa mediante un objeto de la `clase` Cliente, que almacena su ^nombre, apellidos y correo electrónico^.
El programa mantiene todos los clientes en una lista y utiliza identificadores (ID) para poder referirse a cada cliente de forma única al actualizar o eliminar información.

El código está pensado para ser claro, didáctico y fácil de usar, mostrando mensajes de confirmación y evitando modificaciones accidentales.

---

Primero definimos el nombre del restaurante con una variable.

```
nombre_restaurante = "Bar Bara"
```

Luego creamos la clase `Cliente`, que sirve para almacenar los datos de cada cliente.

```
class Cliente():
    def __init__(self,nombre,apellidos,email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
```

Imprimimos un mensaje inicial de bienvenida.

```
print("¡Bienvenido al",nombre_restaurante)
```

Se inicializa una lista vacía donde iremos guardando objetos de tipo `Cliente`

```
clientes = []
```

Con `while True` crearemos un bucle infinito que solo se parará si el usuario cierra el programa.

```
while True:
    print("----Menú de opciones----")
    print("1.-Crear cliente.")
    print("2.-Listar clientes.")
    print("3.-Actualizar cliente.")
    print("4.-Eliminar cliente.")
```

Luego pediremos la opción elegida.

```
    opcion = int(input("Elige una opción: "))
```

Creamos un cliente. Aquí se piden los datos del nuevo cliente y se crea un objeto `Cliente`, que se añade a la lista `clientes`.

```
    if opcion == 1:
        nombre = input("Dime el nombre del cliente: ")
        apellidos = input("Dime los apellidos del cliente: ")
        email = input("Dime el email del cliente: ")
        clientes.append(Cliente(nombre,apellidos,email))
```

Listamos clientes. Recorre la lista de clientes y muestra sus datos. El `identificador` indica la posición del cliente en la lista. Cada vez que imprime un cliente, se incrementa `identificador`.

```
    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print("Id: ",identificador,"|",cliente.nombre,"|",cliente.apellidos,"|",cliente.email)
            identificador += 1
```

Actualizamos cliente. Pide el `idendificador` del cliente que queremos modificar. Pide los nuevos datos. Actualiza los a triburos del cliente con los nuevos valores.

```
    elif opcion == 3:
        identificador = int(input("Dime el identificador del cliente: "))
        nuevo_nombre = input("Dime el nuevo nombre del cliente: ")
        nuevos_apellidos = input("Dime los nuevos apellidos del cliente: ")
        nuevo_email = input("Dime el nuevo email del cliente: ")
        clientes[identificador].nombre = nuevo_nombre
        clientes[identificador].apellidos = nuevos_apellidos
        clientes[identificador].email = nuevo_email
```

Eliminamos cliente. Pide el `identificador` del cliente a eliminar. Solicita confirmación antes de eliminar.

```
    elif opcion == 4:
        identificador = int(input("Dime el identificador del cliente: "))
        confirmacion = input("¿Estás seguro? (s/n): ")
        if confirmacion == "s" or confirmacion == "S":
            clientes.pop(identificador)
        elif confirmacion == "n" or confirmacion == "N":
            print("Eliminación cancelada")
        else:
            print("Opción no válida")
```

---

El código quedará así:

```
nombre_restaurante = "Bar Bara"

class Cliente():
    def __init__(self,nombre,apellidos,email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
    
print("¡Bienvenido al",nombre_restaurante)

clientes = []

while True:
    print("----Menú de opciones----")
    print("1.-Crear cliente.")
    print("2.-Listar clientes.")
    print("3.-Actualizar cliente.")
    print("4.-Eliminar cliente.")
    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        nombre = input("Dime el nombre del cliente: ")
        apellidos = input("Dime los apellidos del cliente: ")
        email = input("Dime el email del cliente: ")
        clientes.append(Cliente(nombre,apellidos,email))
        
    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print("Id: ",identificador,"|",cliente.nombre,"|",cliente.apellidos,"|",cliente.email)
            identificador += 1
    
    elif opcion == 3:
        identificador = int(input("Dime el identificador del cliente: "))
        nuevo_nombre = input("Dime el nuevo nombre del cliente: ")
        nuevos_apellidos = input("Dime los nuevos apellidos del cliente: ")
        nuevo_email = input("Dime el nuevo email del cliente: ")
        clientes[identificador].nombre = nuevo_nombre
        clientes[identificador].apellidos = nuevos_apellidos
        clientes[identificador].email = nuevo_email
        
    elif opcion == 4:
        identificador = int(input("Dime el identificador del cliente: "))
        confirmacion = input("¿Estás seguro? (s/n): ")
        if confirmacion == "s" or confirmacion == "S":
            clientes.pop(identificador)
        elif confirmacion == "n" or confirmacion == "N":
            print("Eliminación cancelada")
        else:
            print("Opción no válida")
```

---

El programa proporciona una forma básica pero funcional de gestionar clientes en un restaurante, permitiendo interactuar con los datos de cada cliente de manera directa y controlada. Aunque es sencillo, sirve como base para desarrollar sistemas más completos, integrando validaciones, almacenamiento permanente o incluso interfaces gráficas. Además, permite practicar conceptos fundamentales de Python, como el uso de clases, listas y bucles, así como la implementación de menús interactivos.

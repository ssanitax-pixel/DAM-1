

Declaramos una clase llamada Cliente, con los atributos de email, nombre y dirección. Iniciamos estos atributos con valores nulos.

```
class Cliente():
    def __init__(self):
        self.email = email
        self.nombre = nombre
        self.direccion = direccion
```

Creamos una lista llamada `clientes` que actuará como una base de datos temporal donde se guardan los objetos creados.

```
clientes = []
```

El programa presenta un menú en consola para permitir al usuario elegir qué acción realizar:

```
while True:
    print("\nElige una opción")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    print("5. Salir")
    opcion = int(input("Opción: "))
```

Cuando el usuario seleccione la opción 1, se solicita la información y se crea un nuevo objeto `Cliente`, que luego se agrega a la lista clientes:

```
    if opcion == 1:
        print("Vamos a crear un cliente")
        nuevocliente = Cliente()
        nuevocliente.email = input("Dime el email del cliente: ")
        nuevocliente.nombre = input("Dime el nombre del cliente: ")
        nuevocliente.direccion = input("Dime la dirección del cliente: ")
```

La opción 2 muestra todos los clientes almacenados, recorriendo la lista y mostrando los atributos de cada uno:

```
elif opcion == 2 :
        print("Vamos a listar los clientes")
        for cliente in clientes:
            print(cliente.email,cliente.nombre,cliente.direccion)
```

La opción 3 permite modificar los datos de un cliente buscando por su nombre:

```
elif opcion == 3:
        print("Vamos a actualizar un cliente")
        nombreborrar = input("Introduce el nombre del usuario a actualizar: ")
        nuevoemail = input("Nuevo email: ")
        nuevonombre = input("Nuevo nombre: ")
        nuevadireccion = input("Nueva dirección: ")
        cliente.email = nuevoemail
        cliente.nombre = nuevonombre
        cliente.direccion = nuevadireccion
```

La opción 4 elimina un cliente de la lista según su nombre:

```
    elif opcion == 4:
        print("Vamos a borrar un cliente: ")
        nombreborrar = input("Introduce el nombre del usuario a borrar: ")
        nombreborrar = clientes.remove(cliente)
```

---

```
class Cliente():
    def __init__(self):
        self.email = ""
        self.nombre = ""
        self.direccion = ""

clientes = []

print("Programa de gestión de clientes v1.0 Ana Sánchez Suárez")

while True:
    print("Elige una opción")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar clientes")
    print("4. Eliminar cliente")
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        print("Vamos a crear un cliente")
        nuevocliente = Cliente()
        nuevocliente.email = input("Dime el email del cliente: ")
        nuevocliente.nombre = input("Dime el nombre del cliente: ")
        nuevocliente.direccion = input("Dime la dirección del cliente: ")
        clientes.append(nuevocliente)
    elif opcion == 2 :
        print("Vamos a listar los clientes")
        for cliente in clientes:
            print(cliente.email,cliente.nombre,cliente.direccion)
    elif opcion == 3:
        print("Vamos a actualizar un cliente")
        nombreborrar = input("Introduce el nombre del usuario a actualizar: ")
        nuevoemail = input("Nuevo email: ")
        nuevonombre = input("Nuevo nombre: ")
        nuevadireccion = input("Nueva dirección: ")
        cliente.email = nuevoemail
        cliente.nombre = nuevonombre
        cliente.direccion = nuevadireccion
    elif opcion == 4:
        print("Vamos a borrar un cliente: ")
        nombreborrar = input("Introduce el nombre del usuario a borrar: ")
        nombreborrar = clientes.remove(cliente)
```

---

Este ejercicio permite comprender la **estructura básica de una clase en Python**, su constructor, y cómo se definen y manipulan sus **miembros** (atributos).
A través de la clase Cliente, se practica la creación de objetos, el almacenamiento de información en listas y la modificación o eliminación de esos objetos desde un programa interactivo.

Además, se introduce de forma implícita el concepto de **visibilidad de los atributos**, entendiendo que, aunque en Python todos los atributos son accesibles públicamente por convención, se pueden manejar como “públicos”, “protegidos” o “privados” según la necesidad del programa.

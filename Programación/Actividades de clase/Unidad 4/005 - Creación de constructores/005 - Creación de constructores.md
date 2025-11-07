En la programación orientada a objetos, una de las prácticas más comunes es la creación de **clases** para representar entidades del mundo real. En este caso, una tienda virtual de mascotas necesita gestionar a sus clientes de forma organizada, guardando su información básica como nombre, apellidos, correo electrónico y dirección.

La **clase** `Cliente` nos permite agrupar estos datos en una sola estructura lógica, facilitando su manipulación, almacenamiento y posterior visualización.
Además, al utilizar un **constructor (`__init__`)**, se inicializan los atributos de cada cliente de manera automática cuando se crea un nuevo objeto. Finalmente, el uso de listas nos permite almacenar múltiples objetos `Cliente`, y un **bucle** hace posible registrar varios clientes de forma dinámica.

---

Creamos la clase cliente.

```
class Cliente():
```

Definimos las variables.

```
    def __init__(self):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
```

Creamos una lista vacía donde almacenaremos los datos de los clientes.

```
clientes = []
```

Creamos un bucle con while y dentro metemos los `input`, para pedir los datos del cliente.

```
while True:
    nombre = input("Dime el nombre del cliente: ")
    apellidos = input("Dime los apellidos del cliente: ")
    email = input("Dime el email del cliente: ")
    direccion = input("Dime dirección del cliente: ")
```

Añadimos los datos de los nuevos clientes a la lista de clientes.

```
    clientes.append(Cliente())
```

Por último listamos los clientes.

```
    for cliente in clientes:
        print(cliente.nombre,"/",cliente.apellidos,"/",cliente.email,"/",cliente.direccion)
```

---

El código completo quedará así:

```
class Cliente():
    def __init__(self):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
        
clientes = []

while True:
    nombre = input("Dime el nombre del cliente: ")
    apellidos = input("Dime los apellidos del cliente: ")
    email = input("Dime el email del cliente: ")
    direccion = input("Dime dirección del cliente: ")

    clientes.append(Cliente())

    for cliente in clientes:
        print(cliente.nombre,"/",cliente.apellidos,"/",cliente.email,"/",cliente.direccion)
```
---

En el desarrollo del ejercicio, hemos definido una clase `Cliente` con los atributos necesarios para representar a cada cliente de la tienda virtual. Posteriormente, mediante el uso de `input`, se solicitaron los datos de los usuarios y se almacenaron los objetos creados dentro de una lista llamada `clientes`.

Finalmente, se recorrió la lista para mostrar la información de cada cliente en pantalla, demostrando cómo el uso de clases, constructores y listas facilita la gestión de información dentro de un programa.

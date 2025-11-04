En este ejercicio, implementamos una aplicación `CRUD` (Crear, Leer, Actualizar, Eliminar) para gestionar clientes. Utilizamos una clase `Cliente` para almacenar la información del cliente, lo que nos permite organizar y manipular los datos de manera eficiente mediante métodos. Para asegurar la persistencia de los datos, usamos la librería `pickle`, que nos permite guardar los datos en un archivo binario y cargarlos al iniciar el programa, asegurando que la información no se pierda entre ejecuciones.

---

Vamos a crear una mini aplicación CRUD.

Para ello empezaremos creando una clase llamada `Cliente`, en este caso con tres propiedades.

```
class Cliente():
    def __init__(self):
        self.nombre = ""
```

Creamos una lista vacía de clientes, que más adelante es donde se irán añadiendo los datos.

```
clientes = []
```

Empezamos a crear un menú, en el que el usuario podrá crear clientes o listar los ya creados, lo haremos dentro de un bucle infinito `while`, para que ahí se atrapen los casos con `if` y `elif`

```
while True:
    print("Menú de selección:")
    print("1. Crear cliente.")
    print("2. Listar clientes.")
    opcion = int(input("Elige opción: "))
    if opcion == 1:
    elif opcion == 2:
```

Procedemos a desarrollar dentro de la opción 1 para que se puedan implementar los clientes.

```
    print("Vamos a crear un cliente.")
```

Definimos un nuevo cliente.

```
        nuevocliente = Cliente()
```

Pedimos los `input` para registrar los datos del cliente.

```
        nuevocliente.nombre = input("Dime el nombre del cliente: ")
```

Añadimos el nuevo cliente a los clientes.

```
        clientes.append(nuevocliente)
```

Ahora desarrollamos la opción dos para listar los clientes registrados anteriormente.

```
    print("Vamos a listar los clientes.")
```

Para listar los clientes será de la siguiente forma:

```
        for cliente in clientes:
            print(cliente.nombre,"/",cliente.apellidos,"/",cliente.email)
```

Ahora para guardar la lista de los clientes, vamos a usar la librería `pickle`.

Lo primero será importar la librería, las librerías se ponen al principio del código.

```
import pickle
```

Ahora vamos a cargar los datos con pickle.

Esta parte está dentro del bloque `try-except` casi al principio del código, justo después de la declaración de la lista clientes:

Dentro del `try` pondremos lo siguiente.

```
try:
```

Abrimos el archivo en modo lectura binaria.

```
    archivo = open("clientes.bin",'rb')
```

Cargamos los datos del archivo, la lista de clientes, en la variable `clientes`.

```
    clientes = pickle.load(archivo)
```

Se recomienda cerrar el archivo después de cargar los datos.

```
    archivo.close()
```

Y ahora dentro del `except`. 

```
except:
```

Si el archivo no existe, imprimos un mensaje.

```
    print("No existe archivo de datos")
```

---

Así quedaría el programa completo:

```
import pickle

class Cliente():
    def __init__(self):
        self.nombre = ""
        self.apellidos = ""
        self.email = ""

clientes = []

try:
    archivo = open("clientes.bin",'rb')
    clientes = pickle.load(archivo)
    archivo.close()
except:
    print("No existe archivo de datos")

while True:
    archivo = open("clientes.bin",'wb')
    pickle.dump(clientes,archivo)
    archivo.close()
    
    print("Menú de selección:")
    print("1. Crear cliente.")
    print("2. Listar clientes.")
    opcion = int(input("Elige opción: "))
    if opcion == 1:
        print("Vamos a crear un cliente.")
        nuevocliente = Cliente()
        nuevocliente.nombre = input("Dime el nombre del cliente: ")
        nuevocliente.apellidos = input("Dime los apellidos del cliente: ")
        nuevocliente.email = input("Dime el email del cliente: ")
        clientes.append(nuevocliente)
    elif opcion == 2:
        print("Vamos a listar los clientes.")
        for cliente in clientes:
            print(cliente.nombre,"/",cliente.apellidos,"/",cliente.email)

```

---

Este ejercicio implementa una aplicación `CRUD` para gestionar clientes, utilizando la librería `pickle` para guardar y cargar datos en un archivo binario. Creamos la clase Cliente para almacenar la información, y un menú interactivo permite al usuario crear y listar clientes. Al final de cada operación, los datos se guardan, asegurando que persistan entre ejecuciones del programa.

En este ejercicio hemos aprendido a trabajar con **ficheros de texto** y **objetos de Python** usando la librería `pickle`.
Primero vimos cómo **crear un fichero de texto**, escribir en él y añadir más contenido al final sin borrar lo anterior.
Después, aprendimos a **leer el contenido de un fichero** línea por línea para poder mostrarlo en la consola.

También creamos una **clase Cliente** con atributos `nombre` y `email`, y vimos cómo guardar una lista de objetos en un fichero binario usando `pickle`.
Finalmente, aprendimos a **recuperar esos objetos** desde el fichero y acceder a sus atributos para mostrarlos.
Con esto integramos los conceptos de **archivos de texto**, **archivos binarios** y **manejo de objetos**, que son fundamentales para guardar y recuperar información en Python.

---

Primero importamos la librería `pickle`, que nos permitirá guardar y recuperar objetos de Python en un fichero binario.

```
import pickle
```

Abrimos el fichero `basededatos.txt` en modo escritura `w`. Si no existe se crea automáticamente, y si existe se borra lo que tenga.

```
archivo = open("basededatos.txt",'w')
archivo.write("esto es otro contenido")
archivo.close()
```

Abrimos el fichero en modo lectura `r` y leemos todas las lineas. `readlines()` devuelve una lista con todas las lineas del fichero.

```
archivo = open("basededatos.txt",'r')
linea = archivo.readlines()
print(linea)
archivo.close()
```

Definimos una clase `Cliente` con dos atributos.

```
class Cliente():
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail
```

Hacemos una lista vacía y añadimos algunos clientes de ejemplo.

```
clientes = []

clientes.append(Cliente("Ana","ana@mail.es"))
clientes.append(Cliente("Fátima","fatima@mail.es"))
```

Abrimos un fichero binario `clientesbin` en modo escritura `wb` y guardamos la lista.

```
archivo = open("clientes.bin",'wb')
pickle.dump(clientes,archivo)
archivo.close()
```

Abrimos el fichero `clientes.bin` en modo lectura binaria `rb` y cargamos la lista.

```
archivo = open("clientes.bin",'rb')
clientes = pickle.load(archivo)
archivo.close()
```

Recorremos la lista y mostramos los atributos de cada cliente.

```
for cliente in clientes:
    print(cliente.nombre, cliente.email)
```

---

El código completo queda así:

```
import pickle

archivo = open("basededatos.txt",'w')
archivo.write("esto es otro contenido")
archivo.close()

archivo = open("basededatos.txt",'a')
archivo.write("esto es un contenido")
archivo.close()

archivo = open("basededatos.txt",'r')
linea = archivo.readlines()
print(linea)
archivo.close()

class Cliente():
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail

clientes = []

clientes.append(Cliente("Ana","ana@mail.es"))
clientes.append(Cliente("Fátima","fatima@mail.es"))

archivo = open("clientes.bin",'wb')
pickle.dump(clientes,archivo)
archivo.close()

archivo = open("clientes.bin",'rb')
clientes = pickle.load(archivo)
archivo.close()

for cliente in clientes:
    print(cliente.nombre, cliente.email)
```

---

Estos conocimientos me ayudan a entender cómo almacenar datos de forma permanente y cómo Python puede gestionar tanto información sencilla (texto) como compleja (objetos).
Además, esto es útil para proyectos futuros donde necesitemos guardar configuraciones, listas de usuarios o datos de aplicaciones de forma segura y organizada.

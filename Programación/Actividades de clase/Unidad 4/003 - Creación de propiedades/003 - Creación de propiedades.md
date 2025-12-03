En esta práctica se trabaja el concepto de **clases y propiedades** dentro de la **Programación Orientada a Objetos** en Python.
Una clase actúa como un molde que define cómo serán los objetos que se creen a partir de ella. Dentro de una clase, las propiedades (o atributos) son variables que almacenan la información del objeto, mientras que los métodos son las funciones que describen su comportamiento.

El objetivo del ejercicio es crear una clase llamada `Cliente` que represente a una persona con la que podríamos quedar para comer o cenar. Cada cliente tendrá un nombre, una edad y una lista de teléfonos. A través de este ejemplo, se busca entender cómo definir propiedades, cómo inicializarlas dentro del método especial __init__, y cómo acceder o modificarlas desde una instancia (objeto).

---

Comenzamos creando la clase `Cliente`, que en este caso tendrá tres propiedades.

```
class Cliente():
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.telefonos = []
```

A continuación, creamos un objeto de la clase, este representara una persona concreta.

```
cliente1 = Cliente()
cliente1.nombre = "Ana"
cliente1.edad = 25
cliente1.telefonos = ["654038456","405639530"]
```

Por último, mostramos la información almacenada en las propiedades del objeto de una forma ordenada.

```
print("Nombre: ",cliente1.nombre)
print("Edad: ",cliente1.edad)
for telefono in cliente1.telefonos:
    print("Teléfono: ",telefono)
```

---

Así queda el código completo:

```
class Cliente():
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.telefonos = []
        
cliente1 = Cliente()
cliente1.nombre = "Ana"
cliente1.edad = 25
cliente1.telefonos = ["654038456","405639530"]

print("Nombre: ",cliente1.nombre)
print("Edad: ",cliente1.edad)
for telefono in cliente1.telefonos:
    print("Teléfono: ",telefono)
```

---

Con este ejercicio hemos aprendido a **definir y utilizar una clase en Python**, comprendiendo cómo funcionan sus **miembros** (atributos y métodos) y su visibilidad.
Hemos creado la clase `Cliente` con tres propiedades básicas y comprobado cómo se pueden inicializar y acceder desde fuera de la clase mediante un objeto.

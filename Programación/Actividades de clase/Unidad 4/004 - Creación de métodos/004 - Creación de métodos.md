En este ejercicio trabajamos con el concepto de clases y objetos dentro de la Programación Orientada a Objetos (POO) en Python, aplicándolo a una situación práctica y cotidiana: gestionar la información de nuestros amigos al organizar una cena.

Una clase puede entenderse como un molde o plantilla que define cómo serán los objetos que creemos a partir de ella. Cada objeto representa una instancia individual de esa clase, con sus propios datos (atributos) y acciones (métodos).

La clase que desarrollaremos, llamada Cliente, permitirá almacenar y acceder a información personal, como el nombre completo y el correo electrónico de cada cliente (o amigo). Para garantizar un buen diseño, emplearemos métodos setter y getter, que sirven para asignar y obtener valores de forma controlada, promoviendo así la encapsulación, uno de los principios fundamentales de la POO.

---

Creamos la clase Cliente, que tendrá dos atributos principales de `nombrecompleto` y `email`
Usamos el método especial __init__ para inicializar estos atributos cuando se crea un nuevo objeto.

```
class Cliente():
    def __init__(self):
        self.nombrecompleto = ""
        self.email = ""
```

Los métodos setter se utilizan para asignar valores a los atributos, mientras que los métodos getter permiten obtener esos valores.
De esta forma, controlamos el acceso a los datos internos del objeto.

```
    def setNombreCompleto(self,nuevonombre):
        self.nombrecompleto = nuevonombre
    def setEmail(self,nuevoemail):
        self.email = nuevoemail
    def getNombreCompleto(self):
        return self.nombrecompleto
    def getEmail(self):
        return self.email
```

Podemos crear un cliente y establecer sus datos utilizando los métodos creados:

```
# Creamos un objeto Cliente
cliente1 = Cliente()

# Asignamos valores usando los métodos setter
cliente1.setNombreCompleto("Ana Sánchez Suárez")
cliente1.setEmail("ana@example.com")

# Mostramos los datos usando los métodos getter
print("Nombre:", cliente1.getNombreCompleto())
print("Email:", cliente1.getEmail())
```

Imaginemos que estamos organizando una cena con nuestros amigos y queremos gestionar sus datos de contacto.
Creamos varios objetos `Cliente`, uno por cada amigo, y almacenamos sus nombres y correos electrónicos.

```
# Creamos objetos para cada amigo
amigo1 = Cliente()
amigo1.setNombreCompleto("Carlos López")
amigo1.setEmail("carlos.lopez@gmail.com")

amigo2 = Cliente()
amigo2.setNombreCompleto("María García")
amigo2.setEmail("maria.garcia@gmail.com")

amigo3 = Cliente()
amigo3.setNombreCompleto("Luis Fernández")
amigo3.setEmail("luis.fernandez@gmail.com")

# Mostramos la información de todos los amigos
print("\nLista de invitados a la cena:")
print(amigo1.getNombreCompleto(), "-", amigo1.getEmail())
print(amigo2.getNombreCompleto(), "-", amigo2.getEmail())
print(amigo3.getNombreCompleto(), "-", amigo3.getEmail())
```

---

El código completo quedará así:

```
class Cliente():
    def __init__(self):
        self.nombrecompleto = ""
        self.email = ""
    def setNombreCompleto(self,nuevonombre):
        self.nombrecompleto = nuevonombre
    def setEmail(self,nuevoemail):
        self.email = nuevoemail
    def getNombreCompleto(self):
        return self.nombrecompleto
    def getEmail(self):
        return self.email

cliente1 = Cliente()

cliente1.setNombreCompleto("Ana Sánchez Suárez")
cliente1.setEmail("ana@example.com")

print("Nombre:", cliente1.getNombreCompleto())
print("Email:", cliente1.getEmail())

amigo1 = Cliente()
amigo1.setNombreCompleto("Carlos López")
amigo1.setEmail("carlos.lopez@gmail.com")

amigo2 = Cliente()
amigo2.setNombreCompleto("María García")
amigo2.setEmail("maria.garcia@gmail.com")

amigo3 = Cliente()
amigo3.setNombreCompleto("Luis Fernández")
amigo3.setEmail("luis.fernandez@gmail.com")

print("Lista de invitados a la cena:")
print(amigo1.getNombreCompleto(), "-", amigo1.getEmail())
print(amigo2.getNombreCompleto(), "-", amigo2.getEmail())
print(amigo3.getNombreCompleto(), "-", amigo3.getEmail())
```

---

Este ejercicio ha permitido comprender de manera práctica cómo crear una clase en Python con atributos y métodos, aplicando el principio de encapsulación mediante el uso de setters y getters.
A través del ejemplo de organizar una cena con amigos, se ha visto cómo la programación orientada a objetos nos ayuda a gestionar información de manera estructurada y reutilizable, representando cada amigo como un objeto con sus propios datos.

La práctica refuerza la comprensión de los conceptos básicos de clases, objetos, propiedades y métodos, que son esenciales para cualquier programa que maneje datos relacionados entre sí.
Además, demuestra cómo la POO puede aplicarse en situaciones cotidianas, permitiendo automatizar tareas o gestionar información de forma más eficiente.

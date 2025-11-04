En la programación orientada a objetos, los métodos `get` y `set` son fundamentales para **acceder y modificar de manera controlada los atributos de una clase**. El método `get` permite **leer el valor de una propiedad**, mientras que el `set` se utiliza para **actualizarla**. En este ejercicio, creamos una clase llamada Cliente con varias propiedades y aplicamos estos métodos para gestionar sus datos, demostrando cómo mejorar la flexibilidad y seguridad del código.

---

Primero vamos a crear una clase llamada `Cliente`.

```
class Cliente():
    def __init__(self):
```

Seguidamente le añadimos las propiedades, que en este caso serán `nombre`, `apellidos`, `email` y `direccion`.

```
        self.nombre = nombre
```

Creamos un método set y un método set para cada una de las propiedades, aquí está como se haría, así para casa una.

```
    def setNombre(self,nuevonombre):
        self.nombre = nuevonombre
    def getNombre(self):
        return self.nombre
```

Creamos tres instancias de la clase, cada una de ellas con sus propias propiedades.

```
cliente1 = Cliente("Ana", "Sánchez Suárez", "ana@gmail.com", "Casa")
```

Por último, para demostrar que los métodos set y get funcionan correctamente, los sacaremos por pantalla.

```
print("Email original del cliente1:", cliente1.getEmail())
cliente1.setEmail("anasanchezsuarez@email.com")
print("Email actualizado del cliente1:", cliente1.getEmail())
```

---

El código completo queda tal que así:

```
class Cliente():
    def __init__(self,nombre,apellidos,email,direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
    def setNombre(self,nuevonombre):
        self.nombre = nuevonombre
    def setApellidos(self,nuevoapellidos):
        self.apellidos = nuevoapellidos
    def setEmail(self,nuevoemail):
        self.email = nuevoemail
    def setDireccion(self,nuevodireccion):
        self.direccion = nuevodireccion
    def getNombre(self):
        return self.nombre
    def getApellidos(self):
        return self.apellidos
    def getEmail(self):
        return self.email
    def getDireccion(self):
        return self.direccion
        
cliente1 = Cliente("Ana", "Sánchez Suárez", "ana@gmail.com", "Casa")
cliente2 = Cliente("María", "Sánchez Suárez", "maria@gmail.com", "Apartamento")
cliente3 = Cliente("Fátima", "Quiñones Torres", "fatima@gmail.com", "Chalet")

print("")
print("Email original del cliente1:", cliente1.getEmail())
cliente1.setEmail("anasanchezsuarez@email.com")
print("Email actualizado del cliente1:", cliente1.getEmail())

print("Email original del cliente2:", cliente2.getEmail())
cliente2.setEmail("mariasanchezsuarez@email.com")
print("Email actualizado del cliente2:", cliente2.getEmail())

print("Email original del cliente3:", cliente3.getEmail())
cliente3.setEmail("fatimaquinonestorres@email.com")
print("Email actualizado del cliente3:", cliente3.getEmail())
print("")
```

---

En este ejercicio, hemos demostrado cómo crear una clase en Python, definir sus propiedades y utilizar métodos `get` y `set` para interactuar con esas propiedades. A través de la creación de tres instancias de la clase Cliente, cada una con valores propios para sus atributos, pudimos verificar que estos métodos funcionan correctamente, permitiendo acceder y actualizar los datos de manera controlada. El uso de estos métodos no solo facilita la manipulación de los atributos de una clase, sino que también contribuye a un diseño más limpio y modular del código.

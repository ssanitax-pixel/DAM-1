En la programación orientada a objetos, la herencia es un mecanismo que nos permite crear una clase nueva (subclase) a partir de una existente (superclase). En Python, esto nos permite organizar el código de forma jerárquica: definimos los atributos comunes en una clase "base" y las clases hijas los heredan automáticamente.

En este ejemplo, hemos creado la superclase `Persona` que contiene los datos básicos, y dos subclases, `Profesor` y `Alumno`, que se benefician de toda esa estructura sin tener que volver a escribirla.

---

Definimos la clase base `Persona`. Esta clase es la "madre" de todas las demás. En su constructor `__init__`, definimos los cuatro datos básicos que cualquier persona tendrá en nuestro sistema.

```
class Persona():
    def __init__(self, nombre, apellidos, email, direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
```

Creamos el método `dameDatos()`. Este método es común para todos. Su función es simplemente concatenar el nombre y los apellidos con un espacio para devolver el nombre completo.

```
def dameDatos(self):
    return self.nombre+" "+self.apellidos
```

Definimos la clase `Profesor` indicando entre paréntesis que hereda de Persona. Al usar `super().__init__`, lo que estamos haciendo es llamar al constructor de la clase padre para que rellene los datos automáticamente.

```
class Profesor(Persona):
    def __init__(self, nombre, apellidos, email, direccion):
        super().__init__(nombre, apellidos, email, direccion)
```

Hacemos exactamente lo mismo con la clase `Alumno`. Al heredar de `Persona`, esta clase ya tiene acceso al método `dameDatos()` sin necesidad de volver a escribirlo.

```
class Alumno(Persona):
    def __init__(self, nombre, apellidos, email, direccion):
        super().__init__(nombre, apellidos, email, direccion)
```

Finalmente, creamos las instancias (objetos reales) con los datos del enunciado. Llamamos al método `dameDatos()` desde ambos objetos para comprobar que la herencia funciona correctamente.

```
profesor1 = Profesor("Juan","García","juan@jocarsa.com","Dirección")
alumno1 = Alumno("Jose Vicente","Carratalá","info@jocarsa.com","Dirección")

print(profesor1.dameDatos())
print(alumno1.dameDatos())
```

---

El código completo quedará así:

```
class Persona():
    def __init__(self, nombre, apellidos, email, direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
    def dameDatos(self):
        return self.nombre+" "+self.apellidos
        
class Profesor(Persona):
    def __init__(self, nombre, apellidos, email, direccion):
        super().__init__(nombre, apellidos, email, direccion)

class Alumno(Persona):
    def __init__(self, nombre, apellidos, email, direccion):
        super().__init__(nombre, apellidos, email, direccion)
        
profesor1 = Profesor("Juan","García","juan@jocarsa.com","Dirección")

alumno1 = Alumno("Jose Vicente","Carratalá","info@jocarsa.com","Dirección")

print(profesor1.dameDatos())
print(alumno1.dameDatos())
```

---

Hemos conseguido modelar una situación escolar mediante una jerarquía de clases. Lo más importante es que, gracias a la herencia, si quisiéramos añadir una nueva funcionalidad (por ejemplo, un método para validar el email), solo tendríamos que hacerlo en la clase `Persona` y tanto los alumnos como los profesores lo tendrían disponible al instante. Esto nos demuestra cómo la POO nos ayuda a escribir programas mucho más eficientes y fáciles de mantener.

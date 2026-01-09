La herencia es un pilar fundamental de la Programación Orientada a Objetos que nos permite organizar el código de forma jerárquica y eficiente. Mediante este mecanismo, definimos una clase "base" o superclase que agrupa los atributos y comportamientos comunes, permitiendo que las clases hijas los hereden automáticamente para evitar la duplicidad de código.

Por otro lado, el polimorfismo es la capacidad que tienen los objetos de diferentes clases de responder al mismo mensaje de formas distintas. En Python, esto se traduce en que una subclase puede proporcionar su propia implementación de un método que ya existe en el padre (sobrescritura). Gracias a esto, podemos tratar a todos los asistentes como "Personas" genéricas pero obtener resultados específicos según si son profesores o alumnos, haciendo que nuestro software sea mucho más flexible y adaptable a situaciones reales.

---

Definimos la clase base `Persona` como la "madre" de todas las demás clases de nuestro sistema.

```
class Persona():
```

En su constructor `__init__`, inicializamos las propiedades básicas de nombre y apellidos.

```
def __init__(self,nombre,apellidos):
    self.nombre = nombre
    self.apellidos = apellidos
```

Creamos el método `dameDatos()`. Este método devuelve la suma de las propiedades para dar una identificación básica.

```
def dameDatos(self):
    return self.nombre+self.apellidos
```

Definimos la clase `Profesor` indicando expresamente que hereda de la clase `Persona`.

```
class Profesor(Persona):
```

Usamos `super().__init__` para reutilizar el constructor del padre. Redefinimos `dameDatos()` para añadir el prefijo de su rol.

```
def __init__(self,nombre,apellidos):
    super().__init__(nombre, apellidos)
def dameDatos(self):
    return "Profesor: "+self.nombre+" "+self.apellidos
```

Hacemos lo mismo con la clase `Alumno`, heredando de nuevo todas las capacidades de `Persona`.

```
class Alumno(Persona):
```

También usamos el constructor del padre mediante `super()`. Redefinimos su propio método `dameDatos()` para que se identifique como alumno.

```
def __init__(self,nombre,apellidos):
    super().__init__(nombre, apellidos)
def dameDatos(self):
    return "Alumno: "+self.nombre+" "+self.apellidos
```

Creamos los objetos reales con los datos específicos de los asistentes que van a venir a casa.

```
alumno1 = Alumno("Jose Vicente","Carratala")
profesor1 = Profesor("Juan","Garcia")
```

Llamamos al método `dameDatos()` desde ambos objetos. Python se encarga de ejecutar la versión correcta para cada uno de forma automática.

```
print(alumno1.dameDatos())
print(profesor1.dameDatos())
```

---

Así queda en código completo:

```
class Persona():
    def __init__(self,nombre,apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
    def dameDatos(self):
        return self.nombre+self.apellidos

class Profesor(Persona):
    def __init__(self,nombre,apellidos):
        super().__init__(nombre, apellidos)
    def dameDatos(self):
        return "Profesor: "+self.nombre+" "+self.apellidos
  
class Alumno(Persona):
    def __init__(self,nombre,apellidos):
        super().__init__(nombre, apellidos)
    def dameDatos(self):
        return "Alumno: "+self.nombre+" "+self.apellidos

alumno1 = Alumno("Jose Vicente","Carratala")
print(alumno1.dameDatos())

profesor1 = Profesor("Juan","Garcia")
print(profesor1.dameDatos())
```

---

Este ejercicio nos demuestra que la combinación de herencia y polimorfismo es vital para modelar la complejidad del mundo real dentro de un programa. Al organizar un evento social, nos ahorramos tener que escribir condiciones complejas para saber cómo tratar a cada invitado, simplemente confiamos en que cada objeto "conoce" su identidad y sabe cómo presentarse.

Esta forma de programar no solo hace que el código sea más limpio y fácil de leer, sino que facilita enormemente el mantenimiento futuro. Si mañana quisiéramos añadir un nuevo tipo de asistente, como un "InvitadoEspecial", solo tendríamos que heredar de Persona y definir su método de presentación sin tocar ni una sola línea del código que ya funciona. Es un salto de calidad necesario para cualquier desarrollador que aspire a crear aplicaciones profesionales y escalables.

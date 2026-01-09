En el desarrollo de software profesional, aplicamos el concepto de Herencia para organizar clases en jerarquías de "padre" e "hijo". Esta técnica es fundamental para la Programacion Orientada a Objetos, porque nos permite definir atributos y comportamientos comunes en una Superclase (Persona) y reutilizarlos en Subclases más específicas (Profesor y Alumno).

La importancia de este modelo viene en la economía de código, evitamos repetir las mistas variables en múltiples lugares, lo que facilita el mantenimiento y asegura que la estructura de nuestra aplicación sea coherente con el diseño de nuestra base de datos relacional.

---

Explicación del JSON:
- Definición de Entidades: Hemos creado tres entidades principales. La entidad Persona actúa como el núcleo (Superclase) al contener el nombre, apellidos y email, que son datos universales para cualquier usuario del centro.
- Especialización de Clases:
    - Profesor: L asignamos el atributo específico `asignatura`, heredando el resto de la madre.
    - Alumno: Le otorgamos el campo `nota` para gestionar su rendimiento académico.
- Método `dameDatos()`: Hemos implementado este método siguiendo el principio de polimorfismo. Cada clase "hija" utiliza la instrucción `super().dameDatos()` para recuperar la información básica de la "madre" y añadirle sus propios detalles específicos.

Explicación del código de Python:
Creamos la clase madre.

```
class Persona:
```

Creamos el constructor con sus atributos.

```
    def __init__(self, nuevo_id, nuevo_nombre, nuevos_apellidos, nuevo_email):
        self.id = nuevo_id
        self.nombre = nuevo_nombre
        self.apellidos = nuevos_apellidos
        self.email = nuevo_email
```

Creamos un método llamado `dameDatos` para devolver los datos de la persona.

```
    def dameDatos(self):
        # Devolvemos la información universal
        return f"[{self.id}] {self.nombre} {self.apellidos} ({self.email})"
```

Creamos la clase `Profesor` que heredará todo lo que tenga `Persona`, y un dato extra.

```
class Profesor(Persona):
    def __init__(self, nuevo_id, nuevo_nombre, nuevos_apellidos, nuevo_email, nueva_asignatura):
        super().__init__(nuevo_id, nuevo_nombre, nuevos_apellidos, nuevo_email)
        self.asignatura = nueva_asignatura
```

Sobreescribimos el código del método, para que se use este en vez de la madre.

```
    def dameDatos(self):
        # Extendemos la información de la madre
        datos_madre = super().dameDatos()
        return f"{datos_madre} | PUESTO: Profesor de {self.asignatura}"
```

Haremos lo mismo con otra clase llamada `Alumno`.

```
class Alumno(Persona):
    def __init__(self, nuevo_id, nuevo_nombre, nuevos_apellidos, nuevo_email, nueva_nota):
        super().__init__(nuevo_id, nuevo_nombre, nuevos_apellidos, nuevo_email)
        self.nota = nueva_nota

    def dameDatos(self):
        # Extendemos la información con el rendimiento
        datos_madre = super().dameDatos()
        return f"{datos_madre} | ESTADO: Alumno con nota {self.nota}"
```

Creamos objetos para poder ver que todo funciona correctamente.

```
profe = Profesor(1, "Jose Vicente", "Carratalá", "info@jocarsa.com", "Bases de Datos")
estudiante = Alumno(2, "Ana", "Sánchez Suárez", "ssanitax@gmail.com", 10)

print(profe.dameDatos())
print(estudiante.dameDatos())
```

---

Hemos comprobado que el uso de la herencia no solo hace que nuestro código sea más elegante, sino que establece una conexión directa con los entornos de desarrollo profesionales y las bases de datos. Este modelo de Superclase y Subclase es el reflejo de las relaciones de especialización que nosotros diseñamos en SQL mediante clases foráneas.

Al dominar esta estructura, estamos preparados para construir aplicaciones modulares donde la lógica está centralizada y los datos están perfectamente jerarquizados, garantizando la escalabilidad de cualquier proyecto intermodular.

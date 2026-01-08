# Definimos la clase madre con los datos comunes
class Persona:
    def __init__(self, nuevo_id, nuevo_nombre, nuevos_apellidos, nuevo_email):
        self.id = nuevo_id
        self.nombre = nuevo_nombre
        self.apellidos = nuevos_apellidos
        self.email = nuevo_email

    def dameDatos(self):
        # Devolvemos la información universal
        return f"[{self.id}] {self.nombre} {self.apellidos} ({self.email})"

# Creamos la subclase para los docentes
class Profesor(Persona):
    def __init__(self, nuevo_id, nuevo_nombre, nuevos_apellidos, nuevo_email, nueva_asignatura):
        super().__init__(nuevo_id, nuevo_nombre, nuevos_apellidos, nuevo_email)
        self.asignatura = nueva_asignatura

    def dameDatos(self):
        # Extendemos la información de la madre
        datos_madre = super().dameDatos()
        return f"{datos_madre} | PUESTO: Profesor de {self.asignatura}"

# Creamos la subclase para los estudiantes
class Alumno(Persona):
    def __init__(self, nuevo_id, nuevo_nombre, nuevos_apellidos, nuevo_email, nueva_nota):
        super().__init__(nuevo_id, nuevo_nombre, nuevos_apellidos, nuevo_email)
        self.nota = nueva_nota

    def dameDatos(self):
        # Extendemos la información con el rendimiento
        datos_madre = super().dameDatos()
        return f"{datos_madre} | ESTADO: Alumno con nota {self.nota}"

# --- PRUEBA DE FUNCIONAMIENTO ---
profe = Profesor(1, "Jose Vicente", "Carratalá", "info@jocarsa.com", "Bases de Datos")
estudiante = Alumno(2, "Ana", "Sánchez Suárez", "ssanitax@gmail.com", 10)

print(profe.dameDatos())
print(estudiante.dameDatos())

-- crea datos de muestra, en español, tantos como puedas, no hay foreign key reales, pero están sugeridas

-- ALUMNOS
INSERT INTO alumnos (Identificador, nombre, apellidos) VALUES
(1, 'María', 'Gómez Ortega'),
(2, 'Juan', 'Pérez Díaz'),
(3, 'Lucía', 'Martín Salas'),
(4, 'Carlos', 'Ruiz Herrera'),
(5, 'Sofía', 'López Medina'),
(6, 'Andrés', 'Serrano Torres'),
(7, 'Elena', 'Vargas Molina'),
(8, 'Diego', 'Santos Fuentes'),
(9, 'Paula', 'Navarro Álvarez'),
(10, 'Hugo', 'Castro Rivas');

-- PROFESORES
INSERT INTO profesores (Identificador, nombre, apellidos) VALUES
(1, 'Antonio', 'Benítez Ramos'),
(2, 'Laura', 'Gil Fernández'),
(3, 'Miguel', 'Sáez Camacho'),
(4, 'Isabel', 'Morales Cano'),
(5, 'Javier', 'Cuesta Barrios');

-- ASIGNATURAS
INSERT INTO asignaturas (Identificador, nombre, id_profesor) VALUES
(1, 'Matemáticas I', 1),
(2, 'Lengua y Literatura', 2),
(3, 'Historia Universal', 4),
(4, 'Física General', 1),
(5, 'Química Básica', 3),
(6, 'Biología y Geología', 5),
(7, 'Filosofía', 4),
(8, 'Educación Física', 2),
(9, 'Tecnología', 3),
(10, 'Inglés Avanzado', 5);

-- MATRICULAS
INSERT INTO matriculas (Identificador, id_asignatura, id_alumno) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 2, 1),
(5, 2, 4),
(6, 2, 5),
(7, 3, 6),
(8, 3, 7),
(9, 4, 2),
(10, 4, 8),
(11, 5, 3),
(12, 5, 9),
(13, 6, 4),
(14, 6, 10),
(15, 7, 5),
(16, 8, 6),
(17, 9, 7),
(18, 10, 8),
(19, 10, 9),
(20, 10, 10);


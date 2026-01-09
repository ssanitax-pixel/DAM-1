CREATE DATABASE IF NOT EXISTS composiciones;
USE composiciones;

CREATE TABLE alumnos(Identificador INT PRIMARY KEY, nombre VARCHAR(100), apellidos VARCHAR(100));
CREATE TABLE asignaturas(Identificador INT PRIMARY KEY, nombre VARCHAR(100), id_profesor INT);
CREATE TABLE matriculas(Identificador INT PRIMARY KEY, id_asignatura INT, id_alumno INT);

CREATE VIEW matriculas_join AS 
SELECT 
asignaturas.nombre AS 'Nombre de la asignatura',
alumnos.nombre AS 'Nombre del alumno',
alumnos.apellidos AS 'Apellidos del alumno'
FROM matriculas
LEFT JOIN asignaturas ON matriculas.id_asignatura = asignaturas.Identificador
LEFT JOIN alumnos ON matriculas.id_alumno = alumnos.Identificador;

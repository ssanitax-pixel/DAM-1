sudo mysql -u root -p

CREATE DATABASE blog2;

SHOW DATABASES;

USE blog2;

CREATE TABLE autores (
    Identificador INT(10),
    nombre VARCHAR(100),
    apellidos VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE autores (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellidos VARCHAR(100),
    email VARCHAR(100)
);

SHOW TABLES;

ALTER TABLE autores
DROP Identificador;

ALTER TABLE autores
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;

DESCRIBE autores;

INSERT INTO autores VALUES(
    NULL,
    'Ana',
    'Sánchez',
    'ana@gmail.com'
);

SELECT * FROM autores;

CREATE TABLE entradas (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    fecha VARCHAR(100),
    imagen VARCHAR(100),
    id_autor VARCHAR(100),
    contenido TEXT
);

SHOW TABLES;

DESCRIBE entradas;

ALTER TABLE entradas
ADD CONSTRAINT autores_a_entradas
FOREIGN KEY (id_autor) REFERENCES autores(Identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE entradas
MODIFY COLUMN id_autor INT;

ALTER TABLE entradas
ADD CONSTRAINT autores_a_entradas
FOREIGN KEY (id_autor) REFERENCES autores(Identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;

INSERT INTO entradas VALUES(
    NULL,
    'Título de la primera entrada'.
    '2025-11-03',
    'imagen.jpg',
    1,
    'Este es el contenido de la primera entrada'
);

SELECT * FROM entradas;

SELECT
entradas.titulo,entradas.fecha,entradas.imagen,entradas.contenido
autores.nombre,autores.apellidos
FROM entradas
LEFT JOIN autores
ON entradas.id_autor = autores.Identificador;

CREATE VIEW vista_entradas AS
SELECT
entradas.titulo,entradas.fecha,entradas.imagen,entradas.contenido
autores.nombre,autores.apellidos
FROM entradas
LEFT JOIN autores
ON entradas.id_autor = autores.Identificador;

SELECT * FROM vista_entradas;


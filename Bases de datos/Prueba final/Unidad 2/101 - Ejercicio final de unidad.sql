sudo mysql -u root -p

CREATE DATABASE biblioteca25;

USE biblioteca25;

SELECT DATABASE();

CREATE TABLE autores (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  pais VARCHAR(80) NULL
);

DESCRIBE autores;

CREATE TABLE libros (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(200) NOT NULL,
  isbn VARCHAR(20) NOT NULL UNIQUE,
  precio DECIMAL(8,2) NOT NULL CHECK (precio >= 0),
  autor_id INT NOT NULL,
  FOREIGN KEY (autor_id) REFERENCES autores(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

CREATE INDEX idx_titulo ON libros(titulo);

DESCRIBE libros;

SHOW INDEX FROM libros;

CREATE TABLE socios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    fecha_alta TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

INSERT INTO socios (nombre, email) 
    -> VALUES ('Juan Pérez', 'juanexamplecom');
ERROR 3819 (HY000): Check constraint 'socios_chk_1' is violated.

INSERT INTO socios (nombre, email)
VALUES ('Juan Pérez', 'juan.perez@example.com');

INSERT INTO socios (nombre, email)
VALUES ('María Gómez', 'maria.gomez@empresa.org');

DESCRIBE socios;

CREATE TABLE prestamos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    socio_id INT NOT NULL,
    libro_id INT NOT NULL,
    fecha_prestamo TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_devolucion DATE NULL,
    CHECK (fecha_devolucion IS NULL OR fecha_devolucion >= fecha_prestamo),
    FOREIGN KEY (socio_id) REFERENCES socios(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (libro_id) REFERENCES libros(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE INDEX idx_socio_libro ON prestamos(socio_id, libro_id);

SHOW INDEX FROM prestamos;

INSERT INTO socios (nombre, email)
VALUES 
('Juan Pérez', 'juan.perez@example.com'),
('María Gómez', 'maria.gomez@empresa.org');

INSERT INTO libros (titulo, isbn, precio, autor_id)
VALUES 
('El Gran Libro', '1234567890', 19.99, 1),
('La Aventura de Hoy', '0987654321', 15.50, 2); 

DESCRIBE prestamos;

INSERT INTO autores (nombre, pais)
VALUES 
    ('Gabriel García Márquez', 'Colombia'),
    ('J.K. Rowling', 'Reino Unido'),
    ('George Orwell', 'Reino Unido');
    
INSERT INTO libros (titulo, isbn, precio, autor_id)
VALUES 
    ('Cien años de soledad', '978-3-16-148410-0', 19.99, 3),
    ('Harry Potter y la piedra filosofal', '978-0-7475-3269-9', 15.99, 4),
    ('1984', '978-0-452-28423-4', 12.99, 5);

INSERT INTO socios (nombre, email)
VALUES 
    ('Ana Sánchez', 'ana.sanchez@example.com'),
    ('Alfredo Martínez', 'alfredo.martinez@example.com');

INSERT INTO prestamos (socio_id, libro_id, fecha_prestamo)
VALUES (5, 14, CURRENT_TIMESTAMP);

INSERT INTO prestamos (socio_id, libro_id, fecha_prestamo, fecha_devolucion)
VALUES (6, 15, '2023-10-01', '2023-10-10');



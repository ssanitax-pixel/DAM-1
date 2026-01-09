-- Creamos el entorno para los patos
CREATE DATABASE tiendapatos;
USE tiendapatos;

CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    id_categoria INT NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

-- Insertamos datos de ejemplo siguiendo el orden jerárquico
INSERT INTO categorias (nombre) VALUES ('Profesiones'), ('Superhéroes');
INSERT INTO productos (nombre, precio, id_categoria) VALUES ('Pato Programador', 12.50, 1),
('Pato Batman', 15.99, 2),
('Pato Spiderman', 15.99, 2),
('Pato Wonder Woman', 16.50, 2),
('Pato Iron Man', 17.00, 2),
('Pato Hulk', 14.99, 2),
('Pato Joker', 15.00, 2);

-- Creamos la vista para facilitar la consulta desde Flask
CREATE VIEW vw_patos AS
SELECT p.nombre, p.precio, c.nombre AS categoria
FROM productos p
JOIN categorias c ON p.id_categoria = c.id_categoria;

-- 1. Creamos el usuario de la tienda
CREATE USER 'patos_user'@'localhost' IDENTIFIED BY 'Patos123$';

-- 2. Configuramos sus límites (opcional pero recomendado en el temario)
ALTER USER 'patos_user'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- 3. Le damos el control total sobre la base de datos de patos
GRANT ALL PRIVILEGES ON tiendapatos.* TO 'patos_user'@'localhost';

-- 4. Aplicamos los cambios inmediatamente
FLUSH PRIVILEGES;

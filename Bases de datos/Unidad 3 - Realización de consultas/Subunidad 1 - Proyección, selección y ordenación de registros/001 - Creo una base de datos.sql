-- sudo mysql -u root -p

CREATE DATABASE clientes;

USE clientes;

CREATE TABLE clientes (
	nombre VARCHAR(255),
	apellidos VARCHAR(255),
	edad INT
);

-- podemos usar ia para crear inserts
INSERT INTO clientes VALUES
('Juan', 'Pérez', 28),
('María', 'Gómez', 34),
('Carlos', 'Rodríguez', 22),
('Laura', 'Martínez', 29),
('Pedro', 'Sánchez', 41),
('Ana', 'López', 25),
('Javier', 'Hernández', 36),
('Marta', 'González', 32),
('David', 'Ramírez', 45),
('Elena', 'Fernández', 38),
('Luis', 'Díaz', 30),
('Carmen', 'Álvarez', 27),
('Raúl', 'Mendoza', 33),
('Beatriz', 'Torres', 50),
('José', 'Vázquez', 48),
('Susana', 'Morales', 23),
('Ricardo', 'Castro', 26),
('Patricia', 'Ruiz', 39),
('Manuel', 'Jiménez', 47),
('Victoria', 'Jiménez', 31),
('Andrés', 'Paredes', 44),
('Raquel', 'Suárez', 29),
('Fernando', 'Ríos', 56),
('Nuria', 'Cordero', 40),
('Isabel', 'Serrano', 22),
('Sergio', 'Navarro', 37),
('Daniela', 'Romero', 24),
('Óscar', 'García', 46),
('Antonio', 'Silva', 52),
('Elena', 'Moreno', 55);


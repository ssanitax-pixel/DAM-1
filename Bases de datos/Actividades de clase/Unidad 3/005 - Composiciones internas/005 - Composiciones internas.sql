-- Creamos la base de datos si no existe y la seleccionamos
CREATE DATABASE IF NOT EXISTS tiendaclase;
USE tiendaclase;

-- Tabla para almacenar la información de los clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    fecha_registro VARCHAR(100)
);

-- Tabla para el catálogo de productos
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0
);

-- Insertamos datos de ejemplo para verificar que todo funciona
INSERT INTO clientes (nombre, email, telefono)
VALUES
    ('Ana López', 'ana@example.com', '600123456'),
    ('Carlos Ruiz', 'carlos@example.com', '611987654'),
    ('María Gómez', 'maria@example.com', '622111222');

INSERT INTO productos (nombre, descripcion, precio, stock)
VALUES
    ('Portátil 15"', 'Portátil de 15 pulgadas con 16GB RAM', 899.99, 10),
    ('Ratón inalámbrico', 'Ratón óptico inalámbrico', 19.90, 50),
    ('Teclado mecánico', 'Teclado con switches azules', 59.95, 30);

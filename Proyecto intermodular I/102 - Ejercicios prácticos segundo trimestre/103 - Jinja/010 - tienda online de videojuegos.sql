CREATE DATABASE videojuegos;
USE videojuegos;
-- ============================================================
--   SCRIPT DE INSTALACIÓN PARA TIENDA DE VIDEOJUEGOS
-- ============================================================

-- ======================
-- 1. BORRADO PREVIO
-- ======================
DROP VIEW IF EXISTS vw_productos;
DROP VIEW IF EXISTS vw_clientes;
DROP VIEW IF EXISTS vw_pedidos;
DROP VIEW IF EXISTS vw_lineas_pedido;
DROP VIEW IF EXISTS vw_stock;
DROP VIEW IF EXISTS vw_categorias;

DROP TABLE IF EXISTS lineas_pedido;
DROP TABLE IF EXISTS pedidos;
DROP TABLE IF EXISTS stock;
DROP TABLE IF EXISTS productos;
DROP TABLE IF EXISTS categorias;
DROP TABLE IF EXISTS clientes;

-- ======================
-- 2. CREACIÓN DE TABLAS
-- ======================

-- Tabla de categorías
CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255)
);

-- Tabla de productos (videojuegos)
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    plataforma VARCHAR(50) NOT NULL,
    id_categoria INT NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

-- Tabla de clientes
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(50),
    direccion VARCHAR(255)
);

-- Tabla de pedidos
CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    fecha_pedido DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- Tabla de líneas de pedido
CREATE TABLE lineas_pedido (
    id_linea INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- Tabla de gestión de stock
CREATE TABLE stock (
    id_stock INT AUTO_INCREMENT PRIMARY KEY,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- ================================
-- 3. INSERTS DE EJEMPLO (ORDENADOS)
-- ================================

-- Categorías
INSERT INTO categorias (nombre, descripcion) VALUES
('Acción', 'Juegos con alta carga de acción'),
('Aventura', 'Juegos de exploración y narrativa'),
('RPG', 'Juegos de rol'),
('Deportes', 'Juegos deportivos');

-- Productos
INSERT INTO productos (nombre, descripcion, precio, plataforma, id_categoria) VALUES
('The Witcher 3', 'RPG de mundo abierto', 29.99, 'PC', 3),
('FIFA 25', 'Simulador de fútbol', 59.99, 'PS5', 4),
('God of War Ragnarok', 'Acción épica nórdica', 49.99, 'PS5', 1),
('Zelda: Breath of the Wild', 'Aventura en mundo abierto', 59.99, 'Nintendo Switch', 2);

-- Stock
INSERT INTO stock (id_producto, cantidad) VALUES
(1, 15),
(2, 40),
(3, 25),
(4, 30);

-- Clientes
INSERT INTO clientes (nombre, email, telefono, direccion) VALUES
('Juan Pérez', 'juan@example.com', '600123456', 'C/ Sol 12'),
('Ana Martínez', 'ana@example.com', '620987654', 'Av. Luna 45');

-- Pedidos
INSERT INTO pedidos (id_cliente, estado) VALUES
(1, 'Procesando'),
(2, 'Completado');

-- Líneas de pedido
INSERT INTO lineas_pedido (id_pedido, id_producto, cantidad, precio_unitario) VALUES
(1, 1, 1, 29.99),
(1, 3, 1, 49.99),
(2, 4, 2, 59.99);

-- ===================================
-- 4. CREACIÓN DE VISTAS DE CONSULTA
-- ===================================

CREATE VIEW vw_categorias AS
SELECT * FROM categorias;

CREATE VIEW vw_productos AS
SELECT p.*, c.nombre AS categoria
FROM productos p
JOIN categorias c ON p.id_categoria = c.id_categoria;

CREATE VIEW vw_stock AS
SELECT s.id_stock, p.nombre AS producto, s.cantidad
FROM stock s
JOIN productos p ON s.id_producto = p.id_producto;

CREATE VIEW vw_clientes AS
SELECT * FROM clientes;

CREATE VIEW vw_pedidos AS
SELECT pe.id_pedido, c.nombre AS cliente, pe.fecha_pedido, pe.estado
FROM pedidos pe
JOIN clientes c ON pe.id_cliente = c.id_cliente;

CREATE VIEW vw_lineas_pedido AS
SELECT lp.id_linea, pe.id_pedido, p.nombre AS producto, lp.cantidad, lp.precio_unitario
FROM lineas_pedido lp
JOIN productos p ON lp.id_producto = p.id_producto
JOIN pedidos pe ON lp.id_pedido = pe.id_pedido;

-- ============================================================
-- FIN DEL SCRIPT
-- ============================================================


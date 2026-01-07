CREATE DATABASE tienda26;

USE tienda26;

-- Creamos la base de datos y sus tablas
CREATE TABLE cliente (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  apellidos VARCHAR(255),
  email VARCHAR(255)
);

CREATE TABLE producto (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  precio VARCHAR(255)
);

-- Añadimos las restricciones FK para asegurar la integridad
CREATE TABLE pedido (
  id INT PRIMARY KEY,
  fecha VARCHAR(255),
  cliente_id INT,
  CONSTRAINT fk_pedido_1 FOREIGN KEY (cliente_id) REFERENCES cliente(id)
);

CREATE TABLE lineapedido (
  id INT PRIMARY KEY,
  pedido_id INT,
  producto_id INT,
  CONSTRAINT fk_lineapedido_1 FOREIGN KEY (pedido_id) REFERENCES pedido(id),
  CONSTRAINT fk_lineapedido_2 FOREIGN KEY (producto_id) REFERENCES producto(id)
);

-- 20 CLIENTES
INSERT INTO cliente (id, nombre, apellidos, email) VALUES
(1, 'Ana', 'García López', 'ana.garcia@email.com'),
(2, 'Luis', 'Martínez Pérez', 'luis.martinez@email.com'),
(3, 'María', 'Sánchez Ruiz', 'maria.sanchez@email.com'),
(4, 'Carlos', 'Fernández Gómez', 'carlos.fernandez@email.com'),
(5, 'Laura', 'López Díaz', 'laura.lopez@email.com'),
(6, 'Pedro', 'Jiménez Torres', 'pedro.jimenez@email.com'),
(7, 'Lucía', 'Moreno Castro', 'lucia.moreno@email.com'),
(8, 'Javier', 'Romero Vega', 'javier.romero@email.com'),
(9, 'Elena', 'Navarro Ortiz', 'elena.navarro@email.com'),
(10, 'David', 'Ruiz Molina', 'david.ruiz@email.com'),
(11, 'Sofía', 'Serrano Ramos', 'sofia.serrano@email.com'),
(12, 'Pablo', 'Gil Herrera', 'pablo.gil@email.com'),
(13, 'Marta', 'Iglesias Cano', 'marta.iglesias@email.com'),
(14, 'Raúl', 'Medina Cruz', 'raul.medina@email.com'),
(15, 'Paula', 'Vargas León', 'paula.vargas@email.com'),
(16, 'Alberto', 'Reyes Flores', 'alberto.reyes@email.com'),
(17, 'Natalia', 'Prieto Núñez', 'natalia.prieto@email.com'),
(18, 'Sergio', 'Campos Soto', 'sergio.campos@email.com'),
(19, 'Cristina', 'Fuentes Pardo', 'cristina.fuentes@email.com'),
(20, 'Iván', 'Rojas Blanco', 'ivan.rojas@email.com');

-- 20 PRODUCTOS
INSERT INTO producto (id, nombre, precio) VALUES
(1,'Portátil','800'),
(2,'Ratón','20'),
(3,'Teclado','30'),
(4,'Monitor','200'),
(5,'Impresora','150'),
(6,'Tablet','300'),
(7,'Móvil','600'),
(8,'Auriculares','50'),
(9,'Altavoces','70'),
(10,'Webcam','40'),
(11,'Disco SSD','120'),
(12,'Memoria USB','15'),
(13,'Router','90'),
(14,'Silla','180'),
(15,'Mesa','250'),
(16,'Cargador','25'),
(17,'Cable HDMI','10'),
(18,'Microfono','85'),
(19,'Smartwatch','220'),
(20,'Proyector','400');

-- 20 PEDIDOS (cada uno asociado a un cliente existente)
INSERT INTO pedido (id, fecha, cliente_id) VALUES
(1,'2026-01-01',1),
(2,'2026-01-02',2),
(3,'2026-01-03',3),
(4,'2026-01-04',4),
(5,'2026-01-05',5),
(6,'2026-01-06',6),
(7,'2026-01-07',7),
(8,'2026-01-08',8),
(9,'2026-01-09',9),
(10,'2026-01-10',10),
(11,'2026-01-11',11),
(12,'2026-01-12',12),
(13,'2026-01-13',13),
(14,'2026-01-14',14),
(15,'2026-01-15',15),
(16,'2026-01-16',16),
(17,'2026-01-17',17),
(18,'2026-01-18',18),
(19,'2026-01-19',19),
(20,'2026-01-20',20);

-- 20 LÍNEAS DE PEDIDO (una por pedido y producto)
INSERT INTO lineapedido (id, pedido_id, producto_id) VALUES
(1,1,1),
(2,2,2),
(3,3,3),
(4,4,4),
(5,5,5),
(6,6,6),
(7,7,7),
(8,8,8),
(9,9,9),
(10,10,10),
(11,11,11),
(12,12,12),
(13,13,13),
(14,14,14),
(15,15,15),
(16,16,16),
(17,17,17),
(18,18,18),
(19,19,19),
(20,20,20);

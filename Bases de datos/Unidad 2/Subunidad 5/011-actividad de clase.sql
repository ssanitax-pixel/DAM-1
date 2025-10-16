CREATE TABLE Productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion TEXT,
    precio DECIMAL(7,2),
    stock INT
);

ALTER TABLE Productos
    ADD CONSTRAINT chk_stock_no_negativo CHECK (stock >= 0),
    ADD CONSTRAINT chk_precio_valido CHECK (precio >= 0 AND precio <= 5000),
    ADD CONSTRAINT chk_nombre_min_longitud CHECK (CHAR_LENGTH(nombre) >= 5);

INSERT INTO Productos (nombre, descripcion, precio, stock) VALUES
('Silla Oficina', 'Silla ergonómica con soporte lumbar.', 129.99, 25),
('Mesa Escritorio', 'Mesa de madera con acabado natural.', 249.50, 10),
('Monitor 24"', 'Pantalla LED Full HD de 24 pulgadas.', 189.00, 15),
('Teclado Mecánico', 'Teclado con switches azules retroiluminado.', 89.90, 40),
('Ratón Inalámbrico', 'Mouse inalámbrico con batería recargable.', 39.99, 50),
('Auriculares Gamer', 'Auriculares con sonido envolvente y micrófono.', 79.95, 30),
('Alfombrilla RGB', 'Alfombrilla con iluminación LED multicolor.', 24.99, 60),
('Webcam HD', 'Cámara web 1080p para videollamadas.', 59.00, 20),
('Soporte Monitor', 'Soporte ajustable para monitor de escritorio.', 34.99, 18),
('Base Refrigerante', 'Base con ventiladores para portátil.', 45.00, 25),
('Cargador USB-C', 'Cargador rápido compatible con varios dispositivos.', 29.90, 100),
('Disco SSD 1TB', 'Disco de estado sólido de alta velocidad.', 129.00, 40),
('Hub USB 4 Puertos', 'Concentrador USB 3.0 con 4 salidas.', 22.99, 75),
('Lámpara LED', 'Lámpara de escritorio regulable con USB.', 49.99, 35),
('Altavoces Bluetooth', 'Par de altavoces estéreo con conexión inalámbrica.', 99.90, 20),
('Tablet 10"', 'Tablet con pantalla de 10 pulgadas y 64GB.', 299.00, 12),
('Cámara Deportiva', 'Cámara resistente al agua con 4K.', 199.90, 8),
('Mochila Laptop', 'Mochila con compartimento para portátil.', 59.95, 28),
('Router WiFi 6', 'Router de última generación para alta velocidad.', 159.00, 14),
('Impresora Láser', 'Impresora monocromo con conexión WiFi.', 149.00, 11);



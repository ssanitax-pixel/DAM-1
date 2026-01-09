sudo mysql -u root -p

SHOW DATABASES;

USE empresadam;

SHOW TABLES;

INSERT INTO pedidos (numerodepedido, cliente) 
VALUES ('001','Juan Doe');

SELECT * FROM pedidos;

INSERT INTO pedidos (numerodepedido, cliente, fecha, precio)
VALUES ('002', 'Maria Perez', '2025-11-01', 200.75);

SELECT * FROM pedidos;

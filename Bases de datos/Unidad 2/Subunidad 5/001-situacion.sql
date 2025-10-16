sudo mysql -u root -p

SHOW DATABASES;

USE empresadam;

SHOW TABLES;

DESCRIBE Clientes;

SELECT * FROM Clientes;

INSERT INTO Clientes VALUES(
	NULL,
	'12345678A',
	'nombre del cliente',
	'apellidos del cliente',
	'algo'
);
	
SELECT * FROM Clientes;

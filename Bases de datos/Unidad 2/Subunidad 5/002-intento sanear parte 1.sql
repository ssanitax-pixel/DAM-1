ALTER TABLE Clientes
	ADD CONSTRAINT comprobar_email
	CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$');

-- Eliminamos regustros que no cumplen	

DELETE FROM Clientes WHERE identificador = 4; -- En mi caso
DELETE FROM Clientes WHERE identificador = 5; -- En mi caso

SELECT * FROM Clientes;

-- Ahora sí, aplicamos

ALTER TABLE Clientes
	ADD CONSTRAINT comprobar_email
	CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$');
	
-- intento meter uno mal

INSERT INTO Clientes VALUES(
	NULL,
	'12345678A',
	'nombre del cliente',
	'apellidos del cliente',
	'algo'
);

 -- da error
ERROR 3819 (HY000): Check constraint 'comprobar_email' is violated.


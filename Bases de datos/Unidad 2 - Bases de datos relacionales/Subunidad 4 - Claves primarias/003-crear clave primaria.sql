ALTER TABLE Clientes
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;

ALTER = Altera
TABLE = tabla
Clientes = la tabla que quiero alterar
ADD = la operacion que quiero realizar
COLUMN = quiero añadir una columna
identificador = es el nombre de la columna (entero)
AUTO_INCREMENT = el numero ca a crecer automaticamente
PRIMARY KEY = clave primaria
FIRST = si hay varias, esta tiene la preferencia

DESCRIBE Clientes;

INSERT INTO Clientes
VALUES(
	NULL,
	'12345678A',
	'Ana',
	'Sánchez Suárez',
	'ana@ana.es'
);

SELECT * FROM Clientes;

INSERT INTO Clientes
VALUES(
	NULL,
	'12345679A',
	'Jose',
	'López García',
	'jose@jose.es'
);

SELECT * FROM Clientes;

INSERT INTO Clientes
VALUES(
	3,
	'12345679A',
	'Jose',
	'López García',
	'jose@jose.es'
);
ERROR 1062 (23000): Duplicate entry '3' for key 'Clientes.PRIMARY'

Ejemplo: 20260001 -- Fechas son interesantes para no repetir --


INSERT INTO Clientes
VALUES(
	NULL,
	'14745679A',
	'Alba',
	'Rayo García',
	'correoincorrecto'
);

SELECT * FROM Clientes;

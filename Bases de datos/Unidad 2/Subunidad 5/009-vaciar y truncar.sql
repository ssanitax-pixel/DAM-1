DELETE FROM Clientes; --lo borra todo, pero se acuerda de los que había

INSERT INTO Clientes VALUES(
	NULL,
	'12345678Z',
	'Jose Vicente',
	'Carratala',
	'info@info.es'
);

SELECT * FROM Clientes;

TRUNCATE TABLE Clientes; -- lo borra todo y empieza de nuevo

INSERT INTO Clientes VALUES(
	NULL,
	'12345678Z',
	'Jose Vicente',
	'Carratala',
	'info@info.es'
);

SELECT * FROM Clientes;

DROP TABLE Clientes; --mucho cuidado con esto porque borra la tabla

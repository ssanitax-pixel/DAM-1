INSERT INTO Clientes VALUES(
	NULL,
	'12345678A',
	'Jose Vicente',
	'Carratala',
	'info@info.es'
);

ERROR 3819 (HY000): Check constraint 'comprobar_dni_nie_letra' is violated.

INSERT INTO Clientes VALUES(
	NULL,
	'12345678Z',
	'Jose Vicente',
	'Carratala',
	'correoincorrecto'
);

ERROR 3819 (HY000): Check constraint 'comprobar_email' is violated.



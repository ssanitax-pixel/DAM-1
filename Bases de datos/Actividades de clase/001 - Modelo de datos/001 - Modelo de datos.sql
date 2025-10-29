CREATE TABLE Cliente(
	dni VARCHAR(9) PRIMARY KEY,
	nombre VARCHAR(50),
	apellidos VARCHAR(100),
	email VARCHAR(255) UNIQUE
);

SHOW TABLES;

INSERT INTO Cliente VALUES(
	'26525959J',
	'Juan',
	'Pérez',
	'juan@gmail.com'
);

INSERT INTO Cliente VALUES(
	'26525961S',
	'María',
	'López',
	'maria@gmail.com'
);

INSERT INTO Cliente VALUES(
	'26214990G',
	'Pedro',
	'López',
	'pedro@gmail.com'
);

SELECT * FROM Cliente;

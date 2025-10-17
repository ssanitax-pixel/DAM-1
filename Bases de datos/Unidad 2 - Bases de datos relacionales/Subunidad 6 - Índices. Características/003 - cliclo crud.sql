--create
INSERT INTO clientes VALUES(
	NULL,
	'Ana',
	'Sánchez Suárez',
	'ana@ana.es'
);
--read
SELECT * FROM clientes;
--update
UPDATE clientes
SET email = 'info@ana.es'
WHERE Identificador = 1;
--delete
DELETE FROM clientes
WHERE Identificador = 1;


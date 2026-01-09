mysqldump -u usuario -p nombre_basedatos > backup_nombre_basedatos.sql

sudo mysql -u root -p

USE empresarial;

INSERT INTO clientes (nombre, telefono, email, direccion)
VALUES ('Laura García', '620891718', 'laura.garcia@example.com', 'Calle Mayor 15, Valencia');

UPDATE clientes
SET nombre = 'Jose Vicente'
WHERE telefono = '620891718';

SELECT * FROM clientes;

DELETE FROM clientes
WHERE telefono = '620891718';

SELECT * FROM clientes WHERE telefono = '620891718';

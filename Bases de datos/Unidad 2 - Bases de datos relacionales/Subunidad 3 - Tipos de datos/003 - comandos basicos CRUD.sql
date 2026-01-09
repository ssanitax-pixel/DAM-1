-- Create
INSERT INTO clientes VALUES(
  '12345678A',
  'Ana',
  'Sánchez Suárez',
  'info@ana.com'
);

Query OK, 1 row affected (0,01 sec)

-- Read

SELECT * FROM clientes;

+-----------+--------------+-------------------+------------------+
| dni       | nombre       | apellidos         | email            |
+-----------+--------------+-------------------+------------------+
| 12345678A | Ana          | Sánchez Suárez    | info@ana         |
+-----------+--------------+-------------------+------------------+
1 row in set (0,00 sec)

-- Update

UPDATE clientes
SET dni = '11111111A'
WHERE nombre = 'Ana';

SELECT * FROM clientes;

UPDATE clientes
SET apellidos = 'Garcia Lopez'
WHERE nombre = 'Ana';

-- Delete

DELETE FROM clientes
WHERE dni = '11111111A';




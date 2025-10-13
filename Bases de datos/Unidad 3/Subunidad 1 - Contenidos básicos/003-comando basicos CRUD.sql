-- Create
INSERT INTO Clientes VALUES(
	'26525959J',
	'Ana',
	'Sánchez Suárez',
	'ssanitax@gmail.com'
);

Query OK, 1 row affected (0,02 sec)

-- Read

SELECT * FROM Clientes;

+-----------+--------+------------------+--------------------+
| dni       | nombre | apellidos        | email              |
+-----------+--------+------------------+--------------------+
| 26525959J | Ana    | Sánchez Suárez   | ssanitax@gmail.com |
+-----------+--------+------------------+--------------------+
1 row in set (0,00 sec)

-- Update

UPDATE Clientes
SET dni = '11111111A'
WHERE nombre = 'Ana';

Query OK, 1 row affected (0,01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

SELECT * FROM Clientes;

+-----------+--------+------------------+--------------------+
| dni       | nombre | apellidos        | email              |
+-----------+--------+------------------+--------------------+
| 11111111A | Ana    | Sánchez Suárez   | ssanitax@gmail.com |
+-----------+--------+------------------+--------------------+
1 row in set (0,00 sec)

UPDATE Clientes
SET apellidos = 'García Garrido'
WHERE nombre = 'Ana';

SELECT * FROM Clientes;

+-----------+--------+-----------------+--------------------+
| dni       | nombre | apellidos       | email              |
+-----------+--------+-----------------+--------------------+
| 11111111A | Ana    | García Garrido  | ssanitax@gmail.com |
+-----------+--------+-----------------+--------------------+
1 row in set (0,00 sec)

-- Delete

DELETE FROM Clientes
WHERE dni = '11111111A';

Query OK, 1 row affected (0,00 sec)

SELECT * FROM Clientes;

Empty set (0,00 sec)

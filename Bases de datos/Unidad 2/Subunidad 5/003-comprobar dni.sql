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

-- asegurar dni

ALTER TABLE Clientes
  ADD CONSTRAINT comprobar_dni_nie_letra
  CHECK (
    (
      -- DNI: 8 dígitos + letra
      dni REGEXP '^[0-9]{8}[A-Za-z]$'
      AND
      UPPER(SUBSTRING(dni, 9, 1)) =
      SUBSTRING('TRWAGMYFPDXBNJZSQVHLCKE',
                (CAST(SUBSTRING(dni, 1, 8) AS UNSIGNED) MOD 23) + 1,
                1)
    )
    OR
    (
      -- NIE: X/Y/Z + 7 dígitos + letra
      dni REGEXP '^[XYZxyz][0-9]{7}[A-Za-z]$'
      AND
      UPPER(SUBSTRING(dni, 9, 1)) =
      SUBSTRING('TRWAGMYFPDXBNJZSQVHLCKE',
                (
                  CAST(CONCAT(
                        CASE UPPER(SUBSTRING(dni, 1, 1))
                          WHEN 'X' THEN '0'
                          WHEN 'Y' THEN '1'
                          WHEN 'Z' THEN '2'
                        END,
                        SUBSTRING(dni, 2, 7)
                  ) AS UNSIGNED) MOD 23
                ) + 1,
                1)
    )
  );

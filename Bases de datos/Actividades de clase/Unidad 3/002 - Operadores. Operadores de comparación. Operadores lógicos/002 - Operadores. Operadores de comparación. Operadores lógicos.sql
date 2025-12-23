SELECT nombre, apellidos, edad + 500 FROM clientes;
SELECT nombre, apellidos, edad - 500 FROM clientes;
SELECT nombre, apellidos, edad * 500 FROM clientes;
SELECT nombre, apellidos, edad / 500 FROM clientes;

SELECT 
    nombre,
    apellidos,
    edad,
    edad < 30 AS 'Menor de 30 años',
    edad >= 30 && edad < 40 AS 'Entre 30 y 40 años',
    edad > 40 AS 'Mayor de 40 años'
FROM clientes;

SELECT 
    nombre,
    apellidos,
    edad,
    edad < 30 AS '¿Es menor de 30 años?'
FROM clientes;

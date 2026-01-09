SELECT 
    nombre, 
    apellidos 
FROM clientes;

SELECT 
    nombre AS 'Nombre del cliente', 
    apellidos AS 'Apellidos del cliente', 
    edad AS 'Edad del cliente' 
FROM clientes 
WHERE edad > 18;

SELECT 
    nombre, 
    apellidos, 
    edad 
FROM clientes 
ORDER BY edad DESC;

SELECT 
    nombre AS 'Nombre del cliente', 
    apellidos AS 'Apellidos del cliente', 
    edad AS 'Edad del cliente' 
FROM clientes 
ORDER BY edad DESC, apellidos ASC;

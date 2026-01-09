-- sudo mysql -u root -p

USE clientes;

SELECT
	ROUND(AVG(edad))
FROM clientes; -- edad promedio redondeada

SELECT
	FLOOR(AVG(edad))
FROM clientes; -- como la anterior pero redondea hacia abajo

SELECT
	CEIL(AVG(edad))
FROM clientes; -- esta redondea hacia arriba

sudo mysql -u root -p

USE clientes;

SELECT ROUND(AVG(edad)) AS 'Media Redondeada' FROM clientes;

SELECT FLOOR(AVG(edad)) AS 'Media Suelo' FROM clientes;

SELECT CEIL(AVG(edad)) AS 'Media Techo' FROM clientes;

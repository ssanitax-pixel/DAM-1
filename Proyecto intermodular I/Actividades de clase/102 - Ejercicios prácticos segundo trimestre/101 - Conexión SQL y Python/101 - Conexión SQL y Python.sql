-- sudo mysql -u root -p

CREATE DATABASE clientes;

USE clientes;

CREATE TABLE clientes(
	nombre VARCHAR(255),
	apellidos VARCHAR(255),
	edad INT
);

INSERT INTO clientes VALUES ("Ana","Sánchez",25);
INSERT INTO clientes VALUES ("Fátima","Quiñones",20);

CREATE USER 
'clientes'@'localhost' 
IDENTIFIED  BY 'Clientes123$';

GRANT USAGE ON *.* TO 'clientes'@'localhost';

ALTER USER 'clientes'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON clientes.* 
TO 'clientes'@'localhost';

FLUSH PRIVILEGES;

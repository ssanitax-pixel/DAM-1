sudo mysql -u root -p

CREATE DATABASE ejemploclaves;

USE ejemploclaves;

-- crear tablas personas
CREATE TABLE Personas (
	nombre VARCHAR(50),
	apellidos VARCHAR(255)
);

-- añado identificador
ALTER TABLE Personas
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;
	
SHOW TABLES;

-- crear tablas emails
CREATE TABLE Emails (
	direccion VARCHAR(50),
	persona VARCHAR(255)
);

-- añado identificador
ALTER TABLE Personas
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;
	
SHOW TABLES;

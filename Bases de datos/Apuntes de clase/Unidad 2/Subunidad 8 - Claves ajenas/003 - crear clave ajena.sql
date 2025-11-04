-- paso 1: cambiar tipo de columna
ALTER TABLE Emails
MODIFY COLUMN persona INT;

-- paso 2: crear la foreign key
ALTER TABLE Emails
ADD CONSTRAINT fk_emails_personas
FOREIGN KEY (persona) REFERENCES Personas(identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE Emails -- Altera la tabla de emails
ADD CONSTRAINT fk_Emails_Personas -- Crea una restriccion con este nombre
FOREIGN KEY (persona)  --Creamos una clave hacia persona
REFERENCES Personas(identificador) -- que refetrencia
ON DELETE CASCADE
ON UPDATE CASCADE;

SHOW TABLES;

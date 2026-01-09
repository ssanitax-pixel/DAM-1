sudo mysql u- root -p

CREATE DATABASE ejemploclaves;

SHOW DATABASES;

USE ejemploclaves;

CREATE TABLE personas (
	nombre VARCHAR(50),
	apellidos VARCHAR(255)
);

SHOW TABLES;

ALTER TABLE personas
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;

DESCRIBE personas;

CREATE TABLE emails (
    direccion VARCHAR(50),
    persona VARCHAR(255)
);

SHOW TABLES;

ALTER TABLE emails
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;

DESCRIBE emails;

INSERT INTO personas VALUES(
	NULL,
	'María',
	'Sánchez Suárez'
);

SELECT * FROM personas;

ALTER TABLE emails
MODIFY COLUMN persona INT;

DESCRIBE emails;

ALTER TABLE emails
ADD CONSTRAINT fk_emails_personas
FOREIGN KEY (persona) REFERENCES personas(identificador);

DESCRIBE emails;

INSERT INTO emails VALUES(
  NULL,
  'info@maria.com',
  1
);

INSERT INTO emails VALUES(
  NULL,
  'mariasanchez@gmail.com',
  1
);

SELECT * FROM emails;

SELECT * FROM emails
LEFT JOIN personas
ON emails.persona = personas.identificador;

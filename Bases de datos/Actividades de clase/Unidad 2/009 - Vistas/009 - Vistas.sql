sudo mysql -u root -p

USE ejemploclaves;

CREATE VIEW personas_correos AS
SELECT
	personas.identificador,
	emails.direccion,
	personas.nombre,
	personas.apellidos
FROM emails
LEFT JOIN personas
ON emails.persona = personas.Identificador;

SHOW FULL TABLES WHERE Table_type = 'VIEW';

SELECT * FROM personas_correos;

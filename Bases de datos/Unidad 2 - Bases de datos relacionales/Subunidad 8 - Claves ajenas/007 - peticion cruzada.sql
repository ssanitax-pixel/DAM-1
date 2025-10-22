SELECT * FROM Emails
LEFT JOIN Personas
ON Emails.Persona = Personas.Identificador;


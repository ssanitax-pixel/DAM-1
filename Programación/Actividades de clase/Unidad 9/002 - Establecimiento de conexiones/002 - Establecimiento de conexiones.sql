mysql -u root -p

CREATE DATABASE empresadam;

USE empresadam;

CREATE TABLE restaurantes (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ubicacion VARCHAR(150),
    calificacion INT
);

DESCRIBE restaurantes;

INSERT INTO restaurantes (nombre, ubicacion, calificacion) VALUES
('La Bella Italia', 'Calle Roma 12', 5),
('El Rincón del Sazón', 'Avenida Central 45', 4),
('Café de la Esquina', 'Plaza Mayor 3', 3);

SELECT * FROM restaurantes;


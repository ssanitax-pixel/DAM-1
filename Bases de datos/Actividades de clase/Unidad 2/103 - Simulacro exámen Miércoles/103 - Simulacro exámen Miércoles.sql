sudo mysql -u root -p

CREATE DATABASE portafolio;

SHOW DATABASES;

USE portafolio;

CREATE TABLE Pieza (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    titulop VARCHAR(100),
    descripcionp TEXT,
    imagen VARCHAR(100),
    url VARCHAR(255),
    id_categoria INT
);

DESCRIBE Pieza;

CREATE TABLE Categoria (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    tituloc VARCHAR(100),
    descripcionc TEXT
);

DESCRIBE Categoria;

ALTER TABLE Pieza
ADD CONSTRAINT Piezas_a_Categorías
FOREIGN KEY (id_categoria) REFERENCES Categoria(Identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;

INSERT INTO Categoria VALUES (
    NULL,
    'Pintura',
    'Obras pictóricas realizadas con diversas técnicas como óleo, acrílico o acuarela, que representan escenas, retratos o paisajes.'
);

INSERT INTO Categoria VALUES (
    NULL,
    'Escultura',
    'Obras tridimensionales elaboradas en materiales como bronce, mármol o madera, que expresan formas humanas, animales o abstractas.'
);

SELECT * FROM Categoria;

INSERT INTO Pieza VALUES (
    NULL,
    'La mañana sobre el río', 
    'Óleo sobre lienzo que representa un amanecer en un paisaje fluvial. Destaca por el uso de luces suaves y reflejos en el agua.', 
    'la_manana_sobre_el_rio.jpg', 
    'https://galeriaarte.com/la-manana-sobre-el-rio', 
    1
);    

INSERT INTO Pieza VALUES (
    NULL,
    'Retrato de mujer con sombrero', 
    'Cuadro al óleo de mediados del siglo XX.',
    'retrato_mujer_sombrero.jpg', 
    'https://galeriaarte.com/retrato-mujer-sombrero', 
    1);

INSERT INTO Pieza VALUES (
    NULL,
    'Estatua del pensador moderno', 
    'Escultura en bronce que representa a una figura humana en actitud reflexiva. Inspirada en el pensamiento contemporáneo y la introspección.', 
    'estatua_pensador_moderno.jpg', 
    'https://galeriaarte.com/estatua-pensador-moderno', 
    2);
    
SELECT * FROM Pieza;

SELECT
Pieza.titulop,Pieza.descripcionp,Pieza.imagen,Pieza.url,
Categoria.tituloc,Categoria.descripcionc
FROM Pieza
LEFT JOIN Categoria
ON Pieza.id_categoria = Categoria.Identificador;

CREATE VIEW vista_categorias AS
SELECT
Pieza.titulop,Pieza.descripcionp,Pieza.imagen,Pieza.url,
Categoria.tituloc,Categoria.descripcionc
FROM Categoria
LEFT JOIN Pieza
ON Pieza.id_categoria = Categoria.Identificador;

SELECT * FROM vista_categorias;

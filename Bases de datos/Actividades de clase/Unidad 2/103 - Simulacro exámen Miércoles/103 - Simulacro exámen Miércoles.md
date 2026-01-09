SQL (Structured Query Language) es un lenguaje de programación utilizado para crear, administrar y manipular bases de datos relacionales. Su objetivo principal es permitir la organización estructurada de la información mediante tablas relacionadas entre sí.
En este ejercicio se desarrolla una base de datos llamada `portafolio`, compuesta por dos entidades: `Pieza` y `Categoria`, unidas por una `clave foránea (FK)`. Esta relación permite clasificar cada pieza artística dentro de una categoría específica (como pintura o escultura).
A través de consultas `JOIN`, se pueden combinar los datos de ambas tablas para mostrar información completa, y con una `vista (VIEW)` se crea una representación virtual que facilita el acceso y consulta de esos datos de forma más práctica.

---

Vamos a crear una base de datos llamada portafolio, para ello, primero abriremos el terminal y entraremos en MySQL.

```
sudo mysql -u root -p
```

Creamos la base de datos con el nombre que nos piden.

```
CREATE DATABASE portafolio;
```

Miramos que se ha creado correctamente.

```
SHOW DATABASES;
```

Ahora nos metemos en la base de datos recién creada.

```
USE portafolio;
```

Hay que crear dos entidades, Pieza (Identificador PK, titulo, descripción, imagen, url, id_categoria FK), y Categoria (Identificador PK, titulo, descripción).

Vamos paso a paso, primero creamos la entidad `Pieza`.

```
CREATE TABLE Pieza (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    titulop VARCHAR(100),
    descripcionp TEXT,
    imagen VARCHAR(100),
    url VARCHAR(255),
    id_categoria INT
);
```

Nos aseguramos que se ha creado correctamente.

```
DESCRIBE Pieza;
```

Procedemos a crear la tabla de `Categoria`.

```
CREATE TABLE Categoria (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    tituloc VARCHAR(100),
    descripcionc TEXT
);
```

Nos aseguramos que se ha insertado correctamente.

```
DESCRIBE Categoria;
```

Creamos la `clave foránea`.

```
ALTER TABLE Pieza
ADD CONSTRAINT Piezas_a_Categorías
FOREIGN KEY (id_categoria) REFERENCES Categoria(Identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;
```

Ahora insertamos tres entradas en `Pieza` y dos en `Categoria`.

Empezamos con `Categoria`.

```
INSERT INTO Categoria VALUES (
    NULL,
    'Pintura',
    'Obras pictóricas realizadas con diversas técnicas como óleo, acrílico o acuarela, que representan escenas, retratos o paisajes.'
);
```

```
INSERT INTO Categoria VALUES (
    NULL,
    'Escultura',
    'Obras tridimensionales elaboradas en materiales como bronce, mármol o madera, que expresan formas humanas, animales o abstractas.'
);
```

Revisamos que se han insertado correctamente las categorías.

```
SELECT * FROM Categoria;
```

Nos vamos a crear ahora las piezas.

```
INSERT INTO Pieza VALUES (
    NULL,
    'La mañana sobre el río', 
    'Óleo sobre lienzo que representa un amanecer en un paisaje fluvial. Destaca por el uso de luces suaves y reflejos en el agua.', 
    'la_manana_sobre_el_rio.jpg', 
    'https://galeriaarte.com/la-manana-sobre-el-rio', 
    1
);    
```

```
INSERT INTO Pieza VALUES (
    NULL,
    'Retrato de mujer con sombrero', 
    'Cuadro al óleo de mediados del siglo XX.',
    'retrato_mujer_sombrero.jpg', 
    'https://galeriaarte.com/retrato-mujer-sombrero', 
    1);
```

```
INSERT INTO Pieza VALUES (
    NULL,
    'Estatua del pensador moderno', 
    'Escultura en bronce que representa a una figura humana en actitud reflexiva. Inspirada en el pensamiento contemporáneo y la introspección.', 
    'estatua_pensador_moderno.jpg', 
    'https://galeriaarte.com/estatua-pensador-moderno', 
    2);
```

Nos aseguramos que las piezas se han implementado.

```
SELECT * FROM Pieza;
```

Realizamos la petición cruzada.

```
SELECT
Pieza.titulop,Pieza.descripcionp,Pieza.imagen,Pieza.url,
Categoria.tituloc,Categoria.descripcionc
FROM Pieza
LEFT JOIN Categoria
ON Pieza.id_categoria = Categoria.Identificador;
```
```
+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+--------------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------+
| titulop                       | descripcionp                                                                                                                                 | imagen                       | url                                              | tituloc   | descripcionc                                                                                                                        |
+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+--------------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------+
| Retrato de mujer con sombrero | Cuadro al óleo de mediados del siglo XX.                                                                                                     | retrato_mujer_sombrero.jpg   | https://galeriaarte.com/retrato-mujer-sombrero   | Pintura   | Obras pictóricas realizadas con diversas técnicas como óleo, acrílico o acuarela, que representan escenas, retratos o paisajes.     |
| Estatua del pensador moderno  | Escultura en bronce que representa a una figura humana en actitud reflexiva. Inspirada en el pensamiento contemporáneo y la introspección.   | estatua_pensador_moderno.jpg | https://galeriaarte.com/estatua-pensador-moderno | Escultura | Obras tridimensionales elaboradas en materiales como bronce, mármol o madera, que expresan formas humanas, animales o abstractas.   |
| La mañana sobre el río        | Óleo sobre lienzo que representa un amanecer en un paisaje fluvial. Destaca por el uso de luces suaves y reflejos en el agua.                | la_manana_sobre_el_rio.jpg   | https://galeriaarte.com/la-manana-sobre-el-rio   | Pintura   | Obras pictóricas realizadas con diversas técnicas como óleo, acrílico o acuarela, que representan escenas, retratos o paisajes.     |
+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+--------------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------+
```

Por último creamos una vista.

```
CREATE VIEW vista_categorias AS
SELECT
Pieza.titulop,Pieza.descripcionp,Pieza.imagen,Pieza.url,
Categoria.tituloc,Categoria.descripcionc
FROM Categoria
LEFT JOIN Pieza
ON Pieza.id_categoria = Categoria.Identificador;
```

Ahora se comportará como una tabla.

```
SELECT * FROM vista_categorias;
```
```
+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+--------------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------+
| titulop                       | descripcionp                                                                                                                                 | imagen                       | url                                              | tituloc   | descripcionc                                                                                                                        |
+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+--------------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------+
| Retrato de mujer con sombrero | Cuadro al óleo de mediados del siglo XX.                                                                                                     | retrato_mujer_sombrero.jpg   | https://galeriaarte.com/retrato-mujer-sombrero   | Pintura   | Obras pictóricas realizadas con diversas técnicas como óleo, acrílico o acuarela, que representan escenas, retratos o paisajes.     |
| La mañana sobre el río        | Óleo sobre lienzo que representa un amanecer en un paisaje fluvial. Destaca por el uso de luces suaves y reflejos en el agua.                | la_manana_sobre_el_rio.jpg   | https://galeriaarte.com/la-manana-sobre-el-rio   | Pintura   | Obras pictóricas realizadas con diversas técnicas como óleo, acrílico o acuarela, que representan escenas, retratos o paisajes.     |
| Estatua del pensador moderno  | Escultura en bronce que representa a una figura humana en actitud reflexiva. Inspirada en el pensamiento contemporáneo y la introspección.   | estatua_pensador_moderno.jpg | https://galeriaarte.com/estatua-pensador-moderno | Escultura | Obras tridimensionales elaboradas en materiales como bronce, mármol o madera, que expresan formas humanas, animales o abstractas.   |
+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+--------------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------+
```

---

Durante el proceso se construyó la base de datos, se definieron las tablas con sus claves primarias y foráneas, se insertaron registros de ejemplo y se comprobó la relación entre las entidades mediante un `LEFT JOIN`. Finalmente, se generó una vista que reúne la información de ambas tablas como si fuera una sola.
Este procedimiento demuestra cómo SQL permite estructurar, relacionar y visualizar datos de manera eficiente, sentando las bases para el desarrollo de la parte visible y administrativa del portafolio web.

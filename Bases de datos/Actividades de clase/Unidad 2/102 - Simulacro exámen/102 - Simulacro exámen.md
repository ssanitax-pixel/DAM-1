Las bases de datos relacionales permiten organizar y gestionar la información de manera estructurada mediante tablas que se relacionan entre sí. En MySQL, este modelo facilita el almacenamiento eficiente de datos y su posterior consulta mediante el uso de claves primarias, foráneas y vistas, elementos fundamentales para garantizar la integridad y coherencia de la información.

---

Inicio sesión en MySQL.
```
sudo mysql -u root -p
```

Creo la base de datos.
```
CREATE DATABASE blog2;
```

Nos aseguramos de que se ha creado:
```
SHOW DATABASES;
```

Nos tenemos que meter en la base de datos.
```
USE blog2;
```

Creamos una tabla:
O bien sin identificador:
```
CREATE TABLE autores (
    Identificador INT(10),
    nombre VARCHAR(100),
    apellidos VARCHAR(100),
    email VARCHAR(100)
);
```
O con:
```
CREATE TABLE autores (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellidos VARCHAR(100),
    email VARCHAR(100)
);
```

Miramos que hemos creado bien.
```
SHOW TABLES;
```

Quiero tirar la columna Identificador para crearla bien.
```
ALTER TABLE autores
DROP Identificador;
```

Ahora creo la columna.
```
ALTER TABLE autores
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;
```

Vamos a ver qué es lo que se ha hecho.
```
DESCRIBE autores;
```

Ahora quiero insertar un autor de prueba.
```
INSERT INTO autores VALUES(
    NULL,
    'Ana',
    'Sánchez',
    'ana@gmail.com'
);
```

Me aseguro.
```
SELECT * FROM autores;
```

Creo la tabla de entradas.
```
CREATE TABLE entradas (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    fecha VARCHAR(100),
    imagen VARCHAR(100),
    id_autor VARCHAR(100),
    contenido TEXT
);
```

Miramos la existencia de la tabla.
```
SHOW TABLES;
```

Miramos que se haya implementado todo.
```
DESCRIBE entradas;
```

Creamos una foreign key.
```
ALTER TABLE entradas
ADD CONSTRAINT autores_a_entradas
FOREIGN KEY (id_autor) REFERENCES autores(Identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;
```
Da fallo.

Cambiamos tipo de datos.
```
ALTER TABLE entradas
MODIFY COLUMN id_autor INT;
```

Volvemos a insertar.
```
ALTER TABLE entradas
ADD CONSTRAINT autores_a_entradas
FOREIGN KEY (id_autor) REFERENCES autores(Identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;
```

Insertamos una entrada.
```
INSERT INTO entradas (titulo, fecha, imagen, id_autor, contenido) VALUES (
    'Titulo de la primera entrada', 
    '2025-11-03', 
    'imagen.jpg', 
    1, 
    'Este es el contenido de la primera entrada'
);
```
```
SELECT * FROM entradas;
```

Petición cruzada.
```
SELECT
entradas.titulo,entradas.fecha,entradas.imagen,entradas.contenido
autores.nombre,autores.apellidos
FROM entradas
LEFT JOIN autores
ON entradas.id_autor = autores.Identificador;
```

Por último creamos una vista.
```
CREATE VIEW vista_entradas AS
SELECT
entradas.titulo,entradas.fecha,entradas.imagen,entradas.contenido
autores.nombre,autores.apellidos
FROM entradas
LEFT JOIN autores
ON entradas.id_autor = autores.Identificador;
```

Ahora se comportará como una tabla.
```
SELECT * FROM vista_entradas;
```

---

En este ejercicio, he aprendido a crear una base de datos para un blog, definir las tablas con sus claves primarias y foráneas, realizar consultas cruzadas y generar vistas. Esta práctica me permitió comprender mejor cómo trabajar con bases de datos relacionales en MySQL.


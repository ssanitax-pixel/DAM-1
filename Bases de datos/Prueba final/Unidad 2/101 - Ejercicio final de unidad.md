# Introducción

Este ejercicio consiste en crear una base de datos para gestionar una biblioteca usando MySQL. Se incluyen tablas para **autores**, **libros**, **socios** y **préstamos**, con claves primarias y foráneas, y restricciones como `UNIQUE`, `CHECK` y **índices** para asegurar la integridad de los datos y mejorar el rendimiento de las consultas.

---

1. **Crear BD y usarla:**

Empezamos abriendo Terminal y entrando a MySQL.

```
sudo mysql -u root -p
```

Creamos la base de datos que nos pide el ejercicio que en este caso se llamará `biblioteca25`

```
CREATE DATABASE biblioteca25;
```

Usamos la acción `USE` para seleccionar la base de datos.

```
USE biblioteca25;
```

Y verificamos que estamos dentro.

```
SELECT DATABASE();
```


2. **Crear tabla `autores`:**

Ahora crearemos la tabla maestra de `autores`, de la siguiente forma:

```
CREATE TABLE autores (
  nombre VARCHAR(100) NOT NULL,
  pais VARCHAR(80) NULL
);
```

Verificamos que está todo correctamente implementado.

```
DESCRIBE autores;
```

Evidencia: 

```
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| id            | int          | NO   | PRI | NULL    | auto_increment |
| nombre        | varchar(100) | NO   |     | NULL    |                |
| pais          | varchar(80)  | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
3 rows in set (0,01 sec)
```


3. **Crear tabla `libros` con UNIQUE, CHECK, y FK:**

Ahora crearemos la tabla hija de `libros`, de la siguiente forma, con todos los requisitos requeridos.

```
CREATE TABLE libros (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(200) NOT NULL,
  isbn VARCHAR(20) NOT NULL UNIQUE,
  precio DECIMAL(8,2) NOT NULL CHECK (precio >= 0),
  autor_id INT NOT NULL,
  FOREIGN KEY (autor_id) REFERENCES autores(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);
```

Ahora creamos un índice sobre `título` que busque según el título.

```
CREATE INDEX idx_titulo ON libros(titulo);
```

Verificación:

Verificamos que está todo correctamente implementado.

```
DESCRIBE libros;
```
```
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| titulo   | varchar(200) | NO   | MUL | NULL    |                |
| isbn     | varchar(20)  | NO   | UNI | NULL    |                |
| precio   | decimal(8,2) | NO   |     | NULL    |                |
| autor_id | int          | NO   | MUL | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
5 rows in set (0,01 sec)

```

Para ver los índices que existen en la tabla `libros`, incluidos los índices únicos, como el que se aplica sobre la columna `isbn`, y el índice que hemos creado sobre la columna `titulo`, usamos lo siguiente.

```
SHOW INDEX FROM libros;
```

```
+--------+------------+------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| Table  | Non_unique | Key_name   | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment | Visible | Expression |
+--------+------------+------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| libros |          0 | PRIMARY    |            1 | id          | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| libros |          0 | isbn       |            1 | isbn        | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| libros |          1 | autor_id   |            1 | autor_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| libros |          1 | idx_titulo |            1 | titulo      | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
+--------+------------+------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
4 rows in set (0,01 sec)

```


4. **Crear tabla `socios` con `UNIQUE` y `CHECK` de email:**

```
CREATE TABLE socios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    fecha_alta TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);
```

Evidencia: 

Un insert inválido se vería así.

```
INSERT INTO socios (nombre, email) 
    -> VALUES ('Juan Pérez', 'juanexamplecom');
ERROR 3819 (HY000): Check constraint 'socios_chk_1' is violated.
```

Los válidos.

```
INSERT INTO socios (nombre, email)
VALUES ('Juan Pérez', 'juan.perez@example.com');

INSERT INTO socios (nombre, email)
VALUES ('María Gómez', 'maria.gomez@empresa.org');
```

Miramos los socios que hay.

```
DESCRIBE socios;
```

```
+------------+--------------+------+-----+-------------------+-------------------+
| Field      | Type         | Null | Key | Default           | Extra             |
+------------+--------------+------+-----+-------------------+-------------------+
| id         | int          | NO   | PRI | NULL              | auto_increment    |
| nombre     | varchar(100) | NO   |     | NULL              |                   |
| email      | varchar(120) | NO   | UNI | NULL              |                   |
| fecha_alta | timestamp    | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+------------+--------------+------+-----+-------------------+-------------------+
4 rows in set (0,00 sec)
```


5. **Crear tabla `prestamos` con FKs y `CHECK` de fechas:**

El objetivo ahora es crear la tabla relacion N:M (socio libro) y coherencia temporal.

Primero creamos la tabla.

```
CREATE TABLE prestamos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    socio_id INT NOT NULL,
    libro_id INT NOT NULL,
    fecha_prestamo TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_devolucion DATE NULL,
    CHECK (fecha_devolucion IS NULL OR fecha_devolucion >= fecha_prestamo),
    FOREIGN KEY (socio_id) REFERENCES socios(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (libro_id) REFERENCES libros(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);
```

Creamos el índice compuesto.

```
CREATE INDEX idx_socio_libro ON prestamos(socio_id, libro_id);
```

Verificación de que hemos hecho todo correctamente.

```
SHOW INDEX FROM prestamos;
```

```
+-----------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| Table     | Non_unique | Key_name        | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment | Visible | Expression |
+-----------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| prestamos |          0 | PRIMARY         |            1 | id          | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| prestamos |          1 | libro_id        |            1 | libro_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| prestamos |          1 | idx_socio_libro |            1 | socio_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| prestamos |          1 | idx_socio_libro |            2 | libro_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
+-----------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
4 rows in set (0,02 sec)
```

Vamos a probar dos inserciones, en las que primero tendremos que insertar `socios`.

```
INSERT INTO socios (nombre, email)
VALUES 
('Juan Pérez', 'juan.perez@example.com'),
('María Gómez', 'maria.gomez@empresa.org');
```

Ahora insertamos libros.

```
INSERT INTO libros (titulo, isbn, precio, autor_id)
VALUES 
('El Gran Libro', '1234567890', 19.99, 1),
('La Aventura de Hoy', '0987654321', 15.50, 2); 
```

Evidencia:

Vemos si está bien hecha la esctructura de la tabla de `prestamos`.

```
DESCRIBE prestamos;
```

```
+------------------+-----------+------+-----+-------------------+-------------------+
| Field            | Type      | Null | Key | Default           | Extra             |
+------------------+-----------+------+-----+-------------------+-------------------+
| id               | int       | NO   | PRI | NULL              | auto_increment    |
| socio_id         | int       | NO   | MUL | NULL              |                   |
| libro_id         | int       | NO   | MUL | NULL              |                   |
| fecha_prestamo   | timestamp | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| fecha_devolucion | date      | YES  |     | NULL              |                   |
+------------------+-----------+------+-----+-------------------+-------------------+
```

Mostramos la información sobre los índices asociados con la tabla prestamos.

```
+----------+--------+------+------------+---------+---------------+---------+------------+
| Table     | Non_unique | Key_name        | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment | Visible | Expression |
+-----------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| prestamos |          0 | PRIMARY         |            1 | id          | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| prestamos |          1 | libro_id        |            1 | libro_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| prestamos |          1 | idx_socio_libro |            1 | socio_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| prestamos |          1 | idx_socio_libro |            2 | libro_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
+-----------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
4 rows in set (0,00 sec)
```

6. **Insertar datos mínimos coherentes:**

Insertamos 3 autores más a la tabla.

```
INSERT INTO autores (nombre, pais)
VALUES 
    ('Gabriel García Márquez', 'Colombia'),
    ('J.K. Rowling', 'Reino Unido'),
    ('George Orwell', 'Reino Unido');
```

Insertamos 3 libros más cada uno referenciado a un `autor_id` existente.

```
INSERT INTO libros (titulo, isbn, precio, autor_id)
VALUES 
    ('Cien años de soledad', '978-3-16-148410-0', 19.99, 3),
    ('Harry Potter y la piedra filosofal', '978-0-7475-3269-9', 15.99, 4),
    ('1984', '978-0-452-28423-4', 12.99, 5);
```

Insertamos dos socios.

```
INSERT INTO socios (nombre, email)
VALUES 
    ('Ana Sánchez', 'ana.sanchez@example.com'),
    ('Alfredo Martínez', 'alfredo.martinez@example.com');
```

Ahora insertaremos dos préstamos, uno activo y otro ya devuelto.

```
INSERT INTO prestamos (socio_id, libro_id, fecha_prestamo)
VALUES (5, 14, CURRENT_TIMESTAMP);

INSERT INTO prestamos (socio_id, libro_id, fecha_prestamo, fecha_devolucion)
VALUES (6, 15, '2023-10-01', '2023-10-10');
```

Verificación:


De la tabla de autores:
```
SELECT * FROM autores;
```

```
+----+--------------------------+-----------------+
| id | nombre                   | pais            |
+----+--------------------------+-----------------+
|  1 | Autor de prueba          | País de prueba  |
|  2 | Paco de Lucía            | España          |
|  3 | Gabriel García Márquez   | Colombia        |
|  4 | J.K. Rowling             | Reino Unido     |
|  5 | George Orwell            | Reino Unido     |
+----+--------------------------+-----------------+
```

De la tabla de libros:

```
SELECT * FROM libros;
```

```
+----+------------------------------------+-------------------+--------+----------+
| id | titulo                             | isbn              | precio | autor_id |
+----+------------------------------------+-------------------+--------+----------+
|  3 | El libro de prueba 2               | 1234567890123     |  20.99 |        1 |
|  5 | El libro de prueba 3               | 12345567890123    |  20.99 |        1 |
|  8 | El libro de prueba 4               | 12345567896923    |  23.99 |        2 |
| 11 | El Gran Libro                      | 1234567890        |  19.99 |        1 |
| 12 | La Aventura de Hoy                 | 0987654321        |  15.50 |        2 |
| 13 | Cien años de soledad               | 978-3-16-148410-0 |  19.99 |        3 |
| 14 | Harry Potter y la piedra filosofal | 978-0-7475-3269-9 |  15.99 |        4 |
| 15 | 1984                               | 978-0-452-28423-4 |  12.99 |        5 |
+----+------------------------------------+-------------------+--------+----------+
```

De la tabla de socios:

```
SELECT * FROM socios;
```

```
+----+-------------------+------------------------------+---------------------+
| id | nombre            | email                        | fecha_alta          |
+----+-------------------+------------------------------+---------------------+
|  5 | Juan Pérez        | juan.perez@example.com       | 2025-10-31 12:57:01 |
|  6 | María Gómez       | maria.gomez@empresa.org      | 2025-10-31 12:57:01 |
|  7 | Ana Sánchez       | ana.sanchez@example.com      | 2025-10-31 13:14:18 |
|  8 | Alfredo Martínez  | alfredo.martinez@example.com | 2025-10-31 13:14:18 |
+----+-------------------+------------------------------+---------------------+
```

De la tabla de prestamos:

```
SELECT * FROM prestamos;
```

```
+----+----------+----------+---------------------+------------------+
| id | socio_id | libro_id | fecha_prestamo      | fecha_devolucion |
+----+----------+----------+---------------------+------------------+
|  3 |        5 |       14 | 2025-10-31 13:20:05 | NULL             |
|  4 |        6 |       15 | 2023-10-01 00:00:00 | 2023-10-10       |
+----+----------+----------+---------------------+------------------+
```

## Paso final: Resumen de comprobaciones finales

```
SHOW TABLES;
DESCRIBE autores;
DESCRIBE libros;
DESCRIBE socios;
```

```
mysql> SHOW TABLES;
+------------------------+
| Tables_in_biblioteca25 |
+------------------------+
| autores                |
| libros                 |
| prestamos              |
| socios                 |
+------------------------+
4 rows in set (0,00 sec)

mysql> DESCRIBE autores;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int          | NO   | PRI | NULL    | auto_increment |
| nombre | varchar(100) | NO   |     | NULL    |                |
| pais   | varchar(80)  | YES  |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
3 rows in set (0,00 sec)

mysql> DESCRIBE libros;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| titulo   | varchar(200) | NO   | MUL | NULL    |                |
| isbn     | varchar(20)  | NO   | UNI | NULL    |                |
| precio   | decimal(8,2) | NO   |     | NULL    |                |
| autor_id | int          | NO   | MUL | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
5 rows in set (0,00 sec)

mysql> DESCRIBE socios;
+------------+--------------+------+-----+-------------------+-------------------+
| Field      | Type         | Null | Key | Default           | Extra             |
+------------+--------------+------+-----+-------------------+-------------------+
| id         | int          | NO   | PRI | NULL              | auto_increment    |
| nombre     | varchar(100) | NO   |     | NULL              |                   |
| email      | varchar(120) | NO   | UNI | NULL              |                   |
| fecha_alta | timestamp    | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+------------+--------------+------+-----+-------------------+-------------------+
4 rows in set (0,01 sec)
```

---

# Conclusión

El ejercicio demuestra cómo estructurar una base de datos relacional con relaciones claras entre tablas y restricciones para garantizar la validez de los datos. La implementación de claves foráneas asegura la consistencia entre las tablas, mientras que los índices optimizan las búsquedas. Este enfoque refuerza las mejores prácticas en diseño de bases de datos, garantizando eficiencia y coherencia en el manejo de la información de la biblioteca.

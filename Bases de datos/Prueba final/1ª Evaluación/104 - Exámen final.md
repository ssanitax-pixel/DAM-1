Hemos usado SQL, que es un lenguaje de programación que nos permite crear, administrar y manipular bases de datos relacionales.
En este ejercicio hemos desarrollado una base de datos llamada `portafolioexamen`, compuesta por dos entidades, `piezasportafolio` y `categoriasportafolio`, unidas por una `clave foránea (FK)`. Esta relación nos permite clasificar cada pieza artística dentro de una categoría específica, que en este caso hemos creado dos `pintura` y `escultura`.
A través de consultas `JOIN`, se pueden combinar los datos de ambas tablas para mostrar información completa, y con una `vista` se crea una representación virtual que facilita el acceso y consulta de esos datos de forma más práctica.

---

Vamos a crear una base de datos llamada `portafolioexamen`, para ello primero abriremos terminal y entraremos en MySQL.

```
sudo mysql -u root -p
```

Creamos la base de datos con el nombre requerido.

```
CREATE DATABASE portafolioexamen;
```

Nos aseguramos que aparece.

```
SHOW DATABASES;
```
```
+--------------------+
| Database           |
+--------------------+
| biblioteca25       |
| ejemploclaves      |
| empresadam         |
| information_schema |
| mysql              |
| performance_schema |
| portafolio         |
| portafolioexamen   |
| sys                |
+--------------------+
```

Ahora nos metemos en la base de datos recién creada.

```
USE portafolioexamen;
```

Hay que crear dos entidades, piezasportafolio (Identificador, titulo, descripcion, fecha, id_categoria) y categoriasportafolio (Identificador, nombre).

Vamos paso a paso, primero creamos la enditad `piezasportafolio`, aquí aprovechamos y creamos en `Identificador` ya la clave primaria, lo mismo haremos con la siguiente tabla.

```
CREATE TABLE piezasportafolio (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    descripcion TEXT,
    fecha VARCHAR(100),
    id_categoria INT
);
```

Nos aseguramos que se ha creado la tabla correctamente.

```
DESCRIBE piezasportafolio;
```
```
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| titulo        | varchar(100) | YES  |     | NULL    |                |
| descripcion   | text         | YES  |     | NULL    |                |
| fecha         | varchar(100) | YES  |     | NULL    |                |
| id_categoria  | int          | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
```

Ahora crearemos la segunda tabla, llamada `categoriasportafolio`.

```
CREATE TABLE categoriasportafolio (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100)
);
```

Nos aseguramos como en la tabla anterior.

```
DESCRIBE categoriasportafolio;
```
```
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| nombre        | varchar(100) | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
```

Creamos la clave foránea.

```
ALTER TABLE piezasportafolio
ADD CONSTRAINT piezas_a_categorias
FOREIGN KEY (id_categoria) REFERENCES categoriasportafolio(Identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;
```

Nos aseguramos.

```
DESCRIBE piezasportafolio;
```
```
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| titulo        | varchar(100) | YES  |     | NULL    |                |
| descripcion   | text         | YES  |     | NULL    |                |
| fecha         | varchar(100) | YES  |     | NULL    |                |
| id_categoria  | int          | YES  | MUL | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
```

Ahora vamos a insertar datos en las tablas.

Primero vamos con la tabla de `categoriasportafolio`, ya que si no hay categorías, no se podría poner el `id_categoria` en la tabla `piezasportafolio`.

```
INSERT INTO categoriasportafolio VALUES (
    NULL,
    'Pintura'
);
```
```
INSERT INTO categoriasportafolio VALUES (
    NULL,
    'Escultura'
);
```

Revisamos que se han insertado correctamente las categorías.

```
SELECT * FROM categoriasportafolio;
```
```
+---------------+-----------+
| Identificador | nombre    |
+---------------+-----------+
|             1 | Pintura   |
|             2 | Escultura |
+---------------+-----------+
```

Ahora vamos a crear las piezas, por ejemplo crearemos tres de momento.

```
INSERT INTO piezasportafolio VALUES (
    NULL,
    'La mañana sobre el río', 
    'Óleo sobre lienzo que representa un amanecer en un paisaje fluvial. Destaca por el uso de luces suaves y reflejos en el agua.', 
    '2020-11-10', 
    1
);
```
```
INSERT INTO piezasportafolio VALUES (
    NULL,
    'Retrato de mujer con sombrero', 
    'Cuadro al óleo de mediados del siglo XX.', 
    '1954-06-28', 
    1
);
```
```
INSERT INTO piezasportafolio VALUES (
    NULL,
    'Estatua del pensador moderno', 
    'Escultura en bronce que representa a una figura humana en actitud reflexiva. Inspirada en el pensamiento contemporáneo y la introspección.', 
    '1999-05-06', 
    2
);
```

Nos aseguramos que las piezas se han implementado correctamente.

```
SELECT * FROM piezasportafolio;
```
```
+---------------+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------+--------------+
| Identificador | titulo                        | descripcion                                                                                                                                  | fecha      | id_categoria |
+---------------+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------+--------------+
|             1 | La mañana sobre el río        | Óleo sobre lienzo que representa un amanecer en un paisaje fluvial. Destaca por el uso de luces suaves y reflejos en el agua.                | 2020-11-10 |            1 |
|             2 | Retrato de mujer con sombrero | Cuadro al óleo de mediados del siglo XX.                                                                                                     | 1954-06-28 |            1 |
|             3 | Estatua del pensador moderno  | Escultura en bronce que representa a una figura humana en actitud reflexiva. Inspirada en el pensamiento contemporáneo y la introspección.   | 1999-05-06 |            2 |
+---------------+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------+--------------+
```

Vamos a actualizar una de las piezas, para asegurarnos que tenemos opción de corregir datos errónemos.

```
UPDATE piezasportafolio
SET titulo = 'La mañana sobre la montaña'
WHERE Identificador = 1;
```

Miramos que se ha actualizado el nombre.

```
SELECT * FROM piezasportafolio;
```
```
+---------------+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------+--------------+
| Identificador | titulo                        | descripcion                                                                                                                                  | fecha      | id_categoria |
+---------------+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------+--------------+
|             1 | La mañana sobre la montaña    | Óleo sobre lienzo que representa un amanecer en un paisaje fluvial. Destaca por el uso de luces suaves y reflejos en el agua.                | 2020-11-10 |            1 |
|             2 | Retrato de mujer con sombrero | Cuadro al óleo de mediados del siglo XX.                                                                                                     | 1954-06-28 |            1 |
|             3 | Estatua del pensador moderno  | Escultura en bronce que representa a una figura humana en actitud reflexiva. Inspirada en el pensamiento contemporáneo y la introspección.   | 1999-05-06 |            2 |
+---------------+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------+--------------+
```

Vamos a probar a borrar un registro. 

```
DELETE FROM 
piezasportafolio
WHERE Identificador = 2;
```

Miramos si se ha borrado o no.

```
SELECT * FROM piezasportafolio;
```
```
+---------------+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------+--------------+
| Identificador | titulo                       | descripcion                                                                                                                                  | fecha      | id_categoria |
+---------------+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------+--------------+
|             1 | La mañana sobre la montaña   | Óleo sobre lienzo que representa un amanecer en un paisaje fluvial. Destaca por el uso de luces suaves y reflejos en el agua.                | 2020-11-10 |            1 |
|             3 | Estatua del pensador moderno | Escultura en bronce que representa a una figura humana en actitud reflexiva. Inspirada en el pensamiento contemporáneo y la introspección.   | 1999-05-06 |            2 |
+---------------+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------+--------------+
```

Realizamos una petición cruzada.

```
SELECT piezasportafolio.titulo,piezasportafolio.descripcion,piezasportafolio.fecha,
categoriasportafolio.nombre
FROM piezasportafolio
LEFT JOIN categoriasportafolio
ON piezasportafolio.id_categoria = categoriasportafolio.Identificador;
```
```
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------+---------+
| titulo                       | descripcion                                                                                                                                  | fecha      | nombre  |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------+---------+
| La mañana sobre la montaña   | Óleo sobre lienzo que representa un amanecer en un paisaje fluvial. Destaca por el uso de luces suaves y reflejos en el agua.                | 2020-11-10 | Pintura |
| Estatua del pensador moderno | Escultura en bronce que representa a una figura humana en actitud reflexiva. Inspirada en el pensamiento contemporáneo y la introspección.   | 1999-05-06 | Escultura |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------+---------+
```

Creamos una vista.

```
CREATE VIEW vista_categorias AS
SELECT piezasportafolio.titulo,piezasportafolio.descripcion,piezasportafolio.fecha,
categoriasportafolio.nombre
FROM piezasportafolio
LEFT JOIN categoriasportafolio
ON piezasportafolio.id_categoria = categoriasportafolio.Identificador;
```

Ahora se comportará como una tabla.

```
SELECT * FROM vista_categorias;
```
```
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------+---------+
| titulo                       | descripcion                                                                                                                                  | fecha      | nombre  |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------+---------+
| La mañana sobre la montaña   | Óleo sobre lienzo que representa un amanecer en un paisaje fluvial. Destaca por el uso de luces suaves y reflejos en el agua.                | 2020-11-10 | Pintura |
| Estatua del pensador moderno | Escultura en bronce que representa a una figura humana en actitud reflexiva. Inspirada en el pensamiento contemporáneo y la introspección.   | 1999-05-06 | Escultura |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+------------+---------+
```

Ahora vamos a crear un usuario con permisos para acceder a la base de datos.

```
CREATE USER 
'usuario2'@'localhost' 
IDENTIFIED  BY 'Portafolio123#';
```

Le damos permisos al ususario.

```
GRANT USAGE ON *.* TO 'usuario2'@'localhost';
```

Le quitamos los límites que pueda tener.

```
ALTER USER 'usuario2'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
```

Le damos acceso a la base de datos de `portafolioexamen`.

```
GRANT ALL PRIVILEGES ON `examenportafolio`.* 
TO 'usuario2'@'localhost';
```

Recargamos la tabla de privilegios.

```
FLUSH PRIVILEGES;
```

Listamos los usuarios para ver su se ha implementado correctamente.

```
SELECT User, Host FROM mysql.user;
```
```
+------------------+-----------+
| User             | Host      |
+------------------+-----------+
| ana              | localhost |
| debian-sys-maint | localhost |
| empresadam       | localhost |
| mysql.infoschema | localhost |
| mysql.session    | localhost |
| mysql.sys        | localhost |
| root             | localhost |
| usuario1         | localhost |
| usuario2         | localhost |
+------------------+-----------+
```

---

Durante el proceso se construyó la base de datos, se definieron las tablas con sus claves primarias y foráneas, se insertaron registros de ejemplo y se comprobó la relación entre las entidades mediante un `LEFT JOIN`. Finalmente, se generó una vista que reúne la información de ambas tablas como si fuera una sola. Este procedimiento demuestra cómo SQL permite estructurar, relacionar y visualizar datos de manera eficiente, sentando las bases para el desarrollo de la parte visible y administrativa del portafolio web.

Y para luego poder usar todo esto que hemos formado, hemos creado un usuario.

En este ejercicio se practican los conceptos de restricciones de validación en bases de datos relacionales, que sirven para asegurar la integridad y validez de los datos.
Se trabajan comandos como 'ALTER TABLE' para modificar la estructura de las tablas y restricciones como 'CHECK', 'NOT NULL' o 'PRIMARY KEY', que controlan los valores permitidos en cada campo.
El objetivo es comprender cómo estas reglas ayudan a mantener la base de datos coherente y evitar errores al insertar o modificar información.

---

Primero revisamos la estructura de la tabla.

```
DESCRIBE clientes;
```

Añadimos una columna llamada dirección, con el tipo VARCHAR(255).

```
ALTER TABLE clientes
ADD COLUMN direccion VARCHAR(255);
```

Verificamos que el cambio se ha realizado correctamente.

```
DESCRIBE clientes;
```

Para borrar la columna llamada dirección será de la siguiente forma:

```
ALTER TABLE clientes
DROP COLUMN direccion;
```

Verificamos también que ha sido borrada.

```
DESCRIBE clientes;
```

Ahora vamos a intentar renombrar la columna dni a dninie.

```
ALTER TABLE clientes
RENAME COLUMN dni TO dninie;
```

Al habar una restricción, nos saldrá un error igual o parecido a este:

```
ERROR 3959 (HY000): Check constraint 'comprobar_dni_nie_letra' uses column 'dni', hence column cannot be dropped or renamed.
```

Así que para que el cambio se haga efectivo antes tenemos que borrar la restricción.

```
ALTER TABLE clientes
DROP CONSTRAINT comprobar_dni_nie_letra;
```

Ahora ya sí que podemos realizar el cambio y comprobarlo.

```
ALTER TABLE clientes
RENAME COLUMN dni TO dninie;

DESCRIBE clientes;
```

Ahora añadiremos la restricción que valide tanto los DNIs como los NIEs utilizando la expresión regular proporcionada en el GitHub del profesor.

```
ALTER TABLE clientes
  ADD CONSTRAINT comprobar_dni_nie_letra
  CHECK (
    (
      -- DNI: 8 dígitos + letra
      dninie REGEXP '^[0-9]{8}[A-Za-z]$'
      AND
      UPPER(SUBSTRING(dninie, 9, 1)) =
      SUBSTRING('TRWAGMYFPDXBNJZSQVHLCKE',
                (CAST(SUBSTRING(dninie, 1, 8) AS UNSIGNED) MOD 23) + 1,
                1)
    )
    OR
    (
      -- NIE: X/Y/Z + 7 dígitos + letra
      dninie REGEXP '^[XYZxyz][0-9]{7}[A-Za-z]$'
      AND
      UPPER(SUBSTRING(dninie, 9, 1)) =
      SUBSTRING('TRWAGMYFPDXBNJZSQVHLCKE',
                (
                  CAST(CONCAT(
                        CASE UPPER(SUBSTRING(dninie, 1, 1))
                          WHEN 'X' THEN '0'
                          WHEN 'Y' THEN '1'
                          WHEN 'Z' THEN '2'
                        END,
                        SUBSTRING(dninie, 2, 7)
                  ) AS UNSIGNED) MOD 23
                ) + 1,
                1)
    )
  );
```

Comprobamos que la restricción se ha añadido ejecuantando nuevamente lo siguiente:

```
DESCRIBE clientes;
```

Insertamos un cliente correctamente y no debería de saltar ningún fallo.

```
INSERT INTO clientes VALUES(
  NULL,
  '12345678Z',
  'Jose Vicente',
  'Carratala Sanchis',
  'info@jocarsa.com'
);
```

Ahora intentaremos insertar otro cliente que no cumpla las restricciones, y nos saldrá el siguiente error.

```
INSERT INTO clientes VALUES(
  NULL,
  '12345678A',
  'Jose Vicente',
  'Carratala Sanchis',
  'info@jocarsa.com'
);

ERROR 3819 (HY000): Check constraint 'comprobar_dni_nie_letra' is violated.
```

Ahora crearemos una tabla llamada productos con las columnas mencionadas en el '011-Actividad en clase.md'.

```
CREATE TABLE productos ( id INT, 
    nombre VARCHAR(255) NOT NULL, 
    descripcion TEXT, 
    precio DECIMAL(7,2) NOT NULL, 
    stock INT NOT NULL ) ENGINE=InnoDB;
```

Y añadimos unas cuantas restricciones necesarias para garantizar que los datos sean válidos.

```
ALTER TABLE productos MODIFY id INT NOT NULL, ADD PRIMARY KEY (id);

ALTER TABLE productos MODIFY id INT NOT NULL AUTO_INCREMENT;

ALTER TABLE productos ADD CONSTRAINT chk_stock_no_negativo CHECK (stock >= 0);

ALTER TABLE productos ADD CONSTRAINT chk_precio_no_negativo CHECK (precio >= 0);

ALTER TABLE productos ADD CONSTRAINT chk_precio_max_5000 CHECK (precio <= 5000);

ALTER TABLE productos ADD CONSTRAINT chk_nombre_min_5 CHECK (CHAR_LENGTH(nombre) >= 5);
```

Ahora nos toca probar meter algunos registros mal de forma intencionada para ver como se comportan, dando así varios errores y no dejando añadirse a la base de datos.

---

La práctica completa:

```
DESCRIBE clientes;

ALTER TABLE clientes
ADD COLUMN direccion VARCHAR(255);

DESCRIBE clientes;

ALTER TABLE clientes
DROP COLUMN direccion;

DESCRIBE clientes;

ALTER TABLE clientes
RENAME COLUMN dni TO dninie;

ERROR 3959 (HY000): Check constraint 'comprobar_dni_nie_letra' uses column 'dni', hence column cannot be dropped or renamed.

ALTER TABLE clientes
DROP CONSTRAINT comprobar_dni_nie_letra;

ALTER TABLE clientes
RENAME COLUMN dni TO dninie;

DESCRIBE clientes;

ALTER TABLE clientes
  ADD CONSTRAINT comprobar_dni_nie_letra
  CHECK (
    (
      -- DNI: 8 dígitos + letra
      dninie REGEXP '^[0-9]{8}[A-Za-z]$'
      AND
      UPPER(SUBSTRING(dninie, 9, 1)) =
      SUBSTRING('TRWAGMYFPDXBNJZSQVHLCKE',
                (CAST(SUBSTRING(dninie, 1, 8) AS UNSIGNED) MOD 23) + 1,
                1)
    )
    OR
    (
      -- NIE: X/Y/Z + 7 dígitos + letra
      dninie REGEXP '^[XYZxyz][0-9]{7}[A-Za-z]$'
      AND
      UPPER(SUBSTRING(dninie, 9, 1)) =
      SUBSTRING('TRWAGMYFPDXBNJZSQVHLCKE',
                (
                  CAST(CONCAT(
                        CASE UPPER(SUBSTRING(dninie, 1, 1))
                          WHEN 'X' THEN '0'
                          WHEN 'Y' THEN '1'
                          WHEN 'Z' THEN '2'
                        END,
                        SUBSTRING(dninie, 2, 7)
                  ) AS UNSIGNED) MOD 23
                ) + 1,
                1)
    )
  );

DESCRIBE clientes;

INSERT INTO clientes VALUES(
  NULL,
  '12345678Z',
  'Jose Vicente',
  'Carratala Sanchis',
  'info@jocarsa.com'
);

INSERT INTO clientes VALUES(
  NULL,
  '12345678A',
  'Jose Vicente',
  'Carratala Sanchis',
  'info@jocarsa.com'
);

ERROR 3819 (HY000): Check constraint 'comprobar_dni_nie_letra' is violated.

CREATE TABLE productos ( id INT, 
    nombre VARCHAR(255) NOT NULL, 
    descripcion TEXT, 
    precio DECIMAL(7,2) NOT NULL, 
    stock INT NOT NULL ) ENGINE=InnoDB;
    
ALTER TABLE productos MODIFY id INT NOT NULL, ADD PRIMARY KEY (id);

ALTER TABLE productos MODIFY id INT NOT NULL AUTO_INCREMENT;

ALTER TABLE productos ADD CONSTRAINT chk_stock_no_negativo CHECK (stock >= 0);

ALTER TABLE productos ADD CONSTRAINT chk_precio_no_negativo CHECK (precio >= 0);

ALTER TABLE productos ADD CONSTRAINT chk_precio_max_5000 CHECK (precio <= 5000);

ALTER TABLE productos ADD CONSTRAINT chk_nombre_min_5 CHECK (CHAR_LENGTH(nombre) >= 5);


```

---

Con esta práctica he aprendido a crear, modificar y eliminar restricciones en SQL, comprobando cómo impiden que se inserten datos incorrectos.
También he entendido la importancia de definir reglas de validación directamente en la base de datos para garantizar su consistencia y fiabilidad.
En resumen, las restricciones son una herramienta esencial para mantener la calidad de los datos en cualquier sistema relacional.

El modelo de datos relacional organiza la información en tablas, facilitando su almacenamiento y gestión. En este ejercicio, definimos una tabla llamada Cliente para almacenar datos personales como dni, nombre, apellidos y email. Este modelo es fundamental en bases de datos, permitiendo organizar, recuperar y mantener los datos de manera eficiente.

---

Primero tenemos que crear la tabla, el VARCHAR es la cantidad de caracteres máximos que dejaremos que se implemente en cada apartado, la PRIMARY KEY servirá para garantizar que cada cliente tenga un DNI único, ya que es un documento personal e intransferible, por último en el email pondremos la restricción UNIQUE para garantizar que no haya dos clientes con el mismo correo electrónico.

```
CREATE TABLE Cliente(
	dni VARCHAR(9) PRIMARY KEY,
	nombre VARCHAR(50),
	apellidos VARCHAR(100),
	email VARCHAR(255) UNIQUE
);
```

Para asegurarnos que lo que hemos ejecutado ha sido implementado correctamente, introducimos el siguiente código.

```
SHOW TABLES;
```

Queda introducir la información de nuestros clientes.

```
INSERT INTO Cliente VALUES(
	'26525959J',
	'Juan',
	'Pérez',
	'juan@gmail.com'
);
```

Y nos aseguramos que hemos metido los datos correctamente.

```
SELECT * FROM Cliente;
```

---

Aquí está el código completo.

```
CREATE TABLE Cliente(
	dni VARCHAR(9) PRIMARY KEY,
	nombre VARCHAR(50),
	apellidos VARCHAR(100),
	email VARCHAR(255) UNIQUE
);

SHOW TABLES;

INSERT INTO Cliente VALUES(
	'26525959J',
	'Juan',
	'Pérez',
	'juan@gmail.com'
);

INSERT INTO Cliente VALUES(
	'26525961S',
	'María',
	'López',
	'maria@gmail.com'
);

INSERT INTO Cliente VALUES(
	'26214990G',
	'Pedro',
	'López',
	'pedro@gmail.com'
);

SELECT * FROM Cliente;
```

---

Al querer visualizar la tabla, se verá así:

+-----------+--------+-----------+-----------------+
| dni       | nombre | apellidos | email           |
+-----------+--------+-----------+-----------------+
| 26214990G | Pedro  | López     | pedro@gmail.com |
| 26525959J | Juan   | Pérez     | juan@gmail.com  |
| 26525961S | María  | López     | maria@gmail.com |
+-----------+--------+-----------+-----------------+

---

Este ejercicio demuestra cómo organizar y almacenar datos en una base de datos relacional utilizando SQL. Al crear la tabla Cliente y aplicar restricciones como la clave primaria en el dni y la restricción UNIQUE en el email, se asegura que los datos sean consistentes y no se repitan. Además, la inserción de registros y la consulta de los datos muestran cómo interactuar con una base de datos para almacenar y recuperar información de manera estructurada. Este tipo de modelo relacional es útil en muchas aplicaciones, como la gestión de clientes, registros de usuarios o cualquier sistema que necesite almacenar información única y organizada.

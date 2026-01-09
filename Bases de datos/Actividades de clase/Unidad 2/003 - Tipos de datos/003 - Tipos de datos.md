Los tipos de datos en una base de datos relacional son esenciales para organizar y almacenar la información de manera eficiente. En este ejercicio, hemos creado una tabla de clientes utilizando tipos como VARCHAR para almacenar nombres, apellidos y correos electrónicos. Aplicar estos conceptos en un ejemplo práctico ayuda a entender cómo gestionar datos de manera estructurada y optimizada.

---

Creamos la tabla de 'clientes':

Para definir la estructura de la tabla, usamos el comando CREATE TABLE para establecer los campos que se utilizarán. En este caso, la tabla tiene cuatro columnas:

dni: Almacenará el DNI del cliente con un tipo de datos VARCHAR(9).

nombre: Almacenará el nombre del cliente con un tipo VARCHAR(50).

apellidos: Almacenará los apellidos del cliente con un tipo VARCHAR(255).

email: Almacenará el correo electrónico del cliente con un tipo VARCHAR(100).

```
CREATE TABLE clientes (
  dni VARCHAR(9),
  nombre VARCHAR(50),
  apellidos VARCHAR(255),
  email VARCHAR(100)
);
```

A continuación, insertamos tres registros de ejemplo para representar clientes en la tabla. Los datos que insertaremos son:

Jose Vicente Carratala Sanchis con el DNI 12345678A y su correo info@jocarsa.com.

María Elena López González con el DNI 98765432B y su correo maria.lopez@example.com.

Pedro Miguel Fernández Rodríguez con el DNI 11223344C y su correo pedro.miguel@ejemplo.com.

Los comandos para insertar estos datos son:

```
INSERT INTO clientes VALUES(
  '12345678A',
  'Jose Vicente',
  'Carratala Sanchis',
  'info@jocarsa.com'
);
```

Finalmente, realizamos una consulta para mostrar todos los registros de la tabla.

```
SELECT * FROM clientes;
```

---

Aquí están todos los comandos:

```
CREATE TABLE clientes (
  dni VARCHAR(9),
  nombre VARCHAR(50),
  apellidos VARCHAR(255),
  email VARCHAR(100)
);

INSERT INTO clientes VALUES(
  '12345678A',
  'Jose Vicente',
  'Carratala Sanchis',
  'info@jocarsa.com'
);

INSERT INTO clientes VALUES(
  '98765432B',
  'María Elena',
  'López González',
  'maria.lopez@example.com'
);

INSERT INTO clientes VALUES(
  '11223344C',
  'Pedro Miguel',
  'Fernández Rodríguez',
  'pedro.miguel@ejemplo.com'
);

SELECT * FROM clientes;
```

---

Este ejercicio muestra cómo los tipos de datos en bases de datos relacionales permiten gestionar la información de forma eficiente. La correcta elección de tipos asegura que los datos se almacenen y consulten de manera óptima.

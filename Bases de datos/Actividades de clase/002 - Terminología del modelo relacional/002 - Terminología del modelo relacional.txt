En el estudio de Bases de Datos Relacionales, aprender a crear y gestionar bases de datos es esencial. La base de datos "empresadam" servirá como ejemplo práctico para entender cómo organizar datos dentro de una empresa, permitiendo manejar información como empleados, sucursales y más. Este ejercicio nos ayuda a familiarizarnos con el proceso de instalación de MySQL, la creación de bases de datos y la gestión de tablas, que son los primeros pasos fundamentales en la administración de bases de datos.

---

Instalamos MySQL en la máquina virtual, así que abrimos terminal y ponemos lo siguiente.

```
sudo apt install mysql-server
```

Aseguramos la instalación.

```
mysql_secure_installation
```

Abrimos MySQL.

```
sudo mysql -u root -p
```

Creamos la base de datos, que en este caso se llamará empresadam.

```
CREATE DATABASE empresadam;
```

Verificamos que la base de datos se ha creado correctamente.

```
SHOW DATABASES;
```

Aquí está creada la tabla de empleados, por ejemplo.

```
CREATE TABLE empleados (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    puesto VARCHAR(50),
    salario DECIMAL(10,2)
);
```

Nos aseguramos que las tablas se han implementado correctamente.

```
SHOW TABLES;
```

--- 

Aquí está el código completo:

```
sudo apt install mysql-server

mysql_secure_installation

sudo mysql -u root -p

CREATE DATABASE empresadam;

SHOW DATABASES;

CREATE TABLE empleados (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    puesto VARCHAR(50),
    salario DECIMAL(10,2)
);

CREATE TABLE sucursales (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    ubicacion VARCHAR(100)
);

SHOW TABLES;
```

---

Este ejercicio es esencial para comprender cómo crear una base de datos y cómo organizar diferentes tipos de información en tablas relacionadas. Al crear una base de datos llamada empresadam, aprenderemos a manejar datos estructurados y a facilitar su acceso y gestión. Además, colaborar en grupos para crear tablas diferentes simula una situación real de trabajo en equipo dentro de una empresa. Estos conocimientos son fundamentales para diseñar y administrar bases de datos de manera eficiente, lo cual es una habilidad crucial en el desarrollo de sistemas de información.

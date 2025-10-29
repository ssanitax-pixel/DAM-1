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

Control + Alt + T

sudo mysql -u root -p

USE empresadam;

SHOW TABLES;

DESCRIBE clientes;

ALTER TABLE clientes ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;

DESCRIBE clientes;

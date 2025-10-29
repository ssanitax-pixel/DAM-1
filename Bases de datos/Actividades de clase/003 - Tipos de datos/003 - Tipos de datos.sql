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

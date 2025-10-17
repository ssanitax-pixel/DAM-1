DESCRIBE Clientes;

-- agregar columna
ALTER TABLE Clientes
ADD COLUMN direction VARCHAR(255);

DESCRIBE Clientes;

--quitar columna
ALTER TABLE Clientes
DROP COLUMN direction;

DESCRIBE Clientes;

--cambio nombre
--antes quitar restricciones
ALTER TABLE Clientes
DROP CONSTRAINT comprobar_dni_nie_letra;

-- ahora si quitamos
ALTER TABLE Clientes
RENAME COLUMN dni TO dninie;

--ponemos restricciones otra vez


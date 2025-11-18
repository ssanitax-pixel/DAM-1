-- crea usuario nuevo con contraseña
-- creamos el nombre de usuario que queramos
CREATE USER
'portafolioceac'@'localhost'
IDENTIFIED BY 'portafolioceac';

--permite acceso a ese usuario
GRANT USAGE ON *.* TO 'portafolioceac'@'localhost';
--[tuservidor] == localhost
-- La contraseña puede requerir Mayus, minus, números, caracteres, min len

-- quitale todos los limites que tenga
ALTER USER 'portafolioceac'@'localhost'
REQUIERE NONE
WITH MAX_

-- crea usuario nuevo con contraseña
-- creamos el nombre de usuario que queramos
--CREATE USER 
--'[tunombredeusuario]'@'[tuservidor]' 
--IDENTIFIED  BY '[tucontraseña]';

CREATE USER 
'ana'@'localhost' 
IDENTIFIED  BY 'Y9ac9WAWTkHx$';

-- permite acceso a ese usuario
-- GRANT USAGE ON *.* TO '[tunombredeusuario]'@'[tuservidor]';

GRANT USAGE ON *.* TO 'ana'@'localhost';

-- quitale todos los limites que tenga
-- ALTER USER '[tunombredeusuario]'@'[tuservidor]' 
-- REQUIRE NONE 
-- WITH MAX_QUERIES_PER_HOUR 0 
-- MAX_CONNECTIONS_PER_HOUR 0 
-- MAX_UPDATES_PER_HOUR 0 
-- MAX_USER_CONNECTIONS 0;

ALTER USER 'ana'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- dale acceso a la base de datos empresadam
-- GRANT ALL PRIVILEGES ON `[tubasededatos]`.* 
-- TO '[tunombredeusuario]'@'[tuservidor]';

GRANT ALL PRIVILEGES ON `empresadam`.* 
TO 'ana'@'localhost';

-- recarga la tabla de privilegios
FLUSH PRIVILEGES;

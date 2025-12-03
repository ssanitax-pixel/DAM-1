sudo mysql -u root -p

USE portafolio;

CREATE USER 
'usuario1'@'localhost' 
IDENTIFIED  BY 'Portafolio123#';

GRANT USAGE ON *.* TO 'usuario1'@'localhost';

ALTER USER 'usuario1'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON `portafolio`.* 
TO 'usuario1'@'localhost';

FLUSH PRIVILEGES;

SELECT User, Host FROM mysql.user;

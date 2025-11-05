Paso 2 . Hacer una aplicación de Python-consola:
a) Mensaje de bienvenida
b) Que presente opciones CRUD
c) Bucle infinito
d) Atrapar las opciones con if-elif
e) Para cada una de las opciones, ejecutar MySQL INSERT, SELECT, UPDATE, DELETE

---

Antes tendremos que crear un usuario en la base de datos `portafolio`.

Nos metemos en MySQL 

```
sudo mysql -u root -p
```

Y ahora en la base de datos.

```
USE portafolio;
```

Empezamos a crear un usuario.

```
CREATE USER 
'usuario1'@'localhost' 
IDENTIFIED  BY 'Portafolio123#';
```

Le damos permiso al usuario.

```
GRANT USAGE ON *.* TO 'usuario1'@'localhost';
```

Le quitamos todos los límites que tenga.

```
ALTER USER 'usuario1'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
```

Le damos acceso a la base de datos de `portafolio`.

```
GRANT ALL PRIVILEGES ON `portafolio`.* 
TO 'usuario1'@'localhost';
```

Recargamos la tabla de privilegios.

```
FLUSH PRIVILEGES;
```

Listamos los usuarios para ver si se ha implementado correctamente.

```
SELECT User, Host FROM mysql.user;
```



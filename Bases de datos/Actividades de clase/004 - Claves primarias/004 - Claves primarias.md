Las bases de datos son esenciales para almacenar y gestionar información de manera eficiente. Una clave primaria es crucial, ya que identifica de forma única cada registro en una tabla. En este ejercicio, aprenderemos cómo crear y gestionar una clave primaria en la tabla clientes de la base de datos empresadam para garantizar la integridad y organización de los datos.

---

Primero abrimos el terminal usando el comando:

```
Control + Alt + T
```

Ingresamos al sistema de gestión de base de datos MySQL con siguiente comando.

```
sudo mysql -u root -p
```

Seleccionamos la base de datos.

```
USE empresadam;
```

Para asegurarnos de que estamos en la base de datos correcta escribimos:

```
SHOW TABLES;
```

Para ver el contenido de la tabla clientes:

```
DESCRIBE clientes;
```

Para crear una clave primaria llamada identificador en la tabla clientes, escribimos el siguiente comando:

```
ALTER TABLE clientes ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;
```

Escribimos nuevamente esto para asegurar que la columna identificador ha sido añadida y ahora es la clave primaria.

```
DESCRIBE clientes;
```

---

Aquí está el código completo:

```
Control + Alt + T

sudo mysql -u root -p

USE empresadam;

SHOW TABLES;

DESCRIBE clientes;

ALTER TABLE clientes ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;

DESCRIBE clientes;
```

---

La creación de una clave primaria es esencial para asegurar que cada registro en una base de datos sea único y fácilmente identificable. Este ejercicio ilustra cómo implementar esta clave primaria en una tabla, lo que es fundamental para la integridad de los datos y la eficiencia en las consultas.

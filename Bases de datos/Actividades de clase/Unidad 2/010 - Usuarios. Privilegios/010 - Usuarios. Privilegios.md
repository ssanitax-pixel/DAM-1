En el ejercicio, hemos repasado el gestionar usuarios y privilegios en MySQL, una habilidad esencial para administrar el acceso y la seguridad en bases de datos. Comenzamos mostrando los usuarios existentes en el sistema y sus privilegios. Luego, creamos un nuevo usuario y le asignamos privilegios completos sobre todas las bases de datos. La correcta administración de usuarios y privilegios es fundamental para garantizar un control adecuado sobre quién tiene acceso a qué datos.

---

1. **Mostrar usuarios en el Sistema:**

Conectamos a nuestra base de datos MySQL como siempre.

```
sudo mysql -u root -p
```

Y ejecutamos la siguiente consulta para ver todos los usuarios y sus privilegios.

```
SELECT User, Host FROM mysql.user;
```

Esta consulta sirve paara mostrar una lista de todos los usuarios configurados en el sistema junto con su host.


2. **Crear un Nuevo Usuario:**

Vamos a crear el usuario utilizando la siguiente consulta.

```
CREATE USER 'anasanchez'@'localhost' IDENTIFIED BY 'sogtulapdt';
```

Comprobamos que el usuario ha sido registrado correctamente.

```
SELECT User, Host FROM mysql.user;
```


3. **Asignar Privilegios al Nuevo Usuario:**

Ahora vamos a darle acceso a todas las bases de datos.

```
GRANT ALL PRIVILEGES ON *.* TO 'anasanchez'@'localhost';
```

Por último recargamos la tabla de privilegios para asegurarnos de que los cambios surgen efecto.

```
FLUSH PRIVILEGES;
```

---

Este ejercicio nos ha permitido comprender cómo gestionar usuarios y asignar privilegios en MySQL. Desde la visualización de los usuarios hasta la creación y configuración de un nuevo usuario con privilegios específicos, hemos aprendido a manejar las herramientas necesarias para administrar la seguridad y el acceso a las bases de datos. Una correcta gestión de usuarios y privilegios es esencial para mantener la integridad y protección de los datos en cualquier entorno de bases de datos.

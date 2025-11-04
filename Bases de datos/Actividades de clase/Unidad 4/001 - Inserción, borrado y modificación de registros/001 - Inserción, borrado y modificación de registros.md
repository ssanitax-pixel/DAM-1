El modelo CRUD (Create, Read, Update, Delete) es la base del manejo de datos en sistemas relacionales. A través de estas cuatro operaciones fundamentales, es posible gestionar la información almacenada en una base de datos de manera eficiente y organizada. Además, la creación de copias de seguridad garantiza la integridad y disponibilidad de los datos ante posibles fallos o pérdidas. Practicar estas operaciones en un entorno real, como una base de datos de clientes, permite afianzar los conocimientos adquiridos en clase y comprender la importancia de combinar el aprendizaje técnico con el bienestar personal.

---

Para crear la copia de seguridad de la base de datos, usando mysqldump desde la terminal, es decir, fuera del entorno MySQL.

Escribimos lo siguiente.

```
mysqldump -u root -p empresarial > backup_empresarial.sql
```

Entramos en MySQL

```
sudo mysql -u root -p
```

Usamos la base de datos correspondiente.

```
USE empresarial;
```

Ahora realizamos una inserción de un nuevo cliente.

```
INSERT INTO clientes (nombre, telefono, email, direccion)
VALUES ('Laura García', '620891718', 'laura.garcia@example.com', 'Calle Mayor 15, Valencia');
```

Ahora cambiamos el nombre del cliente que tiene el número de teléfono `620891718` a Jose Vicente.

```
UPDATE clientes
SET nombre = 'Jose Vicente'
WHERE telefono = '620891718';
```

Verificamos que la actualización se ha implementado.

```
SELECT * FROM clientes;
```

Eliminamos un registro.

```
DELETE FROM clientes
WHERE telefono = '620891718';
```

Comprobamos que se ha borrado.

```
SELECT * FROM clientes WHERE telefono = '620891718';
```

---

A través de este ejercicio puse en práctica los fundamentos del modelo CRUD en una base de datos MySQL. Aprendí a realizar operaciones esenciales como crear copias de seguridad, insertar nuevos registros, actualizar información existente y eliminar datos de manera controlada.
Estas acciones son fundamentales para la gestión y mantenimiento de cualquier sistema de información.

En este ejercicio trabajamos con dos tablas en MySQL, **personas** y **emails**, para entender el uso de **claves primarias** y **claves ajenas**. Primero, creamos la base de datos y las tablas. En la tabla `personas`, añadimos una columna `identificador` como clave primaria con `AUTO_INCREMENT` para garantizar valores únicos. Luego, creamos la tabla `emails`, donde también añadimos una columna `identificador` como clave primaria.

---

1. **Crear las tablas:**

Primero entramos en MySQL.

```
sudo mysql u- root -p
```

Creamos una base de datos que se llame ejemploclaves.

```
CREATE DATABASE ejemploclaves;
```

Verificamos que la base de datos ha sido creada correctamente.

```
SHOW DATABASES;
```

Ahora nos metemos dentro de ella.

```
USE ejemploclaves;
```

Creamos una tabla llamada personas en la que en nombre haya 50 caracteres máximo y apellidos con 255 de máximo.

```
CREATE TABLE personas (
	nombre VARCHAR(50),
	apellidos VARCHAR(255)
);
```

Verificamos que la tabla ha sido creada.

```
SHOW TABLES;
```

A continuación añadimos un identificador, que será la clave primaria de la tabla, para que no se permitan un identificador nulo ni uno repetido.

```
ALTER TABLE personas
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;
```

Nos aseguramos que se ha añadido correctamente.

```
DESCRIBE personas;
```


2. **Crear la tabla emails:**

Ahora crearemos una tabla nueva llamada email, con los campos dirección y persona, además de un identificador único.
Vamos paso a paso, primero creamos la tabla.

```
CREATE TABLE emails (
    direccion VARCHAR(50),
    persona VARCHAR(255)
);
```

Miramos que se ha implementado.

```
SHOW TABLES;
```

Añadimos el identificador único.

```
ALTER TABLE emails
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;
```

Miramos que se ha implementado.

```
DESCRIBE emails;
```


3. **Insertar datos en personas:**

Insertamos un registro en la tabla personas que hemos creado con anterioridad.

```
INSERT INTO personas VALUES(
	NULL,
	'María',
	'Sánchez Suárez'
);
```

Verificamos que la persona ha sido registrada en la tabla.

```
SELECT * FROM personas;
```


4. **Crear clave ajena en emails:**

Modificamos el tipo de columna persona a INT y seguidamente creamos una clave ajena que se refiera al identificador en la tabla personas.

Para cambiar el tipo de columna haremos lo siguiente:

```
ALTER TABLE emails
MODIFY COLUMN persona INT;
```

Miramos que ha sido modificada.

```
DESCRIBE emails;
```

Creamos la foreign key.

```
ALTER TABLE emails
ADD CONSTRAINT fk_emails_personas
FOREIGN KEY (persona) REFERENCES personas(identificador);
```

Volvemos a verificar.

```
DESCRIBE emails;
```


5. **Insertar datos en emails:**

Insertamos registros en la tabla emails, asegurándonos de que el valor de persona coincida con un identificador existente en la tabla personas.

```
INSERT INTO emails VALUES(
  NULL,
  'info@maria.com',
  1
);

INSERT INTO emails VALUES(
  NULL,
  'mariasanchez@gmail.com',
  1
);
```

Miramos que se ha implementado los dos emails, asegurándonos que están relacionados con la misma persona.

```
SELECT * FROM emails;
```


6. **Realizar una petición cruzada:**

Realizaremos una consulta que combine los datos de las tablas emails y personas usando la clave ajena.

```
SELECT * FROM emails
LEFT JOIN personas
ON emails.persona = personas.identificador;
```

---

El uso de claves primarias y ajenas garantiza la integridad de los datos en bases de datos relacionales. La clave primaria asegura la unicidad de los registros, mientras que la clave ajena mantiene las relaciones consistentes entre las tablas. Este ejercicio muestra cómo estructurar correctamente estas relaciones para realizar consultas más eficientes y seguras.

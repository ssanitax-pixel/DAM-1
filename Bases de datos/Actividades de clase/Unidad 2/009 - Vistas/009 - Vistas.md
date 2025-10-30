En este ejercicio, hemos preciticado a crear y usar **vistas** en bases de datos. Las vistas son consultas almacenadas que actúan como tablas virtuales, simplificando el acceso a datos combinados de varias tablas sin necesidad de escribir consultas complejas repetidamente. Creamos la vista `personas_correos` para combinar datos de las tablas `personas` y `emails`, mostrando las direcciones de correo asociadas a cada persona.

---

1. **Introducción y contextualización:**

En este ejercicio vamos a practicar el cómo crear una vista que convine información de dos tablas: `personas` y `emails`.


2. **Desarrollo técnico correcto y preciso:**

Abrimos nuestro entorno de desarrollo, que en este caso será de la siguiente forma:

Primero abrimos Terminal y dentro de él abrimos MySQL.

```
sudo mysql -u root -p
```

Nos metemos en nuestra base de datos, donde tenemos las tablas de `emails` y `personas`.

```
USE ejemploclaves;
```

Ahora ya podemos crear la vista llamada `personas_correos`.

```
CREATE VIEW personas_correos AS
SELECT
	personas.identificador,
	emails.direccion,
	personas.nombre,
	personas.apellidos
FROM emails
LEFT JOIN personas
ON emails.persona = personas.Identificador;
```

Nos aseguramos que la vista está presente en la base de datos.

```
SHOW FULL TABLES WHERE Table_type = 'VIEW';
```

3. **Aplicación práctica con ejemplo claro:**

Ahora verificaremos que se ha creado con los parámetros que queríamos y que funciona como esperamos. También podemos osbervar que se comporta como una tabla normal.

```
SELECT * FROM personas_correos;
```

---

Este ejercicio nos ha mostrado cómo las vistas pueden simplificar consultas y mejorar la eficiencia al acceder a datos de varias tablas. Al usar la vista `personas_correos`, hemos aprendido a organizar y presentar información de manera más clara y accesible, sin modificar las tablas originales. Las vistas son una herramienta clave para mantener las consultas más limpias y fáciles de gestionar.

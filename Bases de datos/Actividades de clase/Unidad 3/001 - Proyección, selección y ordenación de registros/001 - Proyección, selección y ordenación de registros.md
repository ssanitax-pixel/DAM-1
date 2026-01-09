SQL es el lenguaje que usamos para hablar con las bases de datos. En este ejercicio estamos viendo tres cosas básicas: proyección (elegir qué columnas queremos ver), selección (filtrar filas con el `WHERE`) y la ordenación (poner los datos en orden con `ORDER BY`).
Aprender esto es importante porque, cuando tenemos miles de registros, no queremos verlos todos de golpe, sino los que nos interesen en el momento, y bien ordenados.

---

Abrimos terminal e iniciamos sesión.

```
sudo mysql -u root -p
```

Seleccionamos la base de datos que queramos usar.

```
USE clientes;
```

Ahora para visualizar, en lugar de sacar todo con el asterisco, aquí solo pedimos el nombre y los apellidos. Así la tabla queda más limpia.

```
SELECT 
nombre, 
apellidos 
FROM clientes;
```

Para filtrar por condiciones usaremos `WHERE` para que solo salgan los clientes que tengan más de 18 años. También usamos `AS` para que los títulos de las columnas se lean mejor.

```
SELECT 
nombre AS 'Nombre del cliente', 
apellidos AS 'Apellidos del cliente', 
edad AS 'Edad del cliente' 
FROM clientes 
WHERE edad > 18;
```

Ahora para ordenar los datos y ver mejor quién es el más mayor, usamos `ORDER BY` con `DESC`. Esto pone los número más grandes arriba.

```
SELECT 
nombre, 
apellidos, 
edad 
FROM clientes 
ORDER BY edad DESC;
```

Para ordenar por varios campos, a veces hay apellidos iguales, así que podemos ordenar primero por edad y luego si coinciden, hacerlo también por apellidos de forma alfabética (`ASC`).

```
SELECT 
nombre AS 'Nombre del cliente', 
apellidos AS 'Apellidos del cliente', 
edad AS 'Edad del cliente' 
FROM clientes 
ORDER BY edad DESC, apellidos ASC;
```

---

El código completo:

```
SELECT 
    nombre, 
    apellidos 
FROM clientes;

SELECT 
    nombre AS 'Nombre del cliente', 
    apellidos AS 'Apellidos del cliente', 
    edad AS 'Edad del cliente' 
FROM clientes 
WHERE edad > 18;

SELECT 
    nombre, 
    apellidos, 
    edad 
FROM clientes 
ORDER BY edad DESC;

SELECT 
    nombre AS 'Nombre del cliente', 
    apellidos AS 'Apellidos del cliente', 
    edad AS 'Edad del cliente' 
FROM clientes 
ORDER BY edad DESC, apellidos ASC;
```

---

Hacer estas consultas nos ayuda a no volvernos locos con tanta información. Al final, se trata de saber pedirle a la base de datos exactamente lo que necesitamos. Esto nos vendrá muy bien para cuando hagamos programas en Python que tengan que leer datos de SQL, porque así ya le pediremos la lista filtrada y ordenada desde el principio.
Es una forma de trabajar mucho más organizada y profesional.

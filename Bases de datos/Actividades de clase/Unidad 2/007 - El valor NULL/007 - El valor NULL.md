El valor NULL en bases de datos relacionales representa la ausencia de valor o el desconocimiento de un dato. No es lo mismo que un valor vacío o cero, ya que simplemente indica que no se ha proporcionado un valor para esa columna. En MySQL, cuando se insertan registros sin especificar valores para columnas que permiten NULL, MySQL asigna automáticamente este valor a esas columnas.

---

Abrimos una terminal y ejecutamos los siguientes comandos para acceder a MySQL como usuario.

```
sudo mysql -u root -p
```

Mostramos las bases disponibles en nuestro servidor.

```
SHOW DATABASES;
```

Seleccionamos la base de datos que queremos usar, que en este caso será empresadam.

```
USE empresadam;
```

Ahora nos aseguramos de que tenemos creada una tabla llamada pedidos.

```
SHOW TABLES;
```

Intentamos insertar un pedido sin especificar todos los valores, lo cual permitirá el uso del valor NULL en los valores que no hayamos especificado nada.

```
INSERT INTO pedidos (numerodepedido, cliente) 
VALUES ('001','Juan Doe');
```

Consultamos la tabla de pedidos para asegurar que el pedido se haya insertado correctamente y cómo se maneja el valor NULL.

```
SELECT * FROM pedidos;
```

No nos dejará ya que por ejemplo en el precio lo declaramos como que no podía ser nulo.

También podríamos probar lo contrario, rellenar todos los valores para ver las diferencias con NULL.

```
INSERT INTO pedidos (numerodepedido, cliente, fecha, precio)
VALUES ('002', 'Maria Perez', '2025-11-01', 200.75);
```

---

Todo el código usado:

```
sudo mysql -u root -p

SHOW DATABASES;

USE empresadam;

SHOW TABLES;

INSERT INTO pedidos (numerodepedido, cliente) 
VALUES ('001','Juan Doe');

SELECT * FROM pedidos;

INSERT INTO pedidos (numerodepedido, cliente, fecha, precio)
VALUES ('002', 'Maria Perez', '2025-11-01', 200.75);

SELECT * FROM pedidos;
```

---

El valor NULL en bases de datos relacionales representa la ausencia de valor o el desconocimiento de un dato. No es lo mismo que un valor vacío o cero, ya que simplemente indica que no se ha proporcionado un valor para esa columna. En MySQL, cuando se insertan registros sin especificar valores para columnas que permiten NULL, MySQL asigna automáticamente este valor a esas columnas.

El modelo Entidad-Relación (ER) es la base del diseño de bases de datos relacionales.
Nos permite visualizar cómo las entidades (como un Cliente o Producto) interactúan entre sí mediante vínculos lógicos. En este ejercicio, implementaremos una arquitectura donde la integridad de los datos está garantizada por claves primarias (PK) y foráneas (FK), facilitando la gestión de la información en entornos intermodulares.

---

A partir del diagrama proporcionado, identificamos cuatro entidades clave y sus relaciones de cardinalidad.
- **Cliente - LineaPedido (1:n):** Un cliente puede realizar múltiples pedidos, pero cada pedido pertenece a un único cliente.
- **Pedido - LineaPedido (1:n):** Un pedido contiene múltiples líneas de detalle.
- **Producto - LineaPedido( 1:n):** Un producto puede aparecer en muchas líneas de pedido diferentes.

**SQL:**

La tabla `cliente` guarda los datos de las personas que compran. El campo id identifica a cada cliente de forma única y los campos `nombre`, `apellidos` y `email` almacenan su información básica.

```
CREATE TABLE cliente (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  apellidos VARCHAR(255),
  email VARCHAR(255)
);
```

La tabla `producto` almacena los artículos que se venden. Cada producto tiene un id único, un `nombre` y un `precio`, que en este caso está definido como texto.

```
CREATE TABLE producto (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  precio VARCHAR(255)
);
```

La tabla `pedido` representa las compras realizadas. Tiene un `id` único, una `fecha` y un `cliente_id` que indica qué cliente hizo el pedido. Este cliente_id es una clave foránea que obliga a que el cliente exista en la tabla `cliente`.

```
CREATE TABLE pedido (
  id INT PRIMARY KEY,
  fecha VARCHAR(255),
  cliente_id INT,
  CONSTRAINT fk_pedido_1 FOREIGN KEY (cliente_id) REFERENCES cliente(id)
);
```

La tabla `lineapedido` relaciona los pedidos con los productos. Cada registro indica qué producto pertenece a qué pedido mediante `pedido_id` y `producto_id`, que son claves foráneas hacia las tablas `pedido` y `producto`, asegurando la coherencia de los datos.

```
CREATE TABLE lineapedido (
  id INT PRIMARY KEY,
  pedido_id INT,
  producto_id INT,
  CONSTRAINT fk_lineapedido_1 FOREIGN KEY (pedido_id) REFERENCES pedido(id),
  CONSTRAINT fk_lineapedido_2 FOREIGN KEY (producto_id) REFERENCES producto(id)
);
```

**Python:**

Importamos las librerías necesarias.

```
from typing import Optional
```

Representamos a los Clientes.

```
class Cliente:
    def __init__(self, id: Optional[int] = None, nombre: Optional[str] = None, apellidos: Optional[str] = None, email: Optional[str] = None):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

    def __repr__(self):
        return f"Cliente(id={self.id!r}, nombre={self.nombre!r}, apellidos={self.apellidos!r}, email={self.email!r})"
```

Representamos los Pedidos y sus Líneas.

```
class Pedido:
    def __init__(self, id: Optional[int] = None, fecha: Optional[str] = None, cliente_id: Optional[int] = None):
        self.id = id
        self.fecha = fecha
        self.cliente_id = cliente_id

    def __repr__(self):
        return f"Pedido(id={self.id!r}, fecha={self.fecha!r}, cliente_id={self.cliente_id!r})"
        
class Lineapedido:
    def __init__(self, id: Optional[int] = None, pedido_id: Optional[int] = None, producto_id: Optional[int] = None):
        self.id = id
        self.pedido_id = pedido_id
        self.producto_id = producto_id

    def __repr__(self):
        return f"Lineapedido(id={self.id!r}, pedido_id={self.pedido_id!r}, producto_id={self.producto_id!r})"
```

Representamos el catálogo de Productos.

```
class Producto:
    def __init__(self, id: Optional[int] = None, nombre: Optional[str] = None, precio: Optional[str] = None):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f"Producto(id={self.id!r}, nombre={self.nombre!r}, precio={self.precio!r})"
```

---

Aquí está todo el código:

```
CREATE DATABASE tienda26;

USE tienda26;

-- Creamos la base de datos y sus tablas
CREATE TABLE cliente (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  apellidos VARCHAR(255),
  email VARCHAR(255)
);

CREATE TABLE producto (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  precio VARCHAR(255)
);

-- Añadimos las restricciones FK para asegurar la integridad
CREATE TABLE pedido (
  id INT PRIMARY KEY,
  fecha VARCHAR(255),
  cliente_id INT,
  CONSTRAINT fk_pedido_1 FOREIGN KEY (cliente_id) REFERENCES cliente(id)
);

CREATE TABLE lineapedido (
  id INT PRIMARY KEY,
  pedido_id INT,
  producto_id INT,
  CONSTRAINT fk_lineapedido_1 FOREIGN KEY (pedido_id) REFERENCES pedido(id),
  CONSTRAINT fk_lineapedido_2 FOREIGN KEY (producto_id) REFERENCES producto(id)
);

-- 20 CLIENTES
INSERT INTO cliente (id, nombre, apellidos, email) VALUES
(1, 'Ana', 'García López', 'ana.garcia@email.com'),
(2, 'Luis', 'Martínez Pérez', 'luis.martinez@email.com'),
(3, 'María', 'Sánchez Ruiz', 'maria.sanchez@email.com'),
(4, 'Carlos', 'Fernández Gómez', 'carlos.fernandez@email.com'),
(5, 'Laura', 'López Díaz', 'laura.lopez@email.com'),
(6, 'Pedro', 'Jiménez Torres', 'pedro.jimenez@email.com'),
(7, 'Lucía', 'Moreno Castro', 'lucia.moreno@email.com'),
(8, 'Javier', 'Romero Vega', 'javier.romero@email.com'),
(9, 'Elena', 'Navarro Ortiz', 'elena.navarro@email.com'),
(10, 'David', 'Ruiz Molina', 'david.ruiz@email.com'),
(11, 'Sofía', 'Serrano Ramos', 'sofia.serrano@email.com'),
(12, 'Pablo', 'Gil Herrera', 'pablo.gil@email.com'),
(13, 'Marta', 'Iglesias Cano', 'marta.iglesias@email.com'),
(14, 'Raúl', 'Medina Cruz', 'raul.medina@email.com'),
(15, 'Paula', 'Vargas León', 'paula.vargas@email.com'),
(16, 'Alberto', 'Reyes Flores', 'alberto.reyes@email.com'),
(17, 'Natalia', 'Prieto Núñez', 'natalia.prieto@email.com'),
(18, 'Sergio', 'Campos Soto', 'sergio.campos@email.com'),
(19, 'Cristina', 'Fuentes Pardo', 'cristina.fuentes@email.com'),
(20, 'Iván', 'Rojas Blanco', 'ivan.rojas@email.com');

-- 20 PRODUCTOS
INSERT INTO producto (id, nombre, precio) VALUES
(1,'Portátil','800'),
(2,'Ratón','20'),
(3,'Teclado','30'),
(4,'Monitor','200'),
(5,'Impresora','150'),
(6,'Tablet','300'),
(7,'Móvil','600'),
(8,'Auriculares','50'),
(9,'Altavoces','70'),
(10,'Webcam','40'),
(11,'Disco SSD','120'),
(12,'Memoria USB','15'),
(13,'Router','90'),
(14,'Silla','180'),
(15,'Mesa','250'),
(16,'Cargador','25'),
(17,'Cable HDMI','10'),
(18,'Microfono','85'),
(19,'Smartwatch','220'),
(20,'Proyector','400');

-- 20 PEDIDOS (cada uno asociado a un cliente existente)
INSERT INTO pedido (id, fecha, cliente_id) VALUES
(1,'2026-01-01',1),
(2,'2026-01-02',2),
(3,'2026-01-03',3),
(4,'2026-01-04',4),
(5,'2026-01-05',5),
(6,'2026-01-06',6),
(7,'2026-01-07',7),
(8,'2026-01-08',8),
(9,'2026-01-09',9),
(10,'2026-01-10',10),
(11,'2026-01-11',11),
(12,'2026-01-12',12),
(13,'2026-01-13',13),
(14,'2026-01-14',14),
(15,'2026-01-15',15),
(16,'2026-01-16',16),
(17,'2026-01-17',17),
(18,'2026-01-18',18),
(19,'2026-01-19',19),
(20,'2026-01-20',20);

-- 20 LÍNEAS DE PEDIDO (una por pedido y producto)
INSERT INTO lineapedido (id, pedido_id, producto_id) VALUES
(1,1,1),
(2,2,2),
(3,3,3),
(4,4,4),
(5,5,5),
(6,6,6),
(7,7,7),
(8,8,8),
(9,9,9),
(10,10,10),
(11,11,11),
(12,12,12),
(13,13,13),
(14,14,14),
(15,15,15),
(16,16,16),
(17,17,17),
(18,18,18),
(19,19,19),
(20,20,20);
```

```
from typing import Optional

# Representamos a los Clientes
class Cliente:
    def __init__(self, id: Optional[int] = None, nombre: Optional[str] = None, apellidos: Optional[str] = None, email: Optional[str] = None):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

    def __repr__(self):
        return f"Cliente(id={self.id!r}, nombre={self.nombre!r}, apellidos={self.apellidos!r}, email={self.email!r})"

# Representamos los Pedidos y sus Líneas
class Pedido:
    def __init__(self, id: Optional[int] = None, fecha: Optional[str] = None, cliente_id: Optional[int] = None):
        self.id = id
        self.fecha = fecha
        self.cliente_id = cliente_id

    def __repr__(self):
        return f"Pedido(id={self.id!r}, fecha={self.fecha!r}, cliente_id={self.cliente_id!r})"

class Lineapedido:
    def __init__(self, id: Optional[int] = None, pedido_id: Optional[int] = None, producto_id: Optional[int] = None):
        self.id = id
        self.pedido_id = pedido_id
        self.producto_id = producto_id

    def __repr__(self):
        return f"Lineapedido(id={self.id!r}, pedido_id={self.pedido_id!r}, producto_id={self.producto_id!r})"

# Representamos el catálogo de Productos
class Producto:
    def __init__(self, id: Optional[int] = None, nombre: Optional[str] = None, precio: Optional[str] = None):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f"Producto(id={self.id!r}, nombre={self.nombre!r}, precio={self.precio!r})"
```

---

Hemos comprobado que el diseño de un sistema informático comienza mucho antes de escribir la primera línea de código. Al enterder el diagrama ER, garantizamos que las tablas SQL y las clases Python compartan el mismo "idioma", evitando incoherencias en el futuro desarrollo de la aplicación. La correcta definición de las cardinalidades (1:1, 1:N o N:N) es lo que permite que nosotros podamos realizar consultas complejas mediante JOINs de forma eficiente.

Como nosotros somos responsables de la robustez del sistema, este procedimiento asegura que la base de datos no sea simplemente un almacén de texto, sino una representación virtual coherente de un negocio real.

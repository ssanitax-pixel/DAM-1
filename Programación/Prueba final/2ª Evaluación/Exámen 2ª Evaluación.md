## Bar Bara - Programación

Este proyecto consiste en el desarrollo de un sistema de gestión para un establecimiento de hostelería (Bar Bara), diseñado con una arquitectura que separa la lógica del servidor (Backend) de la interfaz de usuario (Frontend).

El objetivo es digitalizar el ciclo de servicio, desde que el cliente se registra hasta que solicita el pago en mesa.

---

**Arquitectura de la Web**

```
Directory structure:
└── ssanitax-bar_bara/
    ├── back/
    │   ├── index.php
    │   ├── listar_productos.php
    │   ├── peticion_login.php
    │   ├── peticion_pedido.php
    │   ├── controladores/
    │   │   ├── PedidoControlador.php
    │   │   ├── ProductoControlador.php
    │   │   └── UsuarioControlador.php
    │   ├── css/
    │   │   └── estilo.css
    │   └── inc/
    │       └── conexion_bd.php
    └── front/
        ├── carrito.php
        ├── catalogo.php
        ├── contacto.php
        ├── finalizacion.php
        ├── historial.php
        ├── index.php
        ├── login.php
        ├── logout.php
        ├── procesar_pedido.php
        ├── producto.php
        ├── registro.php
        ├── css/
        │   └── estilo.css
        ├── img/
        │   └── coctel.webp
        └── inc/
            ├── cabecera.php
            └── piedepagina.php
```

---

Voy a explicar la parte de programación del proyecto Bar Bara, archivo por archivo, que es como mejor se entiende lo que he aprendido.

Voy a explicar qué hace cada archivo, qué código he escrito y qué he aprendido en el proceso.

---

## BACKEND

### back/inc/conexion_bd.php

Este archivo sirve para conectarse a la base de datos. Es uno de los más importantes porque todos los demás lo usan.

```php
$pdo = new PDO("mysql:host=$host;dbname=$db;charset=$charset", $user, $pass, [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
]);
```

Aquí he aprendido a crear una conexión con PDO, a usar excepciones y a no repetir código usando `require_once`.

---

## back/controladores/ProductoControlador.php

En este archivo tengo una clase que se encarga de los productos.

```php
class ProductoControlador {
    private $db;

    public function __construct($conexion) {
        $this->db = $conexion;
    }

    public function listarTodo() {
        return $this->db->query("SELECT * FROM producto")->fetchAll();
    }
}
```

Aquí he aprendido a usar clases, constructores y métodos, y a separar la lógica del resto del código.

---

## back/controladores/UsuarioControlador.php

Este archivo se usa para el login de usuarios.

```php
if ($usuario && password_verify($password, $usuario['contrasena'])) {
    return $usuario;
}
```

He aprendido a comprobar contraseñas cifradas, a validar datos y a controlar el acceso de los usuarios.

---

## back/controladores/PedidoControlador.php

Este es el archivo más importante del proyecto porque gestiona los pedidos.

```php
public function crearNuevoPedido($datos) {
    // insertar pedido y productos
}
```

Aquí he aprendido a trabajar con arrays, a insertar datos relacionados y a controlar estados de los pedidos.

---

## back/index.php

Este archivo es el panel de control del bar.

```php
if (isset($_POST['entregar_id'])) {
    $pedidoCtrl->marcarComoEntregado($_POST['entregar_id']);
}
```

He aprendido a manejar formularios, condiciones y acciones desde el backend.

---

# FRONTEND

## front/catalogo.php

En este archivo se muestran los productos.

```php
$stmt = $pdo->query("SELECT * FROM producto");
```

Aquí he aprendido a recorrer resultados y a mostrar datos usando PHP.

---

## front/carrito.php

Este archivo gestiona el carrito usando sesiones.

```php
$_SESSION['carrito'][] = array(
    'id' => $producto['id'],
    'cantidad' => $cantidad
);
```

He aprendido qué son las sesiones, cómo guardar datos temporales y cómo calcular totales.

---

## front/procesar_pedido.php

Este archivo recoge los datos del pedido y los envía al backend.

He aprendido a usar `$_POST`, a comprobar datos y a vaciar el carrito.

---

## front/historial.php

Aquí el usuario puede ver sus pedidos y pedir la cuenta.

```php
UPDATE pedido SET pedir_cuenta = 'SI' WHERE usuario_id = ?
```

He aprendido a actualizar datos y a usar estados para controlar el flujo del pedido.

---

## Conclusión

Explicando el proyecto archivo por archivo se puede ver todo lo que he aprendido en programación. He pasado de no saber nada a poder crear una aplicación web completa usando PHP, sesiones y base de datos. Aún me queda mucho por aprender, pero este proyecto demuestra claramente mi evolución durante el curso.



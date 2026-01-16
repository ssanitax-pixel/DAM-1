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

```
<?php
$host = 'localhost';
$db   = 'Bar_Bara';
$user = 'admin_bara';
$pass = 'BarBara_2025$';
$charset = 'utf8mb4';

try {
     $pdo = new PDO("mysql:host=$host;dbname=$db;charset=$charset", $user, $pass, [
         PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
         PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
     ]);
} catch (PDOException $e) {
     die("Error de conexión: " . $e->getMessage());
}

header("Access-Control-Allow-Origin: *");
```

Aquí he aprendido a crear una conexión con PDO, a usar excepciones y a no repetir código usando `require_once`.

---

### back/controladores/ProductoControlador.php

En este archivo tengo una clase que se encarga de los productos.

```
<?php

class ProductoControlador {
    private $db;

    public function __construct($conexion) {
        $this->db = $conexion;
    }

    public function listarTodo() {
        // Obtenemos todos los campos: nombre, precio, descripción, categoria e imagen
        $sql = "SELECT * FROM producto";
        $stmt = $this->db->query($sql);
        return $stmt->fetchAll();
    }

    public function obtenerPorId($id) {
        $sql = "SELECT * FROM producto WHERE id = ?";
        $stmt = $this->db->prepare($sql);
        $stmt->execute([$id]);
        return $stmt->fetch();
    }
}
```

Aquí he aprendido a usar clases, constructores y métodos, y a separar la lógica del resto del código.

---

### back/controladores/UsuarioControlador.php

Este archivo se usa para el login de usuarios.

```
<?php

class UsuarioControlador {
    private $db;

    public function __construct($conexion) {
        $this->db = $conexion;
    }

    public function registrar($datos) {
        $passwordSegura = password_hash($datos['contrasea'], PASSWORD_BCRYPT);
        
        $sql = "INSERT INTO usuario (nombre_usuario, apellidos, correo, contrasea) VALUES (?, ?, ?, ?)";
        $stmt = $this->db->prepare($sql);
        return $stmt->execute([
            $datos['nombre_usuario'], 
            $datos['apellidos'], 
            $datos['correo'], 
            $passwordSegura
        ]);
    }

    public function login($correo, $password) {
        $sql = "SELECT * FROM usuario WHERE correo = ?";
        $stmt = $this->db->prepare($sql);
        $stmt->execute([$correo]);
        $usuario = $stmt->fetch();

        if ($usuario && password_verify($password, $usuario['contrasea'])) {
            return $usuario; // Login exitoso
        }
        return false;
    }
}
```

He aprendido a comprobar contraseñas cifradas, a validar datos y a controlar el acceso de los usuarios.

---

## back/controladores/PedidoControlador.php

Este es el archivo más importante del proyecto porque gestiona los pedidos.

```
<?php

class PedidoControlador {
    private $db;

    public function __construct($conexion) {
        $this->db = $conexion;
    }

    public function crearNuevoPedido($datos) {
        // El pedido nace con pedir_cuenta = 'NO' (Pendiente de servir)
        $sqlPedido = "INSERT INTO pedido (usuario_id, numero_mesa, fecha, hora, total, pedir_cuenta) 
                      VALUES (?, ?, CURDATE(), CURTIME(), ?, 'NO')";
        $stmt = $this->db->prepare($sqlPedido);
        $stmt->execute([
            $datos['usuario_id'], 
            $datos['numero_mesa'], 
            $datos['total']
        ]);
        $idPedido = $this->db->lastInsertId();

        foreach ($datos['productos'] as $item) {
            $sqlContenido = "INSERT INTO contenido_pedido (pedido_id, producto_id, cantidad, subtotal) 
                             VALUES (?, ?, ?, ?)";
            $stmtDetalle = $this->db->prepare($sqlContenido);
            $stmtDetalle->execute([
                $idPedido, 
                $item['producto_id'], 
                $item['cantidad'], 
                $item['subtotal']
            ]);
        }
        return $idPedido;
    }

    public function marcarComoEntregado($idPedido) {
        $sql = "UPDATE pedido 
            SET pedir_cuenta = CASE 
                WHEN pedir_cuenta = 'SI' THEN 'SI_ENTREGADO' 
                ELSE 'ENTREGADO' 
            END 
            WHERE id = ?";
    return $this->db->prepare($sql)->execute([$idPedido]);
    }

    public function solicitarCuenta($idPedido) {
        $sql = "UPDATE pedido SET pedir_cuenta = 'SI' WHERE id = ?";
        return $this->db->prepare($sql)->execute([$idPedido]);
    }

    public function marcarComoPagado($idPedido) {
        $sql = "UPDATE pedido SET pedir_cuenta = 'PAGADO' WHERE id = ?";
        return $this->db->prepare($sql)->execute([$idPedido]);
    }
}
```

Aquí he aprendido a trabajar con arrays, a insertar datos relacionados y a controlar estados de los pedidos.

---

### back/index.php

Este archivo es el panel de control del bar. Desde aquí se verán los pedidos que hay que entregar y cuando algún cliente pida la cuenta.

```
<?php
require_once 'inc/conexion_bd.php';
require_once 'controladores/PedidoControlador.php';
require_once 'controladores/ProductoControlador.php';

$pedidoCtrl = new PedidoControlador($pdo);
$productoCtrl = new ProductoControlador($pdo);

if (isset($_POST['entregar_id'])) {
    $pedidoCtrl->marcarComoEntregado($_POST['entregar_id']);
}

if (isset($_POST['cobrar_id'])) {
    $idPedido = $_POST['cobrar_id'];

    $sql = "UPDATE pedido SET pedir_cuenta = 'PAGADO' WHERE id = ?";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([$idPedido]);
}

try {
    $totalProductos = count($productoCtrl->listarTodo());
    
    $pendientes = $pdo->query("SELECT * FROM pedido WHERE pedir_cuenta IN ('NO', 'SI') ORDER BY hora ASC")->fetchAll();    
    $alertas = $pdo->query("SELECT * FROM pedido WHERE pedir_cuenta IN ('SI', 'SI_ENTREGADO') ORDER BY hora ASC")->fetchAll();
    
    $conteoAlertas = count($alertas);
} catch (Exception $e) {
    die("Error en la base de datos: " . $e->getMessage());
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Bar Bara - Panel Unificado</title>
    <link rel="stylesheet" href="css/estilo.css">
    <meta http-equiv="refresh" content="30">
    <style>
        .seccion { margin-bottom: 40px; }
        .titulo-seccion { padding: 10px; border-radius: 8px; margin-bottom: 20px; color: white; }
    </style>
</head>
<body>
    <nav>
        <div class="logo">🍴 BAR BARA - PANEL DE CONTROL</div>
        <div class="header-status">
            <code>PRODUCTOS: <?php echo $totalProductos; ?></code>
        </div>
    </nav>

    <div class="container">
        
        <div class="seccion">
            <h2 class="titulo-seccion" style="background: var(--error);">🔔 ALERTAS DE COBRO (<?php echo $conteoAlertas; ?>)</h2>
            <div class="grid-productos">
                <?php if (empty($alertas)): ?>
                    <div class="card"><h3>No hay mesas solicitando la cuenta.</h3></div>
                <?php else: ?>
                    <?php foreach($alertas as $a): ?>
                        <div class="card" style="border-left: 10px solid var(--error); text-align: left;"> 
                            <h2 style="margin:0">MESA <?php echo $a['numero_mesa']; ?></h2>
                            <p><strong>Total a cobrar: <?php echo $a['total']; ?>€</strong></p>
                            <p>Hora solicitud: <?php echo $a['hora']; ?></p>
                            
                            <form method="POST">
                                <input type="hidden" name="cobrar_id" value="<?php echo $a['id']; ?>">
                                <button type="submit" class="button" style="background: var(--exito); width:100%; border:none; cursor:pointer; margin-top:10px;">
                                    💰 MARCAR COMO COBRADO
                                </button>
                            </form>
                        </div>
                    <?php endforeach; ?>
                <?php endif; ?>
            </div>
        </div>

        <hr>

        <div class="seccion">
            <h2 class="titulo-seccion" style="background: var(--primario);">📥 COMANDAS POR SERVIR</h2>
            <div class="grid-productos">
                <?php if (empty($pendientes)): ?>
                    <div class="card"><h3>Cero comandas pendientes.</h3></div>
                <?php else: ?>
                   <?php foreach ($pendientes as $p): ?>
    <div class="card" style="border-left: 10px solid var(--primario); text-align: left;"> 
        
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <h2 style="margin:0">MESA <?php echo $p['numero_mesa']; ?></h2>
            <span style="background:#eee; padding:5px 10px; border-radius:5px; font-weight:bold;">
                <?php echo date('H:i', strtotime($p['hora'])); ?>
            </span>
        </div>

        <hr style="margin: 10px 0; border: 0; border-top: 1px dashed #ccc;">

        <ul style="padding-left: 20px; margin: 10px 0;">
            <?php 
            $sqlDetalles = "SELECT cp.cantidad, prod.nombre_producto 
                            FROM contenido_pedido cp 
                            JOIN producto prod ON cp.producto_id = prod.id 
                            WHERE cp.pedido_id = ?";
            
            $stmtDetalles = $pdo->prepare($sqlDetalles);
            $stmtDetalles->execute([$p['id']]);
            $detalles = $stmtDetalles->fetchAll();

            foreach($detalles as $d): ?>
                <li style="font-size: 1.1rem; margin-bottom: 5px;">
                    <strong><?php echo $d['cantidad']; ?>x</strong> 
                    <?php echo htmlspecialchars($d['nombre_producto']); ?>
                </li>
            <?php endforeach; ?>
        </ul>
        <p style="text-align: right; color: #666; font-size: 0.9rem;">Total: <?php echo $p['total']; ?>€</p>
        
        <form method="POST">
            <input type="hidden" name="entregar_id" value="<?php echo $p['id']; ?>">
            <button type="submit" class="button" style="background: var(--exito); width:100%; border:none; cursor:pointer;">
                ✅ MARCAR ENTREGADO
            </button>
        </form>
    </div>
<?php endforeach; ?>
                <?php endif; ?>
            </div>
        </div>
    </div>
</body>
</html>
```

He aprendido a manejar formularios, condiciones y acciones desde el backend.

---

## FRONTEND

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



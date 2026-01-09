Los métodos GET y POST son los protocolos que permiten enviar información desde un formulario HTML hacia un servidor.
- **GET:** Envía los datos a través de la URL del navegador. es útil para búsquedas o parámetros que pueden ser compartidos, pero no es seguro para datos sensibles.
- **POST:** Envía la información de forma oculta en el cuerpo de la petición HTTP. es el método estándar para insertar datos, como registros de usuarios o formularios de contacto, ya que ofrece mayor privacidad y no tiene límite de caracteres.

---

Creamos un formulario con el método GET.

```
<form action="?" method="GET">
```

Creamos un campo para el nombre y otro para los apellidos.

```
    <p>Nombre: <input type="text" name="nombre"></p>
```

Al pulsar el botón, los datos se añaden a la URL.

```
    <input type="submit" value="Enviar por GET">
```

Comprobación de datos recibidos por GET.

```
    if(isset($_GET['nombre']) && isset($_GET['apellidos'])){
```

Mostramos los datos recidos por GET.

```
        echo "<h3>Datos recibidos por GET:</h3>";
        echo "Nombre: " . $_GET['nombre'] . "<br>";
        echo "Apellidos: " . $_GET['apellidos'];
```

Ahora creamos un formulario con el método POST.

```
<form action="?" method="POST">
```

Creamos el campo para la pregunta y para la respuesta.

```
    <p>Pregunta: <input type="text" name="pregunta"></p>
```

Enviamos los datos, ahora están ocultos en la petición HTTP.

```
    <input type="submit" value="Enviar por GET">
```

Comprobamos los datos recibidos por POST.

```
    if(isset($_POST['pregunta']) && isset($_POST['respuesta'])){
```

Mostramos  datos.

```
        echo "<h3>Datos recibidos por POST:</h3>";
        echo "La pregunta es: " . $_POST['pregunta'] . "<br>";
        echo "La respuesta es: " . $_POST['respuesta'];
```

---

**Formulario de Usuario (Método GET)**

Este formulario envía el nombre y apellidos de forma visible en la URL.

```
<form action="?" method="GET">
    <p>Nombre: <input type="text" name="nombre"></p>
    <p>Apellidos: <input type="text" name="apellidos"></p>
    <input type="submit" value="Enviar por GET">
</form>

<?php
    if(isset($_GET['nombre']) && isset($_GET['apellidos'])){
        echo "<h3>Datos recibidos por GET:</h3>";
        echo "Nombre: " . $_GET['nombre'] . "<br>";
        echo "Apellidos: " . $_GET['apellidos'];
    }
?>
```

**Preguntas y Respuestas (Método POST)**

Este formulario envía la información de manera privada, ideal para sistemas de cuestionarios.

```
<form action="?" method="POST">
    <p>Pregunta: <input type="text" name="pregunta"></p>
    <p>Respuesta: <input type="text" name="respuesta"></p>
    <input type="submit" value="Enviar por POST">
</form>

<?php
    if(isset($_POST['pregunta']) && isset($_POST['respuesta'])){
        echo "<h3>Datos recibidos por POST:</h3>";
        echo "La pregunta es: " . $_POST['pregunta'] . "<br>";
        echo "La respuesta es: " . $_POST['respuesta'];
    }
?>
```

---

Hemos comprobado que la eleccion entre GET y POST afecta direcctamente a la seguridad y la experiencia de usuario. Mientras que GET permite al usuario guardar una búsqueda en "favoritos" al quedar registrada en la URL, POST es imprescindible cuando manejamos información que no debe ser expuesta o modificada fácilmente por terceros.

Este ejercicio refuerza el concepto de interactividad, permitiendo que nosotros, como desarrolladores, podamos crear aplicaciones de "escuchan" y responden a las acciones.

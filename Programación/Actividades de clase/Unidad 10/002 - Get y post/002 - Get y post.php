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

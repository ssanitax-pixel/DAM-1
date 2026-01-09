<?php
    /* 1. Creamos el array nombrado del cliente */
    $cliente = [];
    $cliente['nombre'] = "Ana";
    $cliente['apellidos'] = "Sánchez Suárez";
    $cliente['email'] = "ssanitax@gmail.com";

    /* 2. Convertimos el array a formato JSON */
    $json_datos = json_encode($cliente);

    /* 3. Guardamos la información en el disco */
    $archivo_escritura = fopen("clientes.json", "w");
    fwrite($archivo_escritura, $json_datos);
    fclose($archivo_escritura);
    
    echo "Información guardada con éxito.<br><br>";

    /* 4. Recuperamos y mostramos la información */
    if (file_exists("clientes.json")) {
        $archivo_lectura = fopen("clientes.json", "r");
        $contenido = fread($archivo_lectura, filesize("clientes.json"));
        fclose($archivo_lectura);

        echo "<h3>Datos recuperados del archivo:</h3>";
        echo $contenido;
    }
?>

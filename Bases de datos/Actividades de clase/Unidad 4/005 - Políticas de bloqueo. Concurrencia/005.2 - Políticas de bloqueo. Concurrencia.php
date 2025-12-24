<?php
    // Nosotros definimos el hash que estaría en la base de datos
    $hash_almacenado = md5("Hola"); 
    
    // Nosotros simulamos la entrada del usuario
    $entrada_usuario = "Hola";
    
    // Nosotros comparamos los hashes
    if(md5($entrada_usuario) == $hash_almacenado){
        echo "Las contraseñas coinciden"; // Devuelve true
    } else {
        echo "Las contraseñas no coinciden"; // Devuelve false
    }
?>

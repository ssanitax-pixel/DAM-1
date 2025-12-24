<?php
    /* Función para codificar 9 veces */
    function codificar($cadena){
        for($i = 0;$i<9;$i++){
            $cadena = base64_encode($cadena);
        }
        return $cadena;
    }

    /* Función para descodificar 9 veces */
    function descodificar($cadena){
        for($i = 0;$i<9;$i++){
            $cadena = base64_decode($cadena);
        }
        return $cadena;
    }

    $original = "contraseñasegura1234";
    $codificado = codificar($original);
    echo "Codificado: ".$codificado."<br>";

    $descodificado = descodificar($codificado);
    echo "Original: ".$descodificado;
?>

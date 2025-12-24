En este ejercicio, hemos repasado cómo el tratamiento de datos es vital para la seguridad en las bases de datos. Hemos aprendido a diferenciar entre la codificación, que es reversible y sirve para transformar datos para su transporte (como `base64`), y el hasheo (picadillo), que es una función de un solo sentido diseñada para proteger contraseñas.
Entender estos conceptos es clave para evitar ataques de fuerza bruta, donde un atacante intenta todas las convinaciones posibles de caracteres para encontrar una contraseña que coincida con un hash.

---

Usamos `base64_encode()` para transformar una cadena y `base64_decode()` para volver al original. Este método es útil para enviar datos que podrían romperse en el transporte, pero no es seguro para guardar contraseñas reales porque cualquiera puede descodificarlo.

```
$contrasena = "contraseñasegura1234";
$codificado = base64_encode($contrasena);
// Nosotros volvemos a la cadena original
$descodificado = base64_decode($codificado);
```

Aumentaremos la complejidad aplicando el proceso varias veces. En este ejercicio, nosotros creamos un bucle que codifica la cadena 9 veces y otra función que realiza el proceso inverso exactamente el mismo número de veces para recuperar el dato.

```
function codificar($cadena){
    for($i = 0;$i<9;$i++){
        $cadena = base64_encode($cadena);
    }
    return $cadena;
}
```

`md5()` sirve para generar un hash o picadillo. A diferencia de base64, nosotros no podemos "deshacer" un MD5; para comprobar una contraseña, nosotros debemos aplicar el mismo algoritmo a lo que introduce el usuario y comparar si los resultados coinciden.

```
$picadillo = md5("Hola"); // Nosotros obtenemos: f688ae26e9cfa3ba6235477831d5122e
```

--- 

El código completo quedará de la siguiente forma:

```
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
```

```
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
```

Hemos practicado la diferencia entre transformar datos (codificar) y protegerlos (hasear). Al aplicar funciones múltiples, nosotros vemos cómo los datos se vuelven más complejos, pero recordamos que esto no sustituye a un buen algoritmo de haseo como SHA1 o MD5.
Entender que las contraseñas nunca deben guardarse en texto plano es el primer paso para construir bases de datos seguras y profesionales.

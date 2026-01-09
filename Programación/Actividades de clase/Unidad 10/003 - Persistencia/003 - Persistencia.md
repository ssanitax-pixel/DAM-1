Utilizamos PHP para gestionar información que debe sobrevivir a una única sesión de usuario. En el desarrollo de aplicaciones empresariales, el concepto de Persistencia es vital: consiste en guardar el estado de los datos en un soporte físico (como un archivo de texto o JSON).

Para lograrlo, empleamos:

- Arrays Nombrados: A diferencia de los arrays numéricos, estos asocian una "clave" (como 'nombre') a un valor. Son ideales para representar entidades complejas como un cliente.

- `json_encode`: Función que traduce un array de PHP a una cadena de texto en formato JSON, legible por casi cualquier sistema.

- `fopen, fwrite y fread`: Funciones del sistema de archivos para abrir, escribir y leer datos en el disco.

---

Creamos un array, con los datos del cliente.

```
    $cliente = [];
    $cliente['nombre'] = "Ana";
    $cliente['apellidos'] = "Sánchez Suárez";
    $cliente['email'] = "ssanitax@gmail.com";
```

Convertimos el array en formato json.

```
    $json_datos = json_encode($cliente);
```

Guardamos la información en un archivo.

```
    $archivo_escritura = fopen("clientes.json", "w");
    fwrite($archivo_escritura, $json_datos);
    fclose($archivo_escritura);
```

Mostramos un mensaje corroborando que se ha guardado con éxito.

```
    echo "Información guardada con éxito.<br><br>";
```

Comprobamos que el archivo existe antes de intentar leerlo.


```
    if (file_exists("clientes.json")) {
```

Para poder abrir y cerrar el archivo pondremos lo siguiente.

```
        $archivo_lectura = fopen("clientes.json", "r");
        $contenido = fread($archivo_lectura, filesize("clientes.json"));
        fclose($archivo_lectura);
```

Mostramos el contenido.

```
        echo "<h3>Datos recuperados del archivo:</h3>";
        echo $contenido;
```

---

El código completo se verá así:

```
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
```

---

Hemos comprobado que conbinar la flexibilidad de los arrays con la universalidad de los archivos JSON nos permite crear sistemas de almacenamiento sencillos pero potentes. Este ejercicio se relaciona directamente con la unidad al enseñarnos que un servidor no solo muestra datos, sino que también tiene la capacidad de recordar información mediante la escritura de archivos.

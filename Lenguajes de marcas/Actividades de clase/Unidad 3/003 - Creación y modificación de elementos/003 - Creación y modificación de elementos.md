La manipulación dinámica del DOM es un pilar importantísimo en el desarrollo web moderno. En este ejercicio, nos enfocamos en la transición de una web estática a una aplicación reactiva mendiante el uso de la API `fetch`. Esta tecnología nos permite realizar peticiones para obtener datos en JSON, el estándar de intercambio de información más utilizado actualmente.

---

Empezamos creando la estructura básica de HTML.

```
<!doctype html>
<html lang="es">
    <head>
    </head>
    <body>
    </body>
</html>
```

Dentro de `<head>` meteremos el estilo que queremos que tenga la tabla.

```
    <style>
        /* Estructura base inspirada en vuestro estilo de diseño */
        html, body { height: 100%; padding: 0px; margin: 0px; display: flex; width: 100%; font-family: Arial, sans-serif; }
        nav { background: RebeccaPurple; flex: 1; color: white; padding: 20px; display: flex; flex-direction: column; gap: 20px; }
        main { flex: 4; background: MediumPurple; padding: 20px; overflow-y: auto; }

        /* Estilo de interactividad para los botones */
        nav button { border: none; background: white; color: indigo; padding: 15px; text-transform: uppercase; cursor: pointer; transition: 0.3s; }
        nav button:hover { background: #e0e0e0; transform: scale(1.02); }

        /* Diseño de la tabla con bordes y colores específicos */
        table { border: 3px solid orchid; border-collapse: collapse; background: white; width: 100%; margin-top: 20px; }
        table tr:first-child { background: mediumorchid; color: white; }
        table tr td { padding: 12px; border: 1px solid orchid; text-align: center; }
    </style>
```

A parte también pondremos el meta y el titulo.

```
    <meta charset="utf-8">
    <title>Panel de Gestión - DAM-1</title>
```

Ahora vamos a empezar con la parte de JavaScript. Que lo meteremos dentro de `<body>`.

```
<!doctype html>
<html lang="es">
    <head>
    </head>
    <body>
        <script>
        </script>
    </body>
</html>
```

Para empezar a cargar el menú, le diremos al navegador que busque el archivo `botones.json`, que tendremos que haber creado con anterioridad.

```
fetch("botones.json")
```

Convertimos el texto recibido en un array.

```
.then(function(respuesta){
    return respuesta.json();
})
```

Seleccionamos el `<nav>` por su `id`.

```
let contenedorMenu = document.querySelector("#menu_navegacion");
```

Recorremos cada texto del array.

```
datos.forEach(function(nombre_boton){
```

Creamos un botón que ponga el texto del JSON.

```
let boton = document.createElement("button");
boton.textContent = nombre_boton;
```

Cuando hagamos click, escribirá en consola y llama a la función que carga la tabla.

```
boton.onclick = function(){
    console.log("Cargando sección: " + nombre_boton);
    ejecutarCargaTabla();
};
```

Insertamos el botón en el `<nav>`.

```
contenedorMenu.appendChild(boton);
```

Cargamos la tabla solo cuando se haga click.

```
function ejecutarCargaTabla() {
```

Que cargará otro archivo JSON con los datos, también introducidos anteriormente.

```
fetch("tabla.json")
```

Borramos lo anterior y escribimos un título nuevo.


```
contenedorMain.innerHTML = "<h3>Vista de Datos Actualizada</h3>";
```

Creamos una tabla en memoria.


```
let tabla = document.createElement("table");
```

Cada `línea` es una fila.

```
datos_tabla.forEach(function(linea){
```

Cada `celda_info` es una celda.

```
linea.forEach(function(celda_info){
```

Creamos una celda y le ponemos el texto.

```
let celda = document.createElement("td");
celda.textContent = celda_info;
```

Finalmente, la tabla aparecerá en pantalla.

```
contenedorMain.appendChild(tabla);
```

---

El código acabado:

```
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>Panel de Gestión - DAM-1</title>
    <style>
        /* Estructura base inspirada en vuestro estilo de diseño */
        html, body { height: 100%; padding: 0px; margin: 0px; display: flex; width: 100%; font-family: Arial, sans-serif; }
        nav { background: RebeccaPurple; flex: 1; color: white; padding: 20px; display: flex; flex-direction: column; gap: 20px; }
        main { flex: 4; background: MediumPurple; padding: 20px; overflow-y: auto; }

        /* Estilo de interactividad para los botones */
        nav button { border: none; background: white; color: indigo; padding: 15px; text-transform: uppercase; cursor: pointer; transition: 0.3s; }
        nav button:hover { background: #e0e0e0; transform: scale(1.02); }

        /* Diseño de la tabla con bordes y colores específicos */
        table { border: 3px solid orchid; border-collapse: collapse; background: white; width: 100%; margin-top: 20px; }
        table tr:first-child { background: mediumorchid; color: white; }
        table tr td { padding: 12px; border: 1px solid orchid; text-align: center; }
    </style>
</head>
<body>
    <nav id="menu_navegacion">ssanitax | panel</nav>
    <main id="area_contenido">Contenido del panel de administración</main>

    <script>
        // Primer paso: Carga dinámica del menú desde botones.json
        fetch("botones.json")
        .then(function(respuesta){
            return respuesta.json(); // Transformamos la respuesta en objeto usable
        })
        .then(function(datos){
            let contenedorMenu = document.querySelector("#menu_navegacion");
            
            datos.forEach(function(nombre_boton){
                // Creamos el botón dinámicamente
                let boton = document.createElement("button");
                boton.textContent = nombre_boton;
                
                // Asignamos el evento click solicitado
                boton.onclick = function(){
                    console.log("Cargando sección: " + nombre_boton);
                    ejecutarCargaTabla();
                };
                
                contenedorMenu.appendChild(boton);
            });
        });

        // Segundo paso: Función para generar la tabla de datos
        function ejecutarCargaTabla() {
            fetch("tabla.json")
            .then(function(respuesta){
                return respuesta.json();
            })
            .then(function(datos_tabla){
                let contenedorMain = document.querySelector("#area_contenido");
                contenedorMain.innerHTML = "<h3>Vista de Datos Actualizada</h3>"; // Limpiamos pantalla
                
                let tabla = document.createElement("table");
                
                // Construcción de filas y celdas
                datos_tabla.forEach(function(linea){
                    let fila = document.createElement("tr");
                    
                    linea.forEach(function(celda_info){
                        let celda = document.createElement("td");
                        celda.textContent = celda_info;
                        fila.appendChild(celda);
                    });
                    
                    tabla.appendChild(fila);
                });
                
                contenedorMain.appendChild(tabla);
            });
        }
    </script>
</body>
</html>
```

---

La implementación de este sistema de carga dinámica no solo optimiza rendimiento al evitar recargas innecesarias, sino que también establece las bases para la integración con el módulo de Bases de datos.

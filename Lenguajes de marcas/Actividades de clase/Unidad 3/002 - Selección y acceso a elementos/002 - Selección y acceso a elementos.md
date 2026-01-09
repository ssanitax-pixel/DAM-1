La selección y el acceso a elementos es la base de la interactividad en la web. JavaScript utiliza el objeto `document` para conectar con el HTML. Mediante métodos como `querySelector`, nosotros podemos apuntar etiquetas, IDs o clases y realizar cambios en tiempo real sin necesitad de recargar la página.

---

Para la lectura y selección de elementos utilizaremos `document.querySelector()` para identificar un elemento. Una vez seleccionado, accedemos a su propiedad `textContent` para leer el texto plano que contiene.

```
// Seleccionamos la etiqueta p
const elemento = document.querySelector("p");
// Escribimos el contenido en la consola para verificarlo
console.log(elemento.textContent);
```

Para la escritura de contenido , es decir, modificar lo que el usuario ve, seleccionaremos el elemento mediante su ID usando el símbolo # y asignaremos un nuevo valor a `textContent`.

```
// Cambiamos el texto de los divs por ID
document.querySelector("#rojo").textContent = "texto rojo";
document.querySelector("#verde").textContent = "texto verde";
document.querySelector("#azul").textContent = "texto azul";
```

Si necesitamos que JavaScript no solo escriba texto, sino que cree también etiquetas nuevas, como por ejemplo un encabezado, utilizamos la propiedad `innerHTML`.

```
// Insertamos una etiqueta h1 completa dentro del div
document.querySelector("div").innerHTML = "<h1>Hola</h1>";
```

Cuando tenemos una lista de datos (array), utilizamos un bucle `for` para recorrerlos e insertarlos uno a uno dentro de un contenedor, como la sección `<main>`.

```
const articulos = ["Primer artículo", "Segundo artículo", "Tercer artículo"];
const contenedor = document.querySelector("main");

for(let i = 0; i < articulos.length; i++) {
    // Usamos += para ir sumando cada artículo al contenido anterior
    contenedor.innerHTML += "<h3>" + articulos[i] + "</h3>";
}
```

---

El código quedará tal que así:

```
<!doctype html>
<html lang="es">
<head>
    <title>Práctica Selección y Acceso</title>
    <meta charset="utf-8">
    <style>
        #rojo{color:red;} #verde{color:green;} #azul{color:blue;}
        main{ border-top: 1px solid #ccc; margin-top: 20px; padding: 10px; }
    </style>
</head>
<body>
    <p>Lectura de párrafo inicial.</p>
    
    <div id="rojo"></div>
    <div id="verde"></div>
    <div id="azul"></div>

    <div id="dinamico"></div>

    <main></main>

    <script>
        // 1. Lectura del párrafo
        const parrafo = document.querySelector("p");
        console.log("Contenido leído: " + parrafo.textContent);

        // 2. Escritura de texto en IDs
        document.querySelector("#rojo").textContent = "texto rojo";
        document.querySelector("#verde").textContent = "texto verde";
        document.querySelector("#azul").textContent = "texto azul";

        // 3. Inserción de HTML dinámico
        document.querySelector("#dinamico").innerHTML = "<h1>Hola</h1>";

        // 4. Microblogging con array y bucle
        const articulos = ["Primer artículo", "Segundo artículo", "Tercer artículo"];
        const contenedor = document.querySelector("main");
        
        for(let i = 0; i < articulos.length; i++){
            contenedor.innerHTML += "<h3>" + articulos[i] + "</h3>";
        }
    </script>
</body>
</html>
```

---

En este ejercicio hemos comprobado que dominar `querySelector` y `innerHTML` nos permite transformar una página estática en una dinámica. Es muy útil para crear aplicaciones reales como blogs, paneles de control o validacines de formularios que respondan al instante.

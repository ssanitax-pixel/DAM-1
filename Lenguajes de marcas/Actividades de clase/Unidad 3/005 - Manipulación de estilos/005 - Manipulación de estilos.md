La manipulación de estilos permite que nuestras páginas web dejen de ser estáticas para responder al comportamiento del usuario. Podemos cambiar la apariencia de un elemento de tres formas principales:
- Estilos directos: Modificando la propiedad `.style` en JavaScript.
- Gestión de clases: Añadiendo o quitando clases CSS con `.classList`.
- CSS dinámico: Utilizando variables y funciones de cálculo directamente en la hoja de estilos.

---

Vamos a explicar el funcionamiento de cada uno de los ejercicios propuestos.

1. Estilo condicional.

Seleccionamos el campo de entrada y usamos el evento `onkeyup`. Dentro de la función, comprobamos la longitud del texto con `.length`. Si es exactamente 9, cambiamos las clases del elemento para que pase de rojo a verde.

```
let entrada = document.querySelector("input");
entrada.onkeyup = function(){
    let longitud = this.value.length;
    if(longitud == 9){
        this.classList.add("verde");
        this.classList.remove("rojo");
    } else {
        this.classList.add("rojo");
        this.classList.remove("verde");
    }
}
```

2. Estilo directo y Gestión de clases.

Podemos cambiar el color de un párrafo con `parrafo.style.color = "blue"`. Sin embargo, es mejor el uso de clases para mantener el código ordenado, utilizando `classList.add()` para aplicar estilos y `classList.remove()` para quitarlos.

3. Variables y Cálculos en CSS.

Definimos variables en el bloque `:root` para poder reutilizar colores o tamaños en todo el documento. Además la función `calc()` nos permite mezclar unidades para que el diseño sea más flexible.

```
:root { --color_primario: #0000ff; } /* Nosotros cambiamos a azul */
div { width: calc(50% + 150px); }    /* Nosotros variamos el cálculo */
```

---

Así queda el código integrado que resuelve los puntos clave de la actividad:

```
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>Práctica de Estilos Dinámicos - DAM</title>
    <style>
        /* Ejercicio 5: Variables en CSS */
        :root {
            --color_primario: #0000ff; /* Definimos el azul global */
        }

        /* Ejercicio 6: Función de cálculo */
        .contenedor {
            width: calc(50% + 150px); /* Ajustamos el ancho dinámico */
            height: 50px;
            background: lightgrey;
            margin-bottom: 20px;
        }

        /* Ejercicio 4: Clases para validación */
        .rojo { background: rgb(255,200,200); border: 2px solid red; }
        .verde { background: rgb(200,255,200); border: 2px solid green; }
        
        .morado { color: purple; font-weight: bold; }
    </style>
</head>
<body>

    <p id="texto-estilo">Este texto cambiará de color mediante JavaScript.</p>
    
    <div class="contenedor">Caja con calc()</div>

    <label>Introduce 9 caracteres:</label>
    <input type="text" class="rojo" id="validador">

    <script>
        // --- Ejercicio 1: Estilo directo ---
        let parrafo = document.querySelector("#texto-estilo");
        parrafo.style.color = "blue"; // Cambiamos el color a azul directamente

        // --- Ejercicio 2 y 3: Añadir y quitar clases ---
        parrafo.classList.add("morado");
        // parrafo.classList.remove("morado"); // Podríamos quitarla así

        // --- Ejercicio 4: Estilo condicional ---
        let entrada = document.querySelector("#validador");
        entrada.onkeyup = function() {
            if(this.value.length == 9) {
                this.classList.add("verde");
                this.classList.remove("rojo");
            } else {
                this.classList.add("rojo");
                this.classList.remove("verde");
            }
        }
    </script>
</body>
</html>
```

---

Hemos comprobado que la manipulación de estilos es una herramienta poderosa para mejorar la experiencia del usuario (UX). Al validar un campo de texto visualmente o usar variables globales, creamos interfaces más intuitivas y fáciles de mantener.
Entender cómo JavaScript interactúa con las clases de CSS nos permite preparar el terreno para proyectos más complejos, como paneles de administración reactivos o juegos sencillos en el navegador.

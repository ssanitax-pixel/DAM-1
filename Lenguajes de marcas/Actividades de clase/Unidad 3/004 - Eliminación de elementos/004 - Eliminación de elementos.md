En este ejercicio vemos que en una página web no todo es para siempre. Con JavaScript, igual que podemos crear cosas con `createElement`, también podemos borrarlas. Esto es muy útil porque si un usuario quiere quitar una fila de una tabla o si estamos haciendo un juego donde desaparecen enemigos, necesitamos el método `.remove()`. Básicamente, pasamos de una web que solo muestra información a una donde el usuario puede limpiar o modificar lo ve que en pantalla.

---

Empezamos con la estructura HTML que hay en la página.
La tabla está vacía en el HTML, ya que se rellenará con JavaScript.

```
<h1>Ejercicio de eliminar filas (Haz click en una)</h1>
<table id="miTabla"></table>
<div id="jugador"></div>
```

Creamos el estilo general.

```
body {
  font-family: arial;
  background: GhostWhite;
}
```

El de la tabla.

```
tr:hover {
  background: #f9f0ff;
}
```

El del jugador.

```
#jugador {
  width: 40px;
  height: 40px;
  position: absolute;
  transition: all 1s;
}
```

Ahora empezaremos con la parte de JavaScript.
Seleccionamos la tabla por su `id`.

```
let miTabla = document.querySelector("#miTabla");
```

Creamos una fila nueva en memoria.

```
let nuevaFila = document.createElement("tr");
```

Añadimos tres celdas. Y hacemos que empiece en 1, no en 0.

```
nuevaFila.innerHTML = "<td>Fila num " + (i+1) + "</td><td>Dato A</td><td>Dato B</td>";
```

Creamos el evento click, que hará lo siguiente, cuando hagamos click, la fila clicada se eliminará.

```
nuevaFila.onclick = function(){
    this.remove();
};
```

Insertamos la fila en la tabla.

```
miTabla.appendChild(nuevaFila);
```

Ahora nos vamos a la parte del minijuego.
Creamos una variable llamada temporizador.

```
let temporizador;
```

Creamos la función que se encargará de mover el cuadrado rojo.

```
function moverJugador(){
```

Seleccionamos el div rojo.

```
let personaje = document.querySelector("#jugador");
```

Hacemos que tenga una posición aleatoria.

```
let x = Math.random() * (window.innerWidth - 50);
let y = Math.random() * (window.innerHeight - 50);
```

Moveremos el div usando CSS.

```
personaje.style.left = x + "px";
personaje.style.top = y + "px";
```

Creamos un bucle infinito con temporizador.

```
clearTimeout(temporizador);
temporizador = setTimeout(moverJugador, 1000);
```

Arrancamos el minijuego.

```
moverJugador();
```

---

Código:

```
<!doctype html>
<html lang="es">
<head>
    <title>Práctica de Eliminación - Ana Sánchez</title>
    <meta charset="utf-8">
    <style>
        /* Estilos parecidos a los que usamos en el CV y Portfolio */
        body { font-family: arial; background: GhostWhite; padding: 20px; }
        
        /* Estilo para la tabla de la actividad */
        table { border: 2px solid indigo; background: white; width: 100%; cursor: pointer; }
        td { border: 1px solid mediumorchid; padding: 8px; text-align: center; }
        tr:hover { background: #f9f0ff; } /* Para que se sepa que puedes clicar */

        /* El cuadrado del minijuego */
        #jugador { 
            width: 40px; 
            height: 40px; 
            background: red; 
            position: absolute; 
            transition: all 1s; /* Para que el movimiento no sea a saltos */
            border: 2px solid black;
        }
    </style>
</head>
<body>

    <h1>Ejercicio de eliminar filas (Haz click en una)</h1>
    <table id="miTabla">
        </table>

    <div id="jugador"></div>

    <script>
        // --- PARTE 1: TABLA INTERACTIVA ---
        let miTabla = document.querySelector("#miTabla");

        for(let i = 0; i < 20; i++){
            let nuevaFila = document.createElement("tr");
            nuevaFila.innerHTML = "<td>Fila num " + (i+1) + "</td><td>Dato A</td><td>Dato B</td>";
            
            // Cuando clicamos, la fila desaparece
            nuevaFila.onclick = function(){
                this.remove();
            };
            
            miTabla.appendChild(nuevaFila);
        }

        // --- PARTE 2: MINIJUEGO ---
        let temporizador;
        
        function moverJugador(){
            let personaje = document.querySelector("#jugador");
            
            // Calculamos posición al azar restando un poco para que no se salga
            let x = Math.random() * (window.innerWidth - 50);
            let y = Math.random() * (window.innerHeight - 50);
            
            personaje.style.left = x + "px";
            personaje.style.top = y + "px";
            
            // Limpiamos y volvemos a llamar para que sea un bucle
            clearTimeout(temporizador);
            temporizador = setTimeout(moverJugador, 1000);
        }

        // Lanzamos el movimiento
        moverJugador();
    </script>
</body>
</html>
```

---

Este ejercicio nos ha servido para ver cómo podemos "limpiar" el HTML sobre la marcha. Es muy parecido a lo que hacíamos con los formularios de la Unidad 2, pero ahora con JavaScript podemos hacer que la página responda al momento sin recargar. Entender bien el `this.remove()` y los bucles nos va a venir genial para cuando empecemos a conectar esto con las Bases de Datos y tengamos que borrar registros de verdad.

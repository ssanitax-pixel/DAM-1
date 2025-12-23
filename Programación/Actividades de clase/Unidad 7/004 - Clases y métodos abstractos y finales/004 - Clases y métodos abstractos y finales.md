En este ejercicio se hemos trabajado la aplicación de transformaciones y rotaciones utilizando HTML, CSS y JavaScript, centrándonos especialmente en el uso del elemento `canvas` y la propiedad `transform` de CSS. A lo largo de la práctica hemos aplicado conceptos matemáticos básicos, como el uso del seno y el coseno, para representar movimientos circulares y rotaciones en pantalla. Además, hemos reforzado el uso del bucle temporal mediante `setTimeout`, permitiendo la actualización constante de los elementos gráficos. Todo esto permite comprender cómo se combinan el diseño visual con la lógica de programación para crear animaciones dinámicas en el navegador.

---

Empezamos creando un documento HTML estándar.
Esto define la estructura mínima que el navegador necesita para interpretar el archivo.

```
<!doctype html>
<html>
```

Dentro del `<head>` definimos los estilos visuales que afectan a la página y al reloj.

```
<head>
  <style>
```

Aplicamos un color rojo al fondo de la ventana usando `backgroung-color`. También usamos flexbox para centrar el reloj en la pantalla.

```
body{
  background-color: red;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}
```

Aplicamos una transformación CSS al elemento `canvas`.

```
canvas{
  background: white;
  transform: rotate(45deg);
}
```

Cerramos bloque de estilos.

```
  </style>
</head>
```

Dentro del `<body>` colocamos el elemento `<canvas>`, que será donde dibujemos el reloj.

```
<body>
  <canvas></canvas>
```

Entramos en la parte lógica del programa.

```
<script>
```

Creamos un temporizador que llama al bucle cada segundo. Esto permite actualizar el reloj continuamente.

```
let temporizador = setTimeout(bucle,1000);
```

Capturamos el canvas y definimos su tamaño.

```
let lienzo = document.querySelector("canvas");
lienzo.width = 512;
lienzo.height = 512;
```

Después obtenemos el contexto en 2D para poder dibujar.

```
let contexto = lienzo.getContext("2d");
contexto.lineCap = "round";
```

Definimos la función que se ejecutará cada segundo.

```
function bucle(){
```

Creamos un objeto `Date` para conocer la hora actual.

```
let fecha = new Date();
```

Extraemos horas, minutos y segundos.

```
let hora = fecha.getHours();
let minuto = fecha.getMinutes();
let segundo = fecha.getSeconds();
```

Antes de volver a dibujar, borramos el contenido anterior. Esto evita que las manecillas se superpongan.

```
contexto.clearRect(0,0,512,512);
```

Para dibujar la manecilla de las horas.
Configuramos el estilo de la línea.

```
contexto.lineWidth = 45;
contexto.strokeStyle = "blue";
```

Convertimos la hora en radianes.

```
let angulo_hora = hora*(Math.PI*2/12)-Math.PI/2;
```

Dibujamos la línea desde el centro.

```
contexto.beginPath();
contexto.moveTo(256,256);
contexto.lineTo(
  256+Math.cos(angulo_hora)*100,
  256+Math.sin(angulo_hora)*100
);
contexto.stroke();
```

Para la manecilla de los minutos.
Repetimos el proceso con otro tamaño y color.

```
contexto.lineWidth = 25;
contexto.strokeStyle = "green";
let angulo_minuto = minuto*(Math.PI*2/60)-Math.PI/2;
```

Y la dibujamos.

```
contexto.beginPath();
contexto.moveTo(256,256);
contexto.lineTo(
  256+Math.cos(angulo_minuto)*150,
  256+Math.sin(angulo_minuto)*150
);
contexto.stroke();
```

Ahora la manecilla de los segundos.
La más fina y larga.

```
contexto.lineWidth = 5;
contexto.strokeStyle = "red";
let angulo_segundo = segundo*(Math.PI*2/60)-Math.PI/2;
```

```
contexto.beginPath();
contexto.moveTo(256,256);
contexto.lineTo(
  256+Math.cos(angulo_segundo)*200,
  256+Math.sin(angulo_segundo)*200
);
contexto.stroke();
```

Para el círculo central del reloj.
Dibujamos un círculo en el centro.

```
contexto.beginPath();
contexto.arc(256,256,50,0,Math.PI*2);
contexto.fill();
```

Ahora para el borde exterior del reloj.
Creamos el marco circular.

```
contexto.lineWidth = 25;
contexto.strokeStyle = "black";
contexto.beginPath();
contexto.arc(256,256,200,0,Math.PI*2);
contexto.stroke();
```

Reiniciamos el temporizador para que el reloj siga funcionando.

```
clearTimeout(temporizador);
temporizador = setTimeout(bucle,1000);
```

Cerramos la función y el script.

```
}
</script>
```

Finalmente, cerramos el documento.

```
</body>
</html>
```

---

El código completo quedará así:

```
<!doctype html>
<html>
  <head>
    <style>
      body{
        background-color: red;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
      }
      canvas{
        background: white;
        transform: rotate(45deg);
      }
    </style>
  </head>
  <body>
    <canvas></canvas>

    <script>
      let temporizador = setTimeout(bucle,1000);
      let lienzo = document.querySelector("canvas");
      lienzo.width = 512;
      lienzo.height = 512;
      let contexto = lienzo.getContext("2d");
      contexto.lineCap = "round";

      function bucle(){
        let fecha = new Date();

        let hora = fecha.getHours();
        let minuto = fecha.getMinutes();
        let segundo = fecha.getSeconds();

        contexto.clearRect(0,0,512,512);

        // Manecilla horas
        contexto.lineWidth = 45;
        contexto.strokeStyle = "blue";
        let angulo_hora = hora*(Math.PI*2/12)-Math.PI/2;
        contexto.beginPath();
        contexto.moveTo(256,256);
        contexto.lineTo(
          256+Math.cos(angulo_hora)*100,
          256+Math.sin(angulo_hora)*100
        );
        contexto.stroke();

        // Manecilla minutos
        contexto.lineWidth = 25;
        contexto.strokeStyle = "green";
        let angulo_minuto = minuto*(Math.PI*2/60)-Math.PI/2;
        contexto.beginPath();
        contexto.moveTo(256,256);
        contexto.lineTo(
          256+Math.cos(angulo_minuto)*150,
          256+Math.sin(angulo_minuto)*150
        );
        contexto.stroke();

        // Manecilla segundos
        contexto.lineWidth = 5;
        contexto.strokeStyle = "red";
        let angulo_segundo = segundo*(Math.PI*2/60)-Math.PI/2;
        contexto.beginPath();
        contexto.moveTo(256,256);
        contexto.lineTo(
          256+Math.cos(angulo_segundo)*200,
          256+Math.sin(angulo_segundo)*200
        );
        contexto.stroke();

        // Centro
        contexto.beginPath();
        contexto.arc(256,256,50,0,Math.PI*2);
        contexto.fill();

        // Borde
        contexto.lineWidth = 25;
        contexto.strokeStyle = "black";
        contexto.beginPath();
        contexto.arc(256,256,200,0,Math.PI*2);
        contexto.stroke();

        clearTimeout(temporizador);
        temporizador = setTimeout(bucle,1000);
      }
    </script>
  </body>
</html>
```

---

Como resultado del ejercicio, se ha implementado un reloj analógico funcional que se actualiza en tiempo real utilizando JavaScript y el objeto `Date`. Se han dibujado correctamente las manecillas de horas, minutos y segundos sobre un `canvas`, respetando sus proporciones y posiciones. Mediante CSS se ha modificado el fondo de la ventana y se ha aplicado una rotación de 45 grados al reloj, manteniendo su coherencia visual. Esta práctica ha permitido consolidar el uso de transformaciones CSS, el dibujo en canvas y la aplicación de lógica matemática para representar rotaciones y movimientos, demostrando cómo estas tecnologías pueden trabajar conjuntamente para crear elementos interactivos y visualmente consistentes.

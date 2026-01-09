En este ejercicio hemos aplicado la teoría de jerarquías de clases en JavaScript para simular un pequeño entorno interactivo. Creamos una clase base llamada `Entidad`, que sirve como “madre” para todas las demás clases y contiene propiedades comunes como `posx`, `posy`, `angulo` y `velocidad`. A partir de esta clase, definimos subclases como `Jugador`, `Bala` y `Roca`, que heredan las propiedades de `Entidad` y añaden características específicas según su comportamiento.

Esto nos permite reutilizar código y organizar mejor nuestra lógica, haciendo que cada objeto pueda moverse, rotar y actualizarse de forma independiente. También vimos cómo interactuar con el HTML y CSS, posicionando elementos en la pantalla y usando eventos de teclado para mover la nave y disparar balas.

---

Creamos la estructura de la página:

```
<!doctype html>
<html>
  <head>
    <style>
      #nave{position:absolute;width:50px;}
      .roca{width:50px;}
      .bala{width:20px;}
      body{background:url("estrellas.jpeg");background-size:cover;}
    </style>
  </head>
  <body>
    <img src="nave.png" id="nave">
  </body>
</html>

```

Definimos la clase base `Entidad` como la madre de todas las demás del juego. Entidad es la clase que almacena las propiedades comunes de jugador, bala, y roca.

```
class Entidad {
  constructor(x, y, a, v){
    this.posx = x;       // Posición horizontal
    this.posy = y;       // Posición vertical
    this.angulo = a;     // Ángulo de rotación
    this.velocidad = v;  // Velocidad de movimiento
  }
}
```

Definimos la clase `Jugador` heredando de `Entidad`.

```
class Jugador extends Entidad {
  constructor(x, y, a, v){
    super(x, y, a, v); // Llamamos al constructor de la clase madre
  }
}
```

Definimos la clase `Bala` heredando de `Entidad`.

```
class Bala extends Entidad {
  constructor(x, y, a, v){
    super(x, y, a, v);
  }
}
```

Definimos la clase `Roca` heredando de `Entidad`. También tendrá `escala` como algo propio.

```
class Roca extends Entidad {
  constructor(x, y, a, e, v){
    super(x, y, a, v); // Llamamos al constructor de Entidad
    this.escala = e;   // Tamaño de la roca
  }
}
```

Creamos las rocas y las mostramos en pantalla.

```
let numero_rocas = 10;
let rocas = [];

for(let i = 0; i < numero_rocas; i++){
  let roca = new Roca(Math.random()*500, Math.random()*500, Math.random()*360, Math.random(), 2);
  let rocaDOM = document.createElement("img");
  rocaDOM.classList.add("roca");
  rocaDOM.src = "roca.png";
  rocaDOM.style.position = "absolute";
  rocaDOM.style.left = roca.posx + "px";
  rocaDOM.style.top = roca.posy + "px";
  rocaDOM.style.transform = "rotate("+roca.angulo+"deg) scale("+roca.escala+")";
  document.body.appendChild(rocaDOM);
  roca.DOM = rocaDOM; // Guardamos referencia al DOM
  rocas.push(roca);
}
```

Creamos el jugador y lo posicionamos en la pantalla.

```
let nave = document.querySelector("#nave");
let jugador = new Jugador(Math.random()*window.innerWidth, Math.random()*window.innerHeight, 0, 0);
nave.style.left = jugador.posx + "px";
nave.style.top = jugador.posy + "px";
```

Creamos un array para las balas.

```
let balas = [];
```

Detectamos teclas para mover al jugador y disparar.

```
document.onkeydown = function(tecla){
  switch(tecla.keyCode){
    case 87: jugador.posy -=5; break; // W
    case 83: jugador.posy +=5; break; // S
    case 65: jugador.posx -=5; break; // A
    case 68: jugador.posx +=5; break; // D
    case 32: // Barra espaciadora
      let bala = new Bala(jugador.posx+20, jugador.posy, 0, 10);
      balas.push(bala);
      let balaDOM = document.createElement("img");
      balaDOM.classList.add("bala");
      balaDOM.src = "bala.png";
      balaDOM.style.position = "absolute";
      balaDOM.style.left = bala.posx + "px";
      balaDOM.style.top = bala.posy + "px";
      document.body.appendChild(balaDOM);
      bala.DOM = balaDOM;
      break;
  }
  nave.style.left = jugador.posx + "px";
  nave.style.top = jugador.posy + "px";
}
```

Animamos las rocas y las balas para que se muevan en la pantalla.

```
function animar(){
  // Mover rocas
  rocas.forEach(r => {
    r.posx += Math.cos(r.angulo*Math.PI/180) * r.velocidad;
    r.posy += Math.sin(r.angulo*Math.PI/180) * r.velocidad;
    r.DOM.style.left = r.posx + "px";
    r.DOM.style.top = r.posy + "px";
  });

  // Mover balas
  balas.forEach((b,i)=>{
    b.posy -= b.velocidad;
    if(b.posy < 0){
      b.DOM.remove();
      balas.splice(i,1);
    } else {
      b.DOM.style.top = b.posy + "px";
    }
  });

  requestAnimationFrame(animar);
}

animar();
```

---

El código completo quedará así: 

```
<!doctype html>
<html>
<head>
<style>
  #nave { position:absolute; width:50px; }
  .roca { width:50px; position:absolute; }
  .bala { width:15px; position:absolute; }
  body { background:url("estrellas.jpeg"); background-size:cover; }
</style>
</head>
<body>
  <img src="nave.png" id="nave">
</body>
<script>
let anchopagina = window.innerWidth;
let altopagina = window.innerHeight;

// Clases
class Entidad { constructor(x,y,a,v){ this.posx=x; this.posy=y; this.angulo=a; this.velocidad=v; } }
class Bala extends Entidad { constructor(x,y,a,v){ super(x,y,a,v); } }
class Jugador extends Entidad { constructor(x,y,a,v){ super(x,y,a,v); } }
class Roca extends Entidad { constructor(x,y,a,e,v){ super(x,y,a,v); this.escala=e; } }

// Crear rocas y sus elementos DOM
let numero_rocas = 10;
let rocas = [];
for(let i=0;i<numero_rocas;i++){
  let roca = new Roca(Math.random()*500, Math.random()*500, Math.random()*360, Math.random(), 2);
  let rocaDOM = document.createElement("img");
  rocaDOM.classList.add("roca");
  rocaDOM.src = "roca.png";
  rocaDOM.style.left = roca.posx + "px";
  rocaDOM.style.top = roca.posy + "px";
  rocaDOM.style.transform = "rotate("+roca.angulo+"deg) scale("+roca.escala+")";
  document.body.appendChild(rocaDOM);
  roca.DOM = rocaDOM; // guardamos referencia al DOM
  rocas.push(roca);
}

// Crear jugador
let nave = document.querySelector("#nave");
let jugador = new Jugador(Math.random()*anchopagina, Math.random()*altopagina, 0, 0);
nave.style.left = jugador.posx+"px";
nave.style.top = jugador.posy+"px";

// Balas
let balas = [];

// Movimiento jugador y disparo
document.onkeydown = function(tecla){
  switch(tecla.keyCode){
    case 87: jugador.posy -=5; break; // W
    case 83: jugador.posy +=5; break; // S
    case 65: jugador.posx -=5; break; // A
    case 68: jugador.posx +=5; break; // D
    case 32: // Barra espaciadora
      let bala = new Bala(jugador.posx+20, jugador.posy, 0, 10);
      balas.push(bala);
      let balaDOM = document.createElement("img");
      balaDOM.classList.add("bala");
      balaDOM.src = "bala.png";
      balaDOM.style.left = bala.posx + "px";
      balaDOM.style.top = bala.posy + "px";
      document.body.appendChild(balaDOM);
      bala.DOM = balaDOM;
      break;
  }
  nave.style.left = jugador.posx+"px";
  nave.style.top = jugador.posy+"px";
}

// Función de animación
function animar(){
  // Mover rocas
  rocas.forEach(r => {
    r.posx += Math.cos(r.angulo*Math.PI/180) * r.velocidad;
    r.posy += Math.sin(r.angulo*Math.PI/180) * r.velocidad;

    // rebote en bordes
    if(r.posx < 0 || r.posx > anchopagina-50) r.velocidad *= -1;
    if(r.posy < 0 || r.posy > altopagina-50) r.velocidad *= -1;

    r.DOM.style.left = r.posx + "px";
    r.DOM.style.top = r.posy + "px";
  });

  // Mover balas hacia arriba
  balas.forEach((b,i)=>{
    b.posy -= b.velocidad;
    if(b.posy < 0) { 
      b.DOM.remove(); 
      balas.splice(i,1); 
    } else {
      b.DOM.style.top = b.posy + "px";
    }
  });

  requestAnimationFrame(animar);
}

animar();
</script>
</html>
```

---

Durante la práctica, logramos crear un jugador móvil, representar rocas con posiciones y rotaciones aleatorias y generar balas disparadas desde la nave, todo mediante clases y objetos. La herencia nos permitió definir propiedades comunes una sola vez en `Entidad` y extenderlas según el tipo de objeto.

Este ejercicio refuerza la importancia de la programación orientada a objetos, mostrando cómo usar clases y subclases para simular comportamientos dinámicos y mantener el código limpio, modular y fácil de ampliar. Además, combinamos JavaScript con HTML y CSS para crear una interacción visual en la pantalla, integrando teoría y práctica de manera efectiva.

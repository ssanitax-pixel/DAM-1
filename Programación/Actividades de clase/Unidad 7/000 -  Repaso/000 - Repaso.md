En este ejercicio hemos aplicado Programación Orientada a Objetos (POO) para gestionar múltiples entidades de forma independiente. La clave ha sido la separación de capas: el servidor (Python) gestiona la lógica física mediante trigonometría (uso de radianes, seno y coseno para movimiento en 360°), mientras que el cliente (HTML/JS) se encarga únicamente de la renderización visual consumiendo datos en formato JSON.

---

1. Backend (Servidor Pyton)

Importamos las librerías necesarias: `random` para el azar, `json` para el formato de datos, `flask` para el servidor web y `math` para los cálculos trigonométricos.

```
import random
import json
from flask import Flask, render_template
import math
```

Definimos la clase Npc. Este será como un molde de nuestros personajes. El método to_dict es crucial: traduce el objeto de Python a un diccionario que pueda convertirse fácilmente a JSON.

```
class Npc():
    def __init__(self, x, y, radio, direccion, velocidad): 
        # ... inicialización de atributos ...
    def to_dict(self):
        return {"posx": self.posx, "posy": self.posy, "radio": self.radio, "direccion": self.direccion}
```

En el método `mover`, aplicamos la lógica física. Usamos `math.cos` y `math.sin` para convertir un ángulo en movimiento sobre los ejes X e Y, además de aumentar la velocidad progresivamente según el enunciado.

```
def mover(self):
    self.direccion += (random.random() - 0.5) * 0.2
    self.velocidad += 0.1 # Aceleración constante
    self.posx += math.cos(self.direccion) * self.velocidad
    self.posy += math.sin(self.direccion) * self.velocidad
```

Creamos la lista de 50 personajes con valores aleatorios para que cada uno empiece en un punto y dirección distintos.

```
personajes = []
numero_personajes = 50

for i in range(0, numero_personajes):
    personajes.append(Npc(...))
```

Definimos las rutas de Flask. La ruta raíz `/` carga la interfaz y la ruta `/api` es la que actualiza las posiciones y envía los datos al navegador.

```
@app.route("/api")
def api():
    for personaje in personajes:    
        personaje.mover()
    return json.dumps([p.to_dict() for p in personajes], indent=2)
```

2. Frontend (Interfaz HTML/JS)

En el CSS, definimos el contenedor `main` y la clase `.npc`, que utiliza una imagen de fondo, que en este caso se llama `shrek.jpg` y posicionamiento absoluto para moverse libremente.

```
.npc {
  position: absolute;
  background-image: url('/static/shrek.jpg');
  background-size: cover;
}
```

En el JavaScript, usamos la función `fetch` para conectar con la API. Es fundamental el uso de dos promesas (`.then`): la primera para convertir la respuesta a formato JSON y la segunda para procesar la lista de NPCs.

```
fetch("/api")
  .then(respuesta => respuesta.json())
  .then(datos => {
    escenario.innerHTML = ""; // Limpiamos la pantalla anterior
    datos.forEach(function(npc) {
        // Creamos el div, le asignamos clase y posiciones desde la API
    });
  })
```

Finalmente, usamos un temporizador con `setTimeout` para repetir este proceso cada 100ms, creando la sensación de animación fluida.

```
temporizador = setTimeout(bucle, 100);
```

---

Código completo:

1. Python:

```
import random
import json
from flask import Flask, render_template
import math

class Npc():
    def __init__(self, x, y, radio, direccion, velocidad): 
        self.posx = x
        self.posy = y
        self.radio = radio
        self.direccion = direccion 
        self.velocidad = velocidad 

    def to_dict(self):
        return {
            "posx": self.posx, 
            "posy": self.posy,
            "radio": self.radio,
            "direccion": self.direccion 
        }

    def mover(self):
        self.direccion += (random.random() - 0.5) * 0.2
        self.velocidad += 0.1
        self.posx += math.cos(self.direccion) * self.velocidad
        self.posy += math.sin(self.direccion) * self.velocidad 

personajes = []
numero_personajes = 50

for i in range(0, numero_personajes):
    personajes.append(Npc(
        random.randint(0, 1000), 
        random.randint(0, 700),
        random.randint(10, 30),
        random.random() * math.pi * 2,
        random.random() * 2 # Empezamos con una velocidad más baja
    ))

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("juego.html")

@app.route("/api")
def api():
    for personaje in personajes:    
        personaje.mover()
    personajes_json = [p.to_dict() for p in personajes]
    return json.dumps(personajes_json, indent=2)

if __name__ == "__main__":
    app.run(debug=True)
```

2. HTML:

```
<!doctype html>
<html>
  <head>
    <style>
      main {
        width: 1000px;
        height: 700px;
        border: 2px solid black;
        position: relative;
        overflow: hidden;
        margin: auto;
      }
      .npc {
        position: absolute;
        background-image: url('/static/shrek.jpg');
        background-size: cover;
        background-position: center;
      }
    </style>
  </head>
  <body>    
    <main></main>
    <script>
      let escenario = document.querySelector("main");
      let temporizador;

      function bucle() {
        fetch("/api")
          .then(respuesta => respuesta.json())
          .then(datos => {
            escenario.innerHTML = ""; 
            
            datos.forEach(function(npc) {
              let personaje = document.createElement("div");
              personaje.classList.add("npc");
              personaje.style.left = npc.posx + "px";
              personaje.style.top = npc.posy + "px";
              personaje.style.width = npc.radio + "px";
              personaje.style.height = npc.radio + "px";
              escenario.appendChild(personaje);
            });
          })
          .catch(error => console.error("Error en la API:", error));

        clearTimeout(temporizador);
        temporizador = setTimeout(bucle, 100);
      }

      bucle();
    </script>
  </body>
</html>
```

---

Hemos construido un sistema asíncrono en tiempo real. Python calcula la física "en la sombra" y el navegador refresca la imagen cada 100ms. Al haber programado una aceleración constante, el ejercicio demuestra cómo una simple variable puede convertir un movimiento errático en una simulación de alta velocidad.

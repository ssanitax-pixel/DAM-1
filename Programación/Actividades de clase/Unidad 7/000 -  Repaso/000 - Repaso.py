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

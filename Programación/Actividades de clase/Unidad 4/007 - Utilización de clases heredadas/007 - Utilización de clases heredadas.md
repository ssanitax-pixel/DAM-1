Creamos la clase Animal como clase madre para representar las características comunes de todos los animales.

```
class Animal():
    def __init__(self):
        self.edad = ""
        self.nombre = ""
        self.raza = ""
```

Creamos la subclase Gato, que hereda de Animal, e inicializamos sus atributos.

```
class Gato(Animal):
    def __init__(self):
        super().__init__()
```

Creamos la subclase Perro, que también hereda de Animal, e inicializamos sus atributos.

```
class Perro(Animal):
    def __init__(self):
        super().__init__()
```

Creamos una nueva clase llamada Comida para representar una situación social en la que los animales comen con sus amigos.

```
class Comida():
    def __init__(self):
        self.tipo_comida = ""
        self.amigos = ""
```

Añadimos un método en la clase Animal que imprime un mensaje indicando que el animal está comiendo con sus amigos.

```
    def comer_con_amigos(self):
        print(self.nombre,"está comiendo",almuerzo1.tipo_comida,"con",almuerzo1.amigos)
```

---

El código completo queda así:

```
class Animal():
    def __init__(self):
        self.edad = ""
        self.nombre = ""
        self.raza = ""
    def comer_con_amigos(self):
        print(self.nombre,"está comiendo",almuerzo1.tipo_comida,"con",almuerzo1.amigos)

class Gato(Animal):
    def __init__(self):
        super().__init__()
        
class Perro(Animal):
    def __init__(self):
        super().__init__()

class Comida():
    def __init__(self):
        self.tipo_comida = ""
        self.amigos = ""
        
gato1 = Gato()
gato1.edad = 9
gato1.nombre = "Jagger"
perro1 = Perro()
perro1.edad = 12
perro1.nombre = "Chula"

almuerzo1 = Comida()
almuerzo1.tipo_comida = "Croquetas"
almuerzo1.amigos = ["Milo", "Lana", "Rocky"]

print("El gato tiene", gato1.edad, "años.")
print("El perro tiene", perro1.edad, "años.")


gato1.comer_con_amigos()
perro1.comer_con_amigos()
```

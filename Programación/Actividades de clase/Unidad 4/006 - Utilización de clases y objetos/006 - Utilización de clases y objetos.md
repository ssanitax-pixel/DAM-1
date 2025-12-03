En este ejercicio aplicamos lo aprendido sobre **clases y objetos** para resolver una situación de la vida real: ayudar a un grupo de amigos a calcular su presupuesto para desayunar juntos.
Creamos una clase llamada Matematicas que nos permite realizar operaciones de **redondeo, techo y suelo**, tres funciones matemáticas básicas que nos ayudan a ajustar los presupuestos al entero más cercano, al superior o al inferior según la necesidad.

---

Creamos la clase Matematicas para poder realizar operaciones numéricas sencillas.

```
class Matematicas():
    def __init__(self):
```

En el método `init,` guardamos el valor de PI dentro de la clase.

```
        self.PI = 3.14159265359
```

En el método redondeo, separamos la parte entera y la parte decimal del número. Comprobamos si la parte decimal es menor que 0.5 para decidir si redondeamos hacia abajo o hacia arriba.
Devolvemos el resultado sumando la parte entera con el valor del redondeo.

```
    def redondeo(self,numero):
        entero = int(numero)
        decimal = numero - entero
        if decimal < 0.5:
            redondeo = 0
        else:
            redondeo = 1
        return entero + redondeo
```

En el método techo, devolvemos el número entero siguiente al valor recibido.

```
    def techo(self,numero):
        return int(numero) + 1
```

En el método suelo, devolvemos solo la parte entera del número.

```
    def suelo(self,numero):
        return int(numero)
```

Creamos una instancia llamada calculadora para usar los métodos de la clase.

```
mate = Matematicas()
```

Guardamos en una lista los presupuestos de nuestros amigos.

```
presupuestos = [3.20, 4.75, 2.40, 5.99, 7.10]
```

Recorremos cada presupuesto con un bucle for.

```
for presupuesto in presupuestos:
```

Mostramos en pantalla el número del amigo y su presupuesto.

```
    print("Amigo", numero_amigo)
    print("Presupuesto original:", presupuesto, "euros")
    print("Presupuesto redondeado:", mate.redondeo(presupuesto), "euros")
    print("Presupuesto con techo:", mate.techo(presupuesto), "euros")
    print("Presupuesto con suelo:", mate.suelo(presupuesto), "euros")
    print()
```

Incrementamos el número del amigo y pasamos al siguiente presupuesto.

```
    numero_amigo = numero_amigo + 1
```

---

El código completo queda así:

```
class Matematicas():
    def __init__(self):
        self.PI = 3.14159265359
    
    def redondeo(self,numero):
        entero = int(numero)
        decimal = numero - entero
        if decimal < 0.5:
            redondeo = 0
        else:
            redondeo = 1
        return entero + redondeo
    
    def techo(self,numero):
        return int(numero) + 1
    def suelo(self,numero):
        return int(numero)

mate = Matematicas()

presupuestos = [3.20, 4.75, 2.40, 5.99, 7.10]

numero_amigo = 1

for presupuesto in presupuestos:
    print("Amigo", numero_amigo)
    print("Presupuesto original:", presupuesto, "euros")
    print("Presupuesto redondeado:", mate.redondeo(presupuesto), "euros")
    print("Presupuesto con techo:", mate.techo(presupuesto), "euros")
    print("Presupuesto con suelo:", mate.suelo(presupuesto), "euros")
    print()

    numero_amigo = numero_amigo + 1
```

---

Con este ejercicio reforzamos el uso de **clases, métodos y objetos**, aplicándolos en un contexto cotidiano.
Aprendimos que las clases nos permiten **organizar funciones relacionadas** dentro de una misma estructura (como las operaciones matemáticas), y que una instancia nos da acceso a esas funciones de manera sencilla.
Este tipo de estructura puede aplicarse más adelante en proyectos mayores, por ejemplo, para manejar cálculos financieros, simulaciones o incluso programas de gestión de gastos.

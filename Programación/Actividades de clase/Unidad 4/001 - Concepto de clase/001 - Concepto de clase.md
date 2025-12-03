Hasta ahora hemos aprendido a **encapsular** código usando funciones, lo que permite reutilizar bloques de instrucciones. Sin embargo, cuando necesitamos representar **entidades más complejas**, por ejemplo, un gato con sus características y comportamientos, las clases se vuelven fundamentales.

Una **clase** es una plantilla o molde que define **propiedades** y **métodos** comunes a un grupo de objetos.

Cada **objeto** creado a partir de una clase se denomina **instancia**, y puede tener valores propios para sus atributos.

---

Empezamos creando la clase llamada gato:

```
class Gato():
```

Definimos el constructor con con los parámetros que consideremos según el caso.

```
    def __init__(self,color,edad):
        self.color = color
```

Creamos un método, que sería una acción del gato, en este caso haremos que el gato maúlle.

```
    def maulla(self):
        print("El gato de color",self.color,"y",self.edad,"años está maullando")
```

Creamos los objetos, con los parámetros de los datos.

```
jaegger = Gato("Crema",9)
```

Y por último hacemos que el gato maulle.

```
jaegger.maulla()
```

---

Así queda en código completo:

```
class Gato():
    def __init__(self,color,edad):
        self.color = color
        self.edad = edad
    def maulla(self):
        print("El gato de color",self.color,"y",self.edad,"años está maullando")
        
jaegger = Gato("Crema",9)
jaegger.maulla()

lana = Gato("Manchas",11)
lana.maulla()
```

--- 

Este ejercicio muestra cómo las **clases** permiten **agrupar datos y comportamientos** dentro de una misma estructura, facilitando la **organización, reutilización y mantenimiento del código**.

En lugar de tener variables y funciones separadas para cada gato, una clase nos permite crear múltiples objetos con las mismas características pero con valores distintos, siguiendo los principios de la **Programación Orientada a Objetos**.

Gracias a las clases:

- Podemos representar entidades del mundo real en el código.

- Reutilizamos la misma plantilla para crear diferentes instancias.

- Encapsulamos propiedades y métodos, manteniendo el código más claro y modular.

Vamos a realizar un programa que nos ayude a clasificar la edad de un amigo y el precio del plato que vamos a compartir con él. Este programa nos permitirá entender mejor cómo tomar decisiones dependiendo de estos dos factores.

---

Primero, declaramos las variables que utilizaremos para almacenar la información del usuario:

```
edad_amigo = 0
```

Solicitamos al usuario que introduzca la edad de nuestro amigo y el precio del plato con un 'input' para poder hacer las evaluaciones correspondientes.

```
edad_amigo = int(input("¿Cuántos años tiene tu amigo?: "))
```

Luego, evaluamos la edad del amigo utilizando estructuras de control simples (if, elif, else) para clasificarla en si es un niño, un joven adulto, joven mayor o ya no es un joven.

```
if edad_amigo < 18:
    print("Tu amigo es un niño")
elif edad_amigo >= 18 and edad_amigo < 26:
    print("Tu amigo es un joven adulto")
else:
    print("Tu amigo ya no es un joven")
```

Después, evaluamos el precio del plato para saber si es un plato económico, de calidad o de lujo.

```
if precio_comida < 10:
    print("El plato es económico")
elif precio_comida >= 10 and precio_comida < 21:
    print("El plato es de calidad")
else:
    print("Es un plato de lujo")
```

Programa completo:

```
'''
Programa para clasificar la edad de un amigo y el precio del plato
Creado por Ana Sánchez Suárez
'''

edad_amigo = 0
precio_comida = 0

edad_amigo = int(input("¿Cuántos años tiene tu amigo?: "))
precio_comida = int(input("¿Cuánto cuesta el menú?: "))

if edad_amigo < 18:
    print("Tu amigo es un niño")
elif edad_amigo >= 18 and edad_amigo < 26:
    print("Tu amigo es un joven adulto")
elif edad_amigo >= 26 and edad_amigo < 36:
    print("Tu amigo es un joven mayor")
else:
    print("Tu amigo ya no es un joven")
    
if precio_comida < 10:
    print("El plato es económico")
elif precio_comida >= 10 and precio_comida < 21:
    print("El plato es de calidad")
else:
    print("Es un plato de lujo")
```

---

Este programa nos permite, con simples condiciones, tomar decisiones basadas en datos que recogemos del entorno, en este caso la edad de un amigo y el precio de un plato. Es un ejemplo claro de cómo las estructuras de control nos ayudan a manejar diferentes situaciones en la vida real, sin complicar el código con condiciones anidadas, facilitando así su comprensión y mantenimiento.

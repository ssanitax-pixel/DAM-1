# Ejercicio 2: Variables

---

## Introducción
En este ejercicio vamos a repasar como se hace una variable y cómo cambiarla más adelante, a demás de enseñar un mensaje en pantalla que diga con quién saldremos a cenar.

---

## Desarrollo técnico
Para comenzar, definimos la variable, que será "nombre_amigo", y le pondremos un valor, que será el nombre del amigo que hemos decidido, quedaría algo así:

```
nombre_amigo = "Evita"
```

A continuación, enseñaremos un mensaje en pantalla usando la función "print".

```
print("Quedaré con mi amiga",nombre_amigo,"este fin de semana para salir a cenar")
```

Por último, para cambiar la variable, pondremos "nombre_amigo" con otro nombre que queramos, sin borrar el anterior y acabaremos con otro "print" igual que el anterior.

---

## Aplicación práctica
El ejercicio completo se verá así:

```
'''
    Ejercicio de variables
    Creado por Ana Sánchez Suárez
    Este es un pequeño programa que lanza un mensaje de con quién voy a quedar este finde.
'''

nombre_amigo = "Evita"
print("Quedaré con mi amiga",nombre_amigo,"este fin de semana para salir a cenar")

nombre_amigo = "Raquel"
print("Quedaré con mi amiga",nombre_amigo,"este fin de semana para salir a cenar")
```

**Anotaciones**
- Cuidado con sobrescribir la primera variable, ya que entonces en los dos "print" saldrá el mismo nombre.
- Las variables con texto van siempre entre comillas.

---

## Conlusión
En este ejercicio hemos aprendido qué es una variable y como cambiarla, a parte de aplicarla en un "print".

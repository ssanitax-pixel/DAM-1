En la vida, como en la programación, pueden ocurrir situaciones inesperadas. Por ejemplo, durante una cena con amigos, algo puede salir mal. De igual forma, un programa puede fallar por un error. Para evitar que todo se detenga, usamos el manejo de excepciones, que nos permite continuar con normalidad.

Desarrollo del código:

```
try:
    print(4/0)
    print("Y la cena continua")
except:
    print("No puedo ejecutar eso")
    
print("Pero la cena continúa pase lo que pase")
```

Cuando ejecutas comida_amigos.py, obtendrás la siguiente salida:

```
No puedo ejecutar eso
Pero la cena continúa pase lo que pase
```

La línea print(4/0) genera un error porque no se puede dividir entre cero.

El error es capturado por el bloque except, que imprime "No puedo ejecutar eso".

Luego, el programa continúa con la siguiente instrucción fuera del bloque try-except, y muestra "Pero la cena continúa pase lo que pase".

---

El manejo de errores con try y except puede ayudar a que un programa siga funcionando incluso después de un problema inesperado. Igual que en una cena con amigos, lo importante es saber adaptarse, resolver y seguir disfrutando.

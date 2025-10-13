En programación, las aserciones son herramientas que nos permiten verificar que ciertas condiciones se cumplan mientras el programa se ejecuta. Si una aserción falla, es decir, si la condición no se cumple, se lanza un error que ayuda a detectar problemas. En este ejercicio, aplicamos esta idea para simular una comida con amigos donde queremos asegurarnos de que solo los invitados mayores de 18 años puedan entrar.

---

Primero declaramos una variable edad que representa la edad del invitado.

```
edad = 15
```

Luego, usamos un bloque 'try-except' para manejar posibles errores que surjan al comprobar si la edad es mayor o igual a 18 años. En caso de que la edad sea menor, lanzamos una aserción con el mensaje "No puedes entrar, eres menor de edad".

```
try:
    assert edad > 18, "No puedes entrar, eres menor de edad"
    print("¡Pasa a la cena!")
        
except:
    print("error")
```

Para mostrar claramente cómo funcionan las aserciones, el mismo 'assert' lo duplico fuera del bloque 'try-except' y dentro de él. La aserción fuera provoca que el programa falle inmediatamente si la condición no se cumple, mientras que la que está dentro del 'try' permite manejar el error y mostrar un mensaje sin detener el programa.

El programa completo quedaría así:

```
edad = 15
assert edad > 18, "No puedes entrar, eres menor de edad"
try:
    assert edad > 18, "No puedes entrar, eres menor de edad"
    print("¡Pasa a la cena!")
        
except:
    print("error")
```

Probamos con dos invitados:

Invitado con edad 15 años: al ejecutar el código, la aserción fuera del 'try' falla y muestra un error que detiene el programa. En el bloque 'try-except', el error es capturado y se muestra el mensaje personalizado:
"No puedes entrar, eres menor de edad"

Invitado con edad 20 años: ambas aserciones pasan correctamente y el programa imprime:
"¡Pasa a la cena!"

---

El programa se comporta según la edad del invitado y cómo las aserciones ayudan a controlar este flujo.

Las aserciones son útiles para mejorar la calidad del código porque permiten detectar errores, antes de que se conviertan en fallos más difíciles de identificar. Además, combinarlas con bloques 'try-except' nos da la posibilidad de manejar esas fallas de manera controlada, brindando una mejor experiencia al usuario o facilitando el proceso de depuración durante el desarrollo.

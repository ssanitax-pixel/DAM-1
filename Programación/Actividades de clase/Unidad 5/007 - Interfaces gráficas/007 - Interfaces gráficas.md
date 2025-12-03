Este programa es una calculadora básica creada con **Tkinter**, la librería de Python para interfaces gráficas. La aplicación permite ingresar dos números en campos de texto, pulsar un botón y ver inmediatamente el resultado en la misma ventana. Con este ejercicio hemos practicado cómo crear **ventanas, botones, entradas y etiquetas**, y cómo manejar eventos para que la interfaz responda a las acciones del usuario.

---

Importamos `Tkinter`, esto sirve para poder usar ventanas, botones, etiquetas y entradas en Python.

```
import tkinter as tk
```

Definimos la función calcular.

```
def calcular():
```

Primero, usamos operando1.get() y operando2.get() para tomar lo que el usuario escribió en los campos de entrada.
Después, convertimos esos valores a números decimales con float(), porque los datos de entrada siempre vienen como texto.

```
    op1valor = float(operando1.get())
    op2valor = float(operando2.get())
```


Sumamos los dos números.

```
    suma = op1valor + op2valor
```

Finalmente, usamos resultado.config(text=str(suma)) para actualizar la etiqueta con el resultado.

```
    resultado.config(text=str(suma))
```

Creamos la ventana principal.

```
ventana = tk.Tk()
```

Creamos los campos de entrada, cada `Entry` es una caja donde el usuario puede escribir un número. `pack` sirve para ponerlas en la ventana, una debajo de la otra.

```
operando1 = tk.Entry()
operando1.pack(padx=10,pady=10)
```

Creamos un botón que diga "Calcular", `command=calcular` significa que al hacer clic, se ejecute la función `calcular`.

```
boton = tk.Button(text="Calcular",command=calcular)
boton.pack(padx=10,pady=10)
```

Creamos la etiqueta del resultado, `Label` es un resultado que aparecerá en la ventana, inicialmente dirá "Resultado", pero cuando pulsemos el botón se actualiza con la suma.

```
resultado = tk.Label(text="Resultado")
resultado.pack(padx=10,pady=10)
```

Ejecutamos la ventana, esto mantiene la ventana abierta, sin esto la ventana se abriría y se cerraría inmediatamente.

```
ventana.mainloop()
```

---

El código completo:

```
import tkinter as tk

def calcular():
    op1valor = float(operando1.get())
    op2valor = float(operando2.get())
    suma = op1valor + op2valor
    resultado.config(text=str(suma))

ventana = tk.Tk()

operando1 = tk.Entry()
operando1.pack(padx=10,pady=10)

operando2 = tk.Entry()
operando2.pack(padx=10,pady=10)

boton = tk.Button(text="Calcular",command=calcular)
boton.pack(padx=10,pady=10)

resultado = tk.Label(text="Resultado")
resultado.pack(padx=10,pady=10)

ventana.mainloop()
```

---

Con esta calculadora hemos aprendido a trabajar con interfaces gráficas en Python, entendiendo cómo tomar datos del usuario, procesarlos y actualizar la ventana en tiempo real. Nos ayuda a ver de manera práctica cómo funcionan los eventos, como el clic en un botón, y cómo interactúan los distintos elementos de la interfaz. Además, podemos relacionarlo con situaciones cotidianas, como hacer sumas rápidas con amigos, lo que hace que el aprendizaje sea más significativo y aplicable a proyectos futuros.

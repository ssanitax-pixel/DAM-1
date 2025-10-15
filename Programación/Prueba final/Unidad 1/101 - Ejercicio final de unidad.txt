El objetivo de este ejercicio, realizar un programa que calcule el total de una factura aplicando IVA y un descuento fijo en el caso de que se pague el mínimo establecido.

---

Vamos a desglosar el programa paso a paso.

Primero pediremos una entrada en cadena, y otra entrada con número decimal, para ello usaremos la función 'input', que servirá para introducir un dato, y usaremos también la función 'float' para convertir el dato introducido en decimal.

```
nombre_cliente = input("¿Cuál es tu nombre?: ")
precio_bruto = float(input("Precio bruto del producto: "))
```

Seguidamente definimos las constantes, que gramaticalmente se recomienda escribirlas en mayúscula.

```
IVA = 0.21
```

Utilizamos las estructuras 'if/elif/else' para que el descuento se active sólo en caso de que el cliente gaste 50€ o más, también como extra, nos aseguraremos de que si en la entrada del precio se pone un numero inferior a 0€ se pare el programa y aparezca un mensaje explicando que no es un valor válido con un 'print'.

```
if precio_bruto >= 50:
    DESCUENTO = DESCUENTO
elif precio_bruto < 0:
    print("No es un valor válido")
    exit()
else:
    DESCUENTO = 0
```

Realizamos los cálculos necesarios para dar todos los resultados que nos piden, aquí dejo un ejemplo de ello:

```
IVA_aplicado = precio_bruto * IVA
```

Y para finalizar, realizamos unas salidas con la función 'print' para desglosar la factura.

```
print("Ticket de la factura")
```

---

El programa al completo:

```
'''
    Factura con IVA y descuento
    Programa que calcula el total de una factura aplicando IVA y un descuento.
    Creado por Ana Sánchez Suárez
    v1.0
    (c) 2025
'''

# Pedimos entradas, que se convertirán en una cadena, y un número decimal
nombre_cliente = input("¿Cuál es tu nombre?: ")
precio_bruto = float(input("Precio bruto del producto: "))

# Definimos las constantes
IVA = 0.21
DESCUENTO = 0.1

# Utilizamos las estructuras 'if/elif/else' , para que el descuento se active solo si es más de 50€ lo gastado, y nos aseguramos de que no ponen un valor menor a 0€
if precio_bruto >= 50:
    DESCUENTO = DESCUENTO
elif precio_bruto < 0:
    print("No es un valor válido")
    exit()
else:
    DESCUENTO = 0
    
# Desarrollamos los cálculos
IVA_aplicado = precio_bruto * IVA
subtotal_con_IVA = precio_bruto + IVA_aplicado
descuento_aplicado = precio_bruto * DESCUENTO
total_a_pagar = subtotal_con_IVA - descuento_aplicado
    
# Salida de datos
print("")
print("------------------------------")
print("Ticket de la factura")
print("------------------------------")
print("Nombre del cliente: ",nombre_cliente)
print("")
print("Precio bruto: ",precio_bruto,"€")
print("IVA aplicado: ",IVA_aplicado,"€")
print("Descuento aplicado: ",descuento_aplicado,"€")
print("------------------------------")
print("Total a pagar: ",total_a_pagar)
```

---

**Conclusión**

En este ejercicio se ha utilizado la función 'input' para recibir datos del usuario y convertirlos a tipos numéricos con 'float'. Se han aplicado constantes para el IVA y el descuento, y se han empleado estructuras condicionales 'if/elif/else' para controlar cuándo aplicar el descuento y validar entradas incorrectas (como valores negativos).

Se debe prestar atención a la correcta aplicación de las fórmulas para cálculos y asegurarse de que los mensajes mostrados al usuario sean claros y completos. Además de que es importante ir probando el programa poco a poco para validar y hay fallos en nuestro código y poder encontrar el fallo más rápido y fácil.

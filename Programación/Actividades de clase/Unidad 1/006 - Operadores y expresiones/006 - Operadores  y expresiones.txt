Cuando compras algo con amigos, como comida o entradas de cine, es útil saber cuánto se paga de impuestos. Con este ejercicio, vamos a crear una calculadora de IVA que nos ayude a saber el total de una factura, aplicando operadores aritméticos y booleanos. Así usamos la programación en algo práctico y cotidiano.

---

Aquí está el desarrollo técnico del programa:

```
# Declaración de Variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Entrada de usuario
print("Programa calculadora de impuestos")
print("(c) 2025 Ana Sánchez Suárez")
print("Introduce una base y te calculo el IVA y el total")
base_imponible = float(input("Introduce la base imponible de la factura: "))

# Varificación booleana (el valor tiene que se mayor que 0)
if base_imponible > 0:
    # Cálculo de IVA
    iva = 0.21 # Tasa del IVA del 21%
    total_iva = base_imponible * iva

    # Cálculo del Total Factura
    total_factura = base_imponible + total_iva

    # Salida de Resultados
    print(f"Base Imponible: {base_imponible}")
    print(f"IVA: {total_iva}")
    print(f"Total Factura: {total_factura}")
else: 
    print("La base imponible debe ser mayor que 0. Intenta de nuevo")
```

Ahora vamos a probar una aplicación práctica, el programa nos pedirá la base imponible, que pondremos por ejemplo 100, y nos indicará lo siguiente:

Ejemplo 1:
```
Base Imponible: 100
IVA: 21
Total Factura 121
```

Ejemplo 2:
```
Base Imponible: 200
IVA: 42
Total Factura: 242
```

Esto demuestra que el cálculo del 21% de IVA funciona correctamente con distintos valores.

---

Con este ejercicio practicamos cómo usar variables para guardar datos, y operadores para hacer cálculos básicos, como el IVA. Así vemos que la programación es una herramienta práctica para resolver problemas reales, como calcular impuestos o dividir cuentas con amigos, usando conceptos que aprendemos en clase.

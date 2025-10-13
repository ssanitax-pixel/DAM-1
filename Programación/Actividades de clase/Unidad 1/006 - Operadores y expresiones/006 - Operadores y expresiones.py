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

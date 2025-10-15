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

# Utilizamos las estructuras 'if/elif/else', para que el descuento se active solo si es más de 50€ lo gastado, y nos aseguramos de que no ponen un valor menor a 0€
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

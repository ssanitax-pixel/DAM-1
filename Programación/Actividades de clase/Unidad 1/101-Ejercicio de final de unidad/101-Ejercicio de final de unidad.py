print("Programa que solicita datos por teclado, valida entradas básicas, calcula IVA y posibles descuentos según reglas dadas y muestre un ticket con formato claro.")

print("Creado por Ana Sánchez Suárez")

print("(c) 2025")

cliente_nombre = input("Dime tu nombre: ")
edad = int(input("Dime tu edad: "))
base_imponible = float(input("Introduce la base imponible de la factura: "))
descuento = 0

IVA = 0.21

if edad < 18:
    print("No se puede emitir factura")
    exit()
else:
    print("Validación de edad correcta")    

if base_imponible < 0:
    print("No se puede emitir factura")
elif base_imponible < 100:
    descuento = 0
    print("La base tras el descuento es: ",base_tras_descuento)
    importe_descuento = base_imponible * descuento
    base_tras_descuento = base_imponible - importe_descuento
elif base_imponible >= 100 and base_imponible < 200:
    descuento = 0.05
    importe_descuento = base_imponible * descuento
    base_tras_descuento = base_imponible - importe_descuento
    print("La base tras el descuento es: ",base_tras_descuento)
else:
    descuento = 0.1
    importe_descuento = base_imponible * descuento
    base_tras_descuento = base_imponible - importe_descuento
    print("La base tras el descuento es: ",base_tras_descuento)
    
importe_iva = base_tras_descuento * IVA
total_factura = base_tras_descuento + importe_iva

print("-----------------------")
print("Ticket")
print("Datos del cliente:")
print("Nombre: ",cliente_nombre)
print("Edad: ",edad)
print("-----------------------")
print("Desglose de la factura:")
print("base: ",base_imponible)
print("% descuento: ",descuento * 100)
print("€ descuento: ",importe_descuento)
print("base tras descuento:",base_tras_descuento)
print("IVA: ",IVA * 100,"%")
print("----------------------")
print("TOTAL: ",total_factura)

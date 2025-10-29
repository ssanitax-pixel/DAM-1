'''
	Calculadora de impuestos
	v0.1 por Ana Sánchez Suárez
	Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''

# Este programa no tiene importaciones, es decir, no está usando códigos de otros módulos/paquetes

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Aquí pondría las funciones/clases, sería un bloque de cógido reutilizable, como una plantilla

# Primero pido una entrada
print("Programa calculadora de impuestos")
print("(c) 2025 Ana Sánchez Suárez")
print("Introduce una base y te calculo el IVA y el total")
base_imponible = int(input("Introduce la base imponible de la factura: "))

# Luego realizo cálculos
total_iva = base_imponible*0.21
total_factura = total_iva + base_imponible

# Por último expreso una salida
print("El IVA de la factura es: ", total_iva)
print("El total de la factura es: ", total_factura)

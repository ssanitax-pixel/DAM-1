'''
Programa para clasificar la edad de un amigo y el precio del plato
Creado por Ana Sánchez Suárez
'''

edad_amigo = 0
precio_comida = 0

edad_amigo = int(input("¿Cuántos años tiene tu amigo?: "))
precio_comida = int(input("¿Cuánto cuesta el menú?: "))

if edad_amigo < 18:
    print("Tu amigo es un niño")
elif edad_amigo >= 18 and edad_amigo < 26:
    print("Tu amigo es un joven adulto")
elif edad_amigo >= 26 and edad_amigo < 36:
    print("Tu amigo es un joven mayor")
else:
    print("Tu amigo ya no es un joven")
    
if precio_comida < 10:
    print("El plato es económico")
elif precio_comida >= 10 and precio_comida < 21:
    print("El plato es de calidad")
else:
    print("Es un plato de lujo")

'''
    Programa que calcula el precio de una cena basado en las personas que van.
    Creado por Ana Sánchez Suárez
'''

numero_personas = 0
precio_por_persona = 25

numero_personas = input("¿Cuántas personas van a ir a comer?: ")
numero_personas = int(numero_personas)

precio_final = (numero_personas * precio_por_persona)

print("¡Aviso! El precio por persona es de",precio_por_persona,"Euros")
print("El precio total de la cena, teniendo en cuenta que hay",numero_personas,"asistentes, será de",precio_final,"Euros")

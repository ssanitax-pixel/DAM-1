'''
    Programa para calcular el total de una cena de amigos con su descuento
    v1.0 Ana Sánchez Suárez
'''

import math

costos_comidas = [15,44,32,12,4,34]

costo_total = sum(costos_comidas)

descuento = costo_total * 0.10
costo_final = costo_total - descuento

print("El costo total de las comidas con amigos es: ",costo_final,"Euros")

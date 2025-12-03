'''
    Programa que calcula cuantas cuadras según los caballos que haya.
    v1.0 Ana Sánchez Suárez
'''

import math

numero_caballos = int(input("¿Cuántos caballos hay?: "))

caballos_por_cuadra = int(input("¿Cuántos caballos caben en cada cuadra?: "))

cuadras_necesarias = math.ceil(numero_caballos/caballos_por_cuadra)

print("Al tener",numero_caballos,"caballos y caber",caballos_por_cuadra,"por cuadra, necesitaremos",cuadras_necesarias,"cuadras en total")

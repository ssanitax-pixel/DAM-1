import math

raiz_cuadrada = math.sqrt(16)

numero_pi = math.pi

def calcular_area_circulo(radio):
    area = numero_pi * radio ** 2
    return area

area = calcular_area_circulo(5)

print("El área del círculo con radio 5 es: ",area)

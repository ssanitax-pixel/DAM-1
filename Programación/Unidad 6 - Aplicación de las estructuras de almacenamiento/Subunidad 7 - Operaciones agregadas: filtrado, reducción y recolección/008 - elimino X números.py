import random

patron = {1,2,3,4,5,6,7,8,9}

while True:
    lista = []
    for i in range(1,10):
        lista.append(random.randint(1,9))
    conjunto = set(lista)
    if conjunto == patron:
        print("El conjunto es correcto")
        print(conjunto)
        print(lista)
        for i in range (1,9):
            # Ahora elimino un número
            indice = random.randint(1,8)
            lista[indice] = "_"
        print(lista)
        break # Fuerzo la finalización del bucle infinito

import sys

argumentos = sys.argv
nombre = argumentos[1]
edad = argumentos[2]
entero = int(edad)
doble = entero*2
print("Hola, "+nombre+" tienes " +str(doble)+" años")

'''
Entrada:

python3 [nombre_archivo.py] Luis 15

Salida:

Hola, Luis tienes 30 años
'''

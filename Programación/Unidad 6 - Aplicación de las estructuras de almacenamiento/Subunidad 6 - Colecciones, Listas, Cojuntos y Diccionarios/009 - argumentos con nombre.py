import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--nombre")
parser.add_argument("--apellidos")

args = parser.parse_args()

diccionario = vars(args)
print(diccionario)

'''
Entrada:

python3 [nombre_archivo.py] --nombre "Juan" --apellidos "Pérez García"

Salida (el diccionario):

{'nombre': 'Juan', 'apellidos': 'Pérez García'}
'''

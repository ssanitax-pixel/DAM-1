archivo = open("mapa.txt",'r') # READ

lineas = archivo.readlines()

for linea in lineas:
    if "001" in linea:
        print("Encontrado!: ",linea)

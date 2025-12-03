import os

carpeta = input("Introduce el nombre de la carpeta: ")

elementos = os.listdir(carpeta)

for elemento in elementos:
    ruta_completa = os.path.join(carpeta, elemento)
    
    if os.path.isfile(ruta_completa):
        tamanio_bytes = os.path.getsize(ruta_completa)
        tamanio_mb = tamanio_bytes / (1024 * 1024)
    else:
        tamanio_mb = 0
    
    print("Ruta: ",ruta_completa," | Tamaño: ",tamanio_mb,"MB")

import os

carpeta = input("Indica una carpeta: ")

elementos = os.listdir(carpeta)

for elemento in elementos:
    ruta = os.path.join(carpeta,elemento)
    print(ruta)
    print(os.path.getsize(ruta)/(1024*1024),"KB")
    print(os.path.getmtime(ruta))

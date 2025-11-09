import os

nombre = input("Introduce el nombre del archivo que deseas crear: ")

try:
    if os.path.exists(nombre):
        print("Error: el archivo ya existe.")
    else:
        archivo = open(nombre, "w")
        archivo.close()
        print("Archivo creado correctamente.")
except:
    print("Ocurrió un error al crear el archivo.")

try:
    archivo = open(nombre, "a")
    archivo.write("Texto de ejemplo dentro del archivo.\n")
    archivo.close()
    print("Texto escrito correctamente.")
except:
    print("Ocurrió un error al escribir en el archivo.")

try:
    archivo = open(nombre, "r")
    contenido = archivo.read()
    archivo.close()
    print("Contenido del archivo:")
    print(contenido)
except:
    print("Ocurrió un error al leer el archivo.")
    
try:
    os.remove(nombre)
    print("Archivo eliminado.")
except:
    print("Ocurrió un error al eliminar el archivo.")


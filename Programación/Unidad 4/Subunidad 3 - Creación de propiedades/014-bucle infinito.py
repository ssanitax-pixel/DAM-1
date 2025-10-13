'''
    Aplicación de gestión de productos
    (c) 2025 Ana Sánchez Suárez
    Esta aplicación gestiona productos
'''

# En esta aplicación no aplica importar librerías

# Definimos clases y funciones

class Producto():
    def __init__(self):
        self.nombre = ""
        self.precio = 0
        
# Creamos las variables globales

productos = []

# Primero lazamos un mensaje de bienvenida
print("Gestor de productos v1.0 Ana Sánchez")
# Metemos al usuario en un bucle infinito
while True:
    # Le mostramos al usuario las opciones que tiene
    print("Selecciona una opción:")
    print("1.-Crear un nuevo producto")
    print("2.-Listar productos")
    print("3.-Actualizar productos")
    print("4.-Eliminar productos")
    option = int(input("Escoge tu opción: "))
    # En función de la opción que coja el usuario
    if option == 1:
        # o bien creamos un nuevo producto
        print("Creamos un nuevo producto")
    elif option == 2:
        # o bien listamos los productos
        print("Vamos a listar los productos")
    elif option == 3:
        # o bien actualizamos los productos
        print("Vamos a actualizar productos")
    elif option == 4:
        # o bien eliminamos los productos
        print("Vamos a eliminar productos")
    # Y volvemos a repetir


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
print("Gestor de productos v1.0 Ana Sánchez)
# Le mostramos al usuario las opciones que tiene
print("Selecciona una opción:")
print("1.-Crear un nuevo producto")
print("2.-Listar productos")
print("3.-Actualizar productos")
print("4.-Eliminar productos")
option = int(input("Escoge tu opción: ")
# En función de la opción que coja el usuario
    # o bien creamos un nuevo producto
    # o bien listamos los productos
    # o bien actualizamos los productos
    # o bien eliminamos los productos
# Y volvemos a repetir

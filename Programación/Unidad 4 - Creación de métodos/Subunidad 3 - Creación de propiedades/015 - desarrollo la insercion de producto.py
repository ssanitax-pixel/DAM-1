'''
    Aplicación de gestión de productos
    (c) 2025 Ana Sánchez Suárez
    Esta aplicación gestiona productos
'''

# En esta aplicación no aplica importa librerías

# Definimos clases y funciones

class Producto():
    def __init__(self):
        self.nombre = ""
        self.precio = 0
    
# Creamos las variables globales

productos = []

# Primero lanzamos un mensaje de bienvenida

print("Gestor de productos v1.0 Ana Sánchez Suárez")


# Metemos al usuario en un bucle infinito

while True:

    # Le mostramos al usuario las opcines que tiene

    print("Selecciona una opción:")
    print("1.-Crear un nuevo producto")
    print("2.-Listar productos")
    print("3.-Actualizar productos")
    print("4.-Eliminar productos")

    # En función de la opción que coja el usuario

    opcion = int(input("Escoge tu opción: "))

        # o bien creamos un nuevo producto
    if opcion == 1:
        print("Creamos un nuevo producto")
        producto = Producto() # Creo una nueva instancia del producto
        producto.nombre = input("Introduce el nombre del producto: ") # Escribo la propiedad
        producto.precio = input("Introduce el precio del producto: ") # Escribo la propiedad
        productos.append(producto)
        
        # o bien listamos los productos
    elif opcion == 2:
        print("Vamos a listar los productos")
        
        # o bien actualizamos los productos
    elif opcion == 3:
        print("Vamos a actualizar productos")
        
        # o bien eliminamos los productos
    elif opcion == 4:
        print("Vamos a eliminar productos")
        
    # Y volvemos a repetir

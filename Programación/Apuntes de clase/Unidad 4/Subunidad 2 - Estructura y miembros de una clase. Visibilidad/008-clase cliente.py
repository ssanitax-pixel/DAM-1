# CRUD
# Create
# Read
# Update
# Delete

class Cliente():
    def __init__(self):
        self.email = ""
        self.nombre = ""
        self.direccion = ""

print("Programa de gestión de clientes v1.0 Ana Sánchez Suárez")

# Muestro opciones en el menú para el usuario
print("Selecciona una opción: ")
print("1.-Insertar un cliente")
print("2.-Listar clientes")
print("3.-Actualizar clientes")
print("4.-Eliminar clientes")

clientes = [] # Creo una lista VACÍA

while True: # Esto desata un bucle infinito pero controlado
    
    #Le permito escoger una opción
    opcion = input("Escoge una opción: ")
    opcion = int(opcion) # Convierto a entero

    if opcion == 1:
        print("Vamos a insertar un cliente")
        #Primero creamos un nuevo cliente
        nuevocliente = Cliente()
        # Ahora le ponemos propiedades
        nuevocliente.nombre = input("Introduce el nombre del cliente: ")
        nuevocliente.email = input("Introduce el email del cliente: ")
        nuevocliente.direccion = input("Introduce la dirección del cliente: ")
        # A la lista de clientes añadimos nuestro cliente
        clientes.append(nuevocliente)
    elif option == 2:
        print("Vamos a ver los clientes")
        print(clientes)
    elif option == 3:
        print("Vamos a actualizar un cliente")
    elif option == 4:
        print("Vamos a eliminar un cliente")
    else:
        break # Rompemos el bucle de while así

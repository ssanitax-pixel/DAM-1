# CRUD
# Create
# Read
# Update
# Delete

print("Programa de gestión de clientes v1.0 Ana Sánchez Suárez")

# Muestro opciones en el menú para el usuario
print("Selecciona una opción: ")
print("1.-Insertar un cliente")
print("2.-Listar clientes")
print("3.-Actualizar clientes")
print("4.-Eliminar clientes")

#Le permito escoger una opción
opcion = input("Escoge una opción: ")
opcion = int(opcion) # Convierto a entero

clientes = [] # Creo una lista VACÍA

while True: # Esto desata un bucle infinito pero controlado
    if opcion == 1:
        print("Vamos a insertar un cliente")
    elif option == 2:
        print("Vamos a ver los clientes")
    elif option == 3:
        print("Vamos a actualizar un cliente")
    elif option == 4:
        print("Vamos a eliminar un cliente")
    else:
        break # Rompemos el bucle así

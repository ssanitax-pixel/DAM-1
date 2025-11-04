import pickle

class Cliente():
    def __init__(self):
        self.nombre = ""
        self.apellidos = ""
        self.email = ""

clientes = []

try:
    archivo = open("clientes.bin",'rb')
    clientes = pickle.load(archivo)
    archivo.close()
except:
    print("No existe archivo de datos")

while True:
    archivo = open("clientes.bin",'wb')
    pickle.dump(clientes,archivo)
    archivo.close()
    
    print("Menú de selección:")
    print("1. Crear cliente.")
    print("2. Listar clientes.")
    opcion = int(input("Elige opción: "))
    if opcion == 1:
        print("Vamos a crear un cliente.")
        nuevocliente = Cliente()
        nuevocliente.nombre = input("Dime el nombre del cliente: ")
        nuevocliente.apellidos = input("Dime los apellidos del cliente: ")
        nuevocliente.email = input("Dime el email del cliente: ")
        clientes.append(nuevocliente)
    elif opcion == 2:
        print("Vamos a listar los clientes.")
        for cliente in clientes:
            print(cliente.nombre,"/",cliente.apellidos,"/",cliente.email)


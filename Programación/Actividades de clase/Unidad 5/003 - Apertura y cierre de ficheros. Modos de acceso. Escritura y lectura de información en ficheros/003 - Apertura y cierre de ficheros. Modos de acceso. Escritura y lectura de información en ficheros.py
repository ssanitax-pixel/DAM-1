import pickle

archivo = open("basededatos.txt",'w')
archivo.write("esto es otro contenido")
archivo.close()

archivo = open("basededatos.txt",'a')
archivo.write("esto es un contenido")
archivo.close()

archivo = open("basededatos.txt",'r')
linea = archivo.readlines()
print(linea)
archivo.close()

class Cliente():
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail

clientes = []

clientes.append(Cliente("Ana","ana@mail.es"))
clientes.append(Cliente("Fátima","fatima@mail.es"))

archivo = open("clientes.bin",'wb')
pickle.dump(clientes,archivo)
archivo.close()

archivo = open("clientes.bin",'rb')
clientes = pickle.load(archivo)

archivo.close()
for cliente in clientes:
    print(cliente.nombre, cliente.email)

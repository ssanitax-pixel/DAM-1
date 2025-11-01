import pickle

class Cliente():
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail

clientes = []

clientes.append(Cliente("Ana","ana@ana.es"))
clientes.append(Cliente("Fátima","fatima@fatima.es"))

archivo = open("clientes.bin",'wb')
pickle.dump(clientes,archivo)
archivo.close()

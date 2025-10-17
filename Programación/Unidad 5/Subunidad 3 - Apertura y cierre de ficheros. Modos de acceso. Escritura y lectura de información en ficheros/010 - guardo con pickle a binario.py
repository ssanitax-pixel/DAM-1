import pickle

class Cliente():
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail
        
clientes =[]

clientes.append(Cliente("Ana Sánchez","anasasu@gmail.com"))
clientes.append(Cliente("Fátima Sánchez","fafasa@gmail.com"))

archivo = open("clientes.bin",'wb')
pickle.dump(clientes,archivo)
archivo.close()

class Cliente():
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail
        
clientes =[]

clientes.append(Cliente("Ana Sánchez","anasasu@gmail.com"))
clientes.append(Cliente("Fátima Sánchez","fafasa@gmail.com"))

print(clientes)

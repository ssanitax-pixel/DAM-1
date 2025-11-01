class Cliente():
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail

clientes = []

clientes.append(Cliente("Ana","ana@ana.es"))
clientes.append(Cliente("Fátima","fatima@fatima.es"))

print(clientes)

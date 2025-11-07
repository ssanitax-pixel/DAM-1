class Matematicas():
    def __init__(self):
        self.PI = 3.14159265359
    
    def redondeo(self,numero):
        entero = int(numero)
        decimal = numero - entero
        if decimal < 0.5:
            redondeo = 0
        else:
            redondeo = 1
        return entero + redondeo
    
    def techo(self,numero):
        return int(numero) + 1
    def suelo(self,numero):
        return int(numero)

mate = Matematicas()

presupuestos = [3.20, 4.75, 2.40, 5.99, 7.10]

numero_amigo = 1

for presupuesto in presupuestos:
    print("Amigo", numero_amigo)
    print("Presupuesto original:", presupuesto, "euros")
    print("Presupuesto redondeado:", mate.redondeo(presupuesto), "euros")
    print("Presupuesto con techo:", mate.techo(presupuesto), "euros")
    print("Presupuesto con suelo:", mate.suelo(presupuesto), "euros")
    print()

    numero_amigo = numero_amigo + 1

lista_participantes = [25, "cinco", 30, "cuatro", "siete"]

numeros_etiquetas = ["cero","uno","dos","tres","cuatro","cinco","seis","siete"]

def calculaDoble():
    for participante in lista_participantes:
        if isinstance(participante, int):
            print(participante * 2)
        else:
            if participante in numeros_etiquetas:
                indice = numeros_etiquetas.index(participante)
                print(indice * 2)
            else:
                print("No es posible hacer eso")

calculaDoble()

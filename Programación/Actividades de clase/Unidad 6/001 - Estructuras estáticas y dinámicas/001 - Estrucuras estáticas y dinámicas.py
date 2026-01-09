lista_amigos = ['Alba','Raquel','Eva']

lista_amigos.append('Nicole')

print("Lista de amigas: ")
for amigo in lista_amigos:
    print(amigo)
    
lista_amigos[1] = 'Pilar'

lista_amigos.pop(0)

print("Lista de amigas actualizado: ")
for amigo in lista_amigos:
    print(amigo)

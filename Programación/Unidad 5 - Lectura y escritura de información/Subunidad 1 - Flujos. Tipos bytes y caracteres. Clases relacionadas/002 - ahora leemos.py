archivo = open("clientes.txt",'r') # Read = Read

contenido = archivo.readline()
# También existe archivo.readlines()

print(contenido)

archivo.close()

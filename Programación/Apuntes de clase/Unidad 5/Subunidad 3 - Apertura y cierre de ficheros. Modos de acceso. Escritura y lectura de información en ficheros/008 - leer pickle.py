# si no lo tienes: pip3 install pickle 
import pickle

archivo = open("datos.bin","rb") # bin = binario

cadena = pickle.load(archivo)
print(cadena)

archivo.close()

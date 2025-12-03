# Si no lo tienes: pip3 install pickle
import pickle

archivo = open("datos.bin",'wb') # bin = binario
cadena = "Ana Sánchez Suárez"

pickle.dump(cadena,archivo)

archivo.close()

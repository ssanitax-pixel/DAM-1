# si no lo tienes: pip3 install pickle 
import pickle

archivo = open("datos.bin","wb") # bin = binario
cadena = "Ana"

pickle.dump(cadena,archivo)

archivo.close()

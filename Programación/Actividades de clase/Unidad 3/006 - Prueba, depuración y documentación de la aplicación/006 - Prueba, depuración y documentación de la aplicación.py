'''
    Calcula la raíz cuadrada de un número de manera segura.
    
    Si el número es negativo, devuelve 0.
    Si el número es una cadena, intenta convertirlo a un valor numérico.
    Si la conversión falla, devuelve 0.
    
    v1.0 Ana Sánchez Suárez
'''

import math as matematicas

def raizSegura(numero):

    try: 
        if isinstance(numero, str):
            numero = float(numero)
        assert numero >= 0
        assert isinstance(numero, (int, float))
        return matematicas.sqrt(numero)
            
    except:
        return 0
    
print(raizSegura(4))
print(raizSegura(0))
print(raizSegura("9"))
print(raizSegura("-1"))
print(raizSegura("hola"))

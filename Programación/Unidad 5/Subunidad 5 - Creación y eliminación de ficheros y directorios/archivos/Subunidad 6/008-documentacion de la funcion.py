def hazDivision(dividendo,divisor):
'''
    Función de división
    Entradas: dividendo y divisor que se espera que sean numéricos
    Salidas: resultado de la división como número ( o cero si hay fallo)
    Capturas de error:
    1. Si es numérico
    2. Si se puede convertir a número
    3. Si no es división entre cero
'''

# comprobamos si son numeros
    print("Entramos en la función")
    if isinstance(dividendo, (int, float, complex)) and isinstance(divisor, (int, float, complex)):
        print("parece que los parámetros no son números")
    # comprobamos que el divisor no es cero
        if divisor != 0:
            print("parece que los puedo dividir")
            resultado = dividendo/divisor
            return resultado
        else:
            print("No puedo dividir porque el divisor es cero")
            resultado = 0
    else:
        print("Los parametros no son números, pero voy a intentar convertirlos")
        try:
            print("Intento convertir a números con éxito")
        # vamos a intentar convertirlo en números
            dividendo = float(dividendo)
            divisor = float(divisor)
            resultado = (dividendo/divisor)
            return resultado
        except:
            print("He intentado convertir a números, pero no he podido")
            return 0
    
print(hazDivision(4,"3"))

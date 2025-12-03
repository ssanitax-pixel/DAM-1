def hazDivision(dividendo,divisor):
# comprobamos si son numeros
    if isinstance(dividendo, (int, float, complex)) and isinstance(divisor, (int, float, complex)):
    # comprobamos que el divisor no es cero
        if divisor != 0:
            resultado = dividendo/divisor
        else:
            resultado = 0
        return resultado
    else:
        return 0
    
print(hazDivision(4,"a"))


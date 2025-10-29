dividendo = 4
divisor = 0

try:
    divisioon = dividendo/divisor
except ZeroDivisionZero:
    print("Tienes un error de división por cero")
except: Exception as mierror:
    print("Hay un error")
    print(mierror)

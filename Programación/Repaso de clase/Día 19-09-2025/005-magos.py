# Pedir edad
edad_mago = input("Introduce la edad del mago: ")
# Convertir a entero
try:
    edad_mago = int(edad_mago)
    print("He convertido la edad del mago correctamente")
# Si falla, pon 100
except:
    edad_mago = 100
    print("No he convertido la edad del mago correctamente")
# Clasifica por edad
clasificacion_mago = ""
# menor de 30 aprendiz
if edad_mago < 30:
    clasificacion_mago = "Aprendiz"
# de 30 a 99 es hechicero
elif edad_mago >= 30 and edad_mago <=99:
    clasificacion_mago = "Hechicero"
# mas de 100 es archimago
elif edad_mago >=100:
    clasificacion_mago = "Archimago"
print("El mago es ",clasificacion_mago)

# funcion poderBase, recibe edad, devuelve entero
# si es aprendiz, devuelve 5
# si es aprendiz, devuelve 8
# si es aprendiz, devuelve 10

# empezamos bucle
# escudo empieza con 15 puntos
#recorre dos turnos con for
# turno 1 fuego daño = poderBase // 2
# turno 2 hechizo rayo = daño = poderBase // 3
# resta el daño al escudo
# si energia escudo baja de cero, ajusta a cero

# tras cada daño, print de daño y mayor que cero
# tras ajuste nergia, print y energia es mayor que cero

# salida: edad, rango, poder baso, energia del escudo
# energia es cero, mago rompe escudo
# energia mayor que cero, escudo resiste duelo

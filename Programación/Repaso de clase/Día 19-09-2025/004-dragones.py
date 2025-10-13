#En este bloque tomo los datos del usuario

nombre_dragon_a = input("Dime el nombre del dragón A: ")
edad_dragon_a = input("Dime la edad del dragón A: ")
clasificacion_dragon_a = ""
fuerza_dragon_a = 0
resistencia_dragon_a = 0

print("El nombre del dragón A es: ",nombre_dragon_a)
print("La edad del dragón A es: ",edad_dragon_a)

nombre_dragon_b = input("Dime el nombre del dragón B: ")
edad_dragon_b = input("Dime la edad del dragón B: ")
clasificacion_dragon_b = ""
fuerza_dragon_b = 0
resistencia_dragon_b = 0

print("El nombre del dragón B es: ",nombre_dragon_b)
print("La edad del dragón B es: ",edad_dragon_b)

# En este bloque me aseguro que son enteros

try:
    edad_dragon_a = int(edad_dragon_a)
    print("He convertido la edad A correctamente")
except:
    edad_dragon_a = 100
    print("No he convertido la edad A correctamente, asigno 100")
    
try:
    edad_dragon_b = int(edad_dragon_b)
    print("He convertido la edad B correctamente")
except:
    edad_dragon_b = 100
    print("No he convertido la edad B correctamente, asigno 100")
  
# En este bloque clasifico a los dragones

if edad_dragon_a < 50:
    clasificacion_dragon_a = "Joven"
elif edad_dragon_a >= 50 and edad_dragon_a <= 199:
    clasificacion_dragon_a = "Adulto"
elif edad_dragon_a >= 200:
    clasificación_dragon_a = "Anciano"
print("El dragón A es: ",clasificacion_dragon_a)

if edad_dragon_b < 50:
    clasificación_dragon_b = "Joven"
elif edad_dragon_b >= 50 and edad_dragon_b <= 199:
    clasificacion_dragon_b = "Adulto"
elif edad_dragon_b >= 200:
    clasificación_dragon_b = "Anciano"
print("El dragón B es: ",clasificacion_dragon_b)

# Ahora los vamos a entrenar

for dia in range (1,4):
    # Como entrenar a tu dragón A
    if clasificacion_dragon_a == "Joven":
        fuerza_dragon_a += 2
        resistencia_dragon_a += 2
    elif clasificacion_dragon_a == "Adulto":
        fuerza_dragon_a += 1
        resistencia_dragon_a += 1
    elif clasificacion_dragon_a == "Anciano":
        fuerza_dragon_a += 1
        resistencia_dragon_a += 1
    print("Final del día,",dia)
    print("El dragón A ahora tiene ",fuerza_dragon_a,"de fuerza y ",resistencia_dragon_a,"de resistencia") 
    # Como entrenar a tu dragón B
    if clasificacion_dragon_b == "Joven":
        fuerza_dragon_b += 2
        resistencia_dragon_b += 2
    elif clasificacion_dragon_b == "Adulto":
        fuerza_dragon_b += 1
        resistencia_dragon_b += 1
    elif clasificacion_dragon_b == "Anciano":
        fuerza_dragon_b += 1
        resistencia_dragon_b += 1
    print("Final del día,",dia)
    print("El dragón B ahora tiene ",fuerza_dragon_b,"de fuerza y ",resistencia_dragon_b,"de resistencia")

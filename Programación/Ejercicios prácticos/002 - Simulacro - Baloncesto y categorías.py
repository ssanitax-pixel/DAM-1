'''
    Baloncesto y categorías
    v1.0 Ana Sánchez Suárez
    En este programa te dice en que categoría de baloncesto estás dependiendo de tu edad
'''
# Preguntamos la edad en números enteros
edad = int(input("¿Qué edad tienes?: "))

# Utilizamos las estructuras de control if/elif/else para saber que categoría corresponde al usuario
if edad < 8:
    categoria = "pre-mini"

elif edad >= 8 and edad < 12:
    categoria = "mini"

elif edad >= 12 and edad < 16:
    categoria = "infantil"

elif edad >= 16 and edad < 18:
    categoria = "cadete"

elif edad >= 18 and edad < 20:
    categoria = "junior"

else:
    categoria = "senior"

# Mostramos por pantalla la edad del usuario y su categoría
print("Tu edad es",edad,", entonces estás en la categoría",categoria)

# Además si el jugador sobrepasa los 40 mostraremos por pantalla lo siguiente:
if edad > 40:
    print("Además eres un veterano con experiencia en la cancha")

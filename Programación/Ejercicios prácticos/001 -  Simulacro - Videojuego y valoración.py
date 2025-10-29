'''    
    Juegos y valoración
    v1.0 Ana Sánchez Suárez
    Este programa pide un videojuego, una puntiación y muestra por pantalla el nombre del juego y el doble de su puntuación.
'''

video_juego = input("¿Cuál es tu videojuego favorito?: ")
valoracion = input("¿Qué nota le pondrías del 1 al 10?: ")

entero = int(valoracion)

print("Tu videojuego favorito es",video_juego,"y el doble de la puntuación que le has dado es",entero*2)

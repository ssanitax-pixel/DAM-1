import random

'''
    Juego en el que el jugador intenta adivinar un número secreto entre 1 y 50.
    
    El usuario tiene 6 intentos para adivinar el número. El programa da pistas sobre si
    el intento es demasiado alto o bajo, y al tercer intento ofrece una pista sobre paridad.
    v1.0 Ana Sánchez Suárez
'''
    
# Generar el número secreto
numero_secreto = random.randint(1, 50)

# Aseguramos que el número secreto está en el rango [1,50]
assert 1 <= numero_secreto <= 50, "El número secreto debe estar entre 1 y 50."

intentos = 0  # Contador de intentos

# Comenzar el juego
while intentos < 6:
    try:
        # Solicitar un número al usuario
        intento = input("Intento "+str(intentos + 1)+"/6: Adivina el número (1-50): ")
        intento = int(intento)  # Convertir la entrada a entero
        
        # Validar el número dentro del rango
        if intento < 1 or intento > 50:
            print("¡El número debe estar entre 1 y 50! Intenta de nuevo.")
            continue  # No cuenta como intento

    except ValueError:
        # Si la entrada no es un número entero
        print("¡Entrada inválida! Debes ingresar un número entero.")
        continue  # No cuenta como intento

    # Incrementamos el contador de intentos
    intentos += 1

    # Aserción para verificar que el contador de intentos no sea negativo
    assert intentos >= 0, "El contador de intentos no puede ser negativo."
    
    # Comprobar si el intento es correcto
    if intento == numero_secreto:
        print("¡Felicidades! Adivinaste el número secreto " +str(numero_secreto)+" en ",intentos," intentos.")
        break  # Finaliza el juego si el usuario adivinó correctamente
    elif intento < numero_secreto:
        print("Demasiado bajo.")
    else:
        print("Demasiado alto.")

    # Después del tercer intento, dar una pista de paridad
    if intentos == 3:
        if numero_secreto % 2 == 0:
            print("Pista: El número secreto es par.")
        else:
            print("Pista: El número secreto es impar.")

# Si se terminó el bucle sin adivinar
if intento != numero_secreto:
    print("Perdiste. El número secreto era "+str(numero_secreto)+".")
    


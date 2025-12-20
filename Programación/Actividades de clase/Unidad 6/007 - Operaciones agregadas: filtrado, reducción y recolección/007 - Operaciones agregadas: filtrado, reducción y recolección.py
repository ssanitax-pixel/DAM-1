import random

# Definimos el patrón como un conjunto
patron = {1, 2, 3, 4, 5, 6, 7, 8, 9}

def generar_sudoku():
    matriz = [[0 for _ in range(9)] for _ in range(9)]
    
    for f in range(9):
        for c in range(9):
            # Operaciones agregadas usando conjuntos:
            en_fila = set(matriz[f])
            en_columna = {matriz[i][c] for i in range(9)}
            
            # Determinamos el cuadrante 3x3
            f_inicio, c_inicio = (f // 3) * 3, (c // 3) * 3
            en_cuadrante = {
                matriz[i][j] 
                for i in range(f_inicio, f_inicio + 3) 
                for j in range(c_inicio, c_inicio + 3)
            }
            
            # FILTRADO: Los números disponibles son el patrón menos lo ya usado
            disponibles = list(patron - en_fila - en_columna - en_cuadrante)
            
            if disponibles:
                matriz[f][c] = random.choice(disponibles)
            else:
                # Si fallamos, reintentamos (recursión)
                return generar_sudoku()
    return matriz

# Ejecutamos
sudoku = generar_sudoku()

# Eliminamos 5 números aleatorios
for _ in range(5):
    sudoku[random.randint(0,8)][random.randint(0,8)] = 0

# Mostramos resultado
for fila in sudoku:
    print(fila)

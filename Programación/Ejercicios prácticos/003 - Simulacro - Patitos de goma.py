'''
    Ejercicio: Contando patitos de goma
    Escribe un programa en Python que utilice bucles for para simular el conteo de patitos de goma en una fábrica.
    
    El programa debe correr:
    Los años de producción (por ejemplo, de 2000 a 2025).
    Los meses del año (de 1 a 12).
    Los días del mes (del 1 al 30).
    Por cada día, el programa mostrará un mensaje indicando cuántos patitos de goma se han fabricado ese día.
    Requisitos adicionales:
    Cada día se fabrican exactamente 10 patitos de goma.
    El programa debe mostrar mensajes como:
    Día 5 del mes 3 del año 2010: 10 patitos de goma fabricados
    Al terminar el bucle, el programa debe mostrar el total de patitos fabricados en todo el período.
'''
patitos = 0
for anio in range(2000,2026):
    for mes in range(1,13):
        for dia in range(1,31):
            patitos += 10
            print("Día",dia,"del mes",mes,"del año",anio,", se han fabricado: 10 patitos")
            print("Día",dia,"del mes",mes,"del año",anio,"llevamos",patitos,"patitos fabricados")
        print("En total, en este período hemos fabricado",patitos,"patitos de goma")

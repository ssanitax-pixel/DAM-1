from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    # Configuramos el diseño y los colores
    cadena = '''
    <!doctype html>
    <html lang="es">
    <head>
        <meta charset="utf-8">
        <style>
            body { font-family: sans-serif; background: #e9ecef; color: #333; }
            h1 { text-align: center; color: #2c3e50; }
            .contenedor-anual { display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; }
            .mes { background: white; border-radius: 8px; padding: 15px; width: 300px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
            .mes h2 { text-align: center; color: PaleVioletRed; font-size: 1.2em; margin-top: 0; }
            .cuadricula { display: grid; grid-template-columns: repeat(7, 1fr); gap: 2px; }
            .dia { padding: 8px; text-align: center; background: #f8f9fa; border-radius: 3px; font-size: 0.85em; }
            .cabecera { font-weight: bold; background: none; color: #777; font-size: 0.75em; }
            .vacio { background: none; }
            .finde { background: #ffe3e3; color: #e74c3c; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>Calendario Anual Dinámico 2025</h1>
        <div class="contenedor-anual">
    '''

    dia_semana_actual = 2 # Suponemos que el año empieza en miércoles (2)
    nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    for i in range(12):
        cadena += f'<div class="mes"><h2>{nombres_meses[i]}</h2><div class="cuadricula">'
        
        # Ponemos la cabecera de la semana
        for d in ["L", "M", "X", "J", "V", "S", "D"]:
            cadena += f'<div class="dia cabecera">{d}</div>'

        # Añadimos los huecos vacíos del inicio del mes
        for v in range(dia_semana_actual):
            cadena += '<div class="dia vacio"></div>'

        # Generamos los 30 días del mes
        for dia in range(1, 31):
            # Calculamos si es sábado (5) o domingo (6)
            posicion_semana = (dia_semana_actual + dia - 1) % 7
            clase = "finde" if posicion_semana >= 5 else ""
            
            cadena += f'<div class="dia {clase}">{dia}</div>'

        # Actualizamos el inicio del siguiente mes
        dia_semana_actual = (dia_semana_actual + 30) % 7
        cadena += '</div></div>'

    cadena += '</div></body></html>'
    return cadena

if __name__ == "__main__":
    aplicacion.run(debug=True)

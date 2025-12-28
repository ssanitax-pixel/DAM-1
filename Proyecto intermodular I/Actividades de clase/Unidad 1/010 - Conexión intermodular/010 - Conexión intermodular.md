Empleamos Flask porque es un microservidor web que nos permite enviar código HTML generando mediante algoritmos de Python. En lugar de escribir cada día a mano, usamos bucles `for` para automatizar la creación de elementos visuales en el navegador.

---

Importamos flask para crear la aplicación.

```
from flask import Flask
```

Creamos la aplicación.

```
aplicacion = Flask(__name__)
```

Definimos la ruta.

```
@aplicacion.route("/")
def raiz():
```

Creamos el HTML como una cadena

```
cadena = '''
<!doctype html>
<html lang="es">
...
'''
```

Dentro del `<style>` definimos el diseño y los colores.

```
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
```

Creamos la variable que representa el dia de la semana en la que empieza el mes.

```
    dia_semana_actual = 2
```

Creamos una lista con los nombres de los 12 meses.

```
    nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
```

Usamos un bucle `for` para crear los 12 meses.

```
    for i in range(12):
```

Creamos la cabecera de los días, se hace una vez por cada mes.

```
for d in ["L", "M", "X", "J", "V", "S", "D"]:
    cadena += f'<div class="dia cabecera">{d}</div>'
```

Creamos los espacios vacíos antes del día uno en los meses que sea necesario.

```
for v in range(dia_semana_actual):
    cadena += '<div class="dia vacio"></div>'
```

Creamos los días del mes.

```
for dia in range(1, 31):
```

Calculamos en qué día va cada número.

```
posicion_semana = (dia_semana_actual + dia - 1) % 7
```

Marcamos los fines de semana.

```
clase = "finde" if posicion_semana >= 5 else ""
```

Añadimos el día al HTML, creamos una fila con el número de día, y si es fin de semana, se pinta diferente.

```
cadena += f'<div class="dia {clase}">{dia}</div>'
```

Ajustamos el inicio del siguiente mes.

```
dia_semana_actual = (dia_semana_actual + 30) % 7
```

Cerramos etiquetas HTML.

```
cadena += '</div></div>'
```

```
cadena += '</div></body></html>'
return cadena
```

Ejecutamos el servidor.

```
if __name__ == "__main__":
    aplicacion.run(debug=True)
```

---

El código se ve así:

```
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
```

---

Hemos comprobado que la potencia de Flask reside en su capacidad para mezclar lógica con diseño web. Al automatizar la creación de calendarios, reducimos la carga de trabajo manual, acortamos el código y aseguramos que la interfaz sea dinámica.

En este ejercicio se ha desarrollado una aplicación web dinámica utilizando `Flask`. El objetivo principal es mejorar la experiencia del usuario mediante una interfaz que no sea tosca, permitiendo gestionar la información de los clientes de forma rápida.
Para lograrlo, hemos separado el proyecto en dos partes, front y back.

---

Vamos a explicar como funciona cada archivo de nuestro sistema:

**A. El servidor de datos:** `app.py`

Utilizaremos Python para la lógica.
- Simulación de Base de datos: Como todavía estamos en la fase prototipo, guardamos los datos en una lista de diccionarios llamada `clientes_bd`.
- Gestión de rutas: Usamos `@app.route` para capturar peticiones del navegador.
- Lógica de eliminación: Cuando recibinos un ID mediante método `POST`, recorremos la lista con un bucle `for` y usamos `.remove()` para borrar al cliente seleccionado.

**B. La interfaz pública:** `clientes.html`

Este archivo servirá como puerta de entrada de nuevos clientes.
- Jinja2: Usamos las llaves `{{}}` para pintar el nombre y el correo de cada cliente que hay en nuestra lista.
- Formulario de registro: Usamos etiquetas `<input>` para recoger los datos y enviarlos al servidor mediante una petición de tipo `POST`.

**C. El Panel de Administración:** `admin_clientes.html`

Hemos creado una tabla funcional para gestionar los datos.
- Tablas de gestión: Organizamos los datos en filas (`tr`) y en celdas (`td`) para que la información sea fácil de leer.
- Acciones CRUD: Incluimos un formulario oculto por cada fila que contiene el ID del cliente. Al pulsar el botón de borrar, enviamos ese ID específico para que el servidor sepa exactamente a quién eliminar.

---

El código quedará así:

index.py

```
from flask import Flask, render_template, request, g

app = Flask(__name__)

# Simulamos una base de datos local
clientes_db = [
    {'id': '1', 'nombre': 'Juan', 'apellidos': 'Pérez', 'correo': 'juan@mail.com'},
    {'id': '2', 'nombre': 'Maria', 'apellidos': 'Garcia', 'correo': 'maria@mail.com'}
]

@app.route('/clientes', methods=['GET', 'POST'])
def gestion_clientes():
    if request.method == 'POST':
        # Añadimos un cliente nuevo
        nuevo = {
            'id': str(len(clientes_db) + 1),
            'nombre': request.form['nombre'],
            'apellidos': request.form['apellidos'],
            'correo': request.form['correo']
        }
        clientes_db.append(nuevo)
    return render_template('clientes.html', clientes=clientes_db)

@app.route('/admin/clientes', methods=['GET', 'POST'])
def admin_clientes():
    if request.method == 'POST':
        id_a_borrar = request.form['id']
        # Recorremos la lista para buscar y eliminar al cliente
        for cliente in clientes_db:
            if cliente['id'] == id_a_borrar:
                clientes_db.remove(cliente)
                break
    return render_template('admin_clientes.html', clientes=clientes_db)

if __name__ == "__main__":
    app.run(debug=True)
```

clientes.html

```
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Restaurante - Clientes</title>
    <style>
        body { font-family: sans-serif; background: #eee; padding: 20px; }
        .ficha { background: white; padding: 10px; margin-bottom: 5px; border-radius: 4px; }
    </style>
</head>
<body>
    <h1>Nuestros Clientes</h1>
    {% for c in clientes %}
        <div class="ficha">{{ c.nombre }} {{ c.apellidos }} ({{ c.correo }})</div>
    {% endfor %}
    <hr>
    <form action="/clientes" method="POST">
        <input type="text" name="nombre" placeholder="Nombre" required>
        <input type="text" name="apellidos" placeholder="Apellidos" required>
        <input type="email" name="correo" placeholder="Email" required>
        <button type="submit">Registrar</button>
    </form>
    <br>
    <a href="/admin/clientes">Ir al Panel de Control</a>
</body>
</html>
```

admin_clientes.html

```
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Admin - Clientes</title>
    <style>
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid black; padding: 8px; text-align: left; }
        th { background: #333; color: white; }
        button { background: red; color: white; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Panel de Administración</h1>
    <table>
        <tr>
            <th>ID</th><th>Nombre</th><th>Acciones</th>
        </tr>
        {% for c in clientes %}
        <tr>
            <td>{{ c.id }}</td>
            <td>{{ c.nombre }} {{ c.apellidos }}</td>
            <td>
                <form action="/admin/clientes" method="POST">
                    <input type="hidden" name="id" value="{{ c.id }}">
                    <button type="submit">Eliminar Cliente</button>
                </form>
            </td>
        </tr>
        {% endfor %}
    </table>
    <br>
    <a href="/clientes">Volver a la web pública</a>
</body>
</html>
```

--- 

Hemos pasado de una idea inicial (mejorar la gestión de un restaurante) a un producto tecnológico funcional. Nosotros hemos integrado el Backend con Python y el Frontend con HTML dinámico, sentando las bases para aplicaciones más complejas.
Como nosotros somos responsables de cómo la tecnología ayuda a las personas, crear sistemas automatizados nos permite reducir la carga de trabajo y aumentar la disponibilidad del servicio.

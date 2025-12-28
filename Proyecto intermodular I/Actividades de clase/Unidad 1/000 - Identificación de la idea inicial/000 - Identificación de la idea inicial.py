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

Trabajamos en formato JSON, ya que es eficiente y tiene buena escalabilidad, además se ha convertido en el estándar de la industria para el intercambio de datos debido a su ligereza y a que es fácilmente legible tanto por nosotros como por las máquinas.
En esta accividad, veremos lo que es la arquitectura desacoplada, donde la información reside en un archivo independiente y la lógica del servidor o del cliente se encarga de que se visualicen esos datos en el navegador. Al usar Flask como microservidor, logramos gestionar estas peticiones de forma profesional, permitiendo que un solo archivo de Python sirva de puente entre nuestra estructura de datos y las plantillas dinámicas de Jinja2.

---

Parte de Python.
Importamos las librerías necesarias.

```
from flask import Flask, render_template
import json
```

Creamos la aplicación Flask.

```
app = Flask(__name__)
```

Definimos una ruta web.

```
@app.route("/")
def inicio():
```

Para poder leer el archivo JSON ponemos lo siguiente.

```
with open("static/curriculum.json", "r", encoding="utf-8") as file:
    datos = json.load(file)
```

Enviamos los datos al HTML.

```
return render_template("index.html", info=datos)
```

Arrancamos el servidor.

```
if __name__ == "__main__":
    app.run(debug=True)
```

Creamos el archivo JSON, donde estarán todos los datos que queremos meter, este archivo es una base de datos ligera.

```
{
  "nombre": "Ana",
  "apellidos": "Sánchez Suárez",
  "correo": "ssanitax@gmail.com",
  ...
}
```

Por último crearemos el archivo HTML.
Creamos variables dinámicas, que se completarán con datos del JSON.

```
<title>Curriculum Vitae - {{ info.nombre }}</title>
```

Creamos una lista dinámica con un bucle `for` para que recorra la lista de habilidades.

```
{% for habilidad in info.habilidades %}
  <li>{{ habilidad }}</li>
{% endfor %}
```

Separamos el documento en dos columnas.

```
<div id="izquierda">...</div>
<div id="derecha">...</div>
```

---

Código de `102 - Leer JSON.py`

```
# Importamos las librerías necesarias para la web y los datos
from flask import Flask, render_template
import json

# Ceamos la aplicación
app = Flask(__name__)

# Definimos la ruta principal
@app.route("/")
def inicio():
    # Abrimos el JSON mejorado
    with open("static/curriculum.json", "r", encoding="utf-8") as file:
        datos = json.load(file)
    
    # Renderizamos la plantilla enviando los datos estructurados
    return render_template("index.html", info=datos)

# Arrancamos el servidor en modo desarrollo
if __name__ == "__main__":
    app.run(debug=True)
```

Código de `static/curriculum.json`

```
{
  "nombre": "Ana",
  "apellidos": "Sánchez Suárez",
  "correo": "ssanitax@gmail.com",
  "perfil": "Desarrolladora Full Stack Junior con enfoque en Python y SQL.",
  "habilidades": ["Python", "Flask", "MySQL", "HTML5", "CSS Grid"],
  "experiencia": [
    {"puesto": "Prácticas de Desarrollo", "empresa": "Tech Solutions", "año": "2024"},
    {"puesto": "Copywriting Digital", "empresa": "CitySem", "año": "2023"}
  ]
}
```

Código de `templates/index.html`

```
<!doctype html>
<html lang="es">
  <head>
    <title>Curriculum Vitae - {{ info.nombre }}</title>
    <meta charset="utf-8">
    <style>
      html { background: #f0f2f5; font-family: 'Segoe UI', sans-serif; }
      body { 
        background: white; 
        margin: 40px auto; 
        display: flex; 
        width: 850px; 
        min-height: 600px; 
        box-shadow: 0 0 20px rgba(0,0,0,0.1); 
      }
      #izquierda { flex: 1; background: #1a2a6c; color: white; padding: 30px; }
      #derecha { flex: 2.5; background: white; padding: 40px; color: #333; }
      
      h1 { margin: 0; color: #1a2a6c; text-transform: uppercase; }
      h3 { border-bottom: 2px solid #1a2a6c; padding-bottom: 5px; margin-top: 30px; }
      ul { padding-left: 20px; }
      .puesto { font-weight: bold; margin-bottom: 0; }
      .empresa { color: #666; font-style: italic; margin-top: 0; }
    </style>
  </head>
  <body>
    <div id="izquierda">
      <h3>Contacto</h3>
      <p>📧 {{ info.correo }}</p>
      
      <h3>Habilidades</h3>
      <ul>
        {% for habilidad in info.habilidades %}
          <li>{{ habilidad }}</li>
        {% endfor %}
      </ul>
    </div>

    <div id="derecha">
      <h1>{{ info.nombre }} {{ info.apellidos }}</h1>
      <p><strong>Perfil:</strong> {{ info.perfil }}</p>

      <h3>Experiencia Laboral</h3>
      {% for exp in info.experiencia %}
        <div class="bloque-exp">
          <p class="puesto">{{ exp.puesto }}</p>
          <p class="empresa">{{ exp.empresa }} | {{ exp.año }}</p>
        </div>
      {% endfor %}
    </div>
  </body>
</html>
```

---

Hemos realizado una práctica que nos permite comprender cómo se construyen las aplicaciones web dinámicas reales. La gran ventaja de este sistema es su modularidad: si nosotros necesitamos cambiar el número de teléfono o la dirección de alguien, solo tenemos que editar el archivo JSON, sin tocar ni una sola línea del código de Python o de la estructura HTML.
La separación de responsabilidades (donde los datos, la lógica y la vista están aislados) es el pilar de arquitecturas más complejas como el modelo MVC (Modelo-Vista-Controlador). Además, el dominio de herramientas como fetch y Flask nos da la versatilidad necesaria para trabajar tanto en el Frontend como en el Backend, preparándonos para crear sitios web altamente personalizados, escalables y fáciles de mantener en el futuro.

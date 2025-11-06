from flask import Flask # Importo flask
import mysql.connector  # Importo el conector a base de datos

conexion = mysql.connector.connect(
    host="localhost",      
    user="usuario1",    
    password="Portafolio123#",  
    database="portafolio"      
    ) # Me conecto a la base de datos
cursor = conexion.cursor() # Creo un cursor
app = Flask(__name__) # creo una aplicacion flask (web)

@app.route("/") # Atrapo la ruta raiz (/)
def raiz(): # defino la funcion
    cursor.execute("SELECT * FROM vista_categorias;") # Pido el contenido de la vista

    resultados = cursor.fetchall() # Lo guardo en una lista
    ####### AQUI PONGO EL INICIO HASTA EL MAIN
    cadena = '''
    <!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portafolio de Arte</title>
    <style>
      /* Reset general */
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }

      /* Body y fondo */
      body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        background-color: #f4f4f4;
        color: #333;
      }

      /* Header */
      header {
        background-color: #333;
        color: white;
        padding: 20px;
        text-align: center;
      }

      header h1 {
        margin: 10px 0;
      }

      header p {
        font-size: 1.1rem;
        margin-top: 5px;
      }

      /* Main */
      main {
        padding: 20px;
      }

      .portfolio {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 20px;
      }

      .piece {
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s;
      }

      .piece:hover {
        transform: scale(1.05);
      }

      .piece-title {
        font-size: 1.5rem;
        color: #333;
        margin-bottom: 10px;
      }

      .piece-description {
        font-size: 1rem;
        margin-bottom: 10px;
      }

      .piece-image {
        width: 100%;
        border-radius: 8px;
        margin-bottom: 10px;
      }

      .piece-category {
        font-weight: bold;
        font-size: 1.1rem;
      }

      /* Footer */
      footer {
        background-color: #333;
        color: white;
        text-align: center;
        padding: 15px;
        position: relative;
        width: 100%;
        bottom: 0;
      }
    </style>
  </head>
  <body>

    <!-- Header -->
    <header>
      <div class="header-content">
        <h1>Ana Sánchez Suárez - Portafolio</h1>
        <p>Email: ssanitax@gmail.com</p>
      </div>
    </header>

    <!-- Main -->
    <main>
    '''
    ####### AQUI PONGO LO QUE SE REPITE
    for fila in resultados: # Para cada elemento de la lista
        cadena += str(fila) # Añado el registro a la cadena
    ####### AQUI PONGO EL FINAL
    cadena += '''
    </main>

    <!-- Footer -->
    <footer>
      <p>&copy; 2025 Ana Sánchez Suárez. Todos los derechos reservados.</p>
    </footer>

  </body>
</html>
    '''
    return cadena
      
if __name__ == "__main__": # si este es el archivo principal
    app.run(debug=True) # ejecuta la web

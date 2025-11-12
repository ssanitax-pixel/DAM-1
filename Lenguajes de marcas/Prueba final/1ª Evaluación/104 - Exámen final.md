En este ejercicio, creamos un portfolio digital utilizando HTML y CSS. Primero, estructuramos el contenido con un encabezado, una sección principal con artículos que muestran las piezas del portfolio, y un pie de página. Luego, aplicamos CSS para mejorar la presentación visual, utilizando una cuadrícula para organizar las piezas y efectos de hover para mayor interactividad.

---

Vamos a hacer un front simulado del portfolio en HTML y CSS.

Para empezar hacemos una estructura HTML básica y legal.

```
<!DOCTYPE html>
<html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
    </body>
</html>
```

Ahora en `<body>` vamos a crear header, main y footer.

```
<!DOCTYPE html>
<html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
      <header>
      </header>
      <main>
      </main>
      <footer>
      </footer>
    </body>
</html>
```

En el header, ponemos nuestro nombre y nuestro email.

```
    <header>
      <div>
        <h1>Ana Sánchez Suárez - Portafolio</h1>
        <p>Email: ssanitax@gmail.com</p>
      </div>
    </header>
```

En el footer pondremos un mensaje de Copyright.

```
    <footer>
      <p>&copy; 2025 Ana Sánchez Suárez. Todos los derechos reservados.</p>
    </footer>
```

En `main`, crearemos una lista de artículos, cada uno con un proyecto.

```
        <article class="piece">
          <h2 class="piece-title">AniWay</h2>
          <p class="piece-description">Proyecto que ayuda a calcular el dinero que debe al conductor según los kilómetros que ha hecho de viaje</p>
          <p class="piece-category"><strong>Categoría:</strong> Viajes</p>
          <a href="https://github.com/aniway" target="_blank">Ver proyecto</a>
        </article>
```

Por último, pondremos el CSS, en este caso lo haremos dentro del HTML dentro del head, poniendo lo siguiente.

```
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
        background-color: PaleVioletRed;
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
        background-color: PaleVioletRed;
        color: white;
        text-align: center;
        padding: 15px;
        position: relative;
        width: 100%;
        bottom: 0;
      }
    </style>
```

---

El HTML completo se verá así:

```
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
        background-color: PaleVioletRed;
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
        background-color: PaleVioletRed;
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
      <section class="portfolio">
        <article class="piece">
          <h2 class="piece-title">AniWay</h2>
          <p class="piece-description">Proyecto que ayuda a calcular el dinero que debe al conductor según los kilómetros que ha hecho de viaje</p>
          <p class="piece-category"><strong>Categoría:</strong> Viajes</p>
          <a href="https://github.com/aniway" target="_blank">Ver proyecto</a>
        </article>

        <article class="piece">
          <h2 class="piece-title">AniWord</h2>
          <p class="piece-description">Proyecto de aplicación que sirve para aprender inglés.</p>
          <p class="piece-category"><strong>Categoría:</strong> Idiomas</p>
          <a href="https://galeriaarte.com/guerrero-en-accion" target="_blank">Ver proyecto</a>
        </article>
        
        <article class="piece">
          <h2 class="piece-title">AniWay</h2>
          <p class="piece-description">Proyecto que ayuda a calcular el dinero que debe al conductor según los kilómetros que ha hecho de viaje</p>
          <p class="piece-category"><strong>Categoría:</strong> Viajes</p>
          <a href="https://github.com/aniway" target="_blank">Ver proyecto</a>
        </article>

        <article class="piece">
          <h2 class="piece-title">AniWord</h2>
          <p class="piece-description">Proyecto de aplicación que sirve para aprender inglés.</p>
          <p class="piece-category"><strong>Categoría:</strong> Idiomas</p>
          <a href="https://galeriaarte.com/guerrero-en-accion" target="_blank">Ver proyecto</a>
        </article>
        
        <article class="piece">
          <h2 class="piece-title">AniWay</h2>
          <p class="piece-description">Proyecto que ayuda a calcular el dinero que debe al conductor según los kilómetros que ha hecho de viaje</p>
          <p class="piece-category"><strong>Categoría:</strong> Viajes</p>
          <a href="https://github.com/aniway" target="_blank">Ver proyecto</a>
        </article>

        <article class="piece">
          <h2 class="piece-title">AniWord</h2>
          <p class="piece-description">Proyecto de aplicación que sirve para aprender inglés.</p>
          <p class="piece-category"><strong>Categoría:</strong> Idiomas</p>
          <a href="https://galeriaarte.com/guerrero-en-accion" target="_blank">Ver proyecto</a>
        </article>
        
      </section>
    </main>

    <!-- Footer -->
    <footer>
      <p>&copy; 2025 Ana Sánchez Suárez. Todos los derechos reservados.</p>
    </footer>

  </body>
</html>
```

---

Este ejercicio nos permitió practicar la creación de una página web básica, aprendiendo a estructurar contenido con HTML y a aplicar estilos visuales con CSS. El resultado es un portfolio funcional y estéticamente agradable para mostrar el trabajo de un programador.

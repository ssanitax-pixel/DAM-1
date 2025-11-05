En este ejercicio, creamos un portfolio digital utilizando `HTML` y `CSS`. Primero, estructuramos el contenido con un encabezado, una sección principal con artículos que muestran las piezas del portfolio, y un pie de página. Luego, aplicamos `CSS` para mejorar la presentación visual, utilizando una cuadrícula para organizar las piezas y efectos de hover para mayor interactividad.

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

En el `header`, ponemos nuestro nombre y nuestro email.

```
    <header>
      <div>
        <h1>Ana Sánchez Suárez - Portafolio</h1>
        <p>Email: ssanitax@gmail.com</p>
      </div>
    </header>
```

En el `footer` pondremos un mensaje de Copyright.

```
    <footer>
      <p>&copy; 2025 Ana Sánchez Suárez. Todos los derechos reservados.</p>
    </footer>
```

En main, crearemos una lista de artículos, cada uno con una pieza del portafolio.

```
        <article>
          <h2>La mañana sobre el río</h2>
          <p>Óleo sobre lienzo que representa un amanecer en un paisaje fluvial. Destaca por el uso de luces suaves y reflejos en el agua.</p>
          <img src="la_manana_sobre_el_rio.jpg" alt="La mañana sobre el río" class="piece-image">
          <p><strong>Categoría:</strong> Pintura</p>
          <a href="https://galeriaarte.com/la-manana-sobre-el-rio" target="_blank">Ver en la galería</a>
        </article>
```

Por último, pondremos el CSS, en este caso lo haremos dentro del HTML dentro del `head`, poniendo lo siguiente.

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
```

---

El `HTML` completo se verá así.

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
      <section class="portfolio">
        <article class="piece">
          <h2 class="piece-title">Atardecer en la montaña</h2>
          <p class="piece-description">Óleo sobre lienzo que muestra un paisaje montañoso al atardecer, con colores cálidos y contrastes de luz.</p>
          <img src="atardecer_montana.jpg" alt="Escultura de mármol" class="piece-image">
          <p class="piece-category"><strong>Categoría:</strong> Pintura</p>
          <a href="https://galeriaarte.com/guerrero-en-accion" target="_blank">Ver en la galería</a>
        </article>

        <article class="piece">
          <h2 class="piece-title">Guerrero en acción</h2>
          <p class="piece-description">Escultura en bronce que representa a un guerrero en plena acción, con gran realismo en los detalles anatómicos.</p>
          <img src="guerrero_en_accion.jpg" alt="Guerrero en acción" class="piece-image">
          <p class="piece-category"><strong>Categoría:</strong> Escultura</p>
          <a href="https://galeriaarte.com/guerrero-en-accion" target="_blank">Ver en la galería</a>
        </article>

        <article class="piece">
          <h2 class="piece-title">Retrato de mujer con sombrero renovado</h2>
            <p class="piece-description">Cuadro al óleo actualizado, con más detalles sobre la técnica y el autor.</p>
            <img src="retrato_mujer_sombrero_actualizado.jpg" alt="Retrato de mujer con sombrero renovado" class="piece-image">
            <p class="piece-category"><strong>Categoría:</strong> Pintura</p>
            <a href="https://galeriaarte.com/retrato-mujer-sombrero-actualizado" target="_blank">Ver en la galería</a>
        </article>
        
        <article class="piece">
          <h2 class="piece-title">Estatua del pensador moderno</h2>
          <p class="piece-description">Escultura en bronce que representa a una figura humana en actitud reflexiva. Inspirada en el pensamiento contemporáneo y la introspección.</p>
          <img src="estatua_pensador_moderno.jpg" alt="Estatua del pensador moderno" class="piece-image">
          <p class="piece-category"><strong>Categoría:</strong> Escultura</p>
          <a href="https://galeriaarte.com/estatua-pensador-moderno" target="_blank">Ver en la galería</a>
        </article>
        
        <article class="piece">
          <h2 class="piece-title">La mañana sobre el río</h2>
          <p class="piece-description">Óleo sobre lienzo que representa un amanecer en un paisaje fluvial. Destaca por el uso de luces suaves y reflejos en el agua.</p>
          <img src="la_manana_sobre_el_rio.jpg" alt="La mañana sobre el río" class="piece-image">
          <p class="piece-category"><strong>Categoría:</strong> Pintura</p>
          <a href="https://galeriaarte.com/la-manana-sobre-el-rio" target="_blank">Ver en la galería</a>
        </article>
        
        <article class="piece">
          <h2 class="piece-title">La Dama del Mar</h2>
          <p class="piece-description">Escultura abstracta en mármol que representa una figura femenina que emerge suavemente del agua, simbolizando la conexión entre la naturaleza y el ser humano.</p>
          <img src="la_dama_del_mar.jpg" alt="La Dama del Mar" class="piece-image">
          <p class="piece-category"><strong>Categoría:</strong> Escultura</p>
          <a href="https://galeriaarte.com/la-dama-del-mar" target="_blank">Ver en la galería</a>
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

Este ejercicio nos permitió practicar la creación de una página web básica, aprendiendo a estructurar contenido con HTML y a aplicar estilos visuales con CSS. El resultado es un portfolio funcional y estéticamente agradable para mostrar el trabajo de un artista.

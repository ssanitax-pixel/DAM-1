El HTML y el CSS son herramientas esenciales para crear páginas web estructuradas y visualmente atractivas. En este ejercicio, hemos aprendido a construir una página de currículum usando estas tecnologías. El HTML nos permite organizar el contenido, mientras que el CSS le da estilo y lo hace más profesional y visualmente agradable.

---

Creamos un archivo HTML, desde el editor de texto que más nos guste.

Creamos una estructura básica de HTML.

```
<!doctype html>
<html lang="es">
  <head>
    <title>Curriculum</title>
    <meta charset="utf-8">
  </head>
  <body>
    <!-- Contenido de la página -->
  </body>
</html>
```

En la etiqueta `<head>`, después de la parte del título y la codificación, agregamos una sección de estilos CSS. El código dentro de `<style>` controla cómo se ve la página web.

```
<style>
  html{
    background:grey;
    font-family:arial;
    font-size:11px;
  }
  body{
    width:600px;
    background:white;
    margin:auto;
    display:flex;
    z-index: 0;
  }
  /* Otros estilos aquí */
</style>
```

Creamos la estructura de la página, que en este caso se divide en dos secciones principales, `#izquierda` y `#derecha`.

```
<section id="izquierda">
  <!-- Aquí va el contenido izquierdo -->
</section>

<section id="derecha">
  <!-- Aquí va el contenido derecho -->
</section>
```

En la sección izquierda meteremos la imagen e información de contacto.

```
<section id="izquierda">
  <img src="imagen-personal.jpg" alt="Foto personal">
  <div id="contenido-texto">
    <article>
      <h3>Contacto</h3>
      <ul>
        <li>Valencia</li>
        <li>+34 722 28 96 95</li>
        <li>ssanitax@gmail.com</li>
      </ul>
    </article>
    <!-- Otro artículo de datos de interés -->
  </div>
</section>
```

En la sección derecha pondremos la información principal del currículum, en este caso el nombre, experiencia, formación académica...

```
<section id="derecha">
  <h1>Ana Sánchez Suárez</h1>
  <h2>Estudiante en Desarrollo de Aplicaciones Multiplataforma</h2>
  <h3>Sobre mi</h3>
  <p>Cuento con habilidades para la resolución de problemas...</p>
  <div id="experiencia">
    <h3>Experiencia profesional</h3>
    <!-- Experiencias pasadas -->
  </div>
  <div id="formacion">
    <h3>Formación académica</h3>
    <!-- Formación académica -->
  </div>
</section>
```

Importante ir visitando la página de vez en cuando para ver como va quedando y que no hay ningún error.

---

Aquí está el código completo:

```
<!doctype html>
<html lang="es">
  <head>
    <title>Curriculum</title>
    <meta charset="utf-8">
    <style>
      html{
        background:grey;
        font-family:arial;
        font-size:11px;
      }
      body{
        width:600px;
        background:white;
        margin:auto;
        display:flex;
        z-index: 0;}
      .franja-azul {
        background-color:CornflowerBlue; 
        height: 180px;             
        width: 600px;             
        position: absolute;      
        top: 0;                  
        margin: 0 auto;
      }
      h1{
        font-size:40px;
        font-family:helvetica;
        position:relative;
        z-index: 300;
        color:white;
      }
      h2{
        font-size:20px;
        font-family:helvetica;
        color:CornflowerBlue;
      }
      #izquierda img{
        width: 160px;
        height: 160px;
        object-fit: cover;
        border-radius: 50%;
        background-color: CornflowerBlue; 
        padding: 0px; 
        border: 10px solid white; 
        margin: 0 auto; 
        display: block;
        box-sizing: border-box; 
        position:relative;
      }
      #izquierda{
        flex:1;
        background:AliceBlue;
        padding:20px;
        color:black;
        margin-top:20px;
      }
      #derecha{
        flex:6;
        padding:20px;
        background-color:white;
      }
      #derecha article{
        display:flex;
        align-items:center;
        gap:20px;
      }
      #derecha article img{max-width:50px;}
      #derecha article *{
        padding:1px;
        margin:1px;
      }
      #contenido-texto {
        padding-top: 50px;
        margin-left: 5px;
      }
      
    </style>
  </head>
  <body>
    <div class="franja-azul"></div>
    <section id="izquierda">
      <img src="imagen-personal.jpg">
      <div id="contenido-texto">
      <article>
        <h3>Contacto</h3>
        <ul>
          <li>Valencia</li>
          <li>+34 722 28 96 95</li>
          <li>ssanitax@gmail.com</li>
        </ul>
      </article>
      <article>
        <h3>Datos de interés</h3>
        <ul>
          <p>Dispongo de carné de conducir y vehículo propio. Además, cuento con titulación de monitora de campamentos, lo que me ha permitido adquirir experiencia en el trato con niños y asumir responsabilidades de organización y cuidado.</p>
        </ul>
      </article>
      </div>
    </section>
    <section id="derecha">
      <h1>Ana Sánchez Suárez</h1>
      <h2>Estudiante en Desarrollo de Aplicaciones Multiplataforma</h2>
      <h3>Sobre mi</h3>
      <p>Cuento con habilidades para la resolución de problemas y mantengo siempre una actitud positiva. Tengo competencias digitales e interés constante por seguir aprendiendo. Me considero creativa y destaco por mi capacidad de trabajo en equipo.</p>
      <div id="experiencia">
        <h3>Experiencia profesional</h3>
        <article>
          <img src="kangar.png">
          <div class="texto">
            <h4>Especialista en posicionamiento SEO</h4>
            <h5>De junio a septiembre de 2023 - Kangar</h5>
            <p>Gestión de blogs en redes sociales, uso de SEMrush para SEO, investigación de palabras clave y manejo de WordPress.</p>
          </div>
        </article>
        <article>
          <img src="citysem.png">
          <div class="texto">
            <h4>Técnico Marketing y Publicidad</h4>
            <h5>De mayo a junio de 2023 - CitySem</h5>
            <p>Desarrollé tareas de copywriting digital y arquitectura web, además de la gestión de blogs en redes sociales y el diseño de logotipos. También cuento con experiencia en el uso de SEMrush, investigación de palabras clave y posicionamiento SEO.</p>
          </div>
        </article>
      </div>
      <div id="formacion">
        <h3>Formación académica</h3>
        <article>
          <img src="ceac.jpeg">
          <div class="texto">
            <h4>Desarrollo de aplicaciones multiplataforma</h4>
            <h5>Ciclo formativo de grado superior - CEAC</h5>
            <p>Valencia - Desde septiembre de 2025 hasta la actualidad</p>
          </div>
        </article>
        <article>
          <img src="angel-ganivet.jpeg">
          <div class="texto">
            <h4>Marketing y publicidad</h4>
            <h5>Ciclo formativo de grado superior - IES Ángel Ganivet</h5>
            <p>Granada - Desde septiembre de 2021 hasta junio de 2023</p>
          </div>
        </article>
      </div>
    </section> 
  </body> 
</html>
```

---

Crear un CV con HTML y CSS no solo nos ayuda a presentar nuestra información de manera clara y ordenada, sino que también nos permite personalizar su apariencia. Este ejercicio muestra cómo, a través de una estructura básica de HTML y estilos CSS, podemos diseñar un currículum que sea tanto funcional como estéticamente atractivo.

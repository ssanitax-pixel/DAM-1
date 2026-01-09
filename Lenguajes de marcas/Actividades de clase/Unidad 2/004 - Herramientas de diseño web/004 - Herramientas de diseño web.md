En esta unidad, hemos aprendido a crear la estructura básica de un documento HTML, aplicando etiquetas clave como `<head>`, `<body>`, y las etiquetas meta, que son esenciales para la optimización en motores de búsqueda (SEO). En este ejercicio, hemos creado una página web sencilla, personalizando el contenido con información sobre nuestra identidad y profesiones, además de incluir un párrafo donde describimos un hobby personal. Este párrafo tiene el propósito de mostrar cómo podemos usar la etiqueta `<p>` para agregar contenido relevante y personal a la página, lo cual contribuye tanto a la experiencia del usuario como a la autenticidad del sitio. Además, las etiquetas `<meta>` mejoran la visibilidad de la página en los motores de búsqueda, lo que es fundamental para la optimización web.

---

Abrimos nuestro editor de texto y creamos un nuevo archivo HTML.

Añadimos el siguiente código básico al archivo.

```
<!doctype html>
<html lang="es">
  <head>
    <title>Ana Sánchez Suárez</title>
    <meta charset="utf-8">
    <!-- Etiquetas de posicionamiento -->
    
  </head>
  <body>
    <header>
      <h1>Ana Sánchez Suárez</h1>
      <h2>Estudiante en Desarrollo de Aplicaciones Multiplataforma</h2>
      <nav>
        <ul>
          <li><a href="#inicio">Inicio</a></li>
          <li><a href="#sobremi">Sobre mi</a></li>
          <li><a href="#docencia">Docencia</a></li>
        </ul>
      </nav>
    </header>
  </body>
</html>
```

En la sección `<head>` el archivo, añadimos las etiquetas meta para descripción y palabras clave.

```
        <meta name="description" content="Web de Ana Sánchez Suárez, Estudiante en Desarrollo de Aplicaciones Multiplataforma">
        <meta name="keywords" content="programación,curso,diseño,IA,big data,estudiante">
```

Añadimos un nuevo párrafo en el cuerpo del documento para escribir nuestro hobby favorito.

```
                <p>Mi hobby favorito es quedarme con amigos para comer y cenar. Es una actividad relajante y divertida que disfruto mucho.</p>
```

---

Así queda el ejercicio completo:

```
<!doctype html>
<html lang="es">
  <head>
    <title>Ana Sánchez Suárez</title>
    <meta charset="utf-8">
    <!-- Etiquetas de posicionamiento -->
    <meta name="description" content="Web de Ana Sánchez Suárez, Estudiante en Desarrollo de Aplicaciones Multiplataforma">
    <meta name="keywords" content="programación,curso,diseño,IA,big data,estudiante">
    
  </head>
  <body>
    <header>
      <h1>Ana Sánchez Suárez</h1>
      <h2>Estudiante en Desarrollo de Aplicaciones Multiplataforma</h2>
      <p>Mi hobby favorito es quedarme con amigos para comer y cenar. Es una actividad relajante y divertida que disfruto mucho.</p>
      <nav>
        <ul>
          <li><a href="#inicio">Inicio</a></li>
          <li><a href="#sobremi">Sobre mi</a></li>
          <li><a href="#docencia">Estudios</a></li>
        </ul>
      </nav>
    </header>
  </body>
</html>
```

---

Este ejercicio me ha permitido practicar la creación de una página HTML básica, incorporando etiquetas meta para mejorar el SEO y un párrafo descriptivo con la etiqueta `<p>`. Al añadir el párrafo sobre un hobby, he aprendido cómo estructurar contenido dentro del cuerpo del documento. Además, las etiquetas meta ayudan a mejorar la visibilidad en los motores de búsqueda, lo que es esencial para la optimización de páginas web.

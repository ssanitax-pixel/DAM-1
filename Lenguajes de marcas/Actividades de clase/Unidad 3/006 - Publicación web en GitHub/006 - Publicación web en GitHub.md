La publicación web requiere tradicionalmente de un dominio y un hosting. Al usar GitHub pages, obenemos ambas cosas gratis: el hosting lo proporciona GitHub y el dominio sigue el formato `[tu_usuario].github.io/[tu_repositorio]`
Es importante recordar que este servicio solo admite contenido estático, no podemos ejecutar código de servidor como PHP o Python, ni conectar directamente con bases de datos MySQL desde aquí.

---

Vamos a explicar paso a paso para que nuestro currículum esté online en cuestión de minutos.

**A. Preparación del repositorio.**

Entramos en GitHub y creamos un nuevo repositorio público llamado `curriculum`. Es fundamental que el repositorio sea público para que GitHub Pages pueda servir los archivos a todo el mundo.

**B. Configuración de archivos**

Debemos asegurarnos de que el archivo principal se llame exactamente `index.html`, ya que es el archivo que el servidor buscará por defecto al cargar la web.
- HTML: Estructuramos el contenido con las etiquetas de cabecera, contenido principal y pie de página.
- CSS: Aplicamos estilos para centrar el contenido y mejorar la tipografía.

**C. El proceso de Commit y Push**

Una vez que tenemos los archivos en nuestra carpeta local, usamos Git para subir los cambios.
- Preparamos todos los archivos para subirlos.
- Guardamos nuestro progreso.
- Enviamos los archivos a la nube de GitHub.

---

El código de ejemplo será así.

index.html

```
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Curriculum - Jose Vicente Carratala</title>
  <link rel="stylesheet" href="estilo.css">
</head>
<body>
  <header>
    <h1>Jose Vicente Carratala</h1>
  </header>
  <main>
    <section>
      <h2>Hobbies</h2>
      <ul>
        <li>Hacer rutas por el campo</li>
        <li>Dar paseos por la ciudad</li>
        <li>Ver películas y series</li>
        <li>Jugar a videojuegos de Nintendo</li>
        <li>Arreglar consolas retro</li>
      </ul>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Jose Vicente Carratala. Todos los derechos reservados.</p>
  </footer>
</body>
</html>
```

estilo.css

```
header, main, footer {
  width: 1200px;
  margin: auto;
  padding: 20px;
  font-family: sans-serif;
}

main {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

header, footer {
  text-align: center;
}
```

---

Hemos comprobado que publicar una web hoy en día es un proceso rápido gracias a herramientas como GitHub. Al configurar GitHub Pages en los ajustes del repositorio, transformamos un simple código en una página web real.

La creación de páginas web requiere conocer y aplicar los elementos esenciales de la estructura de un documento HTML. En este ejercicio, se trata de desarrollar un archivo HTML básico, que incluye los elementos fundamentales como el `DOCTYPE`, la etiqueta `<html>`, las secciones `<head>` y `<body>`, y el título de la página. Estos elementos son indispensables para que una página web funcione correctamente, permitiendo que el navegador interprete y muestre el contenido de manera adecuada. La estructura básica de un documento HTML proporciona el marco necesario para organizar tanto los elementos visibles de la página como los metadatos y otros recursos invisibles, pero importantes, para el funcionamiento y optimización del sitio web.

---

Después de crear el archivo, dentro escribimos el `DOCTYPE` para indicar que estamos utilizando HTML5.

```
<!doctype>
```

Definimos la etiqueta `<html>`, con su atributo para saber que idioma tiene el documento, que en este caso será español, importante también cerrarlo.

```
    <html lang="es">
    </html>
```

Creamos dentro de `<html>` la sección `<head>`, que es donde irán los metadatos y otros elementos que no son visibles en la página, pero son importantes para su funcionamiento.

```
        <head>
        </head>
```

A continuación, dentro de la sección `<head>`, agregamos otra llamada `<title>`, con un texto descriptivo de la página.

```
            <title>Mi página</title>
```

Añadimos la sección `<body>`, importante que va dentro de `<html>` y debajo de `<head>`.

```
        <body>
        </body>
```

Así quedaría todo el código de HTML junto:

```
<!doctype>
  <html lang="es">
    <head>
      <title>Mi página</title>
    </head>
    <body>
    </body>
  </html>
```

---

Este ejercicio muestra cómo crear la estructura básica de un documento HTML, utilizando elementos clave como el `DOCTYPE`, `<html>`, `<head>` y `<body>`. Dominar esta estructura es fundamental para desarrollar páginas web, ya que establece las bases para añadir contenido y funcionalidades adicionales en proyectos más complejos.

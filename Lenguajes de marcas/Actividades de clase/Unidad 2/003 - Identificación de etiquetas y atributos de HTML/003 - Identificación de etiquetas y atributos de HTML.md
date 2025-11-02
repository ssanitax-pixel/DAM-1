En esta unidad, hemos aprendido a crear formularios HTML, un elemento fundamental para interactuar con los usuarios en la web. En este ejercicio, hemos diseñado un formulario sencillo que permite a los usuarios ingresar su nombre, correo electrónico y número de teléfono. Utilizando etiquetas como `<form>`, `<label>`, `<input>` y atributos como `required`, hemos asegurado que el formulario sea claro, funcional y obligatorio en cuanto a la recolección de datos. El propósito de este ejercicio es aplicar lo aprendido sobre la estructura de formularios en HTML para recolectar información de manera eficiente y válida.

---

Después de crear el archivo, primero escribimos el DOCTYPE para especificar que estamos utilizando HTML5:

```
<!DOCTYPE html>
```

Luego, definimos la etiqueta `<html>`, que es la raíz del documento, y usamos el atributo `lang="es"` para indicar que el idioma de la página es español. Es importante cerrar esta etiqueta al final del documento.

```
<html lang="es">
</html>
```

A continuación, dentro de la etiqueta `<html>`, agregamos la sección `<head>`. Esta sección no es visible en la página, pero contiene elementos importantes como los metadatos y el título de la página.

```
    <head>
    </head>
```

Dentro de `<head>`, incluimos una etiqueta `<meta>` para especificar el conjunto de caracteres.

```
        <meta charset="UTF-8">
```

Luego, dentro de `<head>,` añadimos la etiqueta `<title>,` que define el título de la página, el cual aparecerá en la pestaña del navegador.

```
        <title>Formulario de Evento Social</title>
```

Pasamos a la sección `<body>`, que es donde colocamos el contenido visible de la página. Aquí es donde diseñamos el formulario.

```
    <body>
    </body>
```

Dentro de `<body>`, primero agregamos un título para la página, usando la etiqueta `<h1>`, que es importante para dar contexto a lo que el usuario verá.

```
        <h1>Formulario para Evento Social</h1>
```

A continuación, creamos el formulario usando la etiqueta `<form>`. Definimos el atributo `action`, que especifica el archivo al que se enviarán los datos del formulario (en este caso, procesar_formulario.php), y el atributo `method="POST"`, que indica que los datos se enviarán de forma segura a través de POST.

```
        <form action="procesar_formulario.php" method="POST">
```

Dentro del formulario, agregamos el primer campo para ingresar el nombre del usuario. Utilizamos la etiqueta `<label>` para describir el campo y el atributo `for="nombre"` para vincularlo con el campo de entrada. Luego, creamos un campo de entrada de tipo `text`, con el atributo `id="nombre"`, `name="nombre"` y el atributo `required` para asegurarnos de que el usuario no lo deje vacío.

Así mismo lo haremos también con el email y el número de telefono.

```
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre" required>
            <br>
```

Finalmente, añadimos un botón de envío para que el usuario pueda enviar el formulario una vez haya completado los campos.

```
            <button type="submit">Enviar</button>
```

---

Este es el código completo que hemos creado:

```
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Formulario de Evento Social</title>
</head>
<body>
    <h1>Formulario para Evento Social</h1>
    <form action="procesar_formulario.php" method="POST">
        <!-- Nombre -->
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" name="nombre" required>
        <br>

        <!-- Correo electrónico -->
        <label for="correo">Correo electrónico:</label>
        <input type="email" id="correo" name="correo" required>
        <br>

        <!-- Número de teléfono -->
        <label for="telefono">Número de teléfono:</label>
        <input type="tel" id="telefono" name="telefono" required>
        <br>

        <!-- Botón de envío -->
        <button type="submit">Enviar</button>
    </form>
</body>
</html>
```

---

Este ejercicio ha reforzado el concepto de cómo estructurar formularios HTML correctamente. Al usar etiquetas descriptivas y atributos como `required`, hemos logrado crear un formulario funcional que asegura que los usuarios proporcionen los datos necesarios antes de enviarlo. Esta práctica es clave para desarrollar formularios efectivos en cualquier tipo de aplicación web que requiera la recolección de datos, como en el caso de eventos sociales o encuestas.

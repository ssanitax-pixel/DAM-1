En la programación web,  utilizamos lenguajes de script de cliente como JavaScript para añadir interactividad. En esta actividad, emplearemos dos conceptos fundamentales:

- El objeto Date: Permite trabajar con fechas y horas del sistema.

- Funciones con Return: Son bloques de código diseñados para realizar una tarea y devolver un valor específico al lugar donde fueron llamadas.

---

Definimos una función llamada `obtenerFecha()`

```
function obtenerFecha() {}
```

Creamos una variable `hoy` dentro de la función.

```
let hoy = new Date();
```

Devolvemos, también dentro de la función, para que cuando la llamemos obtener la fecha actual.

```
return hoy;
```

Imprimimos la información en la consola del ordenador.

```
console.log(obtenerFecha());
```

Ahora creamos una función llamada `saludar` que recibirá los parámetros de `nombre` y `edad`.

```
function saludar(nombre, edad) {}
```

Devolvemos.

```
return "Hola, " + nombre + " tienes " + edad + " años, ¿cómo estás?";
```

Llamamos a la función `saludar` con los valores que queramos.

```
let mensaje = saludar("Ana", 25);
```

Mostramos el contenido directamente en la página web de la siguiente forma.

```
document.write(mensaje);
```

También imprimimos el mensaje en consola, útil para depuración o pruebas.

```
console.log(mensaje);
```

---

El código se verá así:

```
<script>
// 1. Ejercicio de Fechas
function obtenerFecha() {
  let hoy = new Date();
  return hoy;
}

console.log(obtenerFecha());

// 2. Ejercicio de Funciones con Return
function saludar(nombre, edad) {

  return "Hola, " + nombre + " tienes " + edad + " años, ¿cómo estás?";
}

let mensaje = saludar("Ana", 25);
document.write(mensaje);
console.log(mensaje);
</script>
```

---

Hemos comprobado como el uso de `return` nos permite reutilizar la lógica de nuestras funciones de manera limpia. Al combinar esto con objetos como `Date`, así podremos crear aplicaciones de respondan al contexto temporal del usuario.
Entender estas bases es el primer paso para poder interactuar con el calendario o crear validaciones personalizadas en nuestros futuros proyectos.

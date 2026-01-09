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

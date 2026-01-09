Utilizamos PHP para procesar lógica en el servidor antes de que la página llegue al navegador del usuario. En este ejercicio, los conceptos que usaremos serán:
- Variables: Las declaramos usando el símbolo `$` para almacenar información, como la edad de un amigo.
- Estructuras de Control (`if-else`): Nos permiten tomar decisiones en el código. Si una condición es verdadera, se ejecuta un bloque, sino, se ejecuta otro.
- Funciones: Son bloques de código reutilizables que nosotros definimos para realizar tareas específicas, evitando repetir instrucciones.

---

Creamos una variable llamada `$edad`.

```
	$edad = 47;
```

Realizamos una estrucctura condicional con `if-else` que comprueba una condición.

```
	if($edad < 30){
```

Si la condición es verdadera se imprime "Eres un joven".

```
		echo "Eres un joven";
```

Si la condición es falsa, se ejecutará "Ya no eres un joven".

```
	}else{
		echo "Ya no eres un joven"
	}
```

Definimos la función.

```
	function diHola(){
		echo "Hola como estás";
	}
```

Llamamos a la función.

```
	diHola();
```

---

El código completo:

```
<?php
	/*
		Programa: Gestión de reuniones con amigos
		Finalidad: Verificar edad y saludar a los invitados
	*/
	$edad = 47;

	if($edad < 30){
		echo "Eres un joven";
	}else{
		echo "Ya no eres un joven"
	}
	
	function diHola(){
		echo "Hola como estás";
	}

	
	diHola();
?>
```

---

Hemos comprobado que PHP es una herramienta excelente para gestionar situaciones reales, como organizar quién puede "Quedar con amigos para comer o cenar" basándonos en criterios lógicos. Este ejercicio nos ha permitido entender que las estructuras de control son el "cerebro" que toma decisiones, mientras que las funciones son las "herramientas" que nosotros preparamos para que el código sea modular y limpio.

Dominar estos fundamentos es vital para nosotros, ya que son la base para construir aplicaciones más complejas que interactúen con bases de datos o gestionen formularios de usuarios en el futuro.

<?php
	$cliente = [];
	$cliente['nombre'] = "Ana";
	$cliente['apellidos'] = "Sánchez Suárez";
	$cliente['email'] = "ssanitax@gmail.com";
	
	$json = json_encode($cliente);
	echo $json;
?>

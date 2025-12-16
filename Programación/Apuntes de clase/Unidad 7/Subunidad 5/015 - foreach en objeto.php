<?php
	
	$cliente = [
		"nombre" => "Ana",
		"apellidos" => "Sánchez Suárez",
		"email" => "info@ana.com"
	];
  
	foreach($cliente as $clave=>$valor){
		echo $clave.": ".$valor."<br>";
	}
 

?>

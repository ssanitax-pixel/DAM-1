<?php
	
	$cliente = [
		"nombre" => "Ana",
		"apellidos" => "Sánchez Suárez",
		"email" => "info@ana.com"
	];
  
	foreach($cliente as $clave=>$valor){
		echo "<label>".$clave."</label>";
		echo "<input type='text' value='".$valor."'>";
	}
 
?>

<?php
	class Gato{
		function __construct($color,$edad){
			$this->color = $color;
			$this->edad = $edad;
		}
	}
	
	$gato1 = new Gato("Beige",9);
	$gato2 = new Gato("Manchas",1);
	
	var_dump($gato1);
?>

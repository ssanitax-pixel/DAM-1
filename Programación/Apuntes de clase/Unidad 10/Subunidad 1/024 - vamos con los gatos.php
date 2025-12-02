<?php
	class Gato{
		function __construct($nombre,$edad){
			$this->nombre = $nombre;
			$this->edad = $edad;
		}
	}
	
	$gato1 = new Gato("Jagger",9);
	$gato2 = new Gato("Miley",1);
	
	var_dump($gato1);
?>

<?php
	echo 4 == 4 && 3 == 3 && 2 == 2; // verdadero
	echo 4 == 4 && 3 == 3 && 2 == 1; // falso
	
	echo 4 == 4 || 3 == 3 || 2 == 2; // verdadero
	echo 4 == 4 || 3 == 3 || 2 == 1; // verdadero
	echo 4 == 4 || 3 == 2 || 2 == 1; // verdadero
	echo 4 == 3 || 3 == 2 || 2 == 1; // falso
?>

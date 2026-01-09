<?php
	/*
		Programa: Gestión de reuniones con amigos
		Finalidad: Verificar edad y saludar a los invitados
	*/
	$edad = 47;

	if($edad < 30){
		echo "Eres un joven";
	}else{
		echo "Ya no eres un joven";
	}
	
	function diHola(){
		echo "Hola como estás";
	}

	
	diHola();
?>

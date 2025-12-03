<?php
  $cliente = [];
  $cliente['nombre'] = "Ana";
  $cliente['apellidos'] = "Sánchez Suárez";
  $cliente['email'] = "info@ana.com";
  
  $json = json_encode($cliente);
  echo $json;
?>

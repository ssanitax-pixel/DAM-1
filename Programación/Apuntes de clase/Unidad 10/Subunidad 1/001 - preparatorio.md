PHP es un lenguaje del lado del servidor
Requiere que tengamos un servidor preparado

Formas fáciles de preparar un servidor

**En linux** (la buena):
Terminal:
sudo apt install apache2 (instalar apache)
sudo apt install php (para instalar php)
sudo chdmog 777 -R /var/www/html (para dar permisos a la carpeta)

Y a partir de ese momento:
1. Todos los archivos se meten dentro de /var/www/html
2. En el navegador ponemos http://localhost/...

En Windows (la forma mala):
1. Todos los archivos se metern dentro de C:/xampp/htdocs
2. En el navegador ponemos http://localhost/...

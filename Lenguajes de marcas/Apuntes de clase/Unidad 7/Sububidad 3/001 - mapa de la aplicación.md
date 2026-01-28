En la clase de ayer:

Hicisteis un abstract (párrafos, prosa) del tema de vuestro proyecto

Que quiero que hagáis en la clase de hoy:
Empezar a enumerar, en texto, las "pantallas" que tendrá vuestra aplicación (top-down)

Y los archivos que harán falta para ello

Texto: La carta a los reyes magos

La app va de una biblioteca de videojuegos, tu tienes tus videojuegos fisicos, y los registras a mano en la plataforma, para poder ver los que tienes si sienes demasiados, o si estás fuera de casa, tambien, cada juego, estara explicado y dividido las versiones existentes, seleccionando tu la que tengas, tambien en que plataformas estan y que tipo de consola es para el que lo tienes, a parte, habrá una descripción explicando de que va el videojuego, con imágenes tambien, y un blog, que nos servira para posicionar la pagina, en la que hablaremos de recomendaciones de juegos, trucos, nuevas salidas...

---

📱 Mapa de Pantallas (Top-Down)
1. Gestión de Colección Personal

    Home / Mi Estantería: Vista general de vuestros juegos.

        Filtros: Por estado (Pendiente, Jugando, Completado) y por plataforma.

        Visualización: Modo galería de carátulas (Shelf view).

    Ficha Detallada del Juego: * Info Global: Descripción, imágenes y Nota Media de la Comunidad.

        Mi Espacio: Mi valoración (1-10), notas personales y estado de Préstamo (¿A quién se lo he dejado?).

        Acción: Botón de "Poner en venta".

2. Marketplace (Compraventa)

    Vista del Comprador (Catálogo):

        Listado de ofertas de otros usuarios.

        Comparativa de Precio Recomendado vs. Precio de última venta.

    Vista del Vendedor (Asistente):

        Formulario de publicación con sugerencia de precio basada en el mercado.

        Panel de control: "Mis artículos en venta" y "Mis ganancias".

3. Comunidad y Contenido

    Wishlist (Lista de deseos): Juegos que quieres comprar, vinculados directamente al marketplace.

    Blog: Artículos de trucos y lanzamientos para atraer tráfico (SEO).

📁 Arquitectura de Archivos (El Esqueleto)
💾 Base de Datos (/db)

    schema.sql: Definición de todas las tablas.

    queries_mercado.php: Lógica para calcular automáticamente la Nota Media y el Precio Recomendado.

💻 Frontend (Vistas)

    index.php: Dashboard de la colección.

    juego_detalle.php: Ficha técnica y personal.

    marketplace_home.php: El catálogo de compraventa.

    vender_asistente.php: Formulario para publicar anuncios.

    blog_lista.php y blog_post.php: El sistema de artículos.

⚙️ Lógica de Backend (/includes)

    gestion_prestamos.php: Controla a quién y cuándo prestamos juegos.

    valoraciones.php: Procesa los votos de los usuarios para la media global.

    transacciones.php: Registra las ventas para actualizar el "Precio de la última venta".

📝 Resumen del Proyecto (La Carta a los Reyes Magos Completa)

    "Nuestra plataforma es un ecosistema integral para coleccionistas de videojuegos físicos. Permitiremos el registro manual de colecciones, donde cada usuario podrá gestionar el estado de sus juegos (jugando, completado, pendiente), anotar sus préstamos a terceros y añadir valoraciones personales que alimentarán una nota media global.

    La app contará con un Marketplace especializado con dos interfaces: una para el comprador, que verá datos de confianza como el precio recomendado y el valor de la última venta real; y otra para el vendedor, que tendrá un asistente de tasación. Todo esto se apoyará en un blog de recomendaciones y trucos para posicionar la web y una lista de deseos (wishlist) para que el usuario nunca pierda de vista sus futuras adquisiciones."

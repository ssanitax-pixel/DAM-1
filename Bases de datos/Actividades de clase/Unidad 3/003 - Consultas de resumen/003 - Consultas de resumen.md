Las consultas de resumen son herramientas que nos permiten obtener estadísticas generales de una tabla sin tener que leer todos los registros uno por uno. En lugar de ver cada fila, usamos funciones como `AVG()` para calcular medias, lo cual es muy útil cuando trabajamos con bases de datos grandes.
Además, en SQL tenemos funciones de redondeo para que los resultados numéricos sean más fáciles de leer. Dependiendo de lo que necesitemos, podemos usar el redondeo estándar, forzar que el número baje al entero anterior o que suba al siguiente. Esto es fundamental para presentar informes limpios y precisos en cualquier aplicación.

---

Entramos en MySQL desde la terminal con permisos de administrador.

```
sudo mysql -u root -p
```

Después seleccionamos la base de datos de nuestros clientes para poder trabajar con sus tablas.

```
USE clientes;
```

Calculamos la media de edad de todos los registros usando la función `AVG`.

```
SELECT AVG(edad) FROM clientes;
```

Ahora aplicamos `ROUND()` para que el sistema decida el redondeo más cercano.

```
SELECT ROUND(AVG(edad)) FROM clientes;
```

Usamos `FLOOR()` si queremos ignorar los decimales y quedarnos siempre con el número entero más bajo.

```
SELECT FLOOR(AVG(edad)) FROM clientes;
```

Si necesitamos lo contrario, usamos `CEIL()` para que el resultado suba al siguiente número entero.

```
SELECT CEIL(AVG(edad)) FROM clientes;
```

Para la parte visual, usamos la librería `matplotlib`. Primero importamos el módulo.

```
import matplotlib.pyplot as pt
```

Creamos una lista con las edades. Luego llamamos a `pie()` para crear el gráfico de pastel.

---

El código completo quedará así:

1. SQL:

```
sudo mysql -u root -p

USE clientes;

SELECT ROUND(AVG(edad)) AS 'Media Redondeada' FROM clientes;

SELECT FLOOR(AVG(edad)) AS 'Media Suelo' FROM clientes;

SELECT CEIL(AVG(edad)) AS 'Media Techo' FROM clientes;
```

2. Python:

```
import matplotlib.pyplot as pt

edades = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]

pt.pie(edades)

pt.show()
```

---

Como hemos visto, estas funciones son muy útiles para no liarnos con números llenos de decimales. En clase nos sirve para calcular nuestra media de notas o para ver estadísticas rápidas de un grupo. Es mucho más cómodo ver un "35" bien redondeado que un "34.8765".
Relacionar esto con las gráficas de Python nos hace ver que las bases de datos no son solo texto.

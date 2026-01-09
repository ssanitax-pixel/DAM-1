Los operadores en SQL nos permiten ir un paso más allá de simplemente mostrar los datos que tenemos guardados. En esta lección vamos a ver cómo podemos realizar cálculos matemáticos directamente en nuestras consultas (operadores aritméticos) y cómo podemos crear columnas lógicas que nos digan si se cumple una condición o no (operadores lógicos).
Entender estos operadores es clave porque nos permiten transformar la información antes de mandarla a nuestra aplicación. Ya no solo leemos la edad, sino que podemos calcular promedios, aplicar descuentos o clasificar a los usuarios por rangos de forma automática desde la propia base de datos.

---

Abrimos la terminal y entramos en MySQL como administrador. 

```
sudo mysql -u root -p
```

Después, seleccionamos nuestra base de datos para empezar a trabajar.

```
USE clientes;
```

Podemos modificar los valores numéricos al momento. Aquí sumamos y restamos por 500 para ver cómo cambian los resultados.

```
SELECT nombre, apellidos, edad + 500 FROM clientes;
SELECT nombre, apellidos, edad - 500 FROM clientes;
```

De la misma forma, podemos usar la multiplicación y la división.

```
SELECT nombre, apellidos, edad * 500 FROM clientes;
SELECT nombre, apellidos, edad / 500 FROM clientes;
```

Para el uso de operadores lógicos, creamos columnas nuevas donde nos devuelven un 1 para verdadero o un 0 para falso. Usamos el operador `&&` o `AND` para comprobar si la edad está en un rango específico.

```
SELECT 
    nombre,
    apellidos,
    edad,
    edad < 30 AS 'Menor de 30 años',
    edad >= 30 && edad < 40 AS 'Entre 30 y 40 años'
FROM clientes;
```

Finalmente, usamos `AS` para ponerle un nombre claro a la columna que hemos calculado. Así, en lugar de ver la fórmula, veremos una pregunta clara.

```
SELECT 
    nombre,
    apellidos,
    edad,
    edad < 30 AS '¿Es menor de 30 años?'
FROM clientes;
```

---

El código completo queda así:

```
SELECT nombre, apellidos, edad + 500 FROM clientes;
SELECT nombre, apellidos, edad - 500 FROM clientes;
SELECT nombre, apellidos, edad * 500 FROM clientes;
SELECT nombre, apellidos, edad / 500 FROM clientes;

SELECT 
    nombre,
    apellidos,
    edad,
    edad < 30 AS 'Menor de 30 años',
    edad >= 30 && edad < 40 AS 'Entre 30 y 40 años',
    edad > 40 AS 'Mayor de 40 años'
FROM clientes;

SELECT 
    nombre,
    apellidos,
    edad,
    edad < 30 AS '¿Es menor de 30 años?'
FROM clientes;
```

---

Dominar estos operadores nos permite hacer consultas mucho más inteligentes. Al principio parece que solo estamos jugando con los números, pero en el mundo real esto se usa para cosas importantes, como calcular impuestos, periodos de suscripción o filtrar listas de invitados para un evento social según su edad.

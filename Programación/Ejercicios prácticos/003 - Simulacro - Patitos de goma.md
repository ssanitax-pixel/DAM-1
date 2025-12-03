Vamos a realizar un programa que muestre por pantalla la producción que se hace cada día en una fábrica siendo esa producción siempre 10 patos de goma, además de que tendremos que sacar un mensaje final en el que se sumen todos los patitos que se han fabricado hasta la fecha.

---

Para empezar haremos una anidación de bucles "for" siendo el primero los años, el segundo los meses y el tercero los días estos tendrán un rango cada uno siendo en los años los últimos 25 años, en los meses los 12 meses que hay y en los días aproximaremos a 30 días por mes, para poner el rango se debe sumar 1 al último número del rango, todo esto se hace de la siguiente forma:

```
	for anio in range(2000,2026):
		for mes in range(1,13):
			for dia in range(1,31):
```

Los rangos harán que recorra todos los días que le hemos puesto y el hecho de sumarle 1 al último número es por que el último número del rango no se cuenta.

Para poder mostrar el mensaje utilizaremos un "print" de esta manera:

```
	print("Día",dia,"del mes",mes,"del año",anio,", se han fabricado: 10 patitos")
```

Por último, para que aparezcan al final el total de los patitos fabricados en este período, tendremos que crear la variable "patitos", y al final del bucle señalar que se van sumando de 10 en 10, de la siguiente manera:
Esta primera parte se pondrá al principio, para tener las variables siempre ordenadas y a mano.

```
	patitos = 0
```

Esta parte, será dentro del bucle, al final, para que se sumen todos los patitos:

```
	patitos += 10
```

Y finalmente poner otro "print" para que se visualice.

---

A conticuación estaría el código completo del ejercicio:

```
	'''
		Ejercicio: Contando patitos de goma
		Escribe un programa en Python que utilice bucles for para simular el conteo de patitos de goma en una fábrica.
	'''
	
	patitos = 0
	for anio in range(2000,2026):
    		for mes in range(1,13):
        		for dia in range(1,31):
            			patitos += 10
            			print("Día",dia,"del mes",mes,"del año",anio,", se han fabricado: 10 patitos")
        			print("En total, en este período hemos fabricado",patitos,"patitos de goma")
```

**Notas**
- Tener cuidado a la hora de poner los rangos, el rango llega a un número menos del segundo número.
- Atento al sangrado y los dos puntos del bucle "for".
- Tener en cuenta el orden de la anidación.
- No olvidar definir las variables.

---

En conclusión, hemos aprendido a utilizar los bucles "for" para poder economizar el código y tener un programa más sencillo y limpio.

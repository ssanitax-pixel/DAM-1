Cuando organizamos una cena con amigos, es importante saber cuántos platos comprar para que nadie se quede sin comida. Para ello, podemos usar una lista en Python que almacene los nombres de nuestros amigos, y así saber cuántos somos en total.

---

Una lista es un objeto que nos permite guardar varios elementos, como los nombres de personas. Cada elemento tiene un índice que indica su posición.

```
amigos = ["Alba","Inma","Carmen","Eva","Pilar"]
```

Para añadir uno más, podemos usar el método '.append'.

```
amigos.append("Nicole")
```

Para saber cuántos amigos hay en total, usamos la función 'len' que nos da cuántos elementos hay en la lista.

```
print(len(amigos))
```

El código completo:

```
amigos = ["Alba","Inma","Carmen","Eva","Pilar"]

amigos.append("Nicole")

print(len(amigos))
```

---

En este ejercicio hemos usado objetos predefinidos en Python, concretamente el objeto 'list' y aprendido algunas de sus propiedades básicas, concretamente '.append', que sirve para añadir más elementos a una lista y 'len', que sirve para ver el número de elementos de una lista. Al manipular listas, aprendemos a almacenar, modificar y consultar datos de forma eficiente, lo cual es fundamental en la programación. Además de ser muy útil cuando vais a ser muchos en una cena y queremos saber exactamente cuantos seremos.

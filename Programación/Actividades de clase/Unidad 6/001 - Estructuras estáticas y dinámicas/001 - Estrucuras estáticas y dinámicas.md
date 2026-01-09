En este ejercicio aprendemos a usar las listas en Python. Una lista sirve para guardar varios datos dentro de una sola variable. Con ellas podemos hacer cosas básicas como añadir elementos, cambiar un dato, recorrer la lista para ver qué contiene o borrar algún elemento. Todo esto se usa mucho en programación porque nos permite organizar información de forma ordenada. Aquí pondremos en práctica estas acciones usando una lista de amigos invitados a un almuerzo.

---

Primero hacemos una lista, con este caso mis amigas.

```
lista_amigos = ['Alba','Raquel','Eva']
```

Añadimos a una amiga nueva usando `.append`.

```
lista_amigos.append('Nicole')
```

Listamos a todas las amigas, para corroborar que se ha añadido a Nicole correctamente.

```
for amigo in lista_amigos:
    print(amigo)
```

A continuación, cambiamos el nombre de una amiga por otra, en este caso se cambiará el nombre de Raquel por Pilar. Hay que tener cuidado, ya que se empieza a contar desde 0, no desde 1, así que se cambiará el segundo nombre de la lista.

```
lista_amigos[1] = 'Pilar'
```

Por último, recorremos la lista otra vez para ver como queda la lista de amigas.

```
for amigo in lista_amigos:
    print(amigo)
```

---

Así queda el ejercicio resuelto:

```
lista_amigos = ['Alba','Raquel','Eva']

lista_amigos.append('Nicole')

print("Lista de amigas: ")
for amigo in lista_amigos:
    print(amigo)
    
lista_amigos[1] = 'Pilar'

lista_amigos.pop(0)

print("Lista de amigas actualizado: ")
for amigo in lista_amigos:
    print(amigo)
```

---

En el ejercicio creamos una lista con varios amigos, añadimos uno nuevo, mostramos la lista completa, cambiamos un nombre por otro y, finalmente, eliminamos un amigo usando `pop()`. Con todas estas acciones practicamos cómo trabajar con una lista paso a paso. Al terminar, entendemos mejor cómo añadir, modificar, leer y borrar elementos dentro de una lista en Python.

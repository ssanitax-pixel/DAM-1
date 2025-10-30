DAW1 - U2:

# Actividad (30’): “Aforo Express — entradas, filas y horario”

Crea un mini-programa que calcule cuántas **filas** necesitas para sentar a los asistentes de un evento, redondeando **al alza**, y muestre un **informe de fecha/hora** del evento.

## Objetivos de aprendizaje

* Instanciar y usar **Date** / **datetime.date** y acceder a sus **propiedades y métodos** (`getFullYear`, `getMonth`, `weekday`, etc.). 
* Usar **métodos “estáticos”** de librerías estándar: `Math.ceil`, `Math.round`, `Math.PI`, y `math.ceil`. 
* Seguir el flujo **entrada → cálculo → salida** con validaciones básicas. 
* Ajustarse a la **nota importante**: usar objetos preexistentes, no definir clases nuevas. 

## Enunciado

Pide al usuario:

1. `asistentes` (entero > 0)
2. `asientos_por_fila` (entero > 0)
3. `fecha_evento` (fecha/hora; ver formato por lenguaje)

Calcula:

* `filas = ceil(asistentes / asientos_por_fila)` (redondeo al **alza**). 
* Muestra un **informe de fecha**: año, mes, día y despiece horario (horas, minutos, segundos) con los métodos del objeto fecha. 
* Además, muestra un **número de control**: redondea la media de 3 valores de satisfacción (por ejemplo 7.8, 6.5, 9.2) con `Math.round`/`round` y referencia `PI` para un simple “código de sesión” (p. ej., `Math.round(PI*100)`). 

### Reglas

* Si hay entradas no numéricas o fuera de rango, avisa y **no continúes** hasta que sean válidas.
* No crear clases propias (ajustado a la subunidad). 



DAW1 - U3:

# Actividad (30’): “Taquilla Exprés — control de aforo y recaudación”

Implementa `taquilla.py`, un mini-sistema de venta de entradas que gestiona el **aforo** de una sala y la **recaudación**. Debe usar `if/elif/else`, bucles `while`, saltos (`break`/`continue`), **`try/except`** para entradas, y **`assert`** para invariantes. 

## Objetivos de aprendizaje

* **Selección:** decidir si se puede vender, si hay sobreventa o si la sala está llena. 
* **Repetición:** bucle de venta hasta llenar aforo o parar manualmente. 
* **Saltos:** `continue` para entradas inválidas, `break` al llenar aforo. 
* **Excepciones:** captura de entradas no numéricas con `try/except`. 
* **Aserciones:** garantizar que el aforo restante nunca sea negativo. 
* **Breve prueba y documentación** (docstrings). 

## Requisitos funcionales

1. Pedir por consola:

   * `aforo_total` (entero > 0) y `precio` (float > 0).
2. Repetir ventas: en cada iteración pedir `cantidad` (entradas del cliente).

   * Si no es número entero positivo → aviso y `continue`.
   * Si `cantidad` > `aforo_restante` → ofrecer **ajustar** a lo que queda (`S/N`).
3. Registrar **recaudación** y **entradas vendidas**.
4. Cada **5 ventas efectivas** (no intentos) mostrar un mensaje “⏱ descanso técnico” y continuar.
5. Terminar con `break` si `aforo_restante == 0`.
6. **Aserciones:**

   * `assert aforo_restante >= 0` (invariante).
   * `assert entradas_vendidas + aforo_restante == aforo_total` (conservación).
7. Al final, imprimir **resumen** y marcar **“Sala llena”** o “Quedan X asientos”.

DAM1 : U2:

# Actividad (30’): “Planificador de cuadras — versión exprés”

Crea un script llamado `planificador_cuadras.py` que calcule cuántas cuadras necesitas en una fecha dada, según el número de caballos y la capacidad de cada cuadra. Debe redondear **al alza** el número de cuadras, mostrar propiedades de la fecha y presentar un pequeño informe.

## Objetivos de aprendizaje

* Usar **métodos** y **propiedades** de objetos estándar (`datetime.date`, `date.year`, `date.weekday`, etc.). 
* Llamar a **métodos “estáticos”**/de módulo como `math.ceil`. 
* Manejar **entrada → cálculo → salida** con mensajes claros. 

## Requisitos funcionales

1. **Entrada de datos (por `input`)**

   * `caballos` (entero > 0).
   * `capacidad_por_cuadra` (entero > 0).
   * `fecha` en formato `YYYY-MM-DD`.
     (Estos tres inputs siguen el patrón de los ejercicios de entrada/cálculo/salida). 
2. **Cálculos**

   * `cuadras_necesarias = ceil(caballos / capacidad_por_cuadra)` usando `math.ceil`. 
   * Crear un objeto `date` con la fecha indicada y obtener:

     * `year`, `month`, `day`
     * `weekday()` (0–6) y `isoweekday()` (1–7)
       (Como en los ejemplos de propiedades de fecha). 
3. **Salida (informe)**

   * Línea resumen con caballos, capacidad y cuadras **redondeadas al alza**.
   * Bloque “Datos de la fecha” mostrando `YYYY-MM-DD`, `year`, `month`, `day`, `weekday`, `isoweekday`.
4. **Validaciones mínimas**

   * Si algún valor no es entero positivo, mostrar un mensaje y terminar.
   * Si la fecha no cumple el formato, mostrar mensaje y terminar.
5. **(Opcional, si te da tiempo)**

   * Mostrar si la fecha cae **entre semana** o **fin de semana** (usa `isoweekday()`).



DAM1: U3

# Actividad (30’): “Adivina el número — Modo docente”

Crea un script `adivina.py` que juegue a adivinar un número secreto entre 1 y 50 con un máximo de **6 intentos**. Debe usar condicionales `if/elif/else`, bucles `while`, saltos (`break/continue`), manejo de errores con `try/except` y al menos **2 aserciones** para garantizar invariantes. 

## Objetivos de aprendizaje

* Aplicar **selección** con `if/elif/else` para comparar el intento con el secreto. 
* Usar **repetición** con `while` y contador de intentos. 
* Practicar **saltos** con `break` (acierto) y `continue` (entrada inválida). 
* Validar entradas con **`try/except`** y documentar brevemente con docstrings. 
* Añadir **aserciones** para límites y estado. 

## Requisitos funcionales

1. El programa elige al inicio un **número secreto** en `[1,50]`.
2. El usuario tiene **6 intentos**. En cada intento:

   * Pide un número por `input`. Si no es convertible a `int`, **muestra aviso** y **no gasta intento** (usa `continue`). 
   * Si está **fuera de rango** (`<1` o `>50`), avisa y **no gasta intento**.
   * Compara con `if/elif/else`: imprime “**Demasiado alto**” o “**Demasiado bajo**”; si acierta, **termina con `break`**. 
3. **Pista de paridad**: al **3er** intento consumido (y si no ha acertado), muestra si el secreto es **par o impar**. (Selección + contador). 
4. Al final, muestra **resultado** (ganó/perdió) y el número secreto.
5. **Aserciones mínimas**:

   * El número secreto **siempre** está en `[1,50]`.
   * El contador de intentos **nunca** es negativo. 




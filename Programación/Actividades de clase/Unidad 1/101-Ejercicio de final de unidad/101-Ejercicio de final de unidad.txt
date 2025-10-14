 Ticket de tienda (Factura con IVA y descuentos)
Objetivo

Desarrollar un programa en Python que solicite datos por teclado, valide entradas básicas, calcule IVA y posibles descuentos según reglas dadas y muestre un ticket con formato claro.
Alcance de contenidos (lo que debe evidenciar)

    Identificadores y nomenclatura (snake_case).
    Variables, literales y constantes.
    Tipos y conversiones (int, float).
    Operadores aritméticos, de comparación y booleanos.
    Entradas/salidas con input() y print().
    Comentarios (bloque inicial y en línea).

Requisitos funcionales

    Entradas (por teclado)
        cliente_nombre (cadena).
        edad (convertida a entero; si no es número válido → mensaje y finaliza).
        base_imponible (convertida a float; si no es número positivo → mensaje y finaliza).

    Constantes
        IVA = 0.21 (21%). Debe declararse como constante (MAYÚSCULAS).

    Reglas de negocio

        Si edad < 18: no emitir factura (mostrar mensaje y finalizar).

        Descuento según base_imponible:
            < 100 €: 0%
            100–199.99 €: 5%
            ≥ 200 €: 10%

        Cálculos requeridos:
            importe_descuento
            base_tras_descuento
            importe_iva
            total_factura

    Salida formateada (ticket)
        Encabezado en 3 líneas: nombre del programa, autor/a, año.
        Datos: cliente y edad.
        Desglose: base, % descuento, € descuento, base tras descuento, IVA, TOTAL.
        Mensajes claros, sin trazas de error.

    Comentarios mínimos
        Comentario de bloque al inicio (nombre, versión, autor/a, finalidad).
        Comentarios en línea explicando al menos: una conversión de tipo, una condición y un cálculo.

    Restricciones
        No usar librerías externas.
        Ajustarse a conceptos vistos en la unidad (evitar estructuras no presentadas).

Casos de prueba (a ejecutar por el alumnado)

    No entregar salidas ni soluciones; solo comprobar que el programa se comporta como se describe.

    Menor de edad Entradas: nombre cualquiera, edad < 18, base ≥ 0 → debe mostrar mensaje de no emisión.

    Sin descuento Entradas: adulto, base < 100 → descuento 0%.

    Descuento 5% Entradas: adulto, base en [100, 200) → aplica 5%.

    Descuento 10% Entradas: adulto, base ≥ 200 → aplica 10%.

    Errores de entrada
        Edad no numérica → mensaje de error.
        Base vacía/no numérica/negativa → mensaje de error.


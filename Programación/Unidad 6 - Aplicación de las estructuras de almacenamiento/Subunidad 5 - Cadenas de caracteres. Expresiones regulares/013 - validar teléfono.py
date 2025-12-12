import re

# Patrón de teléfono español:
# Puede empezar con +34 o 0034 opcional, seguido de 9 dígitos
# Se permite espacio, guion o nada entre los números
patron_telefono = r'^(\+34|0034)? ?[6-9]\d{2}[ -]?\d{2}[ -]?\d{2}[ -]?\d{2}$'

# Ejemplos de teléfonos
telefono_mal = "12345"           # Demasiado corto, no válido
telefono_bien1 = "+34699123456"  # Con prefijo internacional
telefono_bien2 = "699 12 34 56"  # Con espacios
telefono_bien3 = "699-12-34-56"  # Con guiones

# Verificamos cada teléfono
print(re.match(patron_telefono, telefono_mal))      # None (no válido)
print(re.match(patron_telefono, telefono_bien1))    # Objeto Match (válido)
print(re.match(patron_telefono, telefono_bien2))    # Objeto Match (válido)
print(re.match(patron_telefono, telefono_bien3))    # Objeto Match (válido)


import datetime as fechas

hoy = fechas.date(2025, 9, 20)
print(hoy)

print(hoy.year)
print(hoy.month)
print(hoy.day)

diadelasemana = hoy.weekday()
print(diadelasemana)
diadelasemana = hoy.isoweekday()
print(diadelasemana)

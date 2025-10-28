import datetime

fecha_hoy = datetime.date.today()
print("Fecha actual: ",fecha_hoy)

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print("Día de la semana:", dias[fecha_hoy.weekday()])

fecha_personal = datetime.date(2000, 5, 6)

edad = fecha_hoy.year - fecha_personal.year

print(edad)

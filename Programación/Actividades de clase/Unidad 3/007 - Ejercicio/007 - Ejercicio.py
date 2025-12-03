menu = ["Pizza","Tortilla de patatas","Fuet","Cerveza"]

for comida in menu:
    if comida == "Pizza":
        print("Para la Pizza necesitas: masa, tomate, queso y jamón york.")
    elif comida == "Tortilla de patatas":
        print("Para la Tortilla de patatas necesitas: patatas, huevo, aceite y cebolla.")
    elif comida == "Fuet":
        print("Para el Fuet necesitas: fuet y un cuchillo para cortarlo.")
    elif comida == "Cerveza":
        print("Para la Cerveza necesitas: cerveza Alhambra muy fría y un vaso congelado.")
    
for comida in menu:
    if comida == "Pizza":
        print("Para preparar la Pizza necesitas 30 minutos.")
    elif comida == "Tortilla de patatas":
        print("Para preparar la Tortilla de patatas necesitas 45 minutos.")
    elif comida == "Fuet":
        print("Para preparar el Fuet necesitas 5 minutos.")
    elif comida == "Cerveza":
        print("Para preparar la Cerveza necesitas 60 minutos.")

platos_servidos = 0

for comida in menu:
    platos_servidos += 1
    print("Se ha servido el plato de",comida,". Platos servidos hasta ahora: ",platos_servidos)


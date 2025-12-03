edad = 15
assert edad > 18, "No puedes entrar, eres menor de edad"
try:
    assert edad > 18, "No puedes entrar, eres menor de edad"
    print("¡Pasa a la cena!")
        
except:
    print("error")
    

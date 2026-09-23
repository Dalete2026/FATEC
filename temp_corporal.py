temperatura=float(input("Digite a temperatura corporal (C°):").replace(",","."))
if(temperatura>=37.8):
    print(f"Atenção {temperatura} : Estado de febre!")
else:
    print(f"Sua temperatura é {temperatura} temperatura normal")

temperatura=float(input("Digite a temperatura atual do laboratorio:  ").replace(",","."))

if(temperatura<15):
    print("Muito frio!")
elif(temperatura==15 or temperatura==25):
    print("Temperatura Ideal")
else:
    print("Muito quente")
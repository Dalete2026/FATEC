largura=float(input("Digite a largura em (CM): "))
comprimento=float(input("Digite o comprimento em (CM): "))
area=largura*comprimento

if(area >= 300):
    print(f"a aréa do terreno é de {area} Terreno de Grande Porte")
else:
    print(f"a aréa do terreno é de {area} Terreno de Porte Médio")
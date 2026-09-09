ladoA=int(input("Digite o primeiro lado do triangulo: "))
ladoB=int(input("Digite o segundo lado do triangulo: "))
ladoC=int(input("Digite o terceiro lado do triangulo: "))

if(ladoA+ladoB+ladoC) and (ladoA+ladoC>ladoB) and (ladoB+ladoC>ladoA):
    print("Triangulo valido!")
if(ladoA==ladoB and ladoB==ladoC):
    print("É um triangulo equilatero!")
elif(ladoA==ladoB or ladoB==ladoC or ladoC==ladoB):
    print("É um triangulo Isósceles!")
else:
    print("É um triangulo escaleno:")
  
    
    


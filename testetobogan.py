nome=input("Qual é a seu nome?")
idade=int(input("Qual é a sua idade? "))
alt=float(input("Qual é a sua altura? ").replace(",","."))

if(idade>=12 or alt>=1.60):
    print("Liberado")

else:
    print("Bloqueado")



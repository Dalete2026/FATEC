idade=int(input("Qual é a sua idade? : "))
cnh=input("Você possui CNH? 's' ou 'n': ")

if(idade>=21 and cnh=='s'):
    print("Aluguel liberado")
else:
    print(f"Sua idade é {idade} e você não possui CNH e por este motivo é não foi liberado o aluguel")
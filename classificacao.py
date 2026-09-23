nota= float(input("Qual a nota final do aluno ?").replace(",","."))

if(nota<5):
    print("Reprovado!")
elif(nota<=5 or nota<=6.9):
    print("Em recuperação")
else:
    print("Aprovado com sucesso")

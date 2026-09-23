estudante=(input("Você é estudante?")).strip()
idade=int(input("Qual é a sua idade?"))
if(estudante == 's' or idade>=60):
    print("Meia-Entrada Liberada")
else:
    print("Ingresso Inteiro")

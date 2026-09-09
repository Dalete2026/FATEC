nome=(input("Digite o seu nome: "))
idade=int(input("Qual é a sua idade?"))
peso=float(input("Qual é o seu peso?").replace(",","."))

if (idade>=18 and peso>=50) :
    print(f"Paciênte {nome} liberado para exames com contraste")
else:
    print(f"Alerta! Paciênte  {nome} Necessita de avaliação médica especial")
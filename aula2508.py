# Exercicio de fixação 25/08

#exercicio01
ano = int(input("Qual ano você nasceu? "))
idade = 2026-ano
pode_dirigir = idade>=18
resposta1= {True:"Sim", False:"Não"}[pode_dirigir]
print(f"Você pode dirigir? {resposta1}")
print()

#exercicio02
temp = float(input("Qual a temperatura atual? "))
aviso= temp>40
resposta2={True:"Sim", False:"Não"}[aviso]
print(f"Alerta de superaquecimento ativo? {resposta2}")
print()

#exercicio03
meta = 1500
venda_vendedor=float(input("Qual o total da venda de hoje? ").replace(",","."))
meta_atingida= venda_vendedor>=meta
resposta3={True:"Sim", False:"Não"}[meta_atingida]
print(f"Meta diária alcançada?{resposta3}")
print()

#exercicio04
distancia = float(input("Qual é o total de km planejado para essa viagem?").replace(",","."))
consumo = float(input("Quantos Km o carro fez por litro? ").replace(",","."))
valor = float(input("Qual o valor do combustivel? ").replace(",","."))
litros_necessarios = distancia/consumo
custo_combustivel = litros_necessarios*valor
custo_total = custo_combustivel/3
print(f"\n A quantidade necessaria de litros para a viagem é de {litros_necessarios:.2f}, \n o custo total do combustivel é de {custo_combustivel:.2f}reais \n e para cada um ficou {custo_total:.2f} ")

#exercicio05
ano = int(input("Qual é o seu ano de nascimento? "))
idade = 2026-ano
altura = float(input("Qual é a sua altura? ").replace(",","."))
pode_entrar = (idade>=12) and (altura>=1.50)
resposta4={True:"Sim", False:"Não"}[pode_entrar]
print(f"Autorização para entrar na montanha russa? {resposta4}")

#exercicio06
ano = int(input("Qual é o seu ano de nascimento? "))
idade = 2026-ano
estudante= input("Você é estudante?(S/N): ".upper())
meia_entrada = (estudante == "S") or (idade>=60)
resposta5={True:"Sim", False:"Não"}[meia_entrada]
print(f"Tem direito?{resposta5}")


# Exercicio 1 tentativas de login
tentativas=5
qtd= int(input("Quantas tentativas você já fez?"))
print(f"Você realizou {qtd} tentativas agora resta {tentativas-qtd} chances")
print()

#exercicio 2 Idade daqui 5 anos
idade= int(input("Qual é sua idade?"))

print(f"Hoje sua idade é: {idade} anos,daqui 5 anos você terá {idade+5} anos")
print()

#Exercicio 3 quantidade,preço e nome do produto
produto= (input("Qual o nome do produto?"))
preco= float(input("Qual é o preço do produto?"))
quantidade= int(input("Qual a quantidade?"))

print(f"O nome do produto é {produto}, a quantidade em estoque é {quantidade} e o valor total de mercadoria é R${quantidade*preco}")
print()

# preço desconto
valor_produto = float(input("Qual é o valor do produto? "))
desconto = float(15/100)
valor_final = valor_produto - (1-desconto)
print(f"O valor original é de R$ {valor_produto} e com o desconto ficou {valor_final}")

#Calculo da nota 
n1 = float(input("Qual é primeira nota"))
n2 = float(input("Qual é segunda nota"))
n3 = float(input("Qual é terceira nota"))
media=(n1+n2+n3)/3
print(f"A média é de {media}")




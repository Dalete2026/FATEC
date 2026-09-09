valor_produto=float(input("Digite o valor do produto: ").replace(",","."))

if(valor_produto>100):
    desconto=10/100
    valor_desconto=valor_produto*desconto
    valor_com_desconto=valor_produto-valor_desconto
    print(f"O valor com desconto foi:{valor_com_desconto}")
else:
    print(f"O seu produto custou {valor_produto}")

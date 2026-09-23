valor_compra=float(input("Qual foi o valor total da sua compra?"))
assinante=input("Você é assinante do clube VIP ? 'sim' ou 'nao'? ")

if(valor_compra>=150) or (assinante=='s'):
    print(f"Você comprou {valor_compra} e {assinante},assina o  clube vip:")
else:
    print(f"Você comprou R${valor_compra} e {assinante}  assina o clube vip")
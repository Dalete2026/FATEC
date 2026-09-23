cor=input("Digite qual a cor do semáforo: ")
if(cor=='verde'):
    print("Ação: Siga em frente")
elif(cor=='amarelo'):
    print("Ação: Atenção! Reduza a velocidade.")
elif(cor=='vermelho'):
    print("Ação: Pare! Aguarde a liberação.")
else:
    print("Sinal inválido!")
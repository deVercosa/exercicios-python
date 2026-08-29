
#Traduza o algoritmo abaixo para Python.
#ALGORITMO calculo_gorjeta
#INÍCIO
#LER valor_conta
#LER percentual_gorjeta
#gorjeta ← valor_conta * (percentual_gorjeta / 100)
#total ← valor_conta + gorjeta
#ESCREVER &quot;Gorjeta: R$ &quot;, gorjeta
#ESCREVER &quot;Total a pagar: R$ &quot;, total
#FIM
#Atenção: percentual_gorjeta é digitado como um número inteiro(por exemplo, 15 para 15%), então sua conversão precisa refletir isso.

calculo_gorjeta

valor_conta=float(input('insira o valor da compra:R$'))
percentual_gorjeta=int(input('insira o percentual da gorgeta: %'))
gorjeta= valor_conta * (percentual_gorjeta/100)
total= valor_conta + gorjeta
print(f'o valor da gorjeta foi {gorjeta}')
print(f'total a pagar: R${total}')

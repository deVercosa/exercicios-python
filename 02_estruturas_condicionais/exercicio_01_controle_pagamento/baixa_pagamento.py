print("-"*20)
cliente = input('Insira o nome ou CPF do cliente: ')
valores_em_aberto = float(input('Informe o valor da dívida: R$ '))
valor_pago = float(input('Insira o valor pago: R$ '))

if valor_pago == valores_em_aberto:
    print(f'Dívida do cliente {cliente} quitada!')

elif valor_pago > valores_em_aberto:
    troco = valor_pago - valores_em_aberto
    print(f'Dívida do cliente {cliente} quitada!')
    print(f'Troco: R$ {troco:.2f}')

else:
    restante = valores_em_aberto - valor_pago
    print(f'Pagamento realizado com sucesso')
    print(f'valor em aberto: R$ {restante:.2f}') 
   
    

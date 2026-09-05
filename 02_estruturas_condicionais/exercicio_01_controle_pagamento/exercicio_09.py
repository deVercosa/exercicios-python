FRETE E DESCONTO DE UMA LOJA ONLINE


valor_pedido = float(input('Insira o valor do pedido R$: '))
cliente = input('Cliente VIP (SIM/NAO): ')
primeira_compra = input('Primeira compra (SIM/NAO): ')

desconto = 0

if cliente == 'SIM' or primeira_compra == 'SIM':
    frete = 0.0

elif valor_pedido <= 100:
    frete = 15.0

elif valor_pedido <= 250:
    frete = 8.0

else:
    frete = 0.0

if cliente == 'SIM' and primeira_compra == 'NAO' and valor_pedido > 200:
    desconto = valor_pedido * 0.10

total = valor_pedido + frete - desconto

print('\n==== RESUMO DO PEDIDO ====')
print(f'Frete: R$ {frete:.2f}')
print(f'Desconto: R$ {desconto:.2f}')
print(f'Valor final: R$ {total:.2f}')

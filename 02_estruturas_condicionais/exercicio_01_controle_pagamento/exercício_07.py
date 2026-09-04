#Uma rede de farmácias dá 20% de desconto em compras acima de R$ 100,00. Escreva um programa que leia o valor da compra e apresente o valor final a pagar.

valor_compra = float(input('Valor da compra: '))

if valor_compra > 100:
    desconto = valor_compra * 0.20
    total = valor_compra - desconto
else:
    total = valor_compra

print(f'Total a pagar: R$ {total:.2f}')

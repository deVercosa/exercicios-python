#Uma biblioteca cobra multa por atraso na devolução de um livro: até 0 dias de atraso, sem multa; de 1 a 7 dias, R$ 1,50 por dia; acima de 7 dias, a conta do usuário é bloqueada e cobra-se uma
multa fixa de R$ 20,00.

dias_atraso = int(input("Dias de atraso: "))
if dias_atraso <= 0:
    multa = 0.00
elif dias_atraso <= 7:
    multa = dias_atraso * 1.50
else:
    multa = 20.00

print(f'multa:{multa}')

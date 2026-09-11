"""
média da turma
"""

quantidade=int(input('Quantas notas?:'))
soma=0

for i in range(quantidade):
    nota=float(input('Nota:'))
    soma= soma + nota

media= soma/quantidade

print(f'média da turma: {media:.2f}')

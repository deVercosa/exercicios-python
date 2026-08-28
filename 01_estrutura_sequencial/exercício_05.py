
#Escreva um programa que leia o salário de um funcionário e o
#percentual de bônus (por exemplo, 10 para 10%), e apresente o
#valor do bônus e o salário com o bônus somado.

#Teste com salário 3200,00 e bônus de 10%.

salario=float(input('salario: R$'))
bonus= salario / 100
print(f'o bonus mensal foi {bonus}')
print(f' o salário mensal com bônus foi {salario + bonus}')


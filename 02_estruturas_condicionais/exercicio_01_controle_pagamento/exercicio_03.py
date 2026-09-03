#Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
 
numero = int(input('Insira um número: '))

if numero > 0:
    print(f'{numero} é positivo')

elif numero < 0:
    print(f'{numero} é negativo')
    
else:
    print('O número é zero')

#Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

f = float(input('Digite a temperatura em fahrenheit: '))
c = 5 * ((f - 32) / 9)
print(f'{f} em celsius é: {c}')


Escreva um programa que leia uma temperatura em graus Celsius e
apresente o valor correspondente em Fahrenheit. A fórmula é:

   F = C * 9/5 + 32

Teste com 28 graus Celsius.

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit}°F")

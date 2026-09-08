#A academia FitPlus tem três planos com preços diferentes, e concede descontos que não se acumulam entre si — vale sempre o que tiver prioridade. O sistema calcula o valor final da mensalidade.

# Entrada de dados
idade = int(input('Insira a sua idade: '))
plano = input('Escolha um plano ("basico", "completo", "premium"): ')
cliente_estudante = input('Estudante (SIM/NAO): ')
cliente_aposentado = input('Aposentado(a) (SIM/NAO): ')

# 1. Definição do valor base do plano
if plano == 'basico':
    valor = 80
elif plano == 'completo':
    valor = 120
elif plano == 'premium':
    valor = 180
else:
    valor = 0
    print("Plano inválido.")

# 2. Aplicação das regras de desconto
desconto = 0

# Regra 1: Estudante E menos de 25 anos (50% de desconto)
if cliente_estudante == 'SIM' and idade < 25:
    desconto = 0.50
# Regra 2: 60 anos ou mais OU aposentado (30% de desconto)
elif idade >= 60 or cliente_aposentado == 'SIM':
    desconto = 0.30

# 3. Cálculo do valor final
valor_final = valor * (1 - desconto)

# Exibição do resultado
print(f"Valor final a pagar: R$ {valor_final:.2f}")

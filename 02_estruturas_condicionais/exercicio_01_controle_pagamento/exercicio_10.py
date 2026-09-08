
#O programa calcula o valor de uma corrida com base na distância percorrida, nas condições do trajeto e no tipo de passageiro.
  
distancia = float(input('A distância em KM é de: '))
horario_pico = input('Horário de pico (SIM/NAO): ')
chuva = input('Está chovendo (SIM/NAO): ')
passageiro_premium = input('Passageira PREMIUM (SIM/NAO): ')

# TARIFA

if distancia <= 2:
    tarifa = 6.00
elif distancia <= 12:
    tarifa = distancia * 2.50
else:
   tarifa = 40.00
# ADICIONAL

if horario_pico == 'SIM' or chuva == 'SIM':
    adicional = 5.00
else:
    adicional = 0.00

# DESCONTO

if passageiro_premium == 'SIM' and distancia > 10:
    desconto = (tarifa + adicional) * 0.20
else:
    desconto = 0.00

# TOTAL

total = tarifa + adicional - desconto

print(f'Tarifa: R$ {tarifa:.2f}')
print(f'Adicional: R$ {adicional:.2f}')
print(f'Desconto: R$ {desconto:.2f}')
print(f'Total: R$ {total:.2f}')



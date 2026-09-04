#Um aplicativo de streaming libera vídeo em alta definição se a velocidade da internet informada for maior ou igual a 5 Mbps; caso contrário, reproduz em qualidade padrão.
#Escreva um programa que leia a velocidade e informe a qualidade de reprodução.

velocidade_internet=int(input('informe a velocidade da internet em Mbps:'))

if velocidade_internet >=5 :
    print('Reproduzir video em alto padrão')

else:
    print('Reproduzir em qualidade padrão')

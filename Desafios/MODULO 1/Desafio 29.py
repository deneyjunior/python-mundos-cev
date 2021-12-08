print('='*10, 'Desafio 28', '='*10)
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('Você está muito rápido. Tenha cuidado.')
    reais = (velocidade - 80 ) * 10
    print('Você foi multado em R$ {}.'.format(reais))
else:
    print('Continue dirigindo assim, dentro dos padrões de segurança dessa rodovia.')
print('='*10, 'Desafio 28', '='*10)



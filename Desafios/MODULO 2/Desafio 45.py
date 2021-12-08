print('='*10, 'Desafio 45', '='*25)
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('''Sua escolha:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input('Qual sua escolha? '))
computador = randint(0,2)
print('=-='*10)
print('O computador escolheu {}.'.format(itens[computador]))
print('O jogador escolheu {}.'.format(itens[jogador]))
print('=-='*10)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:  # jogador jogou PEDRA
        print('EMPATOU')
    elif jogador == 1:  # jogador jogou PAPEL
        print('JOGADOR VENCEU')
    elif jogador == 2:  # jogador jogou TESOURA
        print('COMPUTADOR VENCEU')
    else:
        print('OPÇÃO INVÁLIDA')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:  # jogador jogou PEDRA
        print('COMPUTADOR VENCEU')
    elif jogador == 1:  # jogador jogou PAPEL
        print('EMPATOU')
    elif jogador == 2:  # jogador jogou TESOURA
        print('JOGADOR VENCEU.')
    else:
        print('OPÇÃO INVÁLIDA')
elif computador == 2:  # computador jogou TESOURA
    if jogador == 0:  # jogador jogou PEDRA
        print('JOGADOR VENCEU')
    elif jogador == 1:  # jogador jogou PAPEL
        print('COMPUTADOR VENCEU')
    elif jogador == 2:  # jogador jogou TESOURA
        print('EMPATOU')
    else:
        print('OPÇÃO INVÁLIDA')
print('='*10, 'Desafio 44', '='*25)

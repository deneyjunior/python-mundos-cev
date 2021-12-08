print('='*10, 'Desafio 54', '='*10)
from datetime import date
np = int(input('São quantas pessoas? '))
for n in range(0, np):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(n)))
    atual = date.today().year
    idade = atual - nasc
    print('Essa pessoa tem {} anos.'.format(idade))
    if nasc < atual:
        if idade >= 18:
            print('Essa pessoa é MAIOR DE IDADE.')
        else:
            print('Essa pessoa é MENOR DE IDADE.')
    else:
        print('Digite um ano válido.')
print('='*10, 'Desafio 54', '='*10)

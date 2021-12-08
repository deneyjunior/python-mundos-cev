import random
print('{}{}{}'.format('=' * 10, ' Desafio 20 ', '='*10))
lista = ['Pedro', 'Tiago Primeiro', 'João', 'André', 'Filipe', 'Bartolomeu', 'Mateus', 'Tomé', 'Tiago Segundo', 'Tadeu', 'Simão', 'Zelote', 'Judas Iscariotes']
print('Os alunos são: {}.'.format(lista))
ordem = lista
random.shuffle(ordem)
print('A ordem é: {}'.format(ordem))

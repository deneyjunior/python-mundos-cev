import random
print('{}{}{}'.format('=' * 10, ' Desafio 19 ', '='*10))
alunos = ['Pedro', 'Tiago Primeiro', 'João', 'André', 'Filipe', 'Bartolomeu', 'Mateus', 'Tomé', 'Tiago Segundo', 'Tadeu', 'Simão', 'Zelote', 'Judas Iscariotes']
escolhido = random.choice(alunos)
print('O nome escolhido foi {}.'.format(escolhido))
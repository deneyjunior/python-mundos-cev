print('='*10, 'Desafio 56', '='*10)
np = int(input('Digite a quantidade de pessoas: '))

media_idade = 0
soma_idade = 0
sexo = 0

for p in range(1, np +1):
    print('-'*10, '{} Pessoa'.format(p), '-'*10)
    nome = str(input('Nome da {}ª pessoa: '.format(p))).strip()
    idade = int(input('Idade da {}ª pessoa: '.format(p)))
    sexo = str(input('Sexo da {}ª pessoa [H/M]?'.format(p))).strip()
    if sexo in 'Hh':
        sexo =  'um homem'
    if sexo in 'Mm':
        sexo = 'uma mulher'
    print('A pessoa se chama {}, tem {} anos e é {}.'.format(nome, idade, sexo))
    soma_idade += idade 
media_idade = soma_idade / np
print('='*10, 'Desafio 56', '='*10)


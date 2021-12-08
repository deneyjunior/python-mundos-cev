import datetime
print('='*10, 'Desafio 39', '='*10)
ano_nascimento = int(input('Em qua ano você nasceu? '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade, ano_atual))
if idade < 0:
    print('Coloque um ano de nascimento válido.')
elif idade > 18:
    print('Você já deve ter se alistado no serviço milítar.')
elif idade < 18:
    print('Você ainda não precisa se alistar no serviço militar.')
elif idade == 18:
    print('É hora de se  alistar no serviço milítar.')
print('='*10, 'Desafio 39', '='*10)

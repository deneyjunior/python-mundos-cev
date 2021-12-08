import datetime
print('='*10, 'Desafio 41', '='*10)
ano_nascimento = int(input('Qual o ano em que o atleta nasceu? '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nascimento
print('O ateta tem {} anos.'.format(idade))
if idade <= 9:
    print('O atleta está na categoria MIRIM.')
elif idade > 9 and idade <= 14:
    print('O atleta está na categoria INFANTIL.')
elif idade > 14 and idade <= 19:
    print('O atleta está na categoria JÚNIOR.')
elif idade > 19 and idade <= 25:
    print('O atleta está na categoria SÊNIOR.')
elif idade > 25:
    print('O atleta está na categoria MASTER.')
print('='*10, 'Desafio 41', '='*10)

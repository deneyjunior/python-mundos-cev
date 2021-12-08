print('='*10, 'Desafio Python 23','='*50)
numero = int(input('Digite um numero:'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
d = numero // 1000 % 10
print('Analisando o numero {}.'.format(numero))
print('Unidade: {}.'.format(u))
print('Dezena: {}.'.format(d))
print('Centena: {}.'.format(c))
print('Milhar: {}.'.format(d))
print('='*10, 'Desafio Python 23','='*50)
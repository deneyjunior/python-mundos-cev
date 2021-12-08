print('='*10, 'Desafio 37', '='*10)
numero = int(input('Escreva um numero inteiro: '))
print('Base de Conversão:')
print('[ 1 ] Binário')
print('[ 2 ] Octal')
print('[ 3 ] Hexadecimal')
base = int(input('Qual será a base de conversão? '))
if base == 1:
    print('{} convertido para binário é igual a {}.'.format(numero, bin(numero)))
elif base == 2:
    print('{} convertido para octal é igual a {}.'.format(numero, oct(numero)))
elif base == 3:
    print('{} convertido para hexadecimal é igual a {}.'.format(numero, hex(numero)))
else:
    print('Opção inválida. Tente novamente.')
print('='*10, 'Desafio 36', '='*10)

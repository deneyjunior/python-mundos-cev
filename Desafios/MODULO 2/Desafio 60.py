print('='*10, 'Desafio 60', '='*10)
n = int((input('Digite um número para calcular o fatorial: ')))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end=' ')
    if c > 1:
        print(' x ',end=' ')
    else:
        print(' = ', end=' ')
    f *= c
    c -= 1
print('{}\n'.format(f))
print('='*10, 'Desafio 60', '='*10)

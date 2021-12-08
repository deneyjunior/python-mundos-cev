print('='*10, 'Desafio 52', '='*10)
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[m',end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi dividido {} vezes.'.format(num, tot))
if tot == 2:
    print('O número {} É PRIMO.'.format(num))
else:
    print('O número {} NÂO É PRIMO.'.format(num))
print('='*10, 'Desafio 67', '='*10)
while True:
    num = int(input('Você quer saber a tabuada de qual número? '))
    if num <= 0:
        break
    print('='*15)
    for n in range(1,11):
        print(f'{num} x {n} = {num * n}')
    print('='*15)
print('TABUADA ENCERRADO!')

print('='*10, 'Desafio 68', '='*10)
from random import randint
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    vitoria = 0
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper() [0]
        print(f'O jogador jogou {jogador}. O computador jogou {computador}. O total é {total}.')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCê VENCEU!')
            vitoria += 1
        else:
            print('VOCê PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print('VOCê VENCEU!')
            vitoria += 1
        else:
            print('VOCê PERDEU!')
            break
    print('Vamos jogar novamente!')
print(f'Você venceu {vitoria} vezes.')
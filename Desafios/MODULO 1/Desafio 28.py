print('='*10, 'Desafio 28', '='*18)
from random import randint
from time import sleep
A = int(input('Digite o primeiro numero do intervalo: '))
B = int(input('Digite o ultimo numero do intervalo: '))
computador = randint(A, B) # Faz o computador sortear o numero
print('='*40)
print('Vou pensar em um numero entre {} e {}. Tente adivinhar qual é.'.format(A, B))
sleep(1.5)
usuario = int(input('Digite o numero que você acha que eu pensei: '))
sleep(1)
if usuario == computador:
    print('Você acertou. Você é demais.')
else:
    print('Você errou. Eu pensei em {}. Tente novamente.'.format(computador))
print('='*10, 'Fim de Jogo', '='*17)

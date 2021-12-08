print('='*10, 'Desafio 58', '='*10)
# Bibliotecas importadas
from random import randint
from time import sleep
# Valores de entrada
A = int(input('Digite o primeiro numero do intervalo: '))
B = int(input('Digite o ultimo numero do intervalo: '))
tentativas = 0
# Faz o computador sortear o numero
computador = randint(A, B) 
print('='*40)
print('Vou pensar em um numero entre {} e {}. Tente adivinhar qual é.'.format(A, B))
usuario = int(input('Digite o numero que você acha que eu pensei: '))
while usuario != computador: 
    tentativas += 1
    if tentativas == 1:
        print('Você tentou 1 vez.')
        usuario = int(input('Você errou. Tente novamente: '))
    else: 
        print('Você tentou {} vezes.'.format(tentativas))
        usuario = int(input('Você errou. Tente novamente: '))
print('Você acertou. Você é demais.')
print('='*10, 'Fim de Jogo', '='*17)
print('='*10, 'Desafio 58', '='*10)

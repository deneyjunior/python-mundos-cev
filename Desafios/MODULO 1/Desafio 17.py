import math
print('Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e \n do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da \n hipotenusa.')
print('{}{}{}'.format('=' * 10, ' Desafio 17 ', '='*10))
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
h1 = (co ** 2 + ca ** 2) ** (1/2)
h2 = math.hypot(co, ca)
print('A hipotenusa pelo primeiro método é {}.'.format(h1))
print('A hipotenusa pelo segundo método é {}.'.format(h2))


print('{}{}{}'.format('=' * 10, ' Desafio 17 ', '='*10))



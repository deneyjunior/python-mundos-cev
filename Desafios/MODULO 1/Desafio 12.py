# Faça um algoritmo que leia o preço de um produto e mostre o novo preço com um desconto.
preco = float(input('Digite o preço atual do produto: R$ '))
desconto = float(input('Digite o valor do desconto (0.X): '))
novopreco = preco * desconto
print('O novo preço é R$ {}.'.format(novopreco))
print('='*10, 'Desafio 31', '='*20)
distancia = float(input('Qual a distância da viagem em KM? '))
print('Você esta prestes a começar uma viagem de {} Km.'.format(distancia))
if distancia <= 300:
    preco = distancia * 0.60
    print('O preço da sua passagem é R$ {}.'.format(preco))
else:
    preco = distancia * 0.80
    print('O preço da sua passagem é R$ {}.'.format(preco))
print('='*10, 'Desafio 31', '='*20)

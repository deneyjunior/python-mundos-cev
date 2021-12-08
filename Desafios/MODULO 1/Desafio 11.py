# Faça um programa que leia a altura e a largura e
# a quantidade de tinta necessaria para pinta-la,
# sabendo que um litro de tinta pinta 2m^2.
altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
area = altura * largura
print('A área da parede é {} metros.'.format(area))
litros = area / 2
print('Então você precisa de {} litros de tinta.'.format(litros))


# Faça um programa que mostre um salario e depois o novo salario com uma promoção.
salario = float(input('Digite o salário atual: R$ '))
promo = float(input('Digite o reajuste salarial (0.N ou 1.N): '))
novosalario = salario * promo
print('O novo salario é R$ {}.'.format(novosalario))
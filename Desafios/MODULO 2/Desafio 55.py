print('='*10, 'Desafio 55', '='*10)
np = int(input('São quantas pessoas? '))
maior = 0
menor = 0
idmaior = 1
idmenor = 1
for n in range(1, np + 1):
    peso = float(input('Qual é o peso da {}ª pessoa? '.format(n)))
    print('A {}ª pessoa pesa {:.1f} kg.'.format(n, peso))
    if n == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
            idmaior = n
        elif peso < menor:
            menor = peso
            idmenor = n
print('O maior peso é o da {}ª pessoa e é igual a {} kg.'.format(idmaior, maior))
print('O menor peso é o da {}ª pessoa e é igual a {} kg.'.format(idmenor, menor))
print('='*10, 'Desafio 55', '='*10)

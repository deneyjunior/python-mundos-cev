print('='*10, 'Desafio 61', '='*10)
primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
cont = 1
termo = primeiro
while cont <= 10:
    print('{} → '.format(termo), end=' ')
    termo += razão
    cont += 1
print('Fim!')
print('='*10, 'Desafio 61', '='*10)

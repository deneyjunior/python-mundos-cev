print('='*10, 'Desafio 62', '='*10)
primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end=' ')
        termo += razão
        cont += 1
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Fim!')
print('='*10, 'Desafio 62', '='*10)

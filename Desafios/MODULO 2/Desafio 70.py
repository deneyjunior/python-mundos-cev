print('='*10, 'Desafio 70', '='*10)
total = tot_mil = menor = cont = menor_preco = maior_preco = 0
barato = ' '
while True:
    nome = str(input('NOME DO PRODUTO: '))
    preco = float(input('PREÇO DO PRODUTO: R$ '))
    print('='*32)
    cont += 1
    total += preco
    if preco >= 1000:
        tot_mil += 1
    if cont == 1:
        menor_preco = preco
        barato = nome
    else:
        if preco < menor_preco:
            menor_preco = preco
            barato = nome
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper() [0]
    if resp == 'N':
        break
print('FIM!')
print(f'O total gasto foi R$ {total:.2f}.')
print(f'O produto mais barato foi {barato}.')
print('='*10, 'Desafio 64', '='*10)
resp = 'S'
media = soma = quant = maior = menor = 0
while resp in 'Sn':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = 0
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Você quer continuar? [S/N] ')).upper().strip() [0]
media = soma / quant
print('Você digitou {} números. A soma dos números é igua a {}. A média é igual a {}.'.format(quant, soma, media))    
print('O maior valor é {}. O menor valor é {}.'.format(maior, menor))
print('Fim!')
print('='*10, 'Desafio 66', '='*10)
cont = 0
soma = 0
while True:
    num = int(input('Digite um número (ou use 999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print('FIM!')
print(f'Você digitou {cont} números e a soma de todos eles é igual a {soma}.')